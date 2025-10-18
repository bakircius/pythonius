"""
Python Special Methods (Magic Methods) - Comprehensive Guide
Dunder Methods, Object Behavior Customization, Python Data Model

Bu dosyada Python'da özel methodlar (__dunder__ methods), obje davranışlarını
özelleştirme, Python veri modeli ve magic methods detaylı incelenecek.
"""

import copy
import pickle
import json
from typing import Iterator, Any, Optional
from collections.abc import Sequence
import datetime

# =============================================================================
# 1. TEMEL SPECIAL METHODS
# =============================================================================

print("=== Temel Special Methods ===")

class Kitap:
    """Kitap sınıfı - temel special methods"""
    
    def __init__(self, baslik, yazar, sayfa_sayisi, fiyat):
        self.baslik = baslik
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.fiyat = fiyat
        self.okundu = False
    
    def __str__(self):
        """String representation - user-friendly"""
        durum = "✓ Okundu" if self.okundu else "○ Okunmadı"
        return f"'{self.baslik}' - {self.yazar} ({durum})"
    
    def __repr__(self):
        """Official string representation - developer-friendly"""
        return f"Kitap(baslik='{self.baslik}', yazar='{self.yazar}', sayfa_sayisi={self.sayfa_sayisi}, fiyat={self.fiyat})"
    
    def __len__(self):
        """Length support - len(kitap)"""
        return self.sayfa_sayisi
    
    def __bool__(self):
        """Boolean conversion - if kitap:"""
        return self.sayfa_sayisi > 0
    
    def __eq__(self, other):
        """Equality comparison - kitap1 == kitap2"""
        if not isinstance(other, Kitap):
            return False
        return (self.baslik == other.baslik and 
                self.yazar == other.yazar and
                self.sayfa_sayisi == other.sayfa_sayisi)
    
    def __ne__(self, other):
        """Not equal comparison - kitap1 != kitap2"""
        return not self.__eq__(other)
    
    def __lt__(self, other):
        """Less than comparison - kitap1 < kitap2 (sayfa sayısına göre)"""
        if not isinstance(other, Kitap):
            raise TypeError(f"'{type(other).__name__}' object cannot be compared with Kitap")
        return self.sayfa_sayisi < other.sayfa_sayisi
    
    def __le__(self, other):
        """Less than or equal - kitap1 <= kitap2"""
        return self.__lt__(other) or self.__eq__(other)
    
    def __gt__(self, other):
        """Greater than comparison - kitap1 > kitap2"""
        if not isinstance(other, Kitap):
            raise TypeError(f"'{type(other).__name__}' object cannot be compared with Kitap")
        return self.sayfa_sayisi > other.sayfa_sayisi
    
    def __ge__(self, other):
        """Greater than or equal - kitap1 >= kitap2"""
        return self.__gt__(other) or self.__eq__(other)
    
    def __hash__(self):
        """Hash support - set'lerde ve dict key'lerinde kullanım için"""
        return hash((self.baslik, self.yazar, self.sayfa_sayisi))
    
    def oku(self):
        """Kitabı oku"""
        self.okundu = True
        return f"'{self.baslik}' kitabı okundu!"

# Temel special methods kullanımı
print("Temel special methods örnekleri:")

kitap1 = Kitap("1984", "George Orwell", 328, 25.99)
kitap2 = Kitap("Hayvan Çiftliği", "George Orwell", 112, 18.50)
kitap3 = Kitap("1984", "George Orwell", 328, 25.99)  # kitap1 ile aynı

print(f"str(kitap1): {str(kitap1)}")
print(f"repr(kitap1): {repr(kitap1)}")
print(f"len(kitap1): {len(kitap1)} sayfa")
print(f"bool(kitap1): {bool(kitap1)}")

# Karşılaştırma operatörleri
print(f"kitap1 == kitap3: {kitap1 == kitap3}")
print(f"kitap1 == kitap2: {kitap1 == kitap2}")
print(f"kitap1 > kitap2: {kitap1 > kitap2}")  # Sayfa sayısına göre
print(f"kitap1 < kitap2: {kitap1 < kitap2}")

