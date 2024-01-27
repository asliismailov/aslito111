#FONKSİYONLAR, KOŞULLAR , DÖNGÜLER ,COMPREHENSIONS
#################
#-Fonksiyonlar (Functions)
#-Koşullar (Conditions)
#-Döngüler (Loops)
#-Comprehensiıons

#1.Fonksiyonlar
#Belirli görevleri yerine getirmek için yazılan kod parçalarıdır

#Fonksiyon Okuryazarlığı
print('a')
# ?print yada help(print) bunu aşağıdaki konsolo yazarsak ana scripti, phyton çalışma dosyasını etkilemiş olmaz
#print bir fonksiyondur

#Signature: print(*args, sep=' ', end='\n', file=None, flush=False) : fonksiyonun argümanları ( bazı
#kaynakalarda parametre deniyor)
#sep, end parametre,vs. parametredir ( fonk tanımlanması esnasında ifade edilen değişkendir)
#Argüman ise bu fonksiyonlar çağrıldığında bu parametre değerlerine karşılık girilen değerlerdir
#Yaygın kullanım hepsine arguman denir

#Argümanlar özellik belirtebileceği gibi fonksiyonun genel amacını biçimlendirmek
#üzere kullanılan alt görevleridir

#-örn : sep : string inserted between values, default a space.
# (?print i aşağıdaki konsola yazarak bu tanımı bulduk)

print('a','b')
#a ve b arasında boşluk var, sep argümanı ön tanımlı olarak boşluktu zaten
#bundan dolayı boşluk yazdırdı
print('a','b', sep='__')
#!!!!fonksiyonların ana amaçlarını bu fonksiyonların üçerisinde yer alan argümanlar ile
#biçimlendirebiliriz
#Docstring yazmayı öğreneceğiz

#Fonksiyon-Argüman
#Dokümantasyonu okuabilmemiz lazım (sep, vs onun içinde yer alıyordu print için,
#?print yada help (print) yazarak eriştik

#Fonksiyon tanımlama
#Girilen sayıları 2 ile çarpacak bir fonk tanımlayalım
# def yazarsak fonk tanımlayacağımız anlaşılır

def calculate (x):
    print(x*2)

calculate(5)

#2 argüman(parametreden) oluşan bir fonk tanımlamak istiyoruz

def summer(arg1,arg2):
    print(arg1 + arg2)

summer(7,8)
#Argümanların sırasını biliyorsanız bildiğiniz sırada girdiğinizde, girdiğiniz değerler ile argümanlar
#eşleşir. Eğer argümanların sırasını bilmiyorsanız eşleşmeyecektir.Ama eşleştirmek istersek
#eğer argümanların adını biliyorsak , bu şekilde girerek kullanım gerçekleştirebiliriz
#summer (arg2=8, arg1=7)


#DOCSTRING
#Fonksiyonlarımıza herkesin anlayabileceği ortak dil ile bilgi notu ekleme yoludur

def summer (arg1,arg2)
    print(arg1 + arg2)

#ilk satırın altına 3 tırnak işareti girerek ortada enter a bastık
def summer (arg1,arg2)
    '''
    Sum of two numbers 
    
    Args:
        arg1: int, float
        arg2: int, float

    Returns:
        int,float

    '''
    print(arg1 + arg2)
#Docstring oluşturmanın 2 yolu var
#En yaygın kullanılan google ve NumPy
#Yukarıda NumPy yolunu denedik

#Phycharm-Prefences- Docstring yazıyoruz ve tool altındaki yeri tıklıyoruz numPy yada google seçebiliriz
#Özetle: 1.Fonk ne yapar 2. Argüman ne yapar 3.Çıktısının ne olduğu 4. Örnekler yada notlar da eklenebilir
#? Docstring yazdığım yeri kapatamadım sorarsın

#Fonk üzerine geldiğimizde girdiğimiz açıklamalar geldi
summer()
#Aşağıdaki konsola ?summer yazdığımda bilgi gelmedi sorarsın
summer(1,3)

#FONKSİYONLARIN STATEMENT/BODY BÖLÜMÜ

#def function_name (parameters/arguments):
#    statements(function body)

def say_hi ():
    print('Merhaba')
    print('Hi')
    print('Hello')

#fonk çalıştırdık (parametre yada argüman girmedik)
say_hi()

#argüman girelim
def say_hi (string):
    print(string)
    print('Hi')
    print('Hello')
say_hi('miuul')


#Girilen 2 sayıyı çarpan, bunu önce bir nesnede tutan ve ondan sonra yazdıran bir fonk tanımla
#Sadece fonk  tanımladık
def multiplication (a, b):
    c = a * b
    print(c)
#fonk u çağırdık
    multiplication(10 ,9)
#Gövde bölümünde atama yapabileceğimizi, bazı işlemler yapabileceğimizi, kod bölümüymüş gibi rahat
#kullanılabileceğini pekiştirmiş olduk

#Girilen 2 sayıyı çarpsın sonra değerleri liste içine ekleyen fonk tanımlayalım
list_store = []

def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)

