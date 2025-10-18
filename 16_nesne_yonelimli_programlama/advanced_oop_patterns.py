"""
Python Advanced OOP Patterns - Comprehensive Guide
Design Patterns, Metaclasses, Descriptors, Advanced Architecture

Bu dosyada Python'da ileri seviye OOP kalıpları, tasarım desenleri,
metaclass'lar, descriptor'lar ve gelişmiş mimari patterns incelenecek.
"""

import time
import datetime
import threading
import weakref
from typing import Type, Any, Dict, List, Optional, Callable
from abc import ABC, abstractmethod
from functools import wraps
import json

# =============================================================================
# 1. SINGLETON PATTERN
# =============================================================================

print("=== Singleton Pattern ===")

class Singleton:
    """Singleton pattern implementation"""
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self.creation_time = datetime.datetime.now()
            self.access_count = 0
            self._initialized = True
            print(f"✨ Singleton instance oluşturuldu: {id(self)}")
    
    def get_info(self):
        self.access_count += 1
        return f"Singleton ID: {id(self)}, Created: {self.creation_time}, Access: {self.access_count}"

class DatabaseManager(Singleton):
    """Database manager singleton"""
    
    def __init__(self):
        super().__init__()
        if not hasattr(self, 'connections'):
            self.connections = {}
            self.max_connections = 10
            print("🗄️  Database Manager başlatıldı")
    
    def get_connection(self, db_name):
        """Veritabanı bağlantısı al"""
        if db_name not in self.connections:
            if len(self.connections) < self.max_connections:
                self.connections[db_name] = f"Connection_to_{db_name}_{len(self.connections)}"
                print(f"🔗 Yeni bağlantı oluşturuldu: {db_name}")
            else:
                print(f"❌ Maksimum bağlantı sayısına ulaşıldı!")
                return None
        
        return self.connections[db_name]
    
    def list_connections(self):
        """Aktif bağlantıları listele"""
        print(f"📋 Aktif bağlantılar ({len(self.connections)}/{self.max_connections}):")
        for db, conn in self.connections.items():
            print(f"  {db}: {conn}")

# Singleton kullanımı
print("Singleton pattern örnekleri:")

# Farklı referanslar aynı instance'ı işaret eder
s1 = Singleton()
s2 = Singleton()
print(f"s1 is s2: {s1 is s2}")
print(f"s1 info: {s1.get_info()}")
print(f"s2 info: {s2.get_info()}")

# Database manager singleton
db1 = DatabaseManager()
db2 = DatabaseManager()
print(f"db1 is db2: {db1 is db2}")

db1.get_connection("users_db")
db2.get_connection("products_db")  # Aynı instance
db1.list_connections()

# =============================================================================
# 2. FACTORY PATTERN
# =============================================================================

print("\n=== Factory Pattern ===")

class Shape(ABC):
    """Shape abstract base class"""
    
    @abstractmethod
    def draw(self) -> str:
        pass
    
    @abstractmethod
    def area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def draw(self) -> str:
        return f"🔵 Daire çizildi (r={self.radius})"
    
    def area(self) -> float:
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def draw(self) -> str:
        return f"🟦 Dikdörtgen çizildi ({self.width}x{self.height})"
    
    def area(self) -> float:
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def draw(self) -> str:
        return f"🔺 Üçgen çizildi (taban={self.base}, yükseklik={self.height})"
    
    def area(self) -> float:
        return (self.base * self.height) / 2

class ShapeFactory:
    """Shape factory - object creation logic"""
    
    _shape_registry = {
        'circle': Circle,
        'rectangle': Rectangle,
        'triangle': Triangle
    }
    
    @classmethod
    def create_shape(cls, shape_type: str, **kwargs) -> Shape:
        """Shape oluşturma factory method"""
        shape_type = shape_type.lower()
        
        if shape_type not in cls._shape_registry:
            available = ', '.join(cls._shape_registry.keys())
            raise ValueError(f"Geçersiz şekil tipi: {shape_type}. Mevcut: {available}")
        
        shape_class = cls._shape_registry[shape_type]
        
        try:
            return shape_class(**kwargs)
        except TypeError as e:
            raise ValueError(f"{shape_type} için geçersiz parametreler: {e}")
    
    @classmethod
    def register_shape(cls, name: str, shape_class: Type[Shape]):
        """Yeni şekil tipi kaydet"""
        if not issubclass(shape_class, Shape):
            raise TypeError("Shape sınıfından türetilmiş olmalı")
        
        cls._shape_registry[name.lower()] = shape_class
        print(f"✅ Yeni şekil tipi kaydedildi: {name}")
    
    @classmethod
    def available_shapes(cls) -> List[str]:
        """Mevcut şekil tiplerini listele"""
        return list(cls._shape_registry.keys())

