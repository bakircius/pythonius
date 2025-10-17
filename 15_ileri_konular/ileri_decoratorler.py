"""
Python İleri Düzey Decorator'lar - Comprehensive Guide

Bu dosyada decorator'ların derinlemesine incelemesi, parametreli decorator'lar,
class-based decorator'lar ve gelişmiş kullanım örnekleri bulacaksınız.
"""

import functools
import time
import logging
from typing import Callable, Any, Dict
from datetime import datetime
import warnings

# =============================================================================
# 1. TEMEL DECORATOR YAPISI
# =============================================================================

def basit_decorator(func):
    """En basit decorator örneği"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} fonksiyonu çalıştırılıyor...")
        result = func(*args, **kwargs)
        print(f"{func.__name__} fonksiyonu tamamlandı.")
        return result
    return wrapper

@basit_decorator
def merhaba_de(isim):
    """Basit bir fonksiyon"""
    return f"Merhaba {isim}!"

print("=== Basit Decorator ===")
sonuc = merhaba_de("Ali")
print(f"Sonuç: {sonuc}")

# =============================================================================
# 2. TİMİNG DECORATOR
# =============================================================================

def timing_decorator(func):
    """Fonksiyon çalışma süresini ölçen decorator"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} {execution_time:.4f} saniyede çalıştı")
        return result
    return wrapper

@timing_decorator
def yavas_fonksiyon():
    """Yavaş çalışan örnek fonksiyon"""
    time.sleep(0.1)  # 100ms bekle
    return "İşlem tamamlandı"

print("\n=== Timing Decorator ===")
yavas_fonksiyon()

# =============================================================================
# 3. PARAMETRELİ DECORATOR'LAR
# =============================================================================

def retry(max_attempts=3, delay=1):
    """Fonksiyonu belirlenen sayıda tekrar deneyen decorator"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"Deneme {attempt + 1}/{max_attempts} başarısız: {e}")
                    if attempt < max_attempts - 1:
                        time.sleep(delay)
            
            print(f"Tüm denemeler başarısız oldu.")
            raise last_exception
            
        return wrapper
    return decorator

def cache(max_size=128):
    """Basit önbellekleme decorator'ı"""
    def decorator(func):
        cache_dict = {}
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Anahtarı oluştur (kwargs'i sıralı tuple'a çevir)
            key = args + tuple(sorted(kwargs.items()))
            
            if key in cache_dict:
                print(f"Cache hit for {func.__name__}{key}")
                return cache_dict[key]
            
            result = func(*args, **kwargs)
            
            # Cache boyutunu kontrol et
            if len(cache_dict) >= max_size:
                # En eski entry'yi sil (basit FIFO)
                oldest_key = next(iter(cache_dict))
                del cache_dict[oldest_key]
            
            cache_dict[key] = result
            print(f"Cache miss for {func.__name__}{key} - result cached")
            return result
            
        wrapper.cache_info = lambda: {
            'size': len(cache_dict),
            'maxsize': max_size,
            'cache': cache_dict.copy()
        }
        wrapper.cache_clear = lambda: cache_dict.clear()
        
        return wrapper
    return decorator

# Parametreli decorator örnekleri
@retry(max_attempts=3, delay=0.5)
def hata_verebilecek_fonksiyon(basari_orani=0.3):
    """Belirli oranda başarılı olan fonksiyon"""
    import random
    if random.random() < basari_orani:
        return "Başarılı!"
    else:
        raise Exception("İşlem başarısız")

@cache(max_size=5)
def fibonacci(n):
    """Fibonacci hesaplayan fonksiyon (cache'li)"""
    if n <= 1:
        return n
    time.sleep(0.01)  # Hesaplama simulasyonu
    return fibonacci(n-1) + fibonacci(n-2)

print("\n=== Parametreli Decorator'lar ===")

# Retry decorator testi
print("Retry decorator testi:")
try:
    sonuc = hata_verebilecek_fonksiyon(0.8)
    print(f"Sonuç: {sonuc}")
except Exception as e:
    print(f"Final hata: {e}")