add_element(1, 8)
add_element(18, 8)
add_element(180, 10)
# [8] di sonra [8, 144] oldu ve [8, 144, 1800] oldu -birşeyler ekledik hep
#Özetle fonk tanımladık-matematiksel işlem oldu-listeye eleman eklemek için method kullandık
#Liste ekrana yazdırıldı

#yeni sayıları eklerken list_Store.append(c) i her seferinde atamadık nasıl oldu?
#Bazı metodlar yeniden atama gerektirmez- veri yapısında kalıcı değişiklik yapabilir
#append onlardan biri

#Local etki alanı
# c = a * b -- c geçici kullan at şeklinde
#list_store.append(c)
#print(list_store)--list_Store global etki alanında(global: bütün çalışma içerisinden erişilebilen değişkenler)
#Fonk tanımladık ve statement bölümünde birden fazla işlem, atama işlemelri,burada olmayan nesnelere
#temas edecek işlemler, yazdırma, fonk çağırma iş gerçekleştirebiliriz

#ÖN TANIMLI ARGUMANLAR/PARAMETRELER (DEFAULT PARAMETERS/ARGUMENTS)

def divide(a, b ) :
    print (a/ b)

def divide(a, b ) :
    divide (a/ b)
divide(10)

divide(1, 2)

# b ye ön tanımlı argüman girdik
def divide(a, b=1 ) :
    print (a/ b)

divide(1)
#mesela print in ön argümanları :
#print(*args, sep=' ', end='\n', file=None, flush=False)

def say_hi(string= 'Merhaba'):
    print(string)
    print('hi')
    print('hello')

say_hi()
#direk merhaba, hi ,hello alt alta geldi

say_hi('mrb')

#NE ZAMAN FONKSIYON YAZMA IHTIYACIMIZ OLUR?

#Akıllı sokak lambalarından gelen aşağıdaki bilgiler elimizde
#varm, moisture,charge
#ve yukarıdakileri kullanarak bazı hesaplamalar yapmak istiyoruz

(56 + 15) / 80
(17 + 45 ) / 70
(17 + 45 ) / 80
#tekrar eden işlemlerde fonk tanımlayıp onu çağırdık

#DRY
def calculate(varm, moistture, charge) :
    print((varm + moistture) / charge)

calculate(98, 12, 78)

#RETURN
#fonksiyon çıktılarını giridi olarak kullanmak için

def calculate(varm, moistture, charge) :
    print((varm + moistture) / charge)

calculate(98, 12, 78)
#yukarıdakini tanımladık

#calculate(98, 12, 78) * 10
#10 ile çarpmak istersek kızıyor ve şu mesaj veriliyor:
#TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'

#print yerine return kullandık ve o aşağıdaki return den sonraki ifadeyi döndürdü
def calculate(varm, moistture, charge) :
    return (varm + moistture) / charge
calculate(98, 12, 78) * 10
#return gördükten sonra kod çalışmayı keser

a = calculate(98, 12, 78) * 10

#1.Girilen argümanların yeni değerlerinin çıkması 2. Diğeri de 3 argüman üzerinden hesaplanan
#değerin çıktı olarak verilmesini istiyorum
def calculate(varm, moisture, charge) :
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (varm + moisture) / charge

    return varm, moisture, charge, output

calculate(98, 12, 78)
type(calculate(98, 12, 78))
#tuple

#sadece çağırmakla kalmayıp çıktılarını kaydedip daha sonra kullanmak istersek
varm, moisture, charge, output = calculate(98, 12, 78)
#özetle bir fonksiyonun çıktısını kullanmak istiyorsak return i kullanmamız gerek
#birden fazla çıktı olacaksa ve ben bunları saklamak istiyorsam 4 return olduğu için
#(varm, moisture, charge, output) bunları yazarak yanına calculate(98, 12, 78) yazdım

#FONKSİYON İÇERİSİNDEN FONKSİYON ÇAĞIRMAK

def calculate(varm, moistture, charge) :
    return int ((varm + moistture) / charge)

calculate(98, 12, 78) * 10

def standardization (a, p) :
    return a * 10 / 100 * p * p

standardization(45, 1)

def all_calculation (varm, moistture, charge , p) :
    a = calculate (varm, moistture, charge)
    b = standardization(a, p)
    print(b * 10)
#bu iki fonksiyonu çağırırken bu iki fonksiyonu da dışarıdan biçimlendirmek istiyorum
# a yı 3 argümanın hepsi ile
#p yi ise argümanlardan biri ile biçimlendirmek istiyorum

#1.def all_calculation fonksiyonu tanımlanmıs
#Bu fonksiyona 4 tane argüman verilmiş
#Bu argümanlardan 3 tanesi a = calculate (varm, moistture, charge) burada kullanılıyor
#ki o da bir fonksiyon (fonk tanımlanması esnasında daha önce olan bir fonk çağırdım)

all_calculation(1, 3, 5, 12)

def all_calculation (varm, moistture, charge ,a,  p) :
    print (calculate (varm, moistture, charge))
    b = standardization(a, p)
    print(b * 10)

all_calculation(1, 3, 5, 19, 12)

#LOCAL VE GLOBAL DEĞİŞKENLER (Local & Global Variables)

