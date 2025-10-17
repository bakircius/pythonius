"""
Python Generator Kullanımı - İleri Düzey Örnekler

Bu dosyada generator fonksiyonları, yield kullanımı ve pratik uygulamaları bulacaksınız.
"""

import itertools
import sys

# =============================================================================
# 1. TEMELs GENERATOR FONKSİYONLARI
# =============================================================================

def basit_generator():
    """En basit generator örneği"""
    print("Generator başladı")
    yield 1
    print("İlk yield sonrası")
    yield 2
    print("İkinci yield sonrası")
    yield 3
    print("Generator bitti")

def sayici_generator(start=0, stop=10):
    """Belirli aralıkta sayı üreten generator"""
    current = start
    while current < stop:
        yield current
        current += 1

# Generator kullanımı
print("=== Basit Generator ===")
gen = basit_generator()
for value in gen:
    print(f"Değer: {value}")

print("\n=== Sayıcı Generator ===")
for num in sayici_generator(5, 10):
    print(num)

# =============================================================================
# 2. FİBONACCİ GENERATOR
# =============================================================================

def fibonacci_generator(n):
    """n tane Fibonacci sayısı üreten generator"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

def sonsuz_fibonacci():
    """Sonsuz Fibonacci generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print("\n=== Fibonacci Generator ===")
for fib in fibonacci_generator(10):
    print(fib, end=' ')
print()

# Sonsuz generator'dan ilk 15 değeri al
print("\nSonsuz Fibonacci'den ilk 15 değer:")
fib_gen = sonsuz_fibonacci()
for i in range(15):
    print(next(fib_gen), end=' ')
print()

# =============================================================================
# 3. DOSYA OKUMA GENERATOR'I
# =============================================================================

def dosya_satirlari_generator(dosya_adi):
    """Büyük dosyaları satır satır okuyan generator"""
    try:
        with open(dosya_adi, 'r', encoding='utf-8') as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        print(f"Dosya bulunamadı: {dosya_adi}")

def filtrelenmis_satirlar(dosya_adi, filtre_kelime):
    """Belirli kelimeyi içeren satırları filtreleyen generator"""
    for satir in dosya_satirlari_generator(dosya_adi):
        if filtre_kelime.lower() in satir.lower():
            yield satir

# Örnek dosya oluştur ve test et
ornek_dosya = "ornek_metin.txt"
with open(ornek_dosya, 'w', encoding='utf-8') as f:
    f.write("""Python programlama dili
Generator fonksiyonları çok kullanışlıdır
Bellekte verimli çözümler sunar
Python ile veri işleme kolaydır
Yield anahtar kelimesi önemlidir""")

print(f"\n=== Dosya Okuma Generator ===")
print("Tüm satırlar:")
for satir in dosya_satirlari_generator(ornek_dosya):
    print(f"- {satir}")

print("\n'Python' kelimesini içeren satırlar:")
for satir in filtrelenmis_satirlar(ornek_dosya, "python"):
    print(f"- {satir}")

# =============================================================================
# 4. GENERATOR EXPRESSIONS
# =============================================================================

# Liste comprehension vs Generator expression
print("\n=== Generator Expressions ===")

# Liste comprehension - tüm değerler bellekte
liste = [x**2 for x in range(10)]
print(f"Liste boyutu: {sys.getsizeof(liste)} bytes")
print(f"Liste: {liste}")

# Generator expression - lazy evaluation
gen_exp = (x**2 for x in range(10))
print(f"Generator boyutu: {sys.getsizeof(gen_exp)} bytes")
print(f"Generator değerleri: {list(gen_exp)}")

# Büyük veri seti örneği
print("\nBüyük veri seti karşılaştırması:")
n = 1000000

# Liste - çok bellek kullanır
# liste_buyuk = [x for x in range(n)]  # Yorumda bırakıldı - çok bellek kullanır
# print(f"Büyük liste boyutu: {sys.getsizeof(liste_buyuk)} bytes")

# Generator - az bellek kullanır
gen_buyuk = (x for x in range(n))
print(f"Büyük generator boyutu: {sys.getsizeof(gen_buyuk)} bytes")

# =============================================================================
# 5. GENERATOR PİPELİNE
# =============================================================================

def sayilar_generator(start, end):
    """Sayı dizisi üreten generator"""
    for i in range(start, end + 1):
        yield i

def cift_sayilar_filter(numbers):
    """Çift sayıları filtreleyen generator"""
    for num in numbers:
        if num % 2 == 0:
            yield num

