"""
Python Modüller ve Paketler

Bu dosya Python'da modül sistemi, import mekanizması, paket oluşturma,
namespace'ler ve modül organizasyonu konularını kapsamlı olarak ele alır.
"""

import sys
import os
import importlib
import inspect
from pathlib import Path
import json
import pickle
from types import ModuleType
import pkgutil

# =============================================================================
# 1. MODÜL KAVRAMII VE TEMEL KULLANIM
# =============================================================================

print("=== Modül Kavramı ve Temel Kullanım ===")

def modul_temellerine_giris():
    """Modül sistemine giriş"""
    
    print("📚 Modül Nedir?")
    print("• Modül: Python kodunu organize etmek için kullanılan dosyadır (.py)")
    print("• Her .py dosyası bir modüldür")
    print("• Modüller fonksiyon, sınıf ve değişkenleri organize eder")
    print("• import keyword'ü ile kullanılır")
    
    print(f"\n📂 Bu modülün bilgileri:")
    print(f"• Modül adı: {__name__}")
    print(f"• Dosya yolu: {__file__}")
    if hasattr(__builtins__, '__doc__'):
        print(f"• Docstring: {__doc__[:100]}...")
    
    # Mevcut modüldeki isimler
    print(f"\n🔍 Bu modüldeki isimler:")
    local_names = [name for name in dir() if not name.startswith('_')]
    print(f"• Toplam {len(local_names)} genel isim")
    print(f"• İlk 10 isim: {local_names[:10]}")

modul_temellerine_giris()

# =============================================================================
# 2. İMPORT MEKANİZMASI
# =============================================================================

print("\n=== Import Mekanizması ===")

def import_ornekleri():
    """Farklı import yöntemleri"""
    
    print("--- Standard Library Import ---")
    
    # Temel import
    import math
    print(f"math modülü: {math}")
    print(f"math.pi: {math.pi}")
    print(f"math.sqrt(16): {math.sqrt(16)}")
    
    # from import
    from math import sqrt, pi, sin
    print(f"Direkt sqrt(25): {sqrt(25)}")
    print(f"Direkt pi: {pi}")
    
    # Alias import
    import datetime as dt
    now = dt.datetime.now()
    print(f"Şimdiki zaman (datetime as dt): {now}")
    
    # from import with alias
    from collections import defaultdict as dd
    sayac = dd(int)
    sayac['a'] += 1
    print(f"defaultdict as dd: {dict(sayac)}")
    
    # Wildcard import (dikkatli kullanın!)
    print("\n--- Wildcard Import (dikkatli!) ---")
    # from math import *  # Tüm isimleri import eder
    print("from math import * -> Tüm math fonksiyonları namespace'e gelir")
    print("⚠️  Wildcard import namespace kirliliği yaratabilir")
    
    # Multiple import
    print("\n--- Multiple Import ---")
    from os import path, getcwd, listdir
    print(f"Çalışma dizini: {getcwd()}")
    
    # Conditional import
    print("\n--- Conditional Import ---")
    try:
        import numpy as np
        print("✅ NumPy bulundu")
        print(f"NumPy versiyonu: {np.__version__}")
    except ImportError:
        print("❌ NumPy bulunamadı")
        np = None
    
    # Late import (fonksiyon içinde)
    def gerektiginde_import():
        import random  # Sadece bu fonksiyon çağrıldığında import edilir
        return random.randint(1, 100)
    
    print(f"Late import sonucu: {gerektiginde_import()}")

import_ornekleri()

# =============================================================================
# 3. MODÜL ARAMA YOLU (MODULE SEARCH PATH)
# =============================================================================

print("\n=== Modül Arama Yolu ===")