list_store = [1, 2]
#Liste olduğunu köşeli parantezden anlıyoruz yada bunu çalıştırktan sonra type yazarsak anlarız

#fonk görevi 2 sayıyı çarpmak ve bu sayıyı yukarıdaki listeye eklemek
    def add_element(a, b):
        c = a * b
        list_store.append(c)
        print(list_store)

#list_store : global etki alanında var olan bir değişken
#Her yerden erişebiliriz

add_element(1, 9)
    #c lokal etki alanında olduğu için global etki alanını ifade eden bu bölümde göremiyoruz add_element kısmında
#Örneğimiz lokal etki alanından global etki alanını etkilemek


#KOŞULLAR (CONDITIONS)
#Bir program yazılımı esnasında akış kontrolü sağlayan ve programların belirli kurallara göre yada
# koşullara göre nasıl hareket edilmesi gerektiğini biz kullanıcılar tarafından programlara
# bildirme imkanı sağlayan yapılardır

#True -False
1 == 1
1 == 2

#if
#Buradan türemesi gereken şeyin true yada false olması durumudur
if 1==1 :
    print('something')

#if (Sadece if kullanıldığında) ancak işlemin sonucu true olursa buradaki bloktaki işlemi yapar
if 1==2 :
    print('something')

#buradan true sonucu çıkmadığı için çalışmadı
#(eğer koşul sağlanıyorsa şunu yap)
number =  11
if number == 10 :
    print('number is 10')

number =  20
number =  10

#11 yazdık 20 yazdık 10 yazdık kendimizi tekrarladık-DRY prensipi
#Bu yüzden fonksiyon tanımladık

def number_check(number) :
if number == 10 :
    print('number is 10')

number_check (10)
#number is 10 yazdı

number_check (12)
#Bilgi gelmedi

#else kullanımı
def number_check(number) :
    if number == 10 :
        print('number is 10')
    else :
        print ('number is not 10')

number_check (12)

#if ve else in etki alanlarında farklı işlemler de yapabiliriz

#elif#
#Bir sayının 10 a eşit olması , 10 dan büyük olması yada 10 dan küçük olması durumu olan bu 3 durumu
#göz önünde bulundurarak bir numara kontrolü yapmak istediğimizi düşünelim

def number_check(number) :
    if number > 10 :
        print ('greater than 10')
    elif number < 10 :
        print ('less than 10')
    else :
        print ('equal to 10')

number_check (1)

#değilse ama küçükse-sorgulamak istediğimiz koşul 2 den fazla ise elif kullanırız

#DÖNGÜLER (LOOPS)

#For Loop#
    #Üzerinde iterasyon yapılabilen , nesneler üzerinde gezinmeyi ve bu gezinmeler sonucunda
    #yakalamış olacağımız her bir elaman üzerinde çeşitli işlemler yapma imkanı sağlar

students = ['John', 'Mark', 'Venessa', 'Mariam']
students[0]
students[1]
students[2]

#Yukarıdaki işlemi döngü aracılığı ile yapacağız
#1. Döngüyü nerede gerçekleştireceğiz:
#2. Her bir elemanı bir şeyle temsil etme

for student in students :
    print (student)
#student isimlendirmesini istediğimiz gibi yapabiliriz

#Yakalamak istediğimiz her öğrencinin ismini büyük harfle yazdırmak istersek

for student in students :
    print (student.upper())

#Başka örnek

for salary in salaries :
    print (salary)

salaries = [1000, 2000, 3000, 4000]

#maaşlara %20 zamn uygulamak istersek

for salary in salaries :
    print (salary*20/100 + salary)

#integer olarak gelsin istersek

for salary in salaries :
    print(int(salary*20/100 + salary))

#zam % 30 olursa

for salary in salaries :
    print(int(salary*30/100 + salary))

#zam % 50 olursa

for salary in salaries :
    print(int(salary*50/100 + salary))

#DRY Prensipi
#2 argüman var 1.salary ve 2.rate

def new_salary(salary, rate) :
    return int(salary*rate/100 + salary)

new_salary(1500, 10)

#Bütün maaşlara %10 zam uygulattık
for salary in salaries :
    print (new_salary(salary, 10))

#Genel fonk olusturduk bu yuzden farklı maaş listesi de deneybiliriz

salaries2 = [10030, 20400, 30200, 40100]
for salary in salaries2 :
    print (new_salary(salary, 20))
#Hem döngü, hem fonk , hem de fonk nun 2 argümanı var

#Maaşı 3000 ve üzeri olana 10 zam, 3000 altı olana 20 zam

salaries = [1000, 2000, 3000, 4000]

for salary in salaries :
    if salary >= 3000 :
        print(new_salary(salary,10))
    else :
        print (new_salary(salary, 20))


#UYGULAMA MÜLAKAT SORUSU-Alternating
#############
#AMAÇ : Aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz

#before : 'hi my name is john and i am learning python'
#after: 'Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN'

#Yani girilen string ifadelerin çift indexli harflerini büyük harfle yaz, tek indexli olanlar küçük harf
#kalacak

