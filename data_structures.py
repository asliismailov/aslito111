#DATA STRUCTURES
#######################
#Veri yapılarına giriş ve hızlı özet

#Sayılar : integer
x = 46
type(x)

# Sayılar : float
x = 10.3
type(x)

# Sayılar : complex
x = 2j + 1
type(x)

#String
x = "Hello AI "
type (x)

# Boolean
True
False
type (True)
5 == 4
type(3 ==2 )

#Liste
x = ["otc", "eth","xrp" ]
type (x)

#Sözlük (Dictionary)--key value durumu var : kullanılıyor
x = {" name" :"Peter", "Age":36 }
type (x)

#Demet (Tuple)
x = ("phyton","ml","ds")
type (x)

#Set
x= {"phyton", "ml", "ds"}
type(x)

# Liste, tuple, set ve dictionary veri yapıları aynı zamanda phyton collectıons (arrays) olarak geçmektedir

#1.Sayılar (Numbers) : int, float, complex
a = 5
b = 10.5
a * 3
a / 7
a * b / 10
a ** 2

#Tipleri değiştirme :
int (b)
float (a)

#önce parantez içini yapıp sonra int a çeviriyor
int(a * b / 10)

c= a * b / 10
int(c)

# 2.Karakter dizileri (Strings) :str "
print("John")
print('John')

#print yazmadan kullanabiliriz, program yazarken bilgi paylaşmak istediğimizde print i kullanmamız gerekecek
"John"

name = "John "

#Çok satırlı karakter dizileri
""" Veri yapılarına giriş ve hızlı özet,Sayılar (Numbers) : int, float, complex,Karakter dizileri (Strings) :str"""

long_str= """ Veri yapılarına giriş ve hızlı özet,Sayılar (Numbers) : int, float, complex,Karakter dizileri (Strings) :str"""


#Karakter dizilerinin elemanlarına erişmek
name
name [ 0 ]
name [ 3 ]

#Karakter dizilerinde slice işlemi
# 0 dan başlar ve 2 ye kadar gider (2 hariç (h)) Jo
name [ 0 : 2 ]
#long_str[ 0 : 10 ]

#String içerisinde karakter sorgulamak
#bÜYÜK HARF KÜÇÜK HARF DE ÖNEMLİ

" veri " in long_str

" Veri " in long_str

#  \n 1 satır aşağıdan başladığını ifade eder
"complex" in long_str

#3.Karakter dizisi metodları (String Methods)
#Class lar içerisinde tanımlanan fonksiyonlar metoddur

dir (int)
# Tüm metodlara aşağıdaki komut ile erişebiliriz
dir(str)

#len : Gömülü fonksiyondur, stringlerde boyut bilgisine erişmek için kullanıyoruz
name = " John "
type (name)
type(len)
len ("aslito")
len ("ceptelefonu")

#Metod ve fonksiyonu nasıl ayırt ederiz?
#Eger bir fonk class yapısı içinde tanımlandıysa buna metod nedir
#Eğer class yapısı içinde değilse fonksiyondur-bağımsız
#cmd basıp len e tıkladık- builtins.py sayfası açıldı

#upper () & lover () : küçük- büyük dönüşümleri
"miuul ".upper()
"ASLI".lower()
#type(upper) bize bilgi vermedi, cmd tuşuna basıp upper a tıkladık, upper bir method-class içinde

#replace : karakter değiştirir
hi= " hello AI"
hi.replace("l", "p" )

#split : böler
#boşlukara göre kendi böldü
"Hello AI".split()

#strip : kırpar
#başta boşluklar avrdı onları kırptı
" ofofo ".strip()
# o lara göre yaptı
" ofofo ".strip("o")

#capitalize : ilk harfi büyütür
"foo".capitalize()

dir(str)
"foo".startswith("f")


#Boolean (TRUE-FALSE) : bool


#4.Liste (List)
#-Değiştirilebilir
#-Sıralıdır. Index işlemleri yapılabilir
#-Kapsayıcıdır

notes = [1,2,3,4 ]
type (notes)

names = [ "a", "b","v"]
type(names)

#kapsayıcılık özelliğini kullandık
not_nam = [1,2,3,"a", "b", True , [ 1,2,3 ] ]
not_nam [ 6 ]
# 2 geldi
not_nam [ 6 ][ 1 ]
type (not_nam [ 6 ][ 1 ])

#notes daki 0 ı 99 olarak değiştirdik
notes [ 0 ] = 99

#0 dan 4 e kadar elemanları getirdi
not_nam [0 :4 ]

#List Methods
# '__sizeof__', altta iki çizgi olmalı list methods için kullanabilmemiz için
dir(notes)

#notes = [1,2,3,4 ]
#4 elemanlı
len(notes)