# Cache decorator testi
print("\nCache decorator testi:")
print(f"fibonacci(5) = {fibonacci(5)}")
print(f"fibonacci(7) = {fibonacci(7)}")
print(f"fibonacci(5) = {fibonacci(5)}")  # Cache'den gelecek
print(f"Cache info: {fibonacci.cache_info()}")

# =============================================================================
# 4. CLASS-BASED DECORATOR'LAR
# =============================================================================

class CountCalls:
    """Fonksiyon çağrı sayısını sayan class-based decorator"""
    
    def __init__(self, func):
        self.func = func
        self.count = 0
        functools.update_wrapper(self, func)
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} {self.count}. kez çağrıldı")
        return self.func(*args, **kwargs)
    
    def reset_count(self):
        """Sayacı sıfırla"""
        self.count = 0
        print(f"{self.func.__name__} sayacı sıfırlandı")

class RateLimiter:
    """Rate limiting decorator class"""
    
    def __init__(self, max_calls=5, time_window=60):
        self.max_calls = max_calls
        self.time_window = time_window
        self.calls = []
    
    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            
            # Eski çağrıları temizle
            self.calls = [call_time for call_time in self.calls 
                         if now - call_time < self.time_window]
            
            if len(self.calls) >= self.max_calls:
                raise Exception(f"Rate limit aşıldı: {self.max_calls} çağrı/{self.time_window}s")
            
            self.calls.append(now)
            return func(*args, **kwargs)
        
        wrapper.reset_rate_limit = lambda: setattr(self, 'calls', [])
        return wrapper

# Class-based decorator örnekleri
@CountCalls
def say_hello(name):
    return f"Merhaba {name}!"

@RateLimiter(max_calls=3, time_window=5)
def api_call(endpoint):
    return f"API çağrısı: {endpoint}"

print("\n=== Class-Based Decorator'lar ===")

# Count calls testi
for i in range(3):
    print(say_hello(f"User{i}"))

say_hello.reset_count()
print(say_hello("Reset sonrası"))

# Rate limiter testi
print("\nRate limiter testi:")
for i in range(4):
    try:
        result = api_call(f"/endpoint/{i}")
        print(result)
    except Exception as e:
        print(f"Hata: {e}")
        break

# =============================================================================
# 5. PROPERTY DECORATOR'LARI
# =============================================================================

class Temperature:
    """Sıcaklık sınıfı - property decorator örnekleri"""
    
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Celsius getter"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Celsius setter with validation"""
        if value < -273.15:
            raise ValueError("Sıcaklık -273.15°C'nin altında olamaz")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Fahrenheit hesaplaması"""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Fahrenheit setter"""
        self.celsius = (value - 32) * 5/9
    
    @property
    def kelvin(self):
        """Kelvin hesaplaması"""
        return self._celsius + 273.15
    
    @kelvin.setter
    def kelvin(self, value):
        """Kelvin setter"""
        self.celsius = value - 273.15

print("\n=== Property Decorator'ları ===")

temp = Temperature(25)
print(f"Celsius: {temp.celsius}°C")
print(f"Fahrenheit: {temp.fahrenheit}°F")
print(f"Kelvin: {temp.kelvin}K")

temp.fahrenheit = 100
print(f"\nFahrenheit 100°F'ye ayarlandı:")
print(f"Celsius: {temp.celsius}°C")
print(f"Kelvin: {temp.kelvin}K")

# =============================================================================
# 6. VALIDATION DECORATOR'LARI
# =============================================================================

def validate_types(**expected_types):
    """Tip kontrolü yapan decorator"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Argüman isimlerini al
            import inspect
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            
            # Tip kontrolü
            for param_name, expected_type in expected_types.items():
                if param_name in bound_args.arguments:
                    value = bound_args.arguments[param_name]
                    if not isinstance(value, expected_type):
                        raise TypeError(
                            f"{param_name} parametresi {expected_type.__name__} "
                            f"tipinde olmalı, {type(value).__name__} verildi"
                        )
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

def validate_range(**ranges):
    """Değer aralığı kontrolü yapan decorator"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            import inspect
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            
            for param_name, (min_val, max_val) in ranges.items():
                if param_name in bound_args.arguments:
                    value = bound_args.arguments[param_name]
                    if not (min_val <= value <= max_val):
                        raise ValueError(
                            f"{param_name} parametresi {min_val}-{max_val} "
                            f"aralığında olmalı, {value} verildi"
                        )
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Validation decorator örnekleri
@validate_types(name=str, age=int, salary=float)
@validate_range(age=(0, 150), salary=(0, 1000000))
def create_employee(name, age, salary):
    """Çalışan oluşturan fonksiyon"""
    return {
        'name': name,
        'age': age,
        'salary': salary,
        'created_at': datetime.now()
    }