def modul_arama_yolu():
    """Python'ın modül arama mekanizması"""
    
    print("🔍 Python Modül Arama Sırası:")
    print("1. Yerleşik modüller (built-in)")
    print("2. Çalışma dizini")
    print("3. PYTHONPATH environment variable")
    print("4. Standard library")
    print("5. Site-packages (third-party)")
    
    print(f"\n📂 sys.path içeriği:")
    for i, path in enumerate(sys.path, 1):
        print(f"  {i}. {path}")
    
    # Modül lokasyonu bulma
    import json
    print(f"\n📍 json modülünün lokasyonu: {json.__file__}")
    
    import os
    print(f"📍 os modülünün lokasyonu: {os.__file__}")
    
    # Yerleşik modüller
    print(f"\n🏗️  Yerleşik modüller sayısı: {len(sys.builtin_module_names)}")
    print(f"İlk 10 yerleşik modül: {list(sys.builtin_module_names)[:10]}")
    
    # Yeni path ekleme
    print("\n➕ sys.path'e yeni dizin ekleme:")
    new_path = "/tmp/my_modules"
    if new_path not in sys.path:
        sys.path.append(new_path)
        print(f"✅ Eklendi: {new_path}")
    else:
        print(f"⚠️  Zaten var: {new_path}")

modul_arama_yolu()

# =============================================================================
# 4. MODÜL ÖZELLİKLERİ VE ATTRİBUTLARI
# =============================================================================

print("\n=== Modül Özellikleri ===")

def modul_ozellikleri():
    """Modül özellikleri ve meta bilgileri"""
    
    import math
    
    print("--- Modül Attributları ---")
    print(f"math.__name__: {math.__name__}")
    print(f"math.__file__: {getattr(math, '__file__', 'C extension')}")
    print(f"math.__doc__: {math.__doc__[:100]}...")
    
    # Modül içeriğini listele
    print(f"\n--- math Modülü İçeriği ---")
    math_items = dir(math)
    functions = [item for item in math_items if callable(getattr(math, item)) and not item.startswith('_')]
    constants = [item for item in math_items if not callable(getattr(math, item)) and not item.startswith('_')]
    
    print(f"📊 Toplam öğe: {len(math_items)}")
    print(f"🔧 Fonksiyon sayısı: {len(functions)}")
    print(f"📌 Sabit sayısı: {len(constants)}")
    print(f"🔧 Bazı fonksiyonlar: {functions[:5]}")
    print(f"📌 Sabitler: {constants}")
    
    # Modül tipi kontrolü
    print(f"\n--- Modül Tipi ---")
    print(f"math modül türü: {type(math)}")
    print(f"ModuleType instance: {isinstance(math, ModuleType)}")
    
    # Inspect modülü ile detay
    print(f"\n--- Inspect ile Analiz ---")
    if inspect.ismodule(math):
        print("✅ math bir modüldür")
        
        # Modül üyelerini kategorize et
        members = inspect.getmembers(math)
        functions = inspect.getmembers(math, inspect.isfunction)
        builtins = inspect.getmembers(math, inspect.isbuiltin)
        
        print(f"📊 Toplam üye: {len(members)}")
        print(f"🔧 Python fonksiyon: {len(functions)}")
        print(f"⚙️  Built-in fonksiyon: {len(builtins)}")

modul_ozellikleri()

# =============================================================================
# 5. DİNAMİK İMPORT
# =============================================================================

print("\n=== Dinamik Import ===")

def dinamik_import_ornekleri():
    """Runtime'da dinamik modül import etme"""
    
    print("--- importlib.import_module ---")
    
    # String ile modül import
    module_name = "json"
    json_module = importlib.import_module(module_name)
    print(f"Dinamik import: {module_name} -> {json_module}")
    
    # JSON test
    test_data = {"test": "başarılı"}
    json_string = json_module.dumps(test_data)
    print(f"JSON test: {json_string}")
    
    # Paket alt modülü import
    try:
        urllib_parse = importlib.import_module("urllib.parse")
        print(f"Alt modül import: urllib.parse -> {urllib_parse}")
    except ImportError as e:
        print(f"Import hatası: {e}")
    
    # Koşullu dinamik import
    print("\n--- Koşullu Dinamik Import ---")
    
    def get_json_module():
        """En uygun JSON modülünü döndür"""
        try:
            # Önce orjson'ı dene (hızlı)
            return importlib.import_module("orjson")
        except ImportError:
            try:
                # Sonra ujson'ı dene (hızlı)
                return importlib.import_module("ujson")
            except ImportError:
                # Son çare standart json
                return importlib.import_module("json")
    
    json_mod = get_json_module()
    print(f"Seçilen JSON modülü: {json_mod.__name__}")
    
    # Plugin sistemi simülasyonu
    print("\n--- Plugin Sistemi Simülasyonu ---")
    
    def load_plugin(plugin_name):
        """Plugin yükleme simülasyonu"""
        try:
            plugin = importlib.import_module(plugin_name)
            print(f"✅ Plugin yüklendi: {plugin_name}")
            return plugin
        except ImportError:
            print(f"❌ Plugin bulunamadı: {plugin_name}")
            return None
    
    # Test plugin'leri
    plugins = ["math", "random", "nonexistent_plugin"]
    loaded_plugins = {}
    
    for plugin_name in plugins:
        plugin = load_plugin(plugin_name)
        if plugin:
            loaded_plugins[plugin_name] = plugin
    
    print(f"Yüklenen plugin sayısı: {len(loaded_plugins)}")

