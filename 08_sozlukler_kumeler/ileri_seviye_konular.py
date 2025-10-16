# Sözlük ve Küme İleri Seviye Konular
# Python sözlük ve küme veri tiplerinin ileri seviye kullanımları

print("=== SÖZLÜK VE KÜME İLERİ SEVİYE KONULAR ===\n")

print("1. COLLECTIONS MODÜLÜ:")
print("-" * 23)

from collections import defaultdict, Counter, OrderedDict, ChainMap, UserDict

# defaultdict - varsayılan değerli sözlük
print("defaultdict kullanımı:")

# Normal sözlük problemi
normal_dict = {}
try:
    normal_dict["yok"].append(1)  # KeyError!
except KeyError as e:
    print(f"Normal dict hatası: {e}")

# defaultdict çözümü
dd_list = defaultdict(list)
dd_list["var_olmayan"].append(1)
dd_list["var_olmayan"].append(2)
print(f"defaultdict(list): {dict(dd_list)}")

dd_int = defaultdict(int)
dd_int["sayac"] += 1
dd_int["sayac"] += 1
print(f"defaultdict(int): {dict(dd_int)}")

# Özel factory function
def default_set():
    return set()

dd_set = defaultdict(default_set)
dd_set["grup1"].add("eleman1")
dd_set["grup1"].add("eleman2")
print(f"defaultdict(set): {dict(dd_set)}")

# Nested defaultdict
def make_nested_dict():
    return defaultdict(int)

nested_dd = defaultdict(make_nested_dict)
nested_dd["seviye1"]["seviye2"] = 42
print(f"Nested defaultdict: {dict(nested_dd)}")

# Counter - sayma işlemleri
print(f"\nCounter kullanımı:")
kelimeler = ["python", "java", "python", "go", "java", "python"]
sayac = Counter(kelimeler)
print(f"Kelime sayacı: {sayac}")

# Counter metotları
print(f"En sık 2: {sayac.most_common(2)}")
print(f"Python sayısı: {sayac['python']}")
print(f"C++ sayısı: {sayac['c++']}")  # 0 döner

# Counter aritmetiği
sayac1 = Counter("hello")
sayac2 = Counter("world")
print(f"Counter1: {sayac1}")
print(f"Counter2: {sayac2}")
print(f"Toplam: {sayac1 + sayac2}")
print(f"Çıkarma: {sayac1 - sayac2}")
print(f"Kesişim: {sayac1 & sayac2}")
print(f"Birleşim: {sayac1 | sayac2}")

# OrderedDict (Python 3.7+ normal dict sıralı)
print(f"\nOrderedDict:")
od = OrderedDict()
od["üçüncü"] = 3
od["birinci"] = 1
od["ikinci"] = 2
print(f"OrderedDict: {od}")

# move_to_end metodu
od.move_to_end("birinci")
print(f"move_to_end: {od}")

# ChainMap - çoklu sözlük
print(f"\nChainMap:")
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 20, "c": 3}
dict3 = {"c": 30, "d": 4}

cm = ChainMap(dict1, dict2, dict3)
print(f"ChainMap: {dict(cm)}")
print(f"'b' değeri: {cm['b']}")  # İlk bulunanı alır

# Yeni map ekleme
dict4 = {"e": 5}
cm = cm.new_child(dict4)
print(f"new_child: {dict(cm)}")

print("\n2. DICT VE SET SUBCLASSING:")
print("-" * 28)

# UserDict - sözlük alt sınıfı
class CaselessDict(UserDict):
    """Büyük/küçük harf duyarsız sözlük"""
    
    def __setitem__(self, key, value):
        super().__setitem__(key.lower() if isinstance(key, str) else key, value)
    
    def __getitem__(self, key):
        return super().__getitem__(key.lower() if isinstance(key, str) else key)
    
    def __contains__(self, key):
        return super().__contains__(key.lower() if isinstance(key, str) else key)

caseless = CaselessDict()
caseless["Name"] = "Ali"
caseless["AGE"] = 25

print(f"CaselessDict: {caseless}")
print(f"name: {caseless['name']}")
print(f"NAME: {caseless['NAME']}")
print(f"'AGE' in dict: {'age' in caseless}")

# Custom Set
class LoggingSet(set):
    """İşlemleri loglayan küme"""
    
    def add(self, element):
        print(f"Adding {element}")
        super().add(element)
    
    def remove(self, element):
        print(f"Removing {element}")
        super().remove(element)

