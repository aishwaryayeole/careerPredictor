import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from scipy.sparse import csr_matrix
from sklearn.preprocessing import LabelEncoder


def dataset_statistics(dataset):
    print(dataset.describe())

def split_dataset(dataset, train_percentage, feature_headers, target_header):
    train_x, test_x, train_y, test_y = train_test_split(dataset[feature_headers], dataset[target_header], train_size=train_percentage)
    return train_x, test_x, train_y, test_y

def random_forest_classifier(features, target):
    clf = RandomForestClassifier()
    clf.fit(features, target)
    return clf

def dynamic_prediction(data,name):
    print("data: ",data)
    row = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    col = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    dataArray = np.array(data)
    matrix = csr_matrix((dataArray, (row, col)), shape=(1, 12)).toarray()
    print("Before prediction")
    PredictionVal = trained_model.predict(matrix)
    if PredictionVal == 1:
        return "Congratulations! ",name, ", Your predicted grade is A "
    else:
        return name,", Your predicted grade is B "

def main():
    global trained_model
    dataFile = "dataset\Student_performance.csv"
    HEADERS = ["Pstatus","studytime","failures","schoolsup","famsup","activities","nursery","internet","absences","higher","G1","G2","G3"]

    dataset = pd.read_csv(dataFile, sep=',')

    train_x, test_x, train_y, test_y = split_dataset(dataset, 0.8, HEADERS[:-1], HEADERS[-1])
    trained_model = random_forest_classifier(train_x, train_y)
    Testpredictions = trained_model.predict(test_x)

    for i in range(0, 70):
        print("Actual outcome :: {} and Predicted outcome :: {}".format(list(test_y)[i], Testpredictions[i]))

    # Train and Test Accuracy
    print("Train Accuracy :: ", accuracy_score(train_y, trained_model.predict(train_x)))
    print("Test Accuracy  :: ", accuracy_score(test_y, Testpredictions))

if __name__ == "__main__":
    main()