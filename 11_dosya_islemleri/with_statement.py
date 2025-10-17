"""
Python With Statement ve Context Managers

Bu dosya Python'da with statement kullanımını ve context manager
kavramını detaylı olarak ele alır. Güvenli kaynak yönetimi ve
otomatik temizlik işlemleri konularını öğreneceğiz.
"""

import os
import time
import sys
from contextlib import contextmanager, closing
import tempfile
import threading
import sqlite3

# =============================================================================
# 1. WITH STATEMENT TEMELLERİ
# =============================================================================

print("=== With Statement Temelleri ===")

# Geleneksel dosya açma/kapama
print("--- Geleneksel Yöntem ---")
try:
    dosya = open("test_geleneksel.txt", "w", encoding="utf-8")
    dosya.write("Geleneksel yöntemle yazıldı")
    dosya.close()  # Manuel olarak kapatmak gerekir
    print("✅ Geleneksel yöntem: Dosya manuel olarak kapatıldı")
except Exception as e:
    print(f"❌ Hata: {e}")
    # Hata durumunda dosya açık kalabilir!

# With statement ile (önerilen yöntem)
print("\n--- With Statement Yöntemi ---")
try:
    with open("test_with.txt", "w", encoding="utf-8") as dosya:
        dosya.write("With statement ile yazıldı")
        # Dosya blok sonunda otomatik olarak kapanır
    print("✅ With statement: Dosya otomatik olarak kapatıldı")
except Exception as e:
    print(f"❌ Hata: {e}")
    # Hata durumunda bile dosya otomatik kapanır!

# İki dosyayı aynı anda açma
print("\n--- Çoklu Dosya Açma ---")
with open("dosya1.txt", "w") as f1, open("dosya2.txt", "w") as f2:
    f1.write("İlk dosya içeriği")
    f2.write("İkinci dosya içeriği")
print("✅ İki dosya da otomatik olarak kapatıldı")

# =============================================================================
# 2. CONTEXT MANAGER NEDİR?
# =============================================================================

print("\n=== Context Manager Nedir? ===")

"""
Context Manager, with statement ile kullanılabilen objelerdir.
İki özel metodu vardır:
- __enter__(): Blok başlangıcında çalışır
- __exit__(): Blok sonunda çalışır (hata olsa da olmasa da)
"""

class DogrulamaContextManager:
    """Basit bir context manager örneği"""
    
    def __init__(self, isim):
        self.isim = isim
        print(f"🔧 Context Manager oluşturuldu: {self.isim}")
    
    def __enter__(self):
        print(f"🚪 {self.isim} - Enter metoduna girdi")
        print(f"🔄 {self.isim} - Kaynaklar hazırlanıyor...")
        return self  # with ... as variable için dönen değer
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(f"🚪 {self.isim} - Exit metoduna girdi")
        print(f"🧹 {self.isim} - Temizlik yapılıyor...")
        
        if exc_type:
            print(f"❌ {self.isim} - Hata yakalandı: {exc_type.__name__}: {exc_value}")
            return False  # Hatayı yeniden fırlat
        else:
            print(f"✅ {self.isim} - Normal şekilde tamamlandı")
        
        return False

# Context manager kullanımı
print("\n--- Normal Kullanım ---")
with DogrulamaContextManager("TestManager") as manager:
    print("📝 With bloğu içinde işlem yapılıyor")
    print(f"📋 Manager objesi: {manager.isim}")

print("\n--- Hata Durumunda ---")
try:
    with DogrulamaContextManager("HataManager") as manager:
        print("📝 With bloğu içinde işlem yapılıyor")
        raise ValueError("Test hatası!")
except ValueError as e:
    print(f"🔴 Yakalanan hata: {e}")

# =============================================================================
# 3. DOSYA İŞLEMLERİNDE WITH STATEMENT
# =============================================================================

print("\n=== Dosya İşlemlerinde With Statement ===")