log_set = LoggingSet([1, 2, 3])
log_set.add(4)
log_set.remove(2)

print("\n3. MEMORY VE PERFORMANCE OPTİMİZASYONU:")
print("-" * 38)

import sys
import time

# Sözlük vs Liste bellek kullanımı
print("Bellek kullanımı analizi:")

# Küçük veri
small_list = list(range(100))
small_dict = {i: i for i in range(100)}
small_set = set(range(100))

print(f"100 eleman:")
print(f"  Liste: {sys.getsizeof(small_list)} byte")
print(f"  Sözlük: {sys.getsizeof(small_dict)} byte")
print(f"  Küme: {sys.getsizeof(small_set)} byte")

# Büyük veri
big_list = list(range(10000))
big_dict = {i: i for i in range(10000)}
big_set = set(range(10000))

print(f"10000 eleman:")
print(f"  Liste: {sys.getsizeof(big_list)} byte")
print(f"  Sözlük: {sys.getsizeof(big_dict)} byte")
print(f"  Küme: {sys.getsizeof(big_set)} byte")

# Dict keys optimization
class OptimizedDict:
    """Key'leri tuple olarak saklayan optimized dict"""
    
    def __init__(self):
        self._keys = []
        self._values = []
    
    def __setitem__(self, key, value):
        if key in self._keys:
            index = self._keys.index(key)
            self._values[index] = value
        else:
            self._keys.append(key)
            self._values.append(value)
    
    def __getitem__(self, key):
        index = self._keys.index(key)
        return self._values[index]

# Set operations performance
def set_performance_test():
    # Büyük setler
    set1 = set(range(10000))
    set2 = set(range(5000, 15000))
    
    # Union performansı
    start = time.time()
    union_result = set1 | set2
    union_time = time.time() - start
    
    # Intersection performansı
    start = time.time()
    intersection_result = set1 & set2
    intersection_time = time.time() - start
    
    print(f"\nSet operations (10000 eleman):")
    print(f"Union: {union_time*1000:.3f} ms")
    print(f"Intersection: {intersection_time*1000:.3f} ms")

set_performance_test()

print("\n4. HASH TABLES VE COLLISION HANDLING:")
print("-" * 37)

# Hash function örnekleri
def simple_hash(key, size=10):
    """Basit hash fonksiyonu"""
    return sum(ord(c) for c in str(key)) % size

# Hash collision örneği
keys = ["abc", "bca", "cab"]  # Aynı karakterler, farklı sıra
for key in keys:
    hash_val = simple_hash(key)
    builtin_hash = hash(key) % 10
    print(f"Key: {key}, Simple hash: {hash_val}, Built-in hash: {builtin_hash}")

# Custom hashable class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

# Point'leri sözlük anahtarı olarak kullanma
points_dict = {
    Point(0, 0): "origin",
    Point(1, 1): "diagonal",
    Point(1, 0): "right"
}

print(f"Points dict: {points_dict}")
print(f"Point(0,0): {points_dict[Point(0, 0)]}")

# Set'te Point kullanımı
points_set = {Point(0, 0), Point(1, 1), Point(0, 0)}  # Duplicate ignored
print(f"Points set: {points_set}")

print("\n5. WEAKREF VE WEAK COLLECTIONS:")
print("-" * 31)

import weakref
from weakref import WeakKeyDictionary, WeakValueDictionary, WeakSet

# WeakKeyDictionary
class Person:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"Person({self.name})"

# Normal dict - strong reference
normal_dict = {}
person1 = Person("Ali")
normal_dict[person1] = "Bilgiler"

print(f"Normal dict: {normal_dict}")

# WeakKeyDictionary - weak reference
weak_dict = WeakKeyDictionary()
person2 = Person("Veli")
weak_dict[person2] = "Bilgiler"

print(f"Weak dict: {dict(weak_dict)}")

# Obje silindiğinde weak dict'ten de silinir
del person2
import gc; gc.collect()  # Garbage collection zorla
print(f"After delete: {dict(weak_dict)}")

# WeakSet
weak_set = WeakSet()
person3 = Person("Ayşe")
weak_set.add(person3)
print(f"Weak set: {list(weak_set)}")

print("\n6. THREAD SAFETY VE CONCURRENT ACCESS:")
print("-" * 36)

import threading
from collections import deque

