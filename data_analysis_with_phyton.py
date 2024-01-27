##################################
#PYTHON ILE VERI ANALIZI (DATA ANALYSIS WITH PHYTON)
################
# - NumPy : Kütüphane/ Modül-Matematiksel işlemler için ortaya çıkmış
# - Pandas : Veri analizi/veri manipülasyonu -kütüphane-NumPy üzerine kurulu-onun bazı özelliklerini ve
#veri tutma biçimini geliştirmiştir
# - Veri Görselleştirme : Matplotlib & Seaborn : Kütüphaneler
# - Gelişmiş Fonksiyonel Veri Analizi (Advanced Functional Exploratory Data Analysis)
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1])

#[5 6]

import pandas as pd
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)
subset = df.iloc[0:2, [0, 1]]

########################
#NumPy GİRİŞ#

# - numerical python ifadesinin kısaltılmışı
# - çok boyutlu array ler ve matrisler üzerinde yüksek perf çalışma imkanı sağlar
# - Python programlama dilini kullanarak matematiksel yada istatiksel bazı ihtiyaçları karşılayabilecek bir
#kütüphane -modül oluşturulmuştur
# - Verimli veri saklama ve vektörel operasyonlardır
# - NumPy in listelerden farklılaştığı noktalar :verimli veri saklama ve yüksek seviyeden işlemler(vektörel)
# - NumPy içerisinde veri tutarken , bunu fix type adını verdiği sabitlenmiş tipte tutarak listelere
#kıyasla çok daha hızlı bir şekilde işlem yapmayı sağlar
# - Döngü yazmaya gerek olmadan array seviyesinde çok basit işlemlerle normalde çok daha çaba gerektiren
#işlemleri gerçekleştirme imkanı sağlar

# - Why is NumPy ?
# - Creating NumPy Arrays
# - Attibutes of NumPy Arrays
# - Reshapping
# - Index Selection
# - Slicing
# - Fancy Index
# - Conditions of NumPy
# - Mathematical Operations

########
#Why is NumPy ?#
import numpy as np # np kısa yol ismi

import numpy as np

a = [1, 2, 3, 4]
b= [2, 3, 4, 5]

ab = []

for i in range (0, len(a)) : #  0 dan 4 e kadar sayılar olabilir a da olabilir b de olabilir-listenin
    #bütün elemanlarını gezmek önemli
    ab.append(a[i] * b[i])
#--------
ab = []
for i in range (0, len(a)) :
    ab.append(a[i] * b[i])
ab
#----------
#numPy ile #

a = np.array ([1, 2, 3, 4])
b = np.array ([2, 3, 4, 5])
a * b

#-------------------------
#NumPy ARRAY I OLUSTURMAK##
#array veri yapısı ( diğer veri yapıları: integer, float, string (karakter dizileri, listeler, setler ,
#sözlükler ve tuple)

#ndaary yada numPy array denir

import numpy as np

#Liste üzerinden numpy array oluşturacağız
np.array([1, 2, 3, 4, 5])
type(np.array([1, 2, 3, 4, 5]))
# type : numpy.ndarray

#girdiğimiz sayı adetince 0 değeri oluşturur
np.zeros()
np.zeros(10, dtype=int)

#Hangi sınırdan hangi sınıra kadar array oluşturmak istiyorsun
np.random.randint()
#0-10 arasında rastgele 10 tane integer seç
np.random.randint(0, 10 , size=10)

#örn 3 argümanım var 1.oluşturmak istediğim normal dağılımlı kitlenin ort 2.argümanı 3.boyut bilgisi
np.random.normal()
# 3 satır 4 sütun, ort 10 , standart sapması 4 normal dağılımlı sayılar
np.random.normal(10, 4, (3, 4))

##NOT: Genelde 0 dan array oluşturulmaz var olan veriler üzerinde çalışılır

###NUMPY ARRAY ÖZELLİKLERİ#####
import numpy as np

# ndim: boyut sayısı
# shape : boyut bilgisi
# size : toplam eleman sayısı
# dtype: array veri tipi

a = np.random.randint(10, size = 5)
a

a.ndim
a.shape
a.size
a.dtype
# 1 boyutlu, 5 eleman sayısı olan, 5 toplam eleman sayısı,int 64 dedi

##Reshaping##
#numpy array in shape ini değiştirmek istediğimizde

