"""
Python Encapsulation ve Property Decorator'ları
Data Hiding, Access Control, Property Management - Comprehensive Guide

Bu dosyada Python'da encapsulation prensipleri, veri gizleme teknikleri,
property decorator'ları ve access control mekanizmaları detaylı incelenecek.
"""

import datetime
import re
from typing import Optional, List
import hashlib

# =============================================================================
# 1. ENCAPSULATION TEMELLERİ
# =============================================================================

print("=== Encapsulation Temelleri ===")

class TemelSinif:
    """Encapsulation kavramlarını gösteren temel sınıf"""
    
    def __init__(self, isim):
        # Public attribute (herkese açık)
        self.public_isim = isim
        
        # Protected attribute (alt sınıflara açık) - tek underscore
        self._protected_bilgi = "Bu protected bilgidir"
        
        # Private attribute (sadece bu sınıfa özel) - çift underscore
        self.__private_bilgi = "Bu private bilgidir"
    
    # Public method
    def public_metod(self):
        """Herkese açık metod"""
        return f"Public metod çalıştı: {self.public_isim}"
    
    # Protected method
    def _protected_metod(self):
        """Protected metod - alt sınıflarda kullanılabilir"""
        return f"Protected metod: {self._protected_bilgi}"
    
    # Private method
    def __private_metod(self):
        """Private metod - sadece bu sınıfta kullanılabilir"""
        return f"Private metod: {self.__private_bilgi}"
    
    def private_bilgiye_eris(self):
        """Private bilgiye erişim için public interface"""
        return self.__private_metod()

# Encapsulation kullanımı
print("Encapsulation örnekleri:")
obj = TemelSinif("Test Objesi")

# Public erişim
print(f"Public attribute: {obj.public_isim}")
print(f"Public method: {obj.public_metod()}")

# Protected erişim (convention, zorlanmaz)
print(f"Protected attribute: {obj._protected_bilgi}")
print(f"Protected method: {obj._protected_metod()}")

# Private erişim - doğrudan erişilemez
try:
    print(obj.__private_bilgi)  # AttributeError
except AttributeError as e:
    print(f"Private attribute'a doğrudan erişilemez: {e}")

# Private bilgiye public interface ile erişim
print(f"Private bilgiye dolaylı erişim: {obj.private_bilgiye_eris()}")

# Name mangling ile private erişim (sadece debug için)
print(f"Name mangling ile erişim: {obj._TemelSinif__private_bilgi}")

# =============================================================================
# 2. PROPERTY DECORATOR TEMELLERİ
# =============================================================================

print("\n=== Property Decorator Temelleri ===")

class Yas:
    """Yaş kontrolü için property örneği"""
    
    def __init__(self, dogum_yili):
        self._dogum_yili = dogum_yili
    
    @property
    def yas(self):
        """Yaş getter - hesaplanmış özellik"""
        current_year = datetime.datetime.now().year
        return current_year - self._dogum_yili
    
    @property
    def dogum_yili(self):
        """Doğum yılı getter"""
        return self._dogum_yili
    
    @dogum_yili.setter
    def dogum_yili(self, yil):
        """Doğum yılı setter - validasyon ile"""
        current_year = datetime.datetime.now().year
        
        if not isinstance(yil, int):
            raise TypeError("Doğum yılı integer olmalıdır")
        
        if yil < 1900 or yil > current_year:
            raise ValueError(f"Doğum yılı 1900-{current_year} arasında olmalıdır")
        
        self._dogum_yili = yil
        print(f"Doğum yılı güncellendi: {yil}")
    
    def dogum_gunu_gecti_mi(self):
        """Bu yıl doğum günü geçti mi kontrol et"""
        # Basit örnek - sadece yıl karşılaştırması
        return True  # Gerçek implementasyon ay/gün kontrolü gerektirir

# Property kullanımı
print("Property decorator örnekleri:")
kisi = Yas(1990)

print(f"Doğum yılı: {kisi.dogum_yili}")
print(f"Yaş: {kisi.yas}")  # Hesaplanmış özellik

# Setter kullanımı
kisi.dogum_yili = 1985
print(f"Yeni yaş: {kisi.yas}")

