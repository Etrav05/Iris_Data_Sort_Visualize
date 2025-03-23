from sklearn import datasets

iris = datasets.load_iris()

feature_data = iris.data
label = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

def testFunctionCalls():
    print("Feature Data: ")  # Flower measurements:
    print(feature_data[:5])                 # (sepal length, sepal width, petal length, petal width)

    print("Target Label: ") # Species labels:
    print(label[:5])                 # (0 = setosa, 1 = versicolor, 2 = virginica)

    print("Feature name: ", feature_names)

    print("Target name: ", target_names)

# -------------------------------------------------------------------------------------------------------------------- #

def printSpeciesData(feature_data, label, target_names): # pass these parameters so we can work with copys
    print("#. Species, feature data")

    n = len(feature_data)
    for x in range(n):
        if label[x] == 0:
            print(x + 1, "-", feature_data[x][0], "cm",target_names[0]) # print based on species name

        elif label[x] == 1:
            print(x + 1, "-", feature_data[x][0], "cm", target_names[1])

        else:
            print(x + 1, "-", feature_data[x][0], "cm", target_names[2])

def swap(feature_data, label, x, min_idx):
    (feature_data[x][0], feature_data[min_idx][0]) = (feature_data[min_idx][0], feature_data[x][0])
    (label[x], label[min_idx]) = (label[min_idx], label[x])

def selectionSort(feature_data, label):
    n = len(feature_data)
    for x in range(n):
        min_idx = x

        for y in range(x + 1, n):
            if (feature_data[y][0] < feature_data[min_idx][0]): # sort by first feature (sepal length)
                min_idx = y # change min to this new index

        swap(feature_data, label, x, min_idx)

def printMinMax_SLen(feature_data):
    n = len(feature_data)
    print("min", feature_data[1][0], "---->", feature_data[n - 1][0], "max")

feature_data_copy = feature_data.copy() # create personal copy of data sets
label_copy = label.copy()

# main
selectionSort(feature_data_copy, label_copy)

printSpeciesData(feature_data_copy, label_copy, target_names)

printMinMax_SLen(feature_data_copy)