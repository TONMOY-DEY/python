import pandas as pd
import os

current_dir = os.path.dirname(__file__)
csv_file = os.path.join(current_dir, "student.csv")

df = pd.read_csv(csv_file)

print(df)