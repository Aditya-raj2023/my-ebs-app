from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello My name is Aditya welcome to my AWS App!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