def kare_al(numbers):
    """Sayıların karesini alan generator"""
    for num in numbers:
        yield num ** 2

def toplam_hesapla(numbers):
    """Generator'dan gelen sayıları toplayan fonksiyon"""
    return sum(numbers)

print("\n=== Generator Pipeline ===")
# Pipeline oluştur
sayilar = sayilar_generator(1, 20)
cift_sayilar = cift_sayilar_filter(sayilar)
kareli_sayilar = kare_al(cift_sayilar)
sonuc = toplam_hesapla(kareli_sayilar)

print(f"1-20 arasındaki çift sayıların karelerinin toplamı: {sonuc}")

# Tek satırda pipeline
tek_satirda = toplam_hesapla(
    kare_al(
        cift_sayilar_filter(
            sayilar_generator(1, 20)
        )
    )
)
print(f"Tek satırda sonuç: {tek_satirda}")

# =============================================================================
# 6. RECURSIVE GENERATOR
# =============================================================================

def tree_traverse(node):
    """Ağaç yapısını dolaşan recursive generator"""
    yield node['value']
    for child in node.get('children', []):
        yield from tree_traverse(child)

# Örnek ağaç yapısı
agac = {
    'value': 'A',
    'children': [
        {
            'value': 'B',
            'children': [
                {'value': 'D'},
                {'value': 'E'}
            ]
        },
        {
            'value': 'C',
            'children': [
                {'value': 'F'},
                {'value': 'G'}
            ]
        }
    ]
}

print("\n=== Recursive Generator - Ağaç Dolaşma ===")
print("Ağaç elemanları:")
for node in tree_traverse(agac):
    print(node, end=' ')
print()

# =============================================================================
# 7. GENERATOR İLE VERİ İŞLEME
# =============================================================================

def csv_reader_generator(dosya_adi):
    """CSV dosyasını satır satır okuyan generator"""
    try:
        with open(dosya_adi, 'r', encoding='utf-8') as file:
            header = next(file).strip().split(',')
            for line in file:
                values = line.strip().split(',')
                yield dict(zip(header, values))
    except FileNotFoundError:
        print(f"CSV dosyası bulunamadı: {dosya_adi}")

def veri_filtreleme(data_generator, koşul_func):
    """Veriyi koşula göre filtreleyen generator"""
    for item in data_generator:
        if koşul_func(item):
            yield item

def veri_donusturme(data_generator, donustur_func):
    """Veriyi dönüştüren generator"""
    for item in data_generator:
        yield donustur_func(item)

# Örnek CSV dosyası oluştur
csv_dosya = "ornek_veri.csv"
with open(csv_dosya, 'w', encoding='utf-8') as f:
    f.write("""isim,yas,maas
Ali,25,5000
Ayşe,30,7000
Mehmet,22,4500
Fatma,35,8500
Ahmet,28,6000""")

print("\n=== CSV Veri İşleme Generator ===")

# Veri okuma ve işleme pipeline
veri = csv_reader_generator(csv_dosya)
yetiskin_calisanlar = veri_filtreleme(veri, lambda x: int(x['yas']) >= 25)
maas_artirimi = veri_donusturme(
    yetiskin_calisanlar, 
    lambda x: {**x, 'yeni_maas': int(x['maas']) * 1.1}
)

print("25 yaş üstü çalışanların maaş artırımı sonrası:")
for calisan in maas_artirimi:
    print(f"{calisan['isim']}: {calisan['maas']} -> {calisan['yeni_maas']:.0f}")

# =============================================================================
# 8. GENERATOR İLE MEMORY BENCHMARK
# =============================================================================

import time
import psutil
import os

def memory_benchmark():
    """Generator vs Liste bellek kullanımı karşılaştırması"""
    print("\n=== Memory Benchmark ===")
    
    n = 100000
    process = psutil.Process(os.getpid())
    
    # Liste ile
    print("Liste ile:")
    initial_memory = process.memory_info().rss / 1024 / 1024  # MB
    start_time = time.time()
    
    large_list = [x**2 for x in range(n)]
    sum_list = sum(large_list)
    
    end_time = time.time()
    final_memory = process.memory_info().rss / 1024 / 1024  # MB
    
    print(f"Süre: {end_time - start_time:.4f} saniye")
    print(f"Bellek kullanımı: {final_memory - initial_memory:.2f} MB")
    print(f"Sonuç: {sum_list}")
    
    # Generator ile
    print("\nGenerator ile:")
    initial_memory = process.memory_info().rss / 1024 / 1024  # MB
    start_time = time.time()
    
    large_gen = (x**2 for x in range(n))
    sum_gen = sum(large_gen)
    
    end_time = time.time()
    final_memory = process.memory_info().rss / 1024 / 1024  # MB
    
    print(f"Süre: {end_time - start_time:.4f} saniye")
    print(f"Bellek kullanımı: {final_memory - initial_memory:.2f} MB")
    print(f"Sonuç: {sum_gen}")

