# Sözlük Metotları ve İleri Seviye Kullanım
# Python sözlük metotlarının detaylı incelenmesi

print("=== SÖZLÜK METOTLARI VE İLERİ SEVİYE KULLANIM ===\n")

print("1. GET() VE SETDEFAULT() METOTLARI:")
print("-" * 35)

# Temel sözlük
ogrenci = {"ad": "Ali", "soyad": "Veli", "yas": 20}
print(f"Öğrenci: {ogrenci}")

# get() metodu - güvenli erişim
print(f"Ad: {ogrenci.get('ad')}")
print(f"Telefon: {ogrenci.get('telefon')}")  # None döner
print(f"Telefon (default): {ogrenci.get('telefon', 'Yok')}")

# setdefault() - yoksa ekle, varsa mevcut değeri döndür
telefon = ogrenci.setdefault('telefon', '555-0000')
print(f"Telefon setdefault: {telefon}")
print(f"Güncel sözlük: {ogrenci}")

# Mevcut anahtar için setdefault()
ad = ogrenci.setdefault('ad', 'Bilinmeyen')
print(f"Ad setdefault (değişmez): {ad}")
print(f"Sözlük: {ogrenci}")

# Pratik kullanım: liste oluşturma
gruplar = {}
ogrenciler = [
    ("Ali", "Mühendislik"),
    ("Veli", "Tıp"),
    ("Ayşe", "Mühendislik"),
    ("Mehmet", "Tıp")
]

for isim, bolum in ogrenciler:
    gruplar.setdefault(bolum, []).append(isim)

print(f"Bölüm grupları: {gruplar}")

print("\n2. UPDATE() METODU:")
print("-" * 18)

# Başlangıç sözlüğü
temel_bilgi = {"ad": "Ali", "yas": 20}
print(f"Temel: {temel_bilgi}")

# Sözlükle güncelleme
ek_bilgi = {"soyad": "Veli", "bolum": "Mühendislik"}
temel_bilgi.update(ek_bilgi)
print(f"Sözlükle update: {temel_bilgi}")

# Keyword arguments ile
temel_bilgi.update(telefon="555-1234", email="ali@email.com")
print(f"Kwargs update: {temel_bilgi}")

# Tuple listesi ile
temel_bilgi.update([("adres", "İstanbul"), ("durum", "Aktif")])
print(f"Tuple listesi: {temel_bilgi}")

# Mevcut değerleri güncelleme
temel_bilgi.update({"yas": 21, "bolum": "Bilgisayar Mühendisliği"})
print(f"Güncelleme: {temel_bilgi}")

# Koşullu güncelleme
def kosullu_update(sozluk, **kwargs):
    for key, value in kwargs.items():
        if key not in sozluk:  # Sadece yoksa ekle
            sozluk[key] = value

kosullu_update(temel_bilgi, not_ortalamasi=3.5, yas=25)  # yas değişmez
print(f"Koşullu update: {temel_bilgi}")

print("\n3. POP() VE POPITEM() METOTLARI:")
print("-" * 31)

# Test sözlüğü
test_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
print(f"Test sözlüğü: {test_dict}")

# pop() - anahtar ile silme
deger_b = test_dict.pop("b")
print(f"pop('b'): {deger_b}, kalan: {test_dict}")

# pop() varsayılan değer ile
deger_x = test_dict.pop("x", "Bulunamadı")
print(f"pop('x', default): {deger_x}")

# popitem() - son eklenen çifti çıkar (Python 3.7+)
son_cift = test_dict.popitem()
print(f"popitem(): {son_cift}, kalan: {test_dict}")

# LIFO (Last In, First Out) davranışı
stack_dict = {}
stack_dict["birinci"] = 1
stack_dict["ikinci"] = 2
stack_dict["üçüncü"] = 3

print(f"Stack dict: {stack_dict}")
while stack_dict:
    key, value = stack_dict.popitem()
    print(f"Çıkarılan: {key} = {value}")

print("\n4. KEYS(), VALUES(), ITEMS() GÖRÜNÜMLERİ:")
print("-" * 40)

