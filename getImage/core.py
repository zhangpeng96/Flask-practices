from flask import Response, Flask
from PIL import Image
import io

app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Hello World! <br/>"
  
@app.route("/user/<name>")
def user(name):
    return "<h1>Hello,%s</h1>"%name

@app.route("/image-file")
def image1():
    with open("card.jpg", 'rb') as f:
        image = f.read()

    resp = Response(image, mimetype="image/jpeg")
    return resp

@app.route("/image-pil")
def image2():
    pic = Image.open("card.jpg")
    imgByteArr = io.BytesIO()
    pic.save(imgByteArr, format='jpeg')
    imgByteArr = imgByteArr.getvalue()

    resp = Response(imgByteArr, mimetype="image/jpeg")
    return resp


if __name__ == "__main__":
    app.run(debug=True)