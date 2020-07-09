 #import libraries 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns


def predict(arr):
    # # bank = open("C:\\Users\\sahil\\Desktop\\Minor_Project\\project\\bank-full.csv")
   
    # # Importing the dataset
    # dataset = pd.read_csv("C:\\Users\\sahil\\Desktop\\Minor_Project\\project\\bank-full.csv",delimiter=";")

    # #Count the number of rows and columns in the data set
    # dataset.shape

    # #Count the empty (NaN, NAN, na) values in each column
    # dataset.isna().sum()

    # #Visualize each column count 
    # sns.countplot(dataset['age'],label="Count")
    # sns.countplot(dataset['job'],label="Count")
    # sns.countplot(dataset['marital'],label="Count")
    # sns.countplot(dataset['education'],label="Count")
    # sns.countplot(dataset['default'],label="Count")
    # sns.countplot(dataset['housing'],label="Count")
    # sns.countplot(dataset['loan'],label="Count")
    # sns.countplot(dataset['contact'],label="Count")
    # sns.countplot(dataset['month'],label="Count")
    # sns.countplot(dataset['day_of_week'],label="Count")
    # sns.countplot(dataset['duration'],label="Count")
    # sns.countplot(dataset['campaign'],label="Count")
    # sns.countplot(dataset['pdays'],label="Count")
    # sns.countplot(dataset['previous'],label="Count")
    # sns.countplot(dataset['poutcome'],label="Count")
    # sns.countplot(dataset['emp.var.rate'],label="Count")
    # sns.countplot(dataset['cons.price.idx'],label="Count")
    # sns.countplot(dataset['cons.conf.idx'],label="Count")
    # sns.countplot(dataset['euribor3m'],label="Count")
    # sns.countplot(dataset['nr.employed'],label="Count")
    # sns.countplot(dataset['y'],label="Count")

    # #Get the correlation of the columns
    # dataset.corr()

    # #Visualize the correlation by creating a heat map.
    # plt.figure(figsize=(10,10))  
    # sns.heatmap(dataset.corr(), annot=True, fmt='.0%')
    
    #feature selection
    dataset = pd.read_csv("C:\\Users\\sahil\\Desktop\\Minor_Project\\project\\bank-full.csv",usecols=["age","job","marital","education","default","housing","loan","contact","month","day_of_week","duration","campaign","pdays","previous","poutcome","cons.conf.idx","y"],delimiter=";")

    # #Visualize the correlation by creating a heat map.
    # plt.figure(figsize=(10,10))  
    # sns.heatmap(dataset.corr(), annot=True, fmt='.0%')

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
        
    # def models(X_train,Y_train):
        
    #     #Using Logistic Regression 
    #     from sklearn.linear_model import LogisticRegression
    #     log = LogisticRegression(random_state = 0)
    #     log.fit(X_train, Y_train)
  
    #     #Using KNeighborsClassifier 
    #     from sklearn.neighbors import KNeighborsClassifier
    #     knn = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
    #     knn.fit(X_train, Y_train)
    
    #     #Using SVC linear
    #     from sklearn.svm import SVC
    #     svc_lin = SVC(kernel = 'linear', random_state = 0)
    #     svc_lin.fit(X_train, Y_train)
    
    #     #Using SVC rbf
    #     from sklearn.svm import SVC
    #     svc_rbf = SVC(kernel = 'rbf', random_state = 0)
    #     svc_rbf.fit(X_train, Y_train)

    #     #Using GaussianNB 
    #     from sklearn.naive_bayes import GaussianNB
    #     gauss = GaussianNB()
    #     gauss.fit(X_train, Y_train)

    #     #Using DecisionTreeClassifier 
    #     from sklearn.tree import DecisionTreeClassifier
    #     tree = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
    #     tree.fit(X_train, Y_train)
      
    #     #Using RandomForestClassifier method of ensemble class to use Random Forest Classification algorithm
    # from sklearn.ensemble import RandomForestClassifier
    # forest = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
    # forest.fit(X_train, Y_train)
    
    #     #print model accuracy on the training data.
    #     print('[0]Logistic Regression Training Accuracy:', log.score(X_train, Y_train))
    #     print('[1]K Nearest Neighbor Training Accuracy:', knn.score(X_train, Y_train))
    #     print('[2]Support Vector Machine (Linear Classifier) Training Accuracy:', svc_lin.score(X_train, Y_train))
    #     print('[3]Support Vector Machine (RBF Classifier) Training Accuracy:', svc_rbf.score(X_train, Y_train))
    #     print('[4]Gaussian Naive Bayes Training Accuracy:', gauss.score(X_train, Y_train))
    #     print('[5]Decision Tree Classifier Training Accuracy:', tree.score(X_train, Y_train))
    #     print('[6]Random Forest Classifier Training Accuracy:', forest.score(X_train, Y_train))
  
    #     return log, knn, svc_lin, svc_rbf, gauss, tree, forest

    # model = models(X_train,Y_train)

    # #printing confusion matrix
    # from sklearn.metrics import confusion_matrix
    # for i in range(len(model)):
    #     cm = confusion_matrix(y_test, model[i].predict(X_test))
  
    # TN = cm[0][0]
    # TP = cm[1][1]
    # FN = cm[1][0]
    # FP = cm[0][1]
  
    # print(cm)
    # print('Model[{}] Testing Accuracy = "{}!"'.format(i,  (TP + TN) / (TP + TN + FN + FP)))
    # print()
  
    # from sklearn.metrics import classification_report
    # from sklearn.metrics import accuracy_score
    
    # for i in range(len(model)):
    #     print('Model ',i)
    #     print( classification_report(y_test, model[i].predict(X_test)))
    #     print( accuracy_score(y_test, model[i].predict(X_test)))
    #     print()

    #Using RandomForestClassifier method of ensemble class to use Random Forest Classification algorithm
    from sklearn.ensemble import RandomForestClassifier
    forest = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
    forest.fit(X_train, Y_train)
    
    # arr=np.array([[20,1,1,1,1,1,1,1,1,1,100,1,999,0,1,-36.4]])
    c=forest.predict(arr)
    return c

# a=predict()
# if a == 1:
#     print("Yes")
# else:
#     print("No")