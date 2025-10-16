# Sözlük (Dictionary) Temelleri
# Python sözlük veri tipinin detaylı incelenmesi

print("=== SÖZLÜK (DICTIONARY) TEMELLERİ ===\n")

print("1. SÖZLÜK OLUŞTURMA:")
print("-" * 20)

# Boş sözlük
bos_sozluk = {}
print(f"Boş sözlük: {bos_sozluk}, tip: {type(bos_sozluk)}")

bos_sozluk2 = dict()
print(f"dict(): {bos_sozluk2}")

# Temel sözlük
ogrenci = {
    "ad": "Ali",
    "soyad": "Veli",
    "yas": 20,
    "bolum": "Bilgisayar Mühendisliği"
}
print(f"Öğrenci: {ogrenci}")

# Farklı veri tipleri
karısık = {
    "string": "metin",
    "integer": 42,
    "float": 3.14,
    "boolean": True,
    "liste": [1, 2, 3],
    "tuple": (4, 5, 6),
    "none": None
}
print(f"Karışık tipler: {karısık}")

# dict() fonksiyonu ile
# Tuple'lardan
tuple_listesi = [("a", 1), ("b", 2), ("c", 3)]
sozluk_tuple = dict(tuple_listesi)
print(f"Tuple'lardan: {sozluk_tuple}")

# Keyword argumentlar
sozluk_kwargs = dict(ad="Ayşe", soyad="Yılmaz", yas=25)
print(f"Kwargs: {sozluk_kwargs}")

# zip() ile
anahtarlar = ["isim", "yaş", "şehir"]
değerler = ["Mehmet", 30, "İstanbul"]
sozluk_zip = dict(zip(anahtarlar, değerler))
print(f"zip(): {sozluk_zip}")

print("\n2. SÖZLÜK ERİŞİM:")
print("-" * 17)

# Köşeli parantez ile erişim
print(f"Ad: {ogrenci['ad']}")
print(f"Yaş: {ogrenci['yas']}")

# Olmayan anahtar hatası
try:
    print(ogrenci["not_ortalaması"])
except KeyError as e:
    print(f"KeyError: {e}")

# get() metodu (güvenli erişim)
print(f"Ad (get): {ogrenci.get('ad')}")
print(f"Not (get): {ogrenci.get('not_ortalaması')}")  # None döner
print(f"Not (default): {ogrenci.get('not_ortalaması', 'Bilinmiyor')}")

# İç içe sözlükler
sinif = {
    "101": {
        "öğrenci_sayısı": 25,
        "öğretmen": "Prof. Dr. Ali",
        "dersler": ["Matematik", "Fizik", "Kimya"]
    },
    "102": {
        "öğrenci_sayısı": 30,
        "öğretmen": "Dr. Ayşe",
        "dersler": ["Edebiyat", "Tarih", "Coğrafya"]
    }
}

print(f"101 öğretmeni: {sinif['101']['öğretmen']}")
print(f"102 dersler: {sinif['102']['dersler']}")

# Güvenli iç içe erişim
print(f"Güvenli: {sinif.get('103', {}).get('öğretmen', 'Bulunamadı')}")

print("\n3. SÖZLÜK DEĞİŞTİRME:")
print("-" * 20)

# Yeni anahtar ekleme
ogrenci["not_ortalaması"] = 3.45
print(f"Not eklendi: {ogrenci}")

# Mevcut değeri değiştirme
ogrenci["yas"] = 21
print(f"Yaş değişti: {ogrenci}")

# Çoklu güncelleme
ogrenci.update({"telefon": "555-1234", "email": "ali@email.com"})
print(f"Çoklu güncelleme: {ogrenci}")

# Başka sözlükle güncelleme
ek_bilgiler = {"adres": "İstanbul", "durum": "Aktif"}
ogrenci.update(ek_bilgiler)
print(f"Sözlükle güncelleme: {ogrenci}")

# Keyword arguments ile güncelleme
ogrenci.update(mezuniyet_yili=2025, burs=True)
print(f"Kwargs güncelleme: {ogrenci}")

print("\n4. SÖZLÜK SİLME İŞLEMLERİ:")
print("-" * 26)

# del ile silme
del ogrenci["telefon"]
print(f"Telefon silindi: {ogrenci}")

# pop() ile silme (değer döndürür)
email = ogrenci.pop("email")
print(f"Email çıkarıldı: {email}")
print(f"Sözlük: {ogrenci}")

