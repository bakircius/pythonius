"""
Python Debugging Teknikleri

Bu dosya Python'da debugging, hata ayıklama teknikleri, debugger kullanımı,
profiling, code inspection ve geliştirme araçlarını kapsamlı olarak ele alır.
"""

import pdb
import traceback
import sys
import inspect
import dis
import cProfile
import pstats
import io
import time
import logging
from functools import wraps
from typing import Any, Callable, Dict, List
from datetime import datetime

# =============================================================================
# 1. TEMEL DEBUGGING TEKNİKLERİ
# =============================================================================

print("=== Temel Debugging Teknikleri ===")

def temel_debugging_ornekleri():
    """Temel debugging teknikleri"""
    
    # Print debugging (en temel)
    print("--- Print Debugging ---")
    
    def problem_fonksiyon(liste):
        print(f"🔍 Fonksiyon başlangıcı: liste={liste}")
        
        toplam = 0
        for i, sayi in enumerate(liste):
            print(f"🔍 İterasyon {i}: sayi={sayi}, mevcut_toplam={toplam}")
            toplam += sayi
            
        print(f"🔍 Fonksiyon sonu: toplam={toplam}")
        return toplam
    
    sonuc = problem_fonksiyon([1, 2, 3, 4])
    print(f"Sonuç: {sonuc}\n")
    
    # Assert debugging
    print("--- Assert Debugging ---")
    
    def guvenli_bolme(a, b):
        print(f"🔍 Bölme işlemi: {a} / {b}")
        
        # Girdi kontrolleri
        assert isinstance(a, (int, float)), f"a sayı olmalı: {type(a)}"
        assert isinstance(b, (int, float)), f"b sayı olmalı: {type(b)}"
        assert b != 0, f"Sıfıra bölme hatası: b={b}"
        
        sonuc = a / b
        
        # Çıktı kontrolü
        assert not (sonuc != sonuc), f"NaN sonucu: {a}/{b}={sonuc}"  # NaN kontrolü
        
        print(f"🔍 Sonuç: {sonuc}")
        return sonuc
    
    try:
        guvenli_bolme(10, 2)
        guvenli_bolme(10, 0)  # Assert hatası
    except AssertionError as e:
        print(f"❌ Assert hatası: {e}")

temel_debugging_ornekleri()

# =============================================================================
# 2. TRACEBACK ANALİZİ
# =============================================================================

print("\n=== Traceback Analizi ===")

def traceback_analizi():
    """Traceback analizi ve manipülasyonu"""
    
    def ic_fonksiyon():
        """İç içe fonksiyon hata örneği"""
        hata_verisi = {"durum": "hata"}
        problematik_islem = 1 / 0  # ZeroDivisionError
        return problematik_islem
    
    def orta_fonksiyon():
        """Orta seviye fonksiyon"""
        return ic_fonksiyon()
    
    def dis_fonksiyon():
        """Dış fonksiyon"""
        return orta_fonksiyon()
    
    try:
        dis_fonksiyon()
    except Exception as e:
        print("--- Standart Traceback ---")
        traceback.print_exc()
        
        print("\n--- Detaylı Traceback Analizi ---")
        exc_type, exc_value, exc_traceback = sys.exc_info()
        
        print(f"Hata Türü: {exc_type.__name__}")
        print(f"Hata Mesajı: {exc_value}")
        
        print("\n🔍 Stack Trace Analizi:")
        stack_summary = traceback.extract_tb(exc_traceback)
        
        for i, frame in enumerate(stack_summary):
            print(f"  {i+1}. {frame.filename}:{frame.lineno}")
            print(f"     Fonksiyon: {frame.name}")
            print(f"     Kod: {frame.line}")
        
        print("\n--- Formatted Traceback ---")
        formatted_lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        for line in formatted_lines:
            print(line.rstrip())

traceback_analizi()

