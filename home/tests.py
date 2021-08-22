# import pandas as pd
# import pandas_datareader as web
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score
# from sklearn.pipeline import Pipeline
# from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import classification_report
# from sklearn.preprocessing import MinMaxScaler
# import csv
# import io
# import datetime as dt
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, Dropout, LSTM

# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore

# cred = credentials.Certificate(r"C:\Users\joho10\Desktop\django\django2\hq\home\serviceAccountKey.json")
# firebase_admin.initialize_app(cred)
# db = firestore.client()

# data = {'name':'John', 'age':40, 'employed':True}
# db.collection('people').add(data)

# df = pd.read_csv(r"C:\Users\joho10\Desktop\django\django2\hq\Iris.csv")
# df['SepalLengthCm'].hist()
# plt.figure()
# x = data.drop("Category", axis=1)
# y = data["Category"]
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.15)
# model = LogisticRegression()
# model.fit(x_train, y_train)
# predictions = model.predict(x_test)
# accuracy = accuracy_score(predictions, y_test)
# print(accuracy)
# correlation =data.corr()
# sns.set(font='MS Gothic')
# sns.heatmap(correlation)
# plt.savefig("heatmap_list.png")
# plt.close("all")