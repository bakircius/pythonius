# Liste Metotları ve Kullanımları
# Python liste metotlarının detaylı incelenmesi

print("=== LİSTE METOTLARI VE KULLANIMLARI ===\n")

print("1. APPEND() - SONA EKLEME:")
print("-" * 26)

# append() temel kullanım
meyveler = ["elma", "armut"]
print(f"Başlangıç: {meyveler}")

meyveler.append("muz")
print(f"append('muz'): {meyveler}")

meyveler.append("kiraz")
print(f"append('kiraz'): {meyveler}")

# Farklı tipleri ekleme
meyveler.append(5)
meyveler.append([1, 2, 3])
print(f"Farklı tipler: {meyveler}")

# Döngü ile ekleme
sayilar = []
for i in range(1, 6):
    sayilar.append(i * i)
print(f"Kareler: {sayilar}")

print("\n2. INSERT() - BELİRLİ POZİSYONA EKLEME:")
print("-" * 36)

# insert() temel kullanım
liste = [1, 3, 5]
print(f"Başlangıç: {liste}")

liste.insert(0, 0)  # Başa ekleme
print(f"insert(0, 0): {liste}")

liste.insert(2, 2)  # Ortaya ekleme
print(f"insert(2, 2): {liste}")

liste.insert(10, 99)  # Sınır dışı indeks - sona eklenir
print(f"insert(10, 99): {liste}")

# Negatif indeks
liste.insert(-1, "son_oncesi")
print(f"insert(-1, 'son_oncesi'): {liste}")

# Performance not
import time
print(f"\nPerformance karşılaştırması:")

# Başa ekleme (yavaş)
start = time.time()
test_liste = []
for i in range(1000):
    test_liste.insert(0, i)
insert_time = time.time() - start

# Sona ekleme (hızlı)
start = time.time()
test_liste2 = []
for i in range(1000):
    test_liste2.append(i)
append_time = time.time() - start

print(f"insert(0): {insert_time*1000:.2f} ms")
print(f"append(): {append_time*1000:.2f} ms")

print("\n3. EXTEND() - LİSTE BİRLEŞTİRME:")
print("-" * 30)

# extend() vs append() farkı
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]

print(f"Liste1: {liste1}")
print(f"Liste2: {liste2}")

# extend() kullanımı
liste1_kopya = liste1.copy()
liste1_kopya.extend(liste2)
print(f"extend() sonrası: {liste1_kopya}")

# append() ile karşılaştırma
liste1_kopya2 = liste1.copy()
liste1_kopya2.append(liste2)
print(f"append() ile: {liste1_kopya2}")

# Farklı iterable'larla extend
liste = [1, 2, 3]
liste.extend("abc")
print(f"String ile extend: {liste}")

liste.extend(range(4, 7))
print(f"Range ile extend: {liste}")

liste.extend((7, 8, 9))
print(f"Tuple ile extend: {liste}")

print("\n4. REMOVE() - DEĞERE GÖRE SİLME:")
print("-" * 30)

# remove() temel kullanım
hayvanlar = ["kedi", "köpek", "kuş", "kedi", "balık"]
print(f"Başlangıç: {hayvanlar}")

hayvanlar.remove("kedi")  # İlk "kedi"yi siler
print(f"remove('kedi'): {hayvanlar}")

# Olmayan eleman silmeye çalışma
try:
    hayvanlar.remove("aslan")
except ValueError as e:
    print(f"Hata: {e}")

# Güvenli remove
def guvenli_remove(liste, eleman):
    if eleman in liste:
        liste.remove(eleman)
        return True
    return False

sonuc = guvenli_remove(hayvanlar, "köpek")
print(f"Güvenli remove ('köpek'): {sonuc}, Liste: {hayvanlar}")

sonuc = guvenli_remove(hayvanlar, "aslan")
print(f"Güvenli remove ('aslan'): {sonuc}, Liste: {hayvanlar}")

# Tüm aynı elemanları silme
sayilar = [1, 2, 3, 2, 4, 2, 5]
print(f"\nTüm 2'leri silme: {sayilar}")
while 2 in sayilar:
    sayilar.remove(2)
print(f"Sonuç: {sayilar}")

print("\n5. POP() - İNDEKSE GÖRE SİLME:")
print("-" * 27)

# pop() temel kullanım
renkler = ["kırmızı", "yeşil", "mavi", "sarı", "mor"]
print(f"Başlangıç: {renkler}")

# Son eleman
silinen = renkler.pop()
print(f"pop(): {renkler}, silinen: {silinen}")

# Belirli indeks
silinen = renkler.pop(1)
print(f"pop(1): {renkler}, silinen: {silinen}")

