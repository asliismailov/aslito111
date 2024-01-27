#24.01
#PYTHON ALIŞTIRMALARI
# #GÖREV 1
x = 8
type(x)

y= 3.2
type(y)

z=8j + 18
type(z)

a= 'Hello World'
type(a)

b= True
type(b)

c= 23 < 22
type(c)

l=[1, 2, 3, 4]
type(l)

d= {'Name' : 'Jake', 'Age': 27, 'Adress': 'Downtown'}
type(d)

t = {'Machine Learning', 'Data Science'}
type(t)

s= {'Python', 'Machine Learning', 'Data Science'}
type(s)

#GÖREV 2 : Verilen string ifadenin tüm harflerini büyük harfe çeviriniz
#Virgül ve nokta yerine space koyunuz
#kelime kelime ayırınız

text = 'The goal is to turn data into information, and information into insight.'

text =text.upper()
new_text = text.replace(',', '').replace('.', '')
new_text.split()

#Ekran görüntüsü aldım- farklı bir yol var
##new_text = text.upper().replace (',', '').replace('.', '').split()

#hoca iletti##
import re
text = "The goal is to turn data into information, and information into insight."
text = text.upper()
list_of_words = re.sub(r"[.,]", " ", text).split()

#GÖREV 3:Verilenlisteyeaşağıdakiadımlarıuygulayınız.
lst = ['D', 'A', 'T', 'A', 'S', 'C', 'I', 'E', 'N', 'C', 'E']

#Adım 1: Verilen listenin eleman sayısına bakınız.

len(lst)

#Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.

lst[0]
lst[10]

#Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.

lst[0 :4]

# Adım 4: Sekizinci indeksteki elemanı siliniz.

lst.pop(8)
lst
#(Bu değeri de döndürmüş oluyor)
#del lst [8]

#Adım 5: Yeni bir eleman ekleyiniz.

lst.append ('X')
lst

#Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.

lst.insert(8,'N')
lst

#ADIMLARI UYGULAMADAN YAZMAK İÇİN
lst=[a for a in ("DATASCIENCE")]

#GÖREV 4: Verilensözlükyapısınaaşağıdakiadımlarıuygulayınız.

dict = {'Christian': ['America', 18],
        'Daisy': ['England', 12],
        'Antonio' : ['Spain',22],
        'Dante' : ['Italy', 25]}

#Adım 1: Key değerlerine erişiniz.

dict.keys()

#Adım 2: Value'lara erişiniz.

dict.values()

#Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.

dict['Daisy'] = ['England', 13]

#Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.

dict.update({'Ahmet' : ['Turkey', 24]})

#Adım 5: Antonio'yu dictionary'den siliniz

del dict ['Antonio']


# bu da olur --dict.pop('Antonio')

dict.pop('Antonio')

#GÖREV 5 :Argüman olarak bir liste alan, listenin içerisindeki tek ve çift
# sayıları ayrı listelere atayan ve bu listeleri return eden fonksiyon yazınız.

l = [2, 13, 18, 93, 22]
#kontrol ettirmedin###
def divide_l(l) :
    groups = [[],[]]
    for index, number in enumerate(l) :
        if index %2 == 0 :
           groups[0].append(number)
        else :
           groups[1].append(number)
    print (groups)
    return (groups)
divide_l(l)
st = divide_l()
#[[2, 18, 22], [13, 93]]

#Fonk tanımladım
#bu grup listesinin içerisindeki indexlere göre yer alan listelere eleman göndereceğim
#(Enumerate kullandım :Bir iteratif nesne içinde gezip elemanlarına bir
# şey yaparken aynı zamanda o elemanların index bilgilerini de takip etmek istediğimizde kullanılır)

##yada şöyle bir çözüm var##
def fun(x):
    tek_list = [i for i in x if i%2!=0]
    cift_list = [i for i in x if i%2==0]

    return tek_list, cift_list

tek_list, cift_list = fun(l)
print(tek_list)
print(cift_list)

##yada şöyle bir çözüm var##

l=[2,13,18,93,22]
def function(sayilar):
    even_list = []
    odd_list = []
    for index, i in enumerate(sayilar):
        if index % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    print(even_list,odd_list)
    return even_list,odd_list

 function(l)

#yada şöyle
def my_list(input_list):
    even_list = []
    odd_list = []

    for i in range(len(input_list)):
        if i % 2 == 0:
            even_list.append(input_list[i])
        else:
            odd_list.append(input_list[i])
    return even_list, odd_list

even_list, odd_list = my_list([2,13,18,93,22])
print("Even List: ", even_list)
print("Odd List:", odd_list)

