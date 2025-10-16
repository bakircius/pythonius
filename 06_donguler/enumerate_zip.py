# Enumerate ve Zip Fonksiyonları
# İleri düzey döngü teknikleri

print("=== ENUMERATE VE ZIP FONKSİYONLARI ===\n")

print("1. ENUMERATE() FONKSİYONU:")
print("-" * 26)

# Temel enumerate kullanımı
meyveler = ["elma", "armut", "muz", "kiraz", "üzüm"]
print("Temel enumerate kullanımı:")

for index, meyve in enumerate(meyveler):
    print(f"{index}: {meyve}")

# Enumerate nesnesinin yapısı
print(f"\nEnumerate nesnesi:")
enum_obj = enumerate(meyveler)
print(f"Type: {type(enum_obj)}")
print(f"Liste olarak: {list(enumerate(meyveler))}")

# Farklı başlangıç değeri
print(f"\nFarklı başlangıç değeri (start=1):")
for index, meyve in enumerate(meyveler, start=1):
    print(f"{index}. {meyve}")

# Negatif başlangıç
print(f"\nNegatif başlangıç (start=-2):")
for index, meyve in enumerate(meyveler, start=-2):
    print(f"{index}: {meyve}")

print("\n2. ENUMERATE İLE PRATİK KULLANIM:")
print("-" * 33)

# Çift indeksli elemanları bulma
sayilar = [10, 25, 30, 45, 50, 65, 70]
print(f"Sayılar: {sayilar}")
print("Çift indeksli elemanlar:")

for i, sayi in enumerate(sayilar):
    if i % 2 == 0:
        print(f"Index {i}: {sayi}")

# İlk ve son eleman özel işleme
print(f"\nİlk ve son eleman özel işleme:")
kelimeler = ["Python", "Java", "JavaScript", "C++", "Go"]

for i, kelime in enumerate(kelimeler):
    if i == 0:
        print(f"İlk: {kelime}")
    elif i == len(kelimeler) - 1:
        print(f"Son: {kelime}")
    else:
        print(f"Orta: {kelime}")

# Belirli koşullarda indeks kaydetme
print(f"\nBüyük sayıların indeksleri:")
sayilar = [5, 12, 8, 23, 15, 30, 7, 25]
buyuk_sayi_indeksleri = []

for i, sayi in enumerate(sayilar):
    if sayi > 15:
        buyuk_sayi_indeksleri.append(i)
        print(f"Index {i}: {sayi} > 15")

print(f"Büyük sayı indeksleri: {buyuk_sayi_indeksleri}")

print("\n3. ZIP() FONKSİYONU:")
print("-" * 19)

# Temel zip kullanımı
isimler = ["Ali", "Ayşe", "Mehmet", "Fatma"]
yaslar = [25, 30, 35, 28]

print("Temel zip kullanımı:")
for isim, yas in zip(isimler, yaslar):
    print(f"{isim}: {yas} yaşında")

# Zip nesnesinin yapısı
print(f"\nZip nesnesi:")
zip_obj = zip(isimler, yaslar)
print(f"Type: {type(zip_obj)}")
print(f"Liste olarak: {list(zip(isimler, yaslar))}")

# Üç liste birleştirme
sehirler = ["İstanbul", "Ankara", "İzmir", "Bursa"]
print(f"\nÜç liste birleştirme:")

for isim, yas, sehir in zip(isimler, yaslar, sehirler):
    print(f"{isim} ({yas}) - {sehir}")

print("\n4. FARKLI UZUNLUKTAKI LİSTELER:")
print("-" * 34)

# Farklı uzunluktaki listelerde zip
liste1 = [1, 2, 3, 4, 5]
liste2 = ["a", "b", "c"]
liste3 = [10, 20]

print(f"Liste 1: {liste1}")
print(f"Liste 2: {liste2}")
print(f"Liste 3: {liste3}")

print(f"\nZip sonucu (en kısa liste belirler):")
for item1, item2, item3 in zip(liste1, liste2, liste3):
    print(f"{item1} - {item2} - {item3}")

# zip_longest ile tüm elemanları kullanma
from itertools import zip_longest

print(f"\nzip_longest ile (eksik yerler None):")
for item1, item2, item3 in zip_longest(liste1, liste2, liste3):
    print(f"{item1} - {item2} - {item3}")

