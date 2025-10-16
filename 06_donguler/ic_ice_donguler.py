# İç İçe Döngüler (Nested Loops)
# Çok boyutlu veri yapıları ve karmaşık işlemler

print("=== İÇ İÇE DÖNGÜLER (NESTED LOOPS) ===\n")

print("1. TEMEL İÇ İÇE DÖNGÜ:")
print("-" * 24)

# Basit iç içe döngü
print("İç içe döngü örneği:")
for i in range(1, 4):
    print(f"Dış döngü: i = {i}")
    for j in range(1, 4):
        print(f"  İç döngü: j = {j}")
    print()

# Koordinat sistemi
print("Koordinat sistemi (3x3):")
for x in range(3):
    for y in range(3):
        print(f"({x},{y})", end="  ")
    print()

print("\n2. ÇARPIM TABLOSU:")
print("-" * 18)

# Klasik çarpım tablosu
print("Çarpım tablosu (5x5):")
print("    ", end="")
for j in range(1, 6):
    print(f"{j:3}", end="")
print()

for i in range(1, 6):
    print(f"{i:2}: ", end="")
    for j in range(1, 6):
        print(f"{i*j:3}", end="")
    print()

# Üçgen çarpım tablosu
print(f"\nÜçgen çarpım tablosu:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(f"{i}x{j}={i*j:2}", end="  ")
    print()

print("\n3. MATRİS İŞLEMLERİ:")
print("-" * 19)

# Matris oluşturma
print("3x4 Matris oluşturma:")
matris = []
for i in range(3):
    satir = []
    for j in range(4):
        deger = i * 4 + j + 1
        satir.append(deger)
    matris.append(satir)
    print(f"Satır {i}: {satir}")

print(f"\nOluşan matris:")
for satir in matris:
    for eleman in satir:
        print(f"{eleman:3}", end="")
    print()

# Matris toplama
print(f"\nMatris toplama:")
matris1 = [[1, 2, 3], [4, 5, 6]]
matris2 = [[7, 8, 9], [10, 11, 12]]
sonuc = []

print("Matris 1:")
for satir in matris1:
    print(satir)

print("Matris 2:")
for satir in matris2:
    print(satir)

print("Toplam:")
for i in range(len(matris1)):
    satir_sonuc = []
    for j in range(len(matris1[0])):
        toplam = matris1[i][j] + matris2[i][j]
        satir_sonuc.append(toplam)
    sonuc.append(satir_sonuc)
    print(satir_sonuc)

print("\n4. DESEN ÇİZİMİ:")
print("-" * 16)

# Yıldız desenleri
print("Yıldız üçgeni:")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

print(f"\nTersten yıldız üçgeni:")
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

print(f"\nOrtalanmış üçgen:")
for i in range(1, 6):
    # Boşluklar
    for j in range(5 - i):
        print(" ", end="")
    # Yıldızlar
    for j in range(i):
        print("* ", end="")
    print()

print(f"\nSayı piramidi:")
for i in range(1, 6):
    # Boşluklar
    for j in range(5 - i):
        print(" ", end="")
    # Artan sayılar
    for j in range(1, i + 1):
        print(j, end="")
    # Azalan sayılar
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()

print("\n5. LİSTE İŞLEMLERİ:")
print("-" * 18)

# Liste içinde liste arama
print("İç içe liste arama:")
veriler = [
    ["Ali", 25, "İstanbul"],
    ["Ayşe", 30, "Ankara"],
    ["Mehmet", 28, "İzmir"],
    ["Fatma", 35, "Bursa"]
]

print("Tüm veriler:")
for i, kisi in enumerate(veriler):
    print(f"Kişi {i + 1}:")
    for j, bilgi in enumerate(kisi):
        etiketler = ["İsim", "Yaş", "Şehir"]
        print(f"  {etiketler[j]}: {bilgi}")

# Belirli kritere göre arama
print(f"\n30 yaş üstü kişiler:")
for kisi in veriler:
    isim, yas, sehir = kisi
    if yas > 30:
        print(f"{isim} ({yas} yaşında) - {sehir}")

# İstatistik hesaplama
print(f"\nŞehir bazında sayım:")
sehir_sayimi = {}
for kisi in veriler:
    sehir = kisi[2]
    if sehir in sehir_sayimi:
        sehir_sayimi[sehir] += 1
    else:
        sehir_sayimi[sehir] = 1

for sehir, sayi in sehir_sayimi.items():
    print(f"{sehir}: {sayi} kişi")

print("\n6. OYUN TAHTASI:")
print("-" * 16)

# Satranç tahtası
print("Satranç tahtası (8x8):")
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print("⬜", end="")
        else:
            print("⬛", end="")
    print()

# Tic-tac-toe tahtası
print(f"\nTic-tac-toe örneği:")
tahta = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["X", "O", "X"]
]

for i, satir in enumerate(tahta):
    for j, hucre in enumerate(satir):
        print(f" {hucre} ", end="")
        if j < len(satir) - 1:
            print("|", end="")
    print()
    if i < len(tahta) - 1:
        print("---|---|---")

print("\n7. ASAL SAYI ÇİFTLERİ:")
print("-" * 21)

