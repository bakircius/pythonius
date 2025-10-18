"""
Python Inheritance (Kalıtım) - Comprehensive Guide
Single, Multiple, Multi-level Inheritance ve Advanced Patterns

Bu dosyada Python'da kalıtım mekanizmaları, miras alma çeşitleri,
method overriding, super() kullanımı ve kalıtım best practices incelenecek.
"""

import datetime
from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

# =============================================================================
# 1. TEMEL KALITIM (SINGLE INHERITANCE)
# =============================================================================

print("=== Temel Kalıtım (Single Inheritance) ===")

class Canli:
    """Ana sınıf - Tüm canlılar için temel özellikler"""
    
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas
        self.yasam_durumu = "Canlı"
        self.dogum_tarihi = datetime.datetime.now() - datetime.timedelta(days=yas*365)
    
    def nefes_al(self):
        """Tüm canlılar nefes alır"""
        return f"{self.isim} nefes alıyor..."
    
    def beslen(self):
        """Tüm canlılar beslenir"""
        return f"{self.isim} besleniyor..."
    
    def uyu(self):
        """Tüm canlılar uyur"""
        return f"{self.isim} uyuyor..."
    
    def bilgi_goster(self):
        """Temel bilgileri göster"""
        print(f"İsim: {self.isim}")
        print(f"Yaş: {self.yas}")
        print(f"Yaşam Durumu: {self.yasam_durumu}")
        print(f"Doğum Tarihi: {self.dogum_tarihi.strftime('%Y-%m-%d')}")
    
    def __str__(self):
        return f"Canlı(isim={self.isim}, yas={self.yas})"

class Hayvan(Canli):
    """Hayvan sınıfı - Canlı sınıfından türetilmiş"""
    
    def __init__(self, isim, yas, tur):
        # Ana sınıfın constructor'ını çağır
        super().__init__(isim, yas)
        self.tur = tur
        self.hareket_turu = "Bilinmiyor"
    
    def ses_cikar(self):
        """Hayvanlar ses çıkarır"""
        return f"{self.isim} ses çıkarıyor..."
    
    def hareket_et(self):
        """Hayvanlar hareket eder"""
        return f"{self.isim} {self.hareket_turu} ile hareket ediyor..."
    
    def avlan(self):
        """Bazı hayvanlar avlanır"""
        return f"{self.isim} avlanıyor..."
    
    def bilgi_goster(self):
        """Genişletilmiş bilgi gösterme - method override"""
        super().bilgi_goster()  # Ana sınıfın methodunu çağır
        print(f"Tür: {self.tur}")
        print(f"Hareket Türü: {self.hareket_turu}")
    
    def __str__(self):
        return f"Hayvan(isim={self.isim}, yas={self.yas}, tur={self.tur})"

class Kedi(Hayvan):
    """Kedi sınıfı - Hayvan sınıfından türetilmiş"""
    
    def __init__(self, isim, yas, cinsi="Tekir"):
        super().__init__(isim, yas, "Kedi")
        self.cinsi = cinsi
        self.hareket_turu = "Yürüme/Koşma"
        self.sevimlilik_seviyesi = 100
    
    def ses_cikar(self):
        """Kedi özel ses çıkarır - method override"""
        return f"{self.isim} miyavlıyor: Miyav miyav!"
    
    def murlan(self):
        """Kediye özel davranış"""
        return f"{self.isim} mırıldanıyor: Prrr..."
    
    def tirmal(self):
        """Kediye özel davranış"""
        return f"{self.isim} tırmalıyor!"
    
    def sevil(self):
        """Kediler sevilmeyi sever"""
        self.sevimlilik_seviyesi += 10
        return f"{self.isim} sevildi ve mutlu oldu! Sevimlilik: {self.sevimlilik_seviyesi}"
    
    def bilgi_goster(self):
        """Kedi özel bilgi gösterme"""
        super().bilgi_goster()
        print(f"Cinsi: {self.cinsi}")
        print(f"Sevimlilik Seviyesi: {self.sevimlilik_seviyesi}")