#
l = [2, 13, 18, 93, 22]

#diğer çözüm-hoca iletti#
def odds_evens(numbers: list[int]) -> (list[int], list[int]):
    """Takes in a list of numbers and returns two lists => odds, evens

    Args:
        numbers: list of int numbers

    Returns:
        odds: list of odd numbers
        evens: list of even numbers

    """
    # odds = [number for number in numbers if number % 2 != 0]
    # evens = [number for number in numbers if number % 2 == 0]
    odds = []
    evens = []
    [odds.append(number) if number % 2 != 0 else evens.append(number) for number in numbers]
    return odds, evens


odds_evens(l)

#GÖREV:6 Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin
# isimleri bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını
# temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir.
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.

ogrenciler = ['Ali', 'Veli', 'Ayse', 'Talat', 'Zeynep', 'Ece' ]

for index, ogrenci in enumerate(ogrenciler,1):
    if index < 4 :
      print('Mühendislik Fakültesi', index,'.', 'ogrenci:',ogrenci)
    else :
      print('Tıp Fakültesi', index -3,'.', 'ogrenci:',ogrenci)

#diğer çözüm-hoca iletti#
ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

for i, ogrenci in enumerate(ogrenciler):  # ogrenci refers to student
    if i < 3:
        print(f"{ogrenci}, Mühendislik Fakültesi")  # "Mühendislik Fakültesi" refers to "Engineering Faculty"
    else:
        print(f"{ogrenci}, Tıp Fakültesi")  # "Tıp Fakültesi" refers to "Medical Faculty"


#GÖREV:7 Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu
# kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.

ders_kodu =['CMP1005', 'PSY1001', 'HUK1005', 'SEN2204']
kredi = [3, 4, 2, 4]
kontenjan =[30, 75, 150, 25]

new_list = list(zip(kredi, ders_kodu, kontenjan))

for kredi, ders_kodu, kontenjan in new_list :
    if kredi :
       print ('Kredisi', kredi, 'olan', ders_kodu, 'kodlu dersin kontenjanı', kontenjan, 'kişidir')

#yada
ders_kodu=["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi=[3,4,2,4]
kontenjan=[30,75,150,25]

[print("Kredisi {} olan {} kodlu dersin kontenjanı {} kişidir.".format(a,b,c)) for a,b,c in zip(kredi,ders_kodu,kontenjan)]



#GOREV 8 :Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise
# ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyon
# tanımlamanız beklenmektedir.

kume1 = set(['data', 'python'])
kume2 = set(['data', 'function', 'qcut', 'lambda', 'python', 'miuul'])

def check_kume(kume1, kume2) :
    if kume1.issuperset(kume2) :
        ortak_elemanlar = kume1.intersection(kume2)
        print(ortak_elemanlar)
    else :
        fark = kume2.difference(kume1)
        print(fark)

check_kume(kume1, kume2)



#LIST COMPREHENSION ALIŞTIRMALAR
#GOREV 1 : List Comprehension yapısı kullanarak car_crashes verisindeki
# numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.
#numerik olmayan değişkenlerin de ismi büyümeli

import  seaborn as sns
df = sns.load_dataset ('car_crashes')
df.columns

['NUM_ ' + col.upper() if df[col].dtype != 'O' else col.upper() for col in df.columns]

#hoca iletti#
#df[col].dtype != 'O' yerine kullanılabilir (Object değilse nümeriktir-sayısaldır)
from pandas.api.types import is_numeric_dtype
[f"NUM_{col.upper()}" if is_numeric_dtype(df[col]) else col.upper() for col in df.columns]

#GOREV 2: List Comprehension yapısı kullanarak car_crashes verisinde isminde
# "no" barındırmayan değişkenlerin isimlerinin sonuna "FLAG" yazınız.

#Tüm değişkenlerin isimleri büyük harf olmalı.
import  seaborn as sns
df = sns.load_dataset ('car_crashes')
df.columns

df.columns = [col.upper() if 'no' in col else col.upper() + '_FLAG' for col in df.columns ]

#GOREV 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden
# FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.
import  seaborn as sns
df = sns.load_dataset ('car_crashes')
df.columns

new_cols = [col for col in df.columns if "abbrev" not in col and "no_previous" not in col]

#aşağıdaki gibi kullanmak daha mantıklı #hoca da bunu iletti -her zaman 2 tane olmayabilir
#bi liste yapmak daha iyi

og_list = ['abbrev', 'no_previous']

new_cols = [col for col in df.columns if col not in og_list]
print(new_cols)
new_df = df[new_cols]





