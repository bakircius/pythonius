"""
Python Dekoratörler - Giriş Seviyesi Kılavuz

Bu dosya Python'da dekoratör kavramını temelinden başlayarak öğretir.
Dekoratörler, fonksiyonları değiştirmek veya genişletmek için kullanılan
güçlü bir Python özelliğidir.
"""

# =============================================================================
# 1. DEKORATÖR NEDİR?
# =============================================================================

"""
Dekoratör, bir fonksiyonu alıp onu değiştirebilen veya genişletebilen özel bir fonksiyondur.
Dekoratörler, mevcut kodları değiştirmeden yeni özellikler eklememizi sağlar.

Temel yapı:
@dekorator_adi
def fonksiyon():
    pass
"""

print("=== Dekoratör Nedir? ===")

# İlk olarak, dekoratör olmadan bir örnek
def selam_ver():
    return "Merhaba!"

print(f"Normal fonksiyon: {selam_ver()}")

# Şimdi, bir fonksiyonu manuel olarak "dekore" edelim
def buyuk_harfle(func):
    """Fonksiyonun sonucunu büyük harfe çeviren dekoratör"""
    def wrapper():
        sonuc = func()
        return sonuc.upper()
    return wrapper

# Manuel dekorasyon
selam_ver_buyuk = buyuk_harfle(selam_ver)
print(f"Manuel dekore edilmiş: {selam_ver_buyuk()}")

# =============================================================================
# 2. DEKORATÖR SÖZDİZİMİ (@)
# =============================================================================

print("\n=== @ Sözdizimi ===")

# @ sembolu ile dekoratör kullanımı
@buyuk_harfle
def hosgeldin_mesaji():
    return "Hoş geldiniz!"

print(f"@ ile dekore edilmiş: {hosgeldin_mesaji()}")

# Bu, aşağıdaki ile aynıdır:
# hosgeldin_mesaji = buyuk_harfle(hosgeldin_mesaji)

# =============================================================================
# 3. PARAMETRE ALAN FONKSİYONLAR İÇİN DEKORATÖR
# =============================================================================

def log_fonksiyon(func):
    """Fonksiyon çağrısını loglayan dekoratör"""
    def wrapper(*args, **kwargs):
        print(f"🔍 {func.__name__} fonksiyonu çağrılıyor...")
        print(f"   Parametreler: args={args}, kwargs={kwargs}")
        sonuc = func(*args, **kwargs)
        print(f"   Sonuç: {sonuc}")
        print(f"✅ {func.__name__} tamamlandı\n")
        return sonuc
    return wrapper

@log_fonksiyon
def topla(a, b):
    return a + b

@log_fonksiyon
def selamla(isim, mesaj="Merhaba"):
    return f"{mesaj} {isim}!"

print("=== Parametre Alan Fonksiyonlar ===")
topla(5, 3)
selamla("Ahmet")
selamla("Ayşe", mesaj="İyi günler")

# =============================================================================
# 4. SÜRE ÖLÇEN DEKORATÖR
# =============================================================================

import time
import functools

def sure_olc(func):
    """Fonksiyonun çalışma süresini ölçen dekoratör"""
    @functools.wraps(func)  # Orijinal fonksiyonun metadata'sını korur
    def wrapper(*args, **kwargs):
        başlangıç = time.time()
        sonuc = func(*args, **kwargs)
        bitiş = time.time()
        süre = bitiş - başlangıç
        print(f"⏱️  {func.__name__} {süre:.4f} saniyede tamamlandı")
        return sonuc
    return wrapper

@sure_olc
def yavas_islem():
    """Yavaş bir işlem simülasyonu"""
    time.sleep(0.1)
    return "İşlem tamamlandı"

@sure_olc
def liste_isle(boyut=1000):
    """Liste işleme örneği"""
    return [x**2 for x in range(boyut)]

print("=== Süre Ölçme ===")
yavas_islem()
liste_isle(5000)

# =============================================================================
# 5. ÖNBELLEK (CACHE) DEKORATÖRÜ
# =============================================================================

def cache(func):
    """Basit önbellek dekoratörü"""
    _cache = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Anahtarı oluştur
        key = str(args) + str(sorted(kwargs.items()))
        
        if key in _cache:
            print(f"💾 Önbellekten alındı: {func.__name__}{args}")
            return _cache[key]
        
        print(f"🔄 Hesaplanıyor: {func.__name__}{args}")
        sonuc = func(*args, **kwargs)
        _cache[key] = sonuc
        return sonuc
    
    return wrapper

