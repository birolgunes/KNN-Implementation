# %%
"""
## 171180030 Birol Güneş CENG313 Assignment 2
"""

# %%
from math import sqrt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# %%
iris = load_iris() # Load irisdataset

# %%
print(iris.feature_names) # show data column names

# %%
X = iris.data # x is our data
y = iris.target # y is target data, like virginica, setosa, versicolor type, 0 1 2 

# %%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state= 1920) 

# We split our entire dataset into 70% for practice and 30% for testing.

# Random for every time same random values, why 1920. Because, Even if I didn't select this number, the code works, no problem. The reason I chose this number is to be able to produce different values ​​for different values ​​such as K = 1, K = 3, K = 5. I discovered the number just by shaking it. If we will chose 42, every time accuracy score is %100(1.0). 42 is magical number.

# %%
def euclidean_d(r1,r2): # Euclidean Distance = sqrt(sum i to N (x1_i – x2_i)^2)
    distance = 0.0
    for i in range(len(r1)): 
        distance += (r1[i] - r2[i])**2 # 
    return sqrt(distance)
# Euclidean formula is calculate the distance in the 4th dimension. 4 dimensions are -> sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'

# %%
def KNN(X_train_l, X_test_row, KNN_KEY):
    
    setosa_0 = 0
    versicolor_1 = 0
    virginica_2 = 0
# counter for types, if i found closest, increase it.
    distances = list() # i add all distances in a list and calculate the distances using the list
    for i in range (len(X_train_l)):
        distance = euclidean_d(X_train_l[i],X_test_row)
        distances.append((distance, i))
    distances.sort() # distances sorted because we need closest values
    distances_ID = distances[:KNN_KEY] 
    for i in range (KNN_KEY):
        if y_train[distances_ID[i][1]] == 0:
            setosa_0 += 1
        elif y_train[distances_ID[i][1]] == 1:
            versicolor_1 += 1
        else:
            virginica_2 += 1
    # found it and increase it

    closer_list = list()
    closer_list.append(setosa_0)
    closer_list.append(versicolor_1)
    closer_list.append(virginica_2)
    return closer_list.index(max(closer_list))

# %%
y_true = list()
for i in range (len(y_test)):
    y_true.append(y_test[i])
print(y_true)

# %%
k = 1
prediction_1 = list()
for i in range (len(X_test)):
    prediction_1.append(KNN(X_train,X_test[i],k))
print(prediction_1)
print("Accuracy score for K = 1 : ", accuracy_score(y_true, prediction_1)) 

# %%
k = 3
prediction_3 = list()
for i in range (len(X_test)):
    prediction_3.append(KNN(X_train,X_test[i],k))
print(prediction_3)
print("Accuracy score for K = 3 : ", accuracy_score(y_true, prediction_3)) 

# %%
k = 5
prediction_5 = list()
for i in range (len(X_test)):
    prediction_5.append(KNN(X_train,X_test[i],k))
print(prediction_5)
print("Accuracy score for K = 5 : ", accuracy_score(y_true, prediction_5)) 

# %%
