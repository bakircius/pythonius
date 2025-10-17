"""
Python Temel Hata Yönetimi

Bu dosya Python'da hata yönetimi (exception handling) kavramlarını
kapsamlı olarak ele alır. try, except, finally, else blokları,
hata türleri ve güvenli kod yazma teknikleri öğreneceğiz.
"""

import sys
import traceback
from typing import Union, Optional
from pathlib import Path

# =============================================================================
# 1. HATA YÖNETİMİ TEMELLERİ
# =============================================================================

print("=== Hata Yönetimi Temelleri ===")

"""
Python'da hata yönetimi exception (istisna) sistemi ile yapılır:

- Exception: Program çalışırken oluşan beklenmedik durumlar
- try: Hata oluşabilecek kodun yazıldığı blok
- except: Hatayı yakalayan ve işleyen blok
- finally: Her durumda çalışan blok
- else: Hata oluşmadığında çalışan blok
- raise: Manuel hata fırlatma
"""

# 1.1 Basit hata yakalama
print("--- Basit Hata Yakalama ---")

def basit_bolme(a, b):
    """Basit bölme işlemi - hata yönetimi olmadan"""
    return a / b

def guvenli_bolme(a, b):
    """Güvenli bölme işlemi - hata yönetimi ile"""
    try:
        sonuc = a / b
        print(f"✅ {a} / {b} = {sonuc}")
        return sonuc
    except ZeroDivisionError:
        print(f"❌ Hata: Sıfıra bölme hatası! ({a} / {b})")
        return None

# Test edelim
print("Güvenli bölme testleri:")
guvenli_bolme(10, 2)
guvenli_bolme(10, 0)  # Hata oluşacak ama program durmayacak
guvenli_bolme(15, 3)

# 1.2 Çoklu except blokları
print("\n--- Çoklu Except Blokları ---")

def sayı_işle(girdi):
    """Farklı hata türlerini yakalar"""
    try:
        # String'i sayıya çevir
        sayi = int(girdi)
        
        # 100'e böl
        sonuc = 100 / sayi
        
        # Listeye eriş
        liste = [1, 2, 3]
        eleman = liste[sayi]
        
        print(f"✅ Başarılı: {girdi} -> sonuç: {sonuc}, eleman: {eleman}")
        return sonuc, eleman
        
    except ValueError:
        print(f"❌ ValueError: '{girdi}' geçerli bir sayı değil")
    except ZeroDivisionError:
        print(f"❌ ZeroDivisionError: Sıfıra bölme hatası")
    except IndexError:
        print(f"❌ IndexError: Liste indeksi hatalı (sayı: {girdi})")
    except Exception as e:
        print(f"❌ Beklenmeyen hata: {type(e).__name__}: {e}")

# Test edelim
test_girdileri = ["2", "0", "abc", "5", "-1"]
print("Sayı işleme testleri:")
for girdi in test_girdileri:
    sayı_işle(girdi)

# =============================================================================
# 2. TRY-EXCEPT-ELSE-FINALLY YAPISI
# =============================================================================

print("\n=== Try-Except-Else-Finally Yapısı ===")

def dosya_islemi(dosya_adi, icerik=""):
    """Tam hata yönetimi yapısını gösteren örnek"""
    dosya = None
    
    try:
        print(f"🔄 Dosya açılıyor: {dosya_adi}")
        dosya = open(dosya_adi, "w", encoding="utf-8")
        
        print(f"✏️  Dosyaya yazılıyor...")
        dosya.write(icerik)
        
        # Hata oluşturmak için (test)
        if "hata" in icerik.lower():
            raise ValueError("İçerikte 'hata' kelimesi bulundu!")
            
    except FileNotFoundError:
        print(f"❌ Dosya bulunamadı: {dosya_adi}")
        return False
        
    except PermissionError:
        print(f"❌ Dosya erişim izni yok: {dosya_adi}")
        return False
        
    except ValueError as e:
        print(f"❌ Değer hatası: {e}")
        return False
        
    except Exception as e:
        print(f"❌ Beklenmeyen hata: {e}")
        return False
        
    else:
        # Hata oluşmadığında çalışır
        print(f"✅ Dosya başarıyla yazıldı: {dosya_adi}")
        return True
        
    finally:
        # Her durumda çalışır
        if dosya and not dosya.closed:
            dosya.close()
            print(f"🔒 Dosya kapatıldı: {dosya_adi}")

