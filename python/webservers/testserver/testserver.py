from flask import Flask
app = Flask(__name__,static_url_path='/static')

@app.route("/")
def index():
    return "<html><body><h1>MyPhotos</h1><img src=\"static\image.jpg\"></body></html>"
 
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)