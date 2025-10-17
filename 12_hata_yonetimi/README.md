# 🚨 Hata Yönetimi (Error Handling)

Python'da hata yönetimi, exception handling, debugging teknikleri ve logging sisteminin kapsamlı öğrenimi.

## 📚 Kapsam

Bu bölümde Python'da hata yönetiminin tüm yönlerini öğreneceksiniz:

### 🎯 Temel Hata Yönetimi
- try/except/finally blokları
- Exception türleri ve hiyerarşi
- Hata yakalama teknikleri
- Exception propagation
- Defensive programming

### 🔍 Hata Türleri
- Built-in exception'lar
- ArithmeticError, TypeError, ValueError
- LookupError (IndexError, KeyError)
- OSError ve alt türleri
- Import ve Name hataları
- Unicode ve encoding hataları

### ⚡ Özel Hatalar
- Custom exception sınıfları
- Exception chaining
- Context managers ile hata yönetimi
- Validation ve error reporting
- Best practices

### 🐛 Debugging Teknikleri
- Python Debugger (pdb) kullanımı
- Traceback analizi
- Code inspection ve introspection
- Profiling ve performance debugging
- Memory debugging

### 📊 Logging Sistemi
- Logger configuration
- Handlers ve formatters
- Structured logging (JSON)
- Production logging
- Monitoring ve alerting

## 🎯 Öğrenme Hedefleri

Bu bölümü tamamladığınızda şunları öğrenmiş olacaksınız:

### 🛡️ Hata Yönetimi Becerileri
- ✅ Hataları doğru şekilde yakalama ve işleme
- ✅ Exception hiyerarşisini anlama ve kullanma
- ✅ Özel exception sınıfları oluşturma
- ✅ Hata zinciri (exception chaining) kullanma
- ✅ Context-aware hata yönetimi

### 🔧 Debugging Teknikleri
- ✅ PDB debugger'ı etkili kullanma
- ✅ Traceback analizi yapma
- ✅ Code inspection teknikleri
- ✅ Performance profiling
- ✅ Memory leak detection

### 📝 Logging Mastery
- ✅ Production-ready logging sistemleri kurma
- ✅ Structured logging uygulama
- ✅ Log monitoring ve alerting
- ✅ Thread-safe logging
- ✅ Configuration-based setup

### 🏗️ Production Skills
- ✅ Error handling best practices
- ✅ Defensive programming teknikleri
- ✅ Production debugging
- ✅ Log aggregation ve analysis
- ✅ Error monitoring sistemleri

## 📁 Örnek Dosyalar

### 1. 📖 `temel_hata_yonetimi.py`
**Temel exception handling teknikleri**
- try/except/finally kullanımı
- Multiple exception handling
- Exception propagation
- Defensive programming
- Error handling patterns

```python
# Temel hata yakalama
try:
    result = risky_operation()
except SpecificError as e:
    handle_specific_error(e)
except Exception as e:
    handle_general_error(e)
finally:
    cleanup_resources()
```

### 2. 🎭 `hata_turleri.py`
**Python exception türleri ve hiyerarşi**
- Built-in exception'lar
- ArithmeticError ailesi
- LookupError türleri
- Type ve Value hataları
- OS ve Import hataları

```python
# Exception hiyerarşisi
try:
    operation()
except LookupError:  # IndexError, KeyError'ı yakalar
    handle_lookup_error()
except ArithmeticError:  # ZeroDivisionError'ı yakalar
    handle_math_error()
```

### 3. ⚡ `ozel_hatalar.py`
**Custom exception'lar ve advanced handling**
- Özel exception sınıfları
- Exception chaining
- Context managers
- Validation frameworks
- Error reporting

```python
# Özel hata sınıfı
class ValidationError(Exception):
    def __init__(self, field, value, message):
        self.field = field
        self.value = value
        super().__init__(message)

# Exception chaining
try:
    low_level_operation()
except LowLevelError as e:
    raise HighLevelError("Operation failed") from e
```

### 4. 🐛 `debugging_teknikleri.py`
**Debugging araçları ve teknikleri**
- PDB debugger kullanımı
- Traceback analizi
- Code inspection
- Performance profiling
- Memory debugging

```python
import pdb

def debug_function():
    pdb.set_trace()  # Breakpoint
    result = complex_operation()
    return result

# Profiling
import cProfile
cProfile.run('expensive_function()')
```

### 5. 📊 `logging_kullanimi.py`
**Comprehensive logging sistemi**
- Logger configuration
- Multiple handlers
- JSON structured logging
- Production setup
- Monitoring

```python
# Structured logging
logger = logging.getLogger('app')
logger.info(
    "User action",
    extra={
        'user_id': 12345,
        'action': 'login',
        'ip': '192.168.1.1'
    }
)
```

## 🎖️ Practical Projects

### 🔥 Project 1: Error Handling Framework
```python
class ErrorHandler:
    def __init__(self):
        self.handlers = {}
    
    def register_handler(self, exception_type, handler):
        self.handlers[exception_type] = handler
    
    def handle_error(self, exception):
        handler = self.handlers.get(type(exception))
        if handler:
            return handler(exception)
        return self.default_handler(exception)
```

### 📊 Project 2: Application Monitoring
```python
class AppMonitor:
    def __init__(self):
        self.metrics = defaultdict(int)
        self.logger = self.setup_logger()
    
    def track_error(self, error):
        self.metrics['errors'] += 1
        self.logger.error("Error occurred", extra={
            'error_type': type(error).__name__,
            'error_message': str(error)
        })
```

### 🛠️ Project 3: Development Tools
```python
class DebugTools:
    @staticmethod
    def performance_monitor(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            try:
                result = func(*args, **kwargs)
                return result
            finally:
                duration = time.time() - start
                print(f"{func.__name__}: {duration:.4f}s")
        return wrapper
```

## 🚀 İleri Seviye Konular

### 🎯 Advanced Error Handling
- Custom context managers
- Error aggregation
- Circuit breaker pattern
- Retry mechanisms
- Graceful degradation

### 🔍 Production Debugging
- Remote debugging
- Live system analysis
- Log analysis tools
- Performance monitoring
- APM integration

### 📈 Observability
- Metrics collection
- Distributed tracing
- Health checks
- SLA monitoring
- Incident response

## 💡 Best Practices

### ✅ Hata Yönetimi
- Spesifik exception'ları yakala
- Exception'ları yukarı propagate et
- Cleanup kodunu finally'de yaz
- Error context'i koru
- User-friendly error mesajları

### ✅ Debugging
- Sistematik yaklaşım
- Binary search technique
- Minimal test cases
- Documentation
- Code review

### ✅ Logging
- Structured logging kullan
- Appropriate log levels
- Sensitive data protection
- Performance considerations
- Centralized logging

## 🎯 Sonraki Adımlar

Bu bölümü tamamladıktan sonra:
1. **Modüller ve Paketler** - Code organization
2. **File I/O Operations** - Dosya işlemleri  
3. **Database Integration** - Veritabanı entegrasyonu
4. **Web Development** - Web framework'leri
5. **Testing** - Unit testing ve TDD

## 📚 Ek Kaynaklar

- **Python Documentation**: Exception handling
- **PEP 8**: Error handling style guide
- **PEP 282**: Logging facility
- **Books**: "Effective Python" by Brett Slatkin
- **Tools**: Sentry, New Relic, DataDog

---

🎯 **Hedef**: Production-ready error handling ve debugging skills kazanın!

⚡ **Practice**: Her gün debugging tools kullanın!

🚀 **Level Up**: Open source projelerde error handling inceleyin!