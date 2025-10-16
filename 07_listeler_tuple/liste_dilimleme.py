# Liste Dilimleme (Slicing) ve İleri Seviye Kullanım
# Python liste dilimleme işlemlerinin detaylı incelenmesi

print("=== LİSTE DİLİMLEME (SLICING) ===\n")

print("1. TEMEL DİLİMLEME SÖZDİZİMİ:")
print("-" * 29)

# liste[başlangıç:bitiş:adım]
sayilar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Ana liste: {sayilar}")

# Temel kullanım
print(f"[2:6]: {sayilar[2:6]}")        # İndeks 2'den 6'ya kadar (6 dahil değil)
print(f"[0:5]: {sayilar[0:5]}")        # Baştan 5 eleman
print(f"[5:]: {sayilar[5:]}")          # 5. indeksten sona kadar
print(f"[:5]: {sayilar[:5]}")          # Baştan 5. indekse kadar
print(f"[:]: {sayilar[:]}")            # Tüm liste (kopya)

# Negatif indeksler
print(f"[-3:]: {sayilar[-3:]}")        # Son 3 eleman
print(f"[:-3]: {sayilar[:-3]}")        # Son 3 hariç hepsi
print(f"[-5:-2]: {sayilar[-5:-2]}")    # Sondan 5. ile 2. arası

print("\n2. ADIM (STEP) KULLANIMI:")
print("-" * 25)

harfler = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(f"Harfler: {harfler}")

# Pozitif adımlar
print(f"[::2]: {harfler[::2]}")        # Her 2 eleman
print(f"[1::2]: {harfler[1::2]}")      # 1'den başlayarak her 2 eleman
print(f"[::3]: {harfler[::3]}")        # Her 3 eleman
print(f"[2:8:2]: {harfler[2:8:2]}")    # 2'den 8'e kadar her 2 eleman

# Negatif adım (ters yön)
print(f"[::-1]: {harfler[::-1]}")      # Tüm listeyi ters çevir
print(f"[::-2]: {harfler[::-2]}")      # Tersten her 2 eleman
print(f"[8:2:-1]: {harfler[8:2:-1]}")  # 8'den 2'ye geriye doğru

# İleri seviye ters dilimleme
print(f"[5::-1]: {harfler[5::-1]}")    # 5'ten başa doğru
print(f"[:3:-1]: {harfler[:3:-1]}")    # Sondan 3'e kadar geriye

print("\n3. DİLİMLEME İLE LİSTE DEĞİŞTİRME:")
print("-" * 32)

# Slice assignment
sayilar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Orijinal: {sayilar}")

# Bölge değiştirme
sayilar[2:5] = [20, 30, 40]
print(f"[2:5] değişti: {sayilar}")

# Farklı uzunlukta değiştirme
sayilar[2:5] = [200, 300]  # 3 eleman yerine 2 eleman
print(f"Kısaltma: {sayilar}")

sayilar[2:4] = [200, 250, 300, 350]  # 2 eleman yerine 4 eleman
print(f"Uzatma: {sayilar}")

# Eleman ekleme
sayilar[3:3] = [225, 275]  # Boş slice'a ekleme
print(f"Araya ekleme: {sayilar}")

# Eleman silme
sayilar[3:6] = []  # Boş liste ile değiştirme = silme
print(f"Silme: {sayilar}")

# Adımlı değiştirme
liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"\nAdımlı değiştirme: {liste}")
liste[::2] = [10, 12, 14, 16, 18]  # Çift indeksleri değiştir
print(f"Çift indeksler: {liste}")

print("\n4. DİLİMLEME İLE LİSTE KOPYALAMA:")
print("-" * 31)

orijinal = [1, 2, 3, [4, 5], 6]
print(f"Orijinal: {orijinal}")

# Shallow copy (yüzeysel kopya)
kopya1 = orijinal[:]
kopya2 = orijinal.copy()
kopya3 = list(orijinal)

print(f"Slice kopya: {kopya1}")
print(f"copy() kopya: {kopya2}")
print(f"list() kopya: {kopya3}")

# Shallow copy testi
orijinal[0] = 99
print(f"Orijinal[0] = 99: {orijinal}")
print(f"Slice kopya etkilenmedi: {kopya1}")

# İç liste değişikliği (shallow copy problemi)
orijinal[3].append(7)
print(f"İç liste değişti: {orijinal}")
print(f"Slice kopya da etkilendi: {kopya1}")

# Deep copy için
import copy
derin_kopya = copy.deepcopy(orijinal)
orijinal[3].append(8)
print(f"Derin kopya etkilenmedi: {derin_kopya}")

print("\n5. GELİŞMİŞ DİLİMLEME ÖRNEKLERİ:")
print("-" * 32)

# Matrix (2D liste) dilimleme
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print("Matrix:")
for satir in matrix:
    print(f"  {satir}")

