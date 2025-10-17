"""
Python Type Hints ve Annotations - Comprehensive Guide

Bu dosyada Python type hints, type annotations ve modern tip sistemi
derinlemesine incelenecek. mypy ile tip kontrolü ve gelişmiş typing kullanımı.
"""

from typing import (
    List, Dict, Tuple, Set, Optional, Union, Any, Callable, TypeVar, Generic,
    Protocol, Literal, Final, ClassVar, overload, cast, TYPE_CHECKING
)
from typing_extensions import NotRequired, Required, TypedDict
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
import json

# =============================================================================
# 1. TEMEL TYPE HINTS
# =============================================================================

print("=== Temel Type Hints ===")

def selamla(isim: str) -> str:
    """Basit type hints örneği"""
    return f"Merhaba {isim}!"

def topla(a: int, b: int) -> int:
    """İki sayıyı toplayan fonksiyon"""
    return a + b

def ortalama_hesapla(sayilar: List[int]) -> float:
    """Liste ortalaması hesaplayan fonksiyon"""
    if not sayilar:
        return 0.0
    return sum(sayilar) / len(sayilar)

# Temel kullanım örnekleri
print(selamla("Ahmet"))
print(f"Toplam: {topla(5, 3)}")
print(f"Ortalama: {ortalama_hesapla([1, 2, 3, 4, 5])}")

# Değişken annotations
yas: int = 25
isim: str = "Ali"
aktif_mi: bool = True
notlar: List[float] = [85.5, 92.0, 78.5]

print(f"\nDeğişkenler: {isim} ({yas}) - Aktif: {aktif_mi}")
print(f"Notlar: {notlar}")

# =============================================================================
# 2. COMPLEX TYPE ANNOTATIONS
# =============================================================================

print("\n=== Complex Type Annotations ===")

# Dict annotations
ogrenci_notlari: Dict[str, List[float]] = {
    "Matematik": [85, 90, 88],
    "Fizik": [78, 82, 85],
    "Kimya": [92, 95, 90]
}

def ders_ortalamasi(notlar: Dict[str, List[float]]) -> Dict[str, float]:
    """Her ders için ortalama hesaplar"""
    return {
        ders: sum(ders_notlari) / len(ders_notlari) 
        for ders, ders_notlari in notlar.items()
    }

# Tuple annotations
koordinat: Tuple[float, float] = (3.14, 2.71)
rgb_renk: Tuple[int, int, int] = (255, 128, 0)

