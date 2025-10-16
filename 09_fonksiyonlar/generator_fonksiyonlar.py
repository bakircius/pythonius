# Generator Fonksiyonlar ve Yield
# Python'da generator fonksiyonlar ile memory-efficient programlama

print("=== GENERATOR FONKSİYONLAR VE YIELD ===\n")

print("1. GENERATOR NEDİR?")
print("-" * 19)

print("Generator:")
print("• Değerleri tek seferde değil, ihtiyaç duyuldukça üretir")
print("• Memory-efficient - büyük veri setleri için ideal")
print("• Lazy evaluation - tembel değerlendirme")
print("• Iterator protocol uygular")
print("• yield keyword'ü ile oluşturulur")

# Basit generator örneği
def simple_generator():
    """Basit generator fonksiyonu"""
    print("Generator başladı")
    yield 1
    print("İlk yield'den sonra")
    yield 2
    print("İkinci yield'den sonra")
    yield 3
    print("Generator bitti")

print(f"\nBasit generator örneği:")
gen = simple_generator()
print(f"Generator object: {gen}")
print(f"Type: {type(gen)}")

print(f"\nGenerator değerlerini çek:")
print(f"İlk değer: {next(gen)}")
print(f"İkinci değer: {next(gen)}")
print(f"Üçüncü değer: {next(gen)}")

# StopIteration exception
try:
    print(f"Dördüncü değer: {next(gen)}")
except StopIteration:
    print("Generator tükendi - StopIteration exception")

print("\n2. GENERATOR vs NORMAL FONKSİYON:")
print("-" * 34)

# Normal fonksiyon - liste döndür
def normal_numbers(n):
    """Normal fonksiyon - liste döndürür"""
    result = []
    for i in range(n):
        result.append(i * i)
    return result

# Generator fonksiyon - yield kullan
def generator_numbers(n):
    """Generator fonksiyon - yield kullanır"""
    for i in range(n):
        yield i * i

print("Normal fonksiyon vs Generator:")

# Normal fonksiyon kullanımı
normal_result = normal_numbers(5)
print(f"Normal result: {normal_result}")
print(f"Normal memory: {normal_result.__sizeof__()} bytes")

# Generator kullanımı
gen_result = generator_numbers(5)
print(f"Generator result: {gen_result}")
print(f"Generator memory: {gen_result.__sizeof__()} bytes")

print(f"\nGenerator değerleri:")
for value in gen_result:
    print(f"  {value}")

# Memory comparison için büyük sayılar
import sys

def normal_big_numbers(n):
    return [i for i in range(n)]

def generator_big_numbers(n):
    for i in range(n):
        yield i

n = 1000
normal_big = normal_big_numbers(n)
gen_big = generator_big_numbers(n)

print(f"\n{n} elemanlı liste:")
print(f"Normal liste: {sys.getsizeof(normal_big)} bytes")
print(f"Generator: {sys.getsizeof(gen_big)} bytes")
print(f"Memory farkı: {sys.getsizeof(normal_big) / sys.getsizeof(gen_big):.1f}x")

print("\n3. GENERATOR EXPRESSİONS:")
print("-" * 27)

print("List comprehension vs Generator expression:")

# List comprehension
list_comp = [x*2 for x in range(10)]
print(f"List comprehension: {list_comp}")
print(f"Memory: {sys.getsizeof(list_comp)} bytes")

# Generator expression
gen_exp = (x*2 for x in range(10))
print(f"Generator expression: {gen_exp}")
print(f"Memory: {sys.getsizeof(gen_exp)} bytes")

print(f"\nGenerator expression değerleri:")
for value in gen_exp:
    print(f"  {value}")

# Nested generator expressions
print(f"\nNested generator expressions:")
nested_gen = ((x, y) for x in range(3) for y in range(2))
for pair in nested_gen:
    print(f"  {pair}")

# Conditional generator expression
even_squares = (x*x for x in range(10) if x % 2 == 0)
print(f"Çift sayıların kareleri: {list(even_squares)}")