# İkiz asal sayı bulma
print("İkiz asal sayılar (50'ye kadar):")
def asal_mi(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

ikiz_asallar = []
for i in range(2, 48):  # 50'ye kadar
    if asal_mi(i) and asal_mi(i + 2):
        ikiz_asallar.append((i, i + 2))
        print(f"({i}, {i + 2})")

print(f"Toplam {len(ikiz_asallar)} ikiz asal çift bulundu")

print("\n8. SÖZLÜK İÇ İÇE İŞLEMLER:")
print("-" * 26)

# Öğrenci notları
ogrenci_notlari = {
    "Ali": {"Matematik": 85, "Fizik": 92, "Kimya": 78},
    "Ayşe": {"Matematik": 96, "Fizik": 89, "Kimya": 94},
    "Mehmet": {"Matematik": 72, "Fizik": 81, "Kimya": 69}
}

print("Öğrenci not raporu:")
for ogrenci, dersler in ogrenci_notlari.items():
    print(f"\n{ogrenci}:")
    toplam = 0
    ders_sayisi = 0
    
    for ders, not_degeri in dersler.items():
        print(f"  {ders}: {not_degeri}")
        toplam += not_degeri
        ders_sayisi += 1
    
    ortalama = toplam / ders_sayisi
    print(f"  Ortalama: {ortalama:.2f}")

# Ders bazında istatistik
print(f"\nDers bazında istatistikler:")
ders_istatistikleri = {}

for ogrenci, dersler in ogrenci_notlari.items():
    for ders, not_degeri in dersler.items():
        if ders not in ders_istatistikleri:
            ders_istatistikleri[ders] = []
        ders_istatistikleri[ders].append(not_degeri)

for ders, notlar in ders_istatistikleri.items():
    ortalama = sum(notlar) / len(notlar)
    en_yuksek = max(notlar)
    en_dusuk = min(notlar)
    print(f"{ders}: Ort={ortalama:.1f}, Max={en_yuksek}, Min={en_dusuk}")

print("\n9. PERFORMANS KARŞILAŞTIRMA:")
print("-" * 26)

# İç içe döngü vs list comprehension
import time

print("Performance testi (1000x1000 matris):")

# Geleneksel iç içe döngü
start_time = time.time()
matris_traditional = []
for i in range(100):  # Küçültülmüş test
    satir = []
    for j in range(100):
        satir.append(i * j)
    matris_traditional.append(satir)
end_time = time.time()
print(f"Geleneksel yöntem: {(end_time - start_time)*1000:.2f} ms")

# List comprehension
start_time = time.time()
matris_comprehension = [[i * j for j in range(100)] for i in range(100)]
end_time = time.time()
print(f"List comprehension: {(end_time - start_time)*1000:.2f} ms")

print("List comprehension genellikle daha hızlıdır!")

print("\n10. KARMAŞIK ARAMA ALGORİTMALARI:")
print("-" * 32)

# Maze (labirent) benzeri arama
print("Grid'de yol bulma:")
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

print("Grid (0=yol, 1=engel):")
for satir in grid:
    for hucre in satir:
        print(f"{hucre} ", end="")
    print()

# Basit yol bulma (sadece sağ ve aşağı)
print(f"\nBasit yol arama (0,0)'dan (4,4)'e:")
def yol_var_mi(grid, x, y, hedef_x, hedef_y, yol=[]):
    # Sınır kontrolü
    if x >= len(grid) or y >= len(grid[0]):
        return False
    
    # Engel kontrolü
    if grid[x][y] == 1:
        return False
    
    # Hedef kontrolü
    if x == hedef_x and y == hedef_y:
        yol.append((x, y))
        return True
    
    # Ziyaret edildi işaretle (geçici)
    yol.append((x, y))
    
    # Sağa git
    if yol_var_mi(grid, x, y + 1, hedef_x, hedef_y, yol.copy()):
        return True
    
    # Aşağı git
    if yol_var_mi(grid, x + 1, y, hedef_x, hedef_y, yol.copy()):
        return True
    
    return False

# Not: Bu basit örnek, gerçek pathfinding için daha gelişmiş algoritmalar gerekir
print("Basit yol arama algoritması çalıştırıldı")

print("\n11. DEBUGGING İÇ İÇE DÖNGÜLER:")
print("-" * 30)

# Debug modlu iç içe döngü
DEBUG = True
print("Debug modlu matris işleme:")

for i in range(3):
    if DEBUG:
        print(f"DEBUG: Dış döngü iterasyon {i}")
    
    for j in range(3):
        if DEBUG:
            print(f"  DEBUG: İç döngü iterasyon {j}")
        
        deger = i * 3 + j
        if DEBUG:
            print(f"  DEBUG: Hesaplanan değer: {deger}")
        
        print(f"    Matris[{i}][{j}] = {deger}")

print("\n=== İÇ İÇE DÖNGÜ ÖZETİ ===")
print("Kullanım alanları:")
print("  • Matris/tablo işlemleri")
print("  • Çok boyutlu veri yapıları")
print("  • Kombinatorik problemler")
print("  • Desen çizimi")
print("  • Oyun tahtaları")
print()
print("Performans ipuçları:")
print("  • Mümkünse list comprehension kullan")
print("  • Gereksiz döngü seviyelerinden kaçın")
print("  • Erken çıkış (break) kullan")
print("  • İç döngüde pahalı işlemler yapma")
print()
print("Yaygın hatalar:")
print("  • Sonsuz döngü oluşturma")
print("  • Yanlış indeks kullanımı")
print("  • Bellek aşımı (çok büyük yapılar)")
print("  • Break/continue karıştırma")
print()
print("Alternatifler:")
print("  • NumPy (numerical operations)")
print("  • itertools modülü")
print("  • Functional programming")
print("  • Generator expressions")