# Hash support
kitap_seti = {kitap1, kitap2, kitap3}
print(f"Set içinde kitap sayısı: {len(kitap_seti)}")  # Duplicate'lar kaldırılır

# =============================================================================
# 2. ARİTMETİK OPERATÖR OVERLOADING
# =============================================================================

print("\n=== Aritmetik Operatör Overloading ===")

class Karmaşık_Sayı:
    """Karmaşık sayı sınıfı - full arithmetic support"""
    
    def __init__(self, gerçek, sanal=0):
        self.gerçek = float(gerçek)
        self.sanal = float(sanal)
    
    def __str__(self):
        """String representation"""
        if self.sanal == 0:
            return f"{self.gerçek}"
        elif self.gerçek == 0:
            return f"{self.sanal}i"
        elif self.sanal > 0:
            return f"{self.gerçek} + {self.sanal}i"
        else:
            return f"{self.gerçek} - {abs(self.sanal)}i"
    
    def __repr__(self):
        return f"Karmaşık_Sayı({self.gerçek}, {self.sanal})"
    
    def __add__(self, other):
        """Addition: z1 + z2"""
        if isinstance(other, Karmaşık_Sayı):
            return Karmaşık_Sayı(self.gerçek + other.gerçek, self.sanal + other.sanal)
        elif isinstance(other, (int, float)):
            return Karmaşık_Sayı(self.gerçek + other, self.sanal)
        else:
            return NotImplemented
    
    def __radd__(self, other):
        """Reverse addition: 5 + z1"""
        return self.__add__(other)
    
    def __sub__(self, other):
        """Subtraction: z1 - z2"""
        if isinstance(other, Karmaşık_Sayı):
            return Karmaşık_Sayı(self.gerçek - other.gerçek, self.sanal - other.sanal)
        elif isinstance(other, (int, float)):
            return Karmaşık_Sayı(self.gerçek - other, self.sanal)
        else:
            return NotImplemented
    
    def __rsub__(self, other):
        """Reverse subtraction: 5 - z1"""
        if isinstance(other, (int, float)):
            return Karmaşık_Sayı(other - self.gerçek, -self.sanal)
        else:
            return NotImplemented
    
    def __mul__(self, other):
        """Multiplication: z1 * z2"""
        if isinstance(other, Karmaşık_Sayı):
            # (a + bi)(c + di) = (ac - bd) + (ad + bc)i
            gerçek = self.gerçek * other.gerçek - self.sanal * other.sanal
            sanal = self.gerçek * other.sanal + self.sanal * other.gerçek
            return Karmaşık_Sayı(gerçek, sanal)
        elif isinstance(other, (int, float)):
            return Karmaşık_Sayı(self.gerçek * other, self.sanal * other)
        else:
            return NotImplemented
    
    def __rmul__(self, other):
        """Reverse multiplication: 5 * z1"""
        return self.__mul__(other)
    
    def __truediv__(self, other):
        """Division: z1 / z2"""
        if isinstance(other, Karmaşık_Sayı):
            if other.gerçek == 0 and other.sanal == 0:
                raise ZeroDivisionError("Karmaşık sayı sıfıra bölünemez")
            
            # (a + bi) / (c + di) = [(a + bi)(c - di)] / (c² + d²)
            payda = other.gerçek**2 + other.sanal**2
            gerçek = (self.gerçek * other.gerçek + self.sanal * other.sanal) / payda
            sanal = (self.sanal * other.gerçek - self.gerçek * other.sanal) / payda
            return Karmaşık_Sayı(gerçek, sanal)
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Sıfıra bölünemez")
            return Karmaşık_Sayı(self.gerçek / other, self.sanal / other)
        else:
            return NotImplemented
    
    def __rtruediv__(self, other):
        """Reverse division: 5 / z1"""
        if isinstance(other, (int, float)):
            return Karmaşık_Sayı(other, 0) / self
        else:
            return NotImplemented
    
    def __pow__(self, other):
        """Power: z1 ** n"""
        if isinstance(other, int):
            if other == 0:
                return Karmaşık_Sayı(1, 0)
            elif other > 0:
                result = Karmaşık_Sayı(1, 0)
                base = Karmaşık_Sayı(self.gerçek, self.sanal)
                for _ in range(other):
                    result = result * base
                return result
            else:
                return Karmaşık_Sayı(1, 0) / (self ** abs(other))
        else:
            return NotImplemented
    
    def __neg__(self):
        """Unary minus: -z1"""
        return Karmaşık_Sayı(-self.gerçek, -self.sanal)
    
    def __pos__(self):
        """Unary plus: +z1"""
        return Karmaşık_Sayı(self.gerçek, self.sanal)
    
    def __abs__(self):
        """Absolute value (magnitude): abs(z1)"""
        return (self.gerçek**2 + self.sanal**2)**0.5
    
    def __eq__(self, other):
        """Equality comparison"""
        if isinstance(other, Karmaşık_Sayı):
            return (abs(self.gerçek - other.gerçek) < 1e-10 and 
                    abs(self.sanal - other.sanal) < 1e-10)
        elif isinstance(other, (int, float)):
            return abs(self.gerçek - other) < 1e-10 and abs(self.sanal) < 1e-10
        return False
    
    def eşlenik(self):
        """Karmaşık eşlenik"""
        return Karmaşık_Sayı(self.gerçek, -self.sanal)
    
    def kutupsal(self):
        """Kutupsal forma çevir (r, θ)"""
        r = abs(self)
        theta = math.atan2(self.sanal, self.gerçek)
        return (r, theta)

