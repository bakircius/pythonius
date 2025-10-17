"""
Python Standard Library Modülleri

Bu dosya Python'ın zengin standard library'sini keşfeder.
En önemli ve kullanışlı built-in modülleri, kullanım örnekleri
ve best practices'leri kapsamlı olarak ele alır.
"""

import sys
import os
import math
import random
import datetime
import time
import json
import csv
import re
import collections
import itertools
import functools
import operator
import statistics
import pathlib
import urllib.parse
import urllib.request
import base64
import hashlib
import uuid
import secrets
import sqlite3
from decimal import Decimal
from fractions import Fraction
from enum import Enum, auto
import dataclasses
from typing import List, Dict, Optional, Union

# =============================================================================
# 1. CORE UTILITY MODULES
# =============================================================================

print("=== Core Utility Modules ===")

def core_utilities_ornekleri():
    """Core utility modüller"""
    
    # sys modülü
    print("📊 sys - Sistem bilgileri:")
    print(f"   • Python version: {sys.version}")
    print(f"   • Platform: {sys.platform}")
    print(f"   • Python path: {len(sys.path)} dizin")
    print(f"   • Loaded modules: {len(sys.modules)}")
    print(f"   • Recursion limit: {sys.getrecursionlimit()}")
    print(f"   • Byte order: {sys.byteorder}")
    
    # os modülü
    print(f"\n🖥️ os - İşletim sistemi interface:")
    print(f"   • Current directory: {os.getcwd()}")
    print(f"   • User: {os.getenv('USER', 'Unknown')}")
    print(f"   • Home: {os.path.expanduser('~')}")
    print(f"   • Path separator: '{os.sep}'")
    print(f"   • CPU count: {os.cpu_count()}")
    
    # Environment variables
    important_env_vars = ['PATH', 'HOME', 'USER', 'SHELL', 'PYTHONPATH']
    env_info = {var: os.getenv(var, 'Not set')[:50] + '...' if len(os.getenv(var, '')) > 50 else os.getenv(var, 'Not set') for var in important_env_vars}
    
    print(f"   📋 Environment variables (sample):")
    for var, value in env_info.items():
        if value != 'Not set':
            print(f"      {var}: {value}")
    
    # math modülü
    print(f"\n🧮 math - Matematik fonksiyonları:")
    print(f"   • π (pi): {math.pi}")
    print(f"   • e: {math.e}")
    print(f"   • √2: {math.sqrt(2)}")
    print(f"   • sin(π/2): {math.sin(math.pi/2)}")
    print(f"   • log(e): {math.log(math.e)}")
    print(f"   • 2^10: {math.pow(2, 10)}")
    print(f"   • ceil(4.2): {math.ceil(4.2)}")
    print(f"   • floor(4.8): {math.floor(4.8)}")
    
    # random modülü
    print(f"\n🎲 random - Rastgele sayı üretimi:")
    random.seed(42)  # Reproducible results
    print(f"   • Random float [0,1): {random.random():.4f}")
    print(f"   • Random int [1,10]: {random.randint(1, 10)}")
    print(f"   • Random choice: {random.choice(['A', 'B', 'C', 'D'])}")
    
    sample_list = list(range(1, 11))
    shuffled = sample_list.copy()
    random.shuffle(shuffled)
    print(f"   • Shuffled [1-10]: {shuffled}")
    print(f"   • Random sample (3): {random.sample(sample_list, 3)}")

core_utilities_ornekleri()

# =============================================================================
# 2. DATE VE TIME MODULES
# =============================================================================

print("\n=== Date ve Time Modules ===")

