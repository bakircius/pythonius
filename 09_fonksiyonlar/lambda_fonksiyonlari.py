# Lambda Fonksiyonları ve Anonim Fonksiyonlar
# Python lambda fonksiyonlarının detaylı incelenmesi

print("=== LAMBDA FONKSİYONLARI VE ANONİM FONKSİYONLAR ===\n")

print("1. LAMBDA SÖZDİZİMİ VE TEMEL KULLANIM:")
print("-" * 38)

# Basit lambda sözdizimi: lambda arguments: expression
# Normal fonksiyon
def kare_normal(x):
    return x ** 2

# Lambda ile aynı işlev
kare_lambda = lambda x: x ** 2

print(f"Normal fonksiyon: {kare_normal(5)}")
print(f"Lambda fonksiyon: {kare_lambda(5)}")

# Çoklu parametre
toplam = lambda x, y: x + y
print(f"Toplam (3, 4): {toplam(3, 4)}")

# Üç parametre
uclu_toplam = lambda x, y, z: x + y + z
print(f"Üçlü toplam (1, 2, 3): {uclu_toplam(1, 2, 3)}")

# Karmaşık ifadeler
max_lambda = lambda x, y: x if x > y else y
print(f"Max (5, 8): {max_lambda(5, 8)}")

# String işlemleri
buyut = lambda s: s.upper()
print(f"Büyült 'python': {buyut('python')}")

# Liste işlemleri
liste_uzunluk = lambda lst: len(lst)
print(f"Liste uzunluğu [1,2,3,4]: {liste_uzunluk([1, 2, 3, 4])}")

print("\n2. LAMBDA İLE VARSAYILAN PARAMETRELER:")
print("-" * 36)

# Varsayılan değerli lambda
selamla = lambda isim="Dünya": f"Merhaba {isim}!"
print(selamla())
print(selamla("Python"))

# Çoklu varsayılan parametre
hesapla = lambda x, y=2, z=3: x * y + z
print(f"hesapla(5): {hesapla(5)}")  # 5 * 2 + 3 = 13
print(f"hesapla(5, 3): {hesapla(5, 3)}")  # 5 * 3 + 3 = 18
print(f"hesapla(5, 3, 10): {hesapla(5, 3, 10)}")  # 5 * 3 + 10 = 25

# Keyword arguments ile lambda
format_lambda = lambda isim, yas=25: f"{isim} {yas} yaşında"
print(format_lambda("Ali"))
print(format_lambda("Veli", yas=30))

print("\n3. MAP() FONKSİYONU İLE LAMBDA:")
print("-" * 32)

# map() temel kullanım
sayilar = [1, 2, 3, 4, 5]
kareler = list(map(lambda x: x ** 2, sayilar))
print(f"Sayılar: {sayilar}")
print(f"Kareler: {kareler}")

# String işlemleri
kelimeler = ["python", "java", "go", "rust"]
buyuk_kelimeler = list(map(lambda s: s.upper(), kelimeler))
print(f"Kelimeler: {kelimeler}")
print(f"Büyük kelimeler: {buyuk_kelimeler}")

# Çoklu liste ile map
liste1 = [1, 2, 3, 4]
liste2 = [10, 20, 30, 40]
toplam_listesi = list(map(lambda x, y: x + y, liste1, liste2))
print(f"Liste1: {liste1}")
print(f"Liste2: {liste2}")
print(f"Toplamları: {toplam_listesi}")

# Üç liste ile
liste3 = [100, 200, 300, 400]
uclu_toplam_listesi = list(map(lambda x, y, z: x + y + z, liste1, liste2, liste3))
print(f"Üç liste toplamı: {uclu_toplam_listesi}")

# Kompleks dönüşümler
kisi_listesi = ["ali veli", "ayşe yılmaz", "mehmet öz"]
isim_format = list(map(lambda s: s.title(), kisi_listesi))
print(f"Formatlanmış isimler: {isim_format}")

# Dictionary ile map
sozluk_listesi = [{"isim": "Ali", "yas": 25}, {"isim": "Veli", "yas": 30}]
isim_listesi = list(map(lambda d: d["isim"], sozluk_listesi))
print(f"İsim listesi: {isim_listesi}")