# Test sözlüğü
notlar = {"Ali": 85, "Veli": 92, "Ayşe": 78, "Mehmet": 89}
print(f"Notlar: {notlar}")

# Keys view
anahtarlar = notlar.keys()
print(f"Keys: {anahtarlar}")
print(f"Keys tipi: {type(anahtarlar)}")

# Values view
degerler = notlar.values()
print(f"Values: {degerler}")

# Items view
ciftler = notlar.items()
print(f"Items: {ciftler}")

# View'lar dinamiktir
print(f"\nDinamik özellik testi:")
print(f"Önce keys: {list(anahtarlar)}")
notlar["Fatma"] = 95
print(f"Sonra keys: {list(anahtarlar)}")

# View operasyonları
print(f"\nView operasyonları:")
print(f"'Ali' in keys: {'Ali' in anahtarlar}")
print(f"Keys uzunluğu: {len(anahtarlar)}")

# Set operasyonları (keys ile)
diger_notlar = {"Ali": 90, "Zeynep": 88}
ortak_ogrenciler = notlar.keys() & diger_notlar.keys()
print(f"Ortak öğrenciler: {ortak_ogrenciler}")

# Values'da arama (yavaş)
print(f"90+ not var mı: {any(nota >= 90 for nota in degerler)}")

print("\n5. COPY() VE DEEPCOPY():")
print("-" * 22)

# Shallow copy
orijinal = {
    "sayilar": [1, 2, 3],
    "kisi": {"ad": "Ali", "yas": 20},
    "metin": "Hello"
}
print(f"Orijinal: {orijinal}")

# copy() metodu
kopya1 = orijinal.copy()
# dict() constructor
kopya2 = dict(orijinal)
# dict comprehension
kopya3 = {k: v for k, v in orijinal.items()}

print(f"copy(): {kopya1}")

# Shallow copy testi
orijinal["metin"] = "Değişti"
print(f"Metin değişti - orijinal: {orijinal['metin']}")
print(f"copy() etkilenmedi: {kopya1['metin']}")

# İç obje değişikliği
orijinal["sayilar"].append(4)
print(f"Sayılara 4 eklendi - orijinal: {orijinal['sayilar']}")
print(f"copy() da etkilendi: {kopya1['sayilar']}")

# Deep copy
import copy
derin_kopya = copy.deepcopy(orijinal)
orijinal["sayilar"].append(5)
print(f"Sayılara 5 eklendi - orijinal: {orijinal['sayilar']}")
print(f"deepcopy etkilenmedi: {derin_kopya['sayilar']}")

print("\n6. CLEAR() VE DEL:")
print("-" * 16)

# Test sözlükleri
test1 = {"a": 1, "b": 2, "c": 3}
test2 = {"a": 1, "b": 2, "c": 3}
test3 = {"a": 1, "b": 2, "c": 3}

print(f"Test1: {test1}")
print(f"Test2: {test2}")
print(f"Test3: {test3}")

# clear() - tüm elemanları sil
test1.clear()
print(f"clear() sonrası: {test1}")

# del - belirli anahtarı sil
del test2["b"]
print(f"del test2['b']: {test2}")

# del - tüm sözlüğü sil
del test3
# print(test3)  # NameError!

# Referans testi
sozluk_a = {"x": 1, "y": 2}
sozluk_b = sozluk_a  # Aynı objeye referans

print(f"A: {sozluk_a}")
print(f"B: {sozluk_b}")

sozluk_a.clear()
print(f"A.clear() sonrası:")
print(f"A: {sozluk_a}")
print(f"B: {sozluk_b}")  # B de boş!

print("\n7. FROMKEYS() CLASS METODU:")
print("-" * 27)

# Aynı değerle sözlük oluştur
anahtarlar = ["a", "b", "c", "d"]
varsayilan_sozluk = dict.fromkeys(anahtarlar, 0)
print(f"fromkeys(0): {varsayilan_sozluk}")

# None varsayılan değer
none_sozluk = dict.fromkeys(anahtarlar)
print(f"fromkeys(): {none_sozluk}")