class Kopek(Hayvan):
    """Köpek sınıfı - Hayvan sınıfından türetilmiş"""
    
    def __init__(self, isim, yas, cinsi="Melez"):
        super().__init__(isim, yas, "Köpek")
        self.cinsi = cinsi
        self.hareket_turu = "Yürüme/Koşma"
        self.sadakat_seviyesi = 100
        self.egitim_durumu = "Temel"
    
    def ses_cikar(self):
        """Köpek özel ses çıkarır - method override"""
        return f"{self.isim} havlıyor: Hav hav!"
    
    def kuyruk_salla(self):
        """Köpeğe özel davranış"""
        return f"{self.isim} kuyruk sallıyor!"
    
    def sahip_koru(self):
        """Köpekler sahiplerini korur"""
        return f"{self.isim} sahibini koruyor!"
    
    def egitim_ver(self, komut):
        """Köpek eğitimi"""
        if self.egitim_durumu == "Temel":
            self.egitim_durumu = "Orta"
        elif self.egitim_durumu == "Orta":
            self.egitim_durumu = "İleri"
        
        return f"{self.isim} '{komut}' komutunu öğrendi! Eğitim seviyesi: {self.egitim_durumu}"
    
    def bilgi_goster(self):
        """Köpek özel bilgi gösterme"""
        super().bilgi_goster()
        print(f"Cinsi: {self.cinsi}")
        print(f"Sadakat Seviyesi: {self.sadakat_seviyesi}")
        print(f"Eğitim Durumu: {self.egitim_durumu}")

# Temel kalıtım kullanımı
print("Temel kalıtım örnekleri:")

# Canlı nesnesi
canli = Canli("Bitkimsi", 5)
print(canli.nefes_al())
print(canli.beslen())

print()

# Kedi nesnesi
kedi = Kedi("Pamuk", 3, "Persian")
print(kedi.ses_cikar())  # Override edilmiş method
print(kedi.nefes_al())   # Ana sınıftan miras alınan method
print(kedi.murlan())     # Kediye özel method
print(kedi.sevil())

print("\nKedi bilgileri:")
kedi.bilgi_goster()

print()

# Köpek nesnesi
kopek = Kopek("Karabaş", 2, "Golden Retriever")
print(kopek.ses_cikar())
print(kopek.kuyruk_salla())
print(kopek.egitim_ver("Otur"))
print(kopek.egitim_ver("Yat"))

print("\nKöpek bilgileri:")
kopek.bilgi_goster()

# =============================================================================
# 2. ÇOKLU KALITIM (MULTIPLE INHERITANCE)
# =============================================================================

print("\n=== Çoklu Kalıtım (Multiple Inheritance) ===")

class Ucabilir:
    """Uçma kabiliyeti mixin sınıfı"""
    
    def __init__(self):
        self.ucma_hizi = 0
        self.maksimum_yukseklik = 0
    
    def uc(self):
        """Uçma yeteneği"""
        return f"{getattr(self, 'isim', 'Bilinmeyen')} uçuyor!"
    
    def indir(self):
        """İniş yeteneği"""
        return f"{getattr(self, 'isim', 'Bilinmeyen')} iniyor!"
    
    def ucus_bilgileri(self):
        """Uçuş bilgilerini göster"""
        print(f"Uçma Hızı: {self.ucma_hizi} km/h")
        print(f"Maksimum Yükseklik: {self.maksimum_yukseklik} m")

class Yuzebilir:
    """Yüzme kabiliyeti mixin sınıfı"""
    
    def __init__(self):
        self.yuzme_hizi = 0
        self.maksimum_derinlik = 0
    
    def yuz(self):
        """Yüzme yeteneği"""
        return f"{getattr(self, 'isim', 'Bilinmeyen')} yüzüyor!"
    
    def dalis_yap(self):
        """Dalış yeteneği"""
        return f"{getattr(self, 'isim', 'Bilinmeyen')} dalış yapıyor!"
    
    def yuzme_bilgileri(self):
        """Yüzme bilgilerini göster"""
        print(f"Yüzme Hızı: {self.yuzme_hizi} km/h")
        print(f"Maksimum Derinlik: {self.maksimum_derinlik} m")

