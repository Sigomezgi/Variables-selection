import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from matplotlib import pyplot as plt


def selecting_variables_random_forest (X_train: pd.DataFrame, y_train : pd.DataFrame,estimartors: int = 100):



    rf = RandomForestClassifier(n_estimators=estimartors)
    rf.fit(X_train, y_train)

    feats = {} # a dict to hold feature_name: feature_importance
    for feature, importance in zip(X_train.columns, rf.feature_importances_):
        feats[feature] = importance #add the name/value pair 

    importances = pd.DataFrame.from_dict(feats, orient='index').rename(columns={0: 'Gini-importance'})
    importances = importances.sort_values(by='Gini-importance')
    
    plt.figure(figsize=(10,20))
    plt.barh(importances.index, importances['Gini-importance'])
    plt.xlabel("Feature Importance")
    importances = importances.sort_values(by='Gini-importance', ascending = False)

    #importances.plot(kind='bar', rot=45)

    return importances
