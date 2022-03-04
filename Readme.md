# Image compression to WebP format

With this script you can convert any images for your project to the popular [WebP image format](https://developers.google.com/speed/webp).

WebP is a modern image format that provides superior lossless and lossy compression for images on the web. Using WebP, webmasters and web developers can create smaller, richer images that make the web faster.

WebP lossless images are 26% smaller in size compared to PNGs. WebP lossy images are 25-34% smaller than comparable JPEG images at equivalent SSIM quality index.


### Requirements
1. Python 3 and higher
2. [pip](https://pypi.python.org/pypi/pip/1.0.2) - tool for installing and managing Python packages
3. [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) (not required) - tool to keep the dependencies required by different projects in separate places
 
### Installation
1. Create virtual environment in your project folder
2. Install required libraries and packages
   <code>pip3 install -r requirements.txt</code>
3. Run code:
   <code>python compress.py</code>
4. Enter full path to the folder with your images. You can use `pwd` for more information - (example: /Users/svetlanamargetova/Desktop/web-app/images/).
5. Enter desired compression quality in number format from 1 to 100. Default value is 80 otherwise.

### Error messages
1. ValueError - compression quality not is not a number. 
2. FileNotFoundError - bad path to the image folder or value was not provided.