@cache
def fibonacci(n):
    """Fibonacci sayısını hesaplar"""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

@cache
def faktoriyel(n):
    """Faktöriyel hesaplar"""
    if n <= 1:
        return 1
    return n * faktoriyel(n-1)

print("\n=== Önbellek Dekoratörü ===")
print(f"Fibonacci(10) = {fibonacci(10)}")
print(f"Fibonacci(10) = {fibonacci(10)}")  # Önbellekten
print(f"Faktöriyel(5) = {faktoriyel(5)}")
print(f"Faktöriyel(5) = {faktoriyel(5)}")  # Önbellekten

# =============================================================================
# 6. RETRY (YENİDEN DENEME) DEKORATÖRÜ
# =============================================================================

def retry(max_attempts=3, delay=1):
    """Hata durumunda yeniden deneme dekoratörü"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"🚫 Attempt {attempt + 1} failed: {e}")
                    if attempt == max_attempts - 1:
                        print(f"❌ All {max_attempts} attempts failed")
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator

# Başarısız olabilen fonksiyon simülasyonu
import random

@retry(max_attempts=3, delay=0.5)
def riskli_islem():
    """%70 ihtimalle başarısız olan işlem"""
    if random.random() < 0.7:
        raise Exception("Rastgele hata oluştu!")
    return "İşlem başarılı!"

print("\n=== Retry Dekoratörü ===")
try:
    sonuc = riskli_islem()
    print(f"✅ {sonuc}")
except Exception as e:
    print(f"❌ Nihai hata: {e}")

# =============================================================================
# 7. DOĞRULAMA (VALİDATİON) DEKORATÖRÜ
# =============================================================================

def tip_dogrula(*expected_types):
    """Tip doğrulama dekoratörü"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Pozisyonel argümanları kontrol et
            for i, (arg, expected_type) in enumerate(zip(args, expected_types)):
                if not isinstance(arg, expected_type):
                    raise TypeError(
                        f"{func.__name__} fonksiyonunun {i+1}. parametresi "
                        f"{expected_type.__name__} tipinde olmalı, "
                        f"ama {type(arg).__name__} verildi"
                    )
            return func(*args, **kwargs)
        return wrapper
    return decorator

@tip_dogrula(int, int)
def guvenli_topla(a, b):
    """Sadece integer kabul eden toplama"""
    return a + b

@tip_dogrula(str, int)
def string_tekrarla(metin, tekrar):
    """String'i belirtilen sayıda tekrarlar"""
    return metin * tekrar

print("\n=== Tip Doğrulama ===")
print(f"Güvenli toplama: {guvenli_topla(5, 3)}")
print(f"String tekrar: {string_tekrarla('Merhaba! ', 3)}")

# Hatalı kullanım
try:
    guvenli_topla("5", 3)  # String + int
except TypeError as e:
    print(f"❌ Tip hatası: {e}")

# =============================================================================
# 8. ÇOKLU DEKORATÖR KULLANIMI
# =============================================================================

@sure_olc
@log_fonksiyon
@cache
def karmasik_hesaplama(n):
    """Çoklu dekoratör örneği"""
    result = sum(i**2 for i in range(n))
    time.sleep(0.01)  # Hesaplama simülasyonu
    return result

print("\n=== Çoklu Dekoratör ===")
karmasik_hesaplama(100)
karmasik_hesaplama(100)  # Önbellekten gelecek

# =============================================================================
# 9. SINIF DEKORATÖRLERI
# =============================================================================

def sinif_dekoratoru(cls):
    """Sınıfa yeni özellikler ekleyen dekoratör"""
    # Sınıfa yeni metod ekle
    def __str__(self):
        return f"{cls.__name__} instance with {len(self.__dict__)} attributes"
    
    cls.__str__ = __str__
    
    # Sınıfa yeni attribute ekle
    cls._decorated = True
    
    return cls

@sinif_dekoratoru
class Kisi:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas

print("\n=== Sınıf Dekoratörü ===")
kisi = Kisi("Ahmet", 25)
print(kisi)  # Dekoratörün eklediği __str__ metodu
print(f"Dekore edildi mi? {kisi._decorated}")

# =============================================================================
# 10. PROPERTİES VE DEKORATÖR
# =============================================================================