# Thread-safe operations
thread_safe_dict = {}
lock = threading.Lock()

def safe_increment(key):
    with lock:
        thread_safe_dict[key] = thread_safe_dict.get(key, 0) + 1

# Simulate concurrent access
threads = []
for i in range(10):
    thread = threading.Thread(target=safe_increment, args=("counter",))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Thread-safe counter: {thread_safe_dict}")

# concurrent.futures ile dict processing
from concurrent.futures import ThreadPoolExecutor

def process_dict_item(item):
    key, value = item
    return key, value ** 2

sample_dict = {f"key_{i}": i for i in range(100)}

with ThreadPoolExecutor(max_workers=4) as executor:
    results = dict(executor.map(process_dict_item, sample_dict.items()))

print(f"Concurrent processing sample: {dict(list(results.items())[:5])}")

print("\n7. SERIALIZATION VE PERSISTENCE:")
print("-" * 32)

import json
import pickle
from pathlib import Path

# JSON serialization (basic types only)
data_dict = {
    "name": "Python",
    "version": 3.9,
    "features": ["dynamic", "interpreted"],
    "stats": {"downloads": 1000000, "rating": 4.8}
}

# JSON'a çevirme
json_str = json.dumps(data_dict, indent=2)
print(f"JSON string: {json_str}")

# JSON'dan geri yükleme
loaded_dict = json.loads(json_str)
print(f"Loaded from JSON: {loaded_dict}")

# Pickle serialization (Python objects)
complex_dict = {
    "set": {1, 2, 3},
    "point": Point(5, 10),
    "lambda": lambda x: x * 2  # Pickle edilemez!
}

# Sadece pickle edilebilir kısmı
pickleable_dict = {
    "set": {1, 2, 3},
    "point": Point(5, 10)
}

# Pickle'a çevirme
pickle_data = pickle.dumps(pickleable_dict)
print(f"Pickle size: {len(pickle_data)} bytes")

# Pickle'dan geri yükleme
loaded_pickle = pickle.loads(pickle_data)
print(f"Loaded from pickle: {loaded_pickle}")

print("\n8. PATTERN MATCHING (Python 3.10+):")
print("-" * 34)

# Simüle pattern matching (Python 3.10 öncesi için)
def analyze_data_structure(data):
    """Veri yapısını analiz et"""
    if isinstance(data, dict):
        if not data:
            return "Empty dictionary"
        elif len(data) == 1:
            key, value = next(iter(data.items()))
            return f"Single item dict: {key} -> {value}"
        else:
            return f"Dictionary with {len(data)} items"
    
    elif isinstance(data, set):
        if not data:
            return "Empty set"
        elif len(data) == 1:
            return f"Single item set: {next(iter(data))}"
        else:
            return f"Set with {len(data)} items"
    
    else:
        return f"Other type: {type(data)}"

# Test cases
test_cases = [
    {},
    {"key": "value"},
    {"a": 1, "b": 2, "c": 3},
    set(),
    {42},
    {1, 2, 3, 4, 5},
    [1, 2, 3]
]

for case in test_cases:
    result = analyze_data_structure(case)
    print(f"{case} -> {result}")

print("\n9. FUNCTIONAL PROGRAMMING PATTERNS:")
print("-" * 35)

from functools import reduce
from operator import itemgetter

# Map-Reduce pattern with dicts
data = [
    {"name": "Ali", "score": 85, "subject": "Math"},
    {"name": "Veli", "score": 92, "subject": "Science"},
    {"name": "Ayşe", "score": 78, "subject": "Math"},
    {"name": "Mehmet", "score": 89, "subject": "Science"}
]

# Group by subject
subject_groups = {}
for item in data:
    subject = item["subject"]
    if subject not in subject_groups:
        subject_groups[subject] = []
    subject_groups[subject].append(item)

print(f"Grouped by subject: {subject_groups}")

# Calculate average score per subject
averages = {}
for subject, items in subject_groups.items():
    total_score = sum(item["score"] for item in items)
    averages[subject] = total_score / len(items)

print(f"Average scores: {averages}")

# Functional approach
from itertools import groupby

# Sort by subject first for groupby
sorted_data = sorted(data, key=itemgetter("subject"))

# Group and calculate averages functionally
functional_averages = {
    subject: sum(item["score"] for item in group) / len(list(group))
    for subject, group in groupby(sorted_data, key=itemgetter("subject"))
}

