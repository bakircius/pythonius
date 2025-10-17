"""
Python Import Sistemi ve Optimizasyon

Bu dosya Python'da import sisteminin derinlemesine analizi,
import hooks, meta path finders, import optimization
ve gelişmiş import teknikleri üzerine odaklanır.
"""

import sys
import importlib
import importlib.util
import importlib.machinery
from importlib.abc import Loader, MetaPathFinder
import types
import time
import os
from pathlib import Path
import ast
import dis
from typing import Optional, List, Any

# =============================================================================
# 1. İMPORT SİSTEMİ DERINLEMESINE ANALİZ
# =============================================================================

print("=== Import Sistemi Derinlemesine ===")

def import_sistem_analizi():
    """Python import sisteminin detaylı analizi"""
    
    print("🔍 Python Import Süreci:")
    print("1. sys.modules cache kontrolü")
    print("2. sys.meta_path finder'lar")
    print("3. Module spec oluşturma")
    print("4. Module object oluşturma")
    print("5. Module execution")
    print("6. sys.modules'e ekleme")
    
    # sys.modules analizi
    print(f"\n📦 sys.modules Analizi:")
    print(f"   • Toplam modül sayısı: {len(sys.modules)}")
    
    # Built-in vs imported modules
    builtin_count = len([m for m in sys.modules if m in sys.builtin_module_names])
    imported_count = len(sys.modules) - builtin_count
    
    print(f"   • Built-in modüller: {builtin_count}")
    print(f"   • İmport edilmiş: {imported_count}")
    
    # Module types analizi
    module_types = {}
    for module_name, module in sys.modules.items():
        if module is None:
            module_type = "None"
        else:
            module_type = type(module).__name__
        
        module_types[module_type] = module_types.get(module_type, 0) + 1
    
    print(f"\n📊 Modül Türü İstatistikleri:")
    for mod_type, count in sorted(module_types.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"   • {mod_type}: {count} adet")
    
    # Meta path finders
    print(f"\n🔍 Meta Path Finders:")
    for i, finder in enumerate(sys.meta_path, 1):
        finder_name = type(finder).__name__
        finder_module = type(finder).__module__
        print(f"   {i}. {finder_name} ({finder_module})")

import_sistem_analizi()

# =============================================================================
# 2. CUSTOM IMPORT HOOKS
# =============================================================================

print("\n=== Custom Import Hooks ===")

class DebugImportHook:
    """Import işlemlerini debug eden hook"""
    
    def __init__(self):
        self.import_log = []
        self.original_import = __builtins__.__import__
    
    def debug_import(self, name, globals=None, locals=None, fromlist=(), level=0):
        """Debug import wrapper"""
        start_time = time.time()
        
        try:
            result = self.original_import(name, globals, locals, fromlist, level)
            duration = time.time() - start_time
            
            self.import_log.append({
                'module': name,
                'fromlist': fromlist,
                'level': level,
                'duration': duration,
                'success': True
            })
            
            print(f"   🔍 Import: {name} ({duration:.4f}s)")
            return result
            
        except Exception as e:
            duration = time.time() - start_time
            
            self.import_log.append({
                'module': name,
                'fromlist': fromlist,
                'level': level,
                'duration': duration,
                'success': False,
                'error': str(e)
            })
            
            print(f"   ❌ Import failed: {name} - {e}")
            raise
    
    def install(self):
        """Hook'u yükle"""
        __builtins__.__import__ = self.debug_import
        print("   ✅ Debug import hook yüklendi")
    
    def uninstall(self):
        """Hook'u kaldır"""
        __builtins__.__import__ = self.original_import
        print("   ❌ Debug import hook kaldırıldı")
    
    def get_stats(self):
        """Import istatistiklerini döndür"""
        if not self.import_log:
            return "Henüz import işlemi yapılmadı"
        
        successful = [log for log in self.import_log if log['success']]
        failed = [log for log in self.import_log if not log['success']]
        
        total_time = sum(log['duration'] for log in successful)
        avg_time = total_time / len(successful) if successful else 0
        
        return {
            'total_imports': len(self.import_log),
            'successful': len(successful),
            'failed': len(failed),
            'total_time': total_time,
            'average_time': avg_time,
            'slowest': max(successful, key=lambda x: x['duration']) if successful else None
        }

