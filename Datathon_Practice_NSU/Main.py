import pandas as pd
import os

current_dir = os.path.dirname(__file__)
csv_file = os.path.join(current_dir, "student.csv")

df = pd.read_csv(csv_file)

print(df)

print(".........................................")

X = df[["Hours_Study","Attendance"]]

y = df["Pass"]

print(X)

print("................................................")

print(y)

from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()
model.fit(X,y)

result = model.predict([[7,90]])

print(result)