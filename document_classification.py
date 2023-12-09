import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier
from imblearn.over_sampling import RandomOverSampler, SMOTEN


def filter_location(location):
    result = re.findall("\,\s[A-Z]{2}$", location)
    if len(result) > 0:
        return result[0][2:]
    else:
        return location


data = pd.read_excel("final_project.ods", engine="odf", dtype=str)
target = "career_level"
data["location"] = data["location"].apply(filter_location)
x = data.drop(target, axis=1)
y = data[target]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=100, stratify=y)

ros = SMOTEN(random_state=42,
                        sampling_strategy={"managing_director_small_medium_company": 100, "specialist": 100,
                                           "director_business_unit_leader": 100, "bereichsleiter": 1000}, k_neighbors=2)
print(y_train.value_counts())
print("---------------")
x_train, y_train = ros.fit_resample(x_train, y_train)
print(y_train.value_counts())

preprocessor = ColumnTransformer(transformers=[
    ("title_features", TfidfVectorizer(), "title"),
    ("location_features", OneHotEncoder(handle_unknown="ignore"), ["location"]),
    (
    "des_features", TfidfVectorizer(stop_words="english", ngram_range=(1, 2), min_df=0.01, max_df=0.95), "description"),
    ("function_features", OneHotEncoder(handle_unknown="ignore"), ["function"]),
    ("industry_features", TfidfVectorizer(), "industry"),
])

model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("model", RandomForestClassifier()),
])

model.fit(x_train, y_train)
y_predict = model.predict(x_test)
print(classification_report(y_test, y_predict))
#                                         precision    recall  f1-score   support
#
#                         bereichsleiter       0.67      0.04      0.08       192
#          director_business_unit_leader       1.00      0.14      0.25        14
#                    manager_team_leader       0.64      0.70      0.67       534
# managing_director_small_medium_company       0.00      0.00      0.00         1
#   senior_specialist_or_project_manager       0.80      0.93      0.86       868
#                             specialist       0.00      0.00      0.00         6
#
#                               accuracy                           0.74      1615
#                              macro avg       0.52      0.30      0.31      1615
#                           weighted avg       0.73      0.74      0.70      1615