dinamik_import_ornekleri()

# =============================================================================
# 6. MODÜL CACHE VE RELOAD
# =============================================================================

print("\n=== Modül Cache ve Reload ===")

def modul_cache_ornekleri():
    """Modül cache sistemi ve reload işlemleri"""
    
    print("--- sys.modules Cache ---")
    
    # Cache'teki modül sayısı
    print(f"Cache'teki modül sayısı: {len(sys.modules)}")
    
    # Bazı modülleri listele
    loaded_modules = list(sys.modules.keys())[:10]
    print(f"İlk 10 yüklü modül: {loaded_modules}")
    
    # Belirli modülün cache durumu
    if "json" in sys.modules:
        print("✅ json modülü cache'te")
        print(f"json modül objesi: {sys.modules['json']}")
    
    # Modül silme (dikkatli!)
    print("\n--- Modül Cache Manipülasyonu ---")
    
    # Test modülü import et
    import uuid
    print(f"uuid modülü yüklendi: {uuid in sys.modules.values()}")
    
    # Cache'ten kaldır (dikkatli!)
    if "uuid" in sys.modules:
        uuid_module = sys.modules["uuid"]
        print(f"UUID modül id öncesi: {id(uuid_module)}")
        
        # Yeniden import (cache'ten gelir)
        import uuid as uuid2
        print(f"UUID modül id sonrası: {id(uuid2)}")
        print(f"Aynı obje: {uuid_module is uuid2}")
    
    # importlib.reload
    print("\n--- importlib.reload ---")
    
    # Not: reload sadece development için kullanılmalı
    print("⚠️  importlib.reload() production'da kullanılmamalı")
    print("• Sadece development/debugging için")
    print("• Memory leak'e sebep olabilir")
    print("• Side effect'leri olabilir")
    
    try:
        import math
        math_before = id(math)
        
        # Reload (dikkatli!)
        math_reloaded = importlib.reload(math)
        math_after = id(math_reloaded)
        
        print(f"Math id öncesi: {math_before}")
        print(f"Math id sonrası: {math_after}")
        print(f"Farklı obje: {math_before != math_after}")
        
    except Exception as e:
        print(f"Reload hatası: {e}")

modul_cache_ornekleri()

# =============================================================================
# 7. __INIT__.PY VE PAKET YAPISI
# =============================================================================

print("\n=== __init__.py ve Paket Yapısı ===")

def paket_yapisi_ornekleri():
    """Python paket sistemi"""
    
    print("📦 Python Paket Sistemi:")
    print("• Paket: Modülleri organize eden dizin")
    print("• __init__.py: Paketi tanımlayan dosya")
    print("• Alt paketler: İç içe paket yapısı")
    print("• Namespace paketler: __init__.py olmadan")
    
    # Örnek paket yapısı
    print(f"\n🏗️  Örnek Paket Yapısı:")
    example_structure = """
    mypackage/
        __init__.py          # Paket tanımı
        core/
            __init__.py      # Alt paket
            utils.py         # Modül
            helpers.py       # Modül
        web/
            __init__.py      # Alt paket
            server.py        # Modül
            client.py        # Modül
        tests/
            __init__.py
            test_core.py
    """
    print(example_structure)
    
    # Standard library paket örneği
    print("--- Standard Library Paket Örnekleri ---")
    
    # urllib paketi
    import urllib
    print(f"urllib paketi: {urllib}")
    print(f"urllib.__file__: {getattr(urllib, '__file__', 'Namespace package')}")
    print(f"urllib.__path__: {getattr(urllib, '__path__', 'No path')}")
    
    # urllib alt modülleri
    try:
        import urllib.parse
        import urllib.request
        print("✅ urllib.parse ve urllib.request yüklendi")
    except ImportError as e:
        print(f"❌ urllib alt modül hatası: {e}")
    
    # collections paketi
    import collections
    print(f"\ncollections paketi: {collections}")
    
    # collections'dan spesifik import
    from collections import defaultdict, Counter, deque
    print("✅ collections'dan spesifik sınıflar import edildi")
    
    # __all__ kullanımı
    print(f"\n--- __all__ Attributı ---")
    if hasattr(collections, '__all__'):
        print(f"collections.__all__: {collections.__all__[:5]}...")
    else:
        print("collections.__all__ tanımlı değil")