# =============================================================================
# 3. PYTHON DEBUGGER (PDB) KULLANIMI
# =============================================================================

print("\n=== Python Debugger (PDB) ===")

def pdb_ornekleri():
    """PDB kullanım örnekleri"""
    
    print("📋 PDB Komutları:")
    print("   l (list): Mevcut kodu göster")
    print("   n (next): Sonraki satıra geç")
    print("   s (step): Fonksiyona gir")
    print("   c (continue): Çalışmaya devam et")
    print("   p <var>: Değişken değerini yazdır")
    print("   pp <var>: Pretty print değişken")
    print("   w (where): Stack trace göster")
    print("   u (up): Stack'te yukarı çık")
    print("   d (down): Stack'te aşağı in")
    print("   b <line>: Breakpoint koy")
    print("   cl: Breakpoint'leri temizle")
    print("   q (quit): Debugger'dan çık")
    
    # PDB kullanım örneği (manuel başlatma)
    def debug_ornegi():
        """Debugger ile debug edilecek fonksiyon"""
        sayilar = [1, 2, 3, 4, 5]
        toplam = 0
        
        for i, sayi in enumerate(sayilar):
            # pdb.set_trace()  # Breakpoint (yorumda)
            toplam += sayi * 2
            
        return toplam
    
    sonuc = debug_ornegi()
    print(f"Sonuç: {sonuc}")
    
    # Post-mortem debugging
    print("\n--- Post-mortem Debugging ---")
    
    def hata_ile_fonksiyon():
        x = 10
        y = 0
        return x / y  # Hata oluşacak
    
    try:
        hata_ile_fonksiyon()
    except:
        print("Hata oluştu, post-mortem debug için pdb.pm() kullanılabilir")
        # pdb.pm()  # Post-mortem debugger (yorumda)

pdb_ornekleri()

# =============================================================================
# 4. FUNCTION INSPECTION VE INTROSPECTION
# =============================================================================

print("\n=== Function Inspection ===")

def inspection_ornekleri():
    """Code inspection ve introspection"""
    
    def ornek_fonksiyon(a: int, b: str = "varsayılan", *args, **kwargs) -> str:
        """Örnek fonksiyon
        
        Args:
            a: Integer parametre
            b: String parametre
            *args: Değişken sayıda argüman
            **kwargs: Anahtar kelime argümanları
            
        Returns:
            String sonuç
        """
        return f"{a} - {b}"
    
    print("--- Fonksiyon Bilgileri ---")
    print(f"Fonksiyon adı: {ornek_fonksiyon.__name__}")
    print(f"Docstring: {ornek_fonksiyon.__doc__}")
    print(f"Modül: {ornek_fonksiyon.__module__}")
    print(f"Annotations: {ornek_fonksiyon.__annotations__}")
    
    # Signature analizi
    print("\n--- Signature Analizi ---")
    sig = inspect.signature(ornek_fonksiyon)
    print(f"Signature: {sig}")
    
    for param_name, param in sig.parameters.items():
        print(f"  {param_name}:")
        print(f"    Tür: {param.annotation if param.annotation != param.empty else 'Belirtilmemiş'}")
        print(f"    Varsayılan: {param.default if param.default != param.empty else 'Yok'}")
        print(f"    Kind: {param.kind}")
    
    # Source code
    print("\n--- Source Code ---")
    try:
        source = inspect.getsource(ornek_fonksiyon)
        print("Kaynak kod:")
        print(source)
    except:
        print("Kaynak kod alınamadı")
    
    # Frame inspection
    print("\n--- Frame Inspection ---")
    frame = inspect.currentframe()
    print(f"Fonksiyon: {frame.f_code.co_name}")
    print(f"Dosya: {frame.f_code.co_filename}")
    print(f"Satır: {frame.f_lineno}")
    print(f"Locals: {list(frame.f_locals.keys())}")

inspection_ornekleri()