#Çift yada tek indekslerde gezmemiz gerek( Önce tüm indeksleri sorgulamak ve sonra çift yada teke göre
#işlem yapmak ve onları(yaptıkça) kaydetmek mantıklı olacak

range(len('miuul'))
#range 2 değer arasında sayı üretme imkanı sağlar (range(0, 5) olarak döndü üstteki sorgu)

range(len('miuul'))
range(0, 5)

for i in range(len('miuul')) :
    print(i)

def alternating(string) :
    new_string = ''
#new_string = '' yapılan değişiklikleri kaydetmek istediğimiz yer

#Girilen string ifadenin tüm indexlerini gezebiliyoruz

def alternating(string) :
    new_string = ''
    for string_index in range(len(string)) :
    print(string_index)

#string_index % 2 == 0: (2 ye bölümünden kalan 0 demek-çift index)
#new_string += ile daha önce oluşturduğumuz boş string e değer ekledik, daha sonra bu string in değerini
#bu eklemiş olduğumuz değerle beraber güncel hali olarak güncelledik

def alternating(string) :
    new_string = ''
    for string_index in range(len(string)) :
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        else :
            new_string += string[string_index].lower()

#4 % 2 == 0
#m = 'miuul'
# m[0]


#Boş bir string oluşturduk (new_string = '')
#range(len(string)) dendiğinde örn 'miuul' içim şu döndü range(0,5)
#for string_index in range(len(string)) : ile tüm indexleri geziyoruz
# if string_index % 2 == 0: (2 ye bölümünden kalan 0 mı evet)- upper yaptık
#2 ye bölümden kalan 0 değilse-lower yaptık

#!buna bek benim dönüşte rakam geliyor :(
def alternating(string) :
    new_string = " "
    #girilen string in indexlerinde gez
    for string_index in range(len(string)) :
        if string_index % 2 == 0:
            # += ilgili ifadeyi ekle ve yeni değeri olarak mevcut hali koru demek
            new_string += string[string_index].upper()
        else :
            new_string += string[string_index].lower()
    print(string_index)

alternating("miuul")

#Break & Continue & While
#############
#Döngülerle birlikte kullanılan bu yapılar bir program akışında akışı kesmeye yada
# ilgili şart gözlemlendiğinde o şartı atlayarak devam etmeye yada
#bir koşul sağlandığı sürece çalışmayı sürdürmeye yarayan ifadelerdir

salaries = [1000, 2000, 3000, 4000]

#Break : Bir aranan koşul yakalandığında döngünün durmasını sağlar
for salary in salaries :
    if salary == 3000 :
        break
    print (salary)

#Continue : Aranan koşulu atladı
for salary in salaries :
    if salary == 3000 :
        continue
    print (salary)

#While:-dığı sürece döngüsü, bir şart sağlandığı sürece çalışmayı sürdürür

number = 1
while number < 5 :
    print(number)
    number += 1 #yeni değere 1 ekleyerek gitti ve sonuç 1,2,3,4 geldi

number = 1
while number < 5 :
    print(number)
    number += 1

number = 1
while number < 5 :
    print(number)
    number += 1
break


#ENUMERATE : Otomatik counter/Indexer ile for loop
############
#Bir iteratif nesne içinde gezip elemanlarına bir şey yaparken aynı zamanda o elemanların
#index bilgilerini de takip etmek istediğimizde kullanılır

students = ['John', 'Mark', 'Venessa', 'Mariam']
#Diyelim ki bu öğrenci listesinde gezmek istiyoruz
#Indexi çift olanlara bir işlem tek olanlara başka bir işlem yapmak istediğimizi düşünelim

for student in students :
    print(student)

#bu sorgu ile elimizde index yok

for index, student in enumerate(students,1) :
    print(index, student)

for index, student in enumerate(students) :
    print(index, student)
#çıkan sonuç :
#0 John
#1 Mark
#2 Venessa
#3 Mariam
#normade 0 dan başlıyor, başlangıç değerini değiştirmek istersek:
#for index, student in enumerate(students,1) : yazabiliriz ama genelde biçimlendirmiyoruz
    #print(index, student)

A = []
B = []

for index, student in enumerate(students) : #students listesinde geziyorum, gezerken enumarete bana
    #hem öğrencileri temsil etme hem de öğrencilerin liste içerisindeki indexlerini temsil etme
    #imkanı veriyor
    if index % 2 == 0 :
        A.append(student) #Böylece eş zamanlı olarak gezdiğim hem öğrenciler hem de indexlere göre
        #indexler üzerinde bazı işlemler yapabiliyorum
    else :
        B.append (student)
#Eğer yakaladığın 0 1 2 3 indexlerinden birinin 2 ye bölümünden kalan 0 ise A listesine ekle,
#değilse b listesine ekle

#UYGULAMA MÜLAKAT SORUSU#
############
#divide_students fonksiyonu yazınız
#Çift indexte yer alan öğrencileri bir listeye alınız
#Tek indexte yer alan öğrencileri başka bir listeye alınız
#Fakat bu iki liste tek bir liste olarak return olsun

students = ['John', 'Mark', 'Venessa', 'Mariam']