# Negatif indeks
silinen = renkler.pop(-1)
print(f"pop(-1): {renkler}, silinen: {silinen}")

# Stack (yığın) davranışı
stack = []
print(f"\nStack örneği:")
stack.append("birinci")
stack.append("ikinci")
stack.append("üçüncü")
print(f"Stack: {stack}")

while stack:
    eleman = stack.pop()
    print(f"Çıkarılan: {eleman}, Kalan: {stack}")

print("\n6. INDEX() - ELEMAN ARAMA:")
print("-" * 24)

# index() temel kullanım
harfler = ["a", "b", "c", "d", "e", "c", "f"]
print(f"Liste: {harfler}")

try:
    indeks = harfler.index("c")
    print(f"'c' harfinin ilk indeksi: {indeks}")
    
    # Belirli aralıkta arama
    indeks2 = harfler.index("c", 3)  # 3. indeksten sonra ara
    print(f"3. indeksten sonra 'c': {indeks2}")
    
    # Aralık belirtme
    indeks3 = harfler.index("c", 3, 6)  # 3-6 arası ara
    print(f"3-6 arası 'c': {indeks3}")
    
except ValueError as e:
    print(f"Bulunamadı: {e}")

# Güvenli index
def guvenli_index(liste, eleman):
    try:
        return liste.index(eleman)
    except ValueError:
        return -1

print(f"\nGüvenli arama 'd': {guvenli_index(harfler, 'd')}")
print(f"Güvenli arama 'z': {guvenli_index(harfler, 'z')}")

print("\n7. COUNT() - ELEMAN SAYMA:")
print("-" * 24)

# count() temel kullanım
sayilar = [1, 2, 3, 2, 4, 2, 5, 2, 6]
print(f"Liste: {sayilar}")

print(f"2 sayısı kaç kez var: {sayilar.count(2)}")
print(f"7 sayısı kaç kez var: {sayilar.count(7)}")

# String listede count
kelimeler = ["python", "java", "python", "c++", "python"]
print(f"\nKelimeler: {kelimeler}")
print(f"'python' kaç kez var: {kelimeler.count('python')}")

# İstatistik hesaplama
def liste_istatistik(liste):
    print(f"Liste: {liste}")
    print(f"Uzunluk: {len(liste)}")
    
    # Tekil elemanlar
    tekil = list(set(liste))
    print(f"Tekil elemanlar: {tekil}")
    
    # Her elemanın sayısı
    for eleman in tekil:
        sayi = liste.count(eleman)
        print(f"  {eleman}: {sayi} kez")

liste_istatistik([1, 2, 2, 3, 3, 3, 4])

print("\n8. SORT() - SIRALAMA:")
print("-" * 19)

# sort() temel kullanım
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

# Büyük/küçük harf duyarsız sıralama
isimler2 = ["zeynep", "ALİ", "Mehmet", "AYŞE"]
print(f"\nKarışık: {isimler2}")
isimler2.sort(key=str.lower)
print(f"key=str.lower: {isimler2}")

# Uzunluğa göre sıralama
kelimeler = ["elma", "armut", "muz", "kiraz", "çilek"]
print(f"\nKelimeler: {kelimeler}")
kelimeler.sort(key=len)
print(f"Uzunluğa göre: {kelimeler}")

# Özel sıralama fonksiyonu
def ikinci_harf(kelime):
    return kelime[1] if len(kelime) > 1 else ''

kelimeler.sort(key=ikinci_harf)
print(f"İkinci harfe göre: {kelimeler}")

print("\n9. REVERSE() - TERS ÇEVİRME:")
print("-" * 26)

# reverse() kullanımı
liste = [1, 2, 3, 4, 5]
print(f"Orijinal: {liste}")

liste.reverse()
print(f"reverse(): {liste}")

# Slicing ile ters çevirme (yeni liste)
liste2 = [1, 2, 3, 4, 5]
ters_liste = liste2[::-1]
print(f"Slicing [::-1]: {ters_liste}")
print(f"Orijinal değişmedi: {liste2}")

print("\n10. COPY() - LİSTE KOPYALAMA:")
print("-" * 27)

# copy() kullanımı
orijinal = [1, 2, 3, [4, 5]]
kopya = orijinal.copy()

print(f"Orijinal: {orijinal}")
print(f"Kopya: {kopya}")

# Yüzeysel kopya testi
orijinal[0] = 99
print(f"Orijinal[0] = 99: {orijinal}")
print(f"Kopya etkilenmedi: {kopya}")

# İç liste değişikliği (shallow copy problemi)
orijinal[3].append(6)
print(f"Orijinal[3].append(6): {orijinal}")
print(f"Kopya da etkilendi: {kopya}")

