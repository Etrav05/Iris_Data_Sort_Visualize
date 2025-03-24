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

def test_function_calls():
    print("Feature Data: ")  # Flower measurements:
    print(feature_data[:5])                 # (sepal length, sepal width, petal length, petal width)

    print("Target Label: ")  # Species labels:
    print(label[:5])                 # (0 = setosa, 1 = versicolor, 2 = virginica)

    print("Feature name: ", feature_names)

    print("Target name: ", target_names)
def print_species_data(feature, ffeature_data, flabel, ftarget_names):  # pass parameters so we can work with copies
    print("#. Species, feature data")  # f prefix on all parameters means "function"

    n = len(feature_data)
    for x in range(n):
        if flabel[x] == 0:
            print(x + 1, "-", ffeature_data[x][feature], "cm", ftarget_names[0])  # print based on species name

        elif flabel[x] == 1:
            print(x + 1, "-", ffeature_data[x][feature], "cm", ftarget_names[1])

        else:
            print(x + 1, "-", ffeature_data[x][feature], "cm", ftarget_names[2])

def swap(feature, ffeature_data, flabel, x, min_idx):
    (ffeature_data[x][feature], ffeature_data[min_idx][feature]) = \
        (ffeature_data[min_idx][feature], ffeature_data[x][feature])
    (flabel[x], flabel[min_idx]) = (flabel[min_idx], flabel[x])

def selection_sort(feature, ffeature_data, flabel):
    n = len(ffeature_data)
    for x in range(n):
        min_idx = x

        for y in range(x + 1, n):
            if ffeature_data[y][feature] < ffeature_data[min_idx][feature]:  # sort by first feature (sepal length)
                min_idx = y  # change min to this new index

        swap(feature, ffeature_data, flabel, x, min_idx)

def print_min_max(feature, ffeature_data):
    n = len(ffeature_data)
    print("min", ffeature_data[1][feature], "---->", ffeature_data[n - 1][feature], "max")

feature_data_copy = feature_data.copy()  # create personal copy of data sets
label_copy = label.copy()

# main
featureValue = 3  # 0 = sepal length, 1 = sepal width, 2 = petal length, 3 = petal length

selection_sort(featureValue, feature_data_copy, label_copy)

print_species_data(featureValue, feature_data_copy, label_copy, target_names)

print_min_max(featureValue, feature_data_copy)
