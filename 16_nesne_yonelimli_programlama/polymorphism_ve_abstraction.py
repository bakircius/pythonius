"""
Python Polymorphism ve Abstraction - Comprehensive Guide
Method Overloading, Overriding, Duck Typing, Interfaces, Abstract Classes

Bu dosyada Python'da polimorfizm konseptleri, duck typing, interface design,
abstract sınıflar ve polymorphic behavior patterns detaylı incelenecek.
"""

import datetime
from abc import ABC, abstractmethod
from typing import Protocol, List, Optional, Union, Any
import math

# =============================================================================
# 1. TEMEL POLİMORFİZM (BASIC POLYMORPHISM)
# =============================================================================

print("=== Temel Polimorfizm (Basic Polymorphism) ===")

class Geometrik_Sekil:
    """Geometrik şekil base class"""
    
    def __init__(self, isim):
        self.isim = isim
        self.renk = "Beyaz"
    
    def alan_hesapla(self):
        """Base implementation - override edilecek"""
        return 0
    
    def bilgi_ver(self):
        """Genel bilgi verme"""
        return f"{self.isim} - Renk: {self.renk}, Alan: {self.alan_hesapla()}"
    
    def ciz(self):
        """Çizim methodu - override edilecek"""
        return f"{self.isim} çiziliyor..."

class Kare(Geometrik_Sekil):
    """Kare sınıfı - polimorfik davranış"""
    
    def __init__(self, kenar):
        super().__init__("Kare")
        self.kenar = kenar
    
    def alan_hesapla(self):
        """Kare alan hesaplama - polymorphic override"""
        return self.kenar ** 2
    
    def ciz(self):
        """Kare çizimi - polymorphic override"""
        return f"{self.kenar}x{self.kenar} boyutunda kare çiziliyor"

class Daire(Geometrik_Sekil):
    """Daire sınıfı - polimorfik davranış"""
    
    def __init__(self, yaricap):
        super().__init__("Daire")
        self.yaricap = yaricap
    
    def alan_hesapla(self):
        """Daire alan hesaplama - polymorphic override"""
        return math.pi * (self.yaricap ** 2)
    
    def ciz(self):
        """Daire çizimi - polymorphic override"""
        return f"Yarıçapı {self.yaricap} olan daire çiziliyor"

class Ucgen(Geometrik_Sekil):
    """Üçgen sınıfı - polimorfik davranış"""
    
    def __init__(self, taban, yukseklik):
        super().__init__("Üçgen")
        self.taban = taban
        self.yukseklik = yukseklik
    
    def alan_hesapla(self):
        """Üçgen alan hesaplama - polymorphic override"""
        return (self.taban * self.yukseklik) / 2
    
    def ciz(self):
        """Üçgen çizimi - polymorphic override"""
        return f"Tabanı {self.taban}, yüksekliği {self.yukseklik} olan üçgen çiziliyor"

def sekilleri_islem(sekiller):
    """Polymorphic function - farklı şekil tiplerini aynı şekilde işler"""
    print("=== Şekil İşleme (Polymorphic Behavior) ===")
    toplam_alan = 0
    
    for sekil in sekiller:
        print(f"{sekil.bilgi_ver()}")
        print(f"  {sekil.ciz()}")
        toplam_alan += sekil.alan_hesapla()
        print()
    
    print(f"Toplam Alan: {toplam_alan:.2f}")
    return toplam_alan

# Temel polimorfizm kullanımı
print("Temel polimorfizm örnekleri:")

# Farklı şekil nesneleri
sekiller = [
    Kare(5),
    Daire(3),
    Ucgen(4, 6),
    Kare(3),
    Daire(2)
]

# Tüm şekilleri aynı interface ile işle
sekilleri_islem(sekiller)

# =============================================================================
# 2. DUCK TYPING
# =============================================================================

print("\n=== Duck Typing ===")

class Ördek:
    """Ördek sınıfı - duck typing örneği"""
    
    def __init__(self, isim):
        self.isim = isim
    
    def ses_cikar(self):
        return f"{self.isim} vaklıyor: Vak vak!"
    
    def yürü(self):
        return f"{self.isim} yürüyor"
    
    def yüz(self):
        return f"{self.isim} yüzüyor"

