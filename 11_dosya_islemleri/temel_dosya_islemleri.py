"""
Python Temel Dosya İşlemleri

Bu dosya Python'da dosya açma, okuma, yazma ve kapama işlemlerini
kapsamlı olarak ele alır. Dosya modları, hata yönetimi ve güvenli
dosya işlemleri konularını öğreneceğiz.
"""

import os
import sys
from pathlib import Path

# =============================================================================
# 1. DOSYA AÇMA VE KAPAMA TEMELLERİ
# =============================================================================

print("=== Dosya İşlemleri Temelleri ===")

# Dosya açma - Temel sözdizimi
# file = open(dosya_yolu, mod, encoding=None)

# Test dosyası oluşturalım
test_dosya_yolu = "test_dosya.txt"

# Dosya yazma (write mode)
dosya = open(test_dosya_yolu, 'w', encoding='utf-8')
dosya.write("Merhaba Python!\n")
dosya.write("Bu bir test dosyasıdır.\n")
dosya.write("Türkçe karakterler: ğüşıöçĞÜŞİÖÇ\n")
dosya.close()  # Dosyayı kapatmak önemli!

print("✅ Test dosyası oluşturuldu")

# Dosya okuma (read mode)
dosya = open(test_dosya_yolu, 'r', encoding='utf-8')
icerik = dosya.read()
dosya.close()

print("📖 Dosya içeriği:")
print(icerik)

# =============================================================================
# 2. DOSYA MODLARI (FILE MODES)
# =============================================================================

print("\n=== Dosya Modları ===")

# Yazma modları
modlar = {
    'r': 'Okuma (read) - varsayılan',
    'w': 'Yazma (write) - dosyayı sıfırlar',
    'a': 'Ekleme (append) - dosya sonuna ekler',
    'x': 'Özel oluşturma - sadece yeni dosya',
    'r+': 'Okuma ve yazma',
    'w+': 'Yazma ve okuma - dosyayı sıfırlar',
    'a+': 'Ekleme ve okuma',
    'rb': 'Binary okuma',
    'wb': 'Binary yazma',
    'ab': 'Binary ekleme'
}

for mod, aciklama in modlar.items():
    print(f"'{mod}': {aciklama}")

# Append mode örneği
print("\n--- Append Mode Örneği ---")
with open(test_dosya_yolu, 'a', encoding='utf-8') as dosya:
    dosya.write("Bu satır eklenmiştir.\n")
    dosya.write(f"Zaman: {sys.version}\n")

# Dosyayı tekrar okuyalım
with open(test_dosya_yolu, 'r', encoding='utf-8') as dosya:
    print("Güncellenmiş dosya içeriği:")
    print(dosya.read())

# =============================================================================
# 3. DOSYA OKUMA METOTLARİ
# =============================================================================

print("\n=== Dosya Okuma Metotları ===")

# read() - Tüm dosyayı okur
with open(test_dosya_yolu, 'r', encoding='utf-8') as dosya:
    tum_icerik = dosya.read()
    print(f"read() ile: {len(tum_icerik)} karakter okundu")

# readline() - Tek satır okur
with open(test_dosya_yolu, 'r', encoding='utf-8') as dosya:
    ilk_satir = dosya.readline()
    ikinci_satir = dosya.readline()
    print(f"İlk satır: {ilk_satir.strip()}")
    print(f"İkinci satır: {ikinci_satir.strip()}")

# readlines() - Tüm satırları liste olarak okur
with open(test_dosya_yolu, 'r', encoding='utf-8') as dosya:
    satirlar = dosya.readlines()
    print(f"readlines() ile: {len(satirlar)} satır okundu")
    for i, satir in enumerate(satirlar, 1):
        print(f"Satır {i}: {satir.strip()}")

# Dosyayı iterasyon ile okuma (en verimli)
print("\n--- Iterasyon ile Okuma ---")
with open(test_dosya_yolu, 'r', encoding='utf-8') as dosya:
    for satir_no, satir in enumerate(dosya, 1):
        print(f"{satir_no}: {satir.strip()}")

# =============================================================================
# 4. BÜYÜK DOSYALAR İLE ÇALIŞMA
# =============================================================================