class Kus(Hayvan, Ucabilir):
    """Kuş sınıfı - Hayvan ve Uçabilir'den türetilmiş"""
    
    def __init__(self, isim, yas, cinsi="Genel"):
        # Multiple inheritance'ta super() dikkatli kullanılmalı
        Hayvan.__init__(self, isim, yas, "Kuş")
        Ucabilir.__init__(self)
        
        self.cinsi = cinsi
        self.hareket_turu = "Uçma"
        self.kanat_açikligi = 0
        self.ucma_hizi = 50
        self.maksimum_yukseklik = 1000
    
    def ses_cikar(self):
        """Kuş ses çıkarır"""
        return f"{self.isim} ötüyor: Cik cik!"
    
    def yumurta_birak(self):
        """Kuşa özel davranış"""
        return f"{self.isim} yumurta bırakıyor!"
    
    def bilgi_goster(self):
        """Kuş bilgilerini göster"""
        super().bilgi_goster()
        print(f"Cinsi: {self.cinsi}")
        print(f"Kanat Açıklığı: {self.kanat_açikligi} cm")
        self.ucus_bilgileri()

class Ordek(Hayvan, Ucabilir, Yuzebilir):
    """Ördek sınıfı - Üç sınıftan türetilmiş"""
    
    def __init__(self, isim, yas):
        Hayvan.__init__(self, isim, yas, "Ördek")
        Ucabilir.__init__(self)
        Yuzebilir.__init__(self)
        
        self.hareket_turu = "Yürüme/Uçma/Yüzme"
        self.ucma_hizi = 60
        self.maksimum_yukseklik = 3000
        self.yuzme_hizi = 8
        self.maksimum_derinlik = 10
    
    def ses_cikar(self):
        """Ördek ses çıkarır"""
        return f"{self.isim} vaklıyor: Vak vak!"
    
    def amphibi_hareket(self):
        """Ördek özel hareket - hem uçma hem yüzme"""
        return f"{self.isim} hem uçabiliyor hem yüzebiliyor!"
    
    def bilgi_goster(self):
        """Ördek bilgilerini göster"""
        super().bilgi_goster()
        print("=== Uçuş Yetenekleri ===")
        self.ucus_bilgileri()
        print("=== Yüzme Yetenekleri ===")
        self.yuzme_bilgileri()

# Çoklu kalıtım kullanımı
print("Çoklu kalıtım örnekleri:")

# Kuş nesnesi
kartal = Kus("Kartal", 5, "Kızıl Şahin")
kartal.kanat_açikligi = 200
print(kartal.ses_cikar())
print(kartal.uc())
print(kartal.yumurta_birak())

print("\nKartal bilgileri:")
kartal.bilgi_goster()

print()

# Ördek nesnesi
ordek = Ordek("Donald", 2)
print(ordek.ses_cikar())
print(ordek.uc())
print(ordek.yuz())
print(ordek.amphibi_hareket())

print("\nÖrdek bilgileri:")
ordek.bilgi_goster()

# MRO (Method Resolution Order) kontrolü
print(f"\nÖrdek MRO: {Ordek.__mro__}")

# =============================================================================
# 3. ÇOK SEVİYELİ KALITIM (MULTI-LEVEL INHERITANCE)
# =============================================================================

print("\n=== Çok Seviyeli Kalıtım (Multi-level Inheritance) ===")