class Robot_Ördek:
    """Robot ördek - aynı interface, farklı implementation"""
    
    def __init__(self, model):
        self.model = model
        self.batarya = 100
    
    def ses_cikar(self):
        if self.batarya > 0:
            self.batarya -= 1
            return f"{self.model} robot ördek ses çıkarıyor: BEEP BEEP!"
        return f"{self.model} bataryası bitti!"
    
    def yürü(self):
        if self.batarya > 5:
            self.batarya -= 5
            return f"{self.model} mekanik ayaklarla yürüyor"
        return f"{self.model} yürüyecek bataryası yok!"
    
    def yüz(self):
        if self.batarya > 10:
            self.batarya -= 10
            return f"{self.model} pervane ile yüzüyor"
        return f"{self.model} yüzecek bataryası yok!"

class Oyuncak_Ördek:
    """Oyuncak ördek - sadece ses çıkarır"""
    
    def __init__(self, renk):
        self.renk = renk
    
    def ses_cikar(self):
        return f"{self.renk} oyuncak ördek sıkıştırıldı: Cık cık!"
    
    def yürü(self):
        return f"{self.renk} oyuncak ördek hareket edemez!"
    
    def yüz(self):
        return f"{self.renk} oyuncak ördek suda yüzer!"

def ordek_aktiviteleri(ordek_listesi):
    """Duck typing - tip kontrolü yapmadan interface kullanımı"""
    print("=== Ördek Aktiviteleri (Duck Typing) ===")
    
    for ordek in ordek_listesi:
        print(f"--- {getattr(ordek, 'isim', getattr(ordek, 'model', getattr(ordek, 'renk', 'Bilinmeyen')))} ---")
        
        # Duck typing - eğer method varsa çalıştır
        if hasattr(ordek, 'ses_cikar'):
            print(ordek.ses_cikar())
        
        if hasattr(ordek, 'yürü'):
            print(ordek.yürü())
        
        if hasattr(ordek, 'yüz'):
            print(ordek.yüz())
        
        print()

# Duck typing kullanımı
print("Duck typing örnekleri:")

ordekler = [
    Ördek("Donald"),
    Robot_Ördek("RoboDuck-3000"),
    Oyuncak_Ördek("Sarı")
]

ordek_aktiviteleri(ordekler)

# =============================================================================
# 3. OPERATOR OVERLOADING (POLİMORFİK OPERATÖRLER)
# =============================================================================

print("\n=== Operator Overloading (Polimorfik Operatörler) ===")