# Custom shape for registration demo
class Pentagon(Shape):
    def __init__(self, side_length):
        self.side_length = side_length
    
    def draw(self) -> str:
        return f"⬟ Pentagon çizildi (kenar={self.side_length})"
    
    def area(self) -> float:
        # Approximate pentagon area
        return (1.720477 * self.side_length ** 2)

# Factory pattern kullanımı
print("Factory pattern örnekleri:")

print(f"Mevcut şekiller: {ShapeFactory.available_shapes()}")

# Şekil oluşturma
shapes = [
    ShapeFactory.create_shape('circle', radius=5),
    ShapeFactory.create_shape('rectangle', width=4, height=6),
    ShapeFactory.create_shape('triangle', base=3, height=4)
]

for shape in shapes:
    print(f"{shape.draw()} - Alan: {shape.area():.2f}")

# Yeni şekil tipi kaydet
ShapeFactory.register_shape('pentagon', Pentagon)
pentagon = ShapeFactory.create_shape('pentagon', side_length=5)
print(f"{pentagon.draw()} - Alan: {pentagon.area():.2f}")

# Hatalı kullanım
try:
    invalid_shape = ShapeFactory.create_shape('hexagon')
except ValueError as e:
    print(f"❌ Factory hatası: {e}")

# =============================================================================
# 3. OBSERVER PATTERN
# =============================================================================

print("\n=== Observer Pattern ===")

class Observer(ABC):
    """Observer interface"""
    
    @abstractmethod
    def update(self, subject, event_type: str, data: Any):
        pass

class Subject:
    """Observable subject"""
    
    def __init__(self):
        self._observers: List[Observer] = []
        self._state = {}
    
    def attach(self, observer: Observer):
        """Observer ekle"""
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"👁️  Observer eklendi: {observer.__class__.__name__}")
    
    def detach(self, observer: Observer):
        """Observer çıkar"""
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"👁️  Observer çıkarıldı: {observer.__class__.__name__}")
    
    def notify(self, event_type: str, data: Any = None):
        """Tüm observer'ları bilgilendir"""
        print(f"📢 Event: {event_type}")
        for observer in self._observers:
            try:
                observer.update(self, event_type, data)
            except Exception as e:
                print(f"❌ Observer error: {e}")

class StockPrice(Subject):
    """Stock price subject"""
    
    def __init__(self, symbol: str, initial_price: float):
        super().__init__()
        self.symbol = symbol
        self._price = initial_price
        self.price_history = [initial_price]
    
    @property
    def price(self) -> float:
        return self._price
    
    @price.setter
    def price(self, new_price: float):
        old_price = self._price
        self._price = new_price
        self.price_history.append(new_price)
        
        change = ((new_price - old_price) / old_price) * 100
        self.notify('price_change', {
            'symbol': self.symbol,
            'old_price': old_price,
            'new_price': new_price,
            'change_percent': change
        })
    
    def get_trend(self) -> str:
        """Fiyat trendi"""
        if len(self.price_history) < 2:
            return "stable"
        
        recent_prices = self.price_history[-3:]
        if all(recent_prices[i] < recent_prices[i+1] for i in range(len(recent_prices)-1)):
            return "rising"
        elif all(recent_prices[i] > recent_prices[i+1] for i in range(len(recent_prices)-1)):
            return "falling"
        else:
            return "volatile"

class EmailNotifier(Observer):
    """Email bildirim observer"""
    
    def __init__(self, email: str):
        self.email = email
        self.alerts_sent = 0
    
    def update(self, subject, event_type: str, data: Any):
        if event_type == 'price_change':
            change = data['change_percent']
            if abs(change) > 5:  # %5'ten fazla değişim
                self.alerts_sent += 1
                print(f"📧 Email gönderildi ({self.email}): "
                      f"{data['symbol']} %{change:.1f} değişti!")

class SMSNotifier(Observer):
    """SMS bildirim observer"""
    
    def __init__(self, phone: str):
        self.phone = phone
        self.sms_sent = 0
    
    def update(self, subject, event_type: str, data: Any):
        if event_type == 'price_change':
            change = data['change_percent']
            if abs(change) > 10:  # %10'dan fazla değişim
                self.sms_sent += 1
                print(f"📱 SMS gönderildi ({self.phone}): "
                      f"ALARM! {data['symbol']} %{change:.1f} değişti!")

