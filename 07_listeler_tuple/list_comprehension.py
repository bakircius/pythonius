# List Comprehension - Pythonic Liste Oluşturma
# Python list comprehension özelliğinin detaylı incelenmesi

print("=== LIST COMPREHENSION ===\n")

print("1. TEMEL SÖZDİZİMİ:")
print("-" * 18)

# Geleneksel yöntem vs List Comprehension
print("Geleneksel yöntem:")
sayilar = []
for i in range(10):
    sayilar.append(i ** 2)
print(f"Kareler: {sayilar}")

print("\nList comprehension:")
kareler = [i ** 2 for i in range(10)]
print(f"Kareler: {kareler}")

# Temel sözdizimi: [ifade for eleman in iterable]
print(f"\nBasit örnekler:")
print(f"0-9: {[x for x in range(10)]}")
print(f"Çiftler: {[x * 2 for x in range(5)]}")
print(f"Küpler: {[x ** 3 for x in range(5)]}")

# String'lerle
harfler = [char for char in "Python"]
print(f"Harfler: {harfler}")

kelimeler = ["elma", "armut", "muz"]
uzunluklar = [len(kelime) for kelime in kelimeler]
print(f"Uzunluklar: {uzunluklar}")

print("\n2. KOŞULLU LIST COMPREHENSION:")
print("-" * 31)

# Syntax: [ifade for eleman in iterable if koşul]
sayilar = range(20)

# Çift sayılar
ciftler = [x for x in sayilar if x % 2 == 0]
print(f"Çift sayılar: {ciftler}")

# Tek sayılar
tekler = [x for x in sayilar if x % 2 == 1]
print(f"Tek sayılar: {tekler}")

# 3'e bölünebilen sayılar
ucun_katlari = [x for x in range(30) if x % 3 == 0]
print(f"3'ün katları: {ucun_katlari}")

# Pozitif sayılar
karma_liste = [-5, -3, -1, 0, 1, 3, 5, 7]
pozitifler = [x for x in karma_liste if x > 0]
print(f"Pozitifler: {pozitifler}")

# String filtreleme
isimler = ["Ali", "Veli", "Ayşe", "Mehmet", "Fatma"]
uzun_isimler = [isim for isim in isimler if len(isim) > 4]
print(f"Uzun isimler: {uzun_isimler}")

# Büyük harfle başlayanlar
metinler = ["python", "Java", "javascript", "C++", "Go"]
buyuk_harfli = [metin for metin in metinler if metin[0].isupper()]
print(f"Büyük harfli: {buyuk_harfli}")

print("\n3. KOŞULLU İFADE (TERNARY):")
print("-" * 27)

# Syntax: [ifade_doğru if koşul else ifade_yanlış for eleman in iterable]
sayilar = range(10)

# Çift/tek etiketleme
etiketler = ["çift" if x % 2 == 0 else "tek" for x in sayilar]
print(f"Etiketler: {etiketler}")

# Pozitif/negatif/sıfır
karma = [-2, -1, 0, 1, 2]
isaretler = ["pozitif" if x > 0 else "negatif" if x < 0 else "sıfır" for x in karma]
print(f"İşaretler: {isaretler}")

# Sıcaklık değerlendirmesi
sicakliklar = [15, 25, 35, 5, 45]
degerlendirme = ["sıcak" if s > 30 else "ılık" if s > 20 else "soğuk" for s in sicakliklar]
print(f"Değerlendirmeler: {degerlendirme}")

# Sayı mutlak değeri
sayilar = [-5, -3, 0, 2, 4]
mutlak = [x if x >= 0 else -x for x in sayilar]
print(f"Mutlak değerler: {mutlak}")

print("\n4. İÇ İÇE LIST COMPREHENSION:")
print("-" * 28)

# 2D liste oluşturma
matrix = [[i + j for j in range(3)] for i in range(3)]
print("3x3 Matrix:")
for satir in matrix:
    print(f"  {satir}")

# Çarpım tablosu
carpim_tablosu = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print("\nÇarpım tablosu (5x5):")
for i, satir in enumerate(carpim_tablosu, 1):
    print(f"  {i}: {satir}")

