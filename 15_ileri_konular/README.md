# Python İleri Konular

Bu bölümde Python'un ileri düzey özelliklerini ve modern programlama tekniklerini öğreniyoruz. Generator'lar, decorator'lar, asenkron programlama ve tip belirtimi gibi konular ele alınacak.

## 📚 İçerik

### 1. Generator'lar ve Yield
- Generator fonksiyonları nedir?
- `yield` anahtar kelimesi kullanımı
- Generator expression'ları
- Memory efficient iteration
- Generator composition

### 2. İleri Düzey Decorator'lar
- Decorator nedir ve nasıl çalışır?
- Parametreli decorator'lar
- Class-based decorator'lar
- Property decorator'ları
- Method decorator'ları
- Decorator chaining

### 3. Context Manager'lar
- `with` statement kullanımı
- `__enter__` ve `__exit__` metodları
- Custom context manager'lar
- `contextlib` modülü
- Exception handling in context managers

### 4. Type Hints ve Annotations
- Type annotations nedir?
- Built-in types
- Generic types
- Union types
- Optional ve None handling
- `typing` modülü

### 5. Asenkron Programlama
- `async` ve `await` anahtar kelimeleri
- Coroutine'ler
- Event loop
- `asyncio` modülü
- Concurrent execution

## 🎯 Öğrenme Hedefleri

Bu bölümü tamamladıktan sonra şunları yapabileceksiniz:

- [ ] Generator fonksiyonları yazabilmek
- [ ] Custom decorator'lar oluşturabilmek
- [ ] Context manager'lar kullanabilmek
- [ ] Type hints ile kod yazabilmek
- [ ] Asenkron programlama yapabilmek
- [ ] Memory-efficient kod yazabilmek
- [ ] Modern Python standartlarına uygun kod yazabilmek

## 📝 Örnek Dosyalar

1. **generator_kullanimi.py** - Generator fonksiyonları ve yield kullanımı
2. **ileri_decoratorler.py** - Advanced decorator patterns
3. **context_managers.py** - Custom context manager implementations
4. **type_hints.py** - Type annotation examples
5. **async_programlama.py** - Asynchronous programming examples

## 💡 Temel Kavramlar

### Generator Örneği
```python
def fibonacci_generator(n):
    """Fibonacci sayıları üreten generator"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Kullanım
for num in fibonacci_generator(10):
    print(num)
```

### Decorator Örneği  
```python
def timing_decorator(func):
    """Fonksiyon çalışma süresini ölçen decorator"""
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} {end - start:.4f} saniyede çalıştı")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)
    return "Tamamlandı"
```

### Context Manager Örneği
```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# Kullanım
with FileManager('test.txt', 'w') as f:
    f.write('Merhaba Dünya!')
```

### Type Hints Örneği
```python
from typing import List, Dict, Optional

def process_scores(scores: List[int]) -> Dict[str, float]:
    """Puanları işleyip istatistikleri döndürür"""
    return {
        'average': sum(scores) / len(scores),
        'max': max(scores),
        'min': min(scores)
    }

def find_user(user_id: int) -> Optional[Dict[str, str]]:
    """Kullanıcıyı bulur, bulamazsa None döndürür"""
    # Implementation here
    pass
```

### Async Programlama Örneği
```python
import asyncio
import aiohttp

async def fetch_url(session, url):
    """URL'den veri çeken asenkron fonksiyon"""
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = ['https://example.com', 'https://python.org']
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        
    for result in results:
        print(f"Sayfa uzunluğu: {len(result)}")

# Çalıştırma
asyncio.run(main())
```

## ⚠️ Önemli Notlar

- Generator'lar bellekte verimlidir çünkü tüm değerleri aynı anda tutmazlar
- Decorator'lar kod tekrarını azaltır ve cross-cutting concern'leri ele alır
- Context manager'lar resource yönetimini güvenli hale getirir
- Type hints kod okunabilirliğini artırır ve IDE desteği sağlar
- Async programlama I/O bound işlemlerde performans artırır

Bu bölüm Python'da ileri düzey programlama tekniklerinin temelini oluşturur!