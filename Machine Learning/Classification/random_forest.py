import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt

from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier

#%%

data = pd.read_csv('heart.csv')
X = data.drop('target', axis=1).values
y = data.target.values

split_sizes = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4]
estimators = [50, 60, 70, 80, 90, 100]

results_bayesian = []
results_index_gini = []
results_entropy = []

results_bagging = []
results_RF = []


for size in split_sizes:
    X_train, X_test, y_train, y_test = train_test_split( X, y, 
                                            test_size=size, random_state=42)
    
    # bayesian
    clf_bayesian = GaussianNB()
    clf_bayesian.fit(X_train, y_train)
    y_pred = clf_bayesian.predict(X_test)
    
    results_bayesian.append([
        accuracy_score(y_test, y_pred),
        precision_score(y_test, y_pred),
        recall_score(y_test, y_pred),
        f1_score(y_test, y_pred)
    ])
    
    # decision tree (gini)
    clf_index_gini = DecisionTreeClassifier(criterion='gini',random_state=42)
    clf_index_gini.fit(X_train, y_train)
    y_pred = clf_index_gini.predict(X_test)
    
    results_index_gini.append([
        accuracy_score(y_test, y_pred),
        precision_score(y_test, y_pred),
        recall_score(y_test, y_pred),
        f1_score(y_test, y_pred)
    ])
    
    # decision tree (entropy)
    clf_entropy = DecisionTreeClassifier(criterion='entropy',random_state=42)
    clf_entropy.fit(X_train, y_train)
    y_pred = clf_entropy.predict(X_test)
    
    results_entropy.append([
        accuracy_score(y_test, y_pred),
        precision_score(y_test, y_pred),
        recall_score(y_test, y_pred),
        f1_score(y_test, y_pred)
    ])
     
    
 
    
X_train, X_test, y_train, y_test = train_test_split( X, y, 
                                            test_size=0.2, random_state=42)

for num_e in estimators:
    
    # bagging(bayesian)
    clf_bagging = BaggingClassifier( GaussianNB(), n_estimators=num_e, 
                                                            random_state=42)
    clf_bagging.fit(X_train, y_train)
    y_pred = clf_bagging.predict(X_test)
    
    results_bagging.append([
        accuracy_score(y_test, y_pred),
        precision_score(y_test, y_pred),
        recall_score(y_test, y_pred),
        f1_score(y_test, y_pred)
    ])
    
    
    # Random Forest
    clf_RF = RandomForestClassifier(n_estimators=num_e, random_state=42)
    clf_RF.fit(X_train, y_train)
    y_pred = clf_RF.predict(X_test)
    
    results_RF.append([
        accuracy_score(y_test, y_pred),
        precision_score(y_test, y_pred),
        recall_score(y_test, y_pred),
        f1_score(y_test, y_pred)
    ])
    



#%%

x_axis=estimators.copy()
x_axis.append(110)


parameters=[
    (0,"accuracy"), 
    (1,"precision"), 
    (2,"recall"), 
    (3,"f-score"), 
]

for i, metric in parameters:

    plt.plot(x_axis, [x[i] for x in results_bayesian], 
             color='green', lw=2, linestyle=":", label='bayesian')
    plt.plot(x_axis, [x[i] for x in results_index_gini], 
             color='red', lw=2, label='DT (index gini)')
    plt.plot(x_axis, [x[i] for x in results_entropy], 
             color='orange', lw=2, linestyle='dashed', label='DT (entropy)')
    
    plt.plot(estimators, [x[i] for x in results_bagging], 
             color='blue', lw=2, linestyle='dashdot', label='bagging')
    plt.plot(estimators, [x[i] for x in results_RF], 
             color='black', lw=2, linestyle='solid', label='random forest')
    
    #plt.xlabel('Test split size (%)')
    plt.ylabel(metric)
    #plt.title('Impact of test split size')
    plt.legend()
    fig = plt.gcf()
    fig.set_size_inches(8,6)
    plt.savefig(metric+'.png')
    plt.close()