class Memeliler(Hayvan):
    """Memeli hayvanlar sınıfı"""
    
    def __init__(self, isim, yas, kan_sicakligi=37):
        super().__init__(isim, yas, "Memeli")
        self.kan_sicakligi = kan_sicakligi
        self.tuy_rengi = "Kahverengi"
        self.sut_verebilir = True
    
    def sut_ver(self):
        """Memeliler süt verir"""
        if self.sut_verebilir:
            return f"{self.isim} süt veriyor"
        return f"{self.isim} süt veremiyor"
    
    def vücut_ısısı_kontrol(self):
        """Vücut ısısı kontrolü"""
        if self.kan_sicakligi > 39:
            return f"{self.isim} ateşli! Sıcaklık: {self.kan_sicakligi}°C"
        elif self.kan_sicakligi < 36:
            return f"{self.isim} soğuk! Sıcaklık: {self.kan_sicakligi}°C"
        else:
            return f"{self.isim} normal sıcaklıkta: {self.kan_sicakligi}°C"
    
    def bilgi_goster(self):
        """Memeli bilgilerini göster"""
        super().bilgi_goster()
        print(f"Kan Sıcaklığı: {self.kan_sicakligi}°C")
        print(f"Tüy Rengi: {self.tuy_rengi}")
        print(f"Süt Verebilir: {self.sut_verebilir}")

class Etcil(Memeliler):
    """Etçil memeli sınıfı"""
    
    def __init__(self, isim, yas):
        super().__init__(isim, yas)
        self.beslenme_tipi = "Etçil"
        self.avcı_seviyesi = "Orta"
        self.dis_yapisi = "Sivri"
    
    def avlan(self):
        """Etçiller avlanır"""
        return f"{self.isim} av arıyor... ({self.avcı_seviyesi} seviye avcı)"
    
    def et_ye(self, av):
        """Et yeme"""
        return f"{self.isim} {av} yiyor"
    
    def bilgi_goster(self):
        """Etçil bilgilerini göster"""
        super().bilgi_goster()
        print(f"Beslenme Tipi: {self.beslenme_tipi}")
        print(f"Avcı Seviyesi: {self.avcı_seviyesi}")
        print(f"Diş Yapısı: {self.dis_yapisi}")

class Aslan(Etcil):
    """Aslan sınıfı - En spesifik seviye"""
    
    def __init__(self, isim, yas, cinsiyet="Erkek"):
        super().__init__(isim, yas)
        self.cinsiyet = cinsiyet
        self.avcı_seviyesi = "Yüksek"
        self.tuy_rengi = "Sarı"
        self.yelesi_var = (cinsiyet == "Erkek")
        self.sürü_lideri = False
    
    def kükreç(self):
        """Aslana özel ses"""
        return f"{self.isim} kükrediyor: ROARRR!"
    
    def sürü_yönet(self):
        """Sürü yönetimi"""
        if self.sürü_lideri:
            return f"{self.isim} sürüyü yönetiyor"
        return f"{self.isim} henüz sürü lideri değil"
    
    def lider_ol(self):
        """Liderlik alma"""
        self.sürü_lideri = True
        return f"{self.isim} sürünün yeni lideri oldu!"
    
    def ses_cikar(self):
        """Aslan ses çıkarır - method override"""
        return self.kükreç()
    
    def bilgi_goster(self):
        """Aslan bilgilerini göster"""
        super().bilgi_goster()
        print(f"Cinsiyet: {self.cinsiyet}")
        print(f"Yelesi Var: {self.yelesi_var}")
        print(f"Sürü Lideri: {self.sürü_lideri}")

# Çok seviyeli kalıtım kullanımı
print("Çok seviyeli kalıtım örnekleri:")

aslan = Aslan("Simba", 5, "Erkek")
print(aslan.ses_cikar())  # En spesifik method
print(aslan.nefes_al())   # En üst sınıftan
print(aslan.sut_ver())    # Orta seviyeden
print(aslan.avlan())      # Etçil sınıfından
print(aslan.lider_ol())

print("\nAslan bilgileri:")
aslan.bilgi_goster()

print(f"\nAslan kalıtım zinciri: {[cls.__name__ for cls in Aslan.__mro__]}")

# =============================================================================
# 4. METHOD OVERRIDE VE SUPER() KULLANIMI
# =============================================================================

print("\n=== Method Override ve Super() Kullanımı ===")