paket_yapisi_ornekleri()

# =============================================================================
# 8. NAMESPACE PACKAGES
# =============================================================================

print("\n=== Namespace Packages ===")

def namespace_packages():
    """PEP 420 Namespace Packages"""
    
    print("🌐 Namespace Packages (PEP 420):")
    print("• __init__.py dosyası olmayan paketler")
    print("• Birden fazla lokasyonda olabilir")
    print("• Implicit namespace packages")
    print("• Distribution'lar arası paylaşım")
    
    # pkgutil ile namespace exploration
    print(f"\n--- Namespace Package Detection ---")
    
    def explore_package(package_name):
        """Paket yapısını keşfet"""
        try:
            package = importlib.import_module(package_name)
            print(f"\n📦 {package_name}:")
            print(f"  Type: {type(package)}")
            print(f"  File: {getattr(package, '__file__', 'No file (namespace?)')}")
            print(f"  Path: {getattr(package, '__path__', 'No path')}")
            
            # Alt modülleri listele
            if hasattr(package, '__path__'):
                try:
                    submodules = []
                    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
                        submodules.append(f"{'📦' if ispkg else '📄'} {modname}")
                    
                    if submodules:
                        print(f"  Sub-modules: {submodules[:5]}")
                        if len(submodules) > 5:
                            print(f"    ... ve {len(submodules) - 5} daha")
                    else:
                        print("  Sub-modules: Yok")
                        
                except Exception as e:
                    print(f"  Alt modül listesi alınamadı: {e}")
                    
        except ImportError:
            print(f"❌ {package_name} import edilemedi")
    
    # Bazı paketleri keşfet
    packages_to_explore = ["urllib", "collections", "email", "json"]
    
    for pkg in packages_to_explore:
        explore_package(pkg)

namespace_packages()

# =============================================================================
# 9. MODÜL VE PAKET OLUŞTURMA
# =============================================================================

print("\n=== Modül ve Paket Oluşturma ===")

def modul_paket_olusturma():
    """Kendi modül ve paketlerimizi oluşturma"""
    
    print("🛠️  Kendi Modülümüzü Oluşturalım:")
    
    # Basit modül içeriği
    simple_module_content = '''"""
Basit matematik işlemleri modülü

Bu modül temel matematik işlemlerini içerir.
"""

__version__ = "1.0.0"
__author__ = "Python Öğrencisi"

def toplama(a, b):
    """İki sayıyı topla"""
    return a + b

def carpma(a, b):
    """İki sayıyı çarp"""
    return a * b

def kare(x):
    """Sayının karesini al"""
    return x ** 2

# Modül yüklendiğinde çalışacak kod
print(f"Matematik modülü yüklendi (versiyon {__version__})")

# __all__ ile public API tanımla
__all__ = ['toplama', 'carpma', 'kare']
'''
    
    # Modülü dosyaya yaz
    module_path = Path("matematik.py")
    try:
        with open(module_path, "w", encoding="utf-8") as f:
            f.write(simple_module_content)
        print(f"✅ Modül oluşturuldu: {module_path}")
        
        # Oluşturduğumuz modülü import et
        if str(Path.cwd()) not in sys.path:
            sys.path.insert(0, str(Path.cwd()))
        
        # Import öncesi cache temizle
        if "matematik" in sys.modules:
            del sys.modules["matematik"]
        
        import matematik
        print(f"📦 Modül import edildi: {matematik}")
        print(f"🔢 Toplama testi: 3 + 5 = {matematik.toplama(3, 5)}")
        print(f"🔢 Kare testi: 4² = {matematik.kare(4)}")
        print(f"📋 __all__: {matematik.__all__}")
        
    except Exception as e:
        print(f"❌ Modül oluşturma hatası: {e}")
    
    # Paket yapısı oluşturma örneği
    print(f"\n🏗️  Paket Yapısı Örneği:")
    
    package_structure = {
        "mypackage": {
            "__init__.py": '''"""
MyPackage - Örnek Python Paketi

Bu paket çeşitli utility'leri içerir.
"""

__version__ = "1.0.0"

# Alt modüllerden import
from .core import hello
from .utils import format_text

# Public API
__all__ = ['hello', 'format_text']
''',
            "core.py": '''"""
Core functionality
"""

def hello(name="Dünya"):
    """Selamlama fonksiyonu"""
    return f"Merhaba, {name}!"

def goodbye(name="Dünya"):
    """Veda fonksiyonu"""
    return f"Hoşçakal, {name}!"
''',
            "utils.py": '''"""
Utility functions
"""

def format_text(text, upper=False):
    """Metni formatla"""
    if upper:
        return text.upper()
    return text.lower()

def reverse_text(text):
    """Metni ters çevir"""
    return text[::-1]
'''
        }
    }
    
    print("Paket yapısı:")
    for folder, files in package_structure.items():
        print(f"📁 {folder}/")
        for filename, content in files.items():
            print(f"  📄 {filename}")

