from flask import Flask,render_template



app = Flask(__name__)

app.config["DEBUG"] = True

@app.route('/')
def home():
    return render_template('template/index.html')


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Page Not Found</p>", 404

if __name__ == '__main__':
    app.run(port=5000, debug=True)