class Arac:
    """Araç temel sınıfı"""
    
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil
        self.hiz = 0
        self.motor_calisiyor = False
    
    def motor_calistir(self):
        """Motor çalıştırma"""
        self.motor_calisiyor = True
        return f"{self.marka} {self.model} motoru çalıştırıldı"
    
    def motor_durdur(self):
        """Motor durdurma"""
        self.motor_calisiyor = False
        self.hiz = 0
        return f"{self.marka} {self.model} motoru durduruldu"
    
    def hızlan(self, miktar):
        """Hızlanma"""
        if self.motor_calisiyor:
            self.hiz += miktar
            return f"Hız artırıldı: {self.hiz} km/h"
        return "Önce motoru çalıştırın!"
    
    def yavas(self, miktar):
        """Yavaşlama"""
        self.hiz = max(0, self.hiz - miktar)
        return f"Hız azaltıldı: {self.hiz} km/h"
    
    def bilgi_goster(self):
        """Araç bilgilerini göster"""
        print(f"Marka: {self.marka}")
        print(f"Model: {self.model}")
        print(f"Yıl: {self.yil}")
        print(f"Hız: {self.hiz} km/h")
        print(f"Motor: {'Çalışıyor' if self.motor_calisiyor else 'Durmuş'}")

class Otomobil(Arac):
    """Otomobil sınıfı - method override örnekleri"""
    
    def __init__(self, marka, model, yil, kapi_sayisi=4):
        super().__init__(marka, model, yil)  # Ana sınıf constructor
        self.kapi_sayisi = kapi_sayisi
        self.maksimum_hiz = 200
        self.vites = "P"  # Park
    
    def motor_calistir(self):
        """Motor çalıştırma - override edilmiş"""
        # Ana sınıfın methodunu çağır
        result = super().motor_calistir()
        self.vites = "D"  # Drive
        return result + " - Vites D'ye alındı"
    
    def motor_durdur(self):
        """Motor durdurma - override edilmiş"""
        self.vites = "P"  # Park
        result = super().motor_durdur()
        return result + " - Vites P'ye alındı"
    
    def hızlan(self, miktar):
        """Hızlanma - maksimum hız kontrolü eklendi"""
        if not self.motor_calisiyor:
            return "Önce motoru çalıştırın!"
        
        if self.vites not in ["D", "R"]:
            return "Vitesi D veya R'ye alın!"
        
        # Ana sınıfın methodunu çağır
        if self.hiz + miktar <= self.maksimum_hiz:
            return super().hızlan(miktar)
        else:
            return f"Maksimum hız aşılamaz! Limit: {self.maksimum_hiz} km/h"
    
    def vites_degistir(self, yeni_vites):
        """Vites değiştirme - otomobile özel"""
        gecerli_vitesler = ["P", "R", "N", "D"]
        if yeni_vites in gecerli_vitesler:
            self.vites = yeni_vites
            return f"Vites {yeni_vites}'ye alındı"
        return f"Geçersiz vites: {yeni_vites}"
    
    def bilgi_goster(self):
        """Bilgi gösterme - genişletilmiş"""
        super().bilgi_goster()  # Ana sınıfın methodunu çağır
        print(f"Kapı Sayısı: {self.kapi_sayisi}")
        print(f"Maksimum Hız: {self.maksimum_hiz} km/h")
        print(f"Vites: {self.vites}")

class Motosiklet(Arac):
    """Motosiklet sınıfı - farklı override örnekleri"""
    
    def __init__(self, marka, model, yil, motor_hacmi):
        super().__init__(marka, model, yil)
        self.motor_hacmi = motor_hacmi
        self.maksimum_hiz = 300
        self.kask_takili = False
    
    def motor_calistir(self):
        """Motor çalıştırma - kask kontrolü eklendi"""
        if not self.kask_takili:
            return "Önce kask takın!"
        
        return super().motor_calistir() + " - Güvenli sürüş!"
    
    def kask_tak(self):
        """Kask takma - motosiklete özel"""
        self.kask_takili = True
        return "Kask takıldı"
    
    def kask_cikar(self):
        """Kask çıkarma"""
        if self.hiz > 0:
            return "Hareket halindeyken kask çıkarılamaz!"
        
        self.kask_takili = False
        return "Kask çıkarıldı"
    
    def wheelie_yap(self):
        """Wheelie yapma - motosiklete özel"""
        if self.hiz > 30:
            return f"{self.marka} ile wheelie yapıyor!"
        return "Wheelie için daha fazla hız gerekli!"
    
    def bilgi_goster(self):
        """Bilgi gösterme - motosiklet özel"""
        super().bilgi_goster()
        print(f"Motor Hacmi: {self.motor_hacmi} cc")
        print(f"Kask Takılı: {self.kask_takili}")