# Özel dolgu değeri
print(f"\nzip_longest ile özel dolgu:")
for item1, item2, item3 in zip_longest(liste1, liste2, liste3, fillvalue="---"):
    print(f"{item1} - {item2} - {item3}")

print("\n5. SÖZLÜK OLUŞTURMA:")
print("-" * 21)

# Zip ile sözlük oluşturma
anahtarlar = ["isim", "yas", "sehir", "meslek"]
degerler = ["Ahmet", 32, "İstanbul", "Mühendis"]

kisi = dict(zip(anahtarlar, degerler))
print(f"Oluşturulan sözlük: {kisi}")

# Birden fazla sözlük oluşturma
print(f"\nBirden fazla sözlük:")
kisi_listesi = [
    ["Ali", 25, "İstanbul"],
    ["Ayşe", 30, "Ankara"],
    ["Mehmet", 35, "İzmir"]
]

alanlar = ["isim", "yas", "sehir"]
kisiler = []

for kisi_bilgileri in kisi_listesi:
    kisi_dict = dict(zip(alanlar, kisi_bilgileri))
    kisiler.append(kisi_dict)
    print(kisi_dict)

print("\n6. ENUMERATE VE ZIP BİRLİKTE:")
print("-" * 29)

# Her iki fonksiyonu birlikte kullanma
takimlar = ["Galatasaray", "Fenerbahçe", "Beşiktaş"]
puanlar = [75, 72, 68]

print("Lig tablosu:")
for sira, (takim, puan) in enumerate(zip(takimlar, puanlar), start=1):
    print(f"{sira}. {takim}: {puan} puan")

# Karmaşık veri yapısı
print(f"\nÖğrenci sınav sonuçları:")
ogrenciler = ["Ali", "Ayşe", "Mehmet", "Fatma"]
matematik = [85, 92, 78, 88]
fizik = [90, 85, 82, 91]
kimya = [88, 89, 85, 87]

for sira, (isim, mat, fiz, kim) in enumerate(zip(ogrenciler, matematik, fizik, kimya), 1):
    ortalama = (mat + fiz + kim) / 3
    print(f"{sira}. {isim}: Mat={mat}, Fiz={fiz}, Kim={kim}, Ort={ortalama:.1f}")

print("\n7. LİSTE İŞLEMLERİ:")
print("-" * 18)

# Paralel liste işlemleri
x_koordinatlar = [1, 2, 3, 4, 5]
y_koordinatlar = [2, 4, 1, 3, 5]

print("Koordinat noktaları:")
for i, (x, y) in enumerate(zip(x_koordinatlar, y_koordinatlar)):
    mesafe = (x**2 + y**2)**0.5
    print(f"Nokta {i+1}: ({x},{y}) - Orijine uzaklık: {mesafe:.2f}")

# İki liste karşılaştırma
liste_a = [1, 2, 3, 4, 5]
liste_b = [1, 2, 7, 4, 9]

print(f"\nListe karşılaştırma:")
print(f"Liste A: {liste_a}")
print(f"Liste B: {liste_b}")

for i, (a, b) in enumerate(zip(liste_a, liste_b)):
    if a == b:
        print(f"Index {i}: {a} = {b} ✓")
    else:
        print(f"Index {i}: {a} ≠ {b} ✗")

print("\n8. MATRIX İŞLEMLERİ:")
print("-" * 19)

# Matris transpose (devrik)
print("Matris transpose:")
matris = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Orijinal matris:")
for satir in matris:
    print(satir)

# Zip ile transpose
print(f"\nTranspose (zip ile):")
transpose = list(zip(*matris))
for satir in transpose:
    print(list(satir))

# Manuel transpose
print(f"\nTranspose (manuel):")
transpose_manuel = []
for j in range(len(matris[0])):
    sutun = []
    for i in range(len(matris)):
        sutun.append(matris[i][j])
    transpose_manuel.append(sutun)

for satir in transpose_manuel:
    print(satir)

# Matris çarpımında kullanım
print(f"\nİki matris eleman eleman çarpımı:")
matris1 = [[1, 2], [3, 4]]
matris2 = [[5, 6], [7, 8]]

sonuc = []
for satir1, satir2 in zip(matris1, matris2):
    sonuc_satir = []
    for eleman1, eleman2 in zip(satir1, satir2):
        sonuc_satir.append(eleman1 * eleman2)
    sonuc.append(sonuc_satir)