print("\n4. FILTER() FONKSİYONU İLE LAMBDA:")
print("-" * 34)

# filter() temel kullanım
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ciftler = list(filter(lambda x: x % 2 == 0, sayilar))
print(f"Sayılar: {sayilar}")
print(f"Çift sayılar: {ciftler}")

# Tek sayılar
tekler = list(filter(lambda x: x % 2 != 0, sayilar))
print(f"Tek sayılar: {tekler}")

# Pozitif sayılar
karma_sayilar = [-3, -1, 0, 1, 2, 3, 4, -5]
pozitifler = list(filter(lambda x: x > 0, karma_sayilar))
print(f"Karma sayılar: {karma_sayilar}")
print(f"Pozitif sayılar: {pozitifler}")

# String filtreleme
kelimeler = ["python", "java", "go", "javascript", "c++"]
uzun_kelimeler = list(filter(lambda s: len(s) > 4, kelimeler))
print(f"Kelimeler: {kelimeler}")
print(f"Uzun kelimeler (>4 harf): {uzun_kelimeler}")

# Büyük harfle başlayanlar
metinler = ["Python", "java", "Go", "javascript", "C++"]
buyuk_harfli = list(filter(lambda s: s[0].isupper(), metinler))
print(f"Metinler: {metinler}")
print(f"Büyük harfle başlayanlar: {buyuk_harfli}")

# Kompleks filtreleme
sayilar = range(1, 101)
ozel_sayilar = list(filter(lambda x: x % 3 == 0 and x % 5 != 0, sayilar))
print(f"3'ün katları ama 5'in katları değil (1-100): {ozel_sayilar[:10]}...")

print("\n5. SORTED() FONKSİYONU İLE LAMBDA:")
print("-" * 33)

# Basit sıralama
sayilar = [3, 1, 4, 1, 5, 9, 2, 6]
sirali = sorted(sayilar, key=lambda x: x)  # Normal sıralama
print(f"Normal sıralama: {sirali}")

# Mutlak değere göre sıralama
karma_sayilar = [-5, 2, -1, 3, -4]
mutlak_sirali = sorted(karma_sayilar, key=lambda x: abs(x))
print(f"Karma sayılar: {karma_sayilar}")
print(f"Mutlak değere göre: {mutlak_sirali}")

# String uzunluğuna göre
kelimeler = ["python", "go", "javascript", "c", "java"]
uzunluk_sirali = sorted(kelimeler, key=lambda s: len(s))
print(f"Kelimeler: {kelimeler}")
print(f"Uzunluğa göre: {uzunluk_sirali}")

# Ters uzunluk sıralaması
ters_uzunluk = sorted(kelimeler, key=lambda s: len(s), reverse=True)
print(f"Ters uzunluk: {ters_uzunluk}")

# Tuple sıralama
ogrenciler = [("Ali", 85), ("Veli", 92), ("Ayşe", 78)]
nota_gore = sorted(ogrenciler, key=lambda x: x[1])
print(f"Öğrenciler: {ogrenciler}")
print(f"Nota göre: {nota_gore}")

# İkinci harfe göre sıralama
kelimeler = ["python", "java", "go", "rust"]
ikinci_harf = sorted(kelimeler, key=lambda s: s[1] if len(s) > 1 else '')
print(f"İkinci harfe göre: {ikinci_harf}")

# Dictionary sıralama
kisi_listesi = [
    {"isim": "Ali", "yas": 25, "not": 85},
    {"isim": "Veli", "yas": 20, "not": 92},
    {"isim": "Ayşe", "yas": 22, "not": 78}
]

yasa_gore = sorted(kisi_listesi, key=lambda x: x["yas"])
nota_gore = sorted(kisi_listesi, key=lambda x: x["not"], reverse=True)

print(f"Yaşa göre: {[k['isim'] for k in yasa_gore]}")
print(f"Nota göre: {[k['isim'] for k in nota_gore]}")