#append : Listelere eleman ekler
#Out[91]: [99, 2, 3, 4] sonuna 100 ekledi
notes
notes.append(100)
notes

#pop : indexe göre eleman silme
##Out[91]: [99, 2, 3, 4] 99 u silecek  ve ut[95]: [2, 3, 4, 100] oldu
notes.pop (0)
notes

notes = [1,2,3,4 ]
notes.remove (3)
notes


#insert : indexe ekler   (indert yazarken self çıkıyor bu bir method)
#2. indexe 99 değerini yerleştirdi ve   Out[97]: [2, 3, 99, 4, 100] oldu
notes.insert(2,99)
notes

numbers = [4,2,1,3]
numbers.sort()
numbers

#dir() de çıkan tüm methodlara bakabilirsin
dir(list)

#5.Sözlük (Dictionary)
#Değiştirilebilir
#Sırasız (3.7 sonra sıralı)
#Kapsayıcı

#key- value

#Süslü parantez hem dictionary hem set de var. Dict de key value den dolayı : da var
#Bunlara bir bak çalışmadı
dictionary = {" REG": " Regression",
              " LOG": " Logistic Regression",
              " CART": " Classification and Reg"}

dictionary = {" REG": ["RMSE", 10],
              " LOG": ["MSE", 20],
              " CART": ["CART", 30]}
#dictionary [" CART"][1]      30 a erişmiş oluruz


#key sorgulama
"YSA"in dictionary

#key e göre value ye erişmek
dictionary["REG"]
dictionary.get("REG")

#Value değiştirmek
dictionary["REG"] = ["YSA", 10]

#TÜM metodlara erişmek- ben 1 tane yazmıştım örnek çoğalt
dictionary.keys()
dictionary.values()

#Tüm çiftleri tuple halinde listeye çevirme, key, value şeklinde-liste içerisinde key ve value yi tuple cinsinden verdi
dictionary.items()

dictionary.update ({'REG':11})
#Yeni key eklemek için, Out[108]: {'REG': 11, 'RF': 10} varsa güncelleme yapar yoksa yeni atar
dictionary.update ({'RF':10})


#6.Demet (Tuple) : Listelerin değişime kapalı hali
#-Değiştirilemez
#-Sıralıdır   (Elemanlarına erişilebilir)
#-Kapsayıcıdır       (Birden fazla veri yapısı tutabilir)

t = ('john', 'mark', 1, 2)
type(t)

t[0]
t[0:3]
#t[0]= 99   :TypeError: 'tuple' object does not support item assignment
#tuple da değişiklik yapamayız ama önce list e çevirip değiştirebilirz
#sonra yine tuple a çevirdik ( çok kullanılmıyor tuple)

t= list(t)
t[0]=99
t=tuple(t)
t

#!!!!!!TANIMLARA parantezlerin anlamını da yaz

#7.Set
#-Değiştirilebilir
#-Sırasız + eşsizdir
#- Kapsayıcıdır
#Hız gerektiren, kesişimleri , farkı nedir
#Veri biliminde biraz daha düşük kullanımı

# [] kullandık o yüzden liste
set1 =set ([1, 3, 5])
set2 =set ([1, 2, 3])
type (set1)

#difference : iki kümenin farkı önce girilene göre
# #set1 de olup set2 de olmayanlar  :5
set1.difference(set2)

#set2 de olup set1 de olmayanlar  :2
set2.difference(set1)

#- de kullanabiliriz
set1-set2

#symmetric_difference ()  iki kümede de birbirine göre olmayanlar
set1.symmetric_difference(set2)
set2.symmetric_difference(set1)

#Intersection (): iki kümenin kesişimi
set1 =set ([1, 3, 5])
set2 =set ([1, 2, 3])

set1.intersection(set2)
set2.intersection(set1)
# & da kullanabiliriz
set1 & set2

#union (): iki kümenin birleşimi
set1.union(set2)
set2.union(set1)

#isdisjoint(): iki kümenin kesişimi boş mu (is varsa true false bekleriz)
set1 =set ([7, 8, 9])
set2 =set ([5, 6, 7,8,9,10])
set1.isdisjoint(set2)
set2.isdisjoint(set1)

#isdisjoint(): Bir küme diğer kümenin alt kümesi mi:
set1.issubset(set2)
set2.issubset(set1)

#issuperset() Ç Bir küme diğer kümeyi kapsıyor mu
set2.issuperset(set1)
set1.issuperset(set2)

#set lerin kullanımı da düşük

#NOTE: list, dictionary önemli. Herhangi veri yapısını tanımlamak önemli, hatada veri yapıları arasındakı geçişi bilmeliyiz
#Zamanla pekişecek

