"""
Python Hata Türleri ve Exception Hierarchy

Bu dosya Python'daki farklı hata türlerini ve exception hiyerarşisini
kapsamlı olarak ele alır. Built-in exception'lar, hata kategorileri
ve her hata türüne özgü yakalama yöntemleri öğreneceğiz.
"""

import sys
import math
import json
from collections import defaultdict

# =============================================================================
# 1. PYTHON EXCEPTION HİYERAŞİSİ
# =============================================================================

print("=== Python Exception Hiyerarşisi ===")

"""
Python Exception Hiyerarşisi:

BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
"""

def exception_hiyerarsi_goster():
    """Exception hiyerarşisini gösterir"""
    
    def hiyerarsi_yazdir(exception_class, level=0):
        indent = "  " * level
        print(f"{indent}{exception_class.__name__}")
        
        # Alt sınıfları göster (sadece direct subclasses)
        subclasses = exception_class.__subclasses__()
        for subclass in sorted(subclasses, key=lambda x: x.__name__):
            if level < 2:  # Çok derin gitmeyelim
                hiyerarsi_yazdir(subclass, level + 1)
    
    print("Temel Exception Hiyerarşisi:")
    hiyerarsi_yazdir(Exception)

exception_hiyerarsi_goster()

# =============================================================================
# 2. ARİTMETİK HATALAR (ArithmeticError)
# =============================================================================

print("\n=== Aritmetik Hatalar ===")

def aritmetik_hata_ornekleri():
    """Aritmetik hataların örnekleri"""
    
    # ZeroDivisionError
    print("--- ZeroDivisionError ---")
    try:
        sonuc = 10 / 0
    except ZeroDivisionError as e:
        print(f"❌ Sıfıra bölme: {e}")
    
    try:
        sonuc = 10 % 0
    except ZeroDivisionError as e:
        print(f"❌ Sıfıra mod alma: {e}")
    
    # OverflowError
    print("\n--- OverflowError ---")
    try:
        # Çok büyük sayı
        sonuc = math.exp(1000)  # e^1000
    except OverflowError as e:
        print(f"❌ Sayı çok büyük: {e}")
    
    # Kompleks sayılar için
    try:
        kompleks_sayi = complex(10**308, 10**308)
        sonuc = kompleks_sayi ** 2
    except OverflowError as e:
        print(f"❌ Kompleks sayı overflow: {e}")
    
    # FloatingPointError (çok nadir)
    print("\n--- FloatingPointError ---")
    # Bu genellikle C uzantılarında oluşur
    print("⚠️  FloatingPointError genellikle C uzantılarında oluşur")

aritmetik_hata_ornekleri()

# =============================================================================
# 3. LOOKUP HATALARI (LookupError)
# =============================================================================

print("\n=== Lookup Hataları ===")

def lookup_hata_ornekleri():
    """Lookup hatalarının örnekleri"""
    
    # IndexError
    print("--- IndexError ---")
    liste = [1, 2, 3, 4, 5]
    
    try:
        eleman = liste[10]
    except IndexError as e:
        print(f"❌ Liste indeks hatası: {e}")
        print(f"   Liste boyutu: {len(liste)}, erişilen indeks: 10")
    
    try:
        # Negatif indeks de hata verebilir
        eleman = liste[-10]
    except IndexError as e:
        print(f"❌ Negatif indeks hatası: {e}")
    
    # String için IndexError
    try:
        metin = "Merhaba"
        karakter = metin[20]
    except IndexError as e:
        print(f"❌ String indeks hatası: {e}")
    
    # KeyError
    print("\n--- KeyError ---")
    sozluk = {"ad": "Ahmet", "yas": 30, "sehir": "İstanbul"}
    
    try:
        deger = sozluk["meslek"]
    except KeyError as e:
        print(f"❌ Sözlük anahtar hatası: {e}")
        print(f"   Mevcut anahtarlar: {list(sozluk.keys())}")
    
    # Nested dictionary KeyError
    try:
        nested_dict = {"kisi": {"ad": "Ayşe"}}
        deger = nested_dict["kisi"]["soyad"]
    except KeyError as e:
        print(f"❌ İç içe sözlük anahtar hatası: {e}")

lookup_hata_ornekleri()

