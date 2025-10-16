# Tuple Kullanımı ve Özellikleri
# Python tuple veri tipinin detaylı incelenmesi

print("=== TUPLE KULLANIMI VE ÖZELLİKLERİ ===\n")

print("1. TUPLE OLUŞTURMA:")
print("-" * 19)

# Boş tuple
bos_tuple = ()
print(f"Boş tuple: {bos_tuple}, tip: {type(bos_tuple)}")

# Tek elemanlı tuple (virgül önemli!)
tek_elemanli = (42,)  # Virgül gerekli
print(f"Tek elemanlı: {tek_elemanli}, tip: {type(tek_elemanli)}")

# Virgülsüz (bu tuple değil!)
tek_elemanli_degil = (42)
print(f"Virgülsüz: {tek_elemanli_degil}, tip: {type(tek_elemanli_degil)}")

# Çok elemanlı tuple
renkler = ("kırmızı", "yeşil", "mavi")
print(f"Renkler: {renkler}")

# Parantez olmadan da olur
koordinatlar = 10, 20, 30
print(f"Koordinatlar: {koordinatlar}, tip: {type(koordinatlar)}")

# Karışık tipler
karısık = ("Ali", 25, True, 3.14, [1, 2, 3])
print(f"Karışık: {karısık}")

# tuple() fonksiyonu ile
liste_den = tuple([1, 2, 3, 4])
print(f"Liste'den: {liste_den}")

string_den = tuple("Python")
print(f"String'den: {string_den}")

range_den = tuple(range(5))
print(f"Range'den: {range_den}")

print("\n2. TUPLE İNDEXLEME VE DİLİMLEME:")
print("-" * 32)

sayilar = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f"Tuple: {sayilar}")

# Pozitif indexleme
print(f"İlk eleman [0]: {sayilar[0]}")
print(f"Son eleman [-1]: {sayilar[-1]}")
print(f"Ortadaki [5]: {sayilar[5]}")

# Dilimleme (slicing)
print(f"İlk 3 [0:3]: {sayilar[0:3]}")
print(f"Son 3 [-3:]: {sayilar[-3:]}")
print(f"Çift indeksler [::2]: {sayilar[::2]}")
print(f"Ters sıra [::-1]: {sayilar[::-1]}")
print(f"Ortadan başla [3:7]: {sayilar[3:7]}")

# İç içe tuple'lar
ic_ice = ((1, 2), (3, 4), (5, 6))
print(f"\nİç içe: {ic_ice}")
print(f"İkinci tuple [1]: {ic_ice[1]}")
print(f"İkinci tuple'ın birinci elemanı [1][0]: {ic_ice[1][0]}")

print("\n3. TUPLE DEĞİŞMEZLİĞİ (IMMUTABILITY):")
print("-" * 37)

# Tuple değiştirilemez
meyveler = ("elma", "armut", "muz")
print(f"Meyveler: {meyveler}")

# Bu HATA verir!
try:
    meyveler[0] = "kiraz"
except TypeError as e:
    print(f"Hata: {e}")

# Yeni tuple oluşturmak gerekir
yeni_meyveler = ("kiraz",) + meyveler[1:]
print(f"Yeni tuple: {yeni_meyveler}")

# İç listeler değiştirilebilir (mutable elemanlar)
karısık_tuple = ("sabit", [1, 2, 3], "başka_sabit")
print(f"Karışık: {karısık_tuple}")

# Liste değiştirilebilir
karısık_tuple[1].append(4)
print(f"Liste değişti: {karısık_tuple}")

# Ama tuple'ın kendisi değişmez
try:
    karısık_tuple[1] = [5, 6, 7]
except TypeError as e:
    print(f"Tuple değiştirilemez: {e}")

print("\n4. TUPLE METOTLARI:")
print("-" * 17)

# count() metodu
sayilar = (1, 2, 3, 2, 4, 2, 5)
print(f"Tuple: {sayilar}")
print(f"2'nin sayısı: {sayilar.count(2)}")
print(f"9'un sayısı: {sayilar.count(9)}")