def datetime_ornekleri():
    """Datetime ve time modülleri"""
    
    # datetime modülü
    print("📅 datetime - Tarih ve saat işlemleri:")
    
    now = datetime.datetime.now()
    utc_now = datetime.datetime.utcnow()
    
    print(f"   • Şu an: {now}")
    print(f"   • UTC şu an: {utc_now}")
    print(f"   • Sadece tarih: {now.date()}")
    print(f"   • Sadece saat: {now.time()}")
    
    # Tarih aritmetiği
    tomorrow = now + datetime.timedelta(days=1)
    last_week = now - datetime.timedelta(weeks=1)
    
    print(f"   • Yarın: {tomorrow.date()}")
    print(f"   • Geçen hafta: {last_week.date()}")
    
    # Formatlanmış tarih
    formatted = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"   • Formatlanmış: {formatted}")
    
    # String'den tarih
    date_str = "2023-12-25 15:30:00"
    parsed_date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    print(f"   • Parse edilmiş: {parsed_date}")
    
    # time modülü
    print(f"\n⏰ time - Zaman işlemleri:")
    print(f"   • Timestamp: {time.time()}")
    print(f"   • Local time: {time.ctime()}")
    print(f"   • UTC time: {time.asctime(time.gmtime())}")
    
    # Performance measurement
    start = time.perf_counter()
    time.sleep(0.001)  # 1ms sleep
    end = time.perf_counter()
    print(f"   • Elapsed time: {(end - start)*1000:.2f}ms")

datetime_ornekleri()

# =============================================================================
# 3. DATA STRUCTURES VE COLLECTIONS
# =============================================================================

print("\n=== Collections ve Data Structures ===")

def collections_ornekleri():
    """Collections modülü örnekleri"""
    
    # Counter
    print("🔢 collections.Counter - Sayım yapısı:")
    from collections import Counter
    
    text = "hello world python programming"
    char_count = Counter(text)
    word_count = Counter(text.split())
    
    print(f"   • Karakter sayısı: {dict(char_count.most_common(5))}")
    print(f"   • Kelime sayısı: {dict(word_count)}")
    
    # defaultdict
    print(f"\n📚 collections.defaultdict - Varsayılan değerli dict:")
    from collections import defaultdict
    
    # Kelime grupları
    word_groups = defaultdict(list)
    words = ["apple", "banana", "apricot", "blueberry", "cherry"]
    
    for word in words:
        first_letter = word[0]
        word_groups[first_letter].append(word)
    
    print(f"   • Harfe göre gruplar: {dict(word_groups)}")
    
    # deque
    print(f"\n🔄 collections.deque - Çift uçlu kuyruk:")
    from collections import deque
    
    dq = deque([1, 2, 3])
    dq.appendleft(0)
    dq.append(4)
    dq.extend([5, 6])
    
    print(f"   • Deque: {list(dq)}")
    print(f"   • Pop left: {dq.popleft()}")
    print(f"   • Pop right: {dq.pop()}")
    print(f"   • Rotate(2): ", end="")
    dq.rotate(2)
    print(f"{list(dq)}")
    
    # namedtuple
    print(f"\n📋 collections.namedtuple - İsimli tuple:")
    from collections import namedtuple
    
    Person = namedtuple('Person', ['name', 'age', 'city'])
    person = Person('Alice', 30, 'Istanbul')
    
    print(f"   • Person: {person}")
    print(f"   • Name: {person.name}")
    print(f"   • Age: {person.age}")
    print(f"   • As dict: {person._asdict()}")

collections_ornekleri()

# =============================================================================
# 4. ITERTOOLS VE FUNCTIONAL PROGRAMMING
# =============================================================================

print("\n=== Itertools ve Functional Programming ===")

def itertools_ornekleri():
    """Itertools modülü örnekleri"""
    
    print("🔄 itertools - Iterator araçları:")
    
    # count, cycle, repeat
    print("   • Infinite iterators:")
    counter = itertools.count(10, 2)  # 10'dan başla, 2'şer artır
    print(f"     count(10,2) ilk 5: {[next(counter) for _ in range(5)]}")
    
    cycler = itertools.cycle(['A', 'B', 'C'])
    print(f"     cycle(['A','B','C']) ilk 7: {[next(cycler) for _ in range(7)]}")
    
    repeater = itertools.repeat('X', 4)
    print(f"     repeat('X', 4): {list(repeater)}")
    
    # Combinatorial generators
    print(f"\n   • Kombinatoryal generatorler:")
    data = ['A', 'B', 'C']
    
    print(f"     permutations: {list(itertools.permutations(data, 2))}")
    print(f"     combinations: {list(itertools.combinations(data, 2))}")
    print(f"     combinations_with_replacement: {list(itertools.combinations_with_replacement(data, 2))}")
    
    # product (kartezyen çarpım)
    colors = ['red', 'blue']
    sizes = ['S', 'M', 'L']
    products = list(itertools.product(colors, sizes))
    print(f"     product: {products}")
    
    # chain (iteratorları birleştir)
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list3 = [7, 8, 9]
    chained = list(itertools.chain(list1, list2, list3))
    print(f"     chain: {chained}")
    
    # groupby
    data = [1, 1, 2, 2, 2, 3, 1, 1]
    groups = [(k, list(g)) for k, g in itertools.groupby(data)]
    print(f"     groupby: {groups}")