# Hatalı değer
try:
    kisi.dogum_yili = 2030  # Gelecek yıl
except ValueError as e:
    print(f"Validasyon hatası: {e}")

# =============================================================================
# 3. GELİŞMİŞ PROPERTY KULLANIMI
# =============================================================================

print("\n=== Gelişmiş Property Kullanımı ===")

class BankHesabi:
    """Gelişmiş property örnekleri ile banka hesabı"""
    
    def __init__(self, hesap_no, sahip_adi, baslangic_bakiye=0):
        self.hesap_no = hesap_no
        self.sahip_adi = sahip_adi
        self._bakiye = 0  # Private bakiye
        self._islem_gecmisi = []
        self._hesap_durumu = "Aktif"
        self._minimum_bakiye = 0
        
        # Başlangıç bakiyesi setter ile set et (validasyon için)
        if baslangic_bakiye > 0:
            self.bakiye = baslangic_bakiye
    
    @property
    def bakiye(self):
        """Bakiye getter - okunabilir format"""
        return self._bakiye
    
    @bakiye.setter
    def bakiye(self, miktar):
        """Bakiye setter - validasyon ve logging ile"""
        if not isinstance(miktar, (int, float)):
            raise TypeError("Bakiye sayısal değer olmalıdır")
        
        if miktar < 0:
            raise ValueError("Bakiye negatif olamaz")
        
        eski_bakiye = self._bakiye
        self._bakiye = float(miktar)
        
        # İşlem geçmişine ekle
        self._islem_gecmisi.append({
            'tip': 'Bakiye Güncellemesi',
            'eski_bakiye': eski_bakiye,
            'yeni_bakiye': self._bakiye,
            'tarih': datetime.datetime.now()
        })
        
        print(f"Bakiye güncellendi: {eski_bakiye} -> {self._bakiye} TL")
    
    @property
    def hesap_durumu(self):
        """Hesap durumu getter"""
        return self._hesap_durumu
    
    @hesap_durumu.setter
    def hesap_durumu(self, durum):
        """Hesap durumu setter - sadece geçerli durumlar"""
        gecerli_durumlar = ["Aktif", "Pasif", "Blokeli", "Kapalı"]
        
        if durum not in gecerli_durumlar:
            raise ValueError(f"Geçersiz hesap durumu. Geçerli durumlar: {gecerli_durumlar}")
        
        eski_durum = self._hesap_durumu
        self._hesap_durumu = durum
        
        print(f"Hesap durumu değişti: {eski_durum} -> {durum}")
        
        # Durum değişikliğini logla
        self._islem_gecmisi.append({
            'tip': 'Durum Değişikliği',
            'eski_durum': eski_durum,
            'yeni_durum': durum,
            'tarih': datetime.datetime.now()
        })
    
    @property
    def minimum_bakiye(self):
        """Minimum bakiye getter"""
        return self._minimum_bakiye
    
    @minimum_bakiye.setter
    def minimum_bakiye(self, miktar):
        """Minimum bakiye setter"""
        if miktar < 0:
            raise ValueError("Minimum bakiye negatif olamaz")
        
        self._minimum_bakiye = miktar
        print(f"Minimum bakiye ayarlandı: {miktar} TL")
    
    @property
    def kullanilabilir_bakiye(self):
        """Kullanılabilir bakiye - computed property"""
        return max(0, self._bakiye - self._minimum_bakiye)
    
    @property
    def islem_sayisi(self):
        """Toplam işlem sayısı - computed property"""
        return len(self._islem_gecmisi)
    
    def para_cek(self, miktar):
        """Para çekme - property kullanımı ile"""
        if self.hesap_durumu != "Aktif":
            raise ValueError(f"Hesap {self.hesap_durumu} durumunda. Para çekilemez.")
        
        if miktar > self.kullanilabilir_bakiye:
            raise ValueError(f"Yetersiz bakiye. Kullanılabilir: {self.kullanilabilir_bakiye} TL")
        
        self.bakiye = self._bakiye - miktar  # Setter'ı kullan
        return True
    
    def para_yatir(self, miktar):
        """Para yatırma"""
        if self.hesap_durumu not in ["Aktif", "Pasif"]:
            raise ValueError(f"Hesap {self.hesap_durumu} durumunda. Para yatırılamaz.")
        
        if miktar <= 0:
            raise ValueError("Yatırılacak miktar pozitif olmalıdır")
        
        self.bakiye = self._bakiye + miktar  # Setter'ı kullan
        return True