# Aritmetik operatör overloading kullanımı
print("Aritmetik operatör overloading örnekleri:")

import math

z1 = Karmaşık_Sayı(3, 4)
z2 = Karmaşık_Sayı(1, -2)

print(f"z1 = {z1}")
print(f"z2 = {z2}")

# Aritmetik işlemler
print(f"z1 + z2 = {z1 + z2}")
print(f"z1 - z2 = {z1 - z2}")
print(f"z1 * z2 = {z1 * z2}")
print(f"z1 / z2 = {z1 / z2}")
print(f"z1 ** 2 = {z1 ** 2}")

# Gerçek sayılarla işlemler
print(f"z1 + 5 = {z1 + 5}")
print(f"5 + z1 = {5 + z1}")
print(f"z1 * 2 = {z1 * 2}")
print(f"10 / z1 = {10 / z1}")

# Unary operatörler
print(f"-z1 = {-z1}")
print(f"+z1 = {+z1}")
print(f"abs(z1) = {abs(z1)}")

# Özel methodlar
print(f"z1 eşlenik = {z1.eşlenik()}")
r, theta = z1.kutupsal()
print(f"z1 kutupsal = ({r:.2f}, {theta:.2f} radyan)")

# =============================================================================
# 3. CONTAINER SPECIAL METHODS
# =============================================================================

print("\n=== Container Special Methods ===")