# Satır dilimleme
print(f"İlk 2 satır: {matrix[:2]}")
print(f"Son satır: {matrix[-1]}")

# Sütun alma (list comprehension gerekli)
sutun_2 = [satir[2] for satir in matrix]
print(f"3. sütun: {sutun_2}")

# Alt matrix alma
alt_matrix = [satir[1:3] for satir in matrix[1:]]
print(f"Alt matrix: {alt_matrix}")

print("\n6. DİLİMLEME İLE ALGORITMA ÖRNEKLERİ:")
print("-" * 35)

# Palindrome kontrolü
def palindrome_mu(liste):
    return liste == liste[::-1]

test_listeleri = [
    [1, 2, 3, 2, 1],
    [1, 2, 3, 4, 5],
    ['a', 'b', 'c', 'b', 'a'],
    ['x', 'y', 'z']
]

print("Palindrome testi:")
for test in test_listeleri:
    sonuc = palindrome_mu(test)
    print(f"  {test}: {sonuc}")

# Liste döndürme
def liste_dondur(liste, n):
    """Listeyi n pozisyon sola döndürür"""
    n = n % len(liste)  # Overflow kontrolü
    return liste[n:] + liste[:n]

sayilar = [1, 2, 3, 4, 5, 6, 7, 8]
print(f"\nListe döndürme: {sayilar}")
print(f"2 sola: {liste_dondur(sayilar, 2)}")
print(f"3 sola: {liste_dondur(sayilar, 3)}")
print(f"10 sola: {liste_dondur(sayilar, 10)}")  # Overflow test

# Sliding window
def sliding_window(liste, pencere_boyutu):
    """Liste üzerinde kayar pencere"""
    sonuc = []
    for i in range(len(liste) - pencere_boyutu + 1):
        pencere = liste[i:i + pencere_boyutu]
        sonuc.append(pencere)
    return sonuc

veri = [1, 2, 3, 4, 5, 6, 7, 8]
print(f"\nSliding window: {veri}")
print(f"Pencere 3: {sliding_window(veri, 3)}")
print(f"Pencere 4: {sliding_window(veri, 4)}")

print("\n7. DİLİMLEME PERFORMANS ANALİZİ:")
print("-" * 31)

import time

# Büyük liste oluştur
büyük_liste = list(range(1000000))

# Slicing performansı
start = time.time()
kopya = büyük_liste[:]
slice_time = time.time() - start

# copy() performansı
start = time.time()
kopya = büyük_liste.copy()
copy_time = time.time() - start

# list() performansı
start = time.time()
kopya = list(büyük_liste)
list_time = time.time() - start

print(f"1 milyon elemanlı liste kopyalama:")
print(f"Slicing [:]: {slice_time*1000:.2f} ms")
print(f"copy(): {copy_time*1000:.2f} ms")
print(f"list(): {list_time*1000:.2f} ms")

# Dilimleme vs döngü
def manual_slice(liste, start, end):
    sonuc = []
    for i in range(start, end):
        sonuc.append(liste[i])
    return sonuc

# Performance comparison
start_time = time.time()
slice_result = büyük_liste[10000:20000]
slice_perf = time.time() - start_time

start_time = time.time()
manual_result = manual_slice(büyük_liste, 10000, 20000)
manual_perf = time.time() - start_time

print(f"\n10.000 eleman dilimleme:")
print(f"Built-in slice: {slice_perf*1000:.2f} ms")
print(f"Manual loop: {manual_perf*1000:.2f} ms")
print(f"Built-in {manual_perf/slice_perf:.1f}x daha hızlı")

print("\n8. DİLİMLEME HATALARI VE ÇÖZÜMLER:")
print("-" * 33)

# Yaygın hatalar
liste = [1, 2, 3, 4, 5]
print(f"Test listesi: {liste}")

# 1. Index out of range (slicing'de olmaz)
print(f"[100:200]: {liste[100:200]}")  # Boş liste döner
print(f"[-100:100]: {liste[-100:100]}")  # Tüm liste

# 2. Step = 0 hatası
try:
    result = liste[::0]
except ValueError as e:
    print(f"Step=0 hatası: {e}")

# 3. Ters dilimleme karışıklığı
print(f"[::-1]: {liste[::-1]}")        # Doğru: ters liste
print(f"[5:0:-1]: {liste[5:0:-1]}")    # Doğru: 5'ten 1'e
print(f"[0:5:-1]: {liste[0:5:-1]}")    # Yanlış: boş liste

# 4. Slice assignment boyut uyumsuzluğu
liste_test = [1, 2, 3, 4, 5]
print(f"Değişim öncesi: {liste_test}")

# Bu çalışır (farklı boyutlar)
liste_test[1:3] = [20, 30, 40, 50]
print(f"Değişen boyut: {liste_test}")