# Test edelim
print("Dosya işlemi testleri:")
dosya_islemi("test_normal.txt", "Normal içerik")
dosya_islemi("test_hatali.txt", "Bu içerik HATA kelimesi içeriyor")

# =============================================================================
# 3. HATA BİLGİLERİNE ERİŞİM
# =============================================================================

print("\n=== Hata Bilgilerine Erişim ===")

def detayli_hata_analizi(kod_blogu):
    """Hata hakkında detaylı bilgi toplar"""
    try:
        print(f"🔄 Kod çalıştırılıyor...")
        sonuc = kod_blogu()
        print(f"✅ Başarılı sonuç: {sonuc}")
        return sonuc
        
    except Exception as e:
        print(f"\n❌ Hata yakalandı!")
        print(f"   Hata türü: {type(e).__name__}")
        print(f"   Hata mesajı: {str(e)}")
        print(f"   Hata args: {e.args}")
        
        # Traceback bilgisi
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print(f"   Dosya: {exc_traceback.tb_frame.f_code.co_filename}")
        print(f"   Satır: {exc_traceback.tb_lineno}")
        
        # Detaylı traceback
        print(f"\n📋 Detaylı Traceback:")
        traceback.print_exc()
        
        return None

# Test örnekleri
print("--- Hata Analizi Testleri ---")

# ValueError örneği
detayli_hata_analizi(lambda: int("abc"))

# ZeroDivisionError örneği
detayli_hata_analizi(lambda: 10 / 0)

# IndexError örneği
detayli_hata_analizi(lambda: [1, 2, 3][10])

# =============================================================================
# 4. NESTED (İÇ İÇE) TRY-EXCEPT BLOKLARI
# =============================================================================

print("\n=== İç İçe Try-Except Blokları ===")

def ic_ice_hata_yonetimi():
    """İç içe hata yönetimi örneği"""
    
    try:
        print("🔄 Dış try bloğu başladı")
        
        # Kullanıcıdan sayı al
        girdi = "10"  # Simüle edilmiş girdi
        
        try:
            print("🔄 İç try bloğu - sayı dönüşümü")
            sayi = int(girdi)
            
            try:
                print("🔄 En iç try bloğu - işlem")
                sonuc = 100 / sayi
                print(f"✅ Sonuç: {sonuc}")
                
            except ZeroDivisionError:
                print("❌ İç hata: Sıfıra bölme")
                raise ValueError("Sıfır değeri kabul edilmiyor") from None
                
        except ValueError as e:
            print(f"❌ Orta hata: {e}")
            # Hatayı yeniden fırlat
            raise
            
    except Exception as e:
        print(f"❌ Dış hata yakalandı: {e}")
    
    finally:
        print("🧹 Temizlik işlemi tamamlandı")

ic_ice_hata_yonetimi()

# =============================================================================
# 5. HATA YAKALAMA STRATEJİLERİ
# =============================================================================

print("\n=== Hata Yakalama Stratejileri ===")

# 5.1 Spesifik hatalar önce
def hata_onceligi_ornegi(veri):
    """Hata önceliği örneği - spesifikten genele"""
    try:
        # Karmaşık işlem simülasyonu
        if isinstance(veri, str):
            sayi = int(veri)
        else:
            sayi = veri
            
        if sayi < 0:
            raise ValueError("Negatif sayı")
        
        sonuc = 100 / sayi
        return sonuc ** 0.5
        
    except ValueError as e:
        print(f"❌ Değer hatası: {e}")
        return 0
    except ZeroDivisionError:
        print(f"❌ Sıfıra bölme hatası")
        return float('inf')
    except TypeError as e:
        print(f"❌ Tip hatası: {e}")
        return None
    except Exception as e:
        print(f"❌ Genel hata: {e}")
        return None

# Test
test_verileri = [4, "9", 0, -5, "abc", [1, 2], None]
print("Hata önceliği testleri:")
for veri in test_verileri:
    sonuc = hata_onceligi_ornegi(veri)
    print(f"  {veri} -> {sonuc}")

# 5.2 Hata gruplama
def hata_gruplama_ornegi(veri):
    """Benzer hataları gruplar"""
    try:
        sonuc = int(veri) / 2
        return sonuc
        
    except (ValueError, TypeError):
        # Tip/değer hatalarını birlikte yakala
        print(f"❌ Girdi hatası: {veri} işlenemiyor")
        return None
        
    except (ZeroDivisionError, OverflowError):
        # Matematiksel hataları birlikte yakala
        print(f"❌ Matematiksel hata")
        return None