def mesafe_hesapla(p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
    """İki nokta arası mesafe hesaplar"""
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

# Set annotations
benzersiz_kelimeler: Set[str] = {"python", "programlama", "tip", "annotations"}

def kelime_analizi(metin: str) -> Set[str]:
    """Metindeki benzersiz kelimeleri döndürür"""
    return set(metin.lower().split())

print("Ders ortalamaları:", ders_ortalamasi(ogrenci_notlari))
print(f"Mesafe: {mesafe_hesapla((0, 0), (3, 4))}")
print(f"Kelime analizi: {kelime_analizi('Python çok güçlü bir programlama dili')}")

# =============================================================================
# 3. OPTIONAL VE UNION TYPES
# =============================================================================

print("\n=== Optional ve Union Types ===")

def kullanici_bul(kullanici_id: int) -> Optional[Dict[str, str]]:
    """Kullanıcı bulur, bulamazsa None döndürür"""
    kullanicilar = {
        1: {"isim": "Ali", "email": "ali@example.com"},
        2: {"isim": "Ayşe", "email": "ayse@example.com"}
    }
    return kullanicilar.get(kullanici_id)

def veri_isle(veri: Union[str, int, float]) -> str:
    """Farklı tiplerdeki veriyi işler"""
    if isinstance(veri, str):
        return f"String: {veri.upper()}"
    elif isinstance(veri, int):
        return f"Integer: {veri * 2}"
    elif isinstance(veri, float):
        return f"Float: {veri:.2f}"
    else:
        return "Bilinmeyen tip"

def dosya_oku(dosya_yolu: str, encoding: Optional[str] = None) -> str:
    """Dosya okur, encoding isteğe bağlı"""
    encoding = encoding or 'utf-8'
    try:
        with open(dosya_yolu, 'r', encoding=encoding) as f:
            return f.read()
    except FileNotFoundError:
        return ""

# Optional ve Union kullanımı
kullanici = kullanici_bul(1)
if kullanici:
    print(f"Kullanıcı bulundu: {kullanici['isim']}")

print(veri_isle("hello"))
print(veri_isle(42))
print(veri_isle(3.14159))

# =============================================================================
# 4. CALLABLE TYPE ANNOTATIONS
# =============================================================================

print("\n=== Callable Type Annotations ===")

def isle_ve_cagir(sayilar: List[int], islem: Callable[[int], int]) -> List[int]:
    """Liste elemanlarına işlem uygular"""
    return [islem(sayi) for sayi in sayilar]

def filtrele_ve_isle(
    sayilar: List[int], 
    filtre: Callable[[int], bool],
    donusturucu: Callable[[int], str]
) -> List[str]:
    """Filtreler ve dönüştürür"""
    return [donusturucu(sayi) for sayi in sayilar if filtre(sayi)]

# Higher-order function type
def decorator_fabrika(mesaj: str) -> Callable[[Callable], Callable]:
    """Decorator üreten fonksiyon"""
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            print(f"[{mesaj}] {func.__name__} çalıştırılıyor...")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Callable kullanım örnekleri
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

kareler = isle_ve_cagir(sayilar, lambda x: x**2)
print(f"Kareler: {kareler}")

cift_sayilar_str = filtrele_ve_isle(
    sayilar,
    lambda x: x % 2 == 0,  # çift sayı filtresi
    lambda x: f"sayi_{x}"   # string dönüştürücü
)
print(f"Çift sayılar (str): {cift_sayilar_str}")

@decorator_fabrika("DEBUG")
def test_fonksiyon():
    return "Test sonucu"

print(test_fonksiyon())

# =============================================================================
# 5. GENERIC TYPES VE TYPEVAR
# =============================================================================

print("\n=== Generic Types ve TypeVar ===")

T = TypeVar('T')
K = TypeVar('K')
V = TypeVar('V')

def ilk_eleman(liste: List[T]) -> Optional[T]:
    """Listenin ilk elemanını döndürür"""
    return liste[0] if liste else None

def son_eleman(liste: List[T]) -> Optional[T]:
    """Listenin son elemanını döndürür"""
    return liste[-1] if liste else None

def ters_cevir(liste: List[T]) -> List[T]:
    """Listeyi tersine çevirir"""
    return liste[::-1]

class Stack(Generic[T]):
    """Generic stack implementation"""
    
    def __init__(self) -> None:
        self._items: List[T] = []
    
    def push(self, item: T) -> None:
        """Eleman ekler"""
        self._items.append(item)
    
    def pop(self) -> Optional[T]:
        """Eleman çıkarır"""
        return self._items.pop() if self._items else None
    
    def peek(self) -> Optional[T]:
        """En üstteki elemana bakar"""
        return self._items[-1] if self._items else None
    
    def is_empty(self) -> bool:
        """Stack boş mu kontrol eder"""
        return len(self._items) == 0
    
    def size(self) -> int:
        """Stack boyutunu döndürür"""
        return len(self._items)

# Generic kullanım örnekleri
str_liste = ["a", "b", "c", "d"]
int_liste = [1, 2, 3, 4, 5]

print(f"İlk string: {ilk_eleman(str_liste)}")
print(f"Son integer: {son_eleman(int_liste)}")
print(f"Ters string liste: {ters_cevir(str_liste)}")

# Generic Stack kullanımı
int_stack: Stack[int] = Stack()
int_stack.push(1)
int_stack.push(2)
int_stack.push(3)

print(f"Stack boyutu: {int_stack.size()}")
print(f"En üstteki: {int_stack.peek()}")
print(f"Pop: {int_stack.pop()}")

str_stack: Stack[str] = Stack()
str_stack.push("hello")
str_stack.push("world")

print(f"String stack: {str_stack.peek()}")

# =============================================================================
# 6. PROTOCOL VE STRUCTURAL TYPING
# =============================================================================

print("\n=== Protocol ve Structural Typing ===")

class Drawable(Protocol):
    """Çizilebilir nesneler için protokol"""
    
    def draw(self) -> str:
        """Çizim metodunu tanımlar"""
        ...

class Resizable(Protocol):
    """Boyutlandırılabilir nesneler için protokol"""
    
    def resize(self, width: int, height: int) -> None:
        """Boyutlandırma metodunu tanımlar"""
        ...

# Protocol implementasyonları (explicit inheritance gerekmez)
class Circle:
    def __init__(self, radius: float):
        self.radius = radius
    
    def draw(self) -> str:
        return f"Çember çiziliyor (r={self.radius})"
    
    def resize(self, width: int, height: int) -> None:
        self.radius = min(width, height) / 2

class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
    
    def draw(self) -> str:
        return f"Dikdörtgen çiziliyor ({self.width}x{self.height})"
    
    def resize(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

def ciz_nesne(nesne: Drawable) -> str:
    """Drawable protokolünü implement eden herhangi bir nesneyi çizer"""
    return nesne.draw()

def boyutlandir_ve_ciz(nesne: Drawable, w: int, h: int) -> str:
    """Nesneyi boyutlandırır ve çizer (Drawable ve Resizable implement eden nesne)"""
    if hasattr(nesne, 'resize'):
        nesne.resize(w, h)
    return nesne.draw()

# Protocol kullanımı
circle = Circle(5.0)
rectangle = Rectangle(10, 20)

print(ciz_nesne(circle))
print(ciz_nesne(rectangle))

print(boyutlandir_ve_ciz(circle, 8, 8))
print(boyutlandir_ve_ciz(rectangle, 15, 25))

# =============================================================================
# 7. TYPED DICT VE DATACLASSES
# =============================================================================

print("\n=== TypedDict ve Dataclasses ===")

# TypedDict kullanımı
class PersonDict(TypedDict):
    name: str
    age: int
    email: str
    active: NotRequired[bool]  # İsteğe bağlı field

class ConfigDict(TypedDict, total=False):  # Tüm fieldlar isteğe bağlı
    debug: bool
    timeout: int
    retries: int

def kisi_olustur(name: str, age: int, email: str) -> PersonDict:
    """PersonDict tipinde kişi oluşturur"""
    return {
        "name": name,
        "age": age,
        "email": email,
        "active": True
    }

def kisi_guncelle(kisi: PersonDict, **updates) -> PersonDict:
    """Kişi bilgilerini günceller"""
    return {**kisi, **updates}

# Dataclass kullanımı
@dataclass
class Product:
    """Ürün dataclass'ı"""
    name: str
    price: float
    category: str
    in_stock: bool = True
    tags: List[str] = None
    
    def __post_init__(self):
        if self.tags is None:
            self.tags = []
    
    def add_tag(self, tag: str) -> None:
        """Tag ekler"""
        if tag not in self.tags:
            self.tags.append(tag)
    
    def apply_discount(self, percentage: float) -> 'Product':
        """İndirim uygular ve yeni ürün döndürür"""
        new_price = self.price * (1 - percentage / 100)
        return Product(
            name=self.name,
            price=new_price,
            category=self.category,
            in_stock=self.in_stock,
            tags=self.tags.copy()
        )

# TypedDict ve Dataclass kullanımı
person = kisi_olustur("Ali Veli", 30, "ali@example.com")
print(f"Kişi: {person}")

updated_person = kisi_guncelle(person, age=31, active=False)
print(f"Güncellenmiş kişi: {updated_person}")

product = Product("Laptop", 15000.0, "Elektronik")
product.add_tag("gaming")
product.add_tag("portable")

print(f"Ürün: {product}")

discounted_product = product.apply_discount(15)  # %15 indirim
print(f"İndirimli ürün: {discounted_product}")

# =============================================================================
# 8. LITERAL TYPES VE FINAL
# =============================================================================

print("\n=== Literal Types ve Final ===")

# Literal types
Mode = Literal["read", "write", "append"]
LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR"]

def dosya_ac(dosya: str, mode: Mode) -> str:
    """Dosyayı belirtilen modda açar"""
    return f"Dosya '{dosya}' {mode} modunda açıldı"

def log_mesaj(mesaj: str, level: LogLevel = "INFO") -> str:
    """Log mesajı oluşturur"""
    return f"[{level}] {mesaj}"

# Final values
MAX_CONNECTIONS: Final = 100
API_VERSION: Final[str] = "v1.2.3"

class DatabaseConfig:
    """Database konfigürasyonu"""
    HOST: Final[str] = "localhost"
    PORT: Final[int] = 5432
    
    def __init__(self, database: str):
        self.database: Final[str] = database  # Instance-level final

# Literal kullanımı
print(dosya_ac("data.txt", "read"))
print(dosya_ac("output.txt", "write"))

print(log_mesaj("Uygulama başlatıldı", "INFO"))
print(log_mesaj("Hata oluştu", "ERROR"))

# Final kullanımı
print(f"Max connections: {MAX_CONNECTIONS}")
print(f"API Version: {API_VERSION}")

db_config = DatabaseConfig("production")
print(f"DB Config: {db_config.HOST}:{db_config.PORT}/{db_config.database}")

# =============================================================================
# 9. FUNCTION OVERLOADING
# =============================================================================

print("\n=== Function Overloading ===")

@overload
def process_data(data: str) -> str: ...

@overload  
def process_data(data: int) -> int: ...

@overload
def process_data(data: List[int]) -> List[int]: ...

def process_data(data):
    """Farklı veri tiplerini işler"""
    if isinstance(data, str):
        return data.upper()
    elif isinstance(data, int):
        return data * 2
    elif isinstance(data, list):
        return [x * 2 for x in data]
    else:
        raise TypeError(f"Desteklenmeyen tip: {type(data)}")

@overload
def create_user(name: str) -> Dict[str, str]: ...

@overload
def create_user(name: str, age: int) -> Dict[str, Union[str, int]]: ...

@overload
def create_user(name: str, age: int, email: str) -> Dict[str, Union[str, int]]: ...

def create_user(name: str, age: Optional[int] = None, email: Optional[str] = None):
    """Kullanıcı oluşturur (overloaded)"""
    user = {"name": name}
    if age is not None:
        user["age"] = age
    if email is not None:
        user["email"] = email
    return user

# Overload kullanımı
print(process_data("hello"))  # str -> str
print(process_data(21))       # int -> int  
print(process_data([1, 2, 3])) # List[int] -> List[int]

print(create_user("Ali"))
print(create_user("Ayşe", 25))
print(create_user("Mehmet", 30, "mehmet@example.com"))

# =============================================================================
# 10. TYPE CHECKING VE RUNTIME VALIDATION
# =============================================================================

print("\n=== Type Checking ve Runtime Validation ===")

def runtime_type_check(func: Callable) -> Callable:
    """Runtime'da tip kontrolü yapan decorator"""
    import inspect
    from typing import get_type_hints
    
    def wrapper(*args, **kwargs):
        # Type hints'leri al
        type_hints = get_type_hints(func)
        
        # Argüman isimlerini al
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        # Tip kontrolü yap
        for param_name, value in bound_args.arguments.items():
            if param_name in type_hints:
                expected_type = type_hints[param_name]
                
                # Basit tip kontrolü (gelişmiş typing için daha complex logic gerekir)
                if hasattr(expected_type, '__origin__'):
                    # Generic type (List, Dict, etc.)
                    origin = expected_type.__origin__
                    if not isinstance(value, origin):
                        raise TypeError(
                            f"{param_name} expected {expected_type}, got {type(value)}"
                        )
                else:
                    # Basit type
                    if not isinstance(value, expected_type):
                        raise TypeError(
                            f"{param_name} expected {expected_type}, got {type(value)}"
                        )
        
        return func(*args, **kwargs)
    
    return wrapper

@runtime_type_check
def guvenli_bolme(a: float, b: float) -> float:
    """Tip kontrolü yapan bölme fonksiyonu"""
    if b == 0:
        raise ValueError("Sıfıra bölünemez")
    return a / b

@runtime_type_check  
def liste_topla(numbers: List[int]) -> int:
    """Liste elemanlarını toplar (tip kontrolü ile)"""
    return sum(numbers)

# Type casting
def any_to_string(value: Any) -> str:
    """Any tipini string'e çevirir"""
    return cast(str, str(value))

# Runtime type check kullanımı
try:
    result = guvenli_bolme(10.0, 2.0)
    print(f"Güvenli bölme sonucu: {result}")
    
    # Yanlış tip ile çağır
    # guvenli_bolme("10", "2")  # TypeError verecek
except TypeError as e:
    print(f"Tip hatası: {e}")

try:
    total = liste_topla([1, 2, 3, 4, 5])
    print(f"Liste toplamı: {total}")
    
    # Yanlış tip ile çağır
    # liste_topla("12345")  # TypeError verecek
except TypeError as e:
    print(f"Tip hatası: {e}")

# Type casting
any_value: Any = 42
str_value = any_to_string(any_value)
print(f"Cast edilmiş değer: {str_value} (tip: {type(str_value)})")

# =============================================================================
# 11. CONDITIONAL IMPORTS VE TYPE_CHECKING
# =============================================================================

print("\n=== Conditional Imports ve TYPE_CHECKING ===")

if TYPE_CHECKING:
    # Bu imports sadece type checking sırasında yüklenir
    from datetime import datetime as DateTime
    from decimal import Decimal

def format_timestamp(ts: 'DateTime') -> str:
    """Timestamp'i formatlar (forward reference)"""
    return ts.strftime("%Y-%m-%d %H:%M:%S")

def calculate_price(amount: 'Decimal', tax_rate: float) -> 'Decimal':
    """Fiyat hesaplar (forward reference)"""
    # Runtime'da gerçek import
    from decimal import Decimal
    if isinstance(amount, (int, float)):
        amount = Decimal(str(amount))
    tax = amount * Decimal(str(tax_rate))
    return amount + tax

# Forward reference kullanımı
from datetime import datetime
from decimal import Decimal

now = datetime.now()
print(f"Formatlanmış zaman: {format_timestamp(now)}")

price = calculate_price(Decimal("100.00"), 0.18)
print(f"Vergili fiyat: {price}")

# =============================================================================
# 12. ADVANCED TYPE PATTERNS
# =============================================================================

print("\n=== Advanced Type Patterns ===")

# NewType ile distinct types
from typing import NewType

UserId = NewType('UserId', int)
ProductId = NewType('ProductId', int)

def get_user_by_id(user_id: UserId) -> Optional[str]:
    """Kullanıcıyı ID ile bulur"""
    users = {
        UserId(1): "Ali",
        UserId(2): "Ayşe",
        UserId(3): "Mehmet"
    }
    return users.get(user_id)

def get_product_by_id(product_id: ProductId) -> Optional[str]:
    """Ürünü ID ile bulur"""
    products = {
        ProductId(101): "Laptop",
        ProductId(102): "Mouse", 
        ProductId(103): "Keyboard"
    }
    return products.get(product_id)

# Recursive types
JsonValue = Union[str, int, float, bool, None, List['JsonValue'], Dict[str, 'JsonValue']]

def validate_json(data: JsonValue) -> bool:
    """JSON veriyi validate eder"""
    if data is None or isinstance(data, (str, int, float, bool)):
        return True
    elif isinstance(data, list):
        return all(validate_json(item) for item in data)
    elif isinstance(data, dict):
        return all(
            isinstance(key, str) and validate_json(value)
            for key, value in data.items()
        )
    return False

# Type aliases
Matrix = List[List[float]]
Point3D = Tuple[float, float, float]
Transform = Callable[[Point3D], Point3D]

def apply_transform(points: List[Point3D], transform: Transform) -> List[Point3D]:
    """Transform uygular"""
    return [transform(point) for point in points]

def translate(dx: float, dy: float, dz: float) -> Transform:
    """Translation transform oluşturur"""
    def transform(point: Point3D) -> Point3D:
        x, y, z = point
        return (x + dx, y + dy, z + dz)
    return transform

# NewType kullanımı
user_id = UserId(1)
product_id = ProductId(101)

print(f"Kullanıcı: {get_user_by_id(user_id)}")
print(f"Ürün: {get_product_by_id(product_id)}")

# JSON validation
valid_json = {"name": "Ali", "age": 30, "scores": [85, 92, 78]}
invalid_json = {"name": "Ali", 123: "invalid_key"}  # key int olmamalı

print(f"Valid JSON: {validate_json(valid_json)}")
print(f"Invalid JSON: {validate_json(invalid_json)}")

# 3D transform
points = [(1.0, 2.0, 3.0), (4.0, 5.0, 6.0)]
translate_transform = translate(1.0, 1.0, 1.0)
transformed_points = apply_transform(points, translate_transform)

print(f"Orijinal noktalar: {points}")
print(f"Transform edilmiş noktalar: {transformed_points}")

print("\n" + "="*50)
print("TYPE HINTS VE ANNOTATIONS TAMAMLANDI")
print("="*50)

print("\nType System Özeti:")
print("1. Temel type hints (int, str, bool, float)")
print("2. Collection types (List, Dict, Set, Tuple)")
print("3. Optional ve Union types")
print("4. Callable type annotations")
print("5. Generic types ve TypeVar")
print("6. Protocol ve structural typing")
print("7. TypedDict ve dataclasses")
print("8. Literal types ve Final")
print("9. Function overloading")
print("10. Runtime type checking")
print("11. Conditional imports")
print("12. Advanced patterns (NewType, recursive types)")

print("\nmypy ile tip kontrolü:")
print("pip install mypy")
print("mypy type_hints.py")