# Matrix transpose
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"\nOrijinal matrix: {matrix}")
transpose = [[satir[i] for satir in matrix] for i in range(len(matrix[0]))]
print(f"Transpose: {transpose}")

# 2D liste düzleştirme
ic_ice_liste = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
duzlestirilmis = [eleman for alt_liste in ic_ice_liste for eleman in alt_liste]
print(f"\nİç içe: {ic_ice_liste}")
print(f"Düzleştirilmiş: {duzlestirilmis}")

print("\n5. ÇOK DEĞİŞKENLİ LIST COMPREHENSION:")
print("-" * 36)

# İki liste kombinasyonu
renkler = ["kırmızı", "yeşil", "mavi"]
boyutlar = ["küçük", "orta", "büyük"]

kombinasyonlar = [f"{renk} {boyut}" for renk in renkler for boyut in boyutlar]
print(f"Kombinasyonlar: {kombinasyonlar}")

# Koordinat oluşturma
koordinatlar = [(x, y) for x in range(3) for y in range(3)]
print(f"Koordinatlar: {koordinatlar}")

# Koşullu kombinasyon
# Sadece x != y olanlar
farkli_koordinatlar = [(x, y) for x in range(3) for y in range(3) if x != y]
print(f"Farklı koordinatlar: {farkli_koordinatlar}")

# Matematik: (x, y) çiftleri x + y çift ise
cift_toplam = [(x, y) for x in range(5) for y in range(5) if (x + y) % 2 == 0]
print(f"Çift toplam: {cift_toplam}")

print("\n6. FONKSİYONLARLA LIST COMPREHENSION:")
print("-" * 36)

# Kendi fonksiyonlarımızla
def kare(x):
    return x ** 2