# Method override ve super() kullanımı
print("Method override ve super() örnekleri:")

# Otomobil kullanımı
araba = Otomobil("Toyota", "Corolla", 2023, 4)
print(araba.motor_calistir())  # Override edilmiş method
print(araba.vites_degistir("D"))
print(araba.hızlan(50))
print(araba.hızlan(180))  # Maksimum hız kontrolü

print("\nAraba bilgileri:")
araba.bilgi_goster()

print()

# Motosiklet kullanımı
motor = Motosiklet("Yamaha", "R1", 2023, 1000)
print(motor.motor_calistir())  # Kask kontrolü
print(motor.kask_tak())
print(motor.motor_calistir())  # Şimdi çalışacak
print(motor.hızlan(80))
print(motor.wheelie_yap())

print("\nMotor bilgileri:")
motor.bilgi_goster()

# =============================================================================
# 5. ABSTRACT BASE CLASSES (ABC)
# =============================================================================

print("\n=== Abstract Base Classes (ABC) ===")

class Sekil(ABC):
    """Abstract base class - şekil sınıfı"""
    
    def __init__(self, isim):
        self.isim = isim
        self.renk = "Beyaz"
    
    @abstractmethod
    def alan_hesapla(self):
        """Soyut method - alt sınıflarda implement edilmeli"""
        pass
    
    @abstractmethod
    def cevre_hesapla(self):
        """Soyut method - alt sınıflarda implement edilmeli"""
        pass
    
    def renk_degistir(self, yeni_renk):
        """Concrete method - tüm şekillerde aynı"""
        self.renk = yeni_renk
        return f"{self.isim} rengi {yeni_renk} olarak değiştirildi"
    
    def bilgi_goster(self):
        """Concrete method - genel bilgi"""
        print(f"Şekil: {self.isim}")
        print(f"Renk: {self.renk}")
        print(f"Alan: {self.alan_hesapla()}")
        print(f"Çevre: {self.cevre_hesapla()}")

class Kare(Sekil):
    """Kare sınıfı - abstract methods implement edilmiş"""
    
    def __init__(self, kenar):
        super().__init__("Kare")
        self.kenar = kenar
    
    def alan_hesapla(self):
        """Alan hesaplama implementation"""
        return self.kenar ** 2
    
    def cevre_hesapla(self):
        """Çevre hesaplama implementation"""
        return 4 * self.kenar
    
    def kosegenHesapla(self):
        """Kare özel method"""
        return self.kenar * (2 ** 0.5)

class Daire(Sekil):
    """Daire sınıfı - abstract methods implement edilmiş"""
    
    def __init__(self, yaricap):
        super().__init__("Daire")
        self.yaricap = yaricap
        self.pi = 3.14159
    
    def alan_hesapla(self):
        """Alan hesaplama implementation"""
        return self.pi * (self.yaricap ** 2)
    
    def cevre_hesapla(self):
        """Çevre hesaplama implementation"""
        return 2 * self.pi * self.yaricap
    
    def cap_hesapla(self):
        """Daire özel method"""
        return 2 * self.yaricap