def functools_ornekleri():
    """Functools modülü örnekleri"""
    
    print(f"\n⚙️ functools - Fonksiyonel araçlar:")
    
    # reduce
    numbers = [1, 2, 3, 4, 5]
    product = functools.reduce(operator.mul, numbers)
    print(f"   • reduce (çarpım): {product}")
    
    # partial
    def power(base, exponent):
        return base ** exponent
    
    square = functools.partial(power, exponent=2)
    cube = functools.partial(power, exponent=3)
    
    print(f"   • partial square(5): {square(5)}")
    print(f"   • partial cube(3): {cube(3)}")
    
    # lru_cache (memoization)
    @functools.lru_cache(maxsize=128)
    def fibonacci(n):
        if n < 2:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    
    # Cache performance test
    start = time.perf_counter()
    result = fibonacci(30)
    end = time.perf_counter()
    
    print(f"   • lru_cache fibonacci(30): {result}")
    print(f"   • Cache info: {fibonacci.cache_info()}")
    print(f"   • Time: {(end-start)*1000:.2f}ms")

itertools_ornekleri()
functools_ornekleri()

# =============================================================================
# 5. TEXT PROCESSING VE REGEX
# =============================================================================

print("\n=== Text Processing ve Regex ===")

def text_processing_ornekleri():
    """Text processing modülleri"""
    
    # re modülü
    print("🔍 re - Regular expressions:")
    
    text = "Python 3.11 released in 2022. Contact: info@python.org, support@example.com"
    
    # Email bulma
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    print(f"   • Emails: {emails}")
    
    # Sayı bulma
    numbers = re.findall(r'\d+\.?\d*', text)
    print(f"   • Numbers: {numbers}")
    
    # Kelime değiştirme
    replaced = re.sub(r'\bPython\b', 'Python🐍', text)
    print(f"   • Replaced: {replaced}")
    
    # Pattern matching
    pattern = r'(\w+)@(\w+\.\w+)'
    matches = re.finditer(pattern, text)
    
    print(f"   • Email parts:")
    for match in matches:
        username, domain = match.groups()
        print(f"     {username} at {domain}")
    
    # string modülü
    print(f"\n📝 string - String utilities:")
    import string
    
    print(f"   • ASCII letters: {string.ascii_letters[:20]}...")
    print(f"   • Digits: {string.digits}")
    print(f"   • Punctuation: {string.punctuation[:20]}...")
    
    # Template
    template = string.Template("Hello $name, your score is $score")
    formatted = template.substitute(name="Alice", score=95)
    print(f"   • Template: {formatted}")

text_processing_ornekleri()

# =============================================================================
# 6. DATA SERIALIZATION
# =============================================================================

print("\n=== Data Serialization ===")