# Gelişmiş property kullanımı
print("Gelişmiş property örnekleri:")
hesap = BankHesabi("12345", "Ali Veli", 1000)

print(f"Başlangıç bakiye: {hesap.bakiye} TL")
print(f"Hesap durumu: {hesap.hesap_durumu}")
print(f"Kullanılabilir bakiye: {hesap.kullanilabilir_bakiye} TL")

# Minimum bakiye ayarla
hesap.minimum_bakiye = 500
print(f"Yeni kullanılabilir bakiye: {hesap.kullanilabilir_bakiye} TL")

# Para işlemleri
hesap.para_yatir(500)
hesap.para_cek(200)

print(f"Son durum - Bakiye: {hesap.bakiye} TL, İşlem sayısı: {hesap.islem_sayisi}")

# =============================================================================
# 4. DATA VALIDATION VE SECURITY
# =============================================================================

print("\n=== Data Validation ve Security ===")

class KullaniciHesabi:
    """Güvenli kullanıcı hesabı - data validation örneği"""
    
    def __init__(self, kullanici_adi, email, sifre):
        self._kullanici_adi = None
        self._email = None
        self._sifre_hash = None
        self._oturum_acik = False
        self._yanlis_sifre_sayisi = 0
        self._hesap_kilitli = False
        self._son_giris = None
        
        # Setter'ları kullanarak validasyon yap
        self.kullanici_adi = kullanici_adi
        self.email = email
        self.sifre = sifre
    
    @property
    def kullanici_adi(self):
        """Kullanıcı adı getter"""
        return self._kullanici_adi
    
    @kullanici_adi.setter
    def kullanici_adi(self, adi):
        """Kullanıcı adı setter - validasyon ile"""
        if not isinstance(adi, str):
            raise TypeError("Kullanıcı adı string olmalıdır")
        
        # Boşluk kontrolü
        adi = adi.strip()
        if not adi:
            raise ValueError("Kullanıcı adı boş olamaz")
        
        # Uzunluk kontrolü
        if len(adi) < 3 or len(adi) > 20:
            raise ValueError("Kullanıcı adı 3-20 karakter arasında olmalıdır")
        
        # Geçerli karakterler kontrolü
        if not re.match(r'^[a-zA-Z0-9_]+$', adi):
            raise ValueError("Kullanıcı adı sadece harf, rakam ve _ içerebilir")
        
        self._kullanici_adi = adi
        print(f"Kullanıcı adı ayarlandı: {adi}")
    
    @property
    def email(self):
        """Email getter"""
        return self._email
    
    @email.setter
    def email(self, email_adresi):
        """Email setter - validasyon ile"""
        if not isinstance(email_adresi, str):
            raise TypeError("Email string olmalıdır")
        
        # Email format kontrolü
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email_adresi):
            raise ValueError("Geçersiz email formatı")
        
        self._email = email_adresi.lower()
        print(f"Email ayarlandı: {self._email}")
    
    @property
    def sifre(self):
        """Şifre getter - sadece hash durumunu döner"""
        return "***PROTECTED***"
    
    @sifre.setter
    def sifre(self, yeni_sifre):
        """Şifre setter - güçlü şifre validasyonu"""
        if not isinstance(yeni_sifre, str):
            raise TypeError("Şifre string olmalıdır")
        
        # Şifre uzunluğu
        if len(yeni_sifre) < 8:
            raise ValueError("Şifre en az 8 karakter olmalıdır")
        
        # Şifre güçlülük kontrolü
        kontroller = [
            (r'[a-z]', "küçük harf"),
            (r'[A-Z]', "büyük harf"), 
            (r'[0-9]', "rakam"),
            (r'[!@#$%^&*(),.?":{}|<>]', "özel karakter")
        ]
        
        eksik_kriterler = []
        for pattern, aciklama in kontroller:
            if not re.search(pattern, yeni_sifre):
                eksik_kriterler.append(aciklama)
        
        if eksik_kriterler:
            raise ValueError(f"Şifre şu kriterleri karşılamalı: {', '.join(eksik_kriterler)}")
        
        # Şifreyi hash'le ve sakla
        self._sifre_hash = hashlib.sha256(yeni_sifre.encode()).hexdigest()
        print("Şifre güvenli şekilde ayarlandı")
    
    @property
    def hesap_durumu(self):
        """Hesap durumu bilgisi"""
        if self._hesap_kilitli:
            return "Kilitli"
        elif self._oturum_acik:
            return "Oturum Açık"
        else:
            return "Oturum Kapalı"
    
    @property
    def son_giris_bilgisi(self):
        """Son giriş bilgisi"""
        if self._son_giris:
            return self._son_giris.strftime("%Y-%m-%d %H:%M:%S")
        return "Hiç giriş yapılmadı"
    
    def sifre_dogrula(self, sifre):
        """Şifre doğrulama"""
        if self._hesap_kilitli:
            raise ValueError("Hesap kilitli. Yönetici ile iletişime geçin.")
        
        sifre_hash = hashlib.sha256(sifre.encode()).hexdigest()
        
        if sifre_hash == self._sifre_hash:
            self._yanlis_sifre_sayisi = 0
            return True
        else:
            self._yanlis_sifre_sayisi += 1
            print(f"Yanlış şifre! Deneme sayısı: {self._yanlis_sifre_sayisi}")
            
            if self._yanlis_sifre_sayisi >= 3:
                self._hesap_kilitli = True
                print("Hesap 3 yanlış deneme sonucu kilitlendi!")
            
            return False
    
    def oturum_ac(self, sifre):
        """Oturum açma"""
        if self.sifre_dogrula(sifre):
            self._oturum_acik = True
            self._son_giris = datetime.datetime.now()
            print(f"Oturum açıldı. Hoş geldin {self._kullanici_adi}!")
            return True
        return False
    
    def oturum_kapat(self):
        """Oturum kapatma"""
        self._oturum_acik = False
        print("Oturum kapatıldı. Güle güle!")
    
    def hesap_bilgileri(self):
        """Hesap bilgilerini göster"""
        print(f"\n=== Hesap Bilgileri ===")
        print(f"Kullanıcı Adı: {self._kullanici_adi}")
        print(f"Email: {self._email}")
        print(f"Hesap Durumu: {self.hesap_durumu}")
        print(f"Son Giriş: {self.son_giris_bilgisi}")
        print(f"Yanlış Şifre Sayısı: {self._yanlis_sifre_sayisi}")