# Dosya yazma ve okuma
dosya_adi = "with_ornegi.txt"

# Dosya yazma
with open(dosya_adi, "w", encoding="utf-8") as dosya:
    dosya.write("Python with statement örneği\n")
    dosya.write("Otomatik kaynak yönetimi\n")
    dosya.write("Güvenli dosya işlemleri\n")

print("✅ Dosya yazma tamamlandı")

# Dosya okuma
with open(dosya_adi, "r", encoding="utf-8") as dosya:
    print("📖 Dosya içeriği:")
    for satir_no, satir in enumerate(dosya, 1):
        print(f"  {satir_no}: {satir.strip()}")

# Dosya ekleme
with open(dosya_adi, "a", encoding="utf-8") as dosya:
    dosya.write(f"Eklenme zamanı: {time.ctime()}\n")

print("✅ Dosyaya ekleme yapıldı")

# Dosya boyutunu kontrol
with open(dosya_adi, "r", encoding="utf-8") as dosya:
    icerik = dosya.read()
    print(f"📊 Dosya boyutu: {len(icerik)} karakter")

# =============================================================================
# 4. ÖZEL CONTEXT MANAGER ÖRNEKLERİ
# =============================================================================

print("\n=== Özel Context Manager Örnekleri ===")

class ZamanOlcucu:
    """İşlem süresini ölçen context manager"""
    
    def __init__(self, islem_adi="İşlem"):
        self.islem_adi = islem_adi
        self.baslangic_zamani = None
    
    def __enter__(self):
        print(f"⏰ {self.islem_adi} başlatılıyor...")
        self.baslangic_zamani = time.time()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        bitis_zamani = time.time()
        sure = bitis_zamani - self.baslangic_zamani
        print(f"⌛ {self.islem_adi} tamamlandı: {sure:.4f} saniye")
        return False

# Zaman ölçücü kullanımı
with ZamanOlcucu("Dosya İşlemi"):
    with open("zaman_testi.txt", "w") as f:
        for i in range(1000):
            f.write(f"Satır {i+1}\n")
    time.sleep(0.1)  # Biraz bekleme

class LogYazici:
    """Log dosyasına yazan context manager"""
    
    def __init__(self, log_dosyasi="islem.log"):
        self.log_dosyasi = log_dosyasi
        self.log_file = None
    
    def __enter__(self):
        self.log_file = open(self.log_dosyasi, "a", encoding="utf-8")
        self.log(f"İşlem başlatıldı")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.log(f"Hata oluştu: {exc_type.__name__}: {exc_value}")
        else:
            self.log("İşlem başarıyla tamamlandı")
        
        if self.log_file:
            self.log_file.close()
        return False
    
    def log(self, mesaj):
        zaman_damgasi = time.strftime("%Y-%m-%d %H:%M:%S")
        self.log_file.write(f"[{zaman_damgasi}] {mesaj}\n")
        self.log_file.flush()  # Hemen diske yaz

# Log yazıcı kullanımı
print("\n--- Log Yazıcı Örneği ---")
with LogYazici("test.log") as logger:
    logger.log("Özel log mesajı")
    logger.log("İşlem devam ediyor")

# Log dosyasını oku
with open("test.log", "r", encoding="utf-8") as f:
    print("📋 Log dosyası içeriği:")
    print(f.read())

# =============================================================================
# 5. @CONTEXTMANAGER DECORATOR
# =============================================================================

print("\n=== @contextmanager Decorator ===")

"""
contextlib.contextmanager decorator'ı ile generator fonksiyonları
context manager'a dönüştürebiliriz. Bu daha basit ve okunabilir.
"""