def serialization_ornekleri():
    """Veri serialization modülleri"""
    
    # json modülü
    print("📦 json - JSON serialization:")
    
    data = {
        "name": "Python Tutorial",
        "version": 3.11,
        "features": ["OOP", "Functional", "Dynamic"],
        "metadata": {
            "author": "Developer",
            "year": 2023
        }
    }
    
    # JSON string'e dönüştür
    json_str = json.dumps(data, indent=2, ensure_ascii=False)
    print(f"   • JSON string (ilk 100 char): {json_str[:100]}...")
    
    # JSON'dan geri parse et
    parsed_data = json.loads(json_str)
    print(f"   • Parsed back: {parsed_data['name']}")
    
    # csv modülü
    print(f"\n📊 csv - CSV processing:")
    import io
    
    # CSV data
    csv_data = io.StringIO()
    writer = csv.writer(csv_data)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Alice', 30, 'Istanbul'])
    writer.writerow(['Bob', 25, 'Ankara'])
    writer.writerow(['Charlie', 35, 'Izmir'])
    
    csv_content = csv_data.getvalue()
    print(f"   • CSV content:")
    for line in csv_content.strip().split('\n'):
        print(f"     {line}")
    
    # CSV okuma
    csv_data.seek(0)
    reader = csv.DictReader(csv_data)
    print(f"   • CSV as dicts:")
    for row in reader:
        print(f"     {row}")

serialization_ornekleri()

# =============================================================================
# 7. CRYPTOGRAPHY VE SECURITY
# =============================================================================

print("\n=== Cryptography ve Security ===")

def crypto_security_ornekleri():
    """Cryptography ve güvenlik modülleri"""
    
    # hashlib
    print("🔐 hashlib - Hash algorithms:")
    
    text = "Python programming"
    
    # Different hash algorithms
    md5_hash = hashlib.md5(text.encode()).hexdigest()
    sha1_hash = hashlib.sha1(text.encode()).hexdigest()
    sha256_hash = hashlib.sha256(text.encode()).hexdigest()
    
    print(f"   • MD5: {md5_hash}")
    print(f"   • SHA1: {sha1_hash}")
    print(f"   • SHA256: {sha256_hash[:32]}...")
    
    # secrets modülü
    print(f"\n🎲 secrets - Cryptographically strong random:")
    
    # Güvenli random değerler
    random_bytes = secrets.token_bytes(16)
    random_hex = secrets.token_hex(16)
    random_url = secrets.token_urlsafe(16)
    
    print(f"   • Random bytes (16): {random_bytes}")
    print(f"   • Random hex (16): {random_hex}")
    print(f"   • URL-safe token: {random_url}")
    
    # Secure password generation
    import string
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(secrets.choice(alphabet) for _ in range(12))
    print(f"   • Secure password: {password}")
    
    # uuid modülü
    print(f"\n🆔 uuid - UUID generation:")
    
    # Different UUID versions
    uuid1 = uuid.uuid1()  # MAC address + timestamp
    uuid4 = uuid.uuid4()  # Random
    
    print(f"   • UUID1: {uuid1}")
    print(f"   • UUID4: {uuid4}")
    print(f"   • UUID4 hex: {uuid4.hex}")
    
    # base64 modülü
    print(f"\n📝 base64 - Base64 encoding:")
    
    original = "Python programming tutorial"
    encoded = base64.b64encode(original.encode()).decode()
    decoded = base64.b64decode(encoded).decode()
    
    print(f"   • Original: {original}")
    print(f"   • Encoded: {encoded}")
    print(f"   • Decoded: {decoded}")

crypto_security_ornekleri()

# =============================================================================
# 8. URL VE NETWORK UTILITIES
# =============================================================================

print("\n=== URL ve Network Utilities ===")

def network_utilities_ornekleri():
    """Network ve URL işleme modülleri"""
    
    # urllib.parse
    print("🌐 urllib.parse - URL parsing:")
    
    url = "https://api.example.com:8080/users/123?format=json&limit=10#section1"
    parsed = urllib.parse.urlparse(url)
    
    print(f"   • Original URL: {url}")
    print(f"   • Scheme: {parsed.scheme}")
    print(f"   • Netloc: {parsed.netloc}")
    print(f"   • Path: {parsed.path}")
    print(f"   • Query: {parsed.query}")
    print(f"   • Fragment: {parsed.fragment}")
    
    # Query string parsing
    query_params = urllib.parse.parse_qs(parsed.query)
    print(f"   • Query params: {query_params}")
    
    # URL building
    params = {'user': 'alice', 'action': 'login', 'redirect': '/dashboard'}
    query_string = urllib.parse.urlencode(params)
    new_url = f"https://example.com/auth?{query_string}"
    print(f"   • Built URL: {new_url}")
    
    # URL encoding/decoding
    text_with_spaces = "Python programming tutorial"
    encoded_text = urllib.parse.quote(text_with_spaces)
    decoded_text = urllib.parse.unquote(encoded_text)
    
    print(f"   • URL encoded: {encoded_text}")
    print(f"   • URL decoded: {decoded_text}")

