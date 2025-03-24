from sklearn import datasets

iris = datasets.load_iris()

feature_data = iris.data
label = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

# -------------------------------------------------------------------------------------------------------------------- #
# todo: Figure out how to start visualizing data
# todo: Create Radix sort function (not sure how hard this is lol)
# -------------------------------------------------------------------------------------------------------------------- #

def testFunctionCalls():
    print("Feature Data: ")  # Flower measurements:
    print(feature_data[:5])                 # (sepal length, sepal width, petal length, petal width)

    print("Target Label: ")  # Species labels:
    print(label[:5])                 # (0 = setosa, 1 = versicolor, 2 = virginica)

    print("Feature name: ", feature_names)

    print("Target name: ", target_names)
def printSpeciesData(feature, feature_data, label, target_names):  # pass these parameters so we can work with copys
    print("#. Species, feature data")

    n = len(feature_data)
    for x in range(n):
        if label[x] == 0:
            print(x + 1, "-", feature_data[x][feature], "cm", target_names[0])  # print based on species name

        elif label[x] == 1:
            print(x + 1, "-", feature_data[x][feature], "cm", target_names[1])

        else:
            print(x + 1, "-", feature_data[x][feature], "cm", target_names[2])

def swap(feature, feature_data, label, x, min_idx):
    (feature_data[x][feature], feature_data[min_idx][feature]) = \
        (feature_data[min_idx][feature], feature_data[x][feature])
    (label[x], label[min_idx]) = (label[min_idx], label[x])

def selectionSort(feature, feature_data, label):
    n = len(feature_data)
    for x in range(n):
        min_idx = x

        for y in range(x + 1, n):
            if (feature_data[y][feature] < feature_data[min_idx][feature]):  # sort by first feature (sepal length)
                min_idx = y  # change min to this new index

        swap(feature, feature_data, label, x, min_idx)

def printMinMax_SLen(feature, feature_data):
    n = len(feature_data)
    print("min", feature_data[1][feature], "---->", feature_data[n - 1][feature], "max")

feature_data_copy = feature_data.copy()  # create personal copy of data sets
label_copy = label.copy()

# main
featureValue = 3  # 0 = sepal length, 1 = sepal width, 2 = petal length, 3 = petal length

selectionSort(featureValue, feature_data_copy, label_copy)

printSpeciesData(featureValue, feature_data_copy, label_copy, target_names)

printMinMax_SLen(featureValue, feature_data_copy)