# Data validation kullanımı
print("Data validation örnekleri:")

try:
    kullanici = KullaniciHesabi("john_doe", "john@example.com", "SecurePass123!")
    kullanici.hesap_bilgileri()
    
    # Oturum açma denemeleri
    kullanici.oturum_ac("wrongpass")  # Yanlış şifre
    kullanici.oturum_ac("SecurePass123!")  # Doğru şifre
    
    kullanici.hesap_bilgileri()
    kullanici.oturum_kapat()
    
except (ValueError, TypeError) as e:
    print(f"Hata: {e}")

# Hatalı veri girişi örnekleri
print("\nHatalı veri girişi örnekleri:")

try:
    # Zayıf şifre
    kullanici2 = KullaniciHesabi("test", "test@test.com", "weak")
except ValueError as e:
    print(f"Zayıf şifre hatası: {e}")

try:
    # Geçersiz email
    kullanici3 = KullaniciHesabi("test2", "invalid-email", "StrongPass123!")
except ValueError as e:
    print(f"Email hatası: {e}")

# =============================================================================
# 5. PROPERTY İLE COMPUTED ATTRIBUTES
# =============================================================================

print("\n=== Computed Attributes ===")

class Dikdortgen:
    """Computed properties örneği"""
    
    def __init__(self, genislik, yukseklik):
        self._genislik = 0
        self._yukseklik = 0
        
        # Setter'ları kullan
        self.genislik = genislik
        self.yukseklik = yukseklik
    
    @property
    def genislik(self):
        """Genişlik getter"""
        return self._genislik
    
    @genislik.setter
    def genislik(self, deger):
        """Genişlik setter - validasyon ile"""
        if deger <= 0:
            raise ValueError("Genişlik pozitif olmalıdır")
        self._genislik = deger
    
    @property
    def yukseklik(self):
        """Yükseklik getter"""
        return self._yukseklik
    
    @yukseklik.setter
    def yukseklik(self, deger):
        """Yükseklik setter - validasyon ile"""
        if deger <= 0:
            raise ValueError("Yükseklik pozitif olmalıdır")
        self._yukseklik = deger
    
    @property
    def alan(self):
        """Alan - computed property"""
        return self._genislik * self._yukseklik
    
    @property
    def cevre(self):
        """Çevre - computed property"""
        return 2 * (self._genislik + self._yukseklik)
    
    @property
    def kosegen(self):
        """Köşegen uzunluğu - computed property"""
        return (self._genislik ** 2 + self._yukseklik ** 2) ** 0.5
    
    @property
    def kare_mi(self):
        """Kare mi kontrol et - computed property"""
        return self._genislik == self._yukseklik
    
    @property
    def en_boy_orani(self):
        """En-boy oranı - computed property"""
        return self._genislik / self._yukseklik
    
    def olcek(self, carpan):
        """Dikdörtgeni ölçekle"""
        self.genislik = self._genislik * carpan
        self.yukseklik = self._yukseklik * carpan
        print(f"Dikdörtgen {carpan}x ölçeklendi")
    
    def bilgileri_goster(self):
        """Dikdörtgen bilgilerini göster"""
        print(f"\n=== Dikdörtgen Bilgileri ===")
        print(f"Genişlik: {self.genislik}")
        print(f"Yükseklik: {self.yukseklik}")
        print(f"Alan: {self.alan}")
        print(f"Çevre: {self.cevre}")
        print(f"Köşegen: {self.kosegen:.2f}")
        print(f"Kare mi: {'Evet' if self.kare_mi else 'Hayır'}")
        print(f"En-Boy Oranı: {self.en_boy_orani:.2f}")

