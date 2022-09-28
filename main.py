import re
from flask import Flask, request, render_template
import os
# from keras.models import model_from_json
# from tensorflow.keras.preprocessing.image import load_img , img_to_array
import json
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import model_from_json
import numpy as np
import tensorflow.keras.models as models
from numpyencoder import NumpyEncoder


app = Flask(__name__)
app.config["DEBUG"] = True


diseases=[
    'Acne and Rosacea Photos', 
    'Cellulitis Impetigo and other Bacterial Infections', 
    'Eczema Photos', 
    'Light Diseases and Disorders of Pigmentation', 
    'Lupus and other Connective Tissue diseases', 
    'Psoriasis pictures Lichen Planus and related diseases', 
    'Scabies Lyme Disease and other Infestations and Bites', 
    'Seborrheic Keratoses and other Benign Tumors'
]

# j_file = open('./model_param/model.json', 'r')
# loaded_json_model = j_file.read()
# j_file.close()
# model = model_from_json(loaded_json_model)
# model.load_weights('./model_param/model.h5')
with open('model_param/model.json','r') as json_file:
    json_model = json_file.read()
model = model_from_json(json_model)
model.load_weights('model_param/model.h5')



ALLOWED_EXT = set(['jpg' , 'jpeg' , 'png' , 'jfif'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXT




def predict(filename , model):
    # img = load_img(filename , target_size = (224, 224))
    # img = img_to_array(img)
    # img = img.reshape(1,224,224,3)

    # img = img.astype('float32')
    # img = img/255.0
    # result = model.predict(img)

    test_image = image.load_img(filename, target_size = (100,100))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = model.predict(test_image)
    d = np.argmax(result)
    return d





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

            result = predict(img_path , model)

            r={'5': int(result)}
            print(r)
            diagnosis = json.dumps(r)
            predictions = {
                    "class1":diseases[int(diagnosis[6])],
                    "prob1":"Sumit",
            }
            return  render_template('result.html', img  = img , predictions = predictions )
        else:
            return render_template('test1.html')
    else:
            return render_template('test.html')




if __name__ == '__main__':
    app.run(port=5000, debug=True)