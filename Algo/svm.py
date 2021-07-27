from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn import metrics

cls = svm.SVC(kernel = "linear")

cls.fit(X_train,y_train)

pred = cls.predict(X_test)