class TradingBot(Observer):
    """Trading bot observer"""
    
    def __init__(self, strategy: str):
        self.strategy = strategy
        self.trades_executed = 0
        self.portfolio = {}
    
    def update(self, subject, event_type: str, data: Any):
        if event_type == 'price_change':
            symbol = data['symbol']
            change = data['change_percent']
            
            if self.strategy == "momentum":
                if change > 5:  # Yükseliş momentumu
                    self.trades_executed += 1
                    print(f"🤖 Bot: {symbol} BUY signal (momentum: %{change:.1f})")
                elif change < -5:  # Düşüş momentumu
                    self.trades_executed += 1
                    print(f"🤖 Bot: {symbol} SELL signal (momentum: %{change:.1f})")

# Observer pattern kullanımı
print("Observer pattern örnekleri:")

# Stock price subject
aapl = StockPrice("AAPL", 150.0)

# Observer'ları oluştur
email_notifier = EmailNotifier("trader@example.com")
sms_notifier = SMSNotifier("+90-555-1234")
trading_bot = TradingBot("momentum")

# Observer'ları ekle
aapl.attach(email_notifier)
aapl.attach(sms_notifier)
aapl.attach(trading_bot)

# Fiyat değişimleri simülasyonu
price_changes = [155.0, 148.0, 165.0, 140.0, 168.0]

for new_price in price_changes:
    print(f"\n--- Fiyat güncelleniyor: ${new_price} ---")
    aapl.price = new_price
    time.sleep(0.1)  # Kısa delay

print(f"\nÖzet:")
print(f"Email bildirim sayısı: {email_notifier.alerts_sent}")
print(f"SMS bildirim sayısı: {sms_notifier.sms_sent}")
print(f"Bot işlem sayısı: {trading_bot.trades_executed}")

# =============================================================================
# 4. DECORATOR PATTERN
# =============================================================================

print("\n=== Decorator Pattern ===")

class Component(ABC):
    """Component interface"""
    
    @abstractmethod
    def operation(self) -> str:
        pass
    
    @abstractmethod
    def cost(self) -> float:
        pass

class Coffee(Component):
    """Base coffee component"""
    
    def operation(self) -> str:
        return "Simple Coffee"
    
    def cost(self) -> float:
        return 2.0

class CoffeeDecorator(Component):
    """Base decorator"""
    
    def __init__(self, component: Component):
        self._component = component
    
    def operation(self) -> str:
        return self._component.operation()
    
    def cost(self) -> float:
        return self._component.cost()

class MilkDecorator(CoffeeDecorator):
    """Milk decorator"""
    
    def operation(self) -> str:
        return f"{self._component.operation()} + Milk"
    
    def cost(self) -> float:
        return self._component.cost() + 0.5

class SugarDecorator(CoffeeDecorator):
    """Sugar decorator"""
    
    def operation(self) -> str:
        return f"{self._component.operation()} + Sugar"
    
    def cost(self) -> float:
        return self._component.cost() + 0.2

class VanillaDecorator(CoffeeDecorator):
    """Vanilla decorator"""
    
    def operation(self) -> str:
        return f"{self._component.operation()} + Vanilla"
    
    def cost(self) -> float:
        return self._component.cost() + 0.7

class ExtraShotDecorator(CoffeeDecorator):
    """Extra shot decorator"""
    
    def operation(self) -> str:
        return f"{self._component.operation()} + Extra Shot"
    
    def cost(self) -> float:
        return self._component.cost() + 1.0

# Decorator pattern kullanımı
print("Decorator pattern örnekleri:")

# Base coffee
coffee = Coffee()
print(f"1. {coffee.operation()} - ${coffee.cost():.2f}")

# Single decorator
coffee_with_milk = MilkDecorator(coffee)
print(f"2. {coffee_with_milk.operation()} - ${coffee_with_milk.cost():.2f}")

# Multiple decorators
fancy_coffee = VanillaDecorator(
    SugarDecorator(
        MilkDecorator(
            ExtraShotDecorator(Coffee())
        )
    )
)
print(f"3. {fancy_coffee.operation()} - ${fancy_coffee.cost():.2f}")

# Dynamic decoration
base_coffee = Coffee()
decorators = [MilkDecorator, SugarDecorator, VanillaDecorator]