# pop() varsayılan değer ile
not_var = ogrenci.pop("not_var", "Yok")
print(f"Olmayan anahtar: {not_var}")

# popitem() - son eklenen elemanı çıkarır (Python 3.7+)
son_eleman = ogrenci.popitem()
print(f"Son eleman: {son_eleman}")
print(f"Kalan: {ogrenci}")

# clear() - tüm elemanları sil
yedek = ogrenci.copy()
ogrenci.clear()
print(f"Temizlendi: {ogrenci}")
print(f"Yedek: {yedek}")

# Orijinali geri yükle
ogrenci = yedek

print("\n5. SÖZLÜK METOTLARI:")
print("-" * 18)

print(f"Test sözlüğü: {ogrenci}")

# keys() - anahtarları al
anahtarlar = ogrenci.keys()
print(f"Anahtarlar: {list(anahtarlar)}")

# values() - değerleri al
degerler = ogrenci.values()
print(f"Değerler: {list(degerler)}")

# items() - anahtar-değer çiftleri
çiftler = ogrenci.items()
print(f"Çiftler: {list(çiftler)}")

# copy() - yüzeysel kopya
kopya = ogrenci.copy()
print(f"Kopya: {kopya}")

# Derin kopya gerektiğinde
import copy
ic_ice_sozluk = {
    "kişi": {"ad": "Ali", "yas": 20},
    "hobiler": ["okuma", "spor"]
}

yuzeysel = ic_ice_sozluk.copy()
derin = copy.deepcopy(ic_ice_sozluk)

# Yüzeysel kopya testi
ic_ice_sozluk["kişi"]["yas"] = 25
print(f"Orijinal: {ic_ice_sozluk}")
print(f"Yüzeysel kopya etkilendi: {yuzeysel}")
print(f"Derin kopya etkilenmedi: {derin}")

print("\n6. SÖZLÜK KONTROL İŞLEMLERİ:")
print("-" * 26)

# in operatörü (anahtarlarda arar)
print(f"'ad' var mı: {'ad' in ogrenci}")
print(f"'telefon' var mı: {'telefon' in ogrenci}")

# not in operatörü
print(f"'email' yok mu: {'email' not in ogrenci}")

# Değerlerde arama (yavaş)
print(f"'Ali' değer olarak var mı: 'Ali' in ogrenci.values()")

# Çift olarak arama
print(f"('ad', 'Ali') çifti var mı: ('ad', 'Ali') in ogrenci.items()")

# Boyut kontrolü
print(f"Sözlük uzunluğu: {len(ogrenci)}")
print(f"Boş mu: {len(ogrenci) == 0}")

print("\n7. SÖZLÜK İTERASYONU:")
print("-" * 20)

# Anahtarlar üzerinde
print("Anahtarlar:")
for anahtar in ogrenci:  # Varsayılan: keys()
    print(f"  {anahtar}")

print("\nAnahtar-değerler:")
for anahtar in ogrenci.keys():
    print(f"  {anahtar}: {ogrenci[anahtar]}")

# Değerler üzerinde
print("\nSadece değerler:")
for değer in ogrenci.values():
    print(f"  {değer}")

# Çiftler üzerinde (en yaygın)
print("\nÇiftler:")
for anahtar, değer in ogrenci.items():
    print(f"  {anahtar}: {değer}")

# Enumerate ile
print("\nNumaralı çiftler:")
for i, (anahtar, değer) in enumerate(ogrenci.items(), 1):
    print(f"  {i}. {anahtar}: {değer}")

print("\n8. SÖZLÜK COMPREHENSION:")
print("-" * 23)

# Temel sözdizimi: {anahtar: değer for ... in ...}
sayilar = range(1, 6)
kareler = {x: x**2 for x in sayilar}
print(f"Kareler: {kareler}")

# Koşullu comprehension
cift_kareler = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"Çift kareler: {cift_kareler}")

# String işlemleri
kelimeler = ["python", "java", "go", "rust"]
uzunluklar = {kelime: len(kelime) for kelime in kelimeler}
print(f"Uzunluklar: {uzunluklar}")

# Büyük harfe çevirme
buyuk_harfler = {kelime.upper(): kelime for kelime in kelimeler}
print(f"Büyük harfler: {buyuk_harfler}")

# Mevcut sözlüğü dönüştürme
ters_sozluk = {değer: anahtar for anahtar, değer in uzunluklar.items()}
print(f"Ters sözlük: {ters_sozluk}")