print("\n4. GENERATOR STATE VE YIELD DAVRANIŞI:")
print("-" * 38)

def stateful_generator():
    """Durumu koruyan generator"""
    print("Generator init")
    state = 0
    
    while True:
        print(f"State: {state}")
        value = yield state
        print(f"Received: {value}")
        
        if value is not None:
            state = value
        else:
            state += 1
        
        if state > 5:
            break
    
    print("Generator finished")

print("Stateful generator örneği:")
stateful_gen = stateful_generator()

# İlk next() çağrısı
print(f"İlk next(): {next(stateful_gen)}")

# send() ile değer gönder
print(f"send(10): {stateful_gen.send(10)}")
print(f"send(None): {stateful_gen.send(None)}")

# Normal next() devam
print(f"Normal next(): {next(stateful_gen)}")

print("\n5. GENERATOR METHODS:")
print("-" * 20)

def demo_generator():
    """Generator methodları demo"""
    try:
        for i in range(10):
            print(f"Yielding {i}")
            received = yield i
            if received is not None:
                print(f"Received: {received}")
    except GeneratorExit:
        print("Generator kapatılıyor...")
    except Exception as e:
        print(f"Exception alındı: {e}")
        yield -1  # Exception sonrası devam edebilir
    finally:
        print("Generator cleanup")

print("Generator methods demo:")
demo_gen = demo_generator()

# next() method
print(f"1. next(): {next(demo_gen)}")
print(f"2. next(): {next(demo_gen)}")

# send() method
print(f"3. send('hello'): {demo_gen.send('hello')}")

# throw() method - exception gönder
print(f"4. throw(ValueError): {demo_gen.throw(ValueError, 'Test exception')}")

# close() method - generator'ı kapat
demo_gen.close()

# Kapatılmış generator'a erişim
try:
    next(demo_gen)
except StopIteration:
    print("Generator kapatılmış")

print("\n6. YIELD FROM:")
print("-" * 14)

def sub_generator():
    """Alt generator"""
    yield "Sub 1"
    yield "Sub 2"
    yield "Sub 3"

def main_generator_old():
    """Eski yöntem - manuel iteration"""
    for value in sub_generator():
        yield value
    yield "Main son"

def main_generator_new():
    """Yeni yöntem - yield from"""
    yield from sub_generator()
    yield "Main son"

print("yield from karşılaştırması:")
print("Eski yöntem:")
for value in main_generator_old():
    print(f"  {value}")

print("Yeni yöntem (yield from):")
for value in main_generator_new():
    print(f"  {value}")

# yield from ile veri aktarımı
def delegator():
    """yield from ile bidirectional communication"""
    result = yield from sub_generator_with_input()
    return f"Result: {result}"

def sub_generator_with_input():
    """Input alabilen sub generator"""
    received = yield "İlk değer"
    yield f"Aldım: {received}"
    return "Sub generator return value"

print(f"\nyield from ile bidirectional:")
delegator_gen = delegator()
print(f"İlk: {next(delegator_gen)}")
try:
    print(f"Send: {delegator_gen.send('Test input')}")
    next(delegator_gen)
except StopIteration as e:
    print(f"Return value: {e.value}")

print("\n7. GENERATOR PIPELINE:")
print("-" * 21)

def numbers(max_num):
    """Sayı üretici"""
    for i in range(max_num):
        print(f"Generating {i}")
        yield i

def squares(gen):
    """Kare alma filter"""
    for num in gen:
        square = num * num
        print(f"Squaring {num} = {square}")
        yield square

def even_only(gen):
    """Sadece çift sayılar"""
    for num in gen:
        if num % 2 == 0:
            print(f"Passing even {num}")
            yield num

# Pipeline oluştur
print("Generator pipeline:")
pipeline = even_only(squares(numbers(6)))

print("Pipeline sonuçları:")
for result in pipeline:
    print(f"Final result: {result}")