print(f"Functional averages: {functional_averages}")

# Filter pattern
high_scorers = {
    item["name"]: item["score"] 
    for item in data 
    if item["score"] >= 85
}
print(f"High scorers: {high_scorers}")

print("\n10. CACHING VE MEMOIZATION PATTERNS:")
print("-" * 35)

from functools import lru_cache

# Manual memoization with dict
def fibonacci_memo():
    cache = {}
    
    def fib(n):
        if n in cache:
            return cache[n]
        
        if n <= 1:
            result = n
        else:
            result = fib(n-1) + fib(n-2)
        
        cache[n] = result
        return result
    
    return fib

fib_func = fibonacci_memo()
print(f"Fibonacci(10): {fib_func(10)}")
print(f"Fibonacci(20): {fib_func(20)}")

# LRU Cache decorator
@lru_cache(maxsize=128)
def expensive_function(n):
    print(f"Computing for {n}")
    return n ** 2 + n * 3 + 1

# Test caching
for i in [1, 2, 1, 3, 2, 4]:
    result = expensive_function(i)
    print(f"Result for {i}: {result}")

print(f"Cache info: {expensive_function.cache_info()}")

# Custom cache with expiration
import time

class ExpiringCache:
    def __init__(self, ttl=60):
        self.ttl = ttl
        self.cache = {}
        self.timestamps = {}
    
    def get(self, key):
        if key in self.cache:
            if time.time() - self.timestamps[key] < self.ttl:
                return self.cache[key]
            else:
                del self.cache[key]
                del self.timestamps[key]
        return None
    
    def set(self, key, value):
        self.cache[key] = value
        self.timestamps[key] = time.time()

cache = ExpiringCache(ttl=2)
cache.set("key1", "value1")
print(f"Immediate: {cache.get('key1')}")

# Simulate time passage
time.sleep(1)
print(f"After 1s: {cache.get('key1')}")

print("\n11. DATA VALIDATION PATTERNS:")
print("-" * 28)

# Schema validation for dicts
def validate_user_data(data):
    """Kullanıcı verisi doğrulama"""
    schema = {
        "name": str,
        "age": int,
        "email": str,
        "active": bool
    }
    
    errors = []
    
    # Required fields check
    for field, expected_type in schema.items():
        if field not in data:
            errors.append(f"Missing field: {field}")
        elif not isinstance(data[field], expected_type):
            errors.append(f"Invalid type for {field}: expected {expected_type.__name__}")
    
    # Custom validations
    if "age" in data and data["age"] < 0:
        errors.append("Age cannot be negative")
    
    if "email" in data and "@" not in data["email"]:
        errors.append("Invalid email format")
    
    return errors

# Test validation
valid_data = {"name": "Ali", "age": 25, "email": "ali@test.com", "active": True}
invalid_data = {"name": "Veli", "age": -5, "email": "invalid", "active": "yes"}

print(f"Valid data errors: {validate_user_data(valid_data)}")
print(f"Invalid data errors: {validate_user_data(invalid_data)}")

# Set validation patterns
def validate_permissions(user_permissions, required_permissions):
    """İzin kontrolü"""
    user_set = set(user_permissions)
    required_set = set(required_permissions)
    
    if not required_set.issubset(user_set):
        missing = required_set - user_set
        return False, f"Missing permissions: {missing}"
    
    return True, "All permissions granted"

user_perms = ["read", "write"]
required_perms = ["read", "write", "delete"]

valid, message = validate_permissions(user_perms, required_perms)
print(f"Permission check: {valid}, {message}")

print("\n=== İLERİ SEVİYE KONULAR ÖZETİ ===")
print("Collections modülü:")
print("  • defaultdict - varsayılan değer")
print("  • Counter - sayma işlemleri")
print("  • OrderedDict - sıralı sözlük")
print("  • ChainMap - çoklu sözlük")
print()
print("Performance optimizasyonu:")
print("  • Bellek kullanımı")
print("  • Hash collision handling")
print("  • Thread safety")
print("  • Caching patterns")
print()
print("Advanced patterns:")
print("  • Weak references")
print("  • Serialization")
print("  • Functional programming")
print("  • Data validation")
print()
print("En iyi pratikler:")
print("  • Doğru veri yapısını seçin")
print("  • Memory-efficient kullanın")
print("  • Thread safety düşünün")
print("  • Validation ekleyin")
print("  • Cache when appropriate")