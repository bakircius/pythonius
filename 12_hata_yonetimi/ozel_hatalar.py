"""
Python Özel Hatalar (Custom Exceptions)

Bu dosya Python'da özel exception sınıfları oluşturma, hata zinciri,
exception context ve gelişmiş hata yönetimi tekniklerini kapsar.
"""

import traceback
import sys
import logging
from typing import Optional, Any, Dict, List
from datetime import datetime

# =============================================================================
# 1. TEMEL ÖZEL EXCEPTION SINIFI
# =============================================================================

print("=== Özel Exception Sınıfları ===")

class OzelHata(Exception):
    """Temel özel hata sınıfı"""
    pass

class VeriHatasi(OzelHata):
    """Veri ile ilgili hatalar"""
    pass

class IslemHatasi(OzelHata):
    """İşlem ile ilgili hatalar"""
    pass

def temel_ozel_hata_ornegi():
    """Temel özel hata kullanımı"""
    
    def veri_kontrol(veri):
        if not isinstance(veri, (int, float)):
            raise VeriHatasi(f"Veri sayı olmalı, aldı: {type(veri).__name__}")
        
        if veri < 0:
            raise VeriHatasi(f"Veri pozitif olmalı, aldı: {veri}")
        
        return veri ** 0.5
    
    test_verileri = [16, -4, "abc", None]
    
    for veri in test_verileri:
        try:
            sonuc = veri_kontrol(veri)
            print(f"✅ {veri} -> {sonuc:.2f}")
        except VeriHatasi as e:
            print(f"❌ VeriHatasi: {e}")

temel_ozel_hata_ornegi()

# =============================================================================
# 2. GELİŞMİŞ ÖZEL EXCEPTION SINIFI
# =============================================================================

print("\n=== Gelişmiş Özel Exception ===")

class GelismisHata(Exception):
    """Gelişmiş özel hata sınıfı"""
    
    def __init__(self, message: str, 
                 error_code: str = None,
                 details: Dict[str, Any] = None,
                 suggestions: List[str] = None):
        super().__init__(message)
        self.message = message
        self.error_code = error_code or "GENERIC_ERROR"
        self.details = details or {}
        self.suggestions = suggestions or []
        self.timestamp = datetime.now()
    
    def __str__(self):
        return f"[{self.error_code}] {self.message}"
    
    def __repr__(self):
        return (f"{self.__class__.__name__}("
                f"message='{self.message}', "
                f"error_code='{self.error_code}', "
                f"timestamp='{self.timestamp}')")
    
    def to_dict(self):
        """Hata bilgilerini dictionary olarak döndürür"""
        return {
            'error_type': self.__class__.__name__,
            'message': self.message,
            'error_code': self.error_code,
            'details': self.details,
            'suggestions': self.suggestions,
            'timestamp': self.timestamp.isoformat()
        }
    
    def print_detailed(self):
        """Detaylı hata bilgilerini yazdırır"""
        print(f"🚨 Hata Türü: {self.__class__.__name__}")
        print(f"📋 Mesaj: {self.message}")
        print(f"🔢 Kod: {self.error_code}")
        print(f"⏰ Zaman: {self.timestamp}")
        
        if self.details:
            print("📊 Detaylar:")
            for key, value in self.details.items():
                print(f"   {key}: {value}")
        
        if self.suggestions:
            print("💡 Öneriler:")
            for i, suggestion in enumerate(self.suggestions, 1):
                print(f"   {i}. {suggestion}")

# Spesifik hata türleri
class KullaniciHatasi(GelismisHata):
    """Kullanıcı girişi hatası"""
    pass

class SistemHatasi(GelismisHata):
    """Sistem hatası"""
    pass

class VeriTabaniHatasi(GelismisHata):
    """Veritabanı hatası"""
    pass

