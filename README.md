# Responsi : Workshop Python

**NIM : 195410033**

**Nama : Moh.Fauzi**

**Hari / Tanggal : Selasa, 14 Juni 2022**

## Penjelasan
Hal yang pertama kali saya lakukan adalah mencari dataset di internet yang digunakan. Dataset yang saya gunakan berasal dari data [UCI Machine Learning](https://archive.ics.uci.edu/ml/index.php) yaitu dataset [iris](https://archive.ics.uci.edu/ml/datasets/Iris). Dataset `Iris` merupakan dataset multivariate yang diperkenalkan oleh ahli statistika dan biologi inggris, Ronald Fisher, pada tahun 1936. Dataset bunga Iris ini sangat terkenal di dunia Machine Learning yang digunakan untuk klasifikasi. Dataset ini terdiri dari 3 spesies Iris yaitu Iris Setosa, Iris Virginica, dan Iris Versicolor dan tiap spesiesnya memiliki 50 sampel. Dalam data Iris terdapat 4 atribut yang dapat mempengaruhi klasifikasi yaitu, sepal length, sepal width, petal length, dan petal width dalam centimeter yang berbeda-beda.

## Mengimport library
Kemeudian saya melakukan pengolahan data menggunakan library pandas yang biasa digunakan untuk membuat tabel, mengubah dimensi data, mengecek data, dan lain sebagainya.
```python
# import library pandas
import pandas as pd
```

## mengambil dataset dari UCI-machine learning
Kemudian mengambil dataset menggunakan URL yang telah ditentukan untuk melakukan pengolahan data dan identifikasi variabel `csv_url` yang menyimpan url dataset tersebut. setelah melakukan konversi data pada variabel tersebut menjadi data `csv` yang disimpan ke dalam variabel `iris`.
```python
# mengambil dataset dari UCI-machine learning
csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = pd.read_csv(csv_url, header = None)
iris.head()
```

## Membuat file baru menjadi file csv
Kemudian untuk membuat file baru csv dari dataframe `iris` menggunakan perintah `.to_csv` dengan value saya menentukan nama file yang akan dibuat yaitu `iris.csv`. 
```python
# Membuat file baru menjadi file csv
iris.to_csv("iris.csv")
pd.read_csv("iris.csv")
```