def asal_mi(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

sayilar = range(20)
kareler = [kare(x) for x in sayilar]
print(f"Kareler: {kareler}")

asallar = [x for x in sayilar if asal_mi(x)]
print(f"Asal sayılar: {asallar}")

# Built-in fonksiyonlarla
metinler = ["  Python  ", "  Java  ", "  C++  "]
temizlenmis = [metin.strip() for metin in metinler]
print(f"Temizlenmiş: {temizlenmis}")

sayilar_str = ["1", "2", "3", "4", "5"]
sayilar_int = [int(s) for s in sayilar_str]
print(f"Integer'a çevrilmiş: {sayilar_int}")

# String metotları
kelimeler = ["python", "java", "go", "rust"]
buyuk_harfler = [kelime.upper() for kelime in kelimeler]
print(f"Büyük harfler: {buyuk_harfler}")

print("\n7. LAMBDA İLE LIST COMPREHENSION:")
print("-" * 31)

# Lambda fonksiyonları kullanma
sayilar = range(10)

# Lambda ile karmaşık işlemler
sonuclar = [(lambda x: x ** 2 + 2 * x + 1)(x) for x in sayilar]
print(f"f(x) = x² + 2x + 1: {sonuclar}")

# Map benzeri kullanım
kelimeler = ["python", "java", "go"]
uzunluk_kelime = [(lambda s: (len(s), s))(kelime) for kelime in kelimeler]
print(f"(uzunluk, kelime): {uzunluk_kelime}")

# Filter benzeri kullanım
sayilar = range(20)
ozel_sayilar = [x for x in sayilar if (lambda n: n % 3 == 0 and n % 5 != 0)(x)]
print(f"3'ün katları ama 5'in değil: {ozel_sayilar}")

print("\n8. STRİNG PROCESSING:")
print("-" * 20)

# Metin analizi
metin = "Python programlama dili çok güçlüdür"
kelimeler = metin.split()

# Kelime uzunlukları
uzunluklar = [len(kelime) for kelime in kelimeler]
print(f"Kelime uzunlukları: {uzunluklar}")

# Büyük harfe çevirme
buyuk_kelimeler = [kelime.upper() for kelime in kelimeler]
print(f"Büyük harfler: {buyuk_kelimeler}")

# Uzun kelimeleri filtreleme
uzun_kelimeler = [kelime for kelime in kelimeler if len(kelime) > 5]
print(f"Uzun kelimeler: {uzun_kelimeler}")

# Her kelimenin ilk harfi
ilk_harfler = [kelime[0] for kelime in kelimeler]
print(f"İlk harfler: {ilk_harfler}")

# Karakter filtreleme
metin = "Python123Program456"
sadece_harfler = [char for char in metin if char.isalpha()]
print(f"Sadece harfler: {''.join(sadece_harfler)}")

sadece_rakamlar = [char for char in metin if char.isdigit()]
print(f"Sadece rakamlar: {''.join(sadece_rakamlar)}")

print("\n9. DOSYA İŞLEMLERİ SİMÜLASYONU:")
print("-" * 30)

# Dosya satırları simülasyonu
dosya_satirlari = [
    "# Bu bir Python dosyası",
    "import os",
    "",
    "def main():",
    "    print('Merhaba')",
    "    return 0",
    "",
    "if __name__ == '__main__':",
    "    main()"
]

# Boş olmayan satırlar
bos_olmayan = [satir for satir in dosya_satirlari if satir.strip()]
print(f"Boş olmayan satırlar: {len(bos_olmayan)}")

# Yorum satırları
yorum_satirlari = [satir for satir in dosya_satirlari if satir.strip().startswith('#')]
print(f"Yorum satırları: {yorum_satirlari}")

# İndentli satırlar
indentli = [satir for satir in dosya_satirlari if satir.startswith('    ')]
print(f"İndentli satırlar: {indentli}")

# Satır uzunlukları
uzunluklar = [len(satir) for satir in dosya_satirlari]
print(f"Satır uzunlukları: {uzunluklar}")

print("\n10. PERFORMANS KARŞILAŞTIRMASI:")
print("-" * 29)

import time

# Büyük veri seti
n = 100000
print(f"{n} elemanlı testler:")

# 1. For loop
start = time.time()
sonuc1 = []
for i in range(n):
    if i % 2 == 0:
        sonuc1.append(i ** 2)
for_time = time.time() - start

# 2. List comprehension
start = time.time()
sonuc2 = [i ** 2 for i in range(n) if i % 2 == 0]
comp_time = time.time() - start

# 3. Filter + map
start = time.time()
sonuc3 = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, range(n))))
filter_map_time = time.time() - start

print(f"For loop: {for_time:.4f} saniye")
print(f"List comprehension: {comp_time:.4f} saniye")
print(f"Filter + map: {filter_map_time:.4f} saniye")
print(f"List comp. {for_time/comp_time:.1f}x daha hızlı")

print("\n11. GENERATOR vs LIST COMPREHENSION:")
print("-" * 35)

# Bellek kullanımı karşılaştırması
import sys

# List comprehension (belleği hemen kullanır)
list_comp = [x ** 2 for x in range(1000)]
print(f"List comprehension boyutu: {sys.getsizeof(list_comp)} byte")

# Generator expression (lazy evaluation)
gen_exp = (x ** 2 for x in range(1000))
print(f"Generator boyutu: {sys.getsizeof(gen_exp)} byte")

# Generator kullanımı
print(f"İlk 5 eleman: {[next(gen_exp) for _ in range(5)]}")

print("\n12. KARMAŞIK ÖRNEKLER:")
print("-" * 20)

# Fibonacci sayıları (ilk 10)
def fibonacci_list(n):
    fib = [0, 1]
    [fib.append(fib[-1] + fib[-2]) for _ in range(n - 2)]
    return fib[:n]

fib_sayilari = fibonacci_list(10)
print(f"Fibonacci: {fib_sayilari}")

# Pascal üçgeni
def pascal_satir(n):
    if n == 0:
        return [1]
    onceki = pascal_satir(n - 1)
    return [1] + [onceki[i] + onceki[i + 1] for i in range(len(onceki) - 1)] + [1]

