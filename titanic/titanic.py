"""Titanic - Machine Learning from Disaster.

My first project in Data Science. Yay!
"""
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier as rfc
import os

data = {
    'train_data': pd.read_csv("/kaggle/input/titanic/train.csv"),
    'test_data': pd.read_csv("/kaggle/input/titanic/test.csv"),
    'gender_data': pd.read_csv("/kaggle/input/titanic/gender_submission.csv")
}

def display_tree():
    """Output the current working path."""
    for dirname, _, filenames in os.walk('/kaggle/input'):
        for filename in filenames:
            print(os.path.join(dirname, filename))


def display_data():
    """Output the data contained in file."""
    for k in data:
        data[k].head()


def display_stats_by_gender(gender, status):
    """Output the statistics for the women in the sinking ship."""
    if gender == 'male' or gender == 'female':
        survivors = data["train_data"].loc[data["train_data"].Sex == gender][status]
        survival_rate = sum(survivors) / len(survivors)
        print(f"[INFO] % of {gender}s that {status}: {survival_rate * 100}")

def generate_forest():
    """Create a random forest model."""
    train_y = data["train_data"]['Survived']
    features = ['Pclass', 'Sex', "SibSp", "Parch"]
    train_x = pd.get_dummies(data['train_data'][features])
    test_x = pd.get_dummies(data['test_data'][features])
    model = rfc(n_estimators=100, max_depth=5, random_state=1)
    model.fit(train_x, train_y)
    predictions = model.predict(test_x)
    
    output = pd.DataFrame({
        'PassengerId': data['test_data'].PassengerId,
        'Survived': predictions
    })
    output.to_csv('submission.csv', index=False)
    print("[INFO] Your submission was successfully saved!")
    
if __name__ == "__main__":
    generate_forest()
    submission = pd.read_csv("/kaggle/working/submission.csv")
    submission.head()