# Computed attributes kullanımı
print("Computed attributes örnekleri:")
dikdortgen = Dikdortgen(10, 5)
dikdortgen.bilgileri_goster()

# Boyutları değiştir
dikdortgen.genislik = 8
dikdortgen.yukseklik = 8
dikdortgen.bilgileri_goster()

# Ölçekle
dikdortgen.olcek(1.5)
dikdortgen.bilgileri_goster()

# =============================================================================
# 6. ADVANCED ENCAPSULATION PATTERNS
# =============================================================================

print("\n=== Advanced Encapsulation Patterns ===")

class SaglikKaydi:
    """Sağlık kaydı - advanced encapsulation örneği"""
    
    def __init__(self, hasta_id, isim):
        self._hasta_id = hasta_id
        self._isim = isim
        self._veriler = {}
        self._erisim_loglari = []
        self._yetkililer = set()
        self._gizlilik_seviyesi = "Normal"
    
    def _erisim_logla(self, islem, yetkili=None):
        """Erişim loglama - private method"""
        log = {
            'islem': islem,
            'yetkili': yetkili,
            'tarih': datetime.datetime.now(),
            'hasta_id': self._hasta_id
        }
        self._erisim_loglari.append(log)
    
    def yetkili_ekle(self, yetkili_id):
        """Yetkili kullanıcı ekle"""
        self._yetkililer.add(yetkili_id)
        self._erisim_logla(f"Yetkili eklendi: {yetkili_id}")
        print(f"Yetkili eklendi: {yetkili_id}")
    
    def yetkili_kaldir(self, yetkili_id):
        """Yetkili kullanıcı kaldır"""
        self._yetkililer.discard(yetkili_id)
        self._erisim_logla(f"Yetkili kaldırıldı: {yetkili_id}")
        print(f"Yetkili kaldırıldı: {yetkili_id}")
    
    def veri_ekle(self, veri_tipi, deger, yetkili_id):
        """Sağlık verisi ekle"""
        if yetkili_id not in self._yetkililer:
            raise PermissionError("Bu işlem için yetkiniz yok!")
        
        if veri_tipi not in self._veriler:
            self._veriler[veri_tipi] = []
        
        veri = {
            'deger': deger,
            'tarih': datetime.datetime.now(),
            'yetkili': yetkili_id
        }
        
        self._veriler[veri_tipi].append(veri)
        self._erisim_logla(f"Veri eklendi: {veri_tipi}", yetkili_id)
        print(f"Veri eklendi: {veri_tipi} = {deger}")
    
    def veri_oku(self, veri_tipi, yetkili_id):
        """Sağlık verisi oku"""
        if yetkili_id not in self._yetkililer:
            raise PermissionError("Bu verileri okuma yetkiniz yok!")
        
        self._erisim_logla(f"Veri okundu: {veri_tipi}", yetkili_id)
        
        if veri_tipi in self._veriler:
            return self._veriler[veri_tipi]
        return []
    
    @property
    def gizlilik_seviyesi(self):
        """Gizlilik seviyesi getter"""
        return self._gizlilik_seviyesi
    
    @gizlilik_seviyesi.setter
    def gizlilik_seviyesi(self, seviye):
        """Gizlilik seviyesi setter"""
        gecerli_seviyeler = ["Normal", "Hassas", "Kritik"]
        if seviye not in gecerli_seviyeler:
            raise ValueError(f"Geçersiz gizlilik seviyesi: {seviye}")
        
        eski_seviye = self._gizlilik_seviyesi
        self._gizlilik_seviyesi = seviye
        self._erisim_logla(f"Gizlilik seviyesi değişti: {eski_seviye} -> {seviye}")
        print(f"Gizlilik seviyesi güncellendi: {seviye}")
    
    def erisim_raporu(self, yetkili_id):
        """Erişim raporu - sadece yetkili kişiler görebilir"""
        if yetkili_id not in self._yetkililer:
            raise PermissionError("Erişim raporunu görme yetkiniz yok!")
        
        print(f"\n=== {self._isim} Erişim Raporu ===")
        print(f"Hasta ID: {self._hasta_id}")
        print(f"Gizlilik Seviyesi: {self._gizlilik_seviyesi}")
        print(f"Yetkili Sayısı: {len(self._yetkililer)}")
        print(f"Toplam Erişim: {len(self._erisim_loglari)}")
        
        print("\nSon 5 erişim:")
        for log in self._erisim_loglari[-5:]:
            tarih = log['tarih'].strftime("%Y-%m-%d %H:%M")
            print(f"  {tarih} - {log['islem']} ({log['yetkili']})")
        
        self._erisim_logla("Erişim raporu görüntülendi", yetkili_id)