class Akıllı_Liste:
    """Akıllı liste sınıfı - container protocol implementation"""
    
    def __init__(self, *items):
        self._items = list(items)
        self._access_log = []
    
    def __len__(self):
        """Length support: len(liste)"""
        return len(self._items)
    
    def __getitem__(self, index):
        """Item access: liste[index]"""
        # Erişim logla
        self._access_log.append(('get', index, datetime.datetime.now()))
        
        if isinstance(index, slice):
            return Akıllı_Liste(*self._items[index])
        
        # Negatif index desteği
        if index < 0:
            index = len(self._items) + index
        
        if 0 <= index < len(self._items):
            return self._items[index]
        else:
            raise IndexError(f"Liste index {index} aralık dışı")
    
    def __setitem__(self, index, value):
        """Item assignment: liste[index] = value"""
        self._access_log.append(('set', index, datetime.datetime.now()))
        
        if isinstance(index, slice):
            self._items[index] = value
        else:
            if index < 0:
                index = len(self._items) + index
            
            if 0 <= index < len(self._items):
                self._items[index] = value
            else:
                raise IndexError(f"Liste index {index} aralık dışı")
    
    def __delitem__(self, index):
        """Item deletion: del liste[index]"""
        self._access_log.append(('del', index, datetime.datetime.now()))
        
        if isinstance(index, slice):
            del self._items[index]
        else:
            if index < 0:
                index = len(self._items) + index
            
            if 0 <= index < len(self._items):
                del self._items[index]
            else:
                raise IndexError(f"Liste index {index} aralık dışı")
    
    def __contains__(self, item):
        """Membership test: item in liste"""
        self._access_log.append(('contains', item, datetime.datetime.now()))
        return item in self._items
    
    def __iter__(self):
        """Iterator support: for item in liste"""
        self._access_log.append(('iter', None, datetime.datetime.now()))
        return iter(self._items)
    
    def __reversed__(self):
        """Reverse iterator: reversed(liste)"""
        self._access_log.append(('reversed', None, datetime.datetime.now()))
        return reversed(self._items)
    
    def __str__(self):
        return f"AkıllıListe({self._items})"
    
    def __repr__(self):
        return f"Akıllı_Liste(*{self._items})"
    
    def append(self, item):
        """Element ekleme"""
        self._items.append(item)
        self._access_log.append(('append', item, datetime.datetime.now()))
    
    def remove(self, item):
        """Element kaldırma"""
        self._items.remove(item)
        self._access_log.append(('remove', item, datetime.datetime.now()))
    
    def access_istatistikleri(self):
        """Erişim istatistikleri"""
        print("=== Erişim İstatistikleri ===")
        operasyon_sayaçları = {}
        
        for operasyon, _, _ in self._access_log:
            operasyon_sayaçları[operasyon] = operasyon_sayaçları.get(operasyon, 0) + 1
        
        for operasyon, sayı in operasyon_sayaçları.items():
            print(f"{operasyon}: {sayı} kez")
        
        if self._access_log:
            son_erişim = self._access_log[-1]
            print(f"Son erişim: {son_erişim[0]} - {son_erişim[2].strftime('%H:%M:%S')}")

# Container special methods kullanımı
print("Container special methods örnekleri:")

akıllı_liste = Akıllı_Liste(1, 2, 3, 4, 5)
print(f"Liste: {akıllı_liste}")
print(f"Uzunluk: {len(akıllı_liste)}")

# Index erişimi
print(f"akıllı_liste[0] = {akıllı_liste[0]}")
print(f"akıllı_liste[-1] = {akıllı_liste[-1]}")

# Slicing
print(f"akıllı_liste[1:3] = {akıllı_liste[1:3]}")

# Assignment
akıllı_liste[0] = 10
print(f"[0] = 10 sonrası: {akıllı_liste}")

# Membership
print(f"10 in akıllı_liste: {10 in akıllı_liste}")
print(f"99 in akıllı_liste: {99 in akıllı_liste}")

# Iteration
print("Iteration:")
for item in akıllı_liste:
    print(f"  {item}")

# Reverse iteration
print("Reverse iteration:")
for item in reversed(akıllı_liste):
    print(f"  {item}")

# Element operations
akıllı_liste.append(6)
akıllı_liste.remove(2)
print(f"Son durum: {akıllı_liste}")

# İstatistikler
akıllı_liste.access_istatistikleri()

# =============================================================================
# 4. CONTEXT MANAGER PROTOCOL
# =============================================================================

print("\n=== Context Manager Protocol ===")