class Vektor:
    """Vektör sınıfı - operator overloading örneği"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """String representation"""
        return f"Vektor({self.x}, {self.y})"
    
    def __repr__(self):
        """Developer representation"""
        return f"Vektor(x={self.x}, y={self.y})"
    
    def __add__(self, other):
        """Toplama operatörü overload (+)"""
        if isinstance(other, Vektor):
            return Vektor(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Vektor(self.x + other, self.y + other)
        else:
            raise TypeError(f"Vektor ile {type(other)} toplanamaz")
    
    def __radd__(self, other):
        """Reverse addition (sayı + vektor)"""
        return self.__add__(other)
    
    def __sub__(self, other):
        """Çıkarma operatörü overload (-)"""
        if isinstance(other, Vektor):
            return Vektor(self.x - other.x, self.y - other.y)
        elif isinstance(other, (int, float)):
            return Vektor(self.x - other, self.y - other)
        else:
            raise TypeError(f"Vektor'den {type(other)} çıkarılamaz")
    
    def __mul__(self, other):
        """Çarpma operatörü overload (*)"""
        if isinstance(other, (int, float)):
            # Skaler çarpım
            return Vektor(self.x * other, self.y * other)
        elif isinstance(other, Vektor):
            # Nokta çarpım
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError(f"Vektor ile {type(other)} çarpılamaz")
    
    def __rmul__(self, other):
        """Reverse multiplication (sayı * vektor)"""
        return self.__mul__(other)
    
    def __truediv__(self, other):
        """Bölme operatörü overload (/)"""
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Vektör sıfıra bölünemez")
            return Vektor(self.x / other, self.y / other)
        else:
            raise TypeError(f"Vektor {type(other)} ile bölünemez")
    
    def __eq__(self, other):
        """Eşitlik operatörü overload (==)"""
        if isinstance(other, Vektor):
            return self.x == other.x and self.y == other.y
        return False
    
    def __ne__(self, other):
        """Eşitsizlik operatörü overload (!=)"""
        return not self.__eq__(other)
    
    def __lt__(self, other):
        """Küçüktür operatörü overload (<) - magnitude karşılaştırması"""
        if isinstance(other, Vektor):
            return self.magnitude() < other.magnitude()
        raise TypeError(f"Vektor ile {type(other)} karşılaştırılamaz")
    
    def __le__(self, other):
        """Küçük eşit operatörü overload (<=)"""
        return self.__lt__(other) or self.__eq__(other)
    
    def __gt__(self, other):
        """Büyüktür operatörü overload (>)"""
        if isinstance(other, Vektor):
            return self.magnitude() > other.magnitude()
        raise TypeError(f"Vektor ile {type(other)} karşılaştırılamaz")
    
    def __ge__(self, other):
        """Büyük eşit operatörü overload (>=)"""
        return self.__gt__(other) or self.__eq__(other)
    
    def __len__(self):
        """Uzunluk operatörü overload (len())"""
        return int(self.magnitude())
    
    def __abs__(self):
        """Mutlak değer operatörü overload (abs())"""
        return self.magnitude()
    
    def __neg__(self):
        """Negatif operatör overload (-vector)"""
        return Vektor(-self.x, -self.y)
    
    def __bool__(self):
        """Boolean dönüşüm (if vector:)"""
        return self.x != 0 or self.y != 0
    
    def magnitude(self):
        """Vektör büyüklüğü"""
        return math.sqrt(self.x**2 + self.y**2)
    
    def normalize(self):
        """Vektörü normalize et"""
        mag = self.magnitude()
        if mag == 0:
            return Vektor(0, 0)
        return Vektor(self.x / mag, self.y / mag)

# Operator overloading kullanımı
print("Operator overloading örnekleri:")

v1 = Vektor(3, 4)
v2 = Vektor(1, 2)

print(f"v1 = {v1}")
print(f"v2 = {v2}")

# Aritmetik operatörler
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 2 = {v1 * 2}")
print(f"3 * v1 = {3 * v1}")
print(f"v1 * v2 = {v1 * v2}")  # Nokta çarpım
print(f"v1 / 2 = {v1 / 2}")

# Karşılaştırma operatörleri
print(f"v1 == v2: {v1 == v2}")
print(f"v1 > v2: {v1 > v2}")
print(f"v1 < v2: {v1 < v2}")

# Unary operatörler
print(f"-v1 = {-v1}")
print(f"abs(v1) = {abs(v1)}")
print(f"len(v1) = {len(v1)}")

# Boolean test
if v1:
    print("v1 sıfır vektör değil")

# =============================================================================
# 4. INTERFACE DESIGN VE PROTOCOLS
# =============================================================================

print("\n=== Interface Design ve Protocols ===")

class Cizilir(Protocol):
    """Drawing protocol - interface definition"""
    
    def ciz(self) -> str:
        """Çizim methodu - implement edilmeli"""
        ...
    
    def temizle(self) -> str:
        """Temizleme methodu - implement edilmeli"""
        ...

class Renklendirilir(Protocol):
    """Coloring protocol"""
    
    def renk_degistir(self, renk: str) -> str:
        """Renk değiştirme methodu"""
        ...

class Hareket_Edebilir(Protocol):
    """Movement protocol"""
    
    def hareket_et(self, x: int, y: int) -> str:
        """Hareket methodu"""
        ...

class Grafik_Nesne:
    """Grafik nesnesi - multiple protocols implementation"""
    
    def __init__(self, isim: str, x: int = 0, y: int = 0):
        self.isim = isim
        self.x = x
        self.y = y
        self.renk = "Siyah"
        self.gorünür = True
    
    def ciz(self) -> str:
        """Cizilir protocol implementation"""
        if self.gorünür:
            return f"{self.isim} ({self.x}, {self.y}) konumunda {self.renk} renkte çizildi"
        return f"{self.isim} görünür değil"
    
    def temizle(self) -> str:
        """Cizilir protocol implementation"""
        return f"{self.isim} temizlendi"
    
    def renk_degistir(self, renk: str) -> str:
        """Renklendirilir protocol implementation"""
        eski_renk = self.renk
        self.renk = renk
        return f"{self.isim} rengi {eski_renk}'den {renk}'e değişti"
    
    def hareket_et(self, x: int, y: int) -> str:
        """Hareket_Edebilir protocol implementation"""
        eski_x, eski_y = self.x, self.y
        self.x = x
        self.y = y
        return f"{self.isim} ({eski_x}, {eski_y})'den ({x}, {y})'ye hareket etti"
    
    def gizle(self):
        """Ek fonksiyon"""
        self.gorünür = False
        return f"{self.isim} gizlendi"
    
    def göster(self):
        """Ek fonksiyon"""
        self.gorünür = True
        return f"{self.isim} gösterildi"

class Canva:
    """Canvas sınıfı - protocol kullanan"""
    
    def __init__(self, genişlik: int, yükseklik: int):
        self.genişlik = genişlik
        self.yükseklik = yükseklik
        self.nesneler: List[Grafik_Nesne] = []
    
    def nesne_ekle(self, nesne: Grafik_Nesne):
        """Canvas'a nesne ekleme"""
        self.nesneler.append(nesne)
        return f"{nesne.isim} canvas'a eklendi"
    
    def tümünü_çiz(self):
        """Tüm nesneleri çiz - Cizilir protocol kullanımı"""
        print("=== Canvas Çizimi ===")
        for nesne in self.nesneler:
            print(nesne.ciz())
    
    def tümünü_temizle(self):
        """Tüm nesneleri temizle"""
        print("=== Canvas Temizliği ===")
        for nesne in self.nesneler:
            print(nesne.temizle())
    
    def toplu_renk_degistir(self, renk: str):
        """Tüm nesnelerin rengini değiştir - Renklendirilir protocol"""
        print(f"=== Toplu Renk Değiştirme: {renk} ===")
        for nesne in self.nesneler:
            print(nesne.renk_degistir(renk))
    
    def toplu_hareket(self, dx: int, dy: int):
        """Tüm nesneleri hareket ettir - Hareket_Edebilir protocol"""
        print(f"=== Toplu Hareket: ({dx}, {dy}) ===")
        for nesne in self.nesneler:
            yeni_x = nesne.x + dx
            yeni_y = nesne.y + dy
            print(nesne.hareket_et(yeni_x, yeni_y))