# =============================================================================
# 4. TİP HATALARI (TypeError)
# =============================================================================

print("\n=== Tip Hataları ===")

def tip_hata_ornekleri():
    """TypeError örnekleri"""
    
    # Desteklenmeyen operasyon
    print("--- Desteklenmeyen Operasyonlar ---")
    try:
        sonuc = "merhaba" + 5
    except TypeError as e:
        print(f"❌ String + int: {e}")
    
    try:
        sonuc = "abc" * "def"
    except TypeError as e:
        print(f"❌ String * string: {e}")
    
    # Yanlış fonksiyon çağrısı
    print("\n--- Yanlış Fonksiyon Çağrısı ---")
    try:
        sonuc = len()  # Parametre eksik
    except TypeError as e:
        print(f"❌ Parametre eksik: {e}")
    
    try:
        sonuc = int("123", "456", "789")  # Fazla parametre
    except TypeError as e:
        print(f"❌ Fazla parametre: {e}")
    
    # Immutable obje değiştirme
    print("\n--- Immutable Obje Değiştirme ---")
    try:
        tuple_obj = (1, 2, 3)
        tuple_obj[0] = 10
    except TypeError as e:
        print(f"❌ Tuple değiştirme: {e}")
    
    try:
        string_obj = "merhaba"
        string_obj[0] = "M"
    except TypeError as e:
        print(f"❌ String değiştirme: {e}")
    
    # Çağrılamayan obje
    print("\n--- Çağrılamayan Obje ---")
    try:
        sayi = 42
        sonuc = sayi()  # int çağrılamaz
    except TypeError as e:
        print(f"❌ Int çağırma: {e}")

tip_hata_ornekleri()

# =============================================================================
# 5. DEĞER HATALARI (ValueError)
# =============================================================================

print("\n=== Değer Hataları ===")

def deger_hata_ornekleri():
    """ValueError örnekleri"""
    
    # Tip doğru ama değer yanlış
    print("--- Tip Doğru, Değer Yanlış ---")
    try:
        sayi = int("abc")  # String ama sayı değil
    except ValueError as e:
        print(f"❌ String'den int: {e}")
    
    try:
        sayi = float("merhaba")
    except ValueError as e:
        print(f"❌ String'den float: {e}")
    
    # Matematik fonksiyonları
    print("\n--- Matematik Değer Hataları ---")
    try:
        sonuc = math.sqrt(-1)  # Negatif sayının karekökü
    except ValueError as e:
        print(f"❌ Negatif karekök: {e}")
    
    try:
        sonuc = math.log(-5)  # Negatif sayının logaritması
    except ValueError as e:
        print(f"❌ Negatif logaritma: {e}")
    
    try:
        sonuc = math.acos(2)  # Domain dışı (-1 ile 1 arası olmalı)
    except ValueError as e:
        print(f"❌ acos domain hatası: {e}")
    
    # JSON decode hatası
    print("\n--- JSON Değer Hataları ---")
    try:
        veri = json.loads("{geçersiz json}")
    except json.JSONDecodeError as e:  # ValueError'dan türemiş
        print(f"❌ JSON decode: {e}")
    
    # Unpack hatası
    print("\n--- Unpack Değer Hataları ---")
    try:
        a, b, c = [1, 2]  # 3 değişken, 2 değer
    except ValueError as e:
        print(f"❌ Unpack hatası: {e}")
    
    try:
        x, y = [1, 2, 3, 4]  # 2 değişken, 4 değer
    except ValueError as e:
        print(f"❌ Çok fazla değer unpack: {e}")

deger_hata_ornekleri()

# =============================================================================
# 6. NAME VE ATTRIBUTE HATALARI
# =============================================================================

print("\n=== Name ve Attribute Hataları ===")