def divide_students (students) :
    groups = [[], []] #öğrencilere işlem yaptıktan sonra bu grup listesinin içerisindeki indexlere
    #göre yer alan listelere eleman göndereceğim
for index, student in enumerate(students) :
    if index % 2 == 0 :
        groups [0].append (student)# 0. indexteki elemanı ekle
    else
        groups [1].append (student)
    print (groups)
    return groups #işlenebilir şekilde return etsin

#yani
students = ['John', 'Mark', 'Venessa', 'Mariam']

def divide_students(students) :
    groups = [[],[]]
    for index, student in enumerate(students) :
        if index %2 == 0 :
            groups [0].append(student)
        else :
            groups[1].append(student)
    print(groups)
    return(groups)

divide_students(students)
st = divide_students(students)
st[0] #Out[8]: ['John', 'Venessa']
st[1] #Out[9]: ['Mark', 'Mariam']

#ALTERNATING FONKSIYONUNUN ENUMARETE ILE YAZILMASI
#AMAÇ : Aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz

#before : 'hi my name is john and i am learning python'
#after: 'Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN'

#Yani girilen string ifadelerin çift indexli harflerini büyük harfle yaz, tek indexli olanlar küçük harf
#kalacak

def alternating_with_enumerate(string) :

#kendisinde gezip elemanları değiştireceğiz, indexinde gezelim tek mi çift mi olduğunu anlayalım

def alternating_with_enumerate(string) :
    new_string = ''
    for i, letter in enumerate(string):
        if i %2 ==0 :
            new_string += letter.upper()
        else :
            new_string += letter.lower()
    print(new_string)


#ZIP#
######
#aşağıdaki 3 farklı listenin elemanlarını eşlemek istiyoruz

students = ['John', 'Mark', 'Venessa', 'Mariam']
departmants = ['mathematics', 'statistics', 'physics', 'astronomy']
ages = [23, 30, 26, 22]

#genel çıktının liste olmasını istiyoruz
list (zip(students, departmants, ages))
#Bir liste içinde tuple formatında bu üç ayrı listeyi bir araya getirerek birleştirdi
#[('John', 'mathematics', 23),
 #('Mark', 'statistics', 30),
 #('Venessa', 'physics', 26),
 #('Mariam', 'astronomy', 22)]
 #aynı sırada bir araya getirdi

 #LAMBDA & MAP & FILTER &REDUCE
 #####
 #vektör seviyesinde
 #Lambda : Fonk tanımla şekli-önemli
 #(Lambda en fazla apply fonk ile birlikte kullanılıyor)-Öğreneceğiz
 #map : Önemli

 #Lambda
 ######
 def summer (a, b) :
     return a + b
 summer(4, 5)

 summer(1, 3) * 9

new_sum = lambda a, b  : a + b
new_sum(4, 5)

#lambda nın def den farkı kullan at fonk olması
#apply map gibi lerle kullanıldığında kullan-at özelliği kullanılıyor
#Special variables da yer tutmaz

#map#
#########
salaries = [1000, 2000 , 3000, 4000, 5000]
#zam uyguladık
def new_salary(x) :
    return x * 20 / 100 + x
new_salary (5000)

for salary in salaries :
    print(new_salary(salary))

# Liste olmasını istedik
#new salary fonk salaries e mapledi-döngü yazmaya gerek kalmadı
list(map(new_salary, salaries))

#lambda & map ilişkisi#
#########

list(map(lambda x: x * 20 / 100 + x, salaries))
#del new_sum

#gelen değerlerin karesini alsın
list(map(lambda x: x ** 2 , salaries))

#Filter#
########
#(Kullanım sıklığı düşük)
#Fonk tanımladık, çıktı liste formatında olacak- 2 ye bölümünden kalan 0 mı sorgusunu yapar
#sorgu noktası gibi-filter döngü yazmaya gerek olmadan iteratif bir liste üzerinde gezecek
#her listedeki elemana soraca

list_store = [1, 2, 3, 4, 5, 6, 7,  8, 9 ,10]
list(filter(lambda x : x % 2 == 0, list_store))

#Reduce#
####

#functools içerisinden reduce metodunu, fonksiyonunu import ediyoruz

from functools import reduce
list_store = [1, 2, 3, 4]
#iteratif elemanlara tek tek belirli bir işlemi uygulamak istiyoruz
#lambda ile peş peşe elemanları ekle dedik-sonuç 10

from functools import reduce
list_store = [1, 2, 3, 4]
reduce(lambda a, b : a + b , list_store)

#Reduce ve filter için çok zaman harcama

QUIZ
#1
sayi = 10
for num in range(0, sayi):
                if num %2 == 0:
                             print(num)

#2
sayi = 10

if sayi % 2 == 0:
    print("Sayı çifttir")
    break



#COMPREHENSIONS
#####################################

#LIST COMPREHENSION--!!!!ÖNEMLİ BİR KONU
#birden fazla satır ve kod ile yapılabilecek işlemleri kolayca istediğimiz çıktı veri yapısına göre
#tek bir satırda gerçekleştirme imkanı sağlayan yapılardır