# Daha karmaşık pipeline
def file_lines(filename):
    """Dosya satır generator (simülasyon)"""
    lines = [
        "Python generator tutorial",
        "Generator functions are awesome",
        "Memory efficient programming",
        "Yield keyword is powerful",
        "Pipeline processing rocks"
    ]
    for line in lines:
        yield line

def grep(pattern, lines):
    """Grep benzeri filter"""
    for line in lines:
        if pattern.lower() in line.lower():
            yield line

def uppercase(lines):
    """Büyük harfe çevir"""
    for line in lines:
        yield line.upper()

print(f"\nFile processing pipeline:")
file_pipeline = uppercase(grep("generator", file_lines("dummy.txt")))
for line in file_pipeline:
    print(f"  {line}")

print("\n8. GENERATOR İLE INFINITE SEQUENCES:")
print("-" * 35)

def fibonacci():
    """Sonsuz Fibonacci dizisi"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def primes():
    """Sonsuz asal sayı dizisi"""
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

print("Sonsuz diziler:")
print("İlk 10 Fibonacci sayısı:")
fib = fibonacci()
for i, num in enumerate(fib):
    if i >= 10:
        break
    print(f"  F({i}) = {num}")

print("İlk 10 asal sayı:")
prime_gen = primes()
for i, prime in enumerate(prime_gen):
    if i >= 10:
        break
    print(f"  {i+1}. asal = {prime}")

# Sonsuz counter
def counter(start=0, step=1):
    """Sonsuz counter"""
    while True:
        yield start
        start += step

print("Counter örneği:")
count = counter(10, 2)
for i, num in enumerate(count):
    if i >= 5:
        break
    print(f"  {num}")

print("\n9. GENERATOR DECORATORS VE ADVANCED KULLANIM:")
print("-" * 42)

def generator_decorator(func):
    """Generator için decorator"""
    def wrapper(*args, **kwargs):
        print(f"Generator {func.__name__} başlıyor...")
        gen = func(*args, **kwargs)
        try:
            while True:
                value = next(gen)
                print(f"Yielded: {value}")
                yield value
        except StopIteration:
            print(f"Generator {func.__name__} bitti")
    return wrapper

@generator_decorator
def decorated_generator(n):
    """Decorator'lı generator"""
    for i in range(n):
        yield i * 2

print("Decorated generator:")
for value in decorated_generator(3):
    print(f"Received: {value}")

# Generator context manager
class GeneratorContext:
    """Generator için context manager"""
    
    def __init__(self, generator_func, *args, **kwargs):
        self.generator_func = generator_func
        self.args = args
        self.kwargs = kwargs
        self.generator = None
    
    def __enter__(self):
        print("Generator context başladı")
        self.generator = self.generator_func(*self.args, **self.kwargs)
        return self.generator
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Generator context kapanıyor")
        if self.generator:
            self.generator.close()

print(f"\nGenerator context manager:")
with GeneratorContext(numbers, 3) as gen:
    for value in gen:
        print(f"  Context value: {value}")

# Generator chaining
def chain_generators(*generators):
    """Çoklu generator chain"""
    for gen in generators:
        yield from gen

gen1 = (x for x in range(3))
gen2 = (x*10 for x in range(2))
gen3 = (x*100 for x in range(2))

print(f"Chained generators:")
for value in chain_generators(gen1, gen2, gen3):
    print(f"  {value}")

print("\n10. GENERATOR PERFORMANCE VE MEMORY:")
print("-" * 34)

import time
import tracemalloc

