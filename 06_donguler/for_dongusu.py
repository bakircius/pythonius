# For Döngüsü ve Range Kullanımı
# Python'da for döngüsü ve range() fonksiyonu

print("=== FOR DÖNGÜSÜ VE RANGE KULLANIMI ===\n")

print("1. TEMEL FOR DÖNGÜSÜ:")
print("-" * 21)

# Basit for döngüsü
print("1'den 5'e kadar sayılar:")
for i in range(1, 6):
    print(f"Sayı: {i}")

print("\nListe elemanları:")
meyveler = ["elma", "armut", "muz", "kiraz"]
for meyve in meyveler:
    print(f"Meyve: {meyve}")

print("\n2. RANGE() FONKSİYONU:")
print("-" * 21)

# range() farklı kullanımları
print("range(5):")
for i in range(5):
    print(i, end=" ")
print()

print("\nrange(2, 8):")
for i in range(2, 8):
    print(i, end=" ")
print()

print("\nrange(0, 10, 2):")
for i in range(0, 10, 2):
    print(i, end=" ")
print()

print("\nrange(10, 0, -1):")
for i in range(10, 0, -1):
    print(i, end=" ")
print()

# range() detayları
print(f"\nrange objesi: {range(5)}")
print(f"Liste olarak: {list(range(5))}")
print(f"Tip: {type(range(5))}")

print("\n3. STRING İTERASYONU:")
print("-" * 22)

# String karakterleri üzerinde döngü
kelime = "Python"
print(f"'{kelime}' kelimesinin harfleri:")
for harf in kelime:
    print(f"Harf: {harf}")

# String ile numaralama
print(f"\nNumaralı harfler:")
for i, harf in enumerate(kelime):
    print(f"{i}: {harf}")

print("\n4. LİSTE İŞLEMLERİ:")
print("-" * 18)

# Liste elemanları üzerinde işlem
sayilar = [1, 2, 3, 4, 5]
print(f"Orijinal liste: {sayilar}")

print("Kareler:")
for sayi in sayilar:
    kare = sayi ** 2
    print(f"{sayi}² = {kare}")

# Liste indeks erişimi
print(f"\nİndeks ile erişim:")
for i in range(len(sayilar)):
    print(f"sayilar[{i}] = {sayilar[i]}")

# enumerate() kullanımı (önerilen)
print(f"\nenumerate() ile:")
for index, deger in enumerate(sayilar):
    print(f"İndeks {index}: {deger}")

print("\n5. SÖZLÜK İTERASYONU:")
print("-" * 21)

# Sözlük üzerinde döngü
kisi = {
    "ad": "Ahmet",
    "soyad": "Yılmaz",
    "yaş": 30,
    "şehir": "İstanbul"
}

print("Sadece anahtarlar:")
for anahtar in kisi:
    print(f"Anahtar: {anahtar}")

print("\nSadece değerler:")
for deger in kisi.values():
    print(f"Değer: {deger}")

print("\nAnahtar-değer çiftleri:")
for anahtar, deger in kisi.items():
    print(f"{anahtar}: {deger}")

print("\n6. İÇ İÇE DÖNGÜLER:")
print("-" * 19)