# index() metodu
print(f"2'nin ilk indeksi: {sayilar.index(2)}")
print(f"4'ün indeksi: {sayilar.index(4)}")

# Belirli aralıkta arama
try:
    ikinci_2 = sayilar.index(2, 2)  # 2. indeksten sonra ara
    print(f"İkinci 2'nin indeksi: {ikinci_2}")
except ValueError as e:
    print(f"Bulunamadı: {e}")

# Güvenli arama
def tuple_arama(t, eleman):
    try:
        return t.index(eleman)
    except ValueError:
        return -1

print(f"Güvenli arama (5): {tuple_arama(sayilar, 5)}")
print(f"Güvenli arama (99): {tuple_arama(sayilar, 99)}")

print("\n5. TUPLE vs LİSTE KARŞILAŞTIRMA:")
print("-" * 30)

# Performans karşılaştırması
import time
import sys

# Bellek kullanımı
liste = [1, 2, 3, 4, 5]
tuple_veri = (1, 2, 3, 4, 5)

print(f"Liste boyutu: {sys.getsizeof(liste)} byte")
print(f"Tuple boyutu: {sys.getsizeof(tuple_veri)} byte")

# Oluşturma hızı
def liste_olustur():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def tuple_olustur():
    return (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Liste oluşturma zamanı
start = time.time()
for _ in range(100000):
    liste_olustur()
liste_zaman = time.time() - start

# Tuple oluşturma zamanı
start = time.time()
for _ in range(100000):
    tuple_olustur()
tuple_zaman = time.time() - start

print(f"\n100.000 liste oluşturma: {liste_zaman:.4f} saniye")
print(f"100.000 tuple oluşturma: {tuple_zaman:.4f} saniye")
print(f"Tuple %{((liste_zaman-tuple_zaman)/liste_zaman*100):.1f} daha hızlı")

# Erişim hızı
büyük_liste = list(range(1000))
büyük_tuple = tuple(range(1000))

# Liste erişim
start = time.time()
for _ in range(100000):
    _ = büyük_liste[500]
liste_erisim = time.time() - start

# Tuple erişim
start = time.time()
for _ in range(100000):
    _ = büyük_tuple[500]
tuple_erisim = time.time() - start

print(f"\nErişim hızı (100.000 kez):")
print(f"Liste: {liste_erisim:.4f} saniye")
print(f"Tuple: {tuple_erisim:.4f} saniye")

print("\n6. TUPLE KULLANIM ALANLARI:")
print("-" * 26)

# 1. Koordinatlar
nokta_2d = (10, 20)
nokta_3d = (10, 20, 30)
print(f"2D nokta: {nokta_2d}")
print(f"3D nokta: {nokta_3d}")

# 2. RGB renk kodları
kırmızı = (255, 0, 0)
yeşil = (0, 255, 0)
mavi = (0, 0, 255)
print(f"Kırmızı RGB: {kırmızı}")

# 3. Veritabanı kayıtları
öğrenci = ("Ali Veli", 20, "Bilgisayar Mühendisliği", 3.45)
print(f"Öğrenci: {öğrenci}")

# 4. Fonksiyon return değerleri
def isim_yas_ayir(tam_bilgi):
    parcalar = tam_bilgi.split("-")
    isim = parcalar[0]
    yas = int(parcalar[1])
    return isim, yas  # Tuple return

ad, yıl = isim_yas_ayir("Mehmet-25")
print(f"Ad: {ad}, Yaş: {yıl}")

# 5. Sözlük anahtarları (immutable olduğu için)
sehir_koordinatlari = {
    ("İstanbul", "Türkiye"): (41.0082, 28.9784),
    ("Paris", "Fransa"): (48.8566, 2.3522),
    ("Tokyo", "Japonya"): (35.6762, 139.6503)
}

print(f"İstanbul koordinatları: {sehir_koordinatlari[('İstanbul', 'Türkiye')]}")

print("\n7. TUPLE UNPACKING (AÇMA):")
print("-" * 26)

# Basit unpacking
kişi = ("Ayşe", "Yılmaz", 28)
ad, soyad, yas = kişi
print(f"Ad: {ad}, Soyad: {soyad}, Yaş: {yas}")

# Değişken değiş tokuşu
a = 10
b = 20
print(f"Önce: a={a}, b={b}")

a, b = b, a  # Çok zarif!
print(f"Sonra: a={a}, b={b}")

# Çoklu atama
x, y, z = 1, 2, 3
print(f"x={x}, y={y}, z={z}")

# Star (*) operatörü ile
sayılar = (1, 2, 3, 4, 5, 6)
ilk, ikinci, *geri_kalan = sayılar
print(f"İlk: {ilk}, İkinci: {ikinci}, Geri kalan: {geri_kalan}")

ilk, *orta, son = sayılar
print(f"İlk: {ilk}, Orta: {orta}, Son: {son}")

# Nested unpacking
iç_içe = ((1, 2), (3, 4))
(a, b), (c, d) = iç_içe
print(f"a={a}, b={b}, c={c}, d={d}")

print("\n8. TUPLE VE DÖNGÜLER:")
print("-" * 20)

# Basit iterasyon
meyveler = ("elma", "armut", "muz", "kiraz")
print("Meyveler:")
for meyve in meyveler:
    print(f"  - {meyve}")

# Enumerate ile
print("\nNumaralı liste:")
for i, meyve in enumerate(meyveler, 1):
    print(f"  {i}. {meyve}")

# Tuple'lar listesi
öğrenciler = [
    ("Ali", 85),
    ("Veli", 92),
    ("Ayşe", 78),
    ("Fatma", 89)
]

print("\nÖğrenci notları:")
for isim, not_ortalaması in öğrenciler:
    print(f"  {isim}: {not_ortalaması}")

# Sözlük items() ile
ülke_başkent = {
    "Türkiye": "Ankara",
    "Fransa": "Paris",
    "Almanya": "Berlin"
}

print("\nÜlke-başkent:")
for ülke, başkent in ülke_başkent.items():
    print(f"  {ülke}: {başkent}")

print("\n9. TUPLE İLE FONKSİYONLAR:")
print("-" * 25)

# Multiple return values
def matematik_işlemler(a, b):
    toplam = a + b
    fark = a - b
    çarpım = a * b
    bölüm = a / b if b != 0 else None
    return toplam, fark, çarpım, bölüm

# Kullanımı
sonuçlar = matematik_işlemler(20, 5)
print(f"Tüm sonuçlar: {sonuçlar}")

# Unpacking ile
top, fr, çarp, böl = matematik_işlemler(20, 5)
print(f"Toplam: {top}, Fark: {fr}, Çarpım: {çarp}, Bölüm: {böl}")

# Named tuple (collections modülü)
from collections import namedtuple

# Named tuple tanımlama
Nokta = namedtuple('Nokta', ['x', 'y'])
Kişi = namedtuple('Kişi', ['ad', 'soyad', 'yas'])

# Kullanımı
p1 = Nokta(10, 20)
print(f"Nokta: {p1}")
print(f"X koordinatı: {p1.x}, Y koordinatı: {p1.y}")

kişi1 = Kişi("Mehmet", "Öz", 30)
print(f"Kişi: {kişi1}")
print(f"Ad: {kişi1.ad}, Yaş: {kişi1.yas}")

# Named tuple metotları
print(f"Kişi alanları: {kişi1._fields}")
kişi_dict = kişi1._asdict()
print(f"Sözlük olarak: {kişi_dict}")

print("\n10. TUPLE DÖNÜŞÜMLER:")
print("-" * 21)

# Tuple'dan liste'ye
tuple_data = (1, 2, 3, 4, 5)
liste_data = list(tuple_data)
print(f"Tuple: {tuple_data}")
print(f"Liste: {liste_data}")

# Liste'den tuple'a
liste_data.append(6)
yeni_tuple = tuple(liste_data)
print(f"Değişen liste: {liste_data}")
print(f"Yeni tuple: {yeni_tuple}")

# String'den tuple
string = "Python"
harf_tuple = tuple(string)
print(f"String: {string}")
print(f"Harf tuple: {harf_tuple}")

# Range'den tuple
range_tuple = tuple(range(5, 11))
print(f"Range tuple: {range_tuple}")

# Set'den tuple (sırasız!)
set_data = {3, 1, 4, 1, 5, 9}
set_tuple = tuple(set_data)
print(f"Set: {set_data}")
print(f"Set tuple: {set_tuple}")

print("\n11. TUPLE ADVANCED KULLANIM:")
print("-" * 27)

# Tuple comprehension (aslında generator)
# Bu tuple değil, generator!
gen = (x**2 for x in range(5))
print(f"Generator: {gen}")
tuple_from_gen = tuple(gen)
print(f"Tuple: {tuple_from_gen}")

# Tuple ile hash
# Tuple'lar hashable (immutable oldukları için)
koordinat_set = {(0, 0), (1, 1), (2, 2)}
print(f"Koordinat seti: {koordinat_set}")

# Dict key olarak kullanım
matrix = {
    (0, 0): "a",
    (0, 1): "b", 
    (1, 0): "c",
    (1, 1): "d"
}
print(f"Matrix: {matrix}")
print(f"(0,1) pozisyonu: {matrix[(0, 1)]}")

# Tuple sorting
öğrenci_notları = [
    ("Ali", 85),
    ("Veli", 92),
    ("Ayşe", 78),
    ("Fatma", 89)
]

print(f"\nSıralama öncesi: {öğrenci_notları}")

# İsme göre sırala
öğrenci_notları.sort()
print(f"İsme göre: {öğrenci_notları}")

# Nota göre sırala
öğrenci_notları.sort(key=lambda x: x[1])
print(f"Nota göre: {öğrenci_notları}")

# Ters sıralama
öğrenci_notları.sort(key=lambda x: x[1], reverse=True)
print(f"Nota göre ters: {öğrenci_notları}")

print("\n12. TUPLE BELLEĞİ VE PERFORMANS:")
print("-" * 30)

# Tuple'ların bellek verimliliği
def bellek_kullanimi():
    import sys
    
    # Farklı boyutlarda karşılaştırma
    boyutlar = [10, 100, 1000]
    
    for boyut in boyutlar:
        liste = list(range(boyut))
        tuple_veri = tuple(range(boyut))
        
        liste_boyut = sys.getsizeof(liste)
        tuple_boyut = sys.getsizeof(tuple_veri)
        
        tasarruf = ((liste_boyut - tuple_boyut) / liste_boyut) * 100
        
        print(f"Boyut {boyut}:")
        print(f"  Liste: {liste_boyut} byte")
        print(f"  Tuple: {tuple_boyut} byte") 
        print(f"  Tasarruf: %{tasarruf:.1f}")

bellek_kullanimi()

print("\n=== TUPLE KULLANIMI ÖZETİ ===")
print("Tuple özellikleri:")
print("  • Immutable (değiştirilemez)")
print("  • Ordered (sıralı)")
print("  • Allows duplicates (tekrar eden elemanlara izin verir)")
print("  • Indexable (indekslenebilir)")
print("  • Iterable (döngülerde kullanılabilir)")
print("  • Hashable (sözlük anahtarı olabilir)")
print()
print("Kullanım alanları:")
print("  • Koordinatlar (x, y, z)")
print("  • RGB renk kodları")
print("  • Veritabanı kayıtları")
print("  • Fonksiyon return değerleri")
print("  • Sözlük anahtarları")
print("  • Sabit konfigürasyon değerleri")
print()
print("Performans avantajları:")
print("  • Liste'den daha az bellek kullanır")
print("  • Daha hızlı oluşturulur")
print("  • Daha hızlı erişilir")
print("  • Hash hesaplama mümkün")
print()
print("Metotları:")
print("  • count(x) - x'in sayısını verir")
print("  • index(x) - x'in pozisyonunu verir")
print()
print("Liste vs Tuple:")
print("  • Liste: Mutable, daha çok özellik")
print("  • Tuple: Immutable, daha performanslı")
print("  • Değişecek veriler → Liste")
print("  • Sabit veriler → Tuple")