import numpy as np
np.random.randint(1, 10, size = 9)
#2 boyutlu mesela 3-3 lük matris
np.random.randint(1, 10, size = 9).reshape(3,3 )
#array([[1, 9, 6],
       #[4, 4, 7],
       #[7, 7, 8]])

YADA
ar =np.random.randint(1, 10, size = 9)
ar.reshape(3,3)
# 9 elemanlı olduğu için 3 *3 lük oldu 10 eleman olsa yapamazdık

###INDEX İŞLEMLERİ###ÖNEMLİ!!
#0 dan 10 a kadar oluşsan random sayılardan değer oluşturduk
import numpy as np
a = np.random.randint(10, size = 10)
a
#array([2, 3, 8, 4, 6, 4, 1, 6, 7, 1])

a [0]
a [0 : 5]
#array([2, 3, 8, 4, 6])

#a [0 : 5] slicing

a [0] = 999
a

#2 boyutlu array varsa
m = np.random.randint(10, size = (3, 5))
m
#array([[6, 8, 5, 3, 7],
       #[5, 3, 6, 0, 9],
       #[0, 3, 9, 8, 3]])

m [0, 0]
m [1, 1]
m [2, 3] = 999

m [2, 3] = 2.9
#float sonuç gelemez

#bütün satıları seç 0. sütunu seç
m [: , 0 ]
m [1, :]
m [0 : 2, 0 :3]

#FANCY INDEX#
import numpy as np

#0 dan 30 a kadar 3 er 3 er artacak şekilde
v = np.arange(0, 30 ,3)
v
#array([ 0,  3,  6,  9, 12, 15, 18, 21, 24, 27])

v [1]
v [4]

catch = [1, 2, 3]
v[catch]

#NUMPY KOŞULLU İŞLEMLER###

import numpy as np
v = np.array([1, 2, 3, 4, 5])

#3 den küçüklere nasıl erişiriz
# -klasik python

ab = []
for i in v :
    if i < 3 :
        ab.append(i)
ab

# -Numpy ile #
v < 3
#array([ True,  True, False, False, False])
v [v < 3]

v [v != 3] # eşit değildir demek
v [v ==3 ]
v [v >= 3]

#MATEMATİKSEL İŞLEMLER#

import numpy as np
v = np.array([1, 2, 3, 4, 5])

v / 5
v * 5 / 10
v ** 2
v - 1

np.subtract(v, 1)
np.add (v , 1)
np.mean (v) # ortalama
int (np.mean (v))
np.sum (v)
np.min (v)
np.max (v)
np.var(v) # varyans

#kalıcı olmasını istiyorsak yeni array in tekrar atamamız lazım
v = np.subtract(v, 1)
v

#NUMPY ILE IKI BILINMEYENLI DENKLEM ÇÖZME

# 5*X0 + X1 = 12
# X0 + 3*X1 = 10

#katsayılar (x0 ve x1 in)
import numpy as np
a = np.array ( [5, 1], [1, 3] )
#sonuçlar
b = np.array ([12,10])

a = np.array([[5, 1], [1, 3]])
b = np.array ([12, 10])

np.linalg.solve(a, b)

####PANDAS#####
#Bir çok farklı kaynaktan veri okuyabiliriz
#Derin öğrenme, machine learning vs ilgili

# -Pandas Series
# -Reading data
# -Quick look at data
# -Selection in Pandas
# -Aggregation §grouping
# -Apply & lambda
# - Join işlemleri

#PANDAS SERIES#
#Pandas series :tek boyutlu ve index bilgisi barındıran bir veri tipi
#Pandas dataframe : çok boyutlu ve index bilgisi barındıran bir veri tipi

#Ana veri yapısı : Pandas dataframe
#Etrafında pandas serisi,numpy array, python listeleri de bilmek gerek
#veri manipülasyonu ve analizi genelde pandas dataframe üzerinden olacak

import pandas as pd

pd.Series ([10, 77 ,12, 4, 5])
#0    10
#1    77
#2    12
#3     4
#4     5

s = pd.Series ([10, 77 ,12, 4, 5])
s
type(s)
#pandas.core.series.Series

s.index
s.dtype
s.size
s.ndim # pandas serileri tek boyutlu
s.values
#array([10, 77, 12,  4,  5])
type(s.values)
#numpy.ndarray

#Bir pandas serisinin sonuna values ifadesini girdiğimizde ve değerlerine erişmek istediğimzide
#numpy array olarak döndürdü-index ile ilgilenmediysek