def name_attribute_hata_ornekleri():
    """NameError ve AttributeError örnekleri"""
    
    # NameError
    print("--- NameError ---")
    try:
        print(tanimsiz_degisken)  # Tanımsız değişken
    except NameError as e:
        print(f"❌ Tanımsız değişken: {e}")
    
    try:
        sonuc = tanimsiz_fonksiyon()  # Tanımsız fonksiyon
    except NameError as e:
        print(f"❌ Tanımsız fonksiyon: {e}")
    
    # UnboundLocalError (NameError'dan türemiş)
    print("\n--- UnboundLocalError ---")
    def problemli_fonksiyon():
        try:
            print(local_degisken)  # Kullanmadan önce tanımlanmamış
            local_degisken = "değer"
        except UnboundLocalError as e:
            print(f"❌ Local değişken hatası: {e}")
    
    problemli_fonksiyon()
    
    # AttributeError
    print("\n--- AttributeError ---")
    try:
        sayi = 42
        uzunluk = sayi.length  # int'in length özelliği yok
    except AttributeError as e:
        print(f"❌ Özellik yok: {e}")
    
    try:
        liste = [1, 2, 3]
        liste.append_all([4, 5])  # Böyle bir metod yok
    except AttributeError as e:
        print(f"❌ Metod yok: {e}")
    
    # Module AttributeError
    try:
        import os
        os.nonexistent_function()
    except AttributeError as e:
        print(f"❌ Module fonksiyonu yok: {e}")

name_attribute_hata_ornekleri()

# =============================================================================
# 7. DOSYA VE OS HATALARI (OSError)
# =============================================================================

print("\n=== Dosya ve OS Hataları ===")

def os_hata_ornekleri():
    """OSError ve alt sınıflarının örnekleri"""
    
    # FileNotFoundError
    print("--- FileNotFoundError ---")
    try:
        with open("olmayan_dosya.txt", "r") as dosya:
            icerik = dosya.read()
    except FileNotFoundError as e:
        print(f"❌ Dosya bulunamadı: {e}")
    
    # PermissionError
    print("\n--- PermissionError ---")
    try:
        # Root-only dosyaya yazma (Unix/Linux)
        with open("/etc/passwd", "w") as dosya:
            dosya.write("test")
    except PermissionError as e:
        print(f"❌ İzin hatası: {e}")
    except FileNotFoundError:
        print("⚠️  Bu örnek Unix/Linux sistemlerde çalışır")
    
    # IsADirectoryError
    print("\n--- IsADirectoryError ---")
    import os
    import tempfile
    
    # Geçici klasör oluştur
    temp_dir = tempfile.mkdtemp()
    try:
        with open(temp_dir, "r") as dosya:  # Klasörü dosya gibi açmaya çalış
            icerik = dosya.read()
    except IsADirectoryError as e:
        print(f"❌ Klasör hatası: {e}")
    finally:
        os.rmdir(temp_dir)
    
    # FileExistsError
    print("\n--- FileExistsError ---")
    test_dosya = "test_dosya.txt"
    
    # Önce dosyayı oluştur
    with open(test_dosya, "w") as dosya:
        dosya.write("test")
    
    try:
        # Exclusive creation mode
        with open(test_dosya, "x") as dosya:
            dosya.write("yeni içerik")
    except FileExistsError as e:
        print(f"❌ Dosya zaten var: {e}")
    finally:
        # Temizlik
        try:
            os.remove(test_dosya)
        except:
            pass

os_hata_ornekleri()

# =============================================================================
# 8. İMPORT HATALARI
# =============================================================================

print("\n=== Import Hataları ===")

def import_hata_ornekleri():
    """Import hatalarının örnekleri"""
    
    # ModuleNotFoundError
    print("--- ModuleNotFoundError ---")
    try:
        import olmayan_modul
    except ModuleNotFoundError as e:
        print(f"❌ Modül bulunamadı: {e}")
    
    # ImportError (genel)
    print("\n--- ImportError ---")
    try:
        from math import olmayan_fonksiyon
    except ImportError as e:
        print(f"❌ İmport hatası: {e}")
    
    # Circular import simulation
    print("\n--- Circular Import Benzeri ---")
    try:
        # Bu normalde circular import yapar
        # from sys import modules
        # modules['__main__'] = "problem"
        pass
    except ImportError as e:
        print(f"❌ Circular import: {e}")

import_hata_ornekleri()

# =============================================================================
# 9. SİSTEM HATALARI
# =============================================================================

print("\n=== Sistem Hataları ===")