print("\n=== Büyük Dosyalar ===")

# Büyük test dosyası oluşturalım
buyuk_dosya = "buyuk_test.txt"
with open(buyuk_dosya, 'w', encoding='utf-8') as dosya:
    for i in range(1000):
        dosya.write(f"Bu {i+1}. satırdır. Python ile dosya işlemleri öğreniyoruz.\n")

print("✅ 1000 satırlık büyük dosya oluşturuldu")

# Chunk halinde okuma
def dosya_chunk_oku(dosya_yolu, chunk_boyutu=1024):
    """Dosyayı belirli boyutlarda parçalar halinde okur"""
    with open(dosya_yolu, 'r', encoding='utf-8') as dosya:
        chunk_sayisi = 0
        while True:
            chunk = dosya.read(chunk_boyutu)
            if not chunk:
                break
            chunk_sayisi += 1
            yield chunk_sayisi, chunk

# İlk 3 chunk'ı gösterelim
print("\n--- Chunk Okuma Örneği ---")
for chunk_no, chunk in dosya_chunk_oku(buyuk_dosya, 100):
    if chunk_no <= 3:
        print(f"Chunk {chunk_no}: {len(chunk)} karakter")
        print(f"İçerik önizleme: {chunk[:50]}...")
    else:
        break

# Satır sayısı sayma (büyük dosyalar için verimli)
def satir_sayisi_say(dosya_yolu):
    """Büyük dosyalarda satır sayısını verimli şekilde sayar"""
    with open(dosya_yolu, 'r', encoding='utf-8') as dosya:
        return sum(1 for _ in dosya)

satir_sayisi = satir_sayisi_say(buyuk_dosya)
print(f"\nBüyük dosyadaki satır sayısı: {satir_sayisi}")

# =============================================================================
# 5. DOSYA YAZMA İŞLEMLERİ
# =============================================================================

print("\n=== Dosya Yazma İşlemleri ===")

# Farklı veri türlerini yazma
veri_dosyasi = "veri_ornekleri.txt"

with open(veri_dosyasi, 'w', encoding='utf-8') as dosya:
    # String yazma
    dosya.write("String veri\n")
    
    # Sayı yazma (string'e çevirmek gerekir)
    sayi = 42
    dosya.write(f"Sayı: {sayi}\n")
    
    # Liste yazma
    liste = [1, 2, 3, 4, 5]
    dosya.write(f"Liste: {', '.join(map(str, liste))}\n")
    
    # Sözlük yazma
    sozluk = {'ad': 'Ahmet', 'yas': 25, 'sehir': 'İstanbul'}
    for anahtar, deger in sozluk.items():
        dosya.write(f"{anahtar}: {deger}\n")
    
    # Formatlanmış yazma
    isim = "Python"
    versiyon = 3.9
    dosya.write(f"\n{isim} versiyon {versiyon:.1f}\n")

print("✅ Veri örnekleri dosyası oluşturuldu")

# Dosyayı okuyup kontrol edelim
with open(veri_dosyasi, 'r', encoding='utf-8') as dosya:
    print("Veri dosyası içeriği:")
    print(dosya.read())

# =============================================================================
# 6. DOSYA PORSİYON (SEEK VE TELL) İŞLEMLERİ
# =============================================================================

print("\n=== Dosya Pozisyon İşlemleri ===")

# tell() - mevcut pozisyonu döndürür
# seek() - belirli pozisyona gider

with open(test_dosya_yolu, 'r', encoding='utf-8') as dosya:
    print(f"Başlangıç pozisyonu: {dosya.tell()}")
    
    # İlk 10 karakteri oku
    ilk_parca = dosya.read(10)
    print(f"İlk 10 karakter: '{ilk_parca}'")
    print(f"Şu anki pozisyon: {dosya.tell()}")
    
    # Başa dön
    dosya.seek(0)
    print(f"Başa döndükten sonra pozisyon: {dosya.tell()}")
    
    # 5. karakterden itibaren oku
    dosya.seek(5)
    kalan = dosya.read(15)
    print(f"5. karakterden 15 karakter: '{kalan}'")