s.head(3) #ilk 5 gözlemi getirir
s.tail (3)

#VERİ OKUMA####
import pandas as pd
#csv, txt , excel yada diğer özel bazı dosya formatlarını okuabilir

#CSV#
#örnekte proje dosyası altında csv var-copy path ile onun ismini alıp aşağıda tırnak işareti yerine
#yazabiliriz

df = pd.read_csv('datasets/advertising.csv')
df.head ()
#!pd ya cmd tuşuna absarak tıklayıp buradan cmd f ile metodlara ulaşabiliriz
#cmd ile üzerine tıklarayak fonk detayları ve argüman tanımları yer alıyor

#pandas cheatsheet !!!!BURADAN ARA

#VERİYE HIZLI BAKIŞ###
import pandas as ps
import seaborn as sns

sns.load_dataset() #seaborn içerisinde bazı yaygın verileri koydum, siz bunlarla kolayca çalışın diyerek
#barındırdığı veri setlerine erişebiliriz

df = sns.load_dataset('titanic')
#survived veri setinin ana odağı-bağımlı-hedef değişken

df.head()
df = sns.load_dataset('titanic')
df.head()
df.tail()
df.shape
df.info()
df.columns
df.index
df.describe ().T #ÖZET BİLGİ
df.isnull ().values.any () # en az 1 tane eksik veri var mı
#values kullandığımız için numpy array ine dönüştü
df.isnull ().sum () #değişkenlerdeki eksikliğe bakılacak, true 1 false 0 olarak sayacak

df['sex'].head # sex deki kadın erkek sayısına baktık
df['sex'].value_counts()
#sex
#male      577
#female    314
#Name: count, dtype: int64

#PANDASDA SEÇİM İŞLEMLERİ####!!ÖNEMLİ -veri analizi/manipülasyonu için
#####

import pandas as pd
import seaborn as sns
df = sns.load_dataset('titanic')
df.head()

df.index
df [0 : 13 ]
df.drop(0, axis = 0).head() #0.satırı silmiş olduk

delete_indexes = [1, 3, 5, 7] # 1 3 5 7 indexlerindeki değerleri sil
df.drop(delete_indexes, axis = 0 ).head(10)

#kalıcı hale getirmek için
# df = df.drop(delete_indexes, axis = 0 )
# df = df.drop(delete_indexes, axis = 0, inplace= True )

#Değişkeni indexe çevirme
#Yaş değişkenini indexe ,indeksdeki değeri de bir değişken olarak değişkenlerin arasına almak istediğimizi
#düşünelim

df ['age'].head ()
df.age.head ()

df.index = df.age
#artık index olduğu için değişken olarak ihtiyaç yok silmek için:
df.drop('age', axis =1).head() #axis = 1 dedik sutun olduğu için

df.drop('age', axis=1, inplace=True) # kalıcı olarak bu değişken gitti
df.head()

#şu an yaş değişkeni olarak indexde
#--------------

#indexi değişkene çevirme
#1.yol
df.index

df ['age'] # key error verdi çünkü age i sildik

#Bu dataframe e yeni değişken eklemek için o dataframe içerisinde olmayan bir değişken girersek
#yeni değişken eklemiş oluruz

df ['age'] = df.index
df.head()
#---
#2.yol
df.reset_index().head () #indexde yer alan değeri silecek, yani sütun olarak yeni bir değişken olarak
#ekleyecek

df = df.reset_index().head ()
df = df.reset_index()
df.head()

#--

df.index

df["age"] = df.index

df.head()
df.drop("age", axis=1, inplace=True)

df.reset_index().head()
df = df.reset_index()
df.head()

#DEĞİŞKENLER ÜZERİNDE İŞLEMLER#### (SUTUN INDEXLERI )

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None ) #... lardan kurtulmak istersek
df = sns.load_dataset('titanic')
df.head()

'age' in df

#değişken seçme
df ['age'].head()
df.age.head()

df ['age'].head()
type(df ['age'].head())
#pandas.core.series.Series

#!!ÖNEMLİ:Bir değişken seçerken sonucu seri yada dataframe olarak alabiliriz.
# [[]] girersek veri yapısı bozulmaz ve dataframe olarak devam eder

df [['age']].head()
type(df [['age']].head())
#pandas.core.frame.DataFrame

df[['age', 'alive']]
col_names = ['age','adult_male', 'alive']
df [col_names]

