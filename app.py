#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import flask
import pickle
from flask import Flask, render_template, request


# In[12]:


app=Flask(__name__)

@app.route('/')
#@app.route('/index')
def index():
    return render_template('index.html')


# In[13]:


def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,9)
    loaded_model = pickle.load(open("Model.pkl","rb"))
    result = loaded_model.predict(to_predict)
    return result[0]


# In[14]:


@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list=list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)
        prediction="Predicted sale is "+str(result)
        return render_template("index.html",prediction=prediction)


# In[15]:


if __name__ == "__main__":
    app.run(debug=True, port=5001)


# In[ ]:




