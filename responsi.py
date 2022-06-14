# import library pandas
import pandas as pd

# mengambil dataset dari UCI-machine learning
csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = pd.read_csv(csv_url, header = None)
iris.head()

# Membuat file baru menjadi file csv
iris.to_csv("iris.csv")
pd.read_csv("iris.csv")