# Protocol ve interface kullanımı
print("Protocol ve interface örnekleri:")

canvas = Canva(800, 600)

# Grafik nesneleri oluştur
nesneler = [
    Grafik_Nesne("Kare1", 10, 10),
    Grafik_Nesne("Daire1", 50, 50),
    Grafik_Nesne("Üçgen1", 100, 100)
]

# Canvas'a ekle
for nesne in nesneler:
    print(canvas.nesne_ekle(nesne))

print()

# Protocol methodlarını kullan
canvas.tümünü_çiz()
print()

canvas.toplu_renk_degistir("Kırmızı")
print()

canvas.toplu_hareket(20, 30)
print()

canvas.tümünü_çiz()

# =============================================================================
# 5. ABSTRACT FACTORY PATTERN
# =============================================================================

print("\n=== Abstract Factory Pattern ===")

class UI_Elementi(ABC):
    """UI elementi abstract base class"""
    
    def __init__(self, label: str):
        self.label = label
    
    @abstractmethod
    def render(self) -> str:
        """Render methodu - abstract"""
        pass
    
    @abstractmethod
    def handle_click(self) -> str:
        """Click handler - abstract"""
        pass

class Windows_Button(UI_Elementi):
    """Windows button implementation"""
    
    def render(self) -> str:
        return f"Windows button: [{self.label}] rendered"
    
    def handle_click(self) -> str:
        return f"Windows button '{self.label}' clicked with mouse"

class Mac_Button(UI_Elementi):
    """Mac button implementation"""
    
    def render(self) -> str:
        return f"Mac button: 〈{self.label}〉 rendered"
    
    def handle_click(self) -> str:
        return f"Mac button '{self.label}' clicked with trackpad"

class Linux_Button(UI_Elementi):
    """Linux button implementation"""
    
    def render(self) -> str:
        return f"Linux button: |{self.label}| rendered"
    
    def handle_click(self) -> str:
        return f"Linux button '{self.label}' clicked with various input devices"

class UI_Factory(ABC):
    """Abstract UI factory"""
    
    @abstractmethod
    def create_button(self, label: str) -> UI_Elementi:
        """Button oluşturma - abstract"""
        pass
    
    @abstractmethod
    def get_theme_name(self) -> str:
        """Tema adı - abstract"""
        pass

class Windows_Factory(UI_Factory):
    """Windows UI factory"""
    
    def create_button(self, label: str) -> UI_Elementi:
        return Windows_Button(label)
    
    def get_theme_name(self) -> str:
        return "Windows Modern"

class Mac_Factory(UI_Factory):
    """Mac UI factory"""
    
    def create_button(self, label: str) -> UI_Elementi:
        return Mac_Button(label)
    
    def get_theme_name(self) -> str:
        return "macOS Big Sur"