def gelismis_hata_ornegi():
    """Gelişmiş hata kullanımı"""
    
    def kullanici_dogrula(kullanici_id, yas):
        if not isinstance(kullanici_id, int):
            raise KullaniciHatasi(
                "Kullanıcı ID integer olmalı",
                error_code="INVALID_USER_ID_TYPE",
                details={
                    "received_type": type(kullanici_id).__name__,
                    "received_value": kullanici_id,
                    "expected_type": "int"
                },
                suggestions=[
                    "Kullanıcı ID'yi integer olarak gönderin",
                    "str(kullanici_id) -> int(kullanici_id) dönüşümü yapın"
                ]
            )
        
        if kullanici_id <= 0:
            raise KullaniciHatasi(
                "Kullanıcı ID pozitif olmalı",
                error_code="INVALID_USER_ID_VALUE",
                details={
                    "received_value": kullanici_id,
                    "min_value": 1
                },
                suggestions=[
                    "Geçerli bir kullanıcı ID'si kullanın",
                    "Kullanıcı kaydının varlığını kontrol edin"
                ]
            )
        
        if yas < 0 or yas > 150:
            raise KullaniciHatasi(
                "Yaş geçerli aralıkta değil",
                error_code="INVALID_AGE_RANGE",
                details={
                    "received_age": yas,
                    "valid_range": "0-150",
                    "user_id": kullanici_id
                },
                suggestions=[
                    "Yaşı 0-150 arasında girin",
                    "Doğum tarihinden yaş hesaplama işlemini kontrol edin"
                ]
            )
        
        return True
    
    # Test senaryoları
    test_kullanicilari = [
        (123, 25),      # Geçerli
        ("abc", 30),    # ID hatalı
        (-5, 25),       # ID negatif
        (456, -10),     # Yaş negatif
        (789, 200)      # Yaş çok büyük
    ]
    
    for kullanici_id, yas in test_kullanicilari:
        try:
            kullanici_dogrula(kullanici_id, yas)
            print(f"✅ Kullanıcı geçerli: ID={kullanici_id}, Yaş={yas}")
        except GelismisHata as e:
            print(f"\n❌ Hata oluştu:")
            e.print_detailed()
            print()

gelismis_hata_ornegi()

# =============================================================================
# 3. HATA ZİNCİRİ (Exception Chaining)
# =============================================================================

print("\n=== Hata Zinciri ===")

class VeriTabaniConnectionHatasi(Exception):
    """Veritabanı bağlantı hatası"""
    pass

class UserServiceHatasi(Exception):
    """User service hatası"""
    pass

def hata_zinciri_ornegi():
    """Exception chaining örnekleri"""
    
    def veritabani_baglan():
        """Simulated database connection"""
        raise ConnectionError("Veritabanı sunucusuna bağlanılamıyor")
    
    def kullanici_getir(user_id):
        """Kullanıcı bilgilerini getir"""
        try:
            veritabani_baglan()
            # Burada normalde veritabanı sorgusu olurdu
            return {"id": user_id, "name": "Kullanıcı"}
        except ConnectionError as e:
            # Orijinal hatayı koruyarak yeni hata fırlat
            raise VeriTabaniConnectionHatasi(
                f"Kullanıcı {user_id} getirilemedi"
            ) from e
    
    def kullanici_profil_getir(user_id):
        """Kullanıcı profil servisi"""
        try:
            kullanici = kullanici_getir(user_id)
            return kullanici
        except VeriTabaniConnectionHatasi as e:
            # İkinci seviye hata zinciri
            raise UserServiceHatasi(
                f"Profil servisi hatası: User ID {user_id}"
            ) from e
    
    # Test
    try:
        profil = kullanici_profil_getir(123)
    except UserServiceHatasi as e:
        print("🔗 Hata Zinciri Analizi:")
        print(f"Ana Hata: {e}")
        print(f"Sebep: {e.__cause__}")
        print(f"Sebep Türü: {type(e.__cause__).__name__}")
        
        if e.__cause__.__cause__:
            print(f"Kök Sebep: {e.__cause__.__cause__}")
            print(f"Kök Sebep Türü: {type(e.__cause__.__cause__).__name__}")
        
        print("\n📋 Tam Traceback:")
        traceback.print_exc()

hata_zinciri_ornegi()

# =============================================================================
# 4. CONTEXT MANAGER İLE HATALAR
# =============================================================================

print("\n=== Context Manager ile Hatalar ===")

