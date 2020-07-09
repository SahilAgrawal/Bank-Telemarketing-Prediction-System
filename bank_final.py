 #import libraries 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns


def predict(arr):
    
    
    #feature selection
    dataset = pd.read_csv("C:\\Users\\sahil\\Desktop\\Minor_Project\\project\\bank-full.csv",usecols=["age","job","marital","education","default","housing","loan","contact","month","day_of_week","duration","campaign","pdays","previous","poutcome","cons.conf.idx","y"],delimiter=";")
    
    #splitting the dataset
    X = dataset.iloc[:, :-1].values
    Y = dataset.iloc[:, 16].values
    
    #categorising data
    from sklearn.preprocessing import LabelEncoder
    labelencoder_X=LabelEncoder()
    X[:, 1]=labelencoder_X.fit_transform(X[:, 1])
    X[:, 2]=labelencoder_X.fit_transform(X[:, 2])
    X[:, 3]=labelencoder_X.fit_transform(X[:, 3])
    X[:, 4]=labelencoder_X.fit_transform(X[:, 4])
    X[:, 5]=labelencoder_X.fit_transform(X[:, 5])
    X[:, 6]=labelencoder_X.fit_transform(X[:, 6])
    X[:, 7]=labelencoder_X.fit_transform(X[:, 7])
    X[:, 8]=labelencoder_X.fit_transform(X[:, 8])
    X[:, 9]=labelencoder_X.fit_transform(X[:, 9])
    X[:, 14]=labelencoder_X.fit_transform(X[:, 14])
    labelencoder_Y=LabelEncoder()
    Y=labelencoder_Y.fit_transform(Y)


    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, Y_train, y_test = train_test_split(X, Y, test_size = 0.20, random_state = 0)
    # X_train, X_test, Y_train = train_test_split(X, Y, test_size = 0.20, random_state = 0)

    #feature scaling
    
    from sklearn.preprocessing import StandardScaler
    sc=StandardScaler()
    X_train=sc.fit_transform(X_train)
    X_test=sc.fit_transform(X_test)
        

    #Using RandomForestClassifier method of ensemble class to use Random Forest Classification algorithm
    from sklearn.ensemble import RandomForestClassifier
    forest = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
    forest.fit(X_train, Y_train)
    
    # arr=np.array([[20,1,1,1,1,1,1,1,1,1,100,1,999,0,1,-36.4]])
    c=forest.predict(arr)
    return c