def custom_import_hook_ornegi():
    """Custom import hook örneği"""
    
    print("🪝 Custom Import Hook Kullanımı:")
    
    # Debug hook oluştur
    debug_hook = DebugImportHook()
    
    print("\n--- Hook yüklü değil ---")
    import math  # Normal import
    
    # Hook'u yükle
    debug_hook.install()
    
    print("\n--- Hook yüklü ---")
    try:
        import json  # Debug edilecek
        import random  # Debug edilecek
        import nonexistent_module  # Hata verecek
    except ImportError:
        pass
    
    # Hook'u kaldır
    debug_hook.uninstall()
    
    # İstatistikleri göster
    stats = debug_hook.get_stats()
    print(f"\n📊 Import İstatistikleri:")
    if isinstance(stats, dict):
        print(f"   • Toplam import: {stats['total_imports']}")
        print(f"   • Başarılı: {stats['successful']}")
        print(f"   • Başarısız: {stats['failed']}")
        print(f"   • Toplam süre: {stats['total_time']:.4f}s")
        print(f"   • Ortalama süre: {stats['average_time']:.4f}s")
        
        if stats['slowest']:
            slowest = stats['slowest']
            print(f"   • En yavaş: {slowest['module']} ({slowest['duration']:.4f}s)")
    else:
        print(f"   {stats}")

custom_import_hook_ornegi()

# =============================================================================
# 3. META PATH FINDER OLUŞTURMA
# =============================================================================

print("\n=== Custom Meta Path Finder ===")

class VirtualModuleFinder(MetaPathFinder):
    """Virtual modüller için meta path finder"""
    
    def __init__(self):
        self.virtual_modules = {}
    
    def add_virtual_module(self, name: str, code: str):
        """Virtual modül ekle"""
        self.virtual_modules[name] = code
        print(f"   ✅ Virtual modül eklendi: {name}")
    
    def find_spec(self, fullname, path, target=None):
        """Module spec bulma"""
        if fullname in self.virtual_modules:
            loader = VirtualModuleLoader(fullname, self.virtual_modules[fullname])
            spec = importlib.machinery.ModuleSpec(fullname, loader)
            return spec
        return None

class VirtualModuleLoader(Loader):
    """Virtual modül loader"""
    
    def __init__(self, name: str, code: str):
        self.name = name
        self.code = code
    
    def create_module(self, spec):
        """Modül oluştur"""
        return None  # Default module creation
    
    def exec_module(self, module):
        """Modül execute et"""
        # Code'u compile et ve execute et
        compiled = compile(self.code, f"<virtual:{self.name}>", "exec")
        exec(compiled, module.__dict__)
        print(f"   🚀 Virtual modül execute edildi: {self.name}")

def meta_path_finder_ornegi():
    """Meta path finder örneği"""
    
    print("🔍 Custom Meta Path Finder:")
    
    # Virtual module finder oluştur
    virtual_finder = VirtualModuleFinder()
    
    # Virtual modül ekle
    virtual_code = '''
"""Virtual test modülü"""

def virtual_function():
    return "Virtual modülden merhaba!"

class VirtualClass:
    def __init__(self):
        self.name = "VirtualClass"
    
    def get_info(self):
        return f"Ben {self.name}'im, virtual bir sınıfım!"

VIRTUAL_CONSTANT = "Virtual sabit değer"
'''
    
    virtual_finder.add_virtual_module("virtual_test", virtual_code)
    
    # Finder'ı meta path'e ekle
    sys.meta_path.insert(0, virtual_finder)
    print("   📍 Meta path'e eklendi")
    
    try:
        # Virtual modülü import et
        print("\n🧪 Virtual modülü test et:")
        import virtual_test
        
        print(f"   📄 Docstring: {virtual_test.__doc__}")
        print(f"   ⚙️ Function: {virtual_test.virtual_function()}")
        
        obj = virtual_test.VirtualClass()
        print(f"   🏗️ Class: {obj.get_info()}")
        print(f"   🔢 Constant: {virtual_test.VIRTUAL_CONSTANT}")
        
    except Exception as e:
        print(f"   ❌ Virtual modül hatası: {e}")
    
    finally:
        # Temizlik
        if virtual_finder in sys.meta_path:
            sys.meta_path.remove(virtual_finder)
            print("   🧹 Meta path'den kaldırıldı")
        
        # Module cache'den kaldır
        if "virtual_test" in sys.modules:
            del sys.modules["virtual_test"]
            print("   🗑️ Module cache'den kaldırıldı")

