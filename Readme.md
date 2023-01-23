# Image compression to WebP format

With this script you can convert any images for your project to the popular [WebP image format](https://developers.google.com/speed/webp).

WebP is a modern image format that provides superior lossless and lossy compression for images on the web. Using WebP, webmasters and web developers can create smaller, richer images that make the web faster.

WebP lossless images are 26% smaller in size compared to PNGs. WebP lossy images are 25-34% smaller than comparable JPEG images at equivalent SSIM quality index.

Use only ```compress.py``` script. 

<hr>

## S3 upload ## 
Amazon S3 is part of my custom ugly quick one hour code, but If you really want to implement upload to S3 butckets, you:

need define also content type and correct rights

```python
  ExtraArgs={'ACL': 'public-read', 'ContentType': 'image/webp'})
```

and at least these envs

```
API_ACCESS_ID = config('ACCESS_ID')
API_SECRET_KEY = config('SECRET_KEY')
AWS_ENDPOINT = config('AWS_ENDPOINT')
AWS_CDN = config('AWS_CDN')
FULL_URL = config('FULL_URL')
```
