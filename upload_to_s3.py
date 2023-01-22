from boto3 import session
from botocore.client import Config
from decouple import config
from dotenv import load_dotenv
import os
import pandas as pd
from datetime import datetime
from collections import ChainMap
import re

load_dotenv()

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


now = datetime.now()
dt_string = now.strftime("%Y-%m-%d %H:%M:%S")


API_ACCESS_ID = config('ACCESS_ID')
API_SECRET_KEY = config('SECRET_KEY')
AWS_ENDPOINT = config('AWS_ENDPOINT')
AWS_CDN = config('AWS_CDN')
FULL_URL = config('FULL_URL')

session = session.Session()

client = session.client('s3',
                        endpoint_url=AWS_ENDPOINT,
                        aws_access_key_id=API_ACCESS_ID,
                        aws_secret_access_key=API_SECRET_KEY)


users = pd.read_csv('csv/users.csv')
products = pd.read_csv('csv/products.csv')
localities = pd.read_csv('out/localities.csv')
usersDf = users[['Profile picture', 'Photo name', 'Username']]


def new_photo_name(value):
    return str(value[1])[-4:] + str(value[2]).replace(".", "").replace(" ", "").lower()


def rename_image(name, ext='webp'):
    if 'region' not in name or 'product' not in name:
        for index, data in users.iterrows():
            if users['Photo name'].iloc[index] == str(name):
                return [users['new_name'].iloc[index], ext]

    return [name, ext]


for index, image in enumerate(os.listdir("users")):
    name, ext = os.path.splitext(image)
    new_image = rename_image(name, ext)
    for i, j in enumerate(usersDf['Photo name']):
        if str(name) in str(j).lower():
            if usersDf['Profile picture'].iloc[i] == 'ANO':
                if new_image is not None:
                    client.upload_file(
                        'users/'+image, AWS_CDN, new_image[0]+new_image[1],
                        ExtraArgs={'ACL': 'public-read',
                                   'ContentType': 'image/webp'}
                    )


for index, image in enumerate(os.listdir("images")):
    name, ext = os.path.splitext(image)
    new_image = rename_image(name, ext)
    if new_image is not None:
        client.upload_file(
            'images/'+image, AWS_CDN, new_image[0]+new_image[1],
            ExtraArgs={'ACL': 'public-read', 'ContentType': 'image/webp'}
        )

columns = ['id', 'createdDate', 'updatedDate', 'url', 'localityId', 'productId', 'storyId',
           'mime', 'order', 'creatorId', 'statusId', 'blogPostSectionId']

df = pd.DataFrame(columns=columns)
empty = []


def get(path):
    for _, file in enumerate(os.listdir(path)):
        name, _ = os.path.splitext(file)
        if path == 'users':
            for i, j in enumerate(usersDf['Photo name']):
                if str(name) in str(j).lower():
                    if usersDf['Profile picture'].iloc[i] == 'ANO':
                        empty.append(name)
        else:
            empty.append(name)


get("users")
get("images")


df = pd.DataFrame(data=empty)
df = pd.concat([df, pd.DataFrame(columns=columns)])
df.rename(columns={0: 'name'}, inplace=True)


def set_url(value):
    return FULL_URL + value + '.webp'