# =============================================================================
# 7. BINARY DOSYA İŞLEMLERİ
# =============================================================================

print("\n=== Binary Dosya İşlemleri ===")

# Binary dosya yazma
binary_dosya = "binary_test.bin"

# Text'i binary olarak yaz
text = "Merhaba Binary Dünya! 🌍"
with open(binary_dosya, 'wb') as dosya:
    dosya.write(text.encode('utf-8'))

print("✅ Binary dosya oluşturuldu")

# Binary dosya okuma
with open(binary_dosya, 'rb') as dosya:
    binary_data = dosya.read()
    decoded_text = binary_data.decode('utf-8')
    print(f"Binary'den çözülen text: {decoded_text}")
    print(f"Binary data boyutu: {len(binary_data)} byte")

# Sayıları binary olarak yazma/okuma
import struct

sayilar_binary = "sayilar.bin"
sayilar = [1, 2, 3, 4, 5, 100, 200, 300]

# Integer'ları binary olarak yaz
with open(sayilar_binary, 'wb') as dosya:
    for sayi in sayilar:
        # 4 byte integer olarak yaz
        dosya.write(struct.pack('i', sayi))

print(f"✅ {len(sayilar)} sayı binary olarak yazıldı")

# Binary'den integer'ları oku
with open(sayilar_binary, 'rb') as dosya:
    okunan_sayilar = []
    while True:
        data = dosya.read(4)  # 4 byte oku
        if not data:
            break
        sayi = struct.unpack('i', data)[0]
        okunan_sayilar.append(sayi)

print(f"Binary'den okunan sayılar: {okunan_sayilar}")

# =============================================================================
# 8. DOSYA VAR MI KONTROLÜ VE HATA YÖNETİMİ
# =============================================================================

print("\n=== Dosya Kontrolü ve Hata Yönetimi ===")

def dosya_var_mi(dosya_yolu):
    """Dosyanın var olup olmadığını kontrol eder"""
    return os.path.exists(dosya_yolu)

def dosya_boyutu_al(dosya_yolu):
    """Dosya boyutunu byte cinsinden döndürür"""
    if dosya_var_mi(dosya_yolu):
        return os.path.getsize(dosya_yolu)
    return None

# Dosya kontrolleri
test_dosyalar = [test_dosya_yolu, "olmayan_dosya.txt", buyuk_dosya]

for dosya in test_dosyalar:
    if dosya_var_mi(dosya):
        boyut = dosya_boyutu_al(dosya)
        print(f"✅ {dosya}: {boyut} byte")
    else:
        print(f"❌ {dosya}: Bulunamadı")

# Güvenli dosya okuma
def guvenli_dosya_oku(dosya_yolu):
    """Hata yönetimi ile dosya okur"""
    try:
        with open(dosya_yolu, 'r', encoding='utf-8') as dosya:
            return dosya.read()
    except FileNotFoundError:
        return f"Hata: {dosya_yolu} dosyası bulunamadı"
    except PermissionError:
        return f"Hata: {dosya_yolu} dosyasına erişim izni yok"
    except UnicodeDecodeError:
        return f"Hata: {dosya_yolu} dosyası okunamadı (encoding sorunu)"
    except Exception as e:
        return f"Beklenmeyen hata: {e}"

# Test et
print("\n--- Güvenli Dosya Okuma ---")
print("Var olan dosya:", len(guvenli_dosya_oku(test_dosya_yolu)), "karakter")
print("Olmayan dosya:", guvenli_dosya_oku("olmayan.txt"))

# =============================================================================
# 9. DOSYA METAVERİLERİ VE BİLGİLERİ
# =============================================================================

print("\n=== Dosya Metaverileri ===")

def dosya_bilgileri_al(dosya_yolu):
    """Dosya hakkında detaylı bilgi döndürür"""
    if not dosya_var_mi(dosya_yolu):
        return None
    
    stat = os.stat(dosya_yolu)
    
    return {
        'boyut': stat.st_size,
        'olusturma_zamani': stat.st_ctime,
        'degistirme_zamani': stat.st_mtime,
        'erisim_zamani': stat.st_atime,
        'dosya_mi': os.path.isfile(dosya_yolu),
        'klasor_mu': os.path.isdir(dosya_yolu),
        'mutlak_yol': os.path.abspath(dosya_yolu)
    }

