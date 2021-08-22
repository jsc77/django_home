from base64 import b16decode
from .utils import get_plot
from django.shortcuts import render
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from .models import *
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from datetime import datetime
import time

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

if not firebase_admin._apps:
    cred = credentials.Certificate(r"home\serviceAccountKey.json") 
    firebase_admin.initialize_app(cred)
    db = firestore.client()


df = pd.read_csv(r'info1.csv')
categorical = ['a', 'b', 'c', 'd']
x = df[categorical].values
y = df['result'].values
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2)
# gb_clf = GradientBoostingClassifier(n_estimators=20, learning_rate=1, max_features=2, max_depth=2,random_state=0)
# gb_clf.fit(x_train, y_train)
clf = KNeighborsClassifier(n_neighbors = 2).fit(x_train, y_train)

# from pushbullet import Pushbullet
# API_KEY = "o.RKpdKp7sNn4OuJGgf4dyjHmuc4JjNFPw"
# pb = Pushbullet(API_KEY)

def main_view(request):
    data = pd.read_csv(r'data.csv')
    pred = data[categorical].values
    y = clf.predict(pred)
    for i in y:
        if i == 0:
            a = "普通"
        elif i == 1:
            a = "可能性あり"
        elif i ==2:
            a = "起きる"
    # chart = get_plot(x, y)
    data = pd.read_csv(r'data2.csv')
    pred2 = data[categorical].values
    y2 = clf.predict(pred2)
    for i in y2:
        if i == 0:
            b = "普通"
        elif i == 1:
            b = "可能性あり"
        elif i ==2:
            b = "起きる"
    data = pd.read_csv(r'data3.csv')
    pred2 = data[categorical].values
    y3 = clf.predict(pred2)
    for i in y3:
        if i == 0:
            c = "普通"
        elif i == 1:
            c = "可能性あり"
        elif i ==2:
            c = "起きる"

    now = datetime.now().strftime("%m/%d %H:%M:%S")
    if a == "可能性あり":
        # push = pb.push_note('睡眠中', "１番田中さん"+now)
        db.collection('pika').document(u'user01').update({'name':'田中', 'room':"1番",'state':'留守中', 'img':'https://firebasestorage.googleapis.com/v0/b/home-321408.appspot.com/o/iconoff.png?alt=media&token=bcef3805-f307-45f1-88bc-a0e1d2270fd7', 'time':now})
    elif b == "可能性あり":
        # push = pb.push_note('睡眠中', "2番佐藤さん"+now)
        db.collection('pika').document(u'user02').update({'name':'佐藤', 'room':"2番", 'state':'留守中','img':'https://firebasestorage.googleapis.com/v0/b/home-321408.appspot.com/o/iconoff.png?alt=media&token=bcef3805-f307-45f1-88bc-a0e1d2270fd7','time':now})
    elif c == "可能性あり":
        # push = pb.push_note('睡眠中', "3番加藤さん"+now)
        db.collection('pika').document(u'user03').update({'name':'加藤', 'room':"3番", 'state':'留守中','img':'https://firebasestorage.googleapis.com/v0/b/home-321408.appspot.com/o/iconoff.png?alt=media&token=bcef3805-f307-45f1-88bc-a0e1d2270fd7','time':now})
    elif a == "起きる":
        # push = pb.push_note('確認!', "１番田中さん"+now)
        db.collection('pika').document(u'user01').update({'name':'田中', 'room':"1番", 'state':'目覚め','img':'https://firebasestorage.googleapis.com/v0/b/home-321408.appspot.com/o/getup.png?alt=media&token=70313614-3c89-4f75-80cd-1a40fcda8c3b', 'time':now})
        # db.child("data").push({'date':now,'name':"田中",'room':"1番"})
    elif b == "起きる":
        # push = pb.push_note('確認!', "2番佐藤さん"+now)
        db.collection('pika').document(u'user02').update({'name':'佐藤', 'room':"2番",'state':'目覚め', 'img':'https://firebasestorage.googleapis.com/v0/b/home-321408.appspot.com/o/getup.png?alt=media&token=70313614-3c89-4f75-80cd-1a40fcda8c3b','time':now})
    elif c == "起きる":
        # push = pb.push_note('確認!', "3番加藤さん"+now)
        db.collection('pika').document(u'user03').update({'name':'加藤', 'room':"3番", 'state':'目覚め','img':'https://firebasestorage.googleapis.com/v0/b/home-321408.appspot.com/o/getup.png?alt=media&token=70313614-3c89-4f75-80cd-1a40fcda8c3b','time':now})

    content = {'a':a,'b':b,'c':c}
    return render(request, 'main.html', content)



def simple(request):
    # import serial
    import csv
    import pandas as pd
    from random import randint

    # ser = serial.Serial('COM3', baudrate=19200)

    x_value = 0
    a = 0
    b = 0
    c = 0
    d = 0
    fieldnames = ['x_value', 'a', 'b', 'c', 'd']

    with open('data.csv', 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
    with open('data2.csv', 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
    with open('data3.csv', 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()

    while True:
        with open('data.csv', 'a', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            x_value += 1
            # getdata = str(ser.readline())
            # y = getdata[1:]
            # n1 = y.replace("\\r\\n","")
            # n2 = n1.replace("'","")
            # data = list(n2.split(','))
            # info = {
            #     "x_value": x_value,
            #     "a": data[0],
            #     "b": data[1],
            #     "c": data[2],
            #     "d": data[3],
            # }
            info = {
                "x_value": x_value,
                "a": randint(0,400),
                "b": randint(0,400),
                "c": randint(0,400),
                "d": randint(0,400)
            }
            csv_writer.writerow(info)
        with open('data2.csv', 'a', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            info2 = {
                "x_value": x_value,
                "a": randint(0,400),
                "b": randint(0,400),
                "c": randint(0,400),
                "d": randint(0,400)
            }
            csv_writer.writerow(info2)
        with open('data3.csv', 'a', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            info2 = {
                "x_value": x_value,
                "a": randint(0,400),
                "b": randint(0,400),
                "c": randint(0,400),
                "d": randint(0,400)
            }
            csv_writer.writerow(info2)
            time.sleep(2)

