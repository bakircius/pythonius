"""
Python Nesne Yönelimli Programlama Temelleri
Class, Object, Constructor, Methods - Comprehensive Guide

Bu dosyada Python'da OOP'nin temel kavramları olan sınıflar, nesneler,
constructor'lar ve metodlar detaylı örneklerle incelenecek.
"""

import datetime
from typing import List, Optional, ClassVar

# =============================================================================
# 1. TEMEL CLASS VE OBJECT KAVRAMI
# =============================================================================

print("=== Class ve Object Temelleri ===")

class Araba:
    """Basit araba sınıfı örneği"""
    
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil
        self.hiz = 0
        self.motor_calisiyor = False
    
    def motor_calistir(self):
        """Motoru çalıştır"""
        self.motor_calisiyor = True
        print(f"{self.marka} {self.model} motoru çalıştırıldı.")
    
    def motor_durdur(self):
        """Motoru durdur"""
        self.motor_calisiyor = False
        self.hiz = 0
        print(f"{self.marka} {self.model} motoru durduruldu.")
    
    def hizlan(self, miktar):
        """Hızlanma"""
        if self.motor_calisiyor:
            self.hiz += miktar
            print(f"Hız artırıldı. Şimdiki hız: {self.hiz} km/h")
        else:
            print("Önce motoru çalıştırmalısınız!")
    
    def yavasla(self, miktar):
        """Yavaşlama"""
        if self.hiz >= miktar:
            self.hiz -= miktar
        else:
            self.hiz = 0
        print(f"Hız azaltıldı. Şimdiki hız: {self.hiz} km/h")

# Nesne oluşturma ve kullanma
print("Araba nesneleri oluşturuluyor...")
araba1 = Araba("Toyota", "Corolla", 2020)
araba2 = Araba("BMW", "X5", 2022)

print(f"Araba 1: {araba1.marka} {araba1.model} ({araba1.yil})")
print(f"Araba 2: {araba2.marka} {araba2.model} ({araba2.yil})")

# Metodları kullanma
araba1.motor_calistir()
araba1.hizlan(50)
araba1.hizlan(30)
araba1.yavasla(20)
araba1.motor_durdur()

# =============================================================================
# 2. CONSTRUCTOR (__init__) DETAYLI İNCELEME
# =============================================================================

print("\n=== Constructor Detayları ===")

class Kisi:
    """Gelişmiş constructor örneği"""
    
    def __init__(self, isim, soyisim, yas=None, email=None):
        # Zorunlu parametreler
        self.isim = isim
        self.soyisim = soyisim
        
        # İsteğe bağlı parametreler
        self.yas = yas
        self.email = email
        
        # Otomatik hesaplanan özellikler
        self.tam_isim = f"{isim} {soyisim}"
        self.kayit_tarihi = datetime.datetime.now()
        
        # Varsayılan değerler
        self.aktif = True
        self.notlar = []
        
        print(f"Yeni kişi oluşturuldu: {self.tam_isim}")
    
    def bilgileri_goster(self):
        """Kişi bilgilerini göster"""
        print(f"İsim: {self.tam_isim}")
        print(f"Yaş: {self.yas or 'Belirtilmemiş'}")
        print(f"Email: {self.email or 'Belirtilmemiş'}")
        print(f"Kayıt Tarihi: {self.kayit_tarihi.strftime('%Y-%m-%d %H:%M')}")
        print(f"Aktif: {'Evet' if self.aktif else 'Hayır'}")
    
    def not_ekle(self, not_metni):
        """Kişiye not ekle"""
        self.notlar.append({
            'metin': not_metni,
            'tarih': datetime.datetime.now()
        })
        print(f"Not eklendi: {not_metni}")

# Constructor çeşitleri
print("Farklı constructor kullanımları:")

kisi1 = Kisi("Ali", "Veli")
kisi2 = Kisi("Ayşe", "Demir", 25)
kisi3 = Kisi("Mehmet", "Kaya", 30, "mehmet@example.com")

print("\nKişi bilgileri:")
kisi1.bilgileri_goster()
print()
kisi3.bilgileri_goster()

# =============================================================================
# 3. INSTANCE VARIABLES VE METHODS
# =============================================================================

