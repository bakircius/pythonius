# Liste Temelleri
# Python'da liste oluşturma ve temel işlemler

print("=== LİSTE TEMELLERİ ===\n")

print("1. LİSTE OLUŞTURMA:")
print("-" * 18)

# Boş liste oluşturma
bos_liste = []
bos_liste2 = list()
print(f"Boş liste: {bos_liste}")
print(f"Boş liste (list()): {bos_liste2}")
print(f"Tip: {type(bos_liste)}")

# Eleman ile liste oluşturma
sayilar = [1, 2, 3, 4, 5]
meyveler = ["elma", "armut", "muz", "kiraz"]
karisik = [1, "merhaba", 3.14, True, None]

print(f"\nSayı listesi: {sayilar}")
print(f"String listesi: {meyveler}")
print(f"Karışık liste: {karisik}")

# range() ile liste oluşturma
sayilar_range = list(range(1, 11))
cift_sayilar = list(range(0, 21, 2))
print(f"Range ile: {sayilar_range}")
print(f"Çift sayılar: {cift_sayilar}")

# String'den liste oluşturma
kelime = "Python"
harf_listesi = list(kelime)
print(f"Harf listesi: {harf_listesi}")

print("\n2. LİSTE İNDEKSLEME:")
print("-" * 19)

# Pozitif indeksleme
print(f"Liste: {meyveler}")
print(f"İlk eleman (0): {meyveler[0]}")
print(f"İkinci eleman (1): {meyveler[1]}")
print(f"Son eleman (-1): {meyveler[-1]}")
print(f"Sondan ikinci (-2): {meyveler[-2]}")

# İndeks bilgileri
print(f"\nListe uzunluğu: {len(meyveler)}")
print(f"Geçerli indeksler: 0 ile {len(meyveler)-1} arası")
print(f"Negatif indeksler: -{len(meyveler)} ile -1 arası")

# Hata örnekleri (yorumlanmış)
print(f"\nHata örnekleri:")
print("# meyveler[10]  # IndexError!")
print("# meyveler[-10] # IndexError!")

print("\n3. LİSTE ELEMAN EKLEME:")
print("-" * 21)

# append() - sona ekleme
liste = [1, 2, 3]
print(f"Başlangıç: {liste}")

liste.append(4)
print(f"append(4): {liste}")

liste.append("son")
print(f"append('son'): {liste}")

# insert() - belirli pozisyona ekleme
liste.insert(0, "baş")
print(f"insert(0, 'baş'): {liste}")

liste.insert(2, "orta")
print(f"insert(2, 'orta'): {liste}")

# extend() - başka liste ekleme
liste2 = [10, 20, 30]
liste.extend(liste2)
print(f"extend([10,20,30]): {liste}")

# += operatörü ile ekleme
liste += [40, 50]
print(f"+= [40,50]: {liste}")

print("\n4. LİSTE ELEMAN SİLME:")
print("-" * 20)

# remove() - değere göre silme
meyveler_kopya = ["elma", "armut", "muz", "elma", "kiraz"]
print(f"Başlangıç: {meyveler_kopya}")

meyveler_kopya.remove("elma")  # İlk "elma"yı siler
print(f"remove('elma'): {meyveler_kopya}")

# pop() - indekse göre silme ve döndürme
silinen = meyveler_kopya.pop()  # Son elemanı siler
print(f"pop(): {meyveler_kopya}, silinen: {silinen}")

silinen2 = meyveler_kopya.pop(0)  # İlk elemanı siler
print(f"pop(0): {meyveler_kopya}, silinen: {silinen2}")

# del - indekse göre silme
del meyveler_kopya[1]
print(f"del [1]: {meyveler_kopya}")

# clear() - tüm elemanları silme
temp_liste = [1, 2, 3, 4]
print(f"clear() öncesi: {temp_liste}")
temp_liste.clear()
print(f"clear() sonrası: {temp_liste}")

print("\n5. LİSTE ARAMA VE KONTROL:")
print("-" * 25)

# in operatörü
meyveler = ["elma", "armut", "muz", "kiraz"]
print(f"Liste: {meyveler}")

print(f"'muz' listede var mı? {'muz' in meyveler}")
print(f"'portakal' listede var mı? {'portakal' in meyveler}")

# not in operatörü
print(f"'portakal' listede yok mu? {'portakal' not in meyveler}")

# index() - elemanın indeksini bulma
try:
    muz_index = meyveler.index("muz")
    print(f"'muz'un indeksi: {muz_index}")
except ValueError as e:
    print(f"Bulunamadı: {e}")

# count() - eleman sayısını bulma
tekrar_liste = [1, 2, 3, 2, 2, 4, 2]
print(f"Liste: {tekrar_liste}")
print(f"2 sayısı kaç kez var: {tekrar_liste.count(2)}")
print(f"5 sayısı kaç kez var: {tekrar_liste.count(5)}")

print("\n6. LİSTE SIRALAMA:")
print("-" * 17)

# sort() - listeyi yerinde sıralar
sayilar = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Orijinal: {sayilar}")

sayilar.sort()
print(f"sort(): {sayilar}")

# Ters sıralama
sayilar.sort(reverse=True)
print(f"sort(reverse=True): {sayilar}")

# String sıralama
isimler = ["Zeynep", "Ali", "Mehmet", "Ayşe"]
print(f"\nİsimler: {isimler}")
isimler.sort()
print(f"Alfabetik: {isimler}")