print("\n=== Validation Decorator'ları ===")

# Geçerli çalışan
try:
    employee1 = create_employee("Ali", 30, 5000.0)
    print(f"Çalışan oluşturuldu: {employee1['name']}")
except Exception as e:
    print(f"Hata: {e}")

# Geçersiz tip
try:
    employee2 = create_employee("Ayşe", "otuz", 6000.0)  # Yaş string
except Exception as e:
    print(f"Tip hatası: {e}")

# Geçersiz aralık
try:
    employee3 = create_employee("Mehmet", 200, 5000.0)  # Yaş çok yüksek
except Exception as e:
    print(f"Aralık hatası: {e}")

# =============================================================================
# 7. LOGGİNG DECORATOR'LARI
# =============================================================================

# Logging yapılandırması
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def log_calls(logger=None, level=logging.INFO):
    """Fonksiyon çağrılarını loglayan decorator"""
    if logger is None:
        logger = logging.getLogger(__name__)
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logger.log(level, f"Çağrılıyor: {func.__name__}({args}, {kwargs})")
            
            try:
                result = func(*args, **kwargs)
                logger.log(level, f"Başarılı: {func.__name__} -> {result}")
                return result
            except Exception as e:
                logger.error(f"Hata: {func.__name__} -> {e}")
                raise
        return wrapper
    return decorator

def audit_trail(operation_type="unknown"):
    """Audit trail oluşturan decorator"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            user = kwargs.get('user', 'anonymous')
            
            try:
                result = func(*args, **kwargs)
                end_time = datetime.now()
                duration = (end_time - start_time).total_seconds()
                
                audit_log = {
                    'operation': operation_type,
                    'function': func.__name__,
                    'user': user,
                    'start_time': start_time,
                    'end_time': end_time,
                    'duration': duration,
                    'success': True,
                    'args_count': len(args),
                    'kwargs_count': len(kwargs)
                }
                
                print(f"AUDIT: {audit_log}")
                return result
                
            except Exception as e:
                end_time = datetime.now()
                duration = (end_time - start_time).total_seconds()
                
                audit_log = {
                    'operation': operation_type,
                    'function': func.__name__,
                    'user': user,
                    'start_time': start_time,
                    'end_time': end_time,
                    'duration': duration,
                    'success': False,
                    'error': str(e)
                }
                
                print(f"AUDIT ERROR: {audit_log}")
                raise
                
        return wrapper
    return decorator

# Logging decorator örnekleri
@log_calls()
@audit_trail("database_operation")
def update_user_data(user_id, data, user="admin"):
    """Kullanıcı verisi güncelleme fonksiyonu"""
    print(f"Kullanıcı {user_id} verisi güncelleniyor...")
    if user_id <= 0:
        raise ValueError("Geçersiz kullanıcı ID")
    return f"Kullanıcı {user_id} güncellendi"

print("\n=== Logging Decorator'ları ===")

# Başarılı işlem
try:
    result = update_user_data(123, {'name': 'Yeni İsim'}, user='admin')
    print(f"Sonuç: {result}")
except Exception as e:
    print(f"Hata: {e}")

print()

# Hatalı işlem
try:
    result = update_user_data(-1, {'name': 'Geçersiz'}, user='admin')
except Exception as e:
    print(f"Beklenen hata yakalandı: {e}")

# =============================================================================
# 8. DECORATOR CHAINING
# =============================================================================

def deprecated(reason="Bu fonksiyon kullanımdan kaldırılmıştır"):
    """Deprecated uyarısı veren decorator"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            warnings.warn(
                f"{func.__name__} deprecated: {reason}",
                DeprecationWarning,
                stacklevel=2
            )
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Çoklu decorator kullanımı
@deprecated("Yeni sürümde kaldırılacak")
@timing_decorator
@cache(max_size=10)
@log_calls(level=logging.WARNING)
def eski_fonksiyon(x):
    """Deprecated olan örnek fonksiyon"""
    time.sleep(0.01)  # Simulated work
    return x * x