print("\n=== Instance Variables ve Methods ===")

class BankHesabi:
    """Banka hesabı sınıfı - instance variables örneği"""
    
    def __init__(self, hesap_no, sahip_adi, baslangic_bakiye=0):
        # Instance variables (her nesne için ayrı)
        self.hesap_no = hesap_no
        self.sahip_adi = sahip_adi
        self.bakiye = baslangic_bakiye
        self.islem_gecmisi = []
        self.hesap_durumu = "Aktif"
        self.acilis_tarihi = datetime.datetime.now()
    
    def para_yatir(self, miktar):
        """Para yatırma işlemi"""
        if miktar <= 0:
            print("Yatırılacak miktar pozitif olmalıdır!")
            return False
        
        self.bakiye += miktar
        self.islem_gecmisi.append({
            'tip': 'Yatırma',
            'miktar': miktar,
            'tarih': datetime.datetime.now(),
            'bakiye': self.bakiye
        })
        print(f"{miktar} TL yatırıldı. Yeni bakiye: {self.bakiye} TL")
        return True
    
    def para_cek(self, miktar):
        """Para çekme işlemi"""
        if miktar <= 0:
            print("Çekilecek miktar pozitif olmalıdır!")
            return False
        
        if miktar > self.bakiye:
            print("Yetersiz bakiye!")
            return False
        
        self.bakiye -= miktar
        self.islem_gecmisi.append({
            'tip': 'Çekme',
            'miktar': miktar,
            'tarih': datetime.datetime.now(),
            'bakiye': self.bakiye
        })
        print(f"{miktar} TL çekildi. Yeni bakiye: {self.bakiye} TL")
        return True
    
    def bakiye_sorgula(self):
        """Bakiye sorgulama"""
        print(f"Hesap No: {self.hesap_no}")
        print(f"Sahip: {self.sahip_adi}")
        print(f"Güncel Bakiye: {self.bakiye} TL")
        print(f"Hesap Durumu: {self.hesap_durumu}")
        return self.bakiye
    
    def islem_gecmisini_goster(self, son_n_islem=5):
        """İşlem geçmişini göster"""
        print(f"\n=== Son {son_n_islem} İşlem ===")
        son_islemler = self.islem_gecmisi[-son_n_islem:]
        
        for islem in son_islemler:
            tarih_str = islem['tarih'].strftime("%Y-%m-%d %H:%M")
            print(f"{tarih_str} - {islem['tip']}: {islem['miktar']} TL - Bakiye: {islem['bakiye']} TL")
    
    def hesap_ozeti(self):
        """Hesap özeti"""
        toplam_yatirim = sum(islem['miktar'] for islem in self.islem_gecmisi if islem['tip'] == 'Yatırma')
        toplam_cekim = sum(islem['miktar'] for islem in self.islem_gecmisi if islem['tip'] == 'Çekme')
        
        print(f"\n=== Hesap Özeti ===")
        print(f"Hesap Sahibi: {self.sahip_adi}")
        print(f"Açılış Tarihi: {self.acilis_tarihi.strftime('%Y-%m-%d')}")
        print(f"Toplam Yatırım: {toplam_yatirim} TL")
        print(f"Toplam Çekim: {toplam_cekim} TL")
        print(f"Güncel Bakiye: {self.bakiye} TL")
        print(f"Toplam İşlem Sayısı: {len(self.islem_gecmisi)}")

# Banka hesabı kullanımı
print("Banka hesapları oluşturuluyor...")
hesap1 = BankHesabi("12345", "Ali Veli", 1000)
hesap2 = BankHesabi("67890", "Ayşe Demir")

print("\nHesap 1 işlemleri:")
hesap1.bakiye_sorgula()
hesap1.para_yatir(500)
hesap1.para_cek(200)
hesap1.para_yatir(300)
hesap1.para_cek(50)
hesap1.islem_gecmisini_goster(3)

print("\nHesap 2 işlemleri:")
hesap2.bakiye_sorgula()
hesap2.para_yatir(2000)
hesap2.para_cek(300)

# =============================================================================
# 4. CLASS VARIABLES VE CLASS METHODS
# =============================================================================

print("\n=== Class Variables ve Class Methods ===")