print("\n6. REDUCE() FONKSİYONU İLE LAMBDA:")
print("-" * 33)

from functools import reduce

# Toplam hesaplama
sayilar = [1, 2, 3, 4, 5]
toplam = reduce(lambda x, y: x + y, sayilar)
print(f"Sayılar: {sayilar}")
print(f"Toplam: {toplam}")

# Başlangıç değeri ile
toplam_baslangic = reduce(lambda x, y: x + y, sayilar, 100)
print(f"100 ile başlayarak toplam: {toplam_baslangic}")

# Çarpım hesaplama
carpim = reduce(lambda x, y: x * y, sayilar)
print(f"Çarpım: {carpim}")

# Maximum bulma
maksimum = reduce(lambda x, y: x if x > y else y, sayilar)
print(f"Maksimum: {maksimum}")

# String birleştirme
kelimeler = ["Python", "çok", "güçlü", "bir", "dil"]
cumle = reduce(lambda x, y: x + " " + y, kelimeler)
print(f"Kelimeler: {kelimeler}")
print(f"Cümle: {cumle}")

# Liste düzleştirme
ic_ice_liste = [[1, 2], [3, 4], [5, 6]]
duzlestirilmis = reduce(lambda x, y: x + y, ic_ice_liste)
print(f"İç içe liste: {ic_ice_liste}")
print(f"Düzleştirilmiş: {duzlestirilmis}")

# Karmaşık işlemler
sayilar = [1, 2, 3, 4, 5]
kare_toplami = reduce(lambda x, y: x + y**2, sayilar, 0)
print(f"Karelerin toplamı: {kare_toplami}")

print("\n7. LAMBDA İLE LIST COMPREHENSION KARŞILAŞTIRMA:")
print("-" * 47)

sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Kareler - map vs list comprehension
map_kareler = list(map(lambda x: x**2, sayilar))
comp_kareler = [x**2 for x in sayilar]
print(f"Map kareler: {map_kareler}")
print(f"Comprehension kareler: {comp_kareler}")

# Çiftler - filter vs list comprehension  
filter_ciftler = list(filter(lambda x: x % 2 == 0, sayilar))
comp_ciftler = [x for x in sayilar if x % 2 == 0]
print(f"Filter çiftler: {filter_ciftler}")
print(f"Comprehension çiftler: {comp_ciftler}")

# Kombinasyon - map+filter vs comprehension
map_filter = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, sayilar)))
comp_kombi = [x**2 for x in sayilar if x % 2 == 0]
print(f"Map+Filter: {map_filter}")
print(f"Comprehension kombi: {comp_kombi}")

# Performance karşılaştırması
import time

big_numbers = list(range(100000))

# Map performance
start = time.time()
map_result = list(map(lambda x: x**2, big_numbers))
map_time = time.time() - start

# List comprehension performance
start = time.time()
comp_result = [x**2 for x in big_numbers]
comp_time = time.time() - start

print(f"\n100.000 sayı için performans:")
print(f"Map: {map_time*1000:.2f} ms")
print(f"List comprehension: {comp_time*1000:.2f} ms")
print(f"Fark: {abs(map_time - comp_time)/min(map_time, comp_time)*100:.1f}%")

print("\n8. LAMBDA İLE HIGHER-ORDER FONKSİYONLAR:")
print("-" * 39)

# Fonksiyon döndüren lambda
carpan_olustur = lambda n: lambda x: x * n
iki_ile_carp = carpan_olustur(2)
uc_ile_carp = carpan_olustur(3)

print(f"2 ile çarp 5: {iki_ile_carp(5)}")
print(f"3 ile çarp 4: {uc_ile_carp(4)}")

# Fonksiyon kompozisyonu
kare = lambda x: x**2
iki_ekle = lambda x: x + 2

# f(g(x)) kompozisyonu
kompozit = lambda x: kare(iki_ekle(x))  # (x+2)²
print(f"(3+2)²: {kompozit(3)}")  # (3+2)² = 25

# Çoklu kompozisyon
f1 = lambda x: x + 1
f2 = lambda x: x * 2
f3 = lambda x: x ** 2