@contextmanager
def gecici_dosya(dosya_adi, icerik=""):
    """Geçici dosya oluşturan context manager"""
    print(f"📁 Geçici dosya oluşturuluyor: {dosya_adi}")
    
    # __enter__ kısmı
    with open(dosya_adi, "w", encoding="utf-8") as f:
        f.write(icerik)
    
    try:
        yield dosya_adi  # with ... as variable için değer
    finally:
        # __exit__ kısmı
        if os.path.exists(dosya_adi):
            os.remove(dosya_adi)
            print(f"🗑️  Geçici dosya silindi: {dosya_adi}")

# Geçici dosya kullanımı
with gecici_dosya("gecici.txt", "Bu geçici bir dosyadır") as dosya_yolu:
    print(f"📄 Geçici dosya: {dosya_yolu}")
    
    # Dosyayı oku
    with open(dosya_yolu, "r", encoding="utf-8") as f:
        print(f"📖 İçerik: {f.read()}")

@contextmanager
def klasor_degistir(yeni_klasor):
    """Geçici olarak klasör değiştiren context manager"""
    eski_klasor = os.getcwd()
    
    try:
        print(f"📂 Klasör değiştiriliyor: {eski_klasor} -> {yeni_klasor}")
        os.chdir(yeni_klasor)
        yield yeni_klasor
    finally:
        print(f"📂 Eski klasöre dönülüyor: {eski_klasor}")
        os.chdir(eski_klasor)

# Geçici klasör değişimi
mevcut_klasor = os.getcwd()
print(f"\n📍 Şu anki klasör: {mevcut_klasor}")

# with klasor_degistir("/tmp"):  # Unix/Linux için
#     print(f"📍 Geçici klasör: {os.getcwd()}")

# print(f"📍 Geri döndü: {os.getcwd()}")

# =============================================================================
# 6. VERITABANI BAĞLANTILARI
# =============================================================================

print("\n=== Veritabanı Bağlantıları ===")

# SQLite veritabanı ile context manager kullanımı
@contextmanager
def veritabani_baglanti(db_dosyasi):
    """SQLite veritabanı bağlantısı için context manager"""
    conn = None
    try:
        print(f"🔌 Veritabanına bağlanılıyor: {db_dosyasi}")
        conn = sqlite3.connect(db_dosyasi)
        yield conn
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"❌ Veritabanı hatası: {e}")
        raise
    finally:
        if conn:
            conn.close()
            print("🔌 Veritabanı bağlantısı kapatıldı")