# İç içe comprehension
matrix_dict = {f"satir_{i}": {f"sutun_{j}": i*j for j in range(3)} for i in range(3)}
print(f"Matrix sözlük: {matrix_dict}")

print("\n9. SÖZLÜK ADVANCED KULLANIM:")
print("-" * 26)

# setdefault() - anahtar yoksa ekle
sayac = {}
kelimeler = ["python", "java", "python", "go", "java", "python"]

for kelime in kelimeler:
    sayac.setdefault(kelime, 0)
    sayac[kelime] += 1

print(f"Kelime sayacı: {sayac}")

# get() ile varsayılan değer
sayac2 = {}
for kelime in kelimeler:
    sayac2[kelime] = sayac2.get(kelime, 0) + 1

print(f"get() ile sayaç: {sayac2}")

# defaultdict kullanımı
from collections import defaultdict

# int varsayılan değer (0)
sayac3 = defaultdict(int)
for kelime in kelimeler:
    sayac3[kelime] += 1
print(f"defaultdict: {dict(sayac3)}")

# list varsayılan değer
gruplar = defaultdict(list)
ogrenciler = [
    ("Ali", "Mühendislik"),
    ("Veli", "Tıp"),
    ("Ayşe", "Mühendislik"),
    ("Mehmet", "Tıp"),
    ("Fatma", "Hukuk")
]

for isim, bolum in ogrenciler:
    gruplar[bolum].append(isim)

print(f"Bölüm grupları: {dict(gruplar)}")

print("\n10. SÖZLÜK SIRALAMA:")
print("-" * 18)

# Python 3.7+ sözlükler insertion order tutar
notlar = {"Ali": 85, "Veli": 92, "Ayşe": 78, "Mehmet": 89}
print(f"Orijinal: {notlar}")

# Anahtarlara göre sıralama
anahtara_gore = dict(sorted(notlar.items()))
print(f"Anahtara göre: {anahtara_gore}")

# Değerlere göre sıralama
degere_gore = dict(sorted(notlar.items(), key=lambda x: x[1]))
print(f"Değere göre: {degere_gore}")

# Ters sıralama
ters_siralama = dict(sorted(notlar.items(), key=lambda x: x[1], reverse=True))
print(f"Ters sıralama: {ters_siralama}")

# Karmaşık sıralama
ogrenci_listesi = {
    "Ali": {"not": 85, "yas": 20},
    "Veli": {"not": 92, "yas": 19},
    "Ayşe": {"not": 78, "yas": 21}
}

# Yaşa göre sırala
yasa_gore = dict(sorted(ogrenci_listesi.items(), key=lambda x: x[1]["yas"]))
print(f"Yaşa göre: {yasa_gore}")

print("\n11. SÖZLÜK PERFORMANSI:")
print("-" * 20)

import time

# Büyük sözlük oluştur
n = 100000
büyük_sözlük = {f"anahtar_{i}": i for i in range(n)}

# Erişim hızı (O(1))
start = time.time()
for i in range(1000):
    _ = büyük_sözlük.get(f"anahtar_{i}")
erişim_time = time.time() - start

# Arama hızı (in operatörü)
start = time.time()
for i in range(1000):
    _ = f"anahtar_{i}" in büyük_sözlük
arama_time = time.time() - start

# Liste ile karşılaştırma
büyük_liste = list(büyük_sözlük.keys())
start = time.time()
for i in range(100):  # Daha az çünkü çok yavaş
    _ = f"anahtar_{i}" in büyük_liste
liste_arama_time = time.time() - start

print(f"Sözlük erişim (1000 kez): {erişim_time*1000:.2f} ms")
print(f"Sözlük arama (1000 kez): {arama_time*1000:.2f} ms")
print(f"Liste arama (100 kez): {liste_arama_time*1000:.2f} ms")
print(f"Sözlük {(liste_arama_time/100)/(arama_time/1000):.0f}x daha hızlı")

print("\n12. SÖZLÜK KULLANIM ALANLARI:")
print("-" * 26)

# 1. Veri modelleme
kişi = {
    "ad": "Ali",
    "soyad": "Veli",
    "iletişim": {
        "telefon": "555-1234",
        "email": "ali@email.com"
    },
    "adres": {
        "şehir": "İstanbul",
        "ilçe": "Kadıköy"
    }
}

