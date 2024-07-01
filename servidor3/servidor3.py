from flask import Flask
servidor3 = Flask(__name__)
@servidor3.route('/')
def hola():
    return "Hola mi gente"
if __name__ == '__main__':
    servidor3.run(host='0.0.0.0')