class Ucgen(Sekil):
    """Üçgen sınıfı - farklı constructor"""
    
    def __init__(self, kenar1, kenar2, kenar3):
        super().__init__("Üçgen")
        self.kenar1 = kenar1
        self.kenar2 = kenar2
        self.kenar3 = kenar3
    
    def alan_hesapla(self):
        """Heron formülü ile alan hesaplama"""
        s = (self.kenar1 + self.kenar2 + self.kenar3) / 2
        return (s * (s - self.kenar1) * (s - self.kenar2) * (s - self.kenar3)) ** 0.5
    
    def cevre_hesapla(self):
        """Çevre hesaplama implementation"""
        return self.kenar1 + self.kenar2 + self.kenar3
    
    def ucgen_tipi(self):
        """Üçgen tipi belirleme"""
        kenarlar = sorted([self.kenar1, self.kenar2, self.kenar3])
        if kenarlar[0] == kenarlar[1] == kenarlar[2]:
            return "Eşkenar"
        elif kenarlar[0] == kenarlar[1] or kenarlar[1] == kenarlar[2]:
            return "İkizkenar"
        else:
            return "Çeşitkenar"

# Abstract Base Classes kullanımı
print("Abstract Base Classes örnekleri:")

# Direct instantiation yapılamaz
try:
    sekil = Sekil("Test")  # TypeError
except TypeError as e:
    print(f"Abstract class instantiation hatası: {e}")

# Concrete sınıflardan nesneler
kare = Kare(5)
kare.renk_degistir("Kırmızı")
print("\nKare bilgileri:")
kare.bilgi_goster()
print(f"Köşegen: {kare.kosegenHesapla():.2f}")

print()

daire = Daire(3)
daire.renk_degistir("Mavi")
print("Daire bilgileri:")
daire.bilgi_goster()
print(f"Çap: {daire.cap_hesapla()}")

print()

ucgen = Ucgen(3, 4, 5)
ucgen.renk_degistir("Yeşil")
print("Üçgen bilgileri:")
ucgen.bilgi_goster()
print(f"Üçgen Tipi: {ucgen.ucgen_tipi()}")

# =============================================================================
# 6. COMPLEX INHERITANCE SCENARIO
# =============================================================================

print("\n=== Complex Inheritance Scenario ===")

class EgitimKurumu:
    """Eğitim kurumu base class"""
    
    def __init__(self, isim, kuruluş_yili):
        self.isim = isim
        self.kuruluş_yili = kuruluş_yili
        self.ogrenci_sayisi = 0
        self.personel_sayisi = 0
    
    def ogrenci_kaydet(self, sayi=1):
        """Öğrenci kaydı"""
        self.ogrenci_sayisi += sayi
        return f"{sayi} öğrenci kaydedildi. Toplam: {self.ogrenci_sayisi}"
    
    def personel_iste(self, sayi=1):
        """Personel işe alma"""
        self.personel_sayisi += sayi
        return f"{sayi} personel işe alındı. Toplam: {self.personel_sayisi}"

class Akreditasyon:
    """Akreditasyon mixin"""
    
    def __init__(self):
        self.akreditasyonlar = []
        self.kalite_puani = 0
    
    def akreditasyon_ekle(self, akreditasyon):
        """Akreditasyon ekleme"""
        self.akreditasyonlar.append(akreditasyon)
        self.kalite_puani += 10
        return f"{akreditasyon} akreditasyonu eklendi"
    
    def kalite_degerlendirme(self):
        """Kalite değerlendirmesi"""
        if self.kalite_puani >= 80:
            return "Mükemmel"
        elif self.kalite_puani >= 60:
            return "İyi"
        elif self.kalite_puani >= 40:
            return "Orta"
        else:
            return "Geliştirilmeli"

class OnlineEgitim:
    """Online eğitim mixin"""
    
    def __init__(self):
        self.online_platform = None
        self.online_ogrenci_sayisi = 0
        self.kurs_sayisi = 0
    
    def platform_kur(self, platform_adi):
        """Online platform kurma"""
        self.online_platform = platform_adi
        return f"{platform_adi} platformu kuruldu"
    
    def online_kurs_ac(self, kurs_adi):
        """Online kurs açma"""
        if self.online_platform:
            self.kurs_sayisi += 1
            return f"{kurs_adi} kursu açıldı. Toplam kurs: {self.kurs_sayisi}"
        return "Önce online platform kurun!"