network_utilities_ornekleri()

# =============================================================================
# 9. MATHEMATICAL VE STATISTICAL MODULES
# =============================================================================

print("\n=== Mathematical ve Statistical Modules ===")

def math_stats_ornekleri():
    """Matematik ve istatistik modülleri"""
    
    # statistics modülü
    print("📊 statistics - İstatistik işlemleri:")
    
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print(f"   • Data: {data}")
    print(f"   • Mean (ortalama): {statistics.mean(data)}")
    print(f"   • Median (medyan): {statistics.median(data)}")
    print(f"   • Mode (mod): {statistics.mode([1,1,2,2,2,3])}")
    print(f"   • Std deviation: {statistics.stdev(data):.3f}")
    print(f"   • Variance: {statistics.variance(data):.3f}")
    
    # Harmonik ve geometrik ortalama
    positive_data = [1, 2, 4, 8]
    print(f"   • Harmonic mean: {statistics.harmonic_mean(positive_data):.3f}")
    print(f"   • Geometric mean: {statistics.geometric_mean(positive_data):.3f}")
    
    # decimal modülü
    print(f"\n💰 decimal - Hassas ondalık aritmetik:")
    
    # Float precision issues
    float_calc = 0.1 + 0.2
    decimal_calc = Decimal('0.1') + Decimal('0.2')
    
    print(f"   • Float: 0.1 + 0.2 = {float_calc}")
    print(f"   • Decimal: 0.1 + 0.2 = {decimal_calc}")
    
    # Financial calculations
    price = Decimal('99.99')
    tax_rate = Decimal('0.08')
    tax = price * tax_rate
    total = price + tax
    
    print(f"   • Price: ${price}")
    print(f"   • Tax (8%): ${tax:.2f}")
    print(f"   • Total: ${total:.2f}")
    
    # fractions modülü
    print(f"\n🔢 fractions - Kesirli sayılar:")
    
    frac1 = Fraction(1, 3)
    frac2 = Fraction(2, 6)  # 1/3 ile aynı
    frac3 = Fraction(1, 4)
    
    print(f"   • 1/3: {frac1}")
    print(f"   • 2/6: {frac2} (simplified)")
    print(f"   • 1/3 + 1/4: {frac1 + frac3}")
    print(f"   • 1/3 * 4: {frac1 * 4}")
    
    # String'den fraction
    frac_from_decimal = Fraction('0.25')
    print(f"   • From decimal: {frac_from_decimal}")

math_stats_ornekleri()

# =============================================================================
# 10. MODERN PYTHON FEATURES
# =============================================================================

print("\n=== Modern Python Features ===")

def modern_features_ornekleri():
    """Modern Python özelliklerini gösteren modüller"""
    
    # enum modülü
    print("🏷️ enum - Enumerations:")
    
    class Status(Enum):
        PENDING = auto()
        PROCESSING = auto()
        COMPLETED = auto()
        FAILED = auto()
    
    class Color(Enum):
        RED = "#FF0000"
        GREEN = "#00FF00"
        BLUE = "#0000FF"
    
    print(f"   • Status enum: {list(Status)}")
    print(f"   • Status.PENDING: {Status.PENDING}")
    print(f"   • Color.RED: {Color.RED.value}")
    
    # dataclasses modülü
    print(f"\n📋 dataclasses - Data sınıfları:")
    
    @dataclasses.dataclass
    class Person:
        name: str
        age: int
        city: str = "Unknown"
        active: bool = True
        
        def __post_init__(self):
            if self.age < 0:
                raise ValueError("Age cannot be negative")
    
    person1 = Person("Alice", 30, "Istanbul")
    person2 = Person("Bob", 25)
    
    print(f"   • Person1: {person1}")
    print(f"   • Person2: {person2}")
    print(f"   • Fields: {[f.name for f in dataclasses.fields(Person)]}")
    
    # As dict
    person_dict = dataclasses.asdict(person1)
    print(f"   • As dict: {person_dict}")
    
    # pathlib modülü
    print(f"\n📁 pathlib - Object-oriented paths:")
    
    # Path operations
    current_path = pathlib.Path.cwd()
    home_path = pathlib.Path.home()
    
    print(f"   • Current: {current_path}")
    print(f"   • Home: {home_path}")
    
    # Path building
    config_file = current_path / "config" / "settings.json"
    print(f"   • Config file: {config_file}")
    print(f"   • Parent: {config_file.parent}")
    print(f"   • Name: {config_file.name}")
    print(f"   • Suffix: {config_file.suffix}")
    print(f"   • Stem: {config_file.stem}")
    
    # Path properties
    print(f"   • Exists: {current_path.exists()}")
    print(f"   • Is dir: {current_path.is_dir()}")
    print(f"   • Is file: {current_path.is_file()}")