class HataYoneticisi:
    """Hata yönetimi için context manager"""
    
    def __init__(self, hata_turu=None, log_dosyasi=None):
        self.hata_turu = hata_turu
        self.log_dosyasi = log_dosyasi
        self.baslangic_zamani = None
        self.hatalar = []
    
    def __enter__(self):
        self.baslangic_zamani = datetime.now()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback_obj):
        bitis_zamani = datetime.now()
        sure = bitis_zamani - self.baslangic_zamani
        
        if exc_type is not None:
            hata_bilgisi = {
                'hata_turu': exc_type.__name__,
                'mesaj': str(exc_value),
                'zaman': bitis_zamani.isoformat(),
                'sure': sure.total_seconds()
            }
            self.hatalar.append(hata_bilgisi)
            
            print(f"🚨 Hata Yakalandı:")
            print(f"   Tür: {exc_type.__name__}")
            print(f"   Mesaj: {exc_value}")
            print(f"   Süre: {sure.total_seconds():.3f} saniye")
            
            if self.log_dosyasi:
                self._log_hata(hata_bilgisi)
            
            # Belirli hata türlerini bastır
            if self.hata_turu and isinstance(exc_value, self.hata_turu):
                print("   ✅ Hata bastırıldı")
                return True  # Exception'ı bastır
        
        return False  # Exception'ı yeniden fırlat
    
    def _log_hata(self, hata_bilgisi):
        """Hatayı dosyaya logla"""
        try:
            with open(self.log_dosyasi, "a", encoding="utf-8") as f:
                f.write(f"{datetime.now()}: {hata_bilgisi}\n")
        except:
            pass  # Log hatalarını göz ardı et

def context_manager_hata_ornegi():
    """Context manager ile hata yönetimi"""
    
    # Hata bastırma
    print("--- Hata Bastırma ---")
    with HataYoneticisi(hata_turu=ValueError):
        print("Hatalı işlem başlıyor...")
        int("abc")  # ValueError oluştur
        print("Bu satır çalışmayacak")
    
    print("Program devam ediyor...\n")
    
    # Hata loglama
    print("--- Hata Loglama ---")
    with HataYoneticisi(log_dosyasi="hatalar.log") as hm:
        print("Loglu işlem başlıyor...")
        try:
            result = 10 / 0  # ZeroDivisionError
        except:
            pass  # Hata context manager'a yakalanacak
    
    print("Hata loglandı.\n")
    
    # Multiple hatalar
    print("--- Multiple Hatalar ---")
    with HataYoneticisi() as hm:
        for i in range(3):
            try:
                if i == 0:
                    int("abc")
                elif i == 1:
                    [][5]
                else:
                    {"a": 1}["b"]
            except:
                pass
    
    print(f"Toplam hata sayısı: {len(hm.hatalar)}")

context_manager_hata_ornegi()

# =============================================================================
# 5. HATA DOĞRULAMA VE VALIDATION
# =============================================================================

print("\n=== Hata Doğrulama ===")

class DogrulamaHatasi(Exception):
    """Doğrulama hatası"""
    
    def __init__(self, field: str, value: Any, rule: str, message: str = None):
        self.field = field
        self.value = value
        self.rule = rule
        self.message = message or f"Doğrulama hatası: {field}"
        super().__init__(self.message)
    
    def __str__(self):
        return f"{self.message} (Alan: {self.field}, Değer: {self.value}, Kural: {self.rule})"

class Dogrulayici:
    """Veri doğrulama sınıfı"""
    
    @staticmethod
    def zorunlu(value, field_name):
        if value is None or value == "":
            raise DogrulamaHatasi(
                field_name, value, "required",
                f"{field_name} zorunlu alan"
            )
    
    @staticmethod
    def tip_kontrol(value, expected_type, field_name):
        if not isinstance(value, expected_type):
            raise DogrulamaHatasi(
                field_name, value, f"type:{expected_type.__name__}",
                f"{field_name} {expected_type.__name__} tipinde olmalı"
            )
    
    @staticmethod
    def uzunluk_kontrol(value, min_len=None, max_len=None, field_name="field"):
        length = len(value) if value else 0
        
        if min_len and length < min_len:
            raise DogrulamaHatasi(
                field_name, value, f"min_length:{min_len}",
                f"{field_name} en az {min_len} karakter olmalı"
            )
        
        if max_len and length > max_len:
            raise DogrulamaHatasi(
                field_name, value, f"max_length:{max_len}",
                f"{field_name} en fazla {max_len} karakter olmalı"
            )
    
    @staticmethod
    def aralik_kontrol(value, min_val=None, max_val=None, field_name="field"):
        if min_val is not None and value < min_val:
            raise DogrulamaHatasi(
                field_name, value, f"min_value:{min_val}",
                f"{field_name} en az {min_val} olmalı"
            )
        
        if max_val is not None and value > max_val:
            raise DogrulamaHatasi(
                field_name, value, f"max_value:{max_val}",
                f"{field_name} en fazla {max_val} olmalı"
            )