pascal_5 = [pascal_satir(i) for i in range(6)]
print("\nPascal üçgeni:")
for i, satir in enumerate(pascal_5):
    print(f"  Satır {i}: {satir}")

# Word frequency
metin = "python python java python go java python"
kelimeler = metin.split()
tekil_kelimeler = list(set(kelimeler))
frekanslar = [(kelime, kelimeler.count(kelime)) for kelime in tekil_kelimeler]
print(f"\nKelime frekansları: {frekanslar}")

# En sık geçen kelime
en_sik = max(frekanslar, key=lambda x: x[1])
print(f"En sık geçen: {en_sik}")

print("\n13. LİST COMPREHENSION HATALARI:")
print("-" * 32)

# Yaygın hatalar ve çözümler

# 1. Değişken kapsam hatası
print("Kapsam problemi:")
x = 10
liste = [x for x in range(5)]  # x değişkeni değişir
print(f"Liste: {liste}")
print(f"x değeri: {x}")  # x hala 10 (Python 3'te)

# 2. Mutable default argument problemi
def kotu_ornek(liste=[]):
    return [x * 2 for x in liste]

def iyi_ornek(liste=None):
    if liste is None:
        liste = []
    return [x * 2 for x in liste]

# 3. Çok karmaşık comprehension
# KÖTÜ - okunması zor
karmasik = [x for sublist in [[y**2 for y in range(3)] for x in range(3)] for x in sublist if x % 2 == 0]
print(f"Karmaşık: {karmasik}")

# İYİ - adım adım
alt_listeler = [[y**2 for y in range(3)] for x in range(3)]
duzlestirilmis = [x for sublist in alt_listeler for x in sublist]
ciftler = [x for x in duzlestirilmis if x % 2 == 0]
print(f"Adım adım: {ciftler}")

print("\n14. BEN NEREDE KULLANMALIYIM?")
print("-" * 30)

# List comprehension kullan:
print("List comprehension KULLAN:")
print("  ✓ Basit dönüşümler")
print("  ✓ Basit filtreleme")
print("  ✓ Tek satırda ifade edilebilir")
print("  ✓ Performans kritik")

# Normal döngü kullan:
print("\nNormal döngü KULLAN:")
print("  ✓ Karmaşık logic")
print("  ✓ Çok sayıda koşul")
print("  ✓ Debug gerekebilir")
print("  ✓ Exception handling")

# Örnekler
print(f"\nİYİ örnekler:")
numbers = range(10)
squares = [x**2 for x in numbers]  # Basit
evens = [x for x in numbers if x % 2 == 0]  # Basit filtreleme
print(f"Kareler: {squares}")
print(f"Çiftler: {evens}")

print(f"\nKÖTÜ örnek (çok karmaşık):")
# Bu list comprehension çok karmaşık, normal döngü daha iyi
result = []
for x in range(10):
    if x % 2 == 0:
        try:
            value = 1 / x if x != 0 else 0
            if value > 0.1:
                result.append(value)
        except:
            pass
print(f"Karmaşık işlem sonucu: {result}")

print("\n=== LIST COMPREHENSION ÖZETİ ===")
print("Sözdizimi:")
print("  • [ifade for eleman in iterable]")
print("  • [ifade for eleman in iterable if koşul]")
print("  • [ifade_doğru if koşul else ifade_yanlış for eleman in iterable]")
print()
print("Avantajları:")
print("  • Daha hızlı performans")
print("  • Daha kısa kod")
print("  • Pythonic yazım")
print("  • Okunabilirlik (basit durumlarda)")
print()
print("Dezavantajları:")
print("  • Karmaşık logic için uygun değil")
print("  • Debug zorluğu")
print("  • Bellek kullanımı (büyük listeler)")
print()
print("Alternatifler:")
print("  • Generator expressions (bellek tasarrufu)")
print("  • map() ve filter() fonksiyonları")
print("  • Normal for döngüleri (karmaşık logic)")
print()
print("Best practices:")
print("  • Basit tutun")
print("  • Karmaşık logic için normal döngü")
print("  • Büyük veriler için generator kullanın")
print("  • Okunabilirliği önceleyın")