#elimizdeki veri setine yeni değişken eklemek istersek
df ['age2'] = df ['age']** 2
df.head()

df ['age3'] = df ['age'] / df ['age2']
df.head()

df.drop('age3', axis=1).head() #sütunlara göre silme işlemi yaptık, kalıcı olması için inplace i true yapmalı
col_names = ['age','adult_male', 'alive']
df.drop(col_names, axis=1).head()

#veri setinde belirli string ifade barındıran değişkeneleri silmek istiyoruz
df.loc # seçim yapmak için kullanılan özel yapı
df.loc [:, df.columns.str.contains] # tüm satırlar, columns da str lere contains metodunu uygulayacağıgz
#bana bir string ifade ver ben benden önceki string de bu var mı yok mu bakayım

df.loc [:, df.columns.str.contains ('age')].head()

df.loc [:, ~ df.columns.str.contains ('age')].head() #~ bunun dışındakileri seç demek-age le ilgili olanları
#silmiş olduk

#LOC & ILOC###
#####
#ILOC numpy dan index bilgisi vererek seçim yapma işlemlerini
#LOC ise mutlak olarak indexlerdeli label lara göre seçim yapar

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None )
df = sns.load_dataset('titanic')
df.head()

#iloc : integer based selection

df.iloc[0:3] # e kadar seçer 3 hariç
df.iloc[0 , 0]
# \ kodun aşağı doğru devam ettiğini ifade eder

#loc: label based selection
df.loc [0:3] # e kadar seçmez 3 de dahil

df.iloc [0:3, 'age'] # integer based hata aldık
df.loc [0:3, 'age']
#satır yada indexlerdeki değerlerin bizaat kendilerine göre seçim işlemi yapmak istersek loc kullanırız

col_names = ['age', 'embarked', 'alive']
df.loc [0:3, col_names]

#KOŞULLU SEÇİM###

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None )
df = sns.load_dataset('titanic')
df.head()

#YAŞI 50 DEN BÜYÜK OLANLARA ERİŞMEK İSTİYORUZ
df[df['age'] > 50 ].head() # 5 gözlemi görelim diye head yazdık
df[df['age'] > 50 ].count()
df[df['age'] > 50 ]['age'].count() #sonuç

#yaşı 50 den büyük olan kişilerin  claa ını merak ettik
df.loc[df['age'] > 50, ['age', 'class']].head()

#yaşı 50 den büyük olan erkekler
#2 koşul var-koşulların parantez içine alınması gerek
df.loc[(df['age'] > 50) & (df ['sex']== 'male') , ['age', 'class']].head()

df.loc[(df['age'] > 50)
       & (df ['sex']== 'male')
       & (df['embark_town']== 'Cherbourg') ,
       ['age', 'class', 'embark_town']].head()

df ['embark_town'].value_counts ()

#yaş 50 den büyük, cinsiyet erkek, 'embark_town' de Cherbourg yada Southampton olanlar yada için | kullandık
df_new= df.loc[(df['age'] > 50)
       & (df ['sex']== 'male')
       & ((df['embark_town']== 'Cherbourg') | (df['embark_town']== 'Southampton')) ,
       ['age', 'class', 'embark_town']]

df_new ['embark_town'].value_counts ()

#TOPLULAŞMA VE GRUPLAMA (Aggregation and Grouping)
#####
#Toplulaştırma : özet istatistikler veren fonksiyonlar

# - count ()
# - first ()
# - last ()
# - mean ()
# - median ()
# -min ()
# - max ()
# -std ()
# - var ()
# - sum ()
# - pivot table

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None )
df = sns.load_dataset('titanic')
df.head()

#kadınların ve erkeklerin yaş ort erişmek istiyoruz
df['age'].mean()

#aşağıdaki 2.ye alış-hoca onu önerdi
df.groupby('sex')['age'].mean ()
df.groupby('sex').agg({'age' : 'mean'})
#sex
#female  27.915709
#male    30.726645

df.groupby('sex').agg({'age' : ['mean', 'sum']})
#        mean       sum
#sex
#female  27.915709   7286.00
#male    30.726645  13919.17

df.head()

df.groupby('sex').agg({'age' : ['mean', 'sum'],
                       'survived': 'mean'})
#             age            survived
             mean       sum      mean
#sex
#female  27.915709   7286.00  0.742038
#male    30.726645  13919.17  0.188908
#gemiye binen kadınların % 74 ü hayatta kalmış, erkeklerin % 18 i hayatta kalmış