meta_path_finder_ornegi()

# =============================================================================
# 4. İMPORT PERFORMANCe OPTİMİZASYONU
# =============================================================================

print("\n=== Import Performance Optimizasyonu ===")

def import_performance_analizi():
    """Import performance analizi ve optimizasyon"""
    
    print("⚡ Import Performance Factors:")
    print("• Module search time")
    print("• File I/O operations")
    print("• Code compilation")
    print("• Module execution")
    print("• Dependency chain")
    
    # Import timing measurement
    def measure_import_time(module_name, iterations=5):
        """Import süresini ölç"""
        times = []
        
        for i in range(iterations):
            # Module cache'den kaldır
            if module_name in sys.modules:
                del sys.modules[module_name]
            
            start = time.perf_counter()
            try:
                importlib.import_module(module_name)
                end = time.perf_counter()
                times.append(end - start)
            except ImportError:
                times.append(float('inf'))
        
        return {
            'module': module_name,
            'times': times,
            'avg': sum(t for t in times if t != float('inf')) / len([t for t in times if t != float('inf')]) if any(t != float('inf') for t in times) else 0,
            'min': min(t for t in times if t != float('inf')) if any(t != float('inf') for t in times) else 0,
            'max': max(t for t in times if t != float('inf')) if any(t != float('inf') for t in times) else 0
        }
    
    # Test modülleri
    test_modules = ['json', 'os', 'sys', 'math', 'random']
    
    print(f"\n📊 Import Performance Analizi:")
    results = []
    
    for module in test_modules:
        result = measure_import_time(module, iterations=3)
        results.append(result)
        print(f"   • {module}: avg={result['avg']:.4f}s, min={result['min']:.4f}s, max={result['max']:.4f}s")
    
    # En yavaş modül
    slowest = max(results, key=lambda x: x['avg'])
    fastest = min(results, key=lambda x: x['avg'])
    
    print(f"\n🐌 En yavaş: {slowest['module']} ({slowest['avg']:.4f}s)")
    print(f"🚀 En hızlı: {fastest['module']} ({fastest['avg']:.4f}s)")

def import_optimization_teknikleri():
    """Import optimizasyon teknikleri"""
    
    print(f"\n🚀 Import Optimization Teknikleri:")
    
    # 1. Lazy import
    print("1. 💤 Lazy Import:")
    lazy_example = '''
# Yavaş - module loading time
import heavy_module

def process_data():
    return heavy_module.process()

# Hızlı - on-demand loading
def process_data():
    import heavy_module  # Fonksiyon çağrıldığında yükle
    return heavy_module.process()
'''
    print("   " + "\n   ".join(lazy_example.strip().split('\n')[:8]))
    
    # 2. Conditional import
    print(f"\n2. 🔀 Conditional Import:")
    conditional_example = '''
# Optional dependency
try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False

def advanced_computation(data):
    if HAS_NUMPY:
        return np.array(data).mean()
    else:
        return sum(data) / len(data)
'''
    print("   " + "\n   ".join(conditional_example.strip().split('\n')))
    
    # 3. Import aliasing for performance
    print(f"\n3. 🏷️ Strategic Import Aliasing:")
    aliasing_example = '''
# Yavaş - attribute lookup
import math
result = math.sqrt(math.pow(x, 2) + math.pow(y, 2))

# Hızlı - local reference
from math import sqrt, pow
result = sqrt(pow(x, 2) + pow(y, 2))
'''
    print("   " + "\n   ".join(aliasing_example.strip().split('\n')))
    
    # 4. Module preloading
    print(f"\n4. 📦 Module Preloading:")
    preload_example = '''
# Application startup'ta kritik modülleri önceden yükle
PRELOAD_MODULES = [
    'json', 'os', 'sys', 'math', 'random',
    'datetime', 'collections', 'itertools'
]

def preload_modules():
    for module_name in PRELOAD_MODULES:
        try:
            importlib.import_module(module_name)
        except ImportError:
            pass
'''
    print("   " + "\n   ".join(preload_example.strip().split('\n')))

import_performance_analizi()
import_optimization_teknikleri()

# =============================================================================
# 5. DİNAMİK MODULE CREATION
# =============================================================================