# Derin kopya için
import copy
derin_kopya = copy.deepcopy(orijinal)
orijinal[3].append(7)
print(f"Orijinal[3].append(7): {orijinal}")
print(f"Derin kopya etkilenmedi: {derin_kopya}")

print("\n11. CLEAR() - LİSTEYİ BOŞALTMA:")
print("-" * 28)

# clear() kullanımı
liste = [1, 2, 3, 4, 5]
print(f"Başlangıç: {liste}")

liste.clear()
print(f"clear() sonrası: {liste}")

# Alternatif yöntemler
liste2 = [1, 2, 3, 4, 5]
liste3 = [1, 2, 3, 4, 5]

# del ile
del liste2[:]
print(f"del [:]: {liste2}")

# Slice atama ile
liste3[:] = []
print(f"[:] = []: {liste3}")

print("\n12. METOT ZİNCİRLEME:")
print("-" * 21)

# Bazı metotlar None döndürür (yerinde değişiklik)
liste = [3, 1, 4, 1, 5]
print(f"Başlangıç: {liste}")

# Bu ÇALIŞMAZ (sort None döndürür)
# sonuc = liste.sort().reverse()  # AttributeError!

# Doğru kullanım
liste.sort()
liste.reverse()
print(f"sort() + reverse(): {liste}")

# Fluent interface istiyorsak özel sınıf yazmalıyız
class FluentList(list):
    def fluent_sort(self, **kwargs):
        self.sort(**kwargs)
        return self
    
    def fluent_reverse(self):
        self.reverse()
        return self

fluent_liste = FluentList([3, 1, 4, 1, 5])
sonuc = fluent_liste.fluent_sort().fluent_reverse()
print(f"Fluent: {sonuc}")

print("\n13. METOT PERFORMANS KARŞILAŞTIRMA:")
print("-" * 35)

import time

# Büyük liste ile testler
print("10.000 elemanlı liste testleri:")

# append vs insert performansı
test_liste = list(range(10000))
eleman = 99999

# remove() performansı
start = time.time()
if eleman in test_liste:
    test_liste.remove(eleman)
remove_time = time.time() - start

# pop() performansı
test_liste.append(eleman)
start = time.time()
test_liste.pop()
pop_time = time.time() - start

# index() performansı
test_liste.insert(5000, eleman)
start = time.time()
indeks = test_liste.index(eleman)
index_time = time.time() - start

print(f"remove(): {remove_time*1000:.4f} ms")
print(f"pop(): {pop_time*1000:.4f} ms")
print(f"index(): {index_time*1000:.4f} ms")

print("\n14. PRATIK KULLANIM ÖRNEKLERİ:")
print("-" * 29)

# Playlist yönetimi
class Playlist:
    def __init__(self):
        self.sarkilar = []
    
    def sarki_ekle(self, sarki):
        self.sarkilar.append(sarki)
        print(f"'{sarki}' eklendi")
    
    def sarki_cikar(self, sarki):
        if sarki in self.sarkilar:
            self.sarkilar.remove(sarki)
            print(f"'{sarki}' çıkarıldı")
        else:
            print(f"'{sarki}' bulunamadı")
    
    def karistir(self):
        import random
        random.shuffle(self.sarkilar)
        print("Playlist karıştırıldı")
    
    def listele(self):
        print("Playlist:")
        for i, sarki in enumerate(self.sarkilar, 1):
            print(f"  {i}. {sarki}")

# Playlist kullanımı
playlist = Playlist()
playlist.sarki_ekle("Bohemian Rhapsody")
playlist.sarki_ekle("Hotel California")
playlist.sarki_ekle("Stairway to Heaven")
playlist.listele()

playlist.sarki_cikar("Hotel California")
playlist.listele()

print("\n=== LİSTE METOTLARI ÖZETİ ===")
print("Ekleme metotları:")
print("  • append(x) - sona ekle")
print("  • insert(i, x) - i pozisyonuna ekle")
print("  • extend(iterable) - iterable'ın elemanlarını ekle")
print()
print("Silme metotları:")
print("  • remove(x) - ilk x'i sil")
print("  • pop(i) - i pozisyonunu sil ve döndür")
print("  • clear() - tüm elemanları sil")
print()
print("Arama metotları:")
print("  • index(x) - x'in pozisyonunu bul")
print("  • count(x) - x'in sayısını bul")
print("  • x in liste - x listede var mı")
print()
print("Düzenleme metotları:")
print("  • sort() - sırala")
print("  • reverse() - ters çevir")
print("  • copy() - kopyala")
print()
print("Performans notları:")
print("  • append() hızlı, insert(0) yavaş")
print("  • pop() hızlı, remove() yavaş")
print("  • in operatörü baştan arar")
print("  • sort() çok verimli (Timsort)")