class Linux_Factory(UI_Factory):
    """Linux UI factory"""
    
    def create_button(self, label: str) -> UI_Elementi:
        return Linux_Button(label)
    
    def get_theme_name(self) -> str:
        return "GNOME Modern"

class Uygulama:
    """Application class - factory pattern kullanımı"""
    
    def __init__(self, factory: UI_Factory):
        self.factory = factory
        self.ui_elemanlari: List[UI_Elementi] = []
    
    def create_interface(self):
        """Interface oluşturma"""
        # Polymorphic factory kullanımı
        buttons = [
            self.factory.create_button("OK"),
            self.factory.create_button("Cancel"),
            self.factory.create_button("Apply"),
            self.factory.create_button("Help")
        ]
        
        self.ui_elemanlari.extend(buttons)
        
        print(f"=== {self.factory.get_theme_name()} Teması ile Interface ===")
        for element in self.ui_elemanlari:
            print(element.render())
    
    def simulate_clicks(self):
        """Click simülasyonu"""
        print("\n=== Click Simülasyonu ===")
        for element in self.ui_elemanlari:
            print(element.handle_click())

def create_app_for_platform(platform: str) -> Uygulama:
    """Platform'a göre uygulama oluştur - polymorphic factory selection"""
    factories = {
        "windows": Windows_Factory(),
        "mac": Mac_Factory(),
        "linux": Linux_Factory()
    }
    
    factory = factories.get(platform.lower())
    if not factory:
        raise ValueError(f"Desteklenmeyen platform: {platform}")
    
    return Uygulama(factory)

# Abstract Factory Pattern kullanımı
print("Abstract Factory Pattern örnekleri:")

platforms = ["Windows", "Mac", "Linux"]

for platform in platforms:
    print(f"\n{'='*50}")
    print(f"Platform: {platform}")
    print('='*50)
    
    app = create_app_for_platform(platform)
    app.create_interface()
    app.simulate_clicks()

# =============================================================================
# 6. POLYMORPHİC COLLECTİONS VE ADVANCED PATTERNS
# =============================================================================

print("\n=== Polymorphic Collections ve Advanced Patterns ===")

class Medya_Player(ABC):
    """Media player abstract base"""
    
    def __init__(self, dosya_adi: str):
        self.dosya_adi = dosya_adi
        self.oynatiliyor = False
        self.pozisyon = 0
        self.süre = 0
    
    @abstractmethod
    def oynat(self) -> str:
        """Oynatma - abstract"""
        pass
    
    @abstractmethod
    def durdur(self) -> str:
        """Durdurma - abstract"""
        pass
    
    @abstractmethod
    def get_format(self) -> str:
        """Format bilgisi - abstract"""
        pass
    
    def pozisyon_goster(self) -> str:
        """Pozisyon bilgisi"""
        dakika = self.pozisyon // 60
        saniye = self.pozisyon % 60
        return f"{dakika:02d}:{saniye:02d}"

class MP3_Player(Medya_Player):
    """MP3 player implementation"""
    
    def __init__(self, dosya_adi: str, süre: int = 180):
        super().__init__(dosya_adi)
        self.süre = süre
        self.kalite = "128kbps"
    
    def oynat(self) -> str:
        self.oynatiliyor = True
        return f"🎵 MP3 oynatılıyor: {self.dosya_adi} ({self.kalite})"
    
    def durdur(self) -> str:
        self.oynatiliyor = False
        return f"⏹️ MP3 durduruldu: {self.dosya_adi}"
    
    def get_format(self) -> str:
        return "MP3"

class Video_Player(Medya_Player):
    """Video player implementation"""
    
    def __init__(self, dosya_adi: str, süre: int = 300):
        super().__init__(dosya_adi)
        self.süre = süre
        self.çözünürlük = "1920x1080"
    
    def oynat(self) -> str:
        self.oynatiliyor = True
        return f"🎬 Video oynatılıyor: {self.dosya_adi} ({self.çözünürlük})"
    
    def durdur(self) -> str:
        self.oynatiliyor = False
        return f"⏹️ Video durduruldu: {self.dosya_adi}"
    
    def get_format(self) -> str:
        return "MP4"