# Veritabanı kullanımı
with veritabani_baglanti("test.db") as conn:
    cursor = conn.cursor()
    
    # Tablo oluştur
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS kullanicilar (
            id INTEGER PRIMARY KEY,
            ad TEXT NOT NULL,
            email TEXT UNIQUE
        )
    """)
    
    # Veri ekle
    cursor.execute("INSERT OR REPLACE INTO kullanicilar (ad, email) VALUES (?, ?)", 
                   ("Ahmet", "ahmet@example.com"))
    
    # Veri sorgula
    cursor.execute("SELECT * FROM kullanicilar")
    sonuclar = cursor.fetchall()
    
    print("👥 Kullanıcılar:")
    for sonuc in sonuclar:
        print(f"  ID: {sonuc[0]}, Ad: {sonuc[1]}, Email: {sonuc[2]}")
    
    # Değişiklikleri kaydet
    conn.commit()

# =============================================================================
# 7. THREAD GÜVENLİĞİ VE LOCK'LAR
# =============================================================================

print("\n=== Thread Güvenliği ===")

# Thread lock ile context manager
kilit = threading.Lock()

@contextmanager
def thread_kilidi(lock, timeout=5):
    """Thread kilidi için context manager"""
    acquired = False
    try:
        print("🔒 Kilit alınmaya çalışılıyor...")
        acquired = lock.acquire(timeout=timeout)
        if not acquired:
            raise TimeoutError("Kilit alınamadı")
        print("🔓 Kilit alındı")
        yield
    finally:
        if acquired:
            lock.release()
            print("🔒 Kilit serbest bırakıldı")

# Paylaşılan değişken
sayac = 0

def guvenli_artir():
    """Thread-safe sayaç artırma"""
    global sayac
    with thread_kilidi(kilit):
        eski_deger = sayac
        time.sleep(0.001)  # İşlem simülasyonu
        sayac = eski_deger + 1
        print(f"🔢 Sayaç: {eski_deger} -> {sayac}")

# Tek thread'de test
print("--- Thread Güvenli Sayaç ---")
for _ in range(3):
    guvenli_artir()

# =============================================================================
# 8. DOSYA KILITLEME
# =============================================================================

print("\n=== Dosya Kilitleme ===")

class DosyaKilidi:
    """Dosya kilidi context manager"""
    
    def __init__(self, dosya_yolu, mod="w"):
        self.dosya_yolu = dosya_yolu
        self.mod = mod
        self.dosya = None
        self.kilit_dosyasi = dosya_yolu + ".lock"
    
    def __enter__(self):
        # Kilit dosyası kontrol et
        if os.path.exists(self.kilit_dosyasi):
            raise RuntimeError(f"Dosya zaten kilitli: {self.dosya_yolu}")
        
        # Kilit dosyası oluştur
        with open(self.kilit_dosyasi, "w") as lock_file:
            lock_file.write(str(os.getpid()))
        
        # Asıl dosyayı aç
        self.dosya = open(self.dosya_yolu, self.mod, encoding="utf-8")
        print(f"🔐 Dosya kilitlendi: {self.dosya_yolu}")
        return self.dosya
    
    def __exit__(self, exc_type, exc_value, traceback):
        # Dosyayı kapat
        if self.dosya:
            self.dosya.close()
        
        # Kilit dosyasını sil
        if os.path.exists(self.kilit_dosyasi):
            os.remove(self.kilit_dosyasi)
        
        print(f"🔓 Dosya kilidi kaldırıldı: {self.dosya_yolu}")
        return False

# Dosya kilidi kullanımı
with DosyaKilidi("kilitli_dosya.txt", "w") as dosya:
    dosya.write("Bu dosya kilitli bir şekilde yazıldı\n")
    dosya.write(f"İşlem zamanı: {time.ctime()}\n")

# =============================================================================
# 9. HATA YÖNETİMİ VE EXCEPTION HANDLING
# =============================================================================

print("\n=== Hata Yönetimi ===")

class HataYoneticisi:
    """Hata durumlarını yöneten context manager"""
    
    def __init__(self, log_dosyasi="hata.log"):
        self.log_dosyasi = log_dosyasi
        self.hatalar = []
    
    def __enter__(self):
        print("🛡️  Hata yöneticisi aktif")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            hata_mesaji = f"{exc_type.__name__}: {exc_value}"
            self.hatalar.append(hata_mesaji)
            
            # Log dosyasına yaz
            with open(self.log_dosyasi, "a", encoding="utf-8") as log:
                zaman = time.strftime("%Y-%m-%d %H:%M:%S")
                log.write(f"[{zaman}] HATA: {hata_mesaji}\n")
            
            print(f"❌ Hata yakalandı ve loglandı: {hata_mesaji}")
            return True  # Hatayı bastır
        
        print("✅ İşlem hatasız tamamlandı")
        return False
    
    def hata_ekle(self, mesaj):
        """Manuel hata ekleme"""
        self.hatalar.append(mesaj)
        print(f"⚠️  Manuel hata: {mesaj}")

# Hata yöneticisi kullanımı
print("--- Normal İşlem ---")
with HataYoneticisi() as hata_yoneticisi:
    print("📝 Normal işlem yapılıyor")
    hata_yoneticisi.hata_ekle("Bu bir uyarı mesajı")

print("\n--- Hatalı İşlem ---")
with HataYoneticisi() as hata_yoneticisi:
    print("📝 Hatalı işlem yapılıyor")
    sayi = 10 / 0  # ZeroDivisionError

print("🔄 Program devam ediyor...")

# =============================================================================
# 10. PERFORMANS VE KAYNAK YÖNETİMİ
# =============================================================================

print("\n=== Performans ve Kaynak Yönetimi ===")

@contextmanager
def performans_olcucu(islem_adi="İşlem"):
    """Bellek ve süre ölçen context manager"""
    import psutil
    
    # Başlangıç değerleri
    baslangic_zamani = time.time()
    process = psutil.Process()
    baslangic_bellek = process.memory_info().rss / 1024 / 1024  # MB
    
    print(f"📊 {islem_adi} başlıyor...")
    print(f"   Başlangıç bellek: {baslangic_bellek:.2f} MB")
    
    try:
        yield
    finally:
        # Bitiş değerleri
        bitis_zamani = time.time()
        bitis_bellek = process.memory_info().rss / 1024 / 1024  # MB
        
        sure = bitis_zamani - baslangic_zamani
        bellek_farki = bitis_bellek - baslangic_bellek
        
        print(f"📊 {islem_adi} tamamlandı:")
        print(f"   Süre: {sure:.4f} saniye")
        print(f"   Bitiş bellek: {bitis_bellek:.2f} MB")
        print(f"   Bellek farkı: {bellek_farki:+.2f} MB")

# Performans ölçücü kullanımı (psutil yoksa hata verebilir)
try:
    with performans_olcucu("Büyük Liste Oluşturma"):
        buyuk_liste = [i**2 for i in range(100000)]
        time.sleep(0.1)
except ImportError:
    print("⚠️  psutil modülü bulunamadı, performans ölçümü atlandı")

# =============================================================================
# 11. ÇOKLU CONTEXT MANAGER
# =============================================================================

print("\n=== Çoklu Context Manager ===")

# ExitStack ile çoklu context manager
from contextlib import ExitStack

def coklu_dosya_islem():
    """Çoklu dosya işlemi"""
    with ExitStack() as stack:
        # Birden fazla dosyayı aynı anda aç
        dosya1 = stack.enter_context(open("coklu1.txt", "w"))
        dosya2 = stack.enter_context(open("coklu2.txt", "w"))
        dosya3 = stack.enter_context(open("coklu3.txt", "w"))
        
        # Zaman ölçücü ekle
        timer = stack.enter_context(ZamanOlcucu("Çoklu Dosya İşlemi"))
        
        # Dosyalara yaz
        for i in range(10):
            dosya1.write(f"Dosya 1 - Satır {i+1}\n")
            dosya2.write(f"Dosya 2 - Satır {i+1}\n")
            dosya3.write(f"Dosya 3 - Satır {i+1}\n")
        
        print("✅ Üç dosyaya da yazıldı")
        # Tüm dosyalar otomatik olarak kapanacak

coklu_dosya_islem()

# =============================================================================
# 12. TEMİZLİK - TEST DOSYALARINI SİL
# =============================================================================

print("\n=== Temizlik ===")

# Oluşturulan test dosyalarını sil
test_dosyalari = [
    "test_geleneksel.txt",
    "test_with.txt",
    "dosya1.txt",
    "dosya2.txt",
    "with_ornegi.txt",
    "zaman_testi.txt",
    "test.log",
    "test.db",
    "kilitli_dosya.txt",
    "hata.log",
    "coklu1.txt",
    "coklu2.txt",
    "coklu3.txt"
]

silinen_sayisi = 0
for dosya in test_dosyalari:
    try:
        if os.path.exists(dosya):
            os.remove(dosya)
            silinen_sayisi += 1
    except Exception as e:
        print(f"❌ {dosya} silinemedi: {e}")

print(f"🗑️  {silinen_sayisi} test dosyası temizlendi")

print("\n✅ With Statement ve Context Manager öğrenildi!")
print("✅ Güvenli kaynak yönetimi öğrenildi!")
print("✅ Özel context manager'lar oluşturma öğrenildi!")
print("✅ Hata yönetimi ve performans izleme öğrenildi!")