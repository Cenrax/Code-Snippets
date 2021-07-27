#classification algorithm mainly used for continious values

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

gnb = GaussainNB()

#Load the Dataset

X,y = <load data>

X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.5, random_state=0)
y_pred = gnb.fit(X_train, y_train).predict(X_test)
