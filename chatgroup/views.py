from django.shortcuts import render
from joblib import load
from sklearn.datasets import fetch_20newsgroups

data = fetch_20newsgroups()
categories = ['sci.electronics', 'rec.sport.baseball', 'rec.autos', 'rec.motorcycles']
train = fetch_20newsgroups(subset='train', categories=categories)

# Create your views here.
def index(req):
    model = load('./chatgroup/static/chatgroup.model')
    label = ""
    chat  = ""
    Percent = load('chatgroup\static\Percent.csv')
    if label == "":
        label = "-"
    if req.method == 'POST':
        print("POST IN")
        chat = str(req.POST['chat'])
        print(chat)
        pred = model.predict([chat])
        label = train.target_names[pred[0]]
    return render(req, 'chatgroup/index.html' ,{
            'label':label,
            'Percent':Percent,
    })