# Bu step'li dilimlerde çalışmaz
liste_test2 = [1, 2, 3, 4, 5, 6]
try:
    liste_test2[::2] = [10, 20]  # 3 eleman yerine 2 eleman
except ValueError as e:
    print(f"Step'li assignment hatası: {e}")

print("\n9. DİLİMLEME İLE VERİ YAPILARI:")
print("-" * 30)

# Stack (LIFO) simülasyonu
class SliceStack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.items:
            item = self.items[-1]
            self.items = self.items[:-1]  # Slice ile son elemanı çıkar
            return item
    
    def peek(self):
        return self.items[-1] if self.items else None
    
    def __str__(self):
        return str(self.items)

stack = SliceStack()
stack.push(1)
stack.push(2)
stack.push(3)
print(f"Stack: {stack}")
print(f"Pop: {stack.pop()}, Stack: {stack}")

# Queue (FIFO) simülasyonu
class SliceQueue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.items:
            item = self.items[0]
            self.items = self.items[1:]  # Slice ile ilk elemanı çıkar
            return item
    
    def __str__(self):
        return str(self.items)

queue = SliceQueue()
queue.enqueue("birinci")
queue.enqueue("ikinci")
queue.enqueue("üçüncü")
print(f"Queue: {queue}")
print(f"Dequeue: {queue.dequeue()}, Queue: {queue}")

# Circular buffer
class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = []
    
    def add(self, item):
        self.buffer.append(item)
        if len(self.buffer) > self.size:
            self.buffer = self.buffer[-self.size:]  # Son n elemanı tut
    
    def get_all(self):
        return self.buffer[:]  # Kopya döndür
    
    def __str__(self):
        return str(self.buffer)

circular = CircularBuffer(3)
for i in range(6):
    circular.add(f"item_{i}")
    print(f"Add item_{i}: {circular}")

print("\n10. PRAKTİK DİLİMLEME TEKNİKLERİ:")
print("-" * 33)

# 1. Liste temizleme
veri = [1, 0, 3, 0, 5, 0, 7]
print(f"Orijinal: {veri}")

# Sıfırları temizle
temiz = [x for x in veri if x != 0]
print(f"Sıfırsız: {temiz}")

# 2. Batch processing
def batch_process(liste, batch_size):
    """Listeyi batch'lere böl"""
    batches = []
    for i in range(0, len(liste), batch_size):
        batch = liste[i:i + batch_size]
        batches.append(batch)
    return batches

büyük_veri = list(range(20))
batches = batch_process(büyük_veri, 5)
print(f"\nBatch processing:")
for i, batch in enumerate(batches):
    print(f"  Batch {i}: {batch}")

# 3. Overlap detection
def overlap_detect(liste1, liste2):
    """İki listenin kesişimini bul"""
    return list(set(liste1) & set(liste2))

l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5, 6, 7]
overlap = overlap_detect(l1, l2)
print(f"\nOverlap: {l1} ∩ {l2} = {overlap}")

# 4. Pattern matching
def pattern_match(ana_liste, pattern):
    """Ana liste içinde pattern ara"""
    matches = []
    pattern_len = len(pattern)
    for i in range(len(ana_liste) - pattern_len + 1):
        if ana_liste[i:i + pattern_len] == pattern:
            matches.append(i)
    return matches

ana = [1, 2, 3, 2, 3, 4, 2, 3, 5]
pattern = [2, 3]
matches = pattern_match(ana, pattern)
print(f"\nPattern matching:")
print(f"Ana liste: {ana}")
print(f"Pattern: {pattern}")
print(f"Bulunan pozisyonlar: {matches}")

print("\n=== DİLİMLEME ÖZETİ ===")
print("Sözdizimi: liste[başlangıç:bitiş:adım]")
print()
print("Temel kurallar:")
print("  • başlangıç dahil, bitiş dahil değil")
print("  • Negatif indeksler kullanılabilir")
print("  • Eksik değerler varsayılan alır")
print("  • Index out of range hatası vermez")
print()
print("Yaygın kullanımlar:")
print("  • [:] - Tüm liste (kopya)")
print("  • [n:] - n'den sona kadar")
print("  • [:n] - Baştan n'e kadar") 
print("  • [::-1] - Ters çevir")
print("  • [::2] - Her 2 eleman")
print("  • [-n:] - Son n eleman")
print()
print("Performans notları:")
print("  • Slicing çok hızlı (C seviyesi)")
print("  • Kopya oluşturur (bellek kullanır)")
print("  • Step'li assignment dikkat gerektirir")
print("  • Büyük listlerde bellek optimizasyonu önemli")
print()
print("Kullanım alanları:")
print("  • Liste kopyalama")
print("  • Alt liste alma")
print("  • Pattern matching")
print("  • Batch processing")
print("  • Data structure simülasyonu")