# f3(f2(f1(x)))
zincirleme = lambda x: f3(f2(f1(x)))  # ((x+1)*2)²
print(f"((2+1)*2)²: {zincirleme(2)}")  # ((2+1)*2)² = 36

# Koşullu fonksiyon seçimi
islem_sec = lambda op: (lambda x, y: x + y) if op == '+' else (lambda x, y: x * y)

toplama_func = islem_sec('+')
carpma_func = islem_sec('*')

print(f"Dinamik toplama 3+4: {toplama_func(3, 4)}")
print(f"Dinamik çarpma 3*4: {carpma_func(3, 4)}")

print("\n9. LAMBDA KAPSAMLARI VE CLOSURE:")
print("-" * 31)

# Closure ile lambda
def outer_function(x):
    return lambda y: x + y  # x'i closure ile yakalar

add_10 = outer_function(10)
add_5 = outer_function(5)

print(f"add_10(3): {add_10(3)}")  # 10 + 3 = 13
print(f"add_5(7): {add_5(7)}")    # 5 + 7 = 12

# Loop ile closure problemi
functions = []
for i in range(5):
    functions.append(lambda x: x + i)  # PROBLEM: i hep 4 olacak

print("Loop closure problemi:")
for j, func in enumerate(functions):
    print(f"  Func {j}: {func(1)}")  # Hepsi 1+4=5 verecek

# Doğru yöntem - default parameter
functions_correct = []
for i in range(5):
    functions_correct.append(lambda x, i=i: x + i)  # i'yi yakala

print("Düzeltilmiş version:")
for j, func in enumerate(functions_correct):
    print(f"  Func {j}: {func(1)}")

# Nested closure
def make_multiplier(n):
    return lambda x: lambda y: n * x * y

mult_2 = make_multiplier(2)
mult_2_3 = mult_2(3)  # 2 * 3 * y
print(f"2 * 3 * 4: {mult_2_3(4)}")  # 24

print("\n10. LAMBDA KULLANIM ALANLARI:")
print("-" * 28)

# Event handling simulation
events = []

# Event handlers as lambdas
on_click = lambda: print("Button clicked!")
on_hover = lambda: print("Mouse hover!")
on_key = lambda key: print(f"Key pressed: {key}")

event_handlers = {
    'click': on_click,
    'hover': on_hover,
    'keypress': on_key
}

# Simulate events
print("Event simulation:")
event_handlers['click']()
event_handlers['hover']()
event_handlers['keypress']('Enter')

# Data transformation pipeline
data = [1, 2, 3, 4, 5]

# Pipeline işlemleri
pipeline = [
    lambda x: x * 2,      # İkiyle çarp
    lambda x: x + 1,      # Bir ekle
    lambda x: x ** 2      # Karesi al
]

# Pipeline uygula
def apply_pipeline(data, pipeline):
    result = data
    for func in pipeline:
        result = list(map(func, result))
    return result

pipeline_result = apply_pipeline(data, pipeline)
print(f"Pipeline: {data} -> {pipeline_result}")

# Quick calculations
calculations = {
    'area_circle': lambda r: 3.14159 * r**2,
    'area_square': lambda s: s**2,
    'area_rectangle': lambda w, h: w * h,
    'volume_sphere': lambda r: (4/3) * 3.14159 * r**3
}

print(f"Daire alanı (r=5): {calculations['area_circle'](5)}")
print(f"Kare alanı (s=4): {calculations['area_square'](4)}")
print(f"Dikdörtgen alanı (3x5): {calculations['area_rectangle'](3, 5)}")

print("\n11. LAMBDA SINIRLAMALARI VE ALTERNATİFLER:")
print("-" * 40)

# Lambda yapamadıkları
print("Lambda YAPAMADIĞI şeyler:")
print("  • Statements (if, for, while, try, etc.)")
print("  • Multiple expressions")
print("  • Annotations")
print("  • Docstrings")

# Bu YAPILAMAZ:
# lambda x: if x > 0: return x  # SyntaxError!
# lambda x: for i in range(x): print(i)  # SyntaxError!