# Benchmark çalıştır (psutil kurulu ise)
try:
    memory_benchmark()
except ImportError:
    print("\n=== Memory Benchmark ===")
    print("psutil modülü kurulu değil. 'pip install psutil' ile kurabilirsiniz.")

# =============================================================================
# 9. GENERATOR SEND() VE CLOSE() METODLARİ
# =============================================================================

def interactive_generator():
    """Send() metoduyla etkileşimli generator"""
    print("Generator başladı")
    value = yield "İlk değer"
    
    while True:
        if value is None:
            print("None değeri alındı")
            value = yield "Varsayılan değer"
        else:
            print(f"Gönderilen değer: {value}")
            value = yield f"İşlenen: {value * 2}"

print("\n=== Interactive Generator ===")
gen = interactive_generator()

# Generator'ı başlat
result = next(gen)
print(f"İlk sonuç: {result}")

# Değer gönder
result = gen.send(10)
print(f"10 gönderme sonucu: {result}")

result = gen.send("Merhaba")
print(f"'Merhaba' gönderme sonucu: {result}")

# Generator'ı kapat
gen.close()
print("Generator kapatıldı")

# =============================================================================
# 10. GENERATOR COMPOSITION
# =============================================================================

def range_generator(start, stop, step=1):
    """Custom range generator"""
    current = start
    while current < stop:
        yield current
        current += step

def chain_generators(*generators):
    """Birden fazla generator'ı birleştiren generator"""
    for gen in generators:
        yield from gen

def cycle_generator(iterable, times=None):
    """Iterable'ı döngüsel olarak tekrarlayan generator"""
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    
    if times is None:
        while saved:
            for element in saved:
                yield element
    else:
        for _ in range(times - 1):
            for element in saved:
                yield element

print("\n=== Generator Composition ===")

# Generator'ları birleştir
gen1 = range_generator(1, 5)
gen2 = range_generator(10, 15)
gen3 = range_generator(20, 25)

birlesik = chain_generators(gen1, gen2, gen3)
print("Birleştirilmiş generator'lar:")
print(list(birlesik))

# Döngüsel generator
print("\nDöngüsel generator (3 kez):")
cycle_gen = cycle_generator(['A', 'B', 'C'], times=3)
for i, value in enumerate(cycle_gen):
    print(value, end=' ')
    if i >= 8:  # İlk 9 değeri göster
        break
print()

# =============================================================================
# 11. PRATIK UYGULAMALAR
# =============================================================================

def batch_processor(iterable, batch_size):
    """Veriyi batch'lere bölen generator"""
    iterator = iter(iterable)
    while True:
        batch = list(itertools.islice(iterator, batch_size))
        if not batch:
            break
        yield batch

def unique_generator(iterable):
    """Benzersiz elemanları döndüren generator"""
    seen = set()
    for item in iterable:
        if item not in seen:
            seen.add(item)
            yield item

def window_generator(iterable, window_size):
    """Sliding window generator"""
    iterator = iter(iterable)
    window = list(itertools.islice(iterator, window_size))
    
    if len(window) == window_size:
        yield tuple(window)
    
    for item in iterator:
        window = window[1:] + [item]
        yield tuple(window)

print("\n=== Pratik Uygulamalar ===")

# Batch processing
data = range(1, 16)
print("Batch processing (3'erli gruplar):")
for batch in batch_processor(data, 3):
    print(batch)

# Unique generator
duplicate_data = [1, 2, 2, 3, 1, 4, 5, 3, 6]
print(f"\nOrijinal veri: {duplicate_data}")
print(f"Benzersiz elemanlar: {list(unique_generator(duplicate_data))}")

# Sliding window
sequence = [1, 2, 3, 4, 5, 6, 7]
print(f"\nSequence: {sequence}")
print("3'lü sliding window:")
for window in window_generator(sequence, 3):
    print(window)

print("\n" + "="*50)
print("GENERATOR KULLANIMI TAMAMLANDI")
print("="*50)

# Temizlik
import os
try:
    os.remove(ornek_dosya)
    os.remove(csv_dosya)
    print("Örnek dosyalar temizlendi.")
except:
    pass