modul_paket_olusturma()

# =============================================================================
# 10. MODÜL DOKÜMANTASYONU VE METADAta
# =============================================================================

print("\n=== Modül Dokümantasyonu ===")

def modul_dokumantasyonu():
    """Modül dokümantasyonu ve metadata best practices"""
    
    print("📚 Modül Dokümantasyonu Best Practices:")
    
    # Örnek modül header
    example_header = '''"""
modül_adı - Kısa açıklama

Modülün detaylı açıklaması burada yer alır.
Kullanım örnekleri ve API açıklamaları dahildir.

Author: İsim Soyisim <email@example.com>
License: MIT
Version: 1.0.0
Python: >=3.8

Example:
    Basic usage:
    
    >>> from modul_adi import function_name
    >>> result = function_name(argument)
    >>> print(result)
    'Expected output'

Note:
    Bu modül Python 3.8+ gerektirir.
    Ek bağımlılıklar: requests, numpy

Todo:
    * İyileştirme planları
    * Yeni özellik fikirleri
"""

__version__ = "1.0.0"
__author__ = "İsim Soyisim"
__email__ = "email@example.com"
__license__ = "MIT"
__copyright__ = "Copyright 2024, İsim Soyisim"
__status__ = "Development"  # "Prototype", "Development", "Production"
__maintainer__ = "İsim Soyisim"
__credits__ = ["Contributor1", "Contributor2"]

# Compatibility
__python_requires__ = ">=3.8"
__dependencies__ = ["requests>=2.25.0", "numpy>=1.19.0"]
'''
    
    print("--- Metadata Örnegi ---")
    print(example_header[:500] + "...")
    
    # Gerçek modül metadata örneği
    print(f"\n--- json Modülü Metadata ---")
    import json
    
    metadata_attrs = [
        '__name__', '__doc__', '__file__', '__package__',
        '__version__', '__author__'
    ]
    
    for attr in metadata_attrs:
        value = getattr(json, attr, 'Tanımlı değil')
        if attr == '__doc__' and value:
            value = value[:100] + "..." if len(value) > 100 else value
        print(f"{attr}: {value}")
    
    # Help sistemi
    print(f"\n--- Help Sistemi ---")
    print("Python'da help() fonksiyonu modül dokümantasyonunu gösterir:")
    print("help(json)  # JSON modülü yardımı")
    print("help(json.dumps)  # Spesifik fonksiyon yardımı")
    
    # Docstring konventions
    print(f"\n--- Docstring Konventions ---")
    print("📝 PEP 257 - Docstring Conventions:")
    print("• İlk satır kısa özet")
    print("• Boş satır")
    print("• Detaylı açıklama")
    print("• Args, Returns, Raises bölümleri")
    print("• Examples kullanımı")

modul_dokumantasyonu()