class Dikdortgen:
    def __init__(self, genislik, yukseklik):
        self._genislik = genislik
        self._yukseklik = yukseklik
    
    @property
    def alan(self):
        """Alan hesaplama property'si"""
        return self._genislik * self._yukseklik
    
    @property
    def cevre(self):
        """Çevre hesaplama property'si"""
        return 2 * (self._genislik + self._yukseklik)
    
    @property
    def genislik(self):
        return self._genislik
    
    @genislik.setter
    def genislik(self, deger):
        if deger <= 0:
            raise ValueError("Genişlik pozitif olmalı")
        self._genislik = deger
    
    @property
    def yukseklik(self):
        return self._yukseklik
    
    @yukseklik.setter
    def yukseklik(self, deger):
        if deger <= 0:
            raise ValueError("Yükseklik pozitif olmalı")
        self._yukseklik = deger

print("\n=== Property Dekoratörleri ===")
dikdortgen = Dikdortgen(5, 3)
print(f"Alan: {dikdortgen.alan}")
print(f"Çevre: {dikdortgen.cevre}")

dikdortgen.genislik = 8
print(f"Yeni alan: {dikdortgen.alan}")

# =============================================================================
# 11. BUILT-IN DEKORATÖRLER
# =============================================================================

print("\n=== Built-in Dekoratörler ===")

class Matematik:
    
    @staticmethod
    def topla(a, b):
        """Static method - sınıf instance'ı gerektirmez"""
        return a + b
    
    @classmethod
    def sinif_adi(cls):
        """Class method - sınıfın kendisini alır"""
        return cls.__name__
    
    @property
    def pi(self):
        """Property - hesaplanmış değer"""
        return 3.14159

# Static method kullanımı
print(f"Static toplama: {Matematik.topla(5, 3)}")

# Class method kullanımı
print(f"Sınıf adı: {Matematik.sinif_adi()}")

# Property kullanımı
math_obj = Matematik()
print(f"Pi değeri: {math_obj.pi}")

# =============================================================================
# 12. FUNCTOOLS.LRU_CACHE - HAZIR CACHE DEKORATÖRÜ
# =============================================================================

from functools import lru_cache

@lru_cache(maxsize=128)
def optimize_fibonacci(n):
    """LRU cache ile optimize edilmiş Fibonacci"""
    if n < 2:
        return n
    return optimize_fibonacci(n-1) + optimize_fibonacci(n-2)

print("\n=== LRU Cache ===")
start = time.time()
result = optimize_fibonacci(35)
end = time.time()
print(f"Fibonacci(35) = {result}")
print(f"Süre: {end - start:.4f} saniye")

# Cache bilgisi
print(f"Cache bilgisi: {optimize_fibonacci.cache_info()}")

# =============================================================================
# 13. DEKORATÖR FABRIKASI (PARAMETRELI DEKORATÖR)
# =============================================================================

def yetki_kontrol(required_role):
    """Parametreli yetki kontrolü dekoratörü"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Normalde bu bilgi session'dan alınır
            current_user_role = "admin"  # Simüle edilmiş kullanıcı rolü
            
            if current_user_role != required_role:
                raise PermissionError(
                    f"{func.__name__} için {required_role} yetkisi gerekli, "
                    f"mevcut yetki: {current_user_role}"
                )
            
            print(f"✅ Yetki kontrolü başarılı: {required_role}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@yetki_kontrol("admin")
def kullanici_sil(kullanici_id):
    return f"Kullanıcı {kullanici_id} silindi"

@yetki_kontrol("user")
def profil_guncelle(veri):
    return f"Profil güncellendi: {veri}"

print("\n=== Parametreli Dekoratör ===")
print(kullanici_sil(123))
print(profil_guncelle({"ad": "Yeni Ad"}))

# =============================================================================
# 14. EN İYİ PRATİKLER
# =============================================================================

print("\n=== En İyi Pratikler ===")

# ✅ 1. functools.wraps kullanın
def iyi_dekorator(func):
    @functools.wraps(func)  # Bu önemli!
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# ❌ 2. functools.wraps kullanmamak
def kotu_dekorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@iyi_dekorator
def test_fonksiyon():
    """Bu bir test fonksiyonudur"""
    pass

print(f"İyi dekoratör - fonksiyon adı: {test_fonksiyon.__name__}")
print(f"İyi dekoratör - docstring: {test_fonksiyon.__doc__}")

# ✅ 3. Dekoratörleri modüler yapın
# ✅ 4. Hata durumlarını ele alın
# ✅ 5. Performans etkilerini göz önünde bulundurun
# ✅ 6. Dokümantasyon ekleyin

print("\n✅ Dekoratörlerin temelleri öğrenildi!")
print("✅ Built-in dekoratörler öğrenildi!")
print("✅ Parametreli dekoratörler öğrenildi!")
print("✅ En iyi pratikler öğrenildi!")