class Dosya_Yöneticisi:
    """Custom file manager - context manager protocol"""
    
    def __init__(self, dosya_adı, mod='r', encoding='utf-8'):
        self.dosya_adı = dosya_adı
        self.mod = mod
        self.encoding = encoding
        self.dosya = None
        self.açılma_zamanı = None
        self.kapanma_zamanı = None
        self.hata_oluştu = False
    
    def __enter__(self):
        """Context manager entry"""
        print(f"📂 Dosya açılıyor: {self.dosya_adı}")
        self.açılma_zamanı = datetime.datetime.now()
        
        try:
            self.dosya = open(self.dosya_adı, self.mod, encoding=self.encoding)
            print(f"✅ Dosya başarıyla açıldı")
            return self.dosya
        except Exception as e:
            print(f"❌ Dosya açılamadı: {e}")
            self.hata_oluştu = True
            raise
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Context manager exit"""
        self.kapanma_zamanı = datetime.datetime.now()
        
        if self.dosya:
            self.dosya.close()
            süre = self.kapanma_zamanı - self.açılma_zamanı
            print(f"📁 Dosya kapatıldı. Açık kalma süresi: {süre.total_seconds():.2f} saniye")
        
        if exc_type is not None:
            print(f"⚠️  Context'te hata oluştu: {exc_type.__name__}: {exc_value}")
            self.hata_oluştu = True
            # False döndürmek hatanın yayılmasına izin verir
            return False
        
        print("✅ Context başarıyla tamamlandı")
        return True

class Veritabanı_Bağlantısı:
    """Simulated database connection - advanced context manager"""
    
    def __init__(self, host, port, database):
        self.host = host
        self.port = port
        self.database = database
        self.bağlı = False
        self.transaction_açık = False
        self.sorgular = []
    
    def __enter__(self):
        """Database connection context entry"""
        print(f"🔗 Veritabanına bağlanılıyor: {self.host}:{self.port}/{self.database}")
        
        # Simulated connection
        self.bağlı = True
        print("✅ Veritabanı bağlantısı kuruldu")
        
        # Auto-start transaction
        self.transaction_başlat()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Database connection context exit"""
        if exc_type is not None:
            print(f"❌ Hata nedeniyle transaction geri alınıyor: {exc_type.__name__}")
            self.rollback()
        else:
            print("✅ Transaction commit ediliyor")
            self.commit()
        
        if self.bağlı:
            print("🔌 Veritabanı bağlantısı kapatılıyor")
            self.bağlı = False
        
        return False  # Hataları yayılmasına izin ver
    
    def transaction_başlat(self):
        """Start transaction"""
        self.transaction_açık = True
        print("🔄 Transaction başlatıldı")
    
    def sorgu_çalıştır(self, sql):
        """Execute query"""
        if not self.bağlı:
            raise RuntimeError("Veritabanı bağlantısı yok!")
        
        if not self.transaction_açık:
            raise RuntimeError("Aktif transaction yok!")
        
        print(f"📝 SQL sorgusu: {sql}")
        self.sorgular.append(sql)
        return f"Sorgu sonucu: {len(self.sorgular)} satır etkilendi"
    
    def commit(self):
        """Commit transaction"""
        if self.transaction_açık:
            print(f"💾 {len(self.sorgular)} sorgu commit edildi")
            self.transaction_açık = False
    
    def rollback(self):
        """Rollback transaction"""
        if self.transaction_açık:
            print(f"↩️  {len(self.sorgular)} sorgu geri alındı")
            self.sorgular.clear()
            self.transaction_açık = False

# Context manager protocol kullanımı
print("Context manager protocol örnekleri:")

# Test dosyası oluştur
test_içerik = """Merhaba Dünya!
Bu bir test dosyasıdır.
Context manager ile yönetiliyorum."""

print("1. Dosya Context Manager:")
with Dosya_Yöneticisi('test.txt', 'w') as f:
    f.write(test_içerik)

print("\n2. Dosya okuma:")
with Dosya_Yöneticisi('test.txt', 'r') as f:
    içerik = f.read()
    print(f"Dosya içeriği ({len(içerik)} karakter):")
    print(içerik)