# String'den anahtarlar
harf_sozluk = dict.fromkeys("python", True)
print(f"String anahtarlar: {harf_sozluk}")

# Range'den anahtarlar
sayi_sozluk = dict.fromkeys(range(5), "boş")
print(f"Range anahtarlar: {sayi_sozluk}")

# DİKKAT: Mutable değerler problemi
liste_sozluk = dict.fromkeys(["a", "b", "c"], [])
print(f"Liste değerler: {liste_sozluk}")

# Tüm listeler aynı obje!
liste_sozluk["a"].append(1)
print(f"Bir listeye ekleme: {liste_sozluk}")  # Hepsi değişti!

# Doğru yöntem: comprehension
dogru_liste_sozluk = {key: [] for key in ["a", "b", "c"]}
dogru_liste_sozluk["a"].append(1)
print(f"Doğru yöntem: {dogru_liste_sozluk}")

print("\n8. SÖZLÜK BİRLEŞTİRME VE MERGİNG:")
print("-" * 33)

# Python 3.5+ unpacking
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"e": 5, "f": 6}

# ** unpacking ile birleştirme
birlesik = {**dict1, **dict2, **dict3}
print(f"Unpacking: {birlesik}")

# Çakışan anahtarlar
dict4 = {"a": 10, "g": 7}
birlesik_cakisma = {**dict1, **dict4}  # Son değer kazanır
print(f"Çakışan anahtarlar: {birlesik_cakisma}")

# Python 3.9+ | operatörü
# birlesik_pipe = dict1 | dict2 | dict3  # Python 3.9+
# print(f"Pipe operatörü: {birlesik_pipe}")

# update() ile birleştirme
dict5 = dict1.copy()
dict5.update(dict2)
dict5.update(dict3)
print(f"update() ile: {dict5}")

# Koşullu birleştirme
def merge_dicts(*dicts, strategy="last_wins"):
    """Sözlükleri farklı stratejilerle birleştir"""
    result = {}
    
    if strategy == "last_wins":
        for d in dicts:
            result.update(d)
    elif strategy == "first_wins":
        for d in dicts:
            for key, value in d.items():
                if key not in result:
                    result[key] = value
    elif strategy == "combine_lists":
        for d in dicts:
            for key, value in d.items():
                if key in result:
                    if isinstance(result[key], list):
                        result[key].append(value)
                    else:
                        result[key] = [result[key], value]
                else:
                    result[key] = value
    
    return result

# Test farklı stratejiler
dict_a = {"x": 1, "y": 2}
dict_b = {"x": 10, "z": 3}

print(f"Last wins: {merge_dicts(dict_a, dict_b, strategy='last_wins')}")
print(f"First wins: {merge_dicts(dict_a, dict_b, strategy='first_wins')}")
print(f"Combine: {merge_dicts(dict_a, dict_b, strategy='combine_lists')}")

print("\n9. SÖZLÜK FİLTRELEME VE TRANSFORMATİON:")
print("-" * 41)

# Test verisi
ogrenciler = {
    "Ali": {"yas": 20, "not": 85, "bolum": "Mühendislik"},
    "Veli": {"yas": 19, "not": 92, "bolum": "Tıp"},
    "Ayşe": {"yas": 21, "not": 78, "bolum": "Mühendislik"},
    "Mehmet": {"yas": 22, "not": 89, "bolum": "Tıp"},
    "Fatma": {"yas": 20, "not": 95, "bolum": "Hukuk"}
}

print(f"Öğrenciler: {ogrenciler}")

# Yüksek notlu öğrenciler (90+)
yuksek_notlu = {isim: bilgi for isim, bilgi in ogrenciler.items() 
                if bilgi["not"] >= 90}
print(f"90+ not: {yuksek_notlu}")

# Mühendislik öğrencileri
muhendislik = {isim: bilgi for isim, bilgi in ogrenciler.items() 
               if bilgi["bolum"] == "Mühendislik"}
print(f"Mühendislik: {muhendislik}")