print(f"Matris 1: {matris1}")
print(f"Matris 2: {matris2}")
print(f"Çarpım: {sonuc}")

print("\n9. STATİSTİKSEL İŞLEMLER:")
print("-" * 25)

# Korelasyon hesaplama
x_verileri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_verileri = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print(f"X verileri: {x_verileri}")
print(f"Y verileri: {y_verileri}")

# Ortalama hesaplama
x_ortalama = sum(x_verileri) / len(x_verileri)
y_ortalama = sum(y_verileri) / len(y_verileri)

print(f"X ortalaması: {x_ortalama}")
print(f"Y ortalaması: {y_ortalama}")

# Kovaryanş hesaplama
kovaryan = 0
for x, y in zip(x_verileri, y_verileri):
    kovaryan += (x - x_ortalama) * (y - y_ortalama)
kovaryan /= len(x_verileri)

print(f"Kovaryans: {kovaryan:.2f}")

# Veri noktalarını eşleştirme
print(f"\nVeri noktaları:")
for i, (x, y) in enumerate(zip(x_verileri, y_verileri), 1):
    print(f"Nokta {i:2}: X={x:2}, Y={y:2}")

print("\n10. DOSYA İŞLEMLERİ SİMÜLASYONU:")
print("-" * 32)

# CSV benzeri veri işleme
print("CSV veri işleme simülasyonu:")
basliklar = ["Ad", "Soyad", "Yaş", "Şehir", "Maaş"]
satir1 = ["Ali", "Yılmaz", "25", "İstanbul", "5000"]
satir2 = ["Ayşe", "Demir", "30", "Ankara", "6000"]
satir3 = ["Mehmet", "Kaya", "35", "İzmir", "5500"]

veriler = [satir1, satir2, satir3]

print("Tablo formatı:")
# Başlık yazdır
for i, baslik in enumerate(basliklar):
    print(f"{baslik:>10}", end="")
print()
print("-" * 50)

# Veri satırlarını yazdır
for satir_no, satir in enumerate(veriler, 1):
    for veri in satir:
        print(f"{veri:>10}", end="")
    print()

# Specific field access
print(f"\nSadece isim ve maaş:")
for satir in veriler:
    isim, soyad, yas, sehir, maas = satir
    print(f"{isim} {soyad}: {maas} TL")

print("\n11. PERFORMANS VE BEST PRACTICES:")
print("-" * 34)

# Performans karşılaştırması
import time

# Test verisi
buyuk_liste1 = list(range(10000))
buyuk_liste2 = list(range(10000, 20000))

# enumerate kullanımı
start = time.time()
sonuc1 = []
for i, deger in enumerate(buyuk_liste1):
    sonuc1.append((i, deger, buyuk_liste2[i]))
enumerate_time = time.time() - start

# zip kullanımı
start = time.time()
sonuc2 = list(zip(range(len(buyuk_liste1)), buyuk_liste1, buyuk_liste2))
zip_time = time.time() - start

print(f"Enumerate yöntemi: {enumerate_time*1000:.2f} ms")
print(f"Zip yöntemi: {zip_time*1000:.2f} ms")
print(f"Zip yaklaşık {enumerate_time/zip_time:.1f}x daha hızlı")

print("\n=== ENUMERATE VE ZIP ÖZETİ ===")
print("enumerate(iterable, start=0):")
print("  • (index, değer) tuple'ları döner")
print("  • start parametresi ile başlangıç ayarlanır")
print("  • range(len()) yerine tercih edilir")
print()
print("zip(*iterables):")
print("  • Birden fazla iterable'ı eşleştirir")
print("  • En kısa iterable'da durur")
print("  • Paralel işlemler için ideal")
print()
print("Kullanım alanları:")
print("  • Liste indeks erişimi (enumerate)")
print("  • Paralel liste işleme (zip)")
print("  • Sözlük oluşturma (zip)")
print("  • Matris işlemleri (zip)")
print("  • CSV/tablo verisi (her ikisi)")
print()
print("İpuçları:")
print("  • zip(*matrix) ile transpose")
print("  • dict(zip()) ile sözlük oluştur")
print("  • enumerate() start parametresini kullan")
print("  • zip_longest() farklı uzunluklar için")
print("  • Memory efficient - generator döner")