class Universite(EgitimKurumu, Akreditasyon, OnlineEgitim):
    """Üniversite - complex inheritance"""
    
    def __init__(self, isim, kuruluş_yili, rektor):
        EgitimKurumu.__init__(self, isim, kuruluş_yili)
        Akreditasyon.__init__(self)
        OnlineEgitim.__init__(self)
        
        self.rektor = rektor
        self.fakulte_sayisi = 0
        self.lisans_programlari = []
        self.lisansüstu_programlari = []
    
    def fakulte_kur(self, fakulte_adi):
        """Fakülte kurma"""
        self.fakulte_sayisi += 1
        return f"{fakulte_adi} fakültesi kuruldu. Toplam fakülte: {self.fakulte_sayisi}"
    
    def program_ac(self, program_adi, seviye="Lisans"):
        """Akademik program açma"""
        if seviye == "Lisans":
            self.lisans_programlari.append(program_adi)
            return f"{program_adi} lisans programı açıldı"
        elif seviye == "Lisansüstü":
            self.lisansüstu_programlari.append(program_adi)
            return f"{program_adi} lisansüstü programı açıldı"
    
    def kapsamli_rapor(self):
        """Kapsamlı üniversite raporu"""
        print(f"\n=== {self.isim} Üniversitesi Raporu ===")
        print(f"Kuruluş Yılı: {self.kuruluş_yili}")
        print(f"Rektör: {self.rektor}")
        print(f"Fakülte Sayısı: {self.fakulte_sayisi}")
        print(f"Öğrenci Sayısı: {self.ogrenci_sayisi}")
        print(f"Personel Sayısı: {self.personel_sayisi}")
        print(f"Lisans Programları: {len(self.lisans_programlari)}")
        print(f"Lisansüstü Programları: {len(self.lisansüstu_programlari)}")
        print(f"Kalite Puanı: {self.kalite_puani}")
        print(f"Kalite Seviyesi: {self.kalite_degerlendirme()}")
        print(f"Online Platform: {self.online_platform or 'Yok'}")
        print(f"Online Kurs Sayısı: {self.kurs_sayisi}")
        print(f"Akreditasyonlar: {', '.join(self.akreditasyonlar) or 'Yok'}")

# Complex inheritance kullanımı
print("Complex inheritance örneği:")

uni = Universite("TechEdu Üniversitesi", 1990, "Prof. Dr. Ali Veli")

# Farklı mixin'lerden gelen methodları kullan
print(uni.fakulte_kur("Mühendislik Fakültesi"))
print(uni.fakulte_kur("İİBF"))
print(uni.program_ac("Bilgisayar Mühendisliği", "Lisans"))
print(uni.program_ac("Makine Öğrenmesi", "Lisansüstü"))

print(uni.ogrenci_kaydet(1500))
print(uni.personel_iste(200))

print(uni.akreditasyon_ekle("ABET"))
print(uni.akreditasyon_ekle("EUR-ACE"))

print(uni.platform_kur("TechEduOnline"))
print(uni.online_kurs_ac("Python Programming"))
print(uni.online_kurs_ac("Data Science"))

# Kapsamlı rapor
uni.kapsamli_rapor()

print(f"\nÜniversite MRO: {[cls.__name__ for cls in Universite.__mro__]}")

print("\n" + "="*60)
print("INHERITANCE (KALITIM) TAMAMLANDI")
print("="*60)

print("\nKonular Özeti:")
print("1. Single Inheritance (Tekli Kalıtım)")
print("2. Multiple Inheritance (Çoklu Kalıtım)")
print("3. Multi-level Inheritance (Çok Seviyeli Kalıtım)")
print("4. Method Override ve super() kullanımı")
print("5. Abstract Base Classes (ABC)")
print("6. Complex Inheritance Scenarios")
print("7. Method Resolution Order (MRO)")

print("\nBir sonraki dosya: polymorphism_ve_abstraction.py")