# Çarpım tablosu
print("3x3 Çarpım tablosu:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end="\t")
    print()  # Yeni satır

# Matris işlemleri
print("\nMatris örnegi:")
matris = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for satir in matris:
    for eleman in satir:
        print(f"{eleman:2}", end=" ")
    print()

print("\n7. RANGE İLE MATEMATİKSEL İŞLEMLER:")
print("-" * 35)

# Toplam hesaplama
print("1'den 10'a kadar toplam:")
toplam = 0
for i in range(1, 11):
    toplam += i
    print(f"i={i}, toplam={toplam}")

# Faktöriyel hesaplama
n = 5
faktoriyel = 1
print(f"\n{n}! hesaplama:")
for i in range(1, n + 1):
    faktoriyel *= i
    print(f"{i}! = {faktoriyel}")

# Fibonacci serisi
print(f"\nİlk 10 Fibonacci sayısı:")
a, b = 0, 1
print(f"F(0) = {a}")
print(f"F(1) = {b}")
for i in range(2, 10):
    c = a + b
    print(f"F({i}) = {c}")
    a, b = b, c

print("\n8. LİST COMPREHENSION GİRİŞ:")
print("-" * 28)

# Geleneksel yöntem
kareler = []
for i in range(1, 6):
    kareler.append(i ** 2)
print(f"Geleneksel yöntem: {kareler}")

# List comprehension
kareler_lc = [i ** 2 for i in range(1, 6)]
print(f"List comprehension: {kareler_lc}")

# Koşullu list comprehension
cift_kareler = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(f"Çift sayıların kareleri: {cift_kareler}")

print("\n9. ENUMERATE() DETAYli KULLANIM:")
print("-" * 31)

# enumerate() farklı başlangıç
gunler = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"]

print("0'dan başlayarak:")
for index, gun in enumerate(gunler):
    print(f"{index}: {gun}")

print("\n1'den başlayarak:")
for index, gun in enumerate(gunler, 1):
    print(f"{index}: {gun}")

# enumerate() ile list comprehension
numarali_gunler = [(i, gun) for i, gun in enumerate(gunler, 1)]
print(f"\nNumaralı günler: {numarali_gunler}")

print("\n10. ZIP() FONKSİYONU:")
print("-" * 19)

# İki listeyi eşleştirme
isimler = ["Ali", "Ayşe", "Mehmet"]
yaslar = [25, 30, 35]

print("zip() ile eşleştirme:")
for isim, yas in zip(isimler, yaslar):
    print(f"{isim}: {yas} yaşında")

# Farklı uzunluktaki listeler
notlar = [85, 92]  # Daha kısa liste
print(f"\nFarklı uzunlukta listeler:")
for isim, yas, not_degeri in zip(isimler, yaslar, notlar):
    print(f"{isim} ({yas}): {not_degeri}")

# zip() ile sözlük oluşturma
kisi_sozlugu = dict(zip(isimler, yaslar))
print(f"\nSözlük: {kisi_sozlugu}")

print("\n11. RANGE() İLE ÖZEL DESENLER:")
print("-" * 29)

# Geriye sayma
print("10'dan 1'e geriye sayma:")
for i in range(10, 0, -1):
    print(i, end=" ")
print()

# Çift sayılar
print("\n0-20 arası çift sayılar:")
for i in range(0, 21, 2):
    print(i, end=" ")
print()

# 5'in katları
print("\n50'ye kadar 5'in katları:")
for i in range(5, 51, 5):
    print(i, end=" ")
print()

print("\n12. PRATİK ÖRNEKLER:")
print("-" * 19)

# Yıldız deseni
print("Yıldız üçgeni:")
for i in range(1, 6):
    print("*" * i)

# Tersten yıldız
print("\nTersten yıldız:")
for i in range(5, 0, -1):
    print("*" * i)

# Sayı piramidi
print("\nSayı piramidi:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Asal sayı kontrolü
print("\n2-20 arası asal sayılar:")
for sayi in range(2, 21):
    asal = True
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            asal = False
            break
    if asal:
        print(sayi, end=" ")
print()

print("\n13. PERFORMANCE İPUÇLARI:")
print("-" * 25)

# range() vs list
print("range() memory efficient:")
print(f"range(1000000) boyutu: {range(1000000).__sizeof__()} bytes")
print(f"list(range(1000)) boyutu: {list(range(1000)).__sizeof__()} bytes")

# enumerate() vs range(len())
liste = ["a", "b", "c", "d", "e"]

print("\nÖnerilmeyen yöntem:")
for i in range(len(liste)):
    print(f"{i}: {liste[i]}")

print("\nÖnerilen yöntem:")
for i, eleman in enumerate(liste):
    print(f"{i}: {eleman}")

print("\n=== FOR DÖNGÜSÜ ÖZETİ ===")
print("Temel söz dizimi:")
print("for değişken in iterable:")
print("    # kod bloku")
print()
print("range() kullanımları:")
print("range(n)           # 0'dan n-1'e")
print("range(start, stop) # start'tan stop-1'e")
print("range(start, stop, step) # adım ile")
print()
print("Yararlı fonksiyonlar:")
print("enumerate(list)    # (index, değer) çiftleri")
print("zip(list1, list2)  # Listeleri eşleştir")
print("reversed(list)     # Tersten iterasyon")
print()
print("İpuçları:")
print("• range() memory efficient")
print("• enumerate() tercih et range(len()) yerine")
print("• zip() farklı uzunluktaki listelerde durur")
print("• List comprehension kısa listeler için hızlı")