class Podcast_Player(Medya_Player):
    """Podcast player implementation"""
    
    def __init__(self, dosya_adi: str, süre: int = 1800):
        super().__init__(dosya_adi)
        self.süre = süre
        self.hız = 1.0  # Oynatma hızı
    
    def oynat(self) -> str:
        self.oynatiliyor = True
        return f"🎙️ Podcast oynatılıyor: {self.dosya_adi} ({self.hız}x hız)"
    
    def durdur(self) -> str:
        self.oynatiliyor = False
        return f"⏹️ Podcast durduruldu: {self.dosya_adi}"
    
    def get_format(self) -> str:
        return "Podcast"
    
    def hız_degistir(self, yeni_hız: float):
        """Podcast'e özel özellik"""
        self.hız = yeni_hız
        return f"Oynatma hızı {yeni_hız}x olarak ayarlandı"

class Medya_Kütüphane:
    """Polymorphic media library"""
    
    def __init__(self):
        self.medyalar: List[Medya_Player] = []
        self.çalma_listesi: List[Medya_Player] = []
        self.mevcut_index = 0
    
    def medya_ekle(self, medya: Medya_Player):
        """Medya ekleme"""
        self.medyalar.append(medya)
        return f"Eklendi: {medya.dosya_adi} ({medya.get_format()})"
    
    def tüm_medyaları_listele(self):
        """Tüm medyaları listele - polymorphic iteration"""
        print("=== Medya Kütüphanesi ===")
        for i, medya in enumerate(self.medyalar, 1):
            durum = "▶️" if medya.oynatiliyor else "⏸️"
            print(f"{i}. {durum} {medya.dosya_adi} ({medya.get_format()}) - {medya.pozisyon_goster()}")
    
    def çalma_listesi_oluştur(self, indices: List[int]):
        """Çalma listesi oluşturma"""
        self.çalma_listesi = []
        for index in indices:
            if 0 <= index < len(self.medyalar):
                self.çalma_listesi.append(self.medyalar[index])
        
        print(f"Çalma listesi oluşturuldu: {len(self.çalma_listesi)} öğe")
    
    def çalma_listesi_oynat(self):
        """Çalma listesi oynatma - polymorphic behavior"""
        if not self.çalma_listesi:
            return "Çalma listesi boş!"
        
        print("=== Çalma Listesi Oynatılıyor ===")
        for medya in self.çalma_listesi:
            print(medya.oynat())
            
            # Özel davranışlar (instanceof checks yerine duck typing)
            if hasattr(medya, 'hız') and hasattr(medya, 'hız_degistir'):
                print(f"  (Podcast için 1.5x hız ayarlandı)")
            
            # Simüle edilmiş oynatma
            import time
            time.sleep(0.5)  # Kısa bekleme
            
            print(medya.durdur())
            print("  Sonraki medyaya geçiliyor...\n")
    
    def format_istatistikleri(self):
        """Format istatistikleri - polymorphic data processing"""
        format_sayaçları = {}
        
        for medya in self.medyalar:
            format_tipi = medya.get_format()
            format_sayaçları[format_tipi] = format_sayaçları.get(format_tipi, 0) + 1
        
        print("=== Format İstatistikleri ===")
        for format_tipi, sayi in format_sayaçları.items():
            print(f"{format_tipi}: {sayi} dosya")

# Polymorphic collections kullanımı
print("Polymorphic collections örnekleri:")

kütüphane = Medya_Kütüphane()

# Farklı medya tiplerini ekle
medyalar = [
    MP3_Player("Shape of You.mp3", 180),
    Video_Player("Avengers Endgame.mp4", 7200),
    Podcast_Player("Tech Talk Episode 1.mp3", 2400),
    MP3_Player("Bohemian Rhapsody.mp3", 355),
    Video_Player("Python Tutorial.mp4", 1800),
    Podcast_Player("History Podcast.mp3", 3000)
]

for medya in medyalar:
    print(kütüphane.medya_ekle(medya))

print()

# Polymorphic operations
kütüphane.tüm_medyaları_listele()
print()

kütüphane.format_istatistikleri()
print()

# Çalma listesi oluştur ve oynat
kütüphane.çalma_listesi_oluştur([0, 2, 4])  # MP3, Podcast, Video
kütüphane.çalma_listesi_oynat()

print("\n" + "="*60)
print("POLYMORPHİSM VE ABSTRACTION TAMAMLANDI")
print("="*60)

print("\nKonular Özeti:")
print("1. Temel Polimorfizm (Method Overriding)")
print("2. Duck Typing")
print("3. Operator Overloading")
print("4. Interface Design ve Protocols")
print("5. Abstract Factory Pattern")
print("6. Polymorphic Collections")
print("7. Advanced Polymorphic Patterns")

print("\nBir sonraki dosya: special_methods_magic.py")