# 2. Konfigürasyon
config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "myapp"
    },
    "logging": {
        "level": "INFO",
        "file": "app.log"
    }
}

# 3. Cache/Memoization
cache = {}

def expensive_function(n):
    if n in cache:
        print(f"Cache'den alındı: {n}")
        return cache[n]
    
    # Pahalı hesaplama simülasyonu
    result = n ** 2 + n * 2 + 1
    cache[n] = result
    print(f"Hesaplandı: {n} = {result}")
    return result

# Test
for i in [1, 2, 1, 3, 2, 4]:
    expensive_function(i)

print(f"Cache: {cache}")

# 4. Lookup table
gun_numaralari = {
    "Pazartesi": 1,
    "Salı": 2,
    "Çarşamba": 3,
    "Perşembe": 4,
    "Cuma": 5,
    "Cumartesi": 6,
    "Pazar": 7
}

def gun_no(gun_adi):
    return gun_numaralari.get(gun_adi, "Geçersiz gün")

print(f"Salı: {gun_no('Salı')}")
print(f"Geçersiz: {gun_no('Geçersiz')}")

# 5. Counter/Frequency
def kelime_frekansi(metin):
    kelimeler = metin.lower().split()
    frekans = {}
    for kelime in kelimeler:
        frekans[kelime] = frekans.get(kelime, 0) + 1
    return frekans

metin = "Python programlama dili Python ile python öğreniyorum"
frekans = kelime_frekansi(metin)
print(f"Kelime frekansı: {frekans}")

print("\n13. SÖZLÜK HATALARI VE ÇÖZÜMLER:")
print("-" * 30)

# 1. KeyError
try:
    değer = ogrenci["olmayan_anahtar"]
except KeyError:
    değer = "Varsayılan"
print(f"KeyError çözümü: {değer}")

# 2. Mutable key hatası
try:
    hatalı_sözlük = {[1, 2, 3]: "değer"}  # Liste key olamaz
except TypeError as e:
    print(f"Mutable key hatası: {e}")

# 3. Dictionary changed size during iteration
test_dict = {"a": 1, "b": 2, "c": 3}
# YANLIŞ yöntem
try:
    for key in test_dict:
        if key == "b":
            del test_dict[key]  # RuntimeError!
except RuntimeError as e:
    print(f"Iteration hatası: {e}")

# DOĞRU yöntem
test_dict = {"a": 1, "b": 2, "c": 3}
silinecekler = [key for key in test_dict if key == "b"]
for key in silinecekler:
    del test_dict[key]
print(f"Güvenli silme: {test_dict}")

print("\n14. SÖZLÜK EN İYİ PRATİKLER:")
print("-" * 28)

# 1. get() kullan, KeyError'dan kaçın
print("✓ get() kullanımı:")
değer = ogrenci.get("not_ortalaması", 0.0)
print(f"  Güvenli erişim: {değer}")

# 2. in operatörü kullan
print("✓ in operatörü:")
if "yas" in ogrenci:
    print(f"  Yaş: {ogrenci['yas']}")

# 3. items() ile iterasyon
print("✓ items() iterasyonu:")
for key, value in ogrenci.items():
    if isinstance(value, str):
        print(f"  String değer: {key} = {value}")
        break

# 4. Comprehension kullan
print("✓ Comprehension:")
filtreli = {k: v for k, v in ogrenci.items() if isinstance(v, (int, float))}
print(f"  Sayısal değerler: {filtreli}")

print("\n=== SÖZLÜK ÖZETİ ===")
print("Özellikler:")
print("  • Mutable (değiştirilebilir)")
print("  • Unordered (Python 3.7+'da insertion order)")
print("  • Key-value çiftleri")
print("  • Keys unique (tekil)")
print("  • Keys immutable olmalı")
print("  • O(1) erişim hızı")
print()
print("Temel metotlar:")
print("  • get(key, default) - güvenli erişim")
print("  • keys(), values(), items() - görünümler")
print("  • update(dict) - güncelleme")
print("  • pop(key), popitem() - silme")
print("  • clear() - temizleme")
print()
print("Kullanım alanları:")
print("  • Veri modelleme")
print("  • Konfigürasyon")
print("  • Cache/Memoization")
print("  • Lookup tables")
print("  • Frequency counting")
print()
print("Performance:")
print("  • O(1) average case erişim")
print("  • O(n) worst case (hash collision)")
print("  • Memory efficient")
print("  • Liste'den hızlı arama")