#Bir liste üzerinde gezip bu elemanlara çeşitli işlemler uygulayalım
#Daha sonra işlem uygulanmış elemanları tekrar bir listede görmek istediğimizde burada peş peşe
#bir çok işlem yapmamız gerekmektedir(boş liste oluştur-varolan liste içinde gez- elemanlara işlem
#yap ( belk birden fazla) belki if else ekle koşulla yap işlem içerisindeki elemanları belirli
#bir liste içine tekrar koy gibi

salaries = [1000, 2000 , 3000, 4000, 5000]

def new_salary (x) :
    return x * 20 / 100 + x

for salary in salaries :
    print(new_salary(salary))

bunları listede saklamak için:

null_list = []

for salary in salaries :
    null_list.append(new_salary(salary))

#sonuç : [1200.0, 2400.0, 3600.0, 4800.0, 6000.0]

null_list = []

for salary in salaries :
    if salary > 3000 :
        null_list.append(new_salary(salary))
    else :
        null_list.append(new_salary(salary * 2))

#sonuç : [2400.0, 4800.0, 7200.0, 4800.0, 6000.0]

#List comprehension ile aynı örneği yapalım

[new_salary(salary * 2) if salary < 3000 else new_salary(salary)  for salary in salaries]

#liste ile başlar []
#[for salary in salaries]--yakaladığım maaşları ne yapayım

#[salary * 2 for salary in salaries]--2 ile çarp dedik
[salary * 2 for salary in salaries]
#[2000, 4000, 6000, 8000, 10000]

#maaşı 3000 den az olanları getirelim-else ile kullanmadık if sağda yazılır
[salary * 2 for salary in salaries if salary < 3000 ]
#[2000, 4000]

#maaşı 3000 den büyükse-else ile kullandık for en sağda kaldı
[salary * 2  if salary < 3000 else  salary * 0 for salary in salaries]
#maaşlarda gez-yakaladığın maaşa bak -eğer 3000 den küçükse salary * 2 yap değilse * 0
#[2000, 4000, 0, 0, 0]

#new_Salary i uygulamak istiyoruz
[new_salary(salary * 2 ) if salary < 3000 else  salary * 0 for salary in salaries]
#[2400.0, 4800.0, 0, 0, 0]

[new_salary(salary * 2 ) if salary < 3000 else  new_salary(salary * 0.2) for salary in salaries]
#[2400.0, 4800.0, 720.0, 960.0, 1200.0]
#Hem döngü hem if-else bloğu- hem de belirli bir fonk u bu döngü elemanlarına uygulamayı kolaylıkla yaptık

[new_salary(salary * 2)  if salary < 3000 else new_salary(salary * 0) for salary in salaries ]


#1.liste istediğim öğrenciler 2.liste istemediğim öğrenciler
#Bu istemediğim öğrenciler listesinde olan öğrencilerin isimlerini küçük
#burada olmayan isimleri büyük harfle düzelt

students = ['John', 'Mark', 'Venessa', 'Mariam']

students_no = ['John', 'Venessa']

[student.lower() if student in students_no else student.upper() for student in students]
#['john', 'MARK', 'venessa', 'MARIAM']
[student.upper () if student not in students_no else student.lower() for student in students]

#DICT COMPREHENSIONS###
######

dictionary = {'a' : 1,
              'b' : 2,
              'c' : 3,
              'd' : 4}

dictionary.keys()
#dict_keys(['a', 'b', 'c', 'd'])

dictionary.values()
#dict_values([1, 2, 3, 4])

dictionary.items()
#dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

#Sözlük içindeki her bir value nin karesini almak istiyoruz

{k : v ** 2 for (k, v) in dictionary.items()}
#{'a': 1, 'b': 4, 'c': 9, 'd': 16}

{k.upper() : v  for (k, v) in dictionary.items()}
#{'A': 1, 'B': 2, 'C': 3, 'D': 4}

{k.upper() : v **2  for (k, v) in dictionary.items()}
#{'A': 1, 'B': 4, 'C': 9, 'D': 16}

#UYGULAMA MÜLAKAT SORUSU-DICT COMPREHENSIONS
###

#AMAÇ :Çift sayıların karesi alınarak bir sözlüğe eklenmek istenmektedir
#Key ler orijinal değerler value ler ise değiştirilmiş değerler olacak

numbers = range(10)
new dict = {}

for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2
        #bu değerin kendisini key bölümüne ekliyorum,bu sayının karesini value bölümüne
        #ekliyorum-elemanları gezilen numbers içerisindeki n lere bir işlem yapmadık

numbers = range(10)
new_dict = {}

for n in numbers:
    if n % 2 == 0 :
        new_dict[n] = n ** 2

new_dict
#{0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

{n : n ** 2 for n in numbers if n %2 == 0 }
#{0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

#LIST & DIC COMPREHENSION UYGULAMALAR-1
#######

#BİR VERİ SETİNDEKİ DEĞİŞKEN İSİMLERİNİ DEĞİŞTİRMEK

#before :
#['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev']

#after :
# ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']