# =============================================================================
# 11. MODÜL BEST PRACTICES
# =============================================================================

print("\n=== Modül Best Practices ===")

def modul_best_practices():
    """Modül geliştirme best practices"""
    
    print("🏆 Modül Geliştirme Best Practices:")
    
    print(f"\n1. 📂 Dosya ve Dizin Organizasyonu:")
    print("   ✅ Anlamlı modül isimleri (snake_case)")
    print("   ✅ Tek sorumluluk prensibi")
    print("   ✅ Shallow hierarchy (fazla iç içe paket yok)")
    print("   ✅ __init__.py'da public API tanımla")
    
    print(f"\n2. 📝 Import Best Practices:")
    print("   ✅ Standard library → Third-party → Local imports")
    print("   ✅ Absolute imports tercih et")
    print("   ✅ Wildcard imports'tan kaçın")
    print("   ✅ Import'ları alfabetik sırala")
    
    print(f"\n3. 🎯 API Design:")
    print("   ✅ __all__ ile public API tanımla")
    print("   ✅ Private fonksiyonları _ ile başlat")
    print("   ✅ Consistent naming conventions")
    print("   ✅ Backward compatibility düşün")
    
    print(f"\n4. 📚 Dokümantasyon:")
    print("   ✅ Comprehensive docstrings")
    print("   ✅ Type hints kullan")
    print("   ✅ Examples ve usage patterns")
    print("   ✅ Changelog tutun")
    
    print(f"\n5. 🧪 Testing:")
    print("   ✅ Unit tests yaz")
    print("   ✅ Test discovery conventions")
    print("   ✅ Mock external dependencies")
    print("   ✅ Continuous integration")
    
    print(f"\n6. 🚀 Performance:")
    print("   ✅ Lazy imports kullan")
    print("   ✅ Circular imports'tan kaçın")
    print("   ✅ Module-level cache kullan")
    print("   ✅ Profile ve optimize et")
    
    # Örnek best practice kodu
    best_practice_example = '''
# Good module structure example

"""
Module: data_processor

High-level data processing utilities for scientific computing.

This module provides efficient data processing functions with
built-in validation and error handling.
"""

from typing import List, Dict, Optional, Union
import logging
from pathlib import Path

__version__ = "1.0.0"
__all__ = ['process_data', 'validate_input', 'DataProcessor']

logger = logging.getLogger(__name__)

class DataProcessor:
    """Main data processing class."""
    
    def __init__(self, config: Optional[Dict] = None):
        self.config = config or {}
        self._cache = {}
    
    def process(self, data: List[Union[int, float]]) -> List[float]:
        """Process numerical data."""
        if not self._validate_input(data):
            raise ValueError("Invalid input data")
        
        # Processing logic here
        return [float(x) * 2 for x in data]
    
    def _validate_input(self, data: List) -> bool:
        """Private validation method."""
        return isinstance(data, list) and all(
            isinstance(x, (int, float)) for x in data
        )

def process_data(data: List[Union[int, float]]) -> List[float]:
    """Public API function for data processing."""
    processor = DataProcessor()
    return processor.process(data)
'''
    
    print(f"\n--- Best Practice Örnek Kod ---")
    print("Modül yapısı örneği:")
    print(best_practice_example[:500] + "...")

modul_best_practices()

print("\n💡 Modüller ve Paketler İpuçları:")
print("✅ Modül sistemi Python'ın code organization'ının temelidir")
print("✅ Import mekanizmasını iyi anlayın")
print("✅ Paket yapısını düşünerek tasarlayın")
print("✅ __all__ ile public API'yi kontrol edin")
print("✅ Dokümantasyonu ihmal etmeyin")
print("✅ Testing ve versioning önemlidir")
print("✅ Performance'ı göz önünde bulundurun")

print("\n🛠️  Geliştirme Araçları:")
print("• setuptools: Paket distribution")
print("• wheel: Binary distribution")
print("• pip: Package management")
print("• twine: PyPI upload")
print("• tox: Multi-environment testing")

print("\n✅ Python modül sistemi öğrenildi!")
print("✅ Import mekanizması öğrenildi!")
print("✅ Paket oluşturma teknikleri öğrenildi!")
print("✅ Best practices öğrenildi!")