#iki seviyeden groupby işlemi yaptık
df.groupby(['sex', 'embark_town']).agg({'age' : ['mean'],
                       'survived': 'mean'})

#üç kırılımda groupby yaptık
df.head()
df.groupby(['sex', 'embark_town', 'class']).agg({'age' : ['mean'],
                       'survived': 'mean'})

df.groupby(['sex', 'embark_town', 'class']).agg({
    'age' : ['mean'],
    'survived': 'mean',
    'sex' : 'count'})

#PIVOT TABLE
########
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None )
df = sns.load_dataset('titanic')
df.head()

#1.argüman values argümanı, kesişimlerde ne görmek istediğimizi yazarız 2. indexte(satırda) ne görmek istiyoruz
#3.sütunda ne görmek istiyoruz
#pivot table () ın ön tanımlı değeri mean (ortalama)-kesişimde yer alacak değişkenin ön tanımlı ortalamasını alır
df.pivot_table('survived', 'sex', 'embarked')

df.pivot_table('survived', 'sex', 'embarked', aggfunc= 'std')

df.pivot_table('survived', 'sex', ['embarked', 'class'])
#sütunlarda iki index satırlarda tek index var

#kadınların ve 1.sınıf yolcuların hayatta kalma oranı yüksek, çocukları nasıl öğreniriz?
#age sayısal olduğu için kategorik değişkene çeviriyoruz

df['new_age'] = pd.cut
#cut ve qcut -sayısal değişkenleri kategorik değişkene çevirmek için kullanılan fonksiyonlar
#elindeki sayısal değişkeni biliyorsan cut kullanılır ,sayısal değişkeni bilmiyorsak qcut kullanırız
#qcut otomatik olarak değerleri küçükten büyüye sıralar ve yüzdelik çeyrek değerlerine göre bunları gruplara,
#kategorilere böler-yaygın kullanılır

df['new_age'] = pd.cut(df['age'],[0, 10, 18, 25, 40, 90] ) #neyi nelerden bölücez
df.head()

df.pivot_table('survived', 'sex', 'new_age')
df.pivot_table('survived', 'sex', ['new_age', 'class'])
pd.set_option('display.width', 500)

#APPLY & LAMBDA
#apply : satır yada sütunlarda otomatik olarak fonksiyon çalıştırma imkanı sağlar
#lambda : bir fonksiyon tanımlama şekli

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None )
pd.set_option('display.width', 500)
df = sns.load_dataset('titanic')
df.head()

df["age2"] = df["age"]*2
df["age3"] = df["age"]*5

(df["age"]/10).head()
(df["age2"]/10).head()
(df["age3"]/10).head()

for col in df.columns:
    if "age" in col:
        print(col)

for col in df.columns:
    if "age" in col:
        print((df[col]/10).head())

for col in df.columns:
    if "age" in col:
        df[col] = df[col]/10

df.head()

df[["age", "age2", "age3"]].apply(lambda x: x/10).head()

df.loc[:, df.columns.str.contains("age")].apply(lambda x: x/10).head()

df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head()

def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()

df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()

# df.loc[:, ["age","age2","age3"]] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)

df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)

df.head()

#############################################
# Birleştirme (Join) İşlemleri
#############################################
import numpy as np
import pandas as pd
m = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99

pd.concat([df1, df2])

pd.concat([df1, df2], ignore_index=True)


######################
# Merge ile Birleştirme İşlemleri
#######################

df1 = pd.DataFrame({'employees': ['john', 'dennis', 'mark', 'maria'],
                    'group': ['accounting', 'engineering', 'engineering', 'hr']})

df2 = pd.DataFrame({'employees': ['mark', 'john', 'dennis', 'maria'],
                    'start_date': [2010, 2009, 2014, 2019]})

pd.merge(df1, df2)
pd.merge(df1, df2, on="employees")

# Amaç: Her çalışanın müdürünün bilgisine erişmek istiyoruz.
df3 = pd.merge(df1, df2)

df4 = pd.DataFrame({'group': ['accounting', 'engineering', 'hr'],
                    'manager': ['Caner', 'Mustafa', 'Berkcan']})

pd.merge(df3, df4)


#############################################
# VERİ GÖRSELLEŞTİRME: MATPLOTLIB & SEABORN
#############################################