# sorted() - yeni liste döndürür
orijinal = [3, 1, 4, 1, 5]
sirali = sorted(orijinal)
print(f"\nOrijinal: {orijinal}")
print(f"sorted(): {sirali}")

# reverse() - listeyi ters çevir
liste = [1, 2, 3, 4, 5]
print(f"\nOrijinal: {liste}")
liste.reverse()
print(f"reverse(): {liste}")

print("\n7. LİSTE KOPYALAMA:")
print("-" * 19)

# Yüzeysel kopya (shallow copy)
orijinal = [1, 2, 3, 4]
kopya1 = orijinal.copy()
kopya2 = orijinal[:]
kopya3 = list(orijinal)

print(f"Orijinal: {orijinal}")
print(f"copy(): {kopya1}")
print(f"[:]: {kopya2}")
print(f"list(): {kopya3}")

# Referans atama (kopya DEĞİL!)
referans = orijinal
print(f"\nReferans: {referans}")

orijinal.append(5)
print(f"Orijinal değişti: {orijinal}")
print(f"Referans da değişti: {referans}")
print(f"Kopya değişmedi: {kopya1}")

# İç içe liste kopyalama problemi
ic_ice = [[1, 2], [3, 4]]
yuzeysel_kopya = ic_ice.copy()

print(f"\nİç içe orijinal: {ic_ice}")
print(f"Yüzeysel kopya: {yuzeysel_kopya}")

ic_ice[0].append(3)
print(f"Orijinal değişti: {ic_ice}")
print(f"Kopya da etkilendi: {yuzeysel_kopya}")  # Shallow copy problemi

print("\n8. LİSTE BİRLEŞTİRME:")
print("-" * 20)

# + operatörü
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
birlesik = liste1 + liste2
print(f"Liste1: {liste1}")
print(f"Liste2: {liste2}")
print(f"Birleşik (+): {birlesik}")

# * operatörü (tekrarlama)
tekrar = [1, 2] * 3
print(f"[1,2] * 3: {tekrar}")

bos_tekrar = [0] * 5
print(f"[0] * 5: {bos_tekrar}")

print("\n9. LİSTE DİLİMLEME (SLICING) GİRİŞ:")
print("-" * 33)

# Temel dilimleme
sayilar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Liste: {sayilar}")

print(f"İlk 3 eleman [0:3]: {sayilar[0:3]}")
print(f"3. indeksten sona [3:]: {sayilar[3:]}")
print(f"Son 3 eleman [-3:]: {sayilar[-3:]}")
print(f"Tüm liste [:]: {sayilar[:]}")

# Adımlı dilimleme
print(f"Çift indeksler [::2]: {sayilar[::2]}")
print(f"Ters çevirme [::-1]: {sayilar[::-1]}")

print("\n10. LİSTE İTERASYONU:")
print("-" * 20)

# Basit iterasyon
print("Basit iterasyon:")
for meyve in meyveler:
    print(f"Meyve: {meyve}")

# İndeks ile iterasyon
print(f"\nİndeks ile iterasyon:")
for i in range(len(meyveler)):
    print(f"{i}: {meyveler[i]}")

# enumerate ile iterasyon (önerilen)
print(f"\nEnumerate ile:")
for i, meyve in enumerate(meyveler):
    print(f"{i}: {meyve}")

print("\n11. LİSTE METOTLARl ÖZETİ:")
print("-" * 25)

# Tüm metotları gösterme
ornek_liste = [1, 2, 3]
print("Liste metotları:")
metotlar = [metot for metot in dir(ornek_liste) if not metot.startswith('_')]
for metot in metotlar:
    print(f"  {metot}")

print("\n12. PERFORMANCE İPUÇLARI:")
print("-" * 23)

import time

# append vs insert performansı
print("Performance karşılaştırması:")
print("append() vs insert(0) - 1000 eleman:")

# append() testi
start = time.time()
liste_append = []
for i in range(1000):
    liste_append.append(i)
append_time = time.time() - start

# insert(0) testi
start = time.time()
liste_insert = []
for i in range(1000):
    liste_insert.insert(0, i)
insert_time = time.time() - start

print(f"append(): {append_time*1000:.2f} ms")
print(f"insert(0): {insert_time*1000:.2f} ms")
print(f"insert(0) yaklaşık {insert_time/append_time:.1f}x daha yavaş")

print(f"\nBellek kullanımı:")
import sys
liste = [1, 2, 3, 4, 5]
print(f"Liste boyutu: {sys.getsizeof(liste)} bytes")
print(f"Her eleman: ~{sys.getsizeof(liste[0])} bytes")

print("\n=== LİSTE TEMELLERİ ÖZETİ ===")
print("Oluşturma:")
print("  • [] veya list()")
print("  • [1, 2, 3] veya list(range(10))")
print()
print("Temel işlemler:")
print("  • append(x) - sona ekle")
print("  • insert(i, x) - i pozisyonuna ekle")
print("  • remove(x) - x'i sil")
print("  • pop(i) - i pozisyonunu sil ve döndür")
print("  • index(x) - x'in pozisyonunu bul")
print("  • count(x) - x'in sayısını bul")
print()
print("Sıralama:")
print("  • sort() - yerinde sırala")
print("  • sorted() - yeni liste döndür")
print("  • reverse() - ters çevir")
print()
print("Önemli:")
print("  • Mutable (değiştirilebilir)")
print("  • Sıralı (ordered)")
print("  • Tekrar eden elemanlar olabilir")
print("  • Farklı tipler aynı listede olabilir")