# =============================================================================
# 5. BYTECODE ANALİZİ
# =============================================================================

print("\n=== Bytecode Analizi ===")

def bytecode_analizi():
    """Python bytecode analizi"""
    
    def basit_fonksiyon(x, y):
        """Basit fonksiyon bytecode analizi için"""
        z = x + y
        if z > 10:
            return z * 2
        else:
            return z
    
    print("--- Bytecode Disassembly ---")
    dis.dis(basit_fonksiyon)
    
    # Code object bilgileri
    print("\n--- Code Object Bilgileri ---")
    code = basit_fonksiyon.__code__
    print(f"Argüman sayısı: {code.co_argcount}")
    print(f"Local değişken sayısı: {code.co_nlocals}")
    print(f"Stack boyutu: {code.co_stacksize}")
    print(f"Değişken isimleri: {code.co_varnames}")
    print(f"Constant'lar: {code.co_consts}")
    print(f"İsimler: {code.co_names}")

bytecode_analizi()

# =============================================================================
# 6. PROFILING VE PERFORMANCE DEBUGGING
# =============================================================================

print("\n=== Profiling ve Performance ===")

def profiling_ornekleri():
    """Profiling ve performance analizi"""
    
    # Basit zamanlama
    print("--- Basit Zamanlama ---")
    
    def yavas_fonksiyon():
        """Kasıtlı olarak yavaş fonksiyon"""
        total = 0
        for i in range(100000):
            total += i ** 2
        return total
    
    start_time = time.time()
    sonuc = yavas_fonksiyon()
    end_time = time.time()
    
    print(f"Sonuç: {sonuc}")
    print(f"Süre: {end_time - start_time:.4f} saniye")
    
    # cProfile kullanımı
    print("\n--- cProfile Analizi ---")
    
    def profile_edilen_kod():
        """Profile edilecek kod"""
        # Çeşitli işlemler
        liste = []
        for i in range(1000):
            liste.append(i ** 2)
        
        # Dictionary işlemleri
        sozluk = {}
        for i in range(500):
            sozluk[f"key_{i}"] = i * 3
        
        # String işlemleri
        metin = ""
        for i in range(200):
            metin += f"sayı_{i}_"
        
        return len(liste) + len(sozluk) + len(metin)
    
    # Profile
    profiler = cProfile.Profile()
    profiler.enable()
    
    sonuc = profile_edilen_kod()
    
    profiler.disable()
    
    # Sonuçları analiz et
    s = io.StringIO()
    ps = pstats.Stats(profiler, stream=s)
    ps.sort_stats('cumulative')
    ps.print_stats(10)  # İlk 10 sonucu göster
    
    print("Profiling sonuçları:")
    print(s.getvalue())

profiling_ornekleri()

# =============================================================================
# 7. LOGGING ILE DEBUGGING
# =============================================================================

print("\n=== Logging ile Debugging ===")