for i, decorator_class in enumerate(decorators, 1):
    base_coffee = decorator_class(base_coffee)
    print(f"   Step {i}: {base_coffee.operation()} - ${base_coffee.cost():.2f}")

# =============================================================================
# 5. METACLASSES
# =============================================================================

print("\n=== Metaclasses ===")

class SingletonMeta(type):
    """Singleton metaclass"""
    _instances = {}
    _lock = threading.Lock()
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
                    print(f"🔧 Metaclass: {cls.__name__} instance oluşturuldu")
        return cls._instances[cls]

class ValidatedMeta(type):
    """Validation metaclass"""
    
    def __new__(mcs, name, bases, namespace):
        # Class oluşturulmadan önce validation
        if 'required_methods' in namespace:
            required = namespace['required_methods']
            for method in required:
                if method not in namespace:
                    raise TypeError(f"Class {name} must implement {method} method")
        
        # Method'ları otomatik wrap etme
        for key, value in namespace.items():
            if callable(value) and not key.startswith('_'):
                namespace[key] = mcs._log_method_call(value)
        
        print(f"🏗️  Metaclass: {name} class oluşturuluyor")
        return super().__new__(mcs, name, bases, namespace)
    
    @staticmethod
    def _log_method_call(method):
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            print(f"📝 Method called: {method.__name__}")
            return method(self, *args, **kwargs)
        return wrapper

class ConfigSingleton(metaclass=SingletonMeta):
    """Configuration singleton using metaclass"""
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.config = {}
            self.initialized = True
            print("⚙️  Config singleton başlatıldı")
    
    def set(self, key, value):
        self.config[key] = value
    
    def get(self, key, default=None):
        return self.config.get(key, default)

class ValidatedService(metaclass=ValidatedMeta):
    """Service with validation metaclass"""
    required_methods = ['start', 'stop', 'status']
    
    def __init__(self, name):
        self.name = name
        self.running = False
    
    def start(self):
        self.running = True
        return f"{self.name} service started"
    
    def stop(self):
        self.running = False
        return f"{self.name} service stopped"
    
    def status(self):
        return "running" if self.running else "stopped"
    
    def custom_method(self):
        return f"{self.name} custom operation"

# Metaclasses kullanımı
print("Metaclasses örnekleri:")

# Singleton metaclass
config1 = ConfigSingleton()
config2 = ConfigSingleton()
print(f"config1 is config2: {config1 is config2}")

config1.set('debug', True)
print(f"config2.get('debug'): {config2.get('debug')}")

# Validated metaclass
service = ValidatedService("WebServer")
print(service.start())
print(service.custom_method())  # Otomatik logging
print(f"Status: {service.status()}")

# =============================================================================
# 6. DESCRIPTORS
# =============================================================================

print("\n=== Descriptors ===")

class ValidatedAttribute:
    """Validation descriptor"""
    
    def __init__(self, validator=None, default=None):
        self.validator = validator
        self.default = default
        self.name = None
    
    def __set_name__(self, owner, name):
        """Descriptor name setting"""
        self.name = f"_{name}"
    
    def __get__(self, instance, owner):
        """Attribute access"""
        if instance is None:
            return self
        return getattr(instance, self.name, self.default)
    
    def __set__(self, instance, value):
        """Attribute assignment with validation"""
        if self.validator and not self.validator(value):
            raise ValueError(f"Invalid value for {self.name}: {value}")
        setattr(instance, self.name, value)
        print(f"✅ Validated and set: {self.name} = {value}")
    
    def __delete__(self, instance):
        """Attribute deletion"""
        delattr(instance, self.name)

class TypedProperty:
    """Type-checked property descriptor"""
    
    def __init__(self, expected_type, default=None):
        self.expected_type = expected_type
        self.default = default
        self.name = None
    
    def __set_name__(self, owner, name):
        self.name = f"_{name}"
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name, self.default)
    
    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"{self.name} must be {self.expected_type.__name__}, "
                          f"got {type(value).__name__}")
        setattr(instance, self.name, value)
        print(f"🔍 Type-checked and set: {self.name} = {value}")