print("\n=== Dinamik Module Creation ===")

def dinamik_module_creation():
    """Runtime'da dinamik modül oluşturma"""
    
    print("🏗️ Dinamik Modül Oluşturma Teknikleri:")
    
    # 1. types.ModuleType ile
    print("\n1. 📦 types.ModuleType ile Oluşturma:")
    
    # Dinamik modül oluştur
    dynamic_module = types.ModuleType('dynamic_example')
    dynamic_module.__doc__ = "Dinamik olarak oluşturulan örnek modül"
    dynamic_module.__file__ = "<dynamic>"
    
    # Modüle içerik ekle
    def dynamic_function(x, y):
        return x * y + 42
    
    class DynamicClass:
        def __init__(self, value):
            self.value = value
        
        def compute(self):
            return self.value ** 2
    
    # Modüle ata
    dynamic_module.dynamic_function = dynamic_function
    dynamic_module.DynamicClass = DynamicClass
    dynamic_module.CONSTANT = "Dynamic constant"
    
    # sys.modules'e ekle
    sys.modules['dynamic_example'] = dynamic_module
    
    print("   ✅ Dinamik modül oluşturuldu")
    
    # Test et
    import dynamic_example
    print(f"   🧪 Function test: {dynamic_example.dynamic_function(5, 3)}")
    
    obj = dynamic_example.DynamicClass(7)
    print(f"   🏗️ Class test: {obj.compute()}")
    print(f"   🔢 Constant: {dynamic_example.CONSTANT}")
    
    # 2. String'den modül oluşturma
    print(f"\n2. 📄 String'den Modül Oluşturma:")
    
    module_code = '''
"""String'den oluşturulan modül"""

import math

def calculate_circle_area(radius):
    """Daire alanı hesapla"""
    return math.pi * radius ** 2

class Calculator:
    """Hesap makinesi sınıfı"""
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def get_history(self):
        return self.history.copy()

VERSION = "1.0.0"
'''
    
    # String'den modül oluştur
    string_module = types.ModuleType('string_module')
    string_module.__file__ = "<string>"
    
    # Kodu compile et ve execute et
    compiled_code = compile(module_code, '<string_module>', 'exec')
    exec(compiled_code, string_module.__dict__)
    
    # sys.modules'e ekle
    sys.modules['string_module'] = string_module
    
    print("   ✅ String'den modül oluşturuldu")
    
    # Test et
    import string_module
    area = string_module.calculate_circle_area(5)
    print(f"   🧪 Circle area (r=5): {area:.2f}")
    
    calc = string_module.Calculator()
    result = calc.add(10, 20)
    print(f"   🧮 Calculator: {result}")
    print(f"   📋 History: {calc.get_history()}")
    print(f"   📌 Version: {string_module.VERSION}")
    
    # 3. Template-based module creation
    print(f"\n3. 📋 Template-based Modül Oluşturma:")
    
    module_template = '''
"""Template-based modül: {module_name}"""

class {class_name}:
    def __init__(self):
        self.name = "{class_name}"
        self.module = "{module_name}"
    
    def get_info(self):
        return f"{{self.name}} from {{self.module}}"

def {function_name}():
    return "Hello from {module_name}!"

{constant_name} = "{constant_value}"
'''
    
    # Template'i doldur
    filled_template = module_template.format(
        module_name="templated_module",
        class_name="TemplatedClass",
        function_name="templated_function", 
        constant_name="TEMPLATED_CONSTANT",
        constant_value="Template value"
    )
    
    # Modül oluştur
    templated_module = types.ModuleType('templated_module')
    templated_module.__file__ = "<template>"
    
    compiled_template = compile(filled_template, '<templated_module>', 'exec')
    exec(compiled_template, templated_module.__dict__)
    
    sys.modules['templated_module'] = templated_module
    
    print("   ✅ Template-based modül oluşturuldu")
    
    # Test et
    import templated_module
    obj = templated_module.TemplatedClass()
    print(f"   🏗️ Class: {obj.get_info()}")
    print(f"   ⚙️ Function: {templated_module.templated_function()}")
    print(f"   🔢 Constant: {templated_module.TEMPLATED_CONSTANT}")

dinamik_module_creation()

# =============================================================================
# 6. İMPORT DEBUGGING VE ANALİZ ARAÇLARI
# =============================================================================

