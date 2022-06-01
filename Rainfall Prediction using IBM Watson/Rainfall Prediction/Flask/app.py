import numpy as np
import pickle
import pandas
import os
from flask import Flask, request, render_template


app = Flask(__name__,template_folder='template')

model = pickle.load(open('rainfall.pkl', 'rb'))
scale = pickle.load(open('scale.pkl','rb'))
label = pickle.load(open('encoder.pkl','rb'))

@app.route('/')# route to display the home page
def home():
    return render_template('index.html') #rendering the home page

@app.route('/predict',methods=['post','get'])# route to show the predictions in a web UI
def predict():
    #  reading the inputs given by the user
    input_feature=[x for x in request.form.values()] 
    input_feature[0]=float(label[input_feature[0]])
    input_feature[1]=float(input_feature[1])
    input_feature[2]=float(input_feature[2])
    input_feature[3]=float(input_feature[3])
    input_feature[4]=float(label[input_feature[4]])
    input_feature[5]=float(input_feature[5])
    input_feature[6]=float(label[input_feature[6]])
    input_feature[7]=float(label[input_feature[7]])
    input_feature[8]=float(input_feature[8])
    input_feature[9]=float(input_feature[9])
    input_feature[10]=float(input_feature[10])
    input_feature[11]=float(input_feature[11])
    input_feature[12]=float(input_feature[12])
    input_feature[13]=float(input_feature[13])
    input_feature[14]=float(input_feature[14])
    input_feature[15]=float(input_feature[15])
    input_feature[16]=float(input_feature[16])
    input_feature[17]=float(input_feature[17])
    input_feature[18]=float(input_feature[18])
    input_feature[19]=float(input_feature[19])
    input_feature[20]=float(input_feature[20])
    input_feature[21]=float(label[input_feature[21]])
    print(input_feature)
    features_values=[np.array(input_feature)]
    names = [['Location', 'MinTemp', 'MaxTemp', 'Rainfall', 
       'WindGustDir', 'WindGustSpeed', 'WindDir9am', 'WindDir3pm',
       'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm',
       'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm', 'Temp9am',
       'Temp3pm', 'year', 'month', 'date', 'RainToday']]
    data = pandas.DataFrame(features_values,columns=names)
     # predictions using the loaded model file
    prediction=model.predict(data)
    print(prediction)
    if prediction == 1:
        return render_template("chance.html")
    else:
        return render_template("nochance.html")
     # showing the prediction results in a UI
if __name__=="__main__":
    
    app.run(host='0.0.0.0', port=8000,debug=True)    # running the app
    port=int(os.environ.get('PORT',5000))
    app.run(port=port,debug=True,use_reloader=False)