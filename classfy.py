import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing
from sklearn import utils
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score
import sys
import pickle


def train_test_split(train,test):
    X_train = train.iloc[:,1:]
    y_train = train['label']
    X_test = test.iloc[:,1:]
    y_test = test['label']

    return X_train, X_test, y_train, y_test


def classfy(train,test):
    df_train = pd.read_csv(train)
    df_test = pd.read_csv(test)
    X_train, X_test, y_train, y_test = train_test_split(df_train,df_test)
    neigh = KNeighborsClassifier(n_neighbors=3)
    neigh.fit(X_train,y_train)
    y_predknn = neigh.predict(X_test)
    print('accuracy_score',accuracy_score(y_test, y_predknn))
    print('r2_score', r2_score(y_test, y_predknn))
    print('mean_squared_error', mean_squared_error(y_test, y_predknn))

    with open('save/neigh.pickle', 'wb+') as f:
        pickle.dump(neigh, f)

if __name__ == '__main__':
    classfy(sys.argv[1],sys.argv[2])