#############################################
# MATPLOTLIB
#############################################

# Kategorik değişken: sütun grafik. countplot bar
# Sayısal değişken: hist, boxplot


#############################################
# Kategorik Değişken Görselleştirme
#############################################
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

#df['sex'].value_counts()
#df['sex'].value_counts().plot()

df['sex'].value_counts().plot(kind='bar')
plt.show()




#############################################
# Sayısal Değişken Görselleştirme
#############################################
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

plt.hist(df["age"])
plt.show()

plt.boxplot(df["fare"])
plt.show()


#############################################
# Matplotlib'in Özellikleri
#############################################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

#######################
# plot
#######################

x = np.array([1, 8])
y = np.array([0, 150])

plt.plot(x, y)
plt.show()

plt.plot(x, y, 'o')
plt.show()

x = np.array([2, 4, 6, 8, 10])
y = np.array([1, 3, 5, 7, 9])

plt.plot(x, y)
plt.show()

plt.plot(x, y, 'o')
plt.show()



#######################
# marker
#######################

y = np.array([13, 28, 11, 100])

plt.plot(y, marker='o')
plt.show()

plt.plot(y, marker='*')
plt.show()

markers = ['o', '*', '.', ',', 'x', 'X', '+', 'P', 's', 'D', 'd', 'p', 'H', 'h']

#######################
# line
#######################

y = np.array([13, 28, 11, 100])
#plt.plot(y, linestyle="dashed")

#plt.plot(y, linestyle="dotted")

#plt.plot(y, linestyle="dashdot")

plt.plot(y, linestyle="dashdot", color="r")
plt.show()

#######################
# Multiple Lines
#######################

x = np.array([23, 18, 31, 10])
y = np.array([13, 28, 11, 100])
plt.plot(x)
plt.plot(y)
plt.show()

#######################
# Labels
#######################

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)
# Başlık
plt.title("Bu ana başlık")

# X eksenini isimlendirme
plt.xlabel("X ekseni isimlendirmesi")

plt.ylabel("Y ekseni isimlendirmesi")

plt.grid()
plt.show()

#######################
# Subplots
#######################

# plot 1
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 2, 1)
plt.title("1")
plt.plot(x, y)

# plot 2
x = np.array([8, 8, 9, 9, 10, 15, 11, 15, 12, 15])
y = np.array([24, 20, 26, 27, 280, 29, 30, 30, 30, 30])
plt.subplot(1, 2, 2)
plt.title("2")
plt.plot(x, y)
plt.show()


# 3 grafiği bir satır 3 sütun olarak konumlamak.
# plot 1
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 1)
plt.title("1")
plt.plot(x, y)

# plot 2
    x = np.array([8, 8, 9, 9, 10, 15, 11, 15, 12, 15])
    y = np.array([24, 20, 26, 27, 280, 29, 30, 30, 30, 30])
    plt.subplot(1, 3, 2)
    plt.title("2")
    plt.plot(x, y)

# plot 3
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 3)
plt.title("3")
plt.plot(x, y)

plt.show()

#############################################
# SEABORN
#############################################
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
df = sns.load_dataset("tips")
df.head()


df["sex"].value_counts()
sns.countplot(x=df["sex"], data=df)
plt.show()

df['sex'].value_counts().plot(kind='bar')
plt.show()


#############################################
# Sayısal Değişken Görselleştirme
#############################################

sns.boxplot(x=df["total_bill"])
plt.show()

df["total_bill"].hist()
plt.show()

#############################################
# GELİŞMİŞ FONKSİYONEL KEŞİFÇİ VERİ ANALİZİ (ADVANCED FUNCTIONAL EDA)
#############################################
# 1. Genel Resim
# 2. Kategorik Değişken Analizi (Analysis of Categorical Variables)
# 3. Sayısal Değişken Analizi (Analysis of Numerical Variables)
# 4. Hedef Değişken Analizi (Analysis of Target Variable)
# 5. Korelasyon Analizi (Analysis of Correlation)


#############################################
# 1. Genel Resim
#############################################
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()
df.tail()
df.shape
df.info()
df.columns
df.index
df.describe().T
df.isnull().values.any()
df.isnull().sum()

def check_df(dataframe, head=5):
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head(head))
    print("##################### Tail #####################")
    print(dataframe.tail(head))
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    print("##################### Quantiles #####################")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)


check_df(df)

df = sns.load_dataset("flights")
check_df(df)
