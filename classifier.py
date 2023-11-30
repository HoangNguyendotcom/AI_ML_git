import pandas as pd
import numpy as np
from ydata_profiling import ProfileReport
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

data = pd.read_csv("data/diabetes.csv")
#profile = ProfileReport(data, title = "My Report")
#profile.to_file("Diabetes_report.html")
#data_frame = pd.DataFrame(data)
#print(data_frame)

# Define the target: Outcome columnt 
target = "Outcome"
x = data.drop(target, axis = 1)
y = data[target]

# Step 1: Create the data set for train, test, validation:

# Notice: After every running file, x_train, x_test are randomly generated.
# If wanting to generate constant x_train, x_test, add random_state = (num) to save the generation.
x_train, x_test, y_train, y_test = train_test_split(x, y , test_size= 0.2, random_state = 7089) #Example: random_state = 7089 
# x_train, x_val, y_train, y_val = train_test_split(x_train, y_train , test_size= 0.25, random_state= 7089) #Example: random_state = 7089 


#Step2: Data Preprocessing

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train) # Tranform x_train with scaler
x_test = scaler.transform(x_test)

# fit: 
# transform: After at least one fit process.
# fit_transform:

# Step3: Apply model

'''
# Using Logistic Regression:
model = LogisticRegression()
model.fit(x_train, y_train)
y_predict = model.predict(x_test)
print(classification_report(y_test, y_predict))
precision    recall  f1-score   support

           0       0.82      0.85      0.83       106
           1       0.64      0.58      0.61        48

    accuracy                           0.77       154
   macro avg       0.73      0.72      0.72       154
weighted avg       0.76      0.77      0.76       154
'''

'''
# Using Support Vectors Machine:
model = SVC()
model.fit(x_train, y_train)
y_predict = model.predict(x_test)
print(classification_report(y_test, y_predict))

precision    recall  f1-score   support

           0       0.81      0.86      0.83       106
           1       0.64      0.56      0.60        48

    accuracy                           0.77       154
   macro avg       0.73      0.71      0.72       154
weighted avg       0.76      0.77      0.76       154
'''

#Using Random Forrest:
model = RandomForestClassifier()
model.fit(x_train, y_train)
y_predict = model.predict(x_test)
print(classification_report(y_test, y_predict))

precision    recall  f1-score   support

           0       0.81      0.79      0.80       106
           1       0.56      0.58      0.57        48

    accuracy                           0.73       154
   macro avg       0.68      0.69      0.69       154
weighted avg       0.73      0.73      0.73       154