def performance_test():
    """Generator performance testi"""
    n = 100000
    
    # List comprehension
    print(f"{n} elemanlı performance testi:")
    
    # Memory tracking başlat
    tracemalloc.start()
    
    # List - time and memory
    start_time = time.time()
    list_result = [x*2 for x in range(n)]
    list_time = time.time() - start_time
    current, peak = tracemalloc.get_traced_memory()
    list_memory = peak
    
    tracemalloc.stop()
    tracemalloc.start()
    
    # Generator - time and memory
    start_time = time.time()
    gen_result = (x*2 for x in range(n))
    # Generator'ı consume et
    for _ in gen_result:
        pass
    gen_time = time.time() - start_time
    current, peak = tracemalloc.get_traced_memory()
    gen_memory = peak
    
    tracemalloc.stop()
    
    print(f"List time: {list_time*1000:.2f} ms")
    print(f"Generator time: {gen_time*1000:.2f} ms")
    print(f"List memory: {list_memory/1024/1024:.2f} MB")
    print(f"Generator memory: {gen_memory/1024/1024:.2f} MB")
    print(f"Memory saving: {list_memory/gen_memory:.1f}x")

performance_test()

# Large dataset simulation
def large_dataset_processor():
    """Büyük veri seti işleme simulation"""
    def process_chunk(chunk_size=1000):
        """Chunk'lar halinde işle"""
        for i in range(0, 1000000, chunk_size):
            chunk = range(i, min(i + chunk_size, 1000000))
            yield [x*2 for x in chunk]
    
    total = 0
    chunk_count = 0
    
    for chunk in process_chunk():
        total += sum(chunk)
        chunk_count += 1
        if chunk_count % 100 == 0:
            print(f"İşlenen chunk: {chunk_count}")
    
    return total

print(f"\nBüyük veri seti işleme:")
result = large_dataset_processor()
print(f"Toplam: {result}")

print("\n11. GENERATOR BEST PRACTİCES:")
print("-" * 29)

print("✓ İYİ PRATİKLER:")
print("1. Büyük veri setleri için generator kullanın")
print("2. Memory-intensive işlemler için lazy evaluation")
print("3. Pipeline processing için generator chain")
print("4. Infinite sequences için generator")
print("5. yield from ile delegation")

print("\n✗ YAYGN HATALAR:")
print("1. Generator'ı birden fazla kez iterate etmeye çalışmak")
print("2. Generator state'ini yanlış yönetmek")
print("3. Exception handling'i ihmal etmek")
print("4. Performance'ı test etmeden kullanmak")
print("5. Generator close() methodunu ihmal etmek")

# Common mistakes demonstration
def mistake_demo():
    """Yaygın hataları göster"""
    
    # Hata 1: Generator'ı birden fazla iterate
    gen = (x for x in range(3))
    print(f"İlk iteration: {list(gen)}")
    print(f"İkinci iteration: {list(gen)}")  # Boş!
    
    # Çözüm: Yeniden oluştur veya tee kullan
    from itertools import tee
    
    gen = (x for x in range(3))
    gen1, gen2 = tee(gen)
    print(f"Tee ile ilk: {list(gen1)}")
    print(f"Tee ile ikinci: {list(gen2)}")

print(f"\nYaygın hatalar demo:")
mistake_demo()

print("\n=== GENERATOR FONKSİYONLAR ÖZETİ ===")
print("Temel Kavramlar:")
print("  • yield - değer üret ve bekle")
print("  • Generator object - iterator protocol")
print("  • Lazy evaluation - ihtiyaç duyuldukça hesapla")
print("  • Memory efficient - büyük veri için ideal")
print()
print("Generator Methods:")
print("  • next() - sonraki değeri al")
print("  • send() - değer gönder")
print("  • throw() - exception fırlat")
print("  • close() - generator'ı kapat")
print()
print("Advanced Özellikler:")
print("  • yield from - delegation")
print("  • Generator expressions")
print("  • Generator pipelines")
print("  • Infinite sequences")
print()
print("Kullanım Alanları:")
print("  • Büyük dosya işleme")
print("  • Data streaming")
print("  • Pipeline processing")
print("  • Memory optimization")
print("  • Infinite sequences")
print()
print("Performance Faydaları:")
print("  • Düşük memory kullanımı")
print("  • Lazy computation")
print("  • Scalable processing")
print("  • Better resource management")