class CachedProperty:
    """Cached property descriptor"""
    
    def __init__(self, func):
        self.func = func
        self.name = func.__name__
        self.__doc__ = func.__doc__
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        
        # Cache key
        cache_name = f"_cached_{self.name}"
        
        if not hasattr(instance, cache_name):
            print(f"💾 Computing and caching: {self.name}")
            value = self.func(instance)
            setattr(instance, cache_name, value)
        else:
            print(f"⚡ Using cached value: {self.name}")
        
        return getattr(instance, cache_name)
    
    def __set__(self, instance, value):
        cache_name = f"_cached_{self.name}"
        setattr(instance, cache_name, value)
    
    def __delete__(self, instance):
        cache_name = f"_cached_{self.name}"
        if hasattr(instance, cache_name):
            delattr(instance, cache_name)

# Validators
def positive_number(value):
    return isinstance(value, (int, float)) and value > 0

def valid_email(value):
    return isinstance(value, str) and '@' in value and '.' in value

class User:
    """User class with descriptors"""
    
    # Type-checked properties
    name = TypedProperty(str, "")
    age = TypedProperty(int, 0)
    
    # Validated properties
    salary = ValidatedAttribute(positive_number, 0)
    email = ValidatedAttribute(valid_email, "")
    
    def __init__(self, name, age, email, salary=0):
        self.name = name
        self.age = age
        self.email = email
        self.salary = salary
    
    @CachedProperty
    def annual_bonus(self):
        """Expensive calculation - cached"""
        print("  🔄 Calculating annual bonus...")
        time.sleep(0.1)  # Simulate expensive operation
        return self.salary * 0.15
    
    @CachedProperty
    def tax_bracket(self):
        """Another expensive calculation"""
        print("  🔄 Determining tax bracket...")
        time.sleep(0.1)
        if self.salary < 50000:
            return "Low"
        elif self.salary < 100000:
            return "Medium"
        else:
            return "High"

# Descriptors kullanımı
print("Descriptors örnekleri:")

user = User("Alice", 30, "alice@example.com", 75000)

print(f"User: {user.name}, Age: {user.age}")
print(f"Annual bonus: ${user.annual_bonus:.2f}")  # First calculation
print(f"Annual bonus: ${user.annual_bonus:.2f}")  # Cached value
print(f"Tax bracket: {user.tax_bracket}")         # First calculation
print(f"Tax bracket: {user.tax_bracket}")         # Cached value

# Validation tests
try:
    user.salary = -1000  # Should fail
except ValueError as e:
    print(f"❌ Validation error: {e}")

try:
    user.age = "thirty"  # Should fail
except TypeError as e:
    print(f"❌ Type error: {e}")

# Valid updates
user.salary = 80000  # Valid
print(f"Updated annual bonus: ${user.annual_bonus:.2f}")  # Recalculated

# =============================================================================
# 7. ADVANCED PATTERNS COMBINATION
# =============================================================================

print("\n=== Advanced Patterns Combination ===")

class ServiceRegistry(metaclass=SingletonMeta):
    """Service registry with multiple patterns"""
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self._services = {}
            self._factories = {}
            self._observers = {}
            self.initialized = True
            print("🏛️  Service Registry başlatıldı")
    
    def register_service(self, name: str, service_class: Type):
        """Service kaydet"""
        self._services[name] = service_class
        print(f"📋 Service kaydedildi: {name}")
    
    def register_factory(self, name: str, factory: Callable):
        """Factory kaydet"""
        self._factories[name] = factory
        print(f"🏭 Factory kaydedildi: {name}")
    
    def get_service(self, name: str, *args, **kwargs):
        """Service instance al"""
        if name in self._services:
            return self._services[name](*args, **kwargs)
        elif name in self._factories:
            return self._factories[name](*args, **kwargs)
        else:
            raise KeyError(f"Service not found: {name}")
    
    def add_observer(self, service_name: str, observer: Observer):
        """Service'e observer ekle"""
        if service_name not in self._observers:
            self._observers[service_name] = []
        self._observers[service_name].append(observer)
    
    def notify_observers(self, service_name: str, event: str, data: Any = None):
        """Service observer'larını bilgilendir"""
        if service_name in self._observers:
            for observer in self._observers[service_name]:
                observer.update(None, event, data)

