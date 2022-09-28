from flask import Flask, request, render_template
import os
from keras.models import model_from_json
from tensorflow.keras.preprocessing.image import load_img , img_to_array

app = Flask(__name__)
app.config["DEBUG"] = True


j_file = open('./model_param/model.json', 'r')
loaded_json_model = j_file.read()
j_file.close()
model = model_from_json(loaded_json_model)
model.load_weights('./model_param/model.h5')




ALLOWED_EXT = set(['jpg' , 'jpeg' , 'png' , 'jfif'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXT




def predict(filename , model):
    img = load_img(filename , target_size = (224, 224))
    img = img_to_array(img)
    img = img.reshape(1,224,224,3)

    img = img.astype('float32')
    img = img/255.0
    result = model.predict(img)
    return result





@app.route('/')
def home():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Page Not Found</p>", 404



@app.route('/result', methods=['GET' , 'POST'])
def result():
    # return render_template('test.html')
    target_img = os.path.join(os.getcwd() , 'static/images')
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('test2.html')
        elif (request.files):
            file = request.files['file']
            file.save(os.path.join(target_img , file.filename))
            img_path = os.path.join(target_img , file.filename)
            img = file.filename

            # result = predict(img_path , model)
            result = ["Sumit Jha"]
            predictions = {
                    "class1":result[0],
                    "prob1":result[0],
            }
            return  render_template('result.html', img  = img , predictions = predictions )
        else:
            return render_template('test1.html')
    else:
            return render_template('test.html')




if __name__ == '__main__':
    app.run(port=5000, debug=True)