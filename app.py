from flask import Flask, render_template, request, url_for, Markup, jsonify
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from werkzeug.utils import secure_filename
import pickle
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
 
app = Flask(__name__) #Initialize the flask App

rap = pickle.load(open('kmean.pkl','rb'))

regresso = pickle.load(open('murder.pkl','rb'))

sandy = pickle.load(open('theft.pkl','rb'))
raps = pickle.load(open('rap.pkl','rb'))
lasts = pickle.load(open('total.pkl','rb'))
scaler = MinMaxScaler()
#scaler = MinMaxScaler()
#scaler = MinMaxScaler()

 
@app.route('/')
@app.route('/first')
def first():
    return render_template('first.html')
   
    
 
    
    
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/chart')
def chart():
    return render_template('chart.html')

@app.route('/murder')
def murder():
    return render_template('murder.html')
@app.route('/theft')
def theft():
    return render_template('theft.html')
@app.route('/rape')
def rape():
    return render_template('rape.html')        
@app.route('/upload')
def upload():
    return render_template('upload.html')  
@app.route('/preview',methods=["POST"])
def preview():
    if request.method == 'POST':
        dataset = request.files['datasetfile']
        df = pd.read_csv(dataset,encoding = 'unicode_escape')
        df.set_index('Id', inplace=True)
        return render_template("preview.html",df_view = df) 

 
 
@app.route('/prediction')
def prediction():
 	return render_template("prediction.html")
    
@app.route('/predict',methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    #final_features = pca.transform(final_features)    
    y_pred = rap.predict(final_features)
    if y_pred[0] == 1:         
        label="High rate crime area"
    elif y_pred[0] == 0:
        label="Low rate crime area"
    return render_template('prediction.html', prediction_text= label)

 

@app.route('/crime')
def crime():
 	return render_template("crime.html")
    
@app.route('/predicts',methods=['POST'])
def predicts():
	int_feature = [x for x in request.form.values()]
	 
	final_features = [np.array(int_feature)]
	 
	prediction=regresso.predict(final_features)
	pred=format(int(prediction[0]))
	
	return render_template('crime.html', prediction_text= pred)    	 

@app.route('/total')
def total():
 	return render_template("total.html")
    
@app.route('/prediction',methods=['POST'])
def totals():
	int_feature = [x for x in request.form.values()]
	 
	final_features = [np.array(int_feature)]
	 
	prediction=lasts.predict(final_features)
	pred=format(int(prediction[0]))
	
	return render_template('total.html', prediction_text= pred)
    
@app.route('/crimes')
def crimes():
 	return render_template("crimes.html")
    
@app.route('/predictions',methods=['POST'])
def predictions():
	int_feature = [x for x in request.form.values()]
	 
	final_features = [np.array(int_feature)]
	 
	prediction=raps.predict(final_features)
	pred=format(int(prediction[0]))
	
	return render_template('crimes.html', prediction_text= pred)  
@app.route('/last')
def last():
 	return render_template("last.html")
    
@app.route('/data',methods=['POST'])
def data():
	int_feature = [x for x in request.form.values()]
	 
	final_features = [np.array(int_feature)]
	 
	prediction=sandy.predict(final_features)
	pred=format(int(prediction[0]))
	
	return render_template('last.html', prediction_text= pred)    
#@app.route('/chart')
#def chart():
	#abc = request.args.get('news')	
	#input_data = [abc.rstrip()]
	# transforming input
	#tfidf_test = tfidf_vectorizer.transform(input_data)
	# predicting the input
	#y_pred = pac.predict(tfidf_test)
    #output=y_pred[0]
	#return render_template('chart.html', prediction_text='Review is {}'.format(y_pred[0])) 

 

if __name__=='__main__':
    app.run(debug=True)