# Sadece isim-not eşlemesi
isim_not = {isim: bilgi["not"] for isim, bilgi in ogrenciler.items()}
print(f"İsim-not: {isim_not}")

# Not ortalaması hesaplama
toplam_not = sum(bilgi["not"] for bilgi in ogrenciler.values())
ortalama = toplam_not / len(ogrenciler)
print(f"Not ortalaması: {ortalama:.2f}")

# Ortalama üstü öğrenciler
ortalama_ustu = {isim: bilgi for isim, bilgi in ogrenciler.items() 
                 if bilgi["not"] > ortalama}
print(f"Ortalama üstü: {ortalama_ustu}")

print("\n10. SÖZLÜK SIRALAMA VE SIRTLAMA:")
print("-" * 31)

# Test sözlüğü
notlar = {"Ali": 85, "Zeynep": 95, "Mehmet": 78, "Ayşe": 92}
print(f"Notlar: {notlar}")

# Anahtarlara göre sıralama
anahtara_gore = dict(sorted(notlar.items()))
print(f"Anahtara göre: {anahtara_gore}")

# Değerlere göre sıralama
degere_gore = dict(sorted(notlar.items(), key=lambda x: x[1]))
print(f"Nota göre: {degere_gore}")

# Ters sıralama
ters_not = dict(sorted(notlar.items(), key=lambda x: x[1], reverse=True))
print(f"Ters not sırası: {ters_not}")

# En yüksek 3 not
en_yuksek_3 = dict(sorted(notlar.items(), key=lambda x: x[1], reverse=True)[:3])
print(f"En yüksek 3: {en_yuksek_3}")

# Karmaşık sıralama
karma_veri = {
    "Ali": {"not": 85, "yas": 20},
    "Veli": {"not": 85, "yas": 19},  # Aynı not, farklı yaş
    "Ayşe": {"not": 92, "yas": 21}
}

# Önce nota, sonra yaşa göre sırala
karmasik_siralama = dict(sorted(karma_veri.items(), 
                               key=lambda x: (x[1]["not"], x[1]["yas"]), 
                               reverse=True))
print(f"Karmaşık sıralama: {karmasik_siralama}")

print("\n11. SÖZLÜK PERFORMANCE OPTIMIZASYON:")
print("-" * 36)

import time

# Büyük sözlük oluştur
n = 100000
büyük_sözlük = {f"key_{i}": i for i in range(n)}

# 1. get() vs [] erişim
print(f"{n} elemanlı sözlük testleri:")

# [] erişim (KeyError riski)
start = time.time()
for i in range(1000):
    try:
        _ = büyük_sözlük[f"key_{i}"]
    except KeyError:
        pass
bracket_time = time.time() - start

# get() erişim
start = time.time()
for i in range(1000):
    _ = büyük_sözlük.get(f"key_{i}")
get_time = time.time() - start

print(f"[] erişim: {bracket_time*1000:.2f} ms")
print(f"get() erişim: {get_time*1000:.2f} ms")

# 2. in operatörü vs get() None kontrolü
start = time.time()
for i in range(1000):
    if f"key_{i}" in büyük_sözlük:
        _ = büyük_sözlük[f"key_{i}"]
in_check_time = time.time() - start

start = time.time()
for i in range(1000):
    value = büyük_sözlük.get(f"key_{i}")
    if value is not None:
        _ = value
get_check_time = time.time() - start

print(f"in + []: {in_check_time*1000:.2f} ms")
print(f"get() check: {get_check_time*1000:.2f} ms")

# 3. items() vs keys() + []
start = time.time()
for key, value in list(büyük_sözlük.items())[:1000]:
    _ = value
items_time = time.time() - start

start = time.time()
for key in list(büyük_sözlük.keys())[:1000]:
    _ = büyük_sözlük[key]
keys_time = time.time() - start

print(f"items(): {items_time*1000:.2f} ms")
print(f"keys() + []: {keys_time*1000:.2f} ms")

print("\n12. DEFAULTDICT VE COUNTER:")
print("-" * 25)

from collections import defaultdict, Counter