# Advanced encapsulation kullanımı
print("Advanced encapsulation örnekleri:")

hasta_kaydi = SaglikKaydi("P001", "Ali Yılmaz")

# Yetkili ekleme
hasta_kaydi.yetkili_ekle("DR001")
hasta_kaydi.yetkili_ekle("NRS001")

# Gizlilik seviyesi ayarlama
hasta_kaydi.gizlilik_seviyesi = "Hassas"

# Veri ekleme
hasta_kaydi.veri_ekle("Tansiyon", "120/80", "DR001")
hasta_kaydi.veri_ekle("Nabız", "72", "NRS001")
hasta_kaydi.veri_ekle("Sıcaklık", "36.5", "NRS001")

# Veri okuma
tansiyon_verileri = hasta_kaydi.veri_oku("Tansiyon", "DR001")
print(f"Tansiyon verileri: {len(tansiyon_verileri)} kayıt")

# Yetkisiz erişim denemesi
try:
    hasta_kaydi.veri_oku("Tansiyon", "UNAUTHORIZED")
except PermissionError as e:
    print(f"Yetkisiz erişim engellendi: {e}")

# Erişim raporu
hasta_kaydi.erisim_raporu("DR001")

print("\n" + "="*60)
print("ENCAPSULATION VE PROPERTY TAMAMLANDI")
print("="*60)

print("\nKonular Özeti:")
print("1. Encapsulation temelleri (public, protected, private)")
print("2. Property decorator kullanımı")
print("3. Data validation ve güvenlik")
print("4. Computed attributes")
print("5. Advanced encapsulation patterns")
print("6. Access control ve logging")

print("\nBir sonraki dosya: inheritance_kalitim.py")