class Ogrenci:
    """Öğrenci sınıfı - class variables örneği"""
    
    # Class variables (tüm nesneler için ortak)
    okul_adi = "Python Akademisi"
    toplam_ogrenci_sayisi = 0
    gecme_notu = 60
    aktif_donem = "2024-2025"
    
    def __init__(self, isim, soyisim, numara):
        # Instance variables
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.notlar = {}
        self.devamsizlik = 0
        self.kayit_tarihi = datetime.datetime.now()
        
        # Class variable güncelleme
        Ogrenci.toplam_ogrenci_sayisi += 1
        
        print(f"Yeni öğrenci kaydedildi: {self.isim} {self.soyisim} (#{self.numara})")
    
    @classmethod
    def okul_bilgilerini_goster(cls):
        """Class method - okul bilgilerini göster"""
        print(f"\n=== Okul Bilgileri ===")
        print(f"Okul Adı: {cls.okul_adi}")
        print(f"Aktif Dönem: {cls.aktif_donem}")
        print(f"Toplam Öğrenci Sayısı: {cls.toplam_ogrenci_sayisi}")
        print(f"Geçme Notu: {cls.gecme_notu}")
    
    @classmethod
    def gecme_notunu_guncelle(cls, yeni_not):
        """Class method - geçme notunu güncelle"""
        eski_not = cls.gecme_notu
        cls.gecme_notu = yeni_not
        print(f"Geçme notu güncellendi: {eski_not} -> {yeni_not}")
    
    @classmethod
    def donem_guncelle(cls, yeni_donem):
        """Class method - dönem güncelle"""
        cls.aktif_donem = yeni_donem
        print(f"Aktif dönem güncellendi: {yeni_donem}")
    
    def not_ekle(self, ders, not_degeri):
        """Öğrenci notunu ekle"""
        if ders not in self.notlar:
            self.notlar[ders] = []
        
        self.notlar[ders].append(not_degeri)
        print(f"{self.isim} {self.soyisim} - {ders}: {not_degeri}")
    
    def ortalama_hesapla(self):
        """Genel not ortalaması hesapla"""
        if not self.notlar:
            return 0
        
        tum_notlar = []
        for ders_notlari in self.notlar.values():
            tum_notlar.extend(ders_notlari)
        
        ortalama = sum(tum_notlar) / len(tum_notlar)
        return round(ortalama, 2)
    
    def ders_ortalamasi(self, ders):
        """Belirli bir dersin ortalaması"""
        if ders not in self.notlar:
            return 0
        
        ders_notlari = self.notlar[ders]
        return round(sum(ders_notlari) / len(ders_notlari), 2)
    
    def durum_raporu(self):
        """Öğrenci durum raporu"""
        print(f"\n=== {self.isim} {self.soyisim} Durum Raporu ===")
        print(f"Öğrenci No: {self.numara}")
        print(f"Kayıt Tarihi: {self.kayit_tarihi.strftime('%Y-%m-%d')}")
        print(f"Devamsızlık: {self.devamsizlik} gün")
        
        if self.notlar:
            print("\nDers Notları:")
            for ders, notlar in self.notlar.items():
                ders_ort = self.ders_ortalamasi(ders)
                durum = "Geçti" if ders_ort >= self.gecme_notu else "Kaldı"
                print(f"  {ders}: {notlar} -> Ortalama: {ders_ort} ({durum})")
            
            genel_ortalama = self.ortalama_hesapla()
            genel_durum = "Geçti" if genel_ortalama >= self.gecme_notu else "Kaldı"
            print(f"\nGenel Ortalama: {genel_ortalama} ({genel_durum})")
        else:
            print("Henüz not girilmemiş.")

# Class variables ve methods kullanımı
print("Öğrenci sınıfı örnekleri:")

# İlk durumu göster
Ogrenci.okul_bilgilerini_goster()

# Öğrenci oluştur
ogrenci1 = Ogrenci("Ali", "Yılmaz", "001")
ogrenci2 = Ogrenci("Zehra", "Kaya", "002")
ogrenci3 = Ogrenci("Murat", "Demir", "003")

# Güncellenmiş durumu göster
Ogrenci.okul_bilgilerini_goster()