def sistem_hata_ornekleri():
    """Sistem seviyesi hataların örnekleri"""
    
    # RecursionError
    print("--- RecursionError ---")
    def sonsuz_recursion(x):
        return sonsuz_recursion(x + 1)
    
    try:
        sonsuz_recursion(0)
    except RecursionError as e:
        print(f"❌ Recursion limiti: Maksimum recursion derinliği aşıldı")
        print(f"   Limit: {sys.getrecursionlimit()}")
    
    # MemoryError (simülasyon zor)
    print("\n--- MemoryError ---")
    try:
        # Çok büyük liste (hafıza yetmezse hata verir)
        # buyuk_liste = [0] * (10**10)  # Çok tehlikeli!
        print("⚠️  MemoryError simülasyonu atlandı (sistem güvenliği)")
    except MemoryError as e:
        print(f"❌ Hafıza hatası: {e}")
    
    # SystemError (çok nadir)
    print("\n--- SystemError ---")
    print("⚠️  SystemError genellikle Python interpreter hatalarında oluşur")
    
    # KeyboardInterrupt
    print("\n--- KeyboardInterrupt ---")
    print("⚠️  Ctrl+C ile program durdurulduğunda KeyboardInterrupt oluşur")
    
    # SystemExit
    print("\n--- SystemExit ---")
    try:
        sys.exit(1)  # Program çıkışı
    except SystemExit as e:
        print(f"❌ Sistem çıkışı yakalandı: exit code {e.code}")

sistem_hata_ornekleri()

# =============================================================================
# 10. ASSERTION HATALARI
# =============================================================================

print("\n=== Assertion Hataları ===")

def assertion_hata_ornekleri():
    """AssertionError örnekleri"""
    
    print("--- AssertionError ---")
    
    def yas_kontrol(yas):
        assert isinstance(yas, int), "Yaş integer olmalı"
        assert yas >= 0, "Yaş negatif olamaz"
        assert yas <= 150, "Yaş 150'den büyük olamaz"
        return True
    
    test_yaslari = [25, -5, "otuz", 200]
    
    for yas in test_yaslari:
        try:
            yas_kontrol(yas)
            print(f"✅ Yaş geçerli: {yas}")
        except AssertionError as e:
            print(f"❌ Assertion hatası ({yas}): {e}")
    
    # Assertion debug kontrolü
    print(f"\n📊 Debug modu: {__debug__}")
    if __debug__:
        print("   Assertionlar aktif")
    else:
        print("   Assertionlar devre dışı (-O bayrağı ile)")

assertion_hata_ornekleri()

# =============================================================================
# 11. UNICODE VE ENCODING HATALARI
# =============================================================================

print("\n=== Unicode ve Encoding Hataları ===")

def unicode_hata_ornekleri():
    """Unicode hatalarının örnekleri"""
    
    # UnicodeDecodeError
    print("--- UnicodeDecodeError ---")
    try:
        # Latin-1 encoded bytes'ı UTF-8 olarak decode etmeye çalış
        latin_bytes = "çğşı".encode('latin-1')
        utf8_string = latin_bytes.decode('utf-8')
    except UnicodeDecodeError as e:
        print(f"❌ Unicode decode hatası: {e}")
        print(f"   Encoding: {e.encoding}")
        print(f"   Pozisyon: {e.start}-{e.end}")
        print(f"   Neden: {e.reason}")
    
    # UnicodeEncodeError  
    print("\n--- UnicodeEncodeError ---")
    try:
        # Türkçe karakterleri ASCII'ye encode etmeye çalış
        turkce_metin = "Türkçe karakterler: çğıöşü"
        ascii_bytes = turkce_metin.encode('ascii')
    except UnicodeEncodeError as e:
        print(f"❌ Unicode encode hatası: {e}")
        print(f"   Encoding: {e.encoding}")
        print(f"   Pozisyon: {e.start}-{e.end}")
        print(f"   Karakter: '{e.object[e.start:e.end]}'")
    
    # Güvenli encoding
    print("\n--- Güvenli Encoding ---")
    turkce_metin = "Türkçe karakterler: çğıöşü"
    
    # Hataları göz ardı et
    ascii_ignore = turkce_metin.encode('ascii', errors='ignore')
    print(f"ignore: {ascii_ignore}")
    
    # Hataları değiştir
    ascii_replace = turkce_metin.encode('ascii', errors='replace')
    print(f"replace: {ascii_replace}")
    
    # Hataları escape et
    ascii_backslash = turkce_metin.encode('ascii', errors='backslashreplace')
    print(f"backslashreplace: {ascii_backslash}")