print("\n--- Hata Gruplama ---")
for veri in ["10", None, "abc"]:
    hata_gruplama_ornegi(veri)

# =============================================================================
# 6. RAISE İLE HATA FIRLAMA
# =============================================================================

print("\n=== Raise ile Hata Fırlatma ===")

def yas_kontrol(yas):
    """Yaş kontrolü yapan fonksiyon"""
    if not isinstance(yas, int):
        raise TypeError(f"Yaş integer olmalı, {type(yas).__name__} verildi")
    
    if yas < 0:
        raise ValueError("Yaş negatif olamaz")
    
    if yas > 150:
        raise ValueError("Yaş 150'den büyük olamaz")
    
    return True

def ehliyet_kontrol(yas):
    """Ehliyet yaşı kontrolü"""
    try:
        yas_kontrol(yas)
        
        if yas < 18:
            raise ValueError("Ehliyet için minimum yaş 18")
        
        print(f"✅ {yas} yaş ehliyet için uygun")
        return True
        
    except (TypeError, ValueError) as e:
        print(f"❌ Ehliyet kontrolü hatası: {e}")
        return False

# Test edelim
print("Yaş kontrol testleri:")
test_yaslari = [25, 16, -5, 200, "otuz", None, 18]
for yas in test_yaslari:
    ehliyet_kontrol(yas)

# =============================================================================
# 7. HATA ZİNCİRLEME (EXCEPTION CHAINING)
# =============================================================================

print("\n=== Hata Zincirleme ===")

def veritabani_baglanti():
    """Veritabanı bağlantı simülasyonu"""
    import random
    if random.random() < 0.5:
        raise ConnectionError("Veritabanına bağlanılamadı")
    return "Bağlantı başarılı"

def kullanici_bilgisi_al(kullanici_id):
    """Kullanıcı bilgisi alma - hata zincirleme örneği"""
    try:
        # Veritabanı bağlantısı
        baglanti = veritabani_baglanti()
        
        # Kullanıcı sorgusu
        if kullanici_id <= 0:
            raise ValueError("Geçersiz kullanıcı ID")
        
        # Simüle edilmiş veri
        return {"id": kullanici_id, "ad": f"Kullanıcı_{kullanici_id}"}
        
    except ConnectionError as e:
        # Orijinal hatayı koruyarak yeni hata fırlat
        raise RuntimeError("Kullanıcı bilgisi alınamadı") from e
    
    except ValueError as e:
        # Hata zincirleme olmadan
        raise RuntimeError(f"Kullanıcı işlemi hatası: {e}") from None

# Test edelim
print("Hata zincirleme testleri:")
for kullanici_id in [1, -1, 5]:
    try:
        bilgi = kullanici_bilgisi_al(kullanici_id)
        print(f"✅ Kullanıcı bulundu: {bilgi}")
    except Exception as e:
        print(f"❌ Hata: {e}")
        
        # Chained exception kontrolü
        if e.__cause__:
            print(f"   Sebep: {e.__cause__}")
        if e.__context__:
            print(f"   Bağlam: {e.__context__}")

# =============================================================================
# 8. CONTEXT MANAGER İLE HATA YÖNETİMİ
# =============================================================================

print("\n=== Context Manager ile Hata Yönetimi ===")

class HataYoneticisi:
    """Hata yönetimi için context manager"""
    
    def __init__(self, islem_adi="İşlem"):
        self.islem_adi = islem_adi
        self.hatalar = []
    
    def __enter__(self):
        print(f"🔄 {self.islem_adi} başlatılıyor...")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            print(f"✅ {self.islem_adi} başarıyla tamamlandı")
        else:
            hata_mesaji = f"{exc_type.__name__}: {exc_value}"
            self.hatalar.append(hata_mesaji)
            print(f"❌ {self.islem_adi} hatası: {hata_mesaji}")
            
            # Hatayı bastır (True döndür)
            return True
    
    def hata_raporu(self):
        """Toplanan hataların raporunu verir"""
        if self.hatalar:
            print(f"📋 {self.islem_adi} hata raporu:")
            for i, hata in enumerate(self.hatalar, 1):
                print(f"   {i}. {hata}")
        else:
            print(f"✅ {self.islem_adi} hiç hata olmadı")

# Kullanım örneği
with HataYoneticisi("Veri İşleme") as hata_yoneticisi:
    print("  📊 Veri işleniyor...")
    sayi = 10 / 0  # Hata oluşacak