# Class methods kullan
Ogrenci.gecme_notunu_guncelle(65)
Ogrenci.donem_guncelle("2025-2026")

# Öğrenci notları ekle
ogrenci1.not_ekle("Matematik", 75)
ogrenci1.not_ekle("Matematik", 80)
ogrenci1.not_ekle("Fizik", 70)
ogrenci1.not_ekle("Kimya", 85)

ogrenci2.not_ekle("Matematik", 90)
ogrenci2.not_ekle("Fizik", 95)
ogrenci2.not_ekle("Kimya", 88)

# Durum raporları
ogrenci1.durum_raporu()
ogrenci2.durum_raporu()

# =============================================================================
# 5. STATIC METHODS
# =============================================================================

print("\n=== Static Methods ===")

class MathUtils:
    """Matematik yardımcı fonksiyonları sınıfı"""
    
    @staticmethod
    def faktoryel(n):
        """Faktöriyel hesaplama"""
        if n < 0:
            raise ValueError("Negatif sayıların faktöriyeli hesaplanamaz")
        if n == 0 or n == 1:
            return 1
        
        sonuc = 1
        for i in range(2, n + 1):
            sonuc *= i
        return sonuc
    
    @staticmethod
    def asal_mi(sayi):
        """Sayının asal olup olmadığını kontrol et"""
        if sayi < 2:
            return False
        
        for i in range(2, int(sayi ** 0.5) + 1):
            if sayi % i == 0:
                return False
        return True
    
    @staticmethod
    def ebob(a, b):
        """En büyük ortak bölen"""
        while b:
            a, b = b, a % b
        return a
    
    @staticmethod
    def ekok(a, b):
        """En küçük ortak kat"""
        return (a * b) // MathUtils.ebob(a, b)
    
    @staticmethod
    def fibonacci_dizisi(n):
        """Fibonacci dizisinin ilk n elemanı"""
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        
        dizi = [0, 1]
        for i in range(2, n):
            dizi.append(dizi[i-1] + dizi[i-2])
        return dizi

class StringUtils:
    """String yardımcı fonksiyonları sınıfı"""
    
    @staticmethod
    def palindrom_mu(metin):
        """Metnin palindrom olup olmadığını kontrol et"""
        temiz_metin = ''.join(char.lower() for char in metin if char.isalnum())
        return temiz_metin == temiz_metin[::-1]
    
    @staticmethod
    def kelime_sayisi(metin):
        """Metindeki kelime sayısını say"""
        return len(metin.split())
    
    @staticmethod
    def harf_frekansi(metin):
        """Harflerin frekansını hesapla"""
        frekans = {}
        for harf in metin.lower():
            if harf.isalpha():
                frekans[harf] = frekans.get(harf, 0) + 1
        return frekans
    
    @staticmethod
    def camel_case_yap(metin):
        """Metni camelCase formatına çevir"""
        kelimeler = metin.split()
        if not kelimeler:
            return ""
        
        sonuc = kelimeler[0].lower()
        for kelime in kelimeler[1:]:
            sonuc += kelime.capitalize()
        return sonuc

# Static methods kullanımı
print("Math Utils örnekleri:")
print(f"5! = {MathUtils.faktoryel(5)}")
print(f"17 asal mı? {MathUtils.asal_mi(17)}")
print(f"12 ve 18'in EBOB'u: {MathUtils.ebob(12, 18)}")
print(f"12 ve 18'in EKOK'u: {MathUtils.ekok(12, 18)}")
print(f"İlk 10 Fibonacci sayısı: {MathUtils.fibonacci_dizisi(10)}")

print("\nString Utils örnekleri:")
print(f"'racecar' palindrom mu? {StringUtils.palindrom_mu('racecar')}")
print(f"'A man a plan a canal Panama' palindrom mu? {StringUtils.palindrom_mu('A man a plan a canal Panama')}")
print(f"Kelime sayısı: {StringUtils.kelime_sayisi('Python programlama çok eğlenceli')}")
print(f"Harf frekansı: {StringUtils.harf_frekansi('hello world')}")
print(f"CamelCase: {StringUtils.camel_case_yap('python programlama dili')}")

# =============================================================================
# 6. COMPLEX CLASS EXAMPLE - E-TİCARET SİSTEMİ
# =============================================================================