print("\n=== Decorator Chaining ===")

# Deprecated fonksiyonu çağır
with warnings.catch_warnings(record=True) as w:
    warnings.simplefilter("always")
    result1 = eski_fonksiyon(5)
    result2 = eski_fonksiyon(5)  # Cache'den gelecek
    
    if w:
        print(f"Warning: {w[0].message}")

# =============================================================================
# 9. ASYNC DECORATOR'LAR
# =============================================================================

import asyncio

def async_timing(func):
    """Async fonksiyonlar için timing decorator"""
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        end_time = time.time()
        print(f"Async {func.__name__} {end_time - start_time:.4f} saniyede çalıştı")
        return result
    return wrapper

def async_retry(max_attempts=3, delay=1):
    """Async fonksiyonlar için retry decorator"""
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            last_exception = None
            
            for attempt in range(max_attempts):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"Async deneme {attempt + 1}/{max_attempts} başarısız: {e}")
                    if attempt < max_attempts - 1:
                        await asyncio.sleep(delay)
            
            raise last_exception
            
        return wrapper
    return decorator

# Async decorator örnekleri
@async_timing
@async_retry(max_attempts=2)
async def async_api_call(url):
    """Simulated async API call"""
    await asyncio.sleep(0.1)  # Simulate network delay
    
    # Simulate occasional failure
    import random
    if random.random() < 0.3:
        raise Exception("Network error")
    
    return f"Data from {url}"

async def run_async_examples():
    """Async decorator örneklerini çalıştır"""
    print("\n=== Async Decorator'lar ===")
    
    try:
        result = await async_api_call("https://api.example.com")
        print(f"Async sonuç: {result}")
    except Exception as e:
        print(f"Async hata: {e}")

# Async örnekleri çalıştır
try:
    asyncio.run(run_async_examples())
except Exception as e:
    print(f"Async örnek çalıştırılamadı: {e}")

# =============================================================================
# 10. CUSTOM DECORATOR FACTORY
# =============================================================================

def create_decorator(before_func=None, after_func=None, on_error_func=None):
    """Özelleştirilebilir decorator factory"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Before function
            if before_func:
                before_func(func, args, kwargs)
            
            try:
                result = func(*args, **kwargs)
                
                # After function
                if after_func:
                    after_func(func, args, kwargs, result)
                
                return result
                
            except Exception as e:
                # Error function
                if on_error_func:
                    on_error_func(func, args, kwargs, e)
                raise
                
        return wrapper
    return decorator

# Custom decorator factory kullanımı
def before_execution(func, args, kwargs):
    print(f"[BEFORE] {func.__name__} çalıştırılacak")

def after_execution(func, args, kwargs, result):
    print(f"[AFTER] {func.__name__} sonucu: {type(result).__name__}")

def on_error(func, args, kwargs, error):
    print(f"[ERROR] {func.__name__} hata verdi: {error}")

@create_decorator(
    before_func=before_execution,
    after_func=after_execution,
    on_error_func=on_error
)
def sample_function(x, y):
    """Örnek fonksiyon"""
    if x < 0:
        raise ValueError("x negatif olamaz")
    return x + y

print("\n=== Custom Decorator Factory ===")

# Başarılı çalışma
result = sample_function(5, 3)
print(f"Sonuç: {result}")

print()

# Hatalı çalışma
try:
    sample_function(-1, 3)
except ValueError as e:
    print(f"Yakalanan hata: {e}")

print("\n" + "="*50)
print("İLERİ DÜZEY DECORATOR'LAR TAMAMLANDI")
print("="*50)

# Son özet
print("\nDecorator Türleri Özeti:")
print("1. Basit decorator'lar")
print("2. Parametreli decorator'lar") 
print("3. Class-based decorator'lar")
print("4. Property decorator'ları")
print("5. Validation decorator'ları")
print("6. Logging decorator'ları")
print("7. Decorator chaining")
print("8. Async decorator'lar")
print("9. Custom decorator factory")