def kullanici_dogrula(veri):
    """Kullanıcı verilerini doğrula"""
    hatalar = []
    
    # Ad doğrulama
    try:
        Dogrulayici.zorunlu(veri.get("ad"), "ad")
        Dogrulayici.tip_kontrol(veri.get("ad"), str, "ad")
        Dogrulayici.uzunluk_kontrol(veri.get("ad"), min_len=2, max_len=50, field_name="ad")
    except DogrulamaHatasi as e:
        hatalar.append(e)
    
    # Yaş doğrulama
    try:
        Dogrulayici.zorunlu(veri.get("yas"), "yas")
        Dogrulayici.tip_kontrol(veri.get("yas"), int, "yas")
        Dogrulayici.aralik_kontrol(veri.get("yas"), min_val=0, max_val=150, field_name="yas")
    except DogrulamaHatasi as e:
        hatalar.append(e)
    
    # Email doğrulama
    try:
        email = veri.get("email")
        if email:  # Opsiyonel alan
            Dogrulayici.tip_kontrol(email, str, "email")
            if "@" not in email:
                raise DogrulamaHatasi("email", email, "format", "Geçerli email formatı değil")
    except DogrulamaHatasi as e:
        hatalar.append(e)
    
    if hatalar:
        # Multiple validation errors
        hata_mesajlari = [str(hata) for hata in hatalar]
        raise DogrulamaHatasi(
            "multiple", veri, "validation",
            f"Multiple doğrulama hatası: {'; '.join(hata_mesajlari)}"
        )
    
    return True

def dogrulama_ornegi():
    """Doğrulama örneği"""
    
    test_kullanicilari = [
        {"ad": "Ahmet", "yas": 30, "email": "ahmet@example.com"},  # Geçerli
        {"ad": "", "yas": 25, "email": "test@test.com"},           # Ad eksik
        {"ad": "Ayşe", "yas": -5, "email": "ayse@example.com"},   # Yaş negatif
        {"ad": "Mehmet", "yas": 35, "email": "invalid-email"},    # Email hatalı
        {"yas": 40}                                                # Ad eksik
    ]
    
    for i, kullanici in enumerate(test_kullanicilari, 1):
        try:
            kullanici_dogrula(kullanici)
            print(f"✅ Kullanıcı {i}: Geçerli")
        except DogrulamaHatasi as e:
            print(f"❌ Kullanıcı {i}: {e}")

dogrulama_ornegi()

# =============================================================================
# 6. HATA RAPORLAMA VE MONITORING
# =============================================================================

print("\n=== Hata Raporlama ===")

class HataRaporu:
    """Hata raporlama sınıfı"""
    
    def __init__(self):
        self.hatalar = []
    
    def hata_ekle(self, exception, context=None):
        """Hata ekle"""
        hata_bilgisi = {
            'timestamp': datetime.now().isoformat(),
            'exception_type': type(exception).__name__,
            'message': str(exception),
            'context': context or {},
            'traceback': traceback.format_exc(),
            'system_info': {
                'python_version': sys.version,
                'platform': sys.platform
            }
        }
        self.hatalar.append(hata_bilgisi)
    
    def rapor_olustur(self):
        """Detaylı rapor oluştur"""
        if not self.hatalar:
            return "Hata bulunmadı."
        
        rapor = f"🚨 HATA RAPORU ({len(self.hatalar)} hata)\n"
        rapor += "=" * 50 + "\n"
        
        # Hata türü istatistikleri
        hata_turleri = {}
        for hata in self.hatalar:
            hata_turu = hata['exception_type']
            hata_turleri[hata_turu] = hata_turleri.get(hata_turu, 0) + 1
        
        rapor += "📊 Hata Türü İstatistikleri:\n"
        for hata_turu, sayi in sorted(hata_turleri.items()):
            rapor += f"   {hata_turu}: {sayi} adet\n"
        
        rapor += "\n📋 Detaylı Hatalar:\n"
        for i, hata in enumerate(self.hatalar, 1):
            rapor += f"\n--- Hata {i} ---\n"
            rapor += f"Zaman: {hata['timestamp']}\n"
            rapor += f"Tür: {hata['exception_type']}\n"
            rapor += f"Mesaj: {hata['message']}\n"
            
            if hata['context']:
                rapor += f"Kontekst: {hata['context']}\n"
        
        return rapor
    
    def temizle(self):
        """Hata listesini temizle"""
        self.hatalar.clear()