print("\n=== Kapsamlı Class Örneği: E-Ticaret Sistemi ===")

class Urun:
    """Ürün sınıfı"""
    
    urun_sayaci = 0
    
    def __init__(self, isim, fiyat, kategori, stok=0):
        Urun.urun_sayaci += 1
        self.id = Urun.urun_sayaci
        self.isim = isim
        self.fiyat = fiyat
        self.kategori = kategori
        self.stok = stok
        self.ekleme_tarihi = datetime.datetime.now()
        self.incelemeler = []
    
    def stok_ekle(self, miktar):
        """Stok ekleme"""
        self.stok += miktar
        print(f"{self.isim} ürününe {miktar} adet stok eklendi. Yeni stok: {self.stok}")
    
    def stok_azalt(self, miktar):
        """Stok azaltma"""
        if miktar > self.stok:
            print(f"Yetersiz stok! Mevcut stok: {self.stok}")
            return False
        
        self.stok -= miktar
        print(f"{self.isim} ürününden {miktar} adet satıldı. Kalan stok: {self.stok}")
        return True
    
    def inceleme_ekle(self, puan, yorum):
        """Ürün incelemesi ekle"""
        inceleme = {
            'puan': puan,
            'yorum': yorum,
            'tarih': datetime.datetime.now()
        }
        self.incelemeler.append(inceleme)
        print(f"{self.isim} ürününe {puan}/5 puan ile inceleme eklendi")
    
    def ortalama_puan(self):
        """Ortalama puan hesapla"""
        if not self.incelemeler:
            return 0
        
        toplam_puan = sum(inc['puan'] for inc in self.incelemeler)
        return round(toplam_puan / len(self.incelemeler), 1)
    
    def urun_detayi(self):
        """Ürün detaylarını göster"""
        print(f"\n=== Ürün Detayı ===")
        print(f"ID: {self.id}")
        print(f"İsim: {self.isim}")
        print(f"Kategori: {self.kategori}")
        print(f"Fiyat: {self.fiyat} TL")
        print(f"Stok: {self.stok} adet")
        print(f"Ortalama Puan: {self.ortalama_puan()}/5 ({len(self.incelemeler)} inceleme)")
        print(f"Eklenme Tarihi: {self.ekleme_tarihi.strftime('%Y-%m-%d')}")