print("🔄 Program devam ediyor...")

# =============================================================================
# 9. HATA LOGGİNG
# =============================================================================

print("\n=== Hata Logging ===")

import logging
from datetime import datetime

# Logger yapılandırması
def hata_logger_kurulum():
    """Hata logging sistemi kurar"""
    logger = logging.getLogger('hata_logger')
    logger.setLevel(logging.DEBUG)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_handler.setFormatter(formatter)
    
    logger.addHandler(console_handler)
    return logger

logger = hata_logger_kurulum()

def loglu_islem(sayi):
    """Logging ile hata yönetimi"""
    logger.info(f"İşlem başlatıldı: {sayi}")
    
    try:
        if sayi < 0:
            raise ValueError("Negatif sayı")
        
        sonuc = 100 / sayi
        logger.info(f"İşlem başarılı: {sayi} -> {sonuc}")
        return sonuc
        
    except ValueError as e:
        logger.error(f"Değer hatası: {e}")
        raise
    except ZeroDivisionError as e:
        logger.critical(f"Kritik hata - Sıfıra bölme: {e}")
        raise
    except Exception as e:
        logger.exception(f"Beklenmeyen hata: {e}")
        raise

# Test edelim
print("Loglu işlem testleri:")
for sayi in [10, 0, -5]:
    try:
        loglu_islem(sayi)
    except Exception:
        pass  # Hata zaten loglandı

# =============================================================================
# 10. DEFENSIVE PROGRAMMING
# =============================================================================

print("\n=== Defensive Programming ===")

def guvenli_liste_erisim(liste, indeks, varsayilan=None):
    """Güvenli liste erişimi"""
    # Input validation
    if not isinstance(liste, (list, tuple)):
        raise TypeError("İlk parametre liste veya tuple olmalı")
    
    if not isinstance(indeks, int):
        raise TypeError("İndeks integer olmalı")
    
    # Güvenli erişim
    try:
        return liste[indeks]
    except IndexError:
        print(f"⚠️  İndeks {indeks} liste boyutunun ({len(liste)}) dışında")
        return varsayilan

def guvenli_sozluk_erisim(sozluk, anahtar, varsayilan=None):
    """Güvenli sözlük erişimi"""
    # Input validation
    if not isinstance(sozluk, dict):
        raise TypeError("İlk parametre dict olmalı")
    
    # Güvenli erişim
    if anahtar in sozluk:
        return sozluk[anahtar]
    else:
        print(f"⚠️  Anahtar '{anahtar}' sözlükte bulunamadı")
        return varsayilan

def guvenli_dosya_oku(dosya_yolu, encoding='utf-8'):
    """Güvenli dosya okuma"""
    # Input validation
    if not isinstance(dosya_yolu, (str, Path)):
        raise TypeError("Dosya yolu string veya Path olmalı")
    
    try:
        with open(dosya_yolu, 'r', encoding=encoding) as dosya:
            icerik = dosya.read()
            print(f"✅ Dosya başarıyla okundu: {dosya_yolu}")
            return icerik
            
    except FileNotFoundError:
        print(f"❌ Dosya bulunamadı: {dosya_yolu}")
        return None
    except PermissionError:
        print(f"❌ Dosya erişim izni yok: {dosya_yolu}")
        return None
    except UnicodeDecodeError as e:
        print(f"❌ Encoding hatası: {e}")
        return None
    except Exception as e:
        print(f"❌ Beklenmeyen hata: {e}")
        return None

# Test edelim
print("Defensive programming testleri:")

# Güvenli liste erişimi
test_liste = [1, 2, 3, 4, 5]
print(f"Liste[2] = {guvenli_liste_erisim(test_liste, 2)}")
print(f"Liste[10] = {guvenli_liste_erisim(test_liste, 10, 'Bulunamadı')}")

# Güvenli sözlük erişimi
test_sozluk = {"ad": "Ahmet", "yas": 30}
print(f"Sözlük['ad'] = {guvenli_sozluk_erisim(test_sozluk, 'ad')}")
print(f"Sözlük['meslek'] = {guvenli_sozluk_erisim(test_sozluk, 'meslek', 'Bilinmiyor')}")

# =============================================================================
# 11. HATA YÖNETİMİ BEST PRACTICES
# =============================================================================

print("\n=== Hata Yönetimi Best Practices ===")

