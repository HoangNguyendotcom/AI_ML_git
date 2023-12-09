import pandas as pd
from ydata_profiling import ProfileReport
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OrdinalEncoder, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
data = pd.read_csv("data/StudentScore.xls")

'''
profile = ProfileReport(data, title ="My Report")
profile.to_file("StudentScore_report.html")
'''

# Define the target:
target = "math score"
# Step 1: Create the data set for train, test, validation:

x = data.drop(target, axis=1)
y = data[target]

x_train, x_test, y_train, y_test =train_test_split(x, y, test_size=0.2, random_state=7089)


# data["gender"] - maybe bool data, need to check the unique()
# data["race/ethicity"]: nominal feature
# data["parental level of education"]: ordinal feature
# data["lunch"] : bool data
# data["test preparation course"]: bool data
# data["_ score"] : numerical feature

# Step 2: Data Preprocessing
# Notice: With the missing data, use Simple Imputer
num_trans = Pipeline(steps=[
("imputer", SimpleImputer(strategy="median")),
("scaler", StandardScaler())
])

education_levels = ["some high school", "high school", "some college", "associate's degree", "bachelor's degree", "master's degree"]
gender_value = data["gender"].unique()
lunch_value = data["lunch"].unique()
preparation_value = data["test preparation course"].unique()

ordinal_trans = Pipeline(steps=[
("imputer", SimpleImputer(strategy="most_frequent")),
("encoder", OrdinalEncoder(categories=[education_levels, gender_value, lunch_value, preparation_value]))
])

nominal_trans = Pipeline(steps=[
("imputer", SimpleImputer(strategy="most_frequent")),
("encoder", OneHotEncoder())
])

'''
result_1= num_trans.fit_transform(x_train[["reading score", "writing score"]])
for i, j in zip(x_train[["reading score", "writing score"]].values, result_1):
    print("Before: {}. After: {}".format(i, j))
'''
'''
result_2= ordinal_trans.fit_transform(x_train[["parental level of education"]])
for i, j in zip(x_train[["parental level of education"]].values, result_2):
    print("Before: {}. After: {}".format(i, j))
'''
'''
result_3= nominal_trans.fit_transform(x_train[["race/ethnicity"]])
for i, j in zip(x_train[["race/ethnicity"]].values, result_3):
    print("Before: {}. After: {}".format(i, j))
'''

preprocessor = ColumnTransformer(transformers=[
    ("num_features", num_trans, ["reading score", "writing score"]),
    ("ord_features", ordinal_trans, ["parental level of education", "gender", "lunch", "test preparation course"]),
    ("nom_features", nominal_trans, ["race/ethnicity"])
])


# Create pipeline for model:
model = Pipeline(
    steps = [
        ("preprocessor", preprocessor),
        ("model", LinearRegression())
    ]
)
model.fit(x_train, y_train)
y_predict = model.predict(x_test)

for i, j in zip(y_predict, y_test):
    print("Prediction: {}. Actual: {} ".format(i,j))

# The most popular metric for evaluating a regression model: R2_score