print("\n=== Import Debugging Araçları ===")

class ImportAnalyzer:
    """Import analizi ve debugging araçları"""
    
    def __init__(self):
        self.import_trace = []
        self.dependency_graph = {}
    
    def trace_imports(self, module_name):
        """Modül import'larını trace et"""
        if module_name not in sys.modules:
            print(f"   ❌ Modül bulunamadı: {module_name}")
            return
        
        module = sys.modules[module_name]
        
        # Modül bilgilerini topla
        module_info = {
            'name': module_name,
            'file': getattr(module, '__file__', '<built-in>'),
            'package': getattr(module, '__package__', None),
            'path': getattr(module, '__path__', None),
            'spec': getattr(module, '__spec__', None)
        }
        
        self.import_trace.append(module_info)
        return module_info
    
    def analyze_dependencies(self, module_name):
        """Modül bağımlılıklarını analiz et"""
        if module_name not in sys.modules:
            return {}
        
        module = sys.modules[module_name]
        dependencies = set()
        
        # Module'ün __dict__'indeki import'ları bul
        for attr_name, attr_value in module.__dict__.items():
            if isinstance(attr_value, types.ModuleType):
                dep_name = getattr(attr_value, '__name__', attr_name)
                if dep_name != module_name:
                    dependencies.add(dep_name)
        
        self.dependency_graph[module_name] = list(dependencies)
        return list(dependencies)
    
    def get_import_stats(self):
        """Import istatistiklerini döndür"""
        total_modules = len(sys.modules)
        traced_modules = len(self.import_trace)
        
        file_modules = sum(1 for info in self.import_trace if info['file'] != '<built-in>')
        builtin_modules = traced_modules - file_modules
        
        return {
            'total_modules_in_system': total_modules,
            'traced_modules': traced_modules,
            'file_based_modules': file_modules,
            'builtin_modules': builtin_modules,
            'dependency_graph_size': len(self.dependency_graph)
        }

def import_debugging_ornegi():
    """Import debugging örneği"""
    
    print("🔧 Import Analyzer Kullanımı:")
    
    analyzer = ImportAnalyzer()
    
    # Bazı modülleri analiz et
    test_modules = ['json', 'os', 'math', 'sys']
    
    print(f"\n📊 Modül Analizi:")
    for module_name in test_modules:
        info = analyzer.trace_imports(module_name)
        if info:
            print(f"   📦 {module_name}:")
            print(f"      Dosya: {info['file']}")
            print(f"      Package: {info['package']}")
        
        deps = analyzer.analyze_dependencies(module_name)
        if deps:
            print(f"      Bağımlılıklar: {', '.join(deps[:5])}")
            if len(deps) > 5:
                print(f"      ... ve {len(deps)-5} tane daha")
    
    # İstatistikler
    stats = analyzer.get_import_stats()
    print(f"\n📈 Import İstatistikleri:")
    for key, value in stats.items():
        print(f"   • {key.replace('_', ' ').title()}: {value}")
    
    # Dependency graph gösterimi
    print(f"\n🕸️ Dependency Graph (örnek):")
    for module, deps in list(analyzer.dependency_graph.items())[:3]:
        if deps:
            print(f"   {module} -> {', '.join(deps[:3])}")
            if len(deps) > 3:
                print(f"      ... (+{len(deps)-3} tane daha)")

import_debugging_ornegi()

print("\n💡 Import Sistemi İpuçları:")
print("✅ Import cache'i (sys.modules) etkili kullanın")
print("✅ Lazy import ile startup time'ı optimize edin")
print("✅ Circular import'lardan kaçının")
print("✅ Import hooks dikkatli kullanın")
print("✅ Performance critical path'lerde import profiling yapın")
print("✅ Virtual modules ile testing'i kolaylaştırın")
print("✅ Custom finders ile special use case'leri çözün")

print("\n🚀 İleri Seviye Import Konuları:")
print("• ImportError handling strategies")
print("• Module reloading in production")
print("• Import-time side effects")
print("• Thread-safe importing")
print("• Namespace package advanced usage")

print("\n✅ Python import sistemi derinlemesine öğrenildi!")
print("✅ Custom import hooks ve finders öğrenildi!")
print("✅ Import performance optimizasyonu öğrenildi!")
print("✅ Dinamik modül oluşturma teknikleri öğrenildi!")