def hata_raporlama_ornegi():
    """Hata raporlama örneği"""
    
    rapor = HataRaporu()
    
    # Çeşitli hatalar oluştur
    hata_senaryolari = [
        (lambda: int("abc"), {"operation": "string_to_int", "input": "abc"}),
        (lambda: [][5], {"operation": "list_access", "index": 5}),
        (lambda: 10/0, {"operation": "division", "divisor": 0}),
        (lambda: {"a": 1}["b"], {"operation": "dict_access", "key": "b"}),
    ]
    
    for islem, context in hata_senaryolari:
        try:
            islem()
        except Exception as e:
            rapor.hata_ekle(e, context)
    
    print(rapor.rapor_olustur())

hata_raporlama_ornegi()

# =============================================================================
# 7. ÖZEL HATA BEST PRACTICES
# =============================================================================

print("\n=== Özel Hata Best Practices ===")

def ozel_hata_best_practices():
    """Özel hata sınıfları için best practices"""
    
    print("📋 Özel Hata Sınıfları Best Practices:")
    print("1. Exception'dan kalıt alın (BaseException değil)")
    print("2. Anlamlı hata isimleri kullanın (XxxError, XxxException)")
    print("3. Hata hiyerarşisi oluşturun (genel -> spesifik)")
    print("4. Hata mesajlarını açık ve yardımcı yapın")
    print("5. Hata kodları kullanın (error_code)")
    print("6. Ek bilgileri attributes olarak saklayın")
    print("7. __str__ ve __repr__ metodlarını override edin")
    print("8. Exception chaining kullanın (raise ... from)")
    print("9. Docstring yazın")
    print("10. Hata türlerini modüllere gruplandırın")

# Örnek best practice implementasyonu
class APIHatasi(Exception):
    """API hataları için base sınıf
    
    Bu sınıf tüm API hatalarının base'idir.
    Standart hata bilgilerini ve format metodlarını sağlar.
    """
    
    def __init__(self, message, status_code=None, error_code=None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.error_code = error_code
        self.timestamp = datetime.now()

class AuthenticationError(APIHatasi):
    """Kimlik doğrulama hatası"""
    
    def __init__(self, message="Kimlik doğrulama başarısız"):
        super().__init__(message, status_code=401, error_code="AUTH_FAILED")

class AuthorizationError(APIHatasi):
    """Yetkilendirme hatası"""
    
    def __init__(self, message="Yetkisiz erişim"):
        super().__init__(message, status_code=403, error_code="UNAUTHORIZED")

class RateLimitError(APIHatasi):
    """Rate limit hatası"""
    
    def __init__(self, message="Rate limit aşıldı", retry_after=None):
        super().__init__(message, status_code=429, error_code="RATE_LIMIT")
        self.retry_after = retry_after

print(f"\n✅ Özel hata sınıfları öğrenildi!")

ozel_hata_best_practices()

print("\n💡 Özel Hatalar İpuçları:")
print("✅ Kendi exception hiyerarşinizi oluşturun")
print("✅ Hata mesajlarını kullanıcı dostu yapın")
print("✅ Exception chaining ile hata geçmişini koruyun")
print("✅ Context manager'lar ile hata yönetimini otomatikleştirin")
print("✅ Validation hatalarını spesifik yapın")
print("✅ Hata raporlama sistemleri kurun")
print("✅ Error codes ile kategorization yapın")

print("\n✅ Python özel hatalar öğrenildi!")
print("✅ Exception chaining öğrenildi!")
print("✅ Hata doğrulama teknikleri öğrenildi!")
print("✅ Hata raporlama sistemleri öğrenildi!")