print("\n3. Veritabanı Context Manager:")
with Veritabanı_Bağlantısı('localhost', 5432, 'testdb') as db:
    db.sorgu_çalıştır("CREATE TABLE users (id INT, name VARCHAR(100))")
    db.sorgu_çalıştır("INSERT INTO users VALUES (1, 'Ali')")
    db.sorgu_çalıştır("INSERT INTO users VALUES (2, 'Veli')")

print("\n4. Hatalı context manager:")
try:
    with Veritabanı_Bağlantısı('localhost', 5432, 'testdb') as db:
        db.sorgu_çalıştır("INSERT INTO users VALUES (3, 'Mehmet')")
        raise ValueError("Simulated error!")  # Hata simülasyonu
except ValueError as e:
    print(f"Yakalanan hata: {e}")

# =============================================================================
# 5. COPY VE PICKLE SUPPORT
# =============================================================================

print("\n=== Copy ve Pickle Support ===")

class Kompleks_Nesne:
    """Kompleks nesne - copy ve pickle support"""
    
    def __init__(self, isim, veriler=None):
        self.isim = isim
        self.veriler = veriler or {}
        self.oluşturma_zamanı = datetime.datetime.now()
        self._gizli_veri = "Bu gizli bir veridir"
        self.bağlantılar = []
    
    def __str__(self):
        return f"Kompleks_Nesne(isim='{self.isim}', veri_sayısı={len(self.veriler)})"
    
    def __copy__(self):
        """Shallow copy support"""
        print(f"🔄 Shallow copy oluşturuluyor: {self.isim}")
        yeni_nesne = Kompleks_Nesne(self.isim + "_copy")
        yeni_nesne.veriler = self.veriler  # Shallow copy - aynı dict referansı
        yeni_nesne.oluşturma_zamanı = self.oluşturma_zamanı
        yeni_nesne._gizli_veri = self._gizli_veri
        yeni_nesne.bağlantılar = self.bağlantılar  # Shallow copy
        return yeni_nesne
    
    def __deepcopy__(self, memo):
        """Deep copy support"""
        print(f"🔄 Deep copy oluşturuluyor: {self.isim}")
        yeni_nesne = Kompleks_Nesne(self.isim + "_deepcopy")
        yeni_nesne.veriler = copy.deepcopy(self.veriler, memo)
        yeni_nesne.oluşturma_zamanı = copy.deepcopy(self.oluşturma_zamanı, memo)
        yeni_nesne._gizli_veri = copy.deepcopy(self._gizli_veri, memo)
        yeni_nesne.bağlantılar = copy.deepcopy(self.bağlantılar, memo)
        return yeni_nesne
    
    def __getstate__(self):
        """Pickle serialization preparation"""
        print(f"📦 Pickle state hazırlanıyor: {self.isim}")
        state = self.__dict__.copy()
        # Gizli veriyi pickle'dan çıkar
        del state['_gizli_veri']
        # Zamanı string'e çevir
        state['oluşturma_zamanı'] = state['oluşturma_zamanı'].isoformat()
        return state
    
    def __setstate__(self, state):
        """Pickle deserialization restoration"""
        print(f"📤 Pickle state geri yükleniyor")
        # Zamanı geri çevir
        state['oluşturma_zamanı'] = datetime.datetime.fromisoformat(state['oluşturma_zamanı'])
        self.__dict__.update(state)
        # Gizli veriyi varsayılan değere ayarla
        self._gizli_veri = "Pickle'dan geri yüklendi"
    
    def veri_ekle(self, anahtar, değer):
        """Veri ekleme"""
        self.veriler[anahtar] = değer
    
    def bağlantı_ekle(self, nesne):
        """Bağlantı ekleme"""
        self.bağlantılar.append(nesne)
    
    def bilgi_göster(self):
        """Nesne bilgilerini göster"""
        print(f"  İsim: {self.isim}")
        print(f"  Veri sayısı: {len(self.veriler)}")
        print(f"  Veriler: {self.veriler}")
        print(f"  Oluşturma zamanı: {self.oluşturma_zamanı.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"  Gizli veri: {self._gizli_veri}")
        print(f"  Bağlantı sayısı: {len(self.bağlantılar)}")

# Copy ve Pickle support kullanımı
print("Copy ve Pickle support örnekleri:")

# Orijinal nesne oluştur
orijinal = Kompleks_Nesne("Ana_Nesne")
orijinal.veri_ekle("kullanıcı", "Ali")
orijinal.veri_ekle("yaş", 25)

# Bağlantılı nesne
bağlantılı = Kompleks_Nesne("Bağlantılı_Nesne")
orijinal.bağlantı_ekle(bağlantılı)

print("Orijinal nesne:")
orijinal.bilgi_göster()

print("\n1. Shallow Copy:")
shallow_copy = copy.copy(orijinal)
shallow_copy.bilgi_göster()

# Shallow copy'de orijinal veriye dokunmak
orijinal.veri_ekle("yeni_veri", "test")
print("\nOrijinale veri eklendikten sonra shallow copy:")
shallow_copy.bilgi_göster()  # Aynı dict referansı nedeniyle etkilenir

print("\n2. Deep Copy:")
deep_copy = copy.deepcopy(orijinal)
deep_copy.bilgi_göster()

# Deep copy'ye veri eklemek
deep_copy.veri_ekle("sadece_deep", "deep_copy_verisi")
print("\nDeep copy'ye veri eklendikten sonra orijinal:")
orijinal.bilgi_göster()  # Etkilenmez

print("\n3. Pickle Serialization:")
# Pickle'a kaydet
pickle_data = pickle.dumps(orijinal)
print(f"Pickle boyutu: {len(pickle_data)} byte")

# Pickle'dan yükle
print("\n4. Pickle Deserialization:")
yüklenen = pickle.loads(pickle_data)
yüklenen.bilgi_göster()

# =============================================================================
# 6. ADVANCED SPECIAL METHODS
# =============================================================================

print("\n=== Advanced Special Methods ===")

class Akıllı_Sözlük:
    """Advanced dictionary-like class with special methods"""
    
    def __init__(self, **kwargs):
        self._data = {}
        self._access_count = {}
        self._history = []
        
        for key, value in kwargs.items():
            self[key] = value
    
    def __getitem__(self, key):
        """Item access with tracking"""
        if key not in self._data:
            raise KeyError(f"'{key}' anahtarı bulunamadı")
        
        # Erişim sayısını artır
        self._access_count[key] = self._access_count.get(key, 0) + 1
        
        # Geçmişe ekle
        self._history.append(('get', key, datetime.datetime.now()))
        
        return self._data[key]
    
    def __setitem__(self, key, value):
        """Item assignment with tracking"""
        old_value = self._data.get(key, "YOK")
        self._data[key] = value
        
        # Geçmişe ekle
        action = 'update' if old_value != "YOK" else 'create'
        self._history.append((action, key, datetime.datetime.now()))
        
        print(f"📝 {action.title()}: '{key}' = {value}")
    
    def __delitem__(self, key):
        """Item deletion with tracking"""
        if key not in self._data:
            raise KeyError(f"'{key}' anahtarı bulunamadı")
        
        deleted_value = self._data[key]
        del self._data[key]
        
        # Erişim sayısını da sil
        if key in self._access_count:
            del self._access_count[key]
        
        # Geçmişe ekle
        self._history.append(('delete', key, datetime.datetime.now()))
        print(f"🗑️  Silindi: '{key}' (değer: {deleted_value})")
    
    def __contains__(self, key):
        """Membership test with tracking"""
        result = key in self._data
        self._history.append(('contains', key, datetime.datetime.now()))
        return result
    
    def __len__(self):
        """Length support"""
        return len(self._data)
    
    def __iter__(self):
        """Iterator support"""
        self._history.append(('iter', None, datetime.datetime.now()))
        return iter(self._data)
    
    def __str__(self):
        return f"AkıllıSözlük({dict(self._data)})"
    
    def __repr__(self):
        return f"Akıllı_Sözlük(**{dict(self._data)})"
    
    def __eq__(self, other):
        """Equality comparison"""
        if isinstance(other, Akıllı_Sözlük):
            return self._data == other._data
        elif isinstance(other, dict):
            return self._data == other
        return False
    
    def __or__(self, other):
        """Union operator: sözlük1 | sözlük2"""
        if isinstance(other, (Akıllı_Sözlük, dict)):
            yeni_sözlük = Akıllı_Sözlük(**self._data)
            if isinstance(other, Akıllı_Sözlük):
                yeni_sözlük._data.update(other._data)
            else:
                yeni_sözlük._data.update(other)
            return yeni_sözlük
        return NotImplemented
    
    def __ior__(self, other):
        """In-place union: sözlük1 |= sözlük2"""
        if isinstance(other, (Akıllı_Sözlük, dict)):
            if isinstance(other, Akıllı_Sözlük):
                self._data.update(other._data)
            else:
                self._data.update(other)
            return self
        return NotImplemented
    
    def en_çok_erişilen(self, n=5):
        """En çok erişilen anahtarlar"""
        sorted_keys = sorted(self._access_count.items(), 
                           key=lambda x: x[1], reverse=True)
        return sorted_keys[:n]
    
    def istatistikler(self):
        """Detaylı istatistikler"""
        print("=== Akıllı Sözlük İstatistikleri ===")
        print(f"Toplam anahtar sayısı: {len(self._data)}")
        print(f"Toplam işlem sayısı: {len(self._history)}")
        
        # İşlem türü istatistikleri
        işlem_sayaçları = {}
        for işlem, _, _ in self._history:
            işlem_sayaçları[işlem] = işlem_sayaçları.get(işlem, 0) + 1
        
        print("İşlem türleri:")
        for işlem, sayı in işlem_sayaçları.items():
            print(f"  {işlem}: {sayı}")
        
        # En çok erişilen
        if self._access_count:
            print("En çok erişilen anahtarlar:")
            for key, count in self.en_çok_erişilen():
                print(f"  '{key}': {count} erişim")

# Advanced special methods kullanımı
print("Advanced special methods örnekleri:")

sözlük = Akıllı_Sözlük(isim="Ali", yaş=25, şehir="İstanbul")
print(f"İlk durum: {sözlük}")

# Çeşitli işlemler
print(f"\nİsim: {sözlük['isim']}")  # __getitem__
print(f"Yaş: {sözlük['yaş']}")      # __getitem__ (ikinci kez)
print(f"İsim: {sözlük['isim']}")    # __getitem__ (üçüncü kez)

sözlük['meslek'] = 'Mühendis'        # __setitem__
sözlük['yaş'] = 26                   # __setitem__ (güncelleme)

print(f"'meslek' var mı: {'meslek' in sözlük}")  # __contains__
print(f"Uzunluk: {len(sözlük)}")                 # __len__

# Iteration
print("Anahtarlar:")
for key in sözlük:  # __iter__
    print(f"  {key}")

# Union operations
yeni_veriler = {'telefon': '555-1234', 'email': 'ali@example.com'}
birleşik = sözlük | yeni_veriler  # __or__
print(f"\nBirleşik sözlük: {birleşik}")

sözlük |= {'adres': 'Ankara'}  # __ior__
print(f"In-place union sonrası: {sözlük}")

# Silme işlemi
del sözlük['şehir']  # __delitem__

# İstatistikler
sözlük.istatistikler()

print("\n" + "="*60)
print("SPECIAL METHODS (MAGIC METHODS) TAMAMLANDI")
print("="*60)

print("\nKonular Özeti:")
print("1. Temel Special Methods (__str__, __repr__, __len__, etc.)")
print("2. Aritmetik Operatör Overloading")
print("3. Container Special Methods")
print("4. Context Manager Protocol")
print("5. Copy ve Pickle Support")
print("6. Advanced Special Methods")
print("7. Custom Collections ve Protocols")

print("\nBir sonraki dosya: advanced_oop_patterns.py")