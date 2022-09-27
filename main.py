
from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

app.config["DEBUG"] = True



ALLOWED_EXT = set(['jpg' , 'jpeg' , 'png' , 'jfif'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXT




@app.route('/')
def home():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Page Not Found</p>", 404



@app.route('/result', methods=['GET' , 'POST'])
def result():
    error = '1'
    # target_img = os.path.join(os.getcwd() , 'static/images')
    if request.method == 'POST':
        if (request.files):
            # file = request.files['file']
            # if file and allowed_file(file.filename):
            #     file.save(os.path.join(target_img , file.filename))
            # else:
            #     error = "Please upload images of jpg , jpeg and png extension only"

            if(len(error) == 1):
                return  render_template('result.html' )
            else:
                return render_template('index.html' , error = error)

    else:
        return render_template('index.html')



if __name__ == '__main__':
    app.run(port=5000, debug=True)