#Bunlar bir dataframe in değişkenlerinin isimleri
#DATAFRAME : Pandas modülünün , paketinin , kütüphanesinin bir veri yapısıdır
#Birbirinden farklı tiplerdeki verileri tutma imkanı sağlar

#seaborn kütüphanesini import ediyoruz-kütüphane import etme şekli
#BİLGİ AMAÇLI GÖRÜYORUZ ŞU AN##
import  seaborn as sns # Bu kütüphaneyi şu şekilde temsil et
df = sns.load_dataset('car_crashes') # seaborn kütüphanesi içinden 'car_crashes' veri setini getir diyerek
#df şeklinde kaydediyoruz
df.columns # ilgili dataframe in değişkenlerinin ismi gelir
#Index(['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous',
#       'ins_premium', 'ins_losses', 'abbrev'],
 #     dtype='object')

import  seaborn as sns
df = sns.load_dataset ('car_crashes')
df.columns

#df çağırdık
#df bir dataframe-veri çerçevesi- excel tarzında veri tutmak gibi
#total  speeding  alcohol  ...  ins_premium  ins_losses  abbrev
#0    18.8     7.332    5.640  ...       784.55      145.08      AL
#1    18.1     7.421    4.525  ...      1053.48      133.93      AK
#2    18.6     6.510    5.208  ...       899.47      110.35      AZ
#3    22.4     4.032    5.824  ...       827.34      142.39      AR
#4    12.0     4.200    3.360  ...       878.41      165.63      CA
#5    13.6     5.032    3.808  ...       835.50      139.91      CO

for col in df.columns :
    print (col)

#bütün isimleri tek tek ekrana yazdırdı
#total
#speeding
#alcohol
#not_distracted
#no_previous
#ins_premium
#ins_losses
#abbrev

for col in df.columns :
    print (col.upper ())
#Harfleri büyüttük

#Bunları kalıcı bir şekilde dataframe e yansıtmamız lazım

A = []

for col in df.columns :
    A.append(col.upper())

df.columns = A
#Index(['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS',
 #      'INS_PREMIUM', 'INS_LOSSES', 'ABBREV'],
  #    dtype='object')


import  seaborn as sns
df = sns.load_dataset ('car_crashes')
df.columns

A = []

for col in df.columns :
    A.append(col.upper())

df.columns = A

#Sonuç : Ek bir modül indirmedik, tek bir modül indirme işlemi yaptık. Bunun da sebebi veriye hızlı bir
#şekilde erişmek için
#seaborn modülünü getirdi, içindeki veriye eriştik
#Veri ile işimiz yok değişkenlerin isimlerini çektik

#BUNU LIST COMPRHENSION ILE NASIL YAPARIZ

#önce veri setini baştan okuttuk
df = sns.load_dataset('car_crashes')
df.columns = [col.upper () for col in df.columns]#Index(['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS',
       'INS_PREMIUM', 'INS_LOSSES', 'ABBREV'],
      dtype='object')

df = sns.load_dataset('car_crashes')
df.columns = [col.upper () for col in df.columns]

import  seaborn as sns
df = sns.load_dataset ('car_crashes')
df.columns

df.columns = [col.upper () for col in df.columns]

#bunlara tekrar et!!

#LIST & DIC COMPREHENSION UYGULAMALAR-2
#######

#İSMİNDE 'INS' OLAN DEĞİŞKENELRİN BAŞINA FLAG DİĞERLERİNE NO_FLAG EKLEMEK İSTİYORUZ

#before :
#['TOTAL',
#'SPEEDING',
#'ALCOHOL',
#'NOT_DISTRACTED',
#'NO_PREVIOUS',
#'INS_PREMIUM',
#'INS_LOSSES',
#'ABBREV' ]

#after :
#['NO_FLAG_TOTAL',
#'NO_FLAG_SPEEDING',
#'NO_FLAG_ALCOHOL',
#'NO_FLAG_NOT_DISTRACTED',
#'NO_FLAG_NO_PREVIOUS',
#'FLAG_INS_PREMIUM',
#'FLAG_INS_LOSSES',
#'NO_FLAG_ABBREV' ]

#LIST COMPREHENSION

#kolonlarda gez eğer içinde INS varsa
#INS yoksa olduğu gibi yazacak

[col for col in df.columns if 'INS' in col]
#Out[93]: ['INS_PREMIUM', 'INS_LOSSES']

#Kolonlarda gez eğer içerisinde INS varsa bunun basına FLAG_ ekle
#col : her bir kolonu, sütunu temsil eder-string
['FLAG_ ' + col for col in df.columns if 'INS' in col]
#ut[94]: ['FLAG_ INS_PREMIUM', 'FLAG_ INS_LOSSES']

#kolon isimlerinde gez -eğer INS ifadesi bu kolonun içerisinde ise FLAG_ ekle
# yoksa NO-FLAG yaz -yine bu col string ifadesiyle bunu birleştir

['FLAG_ ' + col if 'INS' in col else 'NO_FLAG' + col for col in df.columns ]