# Karmaşık logic için normal fonksiyon kullan
def complex_function(x):
    """Karmaşık işlem fonksiyonu"""
    if x < 0:
        return 0
    elif x == 0:
        return 1
    else:
        result = 1
        for i in range(1, x + 1):
            result *= i
        return result

print(f"Faktöriyel 5: {complex_function(5)}")

# Lambda'nın uygun olduğu durumlar
good_lambdas = [
    lambda x: x**2,                    # Basit matematik
    lambda s: s.strip().lower(),       # String işleme
    lambda d: d.get('key', 0),         # Dict erişimi
    lambda x, y: x + y,                # Basit operasyon
    lambda lst: len(lst) > 0           # Basit kontrol
]

# Lambda'nın uygun olmadığı durumlar - normal fonksiyon kullan
def validate_email(email):
    """Email validasyonu - çok karmaşık lambda için"""
    if not isinstance(email, str):
        return False
    if '@' not in email:
        return False
    parts = email.split('@')
    if len(parts) != 2:
        return False
    local, domain = parts
    if not local or not domain:
        return False
    return True

print(f"Email validation: {validate_email('user@example.com')}")

print("\n12. LAMBDA PERFORMANS VE BEST PRACTICES:")
print("-" * 40)

import time

# Performance comparison
def regular_square(x):
    return x**2

lambda_square = lambda x: x**2

# Test data
test_data = list(range(10000))

# Regular function
start = time.time()
regular_results = [regular_square(x) for x in test_data]
regular_time = time.time() - start

# Lambda function  
start = time.time()
lambda_results = [lambda_square(x) for x in test_data]
lambda_time = time.time() - start

# Map with lambda
start = time.time()
map_results = list(map(lambda x: x**2, test_data))
map_time = time.time() - start

print(f"10.000 eleman için performans:")
print(f"Regular function: {regular_time*1000:.2f} ms")
print(f"Lambda function: {lambda_time*1000:.2f} ms")
print(f"Map + lambda: {map_time*1000:.2f} ms")

# Best practices
print(f"\n✓ LAMBDA İYİ PRATİKLER:")
print("  • Basit, tek satır işlemler için kullan")
print("  • map(), filter(), sorted() ile birlikte kullan")
print("  • Event handling için uygun")
print("  • Quick calculations için ideal")

print(f"\n✗ LAMBDA KULLANMA:")
print("  • Karmaşık logic gerektiriyorsa")
print("  • Multiple statements gerekiyorsa")
print("  • Debugging gerekiyorsa")
print("  • Reusability önemliyse")
print("  • Docstring gerekiyorsa")

# Readability comparison
# KÖTÜ - okunması zor lambda
bad_lambda = lambda x: x**2 + 2*x + 1 if x >= 0 else (-x)**2 + 2*(-x) + 1

# İYİ - açık fonksiyon
def quadratic_abs(x):
    """Quadratic function with absolute value"""
    abs_x = abs(x)
    return abs_x**2 + 2*abs_x + 1

print(f"Karmaşık lambda: {bad_lambda(-3)}")
print(f"Açık fonksiyon: {quadratic_abs(-3)}")

print("\n=== LAMBDA FONKSİYONLARI ÖZETİ ===")
print("Sözdizimi:")
print("  lambda arguments: expression")
print()
print("Kullanım alanları:")
print("  • map(), filter(), sorted() ile")
print("  • Event handling")
print("  • Quick calculations")
print("  • Functional programming")
print("  • Higher-order functions")
print()
print("Avantajları:")
print("  • Kısa ve öz")
print("  • Inline tanımlama")
print("  • Functional style")
print("  • Geçici işlemler için ideal")
print()
print("Dezavantajları:")
print("  • Tek expression sınırı")
print("  • Debugging zorluğu")  
print("  • Okunabilirlik (karmaşık durumlar)")
print("  • Docstring yok")
print()
print("Ne zaman kullan:")
print("  ✓ Basit, tek satır işlemler")
print("  ✓ Functional programming patterns")
print("  ✗ Karmaşık logic")
print("  ✗ Reusable fonksiyonlar")