class MonitoredService:
    """Monitored service with logging"""
    
    def __init__(self, name: str):
        self.name = name
        self.start_time = None
        self.is_running = False
        self.operation_count = 0
    
    def start(self):
        """Service başlat"""
        self.start_time = datetime.datetime.now()
        self.is_running = True
        
        # Registry'ye bildirim gönder
        registry = ServiceRegistry()
        registry.notify_observers(self.name, 'service_started', {
            'service': self.name,
            'start_time': self.start_time
        })
        
        return f"✅ {self.name} service started"
    
    def stop(self):
        """Service durdur"""
        if self.is_running:
            runtime = datetime.datetime.now() - self.start_time
            self.is_running = False
            
            # Registry'ye bildirim gönder
            registry = ServiceRegistry()
            registry.notify_observers(self.name, 'service_stopped', {
                'service': self.name,
                'runtime': runtime.total_seconds(),
                'operations': self.operation_count
            })
        
        return f"⏹️  {self.name} service stopped"
    
    def perform_operation(self, operation: str):
        """İşlem gerçekleştir"""
        if not self.is_running:
            raise RuntimeError(f"{self.name} service is not running")
        
        self.operation_count += 1
        
        # Registry'ye bildirim gönder
        registry = ServiceRegistry()
        registry.notify_observers(self.name, 'operation_performed', {
            'service': self.name,
            'operation': operation,
            'count': self.operation_count
        })
        
        return f"🔧 {self.name}: {operation} completed"

class ServiceMonitor(Observer):
    """Service monitoring observer"""
    
    def __init__(self):
        self.events = []
        self.service_stats = {}
    
    def update(self, subject, event_type: str, data: Any):
        """Monitor event'lerini işle"""
        timestamp = datetime.datetime.now()
        event = {
            'timestamp': timestamp,
            'event_type': event_type,
            'data': data
        }
        self.events.append(event)
        
        service_name = data.get('service', 'unknown')
        
        if event_type == 'service_started':
            print(f"🟢 Monitor: {service_name} started at {timestamp.strftime('%H:%M:%S')}")
        elif event_type == 'service_stopped':
            runtime = data.get('runtime', 0)
            operations = data.get('operations', 0)
            print(f"🔴 Monitor: {service_name} stopped. Runtime: {runtime:.1f}s, Operations: {operations}")
        elif event_type == 'operation_performed':
            operation = data.get('operation', 'unknown')
            count = data.get('count', 0)
            print(f"⚙️  Monitor: {service_name} performed '{operation}' (total: {count})")
    
    def get_report(self):
        """Monitoring raporu"""
        print("\n=== Service Monitor Report ===")
        print(f"Total events: {len(self.events)}")
        
        event_types = {}
        for event in self.events:
            event_type = event['event_type']
            event_types[event_type] = event_types.get(event_type, 0) + 1
        
        for event_type, count in event_types.items():
            print(f"  {event_type}: {count}")

# Advanced patterns combination kullanımı
print("Advanced patterns combination örnekleri:")

# Registry setup
registry = ServiceRegistry()
monitor = ServiceMonitor()

# Service'leri kaydet
registry.register_service('web_server', MonitoredService)
registry.register_service('database', MonitoredService)

# Monitor'ı observer olarak ekle
registry.add_observer('web_service', monitor)
registry.add_observer('db_service', monitor)

# Service'leri oluştur ve çalıştır
web_service = registry.get_service('web_server', 'web_service')
db_service = registry.get_service('database', 'db_service')

print(web_service.start())
print(db_service.start())

# İşlemler gerçekleştir
operations = [
    (web_service, "handle_request"),
    (db_service, "execute_query"),
    (web_service, "serve_static_file"),
    (db_service, "backup_data"),
    (web_service, "process_form")
]

for service, operation in operations:
    print(service.perform_operation(operation))
    time.sleep(0.1)

# Service'leri durdur
print(web_service.stop())
print(db_service.stop())

# Monitor raporu
monitor.get_report()

# Registry test - singleton behavior
registry2 = ServiceRegistry()
print(f"registry is registry2: {registry is registry2}")

print("\n" + "="*60)
print("ADVANCED OOP PATTERNS TAMAMLANDI")
print("="*60)

print("\nKonular Özeti:")
print("1. Singleton Pattern (Thread-safe)")
print("2. Factory Pattern (Extensible)")
print("3. Observer Pattern (Event-driven)")
print("4. Decorator Pattern (Composition)")
print("5. Metaclasses (Class creation control)")
print("6. Descriptors (Attribute behavior)")
print("7. Advanced Pattern Combinations")
print("8. Service Registry Architecture")

print(f"\n🎉 Section 16 - Nesne Yönelimli Programlama TAMAMLANDI!")
print("6 dosya başarıyla oluşturuldu:")
print("  1. oop_temelleri.py")
print("  2. encapsulation_ve_property.py")
print("  3. inheritance_kalitim.py")
print("  4. polymorphism_ve_abstraction.py")
print("  5. special_methods_magic.py")
print("  6. advanced_oop_patterns.py")