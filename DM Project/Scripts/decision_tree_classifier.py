import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
import os

# File path
csv_file = "C:/Users/mhamz/PycharmProjects/DM project/DM Project/Training Data/Model Train Data Bef Final.csv"

# Check if the file exists
if os.path.exists(csv_file):
    # Read the cleaned CSV file
    df = pd.read_csv(csv_file)

    # Calculate weighted scores for assignments and quizzes
    # for i in range(1, 5):  # Assuming there are 4 assignments and quizzes
    #     df[f'As:{i}'] *= 3  # Assignments weighted by 3
    #     df[f'Qz:{i}'] *= 2  # Quizzes weighted by 2
    #
    # # S1 weighted by 15
    # df['S-I'] *= 15


    df[f'AS']*=15
    df[f'QZ'] *= 10
    df[f'S1'] *= 15
    df[f'S2'] *= 15


    # Split the data into features (X) and target variable (y)
    X = df.drop(columns=['Grade'])  # Features
    y = df['Grade']  # Target variable

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the DecisionTreeClassifier
    clf = DecisionTreeClassifier(random_state=42)

    # Train the classifier
    clf.fit(X_train, y_train)

    # Make predictions
    y_pred = clf.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    precision, recall, f1, _ = precision_recall_fscore_support(y_test, y_pred, average=None)

    print("Accuracy:", accuracy)
    print("Precision per class:", precision)
    print("Recall per class:", recall)
    print("F1 Score per class:", f1)

    # Assuming you have a new data point represented as a dictionary
    #new_data = {'As:1': 29, 'As:2': 90, 'As:3': 120, 'As:4': 80, 'Qz:1': 7.5, 'Qz:2': 4.5, 'Qz:3': 5, 'Qz:4': 3, 'S-I': 9.7}
    new_data = {'AS': 0.001,'QZ': 0.001, 'S1': 0.001, 'S2': 0.001}

    # for i in range(1, 5):  # Assuming there are 4 assignments and quizzes
    #     new_data[f'As:{i}'] *= 3  # Assignments weighted by 3
    #     new_data[f'Qz:{i}'] *= 2  # Quizzes weighted by 2
    # new_data['S-I'] *= 15  # S1 weighted by 15

    df[f'AS']*=15
    df[f'QZ'] *= 10
    df[f'S1'] *= 15
    df[f'S2'] *= 15


    new_df = pd.DataFrame([new_data])
    predicted_grade = clf.predict(new_df)

    print("Predicted Grade of New Entry:", predicted_grade)
else:
    print(f"The file '{csv_file}' does not exist.")