unicode_hata_ornekleri()

# =============================================================================
# 12. HATA TÜRLERİ KARŞILAŞTIRMASI VE SEÇİM
# =============================================================================

print("\n=== Hata Türleri Karşılaştırması ===")

def hata_turlerini_karsilastir():
    """Farklı hata türlerini karşılaştırır"""
    
    hata_sayilari = defaultdict(int)
    
    test_islemleri = [
        # (İşlem, Beklenen Hata Türü)
        (lambda: 10 / 0, ZeroDivisionError),
        (lambda: int("abc"), ValueError),
        (lambda: [1, 2, 3][10], IndexError),
        (lambda: {"a": 1}["b"], KeyError),
        (lambda: "hello" + 5, TypeError),
        (lambda: nonexistent_var, NameError),
        (lambda: (42).nonexistent_attr, AttributeError),
        (lambda: open("nonexistent.txt"), FileNotFoundError),
    ]
    
    print("Hata türü testleri:")
    for i, (islem, beklenen_hata) in enumerate(test_islemleri, 1):
        try:
            sonuc = islem()
            print(f"  {i}. ✅ Başarılı (beklenmedik)")
        except Exception as e:
            hata_turu = type(e).__name__
            hata_sayilari[hata_turu] += 1
            
            if isinstance(e, beklenen_hata):
                print(f"  {i}. ✅ Beklenen hata: {hata_turu}")
            else:
                print(f"  {i}. ❌ Beklenmeyen hata: {hata_turu} (beklenen: {beklenen_hata.__name__})")
    
    print(f"\nHata türü istatistikleri:")
    for hata_turu, sayi in sorted(hata_sayilari.items()):
        print(f"  {hata_turu}: {sayi} adet")

hata_turlerini_karsilastir()

# =============================================================================
# 13. HATA TÜRLERİ BEST PRACTICES
# =============================================================================

print("\n=== Hata Türleri Best Practices ===")

def hata_turleri_best_practices():
    """Hata türleri için en iyi pratikler"""
    
    print("📋 Hata Yakalama Kuralları:")
    print("1. En spesifik hatayı önce yakala")
    print("2. Birden fazla hata türünü grupla")
    print("3. Exception'ı son çare olarak kullan")
    print("4. Hatanın nedenini anla ve uygun aksiyonu al")
    
    def ornek_fonksiyon(veri):
        """Best practice örneği"""
        try:
            # Veri dönüşümü
            if isinstance(veri, str):
                sayi = int(veri)
            else:
                sayi = float(veri)
            
            # İşlem
            sonuc = 100 / sayi
            return sonuc
            
        except (ValueError, TypeError) as e:
            # Veri türü/değer hataları
            print(f"❌ Veri hatası: {e}")
            return None
            
        except ZeroDivisionError:
            # Matematik hatası
            print(f"❌ Sıfıra bölme hatası")
            return float('inf')
            
        except Exception as e:
            # Beklenmeyen hatalar
            print(f"❌ Beklenmeyen hata: {type(e).__name__}: {e}")
            return None
    
    # Test
    test_verileri = [10, "5", 0, "abc", [1, 2], None]
    print("\nBest practice testi:")
    for veri in test_verileri:
        sonuc = ornek_fonksiyon(veri)
        print(f"  {veri} -> {sonuc}")

hata_turleri_best_practices()

print("\n💡 Hata Türleri İpuçları:")
print("✅ Her hata türünün amacını ve ne zaman oluştuğunu öğrenin")
print("✅ Hata hiyerarşisini anlayın (LookupError > IndexError)")
print("✅ Uygun hata türünü yakalayın (Exception yerine spesifik)")
print("✅ Hata mesajlarından yararlanın (encoding, position, reason)")
print("✅ Birden fazla ilgili hatayı tuple ile gruplayın")
print("✅ BaseException alt türlerini (SystemExit, KeyboardInterrupt) genellikle yakalamayın")

print("\n✅ Python hata türleri öğrenildi!")
print("✅ Exception hiyerarşisi öğrenildi!")
print("✅ Spesifik hata yakalama teknikleri öğrenildi!")
print("✅ Hata türü seçimi best practices öğrenildi!")