class Musteri:
    """Müşteri sınıfı"""
    
    def __init__(self, isim, email, telefon):
        self.isim = isim
        self.email = email
        self.telefon = telefon
        self.sepet = []
        self.siparis_gecmisi = []
        self.kayit_tarihi = datetime.datetime.now()
        self.toplam_harcama = 0
    
    def sepete_ekle(self, urun, miktar=1):
        """Sepete ürün ekle"""
        if urun.stok < miktar:
            print(f"Yetersiz stok! {urun.isim} için mevcut stok: {urun.stok}")
            return False
        
        # Sepette zaten var mı kontrol et
        for item in self.sepet:
            if item['urun'].id == urun.id:
                item['miktar'] += miktar
                print(f"{urun.isim} sepetteki miktarı artırıldı: {item['miktar']} adet")
                return True
        
        # Yeni ürün ekle
        self.sepet.append({
            'urun': urun,
            'miktar': miktar,
            'ekleme_tarihi': datetime.datetime.now()
        })
        print(f"{urun.isim} sepete eklendi: {miktar} adet")
        return True
    
    def sepetten_cikar(self, urun_id):
        """Sepetten ürün çıkar"""
        for i, item in enumerate(self.sepet):
            if item['urun'].id == urun_id:
                cikarilan = self.sepet.pop(i)
                print(f"{cikarilan['urun'].isim} sepetten çıkarıldı")
                return True
        
        print("Ürün sepette bulunamadı!")
        return False
    
    def sepeti_goster(self):
        """Sepet içeriğini göster"""
        if not self.sepet:
            print("Sepet boş!")
            return
        
        print(f"\n=== {self.isim} Sepeti ===")
        toplam_tutar = 0
        
        for item in self.sepet:
            urun = item['urun']
            miktar = item['miktar']
            tutar = urun.fiyat * miktar
            toplam_tutar += tutar
            
            print(f"{urun.isim} - {miktar} adet x {urun.fiyat} TL = {tutar} TL")
        
        print(f"Toplam: {toplam_tutar} TL")
        return toplam_tutar
    
    def siparisi_tamamla(self):
        """Siparişi tamamla"""
        if not self.sepet:
            print("Sepet boş! Sipariş verilemez.")
            return False
        
        # Stok kontrolü
        for item in self.sepet:
            if item['urun'].stok < item['miktar']:
                print(f"Stok yetersiz: {item['urun'].isim}")
                return False
        
        # Siparişi oluştur
        siparis = {
            'tarih': datetime.datetime.now(),
            'urunler': self.sepet.copy(),
            'toplam_tutar': 0
        }
        
        # Stokları güncelle ve tutarı hesapla
        toplam_tutar = 0
        for item in self.sepet:
            urun = item['urun']
            miktar = item['miktar']
            
            urun.stok_azalt(miktar)
            tutar = urun.fiyat * miktar
            toplam_tutar += tutar
        
        siparis['toplam_tutar'] = toplam_tutar
        self.siparis_gecmisi.append(siparis)
        self.toplam_harcama += toplam_tutar
        
        print(f"\nSipariş başarıyla tamamlandı!")
        print(f"Sipariş tutarı: {toplam_tutar} TL")
        print(f"Sipariş tarihi: {siparis['tarih'].strftime('%Y-%m-%d %H:%M')}")
        
        # Sepeti temizle
        self.sepet = []
        return True
    
    def siparis_gecmisini_goster(self):
        """Sipariş geçmişini göster"""
        if not self.siparis_gecmisi:
            print("Henüz sipariş verilmemiş.")
            return
        
        print(f"\n=== {self.isim} Sipariş Geçmişi ===")
        for i, siparis in enumerate(self.siparis_gecmisi, 1):
            print(f"\nSipariş {i}:")
            print(f"Tarih: {siparis['tarih'].strftime('%Y-%m-%d %H:%M')}")
            print(f"Toplam Tutar: {siparis['toplam_tutar']} TL")
            print("Ürünler:")
            for item in siparis['urunler']:
                urun = item['urun']
                miktar = item['miktar']
                print(f"  - {urun.isim} x{miktar}")

# E-ticaret sistemi kullanımı
print("E-ticaret sistemi örneği:")

# Ürünler oluştur
laptop = Urun("Gaming Laptop", 15000, "Elektronik", 5)
mouse = Urun("Oyuncu Mouse", 250, "Aksesuar", 20)
klavye = Urun("Mekanik Klavye", 800, "Aksesuar", 15)

# Ürün bilgileri
laptop.urun_detayi()

# Stok işlemleri
laptop.stok_ekle(3)
mouse.stok_azalt(2)

# İncelemeler
laptop.inceleme_ekle(5, "Mükemmel performans!")
laptop.inceleme_ekle(4, "Fiyatına göre iyi")
mouse.inceleme_ekle(4, "Ergonomik ve kullanışlı")

laptop.urun_detayi()

# Müşteri oluştur
musteri1 = Musteri("Ahmet Yılmaz", "ahmet@email.com", "0555-123-4567")

# Alışveriş
musteri1.sepete_ekle(laptop, 1)
musteri1.sepete_ekle(mouse, 2)
musteri1.sepete_ekle(klavye, 1)

musteri1.sepeti_goster()

# Sipariş ver
musteri1.siparisi_tamamla()

# Tekrar alışveriş
musteri1.sepete_ekle(mouse, 3)
musteri1.siparisi_tamamla()

# Geçmiş
musteri1.siparis_gecmisini_goster()

print(f"\nMüşteri toplam harcama: {musteri1.toplam_harcama} TL")

print("\n" + "="*60)
print("OOP TEMELLERİ TAMAMLANDI")
print("="*60)

print("\nKonular Özeti:")
print("1. Class ve Object temelleri")
print("2. Constructor (__init__) kullanımı")
print("3. Instance variables ve methods")
print("4. Class variables ve class methods")
print("5. Static methods")
print("6. Kapsamlı örnek: E-ticaret sistemi")

print("\nBir sonraki dosya: encapsulation_ve_property.py")