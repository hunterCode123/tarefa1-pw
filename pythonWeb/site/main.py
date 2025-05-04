from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
	return "<h1> Site feito com python estus flasks</h1>"

@app.route('/outrapag')
def outpag():
	return "<h1> Outra pag saborosa</h1>"

if __name__=="__main__":
	app.run(host='0.0.0.0', port=5000)