# Test dosyasının bilgilerini alalım
import time

bilgiler = dosya_bilgileri_al(test_dosya_yolu)
if bilgiler:
    print(f"Dosya: {test_dosya_yolu}")
    print(f"  Boyut: {bilgiler['boyut']} byte")
    print(f"  Oluşturma: {time.ctime(bilgiler['olusturma_zamani'])}")
    print(f"  Değişiklik: {time.ctime(bilgiler['degistirme_zamani'])}")
    print(f"  Mutlak yol: {bilgiler['mutlak_yol']}")

# =============================================================================
# 10. ENCODING VE KARAKTER SETLERİ
# =============================================================================

print("\n=== Encoding ve Karakter Setleri ===")

# Farklı encoding'lerle dosya yazma
turkish_text = "Türkçe karakterler: ğüşıöçĞÜŞİÖÇ"

encodings = ['utf-8', 'latin-1', 'ascii']

for encoding in encodings:
    dosya_adi = f"test_{encoding.replace('-', '_')}.txt"
    try:
        with open(dosya_adi, 'w', encoding=encoding) as dosya:
            dosya.write(turkish_text)
        print(f"✅ {encoding} ile yazıldı: {dosya_adi}")
        
        # Tekrar oku
        with open(dosya_adi, 'r', encoding=encoding) as dosya:
            okunan = dosya.read()
            print(f"   Okunan: {okunan}")
            
    except UnicodeEncodeError as e:
        print(f"❌ {encoding} ile yazılamadı: {e}")

# =============================================================================
# 11. PERFORMANS İPUÇLARI
# =============================================================================

print("\n=== Performans İpuçları ===")

import time

def performans_testi():
    """Farklı okuma yöntemlerinin performansını test eder"""
    
    # Test için büyük dosya oluştur
    test_performance_file = "performance_test.txt"
    with open(test_performance_file, 'w') as f:
        for i in range(10000):
            f.write(f"Bu {i} numaralı satırdır.\n")
    
    # 1. read() ile tümünü oku
    start = time.time()
    with open(test_performance_file, 'r') as f:
        content = f.read()
    read_time = time.time() - start
    
    # 2. readline() ile teker teker oku
    start = time.time()
    with open(test_performance_file, 'r') as f:
        lines = []
        while True:
            line = f.readline()
            if not line:
                break
            lines.append(line)
    readline_time = time.time() - start
    
    # 3. Iterasyon ile oku
    start = time.time()
    with open(test_performance_file, 'r') as f:
        lines = [line for line in f]
    iteration_time = time.time() - start
    
    print(f"read() metodu: {read_time:.4f} saniye")
    print(f"readline() metodu: {readline_time:.4f} saniye")
    print(f"iterasyon metodu: {iteration_time:.4f} saniye")
    
    # Temizlik
    os.remove(test_performance_file)

# performans_testi()  # Çok fazla çıktı olmasın diye yorum satırında

# =============================================================================
# 12. TEMİZLİK - TEST DOSYALARINI SİL
# =============================================================================

print("\n=== Temizlik ===")

# Oluşturulan test dosyalarını sil
test_dosyalari = [
    test_dosya_yolu,
    buyuk_dosya,
    veri_dosyasi,
    binary_dosya,
    sayilar_binary,
    "test_utf_8.txt",
    "test_latin_1.txt",
    "test_ascii.txt"
]

silinen_sayisi = 0
for dosya in test_dosyalari:
    try:
        if dosya_var_mi(dosya):
            os.remove(dosya)
            silinen_sayisi += 1
            print(f"🗑️  {dosya} silindi")
    except Exception as e:
        print(f"❌ {dosya} silinemedi: {e}")

print(f"\n✅ {silinen_sayisi} test dosyası temizlendi")
print("✅ Temel dosya işlemleri tamamlandı!")
print("✅ Dosya modları ve encoding'ler öğrenildi!")
print("✅ Binary dosya işlemleri öğrenildi!")
print("✅ Hata yönetimi ve güvenli dosya işlemleri öğrenildi!")