modern_features_ornekleri()

# =============================================================================
# 11. PERFORMANCE VE DEBUGGING MODULES
# =============================================================================

print("\n=== Performance ve Debugging ===")

def performance_debugging_ornekleri():
    """Performance ve debugging modülleri"""
    
    # timeit for micro-benchmarks
    print("⏱️ timeit - Performance measurement:")
    import timeit
    
    # List comprehension vs loop
    list_comp_time = timeit.timeit(
        '[x**2 for x in range(100)]',
        number=10000
    )
    
    loop_time = timeit.timeit(
        '''
result = []
for x in range(100):
    result.append(x**2)
''',
        number=10000
    )
    
    print(f"   • List comprehension: {list_comp_time:.6f}s")
    print(f"   • Traditional loop: {loop_time:.6f}s")
    print(f"   • Speedup: {loop_time/list_comp_time:.2f}x")
    
    # profile module
    print(f"\n🔍 cProfile - Code profiling:")
    import cProfile
    import io
    import pstats
    
    def example_function():
        """Örnek fonksiyon profiling için"""
        result = []
        for i in range(1000):
            result.append(i ** 2)
        return sum(result)
    
    # Profile
    profiler = cProfile.Profile()
    profiler.enable()
    
    example_function()
    
    profiler.disable()
    
    # Results
    stats_stream = io.StringIO()
    stats = pstats.Stats(profiler, stream=stats_stream)
    stats.sort_stats('cumulative')
    stats.print_stats(5)  # Top 5
    
    profile_output = stats_stream.getvalue()
    print(f"   • Profile output (sample):")
    lines = profile_output.split('\n')[:10]
    for line in lines:
        if line.strip():
            print(f"     {line}")

performance_debugging_ornekleri()

print("\n🏆 Standard Library Best Practices:")
print("✅ Built-in modülleri third-party'den önce tercih edin")
print("✅ Performans kritik kodlarda C extensions kullanın")
print("✅ Appropriate data structures seçin (collections)")
print("✅ Lazy evaluation için generators kullanın")
print("✅ Memory efficient işlemler için itertools kullanın")
print("✅ Type hints ile code quality artırın")
print("✅ Dataclasses ile boilerplate code azaltın")

print("\n📚 Önemli Standard Library Modülleri:")
print("• 🔧 Utilities: sys, os, pathlib, argparse")
print("• 📊 Data: collections, itertools, functools")
print("• 🕒 Time: datetime, time, calendar")
print("• 📝 Text: re, string, textwrap")
print("• 📦 Serialization: json, pickle, csv")
print("• 🌐 Network: urllib, http, email")
print("• 🔐 Security: hashlib, secrets, ssl")
print("• 🧮 Math: math, statistics, decimal, fractions")
print("• 🧪 Testing: unittest, doctest")
print("• ⚡ Performance: timeit, cProfile, trace")

print("\n✅ Python Standard Library mastery kazanıldı!")
print("✅ Core modules ve kullanım patterns öğrenildi!")
print("✅ Performance ve debugging tools öğrenildi!")
print("✅ Modern Python features öğrenildi!")