def logging_debugging_setup():
    """Logging ile debugging kurulumu"""
    
    # Özel formatter
    class DebugFormatter(logging.Formatter):
        """Debug için özel formatter"""
        
        def format(self, record):
            # Frame bilgilerini ekle
            frame = inspect.currentframe()
            if frame and frame.f_back and frame.f_back.f_back:
                caller_frame = frame.f_back.f_back
                record.caller_function = caller_frame.f_code.co_name
                record.caller_line = caller_frame.f_lineno
            else:
                record.caller_function = "unknown"
                record.caller_line = 0
            
            return super().format(record)
    
    # Logger kurulumu
    logger = logging.getLogger('debug_logger')
    logger.setLevel(logging.DEBUG)
    
    # Handler
    handler = logging.StreamHandler()
    formatter = DebugFormatter(
        '%(asctime)s - %(levelname)s - %(caller_function)s:%(caller_line)d - %(message)s'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger

def debug_decorator(func):
    """Debug için decorator"""
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger('debug_logger')
        
        # Fonksiyon başlangıcı
        logger.debug(f"🚀 {func.__name__} başladı")
        logger.debug(f"   Args: {args}")
        logger.debug(f"   Kwargs: {kwargs}")
        
        start_time = time.time()
        
        try:
            sonuc = func(*args, **kwargs)
            end_time = time.time()
            
            logger.debug(f"✅ {func.__name__} başarılı")
            logger.debug(f"   Sonuç: {sonuc}")
            logger.debug(f"   Süre: {end_time - start_time:.4f}s")
            
            return sonuc
            
        except Exception as e:
            end_time = time.time()
            
            logger.error(f"❌ {func.__name__} hata")
            logger.error(f"   Hata: {e}")
            logger.error(f"   Süre: {end_time - start_time:.4f}s")
            
            raise
    
    return wrapper

def logging_debugging_ornegi():
    """Logging ile debugging örneği"""
    
    # Logger'ı kur
    logger = logging_debugging_setup()
    
    @debug_decorator
    def hesaplama_fonksiyonu(a, b, operation="add"):
        """Matematiksel işlem fonksiyonu"""
        logger = logging.getLogger('debug_logger')
        
        logger.debug(f"İşlem türü: {operation}")
        
        if operation == "add":
            sonuc = a + b
        elif operation == "multiply":
            sonuc = a * b
        elif operation == "divide":
            if b == 0:
                logger.warning("Sıfıra bölme riski!")
                raise ValueError("Sıfıra bölme")
            sonuc = a / b
        else:
            logger.error(f"Bilinmeyen işlem: {operation}")
            raise ValueError(f"Desteklenmeyen işlem: {operation}")
        
        return sonuc
    
    # Test işlemleri
    test_islemleri = [
        (10, 5, "add"),
        (10, 5, "multiply"),
        (10, 5, "divide"),
        (10, 0, "divide"),  # Hata oluşacak
        (10, 5, "unknown")  # Hata oluşacak
    ]
    
    for a, b, op in test_islemleri:
        try:
            sonuc = hesaplama_fonksiyonu(a, b, op)
            print(f"✅ {a} {op} {b} = {sonuc}")
        except Exception as e:
            print(f"❌ {a} {op} {b} -> {e}")
        print()

logging_debugging_ornegi()

# =============================================================================
# 8. MEMORY DEBUGGING
# =============================================================================

print("\n=== Memory Debugging ===")

def memory_debugging():
    """Memory debugging teknikleri"""
    
    import gc
    import sys
    
    print("--- Memory Profiling ---")
    
    # Object tracking
    def object_counter():
        """Object sayısını say"""
        return len(gc.get_objects())
    
    # Başlangıç durumu
    initial_objects = object_counter()
    print(f"Başlangıç object sayısı: {initial_objects}")
    
    # Memory intensive işlem
    def memory_intensive_operation():
        """Hafıza yoğun işlem"""
        big_list = []
        for i in range(10000):
            big_list.append([i] * 100)
        return big_list
    
    # Işlem öncesi
    before_objects = object_counter()
    
    big_data = memory_intensive_operation()
    
    # İşlem sonrası
    after_objects = object_counter()
    print(f"İşlem sonrası object sayısı: {after_objects}")
    print(f"Oluşturulan object sayısı: {after_objects - before_objects}")
    
    # Memory usage
    import psutil
    import os
    
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    print(f"RSS Memory: {memory_info.rss / 1024 / 1024:.2f} MB")
    print(f"VMS Memory: {memory_info.vms / 1024 / 1024:.2f} MB")
    
    # Cleanup
    del big_data
    gc.collect()
    
    after_cleanup = object_counter()
    print(f"Cleanup sonrası object sayısı: {after_cleanup}")

try:
    memory_debugging()
except ImportError:
    print("⚠️  psutil paketi bulunamadı, memory debugging atlandı")

# =============================================================================
# 9. DEBUGGING BEST PRACTICES
# =============================================================================

print("\n=== Debugging Best Practices ===")

def debugging_best_practices():
    """Debugging best practices"""
    
    print("📋 Debugging Best Practices:")
    print("1. 🔍 Sorunun localizasyonunu yapın")
    print("2. 📝 Hatayı tekrarlanabilir hale getirin")
    print("3. 🧪 En küçük test case'i oluşturun")
    print("4. 📊 Logging kullanın (print değil)")
    print("5. 🛠️  Debugger'ı öğrenin ve kullanın")
    print("6. 🔬 Code inspection araçlarını kullanın")
    print("7. ⚡ Performance profiling yapın")
    print("8. 🧹 Clean code yazın (debug edilebilir)")
    print("9. 📚 Exception handling yapın")
    print("10. 🔄 Test-driven development yapın")
    
    print("\n🛠️  Debugging Araçları:")
    print("• pdb: Python Debugger")
    print("• cProfile: Performance profiling")
    print("• traceback: Hata analizi")
    print("• inspect: Code introspection")
    print("• dis: Bytecode analizi")
    print("• logging: Structured debugging")
    print("• IDE debuggers: Visual debugging")
    print("• Memory profilers: Memory leaks")
    
    print("\n⚠️  Debugging Tuzakları:")
    print("• Heisenbugs: Debug sırasında kaybolan hatalar")
    print("• Race conditions: Timing-dependent hatalar")
    print("• Memory leaks: Hafıza sızıntıları")
    print("• Side effects: Beklenmeyen yan etkiler")
    print("• State mutations: Durum değişiklikleri")

debugging_best_practices()

# =============================================================================
# 10. İNTERAKTİF DEBUGGING TOOLS
# =============================================================================

print("\n=== İnteraktif Debugging ===")

def interaktif_debugging_araclari():
    """İnteraktif debugging araçları"""
    
    print("🛠️  İnteraktif Debugging Araçları:")
    
    # IPython'da debugging
    print("\n--- IPython/Jupyter Debugging ---")
    print("• %debug: Post-mortem debugging")
    print("• %pdb: Otomatik debugger")
    print("• %run -d: Script debug")
    print("• %timeit: Performance ölçümü")
    print("• %memit: Memory ölçümü")
    print("• %lprun: Line profiling")
    
    # VS Code debugging
    print("\n--- VS Code Debugging ---")
    print("• Breakpoints: F9")
    print("• Start debugging: F5") 
    print("• Step over: F10")
    print("• Step into: F11")
    print("• Step out: Shift+F11")
    print("• Continue: F5")
    print("• Variable inspection")
    print("• Watch expressions")
    print("• Call stack")
    
    # PyCharm debugging
    print("\n--- PyCharm Debugging ---")
    print("• Visual debugger")
    print("• Conditional breakpoints")
    print("• Exception breakpoints")
    print("• Remote debugging")
    print("• Memory viewer")
    print("• Thread debugging")
    
    # Terminal-based debugging
    print("\n--- Terminal Debugging ---")
    print("• pdb: python -m pdb script.py")
    print("• pudb: Enhanced pdb")
    print("• pdb++: Improved pdb")
    print("• winpdb: Cross-platform")

interaktif_debugging_araclari()

print("\n💡 Debugging İpuçları:")
print("✅ Sistematik yaklaşım kullanın")
print("✅ Binary search ile hata aralığını daraltın")
print("✅ Rubber duck debugging uygulayın")
print("✅ Pair debugging yapın")
print("✅ Defensive programming kullanın")
print("✅ Unit testler yazın")
print("✅ Code review süreçlerini uygulayın")

print("\n✅ Python debugging teknikleri öğrenildi!")
print("✅ Profiling ve performance analizi öğrenildi!")
print("✅ Code inspection teknikleri öğrenildi!")
print("✅ Interactive debugging araçları öğrenildi!")