def ornek_best_practice_fonksiyon(veri, islem="toplama"):
    """
    Best practice örneği:
    1. Input validation
    2. Spesifik hata yakalama
    3. Anlamlı hata mesajları
    4. Logging
    5. Graceful degradation
    """
    
    # 1. Input validation
    if not isinstance(veri, (list, tuple)):
        raise TypeError(f"Veri liste veya tuple olmalı, {type(veri).__name__} verildi")
    
    if not veri:
        raise ValueError("Veri boş olamaz")
    
    if islem not in ["toplama", "çarpma", "ortalama"]:
        raise ValueError(f"Desteklenmeyen işlem: {islem}")
    
    logger.info(f"İşlem başlatıldı: {islem} - {len(veri)} eleman")
    
    try:
        # 2. İşlemi gerçekleştir
        if islem == "toplama":
            sonuc = sum(veri)
        elif islem == "çarpma":
            sonuc = 1
            for x in veri:
                sonuc *= x
        elif islem == "ortalama":
            sonuc = sum(veri) / len(veri)
        
        logger.info(f"İşlem başarılı: {sonuc}")
        return sonuc
        
    except TypeError as e:
        # 3. Spesifik hata mesajı
        hata_mesaji = f"Veri elemanları sayısal olmalı: {e}"
        logger.error(hata_mesaji)
        raise ValueError(hata_mesaji) from e
        
    except OverflowError as e:
        hata_mesaji = f"Sonuç çok büyük: {e}"
        logger.error(hata_mesaji)
        raise ValueError(hata_mesaji) from e
        
    except Exception as e:
        # 4. Beklenmeyen hatalar
        hata_mesaji = f"Beklenmeyen hata oluştu: {e}"
        logger.exception(hata_mesaji)
        raise RuntimeError(hata_mesaji) from e

# Test edelim
print("Best practice testleri:")
test_verileri = [
    ([1, 2, 3, 4, 5], "toplama"),
    ([2, 3, 4], "çarpma"),
    ([10, 20, 30], "ortalama"),
    ("geçersiz", "toplama"),  # Hata
    ([1, "iki", 3], "toplama"),  # Hata
]

for veri, islem in test_verileri:
    try:
        sonuc = ornek_best_practice_fonksiyon(veri, islem)
        print(f"✅ {islem}({veri}) = {sonuc}")
    except Exception as e:
        print(f"❌ {islem}({veri}) -> {e}")

# =============================================================================
# 12. PERFORMANS VE HATA YÖNETİMİ
# =============================================================================

print("\n=== Performans ve Hata Yönetimi ===")

import time

def performans_karsilastir():
    """EAFP vs LBYL performans karşılaştırması"""
    
    test_verileri = ["1", "2", "abc", "4", "xyz"] * 1000
    
    # LBYL (Look Before You Leap) yaklaşımı
    start = time.time()
    lbyl_sonuclar = []
    for veri in test_verileri:
        if veri.isdigit():  # Önce kontrol et
            lbyl_sonuclar.append(int(veri))
    lbyl_sure = time.time() - start
    
    # EAFP (Easier to Ask for Forgiveness than Permission) yaklaşımı
    start = time.time()
    eafp_sonuclar = []
    for veri in test_verileri:
        try:
            eafp_sonuclar.append(int(veri))  # Direkt dene
        except ValueError:
            pass
    eafp_sure = time.time() - start
    
    print(f"LBYL yaklaşımı: {lbyl_sure:.4f} saniye")
    print(f"EAFP yaklaşımı: {eafp_sure:.4f} saniye")
    print(f"Hız farkı: {lbyl_sure/eafp_sure:.2f}x")
    print(f"Sonuç sayısı: LBYL={len(lbyl_sonuclar)}, EAFP={len(eafp_sonuclar)}")

# performans_karsilastir()  # Uzun sürebilir, yorum satırında

print("\n💡 Hata Yönetimi İpuçları:")
print("✅ Spesifik hataları yakalayın (Exception yerine ValueError, etc.)")
print("✅ Hata mesajlarını anlaşılır yazın")
print("✅ Logging kullanın")
print("✅ EAFP yaklaşımını tercih edin (Pythonic)")
print("✅ Finally blokunda temizlik yapın")
print("✅ Input validation yapın")
print("✅ Hataları sessizce geçmeyin")

print("\n✅ Temel hata yönetimi öğrenildi!")
print("✅ Try-except-finally yapısı öğrenildi!")
print("✅ Hata türleri ve yakalama stratejileri öğrenildi!")
print("✅ Best practices ve defensive programming öğrenildi!")