#kalıcı hale getirmek için
df.columns = ['FLAG_ ' + col if 'INS' in col else 'NO_FLAG' + col for col in df.columns ]
#Index(['NO_FLAGTOTAL', 'NO_FLAGSPEEDING', 'NO_FLAGALCOHOL',
#       'NO_FLAGNOT_DISTRACTED', 'NO_FLAGNO_PREVIOUS', 'FLAG_ INS_PREMIUM',
#      'FLAG_ INS_LOSSES', 'NO_FLAGABBREV'],
#     dtype='object')

#LIST & DIC COMPREHENSION UYGULAMALAR-3
#######

#Amaç key string i, value su aşağıdaki gibi bir liste olan sözlük oluşturmak
#sadece sayısal değişkenler için yapmak istiyoruz

#liste ve liste içinde çeşitli fonksiyon isimleri var
#Output :
# {'total' : ['mean', 'min', 'max', 'var' ],
# 'speeding' : ['mean', 'min', 'max', 'var' ],
# 'alcohol ' : ['mean', 'min', 'max', 'var' ],
# 'not_distracted' : ['mean', 'min', 'max', 'var' ],
# 'no_previous' : ['mean', 'min', 'max', 'var' ],
# 'ins_premium' : ['mean', 'min', 'max', 'var' ],
# 'ins_losses' : ['mean', 'min', 'max', 'var' ]}

#1.VERIYI OKUYORUZ
#sns olarak isimlendirdik
#bu kütüphaenin içerisindeki load_dataset fonksiyonunu  kullanarak veri setini yükledik

import seaborn as sns
df = sns.load_dataset ('car_crashes')
df.columns
#Index(['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous',
      # 'ins_premium', 'ins_losses', 'abbrev'],
      #dtype='object')

#sadece sayısal değişkenleri veri seti içinden çekmemiz gerek

num_cols = [col for col in df.columns] # değişkenlerde gezdik
num_cols = [col for col in df.columns df[col]] # bu dataframe içerisinden ilgili değişkeni seç
num_cols = [col for col in df.columns df[col].dtype != 'O'] #eşit değildir object isimlendirmesi
#yaptığımızda bu veri setinin içerisinde object olmayan tipteki değişkenleri seçmiş olacak

num_cols = [col for col in df.columns if df[col].dtype != 'O']
#herhangi bir metoda gerek kalmadan bir dataframe in içerisindeki sayısal değişkenleri seçtik

#1.for col in df.columns -değişkenlerin isimlerinde gez
#2.Bir değişkeni yakaladığında (df[col].dtype != '0') örn no_previous'-bu değişkenin ismini yazdığımızda
#bu değişkeni dataframe içerisinden seçer-tipine bak-O:Object i yani kategorik değişkenleri temsil eder
#kategorik olmayanlara ifade etmek için != '0' kullandık (== demedik :string tiptekileri getirir
# biz numerik istiyoruz)

num_cols = [col for col in df.columns if df[col].dtype != 'O']
soz = {}
agg_list = ['mean', 'min', 'max', 'var' ]

for col in num_cols : #num_cols numerik kolonlarda geziyoruz
    soz [col]= agg_list #bu sözlüğe köşeli parantez ile sutunları ekliyoruz, bunlar değişken num_cols dan geliyor
#sol taraf dinamik sağ taraf sabit olacak-sütunlarda geziyoruz-key değerine köşeli parantez ile
# = diyip value bölümlerine sabit bir liste giriyoruz

for col in num_cols :
    soz [col] = agg_list
soz
#Sonuca ulaştık

#KISA YOL
{col : agg_list for col in num_cols} # key :col (dinamik) , value :agg_list (sabit)-num_cols da gezdik

{col : agg_list for col in num_cols}

#sol taraftaki key lerin değişken isimleri var-bu bir dataframe in içerisindeki değişkenlerin isimleri
#total,speeding,..vs-exceldeki sütunların isimleri gibi-bunların altında değerler var

eski_fiyat = {'süt': 1.02, 'kahve': 2.5, 'ekmek': 2.5}
eski_fiyat.items()
#dict_items([('süt', 1.02), ('kahve', 2.5), ('ekmek', 2.5)])


df.head () #bir dataframe in ilk gözlemlerine erişme metodu
#----------

new_dict = {col : agg_list for col in num_cols}

#dataframe içinden nümerik columns seçeceğiz
#numcols içinde sayısal değişkenler var

df[num_cols].head () # eğer bir dataframe e [] girdikten sonra bir değişken listesi verirsek bu dataframe
#içinden o değişkenleri seçer


df[num_cols].head ()


df[num_cols].agg(new_dict) # aggregation a bu şekilde bir sözlük gönderirsek ve agg bu şekilde bir dataframe
#uygularsak gödnerdiğiniz sözlüğün içerisindeki değişkenler eğer buradaki dataframa de varsa (ki var)
#bu değişkenleri key bölümünden tutar value bölümüne girdiğiniz bütün fonksiyonları gidip bu
#değişkenlere otomatik olarak uygular

df[num_cols].aggregate(new_dict)
#Belirli bir dataframe deki bütün değişkenlere isteeybileceğiniz bir fonk setini çok kolay bir hamlede
#dict comprehension yapısı sayesinde biçimlendirmeler gerçekleştirerek bunalrı göndermiş olduk