# defaultdict örneği
print("defaultdict kullanımı:")

# Normal sözlük ile kelime sayma
kelimeler = "python java python go java python go".split()
normal_sayac = {}
for kelime in kelimeler:
    if kelime in normal_sayac:
        normal_sayac[kelime] += 1
    else:
        normal_sayac[kelime] = 1

print(f"Normal sözlük: {normal_sayac}")

# defaultdict ile
dd_sayac = defaultdict(int)
for kelime in kelimeler:
    dd_sayac[kelime] += 1

print(f"defaultdict: {dict(dd_sayac)}")

# defaultdict(list) örneği
gruplar = defaultdict(list)
veriler = [("A", 1), ("B", 2), ("A", 3), ("B", 4), ("C", 5)]

for grup, deger in veriler:
    gruplar[grup].append(deger)

print(f"Gruplar: {dict(gruplar)}")

# Counter kullanımı
print("\nCounter kullanımı:")
sayac = Counter(kelimeler)
print(f"Counter: {sayac}")
print(f"En sık 2: {sayac.most_common(2)}")

# Counter operasyonları
sayac2 = Counter("python programming")
print(f"Harf sayacı: {sayac2}")

print("\n13. PRACTICAL PATTERNS:")
print("-" * 21)

# 1. Config manager
class ConfigManager:
    def __init__(self):
        self.config = {
            "database": {"host": "localhost", "port": 5432},
            "logging": {"level": "INFO", "file": "app.log"},
            "cache": {"ttl": 3600, "size": 1000}
        }
    
    def get(self, path, default=None):
        """Dot notation ile config değeri al"""
        keys = path.split('.')
        value = self.config
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default
        return value
    
    def set(self, path, value):
        """Dot notation ile config değeri ayarla"""
        keys = path.split('.')
        config = self.config
        for key in keys[:-1]:
            if key not in config:
                config[key] = {}
            config = config[key]
        config[keys[-1]] = value

config = ConfigManager()
print(f"DB host: {config.get('database.host')}")
print(f"Timeout: {config.get('api.timeout', 30)}")

config.set('api.timeout', 60)
print(f"Config: {config.config}")

# 2. LRU Cache simülasyonu
class SimpleLRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = []
    
    def get(self, key):
        if key in self.cache:
            # Key'i en sona taşı
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return None
    
    def put(self, key, value):
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) >= self.capacity:
            # En eski elemanı çıkar
            oldest = self.order.pop(0)
            del self.cache[oldest]
        
        self.cache[key] = value
        self.order.append(key)
    
    def __str__(self):
        return f"Cache: {self.cache}, Order: {self.order}"

lru = SimpleLRU(3)
lru.put("a", 1)
lru.put("b", 2)
lru.put("c", 3)
print(f"LRU: {lru}")

lru.get("a")  # a'yı son kullanılan yap
lru.put("d", 4)  # b çıkacak (en az kullanılan)
print(f"LRU: {lru}")

print("\n=== SÖZLÜK METOTLARI ÖZETİ ===")
print("Erişim metotları:")
print("  • get(key, default) - güvenli erişim")
print("  • setdefault(key, default) - yoksa ekle")
print("  • __getitem__() - [] operatörü")
print()
print("Güncelleme metotları:")
print("  • update(dict) - birden fazla güncelleme")
print("  • __setitem__() - [] atama")
print()
print("Silme metotları:")
print("  • pop(key, default) - anahtar ile sil")
print("  • popitem() - son çifti sil")
print("  • del dict[key] - anahtar sil")
print("  • clear() - tümünü sil")
print()
print("Görünüm metotları:")
print("  • keys() - anahtarlar")
print("  • values() - değerler")
print("  • items() - çiftler")
print()
print("Yardımcı metotları:")
print("  • copy() - yüzeysel kopya")
print("  • fromkeys() - aynı değerle sözlük")
print()
print("Performance ipuçları:")
print("  • get() > try/except KeyError")
print("  • in operator çok hızlı")
print("  • items() > keys() + []")
print("  • defaultdict > setdefault")