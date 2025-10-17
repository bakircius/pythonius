# 📦 Modüller ve Paketler (Modules & Packages)

Python'da modüler programlama, package oluşturma, import sistemi ve modern Python package development.

## 📚 Kapsam

Bu bölümde Python'da modüller ve paketlerin tüm yönlerini öğreneceksiniz:

### 🎯 Modül Temelleri
- Modül kavramı ve import sistemi
- Namespace yönetimi
- Module search path (sys.path)
- Import çeşitleri ve optimizasyon
- Circular import sorunları ve çözümleri

### 📦 Package Development
- Package yapısı ve __init__.py
- setup.py ve modern build tools
- pyproject.toml (PEP 517/518)
- Virtual environment yönetimi
- Dependency management

### 🔧 Advanced Import Techniques
- Custom import hooks
- Meta path finders
- Dynamic module creation
- Import performance optimization
- Import debugging tools

### 📚 Standard Library Mastery
- Core utility modules
- Data structures ve collections
- Text processing ve regex
- Cryptography ve security
- Modern Python features

## 🎯 Öğrenme Hedefleri

Bu bölümü tamamladığınızda şunları öğrenmiş olacaksınız:

### 🏗️ Modüler Programlama
- ✅ Modül tasarımı ve best practices
- ✅ Import sistemini etkili kullanma
- ✅ Namespace pollution'ı önleme
- ✅ Code organization teknikleri
- ✅ Dependency injection patterns

### 📦 Package Development Skills
- ✅ Professional package structure
- ✅ Modern build systems (Poetry, setuptools)
- ✅ Distribution ve PyPI publishing
- ✅ Version management (SemVer)
- ✅ Documentation ve testing

### 🚀 Advanced Techniques
- ✅ Custom import hooks yazma
- ✅ Dynamic module creation
- ✅ Import performance optimization
- ✅ Plugin systems tasarlama
- ✅ Meta-programming techniques

### 📚 Standard Library Expertise
- ✅ Built-in modules'ı etkili kullanma
- ✅ Performance-critical modules
- ✅ Security ve cryptography modules
- ✅ Modern Python features (dataclasses, enum)
- ✅ Debugging ve profiling tools

## 📁 Örnek Dosyalar

### 1. 📖 `modul_temelleri.py`
**Modül kavramı ve temel import sistemi**
- Python modül sistemi analizi
- Import çeşitleri ve kulımları
- sys.modules ve module cache
- Module introspection teknikleri
- Circular import sorunları

```python
# Import çeşitleri
import math
import numpy as np
from math import sqrt, pi
from collections import defaultdict, Counter

# Dynamic import
module_name = 'json'
json_module = importlib.import_module(module_name)
```

### 2. 🏗️ `package_olusturma.py`
**Professional package development**
- Package yapısı ve organizasyon
- setup.py ve pyproject.toml
- Modern build tools (Poetry)
- CI/CD pipeline setup
- Package security practices

```python
# Package yapısı örneği
my_package/
├── src/
│   └── my_package/
│       ├── __init__.py
│       ├── core/
│       └── utils/
├── tests/
├── docs/
├── pyproject.toml
└── README.md
```

### 3. ⚡ `import_sistemi.py`
**Advanced import techniques ve optimization**
- Custom import hooks
- Meta path finders
- Dynamic module creation
- Import performance profiling
- Virtual modules

```python
# Custom meta path finder
class VirtualModuleFinder(MetaPathFinder):
    def find_spec(self, fullname, path, target=None):
        if fullname in self.virtual_modules:
            return ModuleSpec(fullname, VirtualLoader())
        return None
```

### 4. 📚 `standart_kutuphane.py`
**Standard Library comprehensive guide**
- Core utility modules
- Collections ve data structures
- Text processing ve regex
- Cryptography modules
- Performance tools

```python
# Standard library highlights
from collections import Counter, defaultdict
from itertools import combinations, groupby
from functools import lru_cache, partial
from datetime import datetime, timedelta
import hashlib, secrets, uuid
```

## 🎖️ Practical Projects

### 🔥 Project 1: Plugin System
```python
class PluginManager:
    def __init__(self):
        self.plugins = {}
    
    def discover_plugins(self, package_name):
        """Package'dan plugin'leri keşfet"""
        for finder, name, ispkg in pkgutil.iter_modules():
            if name.startswith(f"{package_name}_"):
                self.load_plugin(name)
    
    def load_plugin(self, plugin_name):
        """Plugin'i dinamik olarak yükle"""
        module = importlib.import_module(plugin_name)
        self.plugins[plugin_name] = module
```

### 📦 Project 2: Package Template Generator
```python
class PackageGenerator:
    def __init__(self, package_name):
        self.package_name = package_name
        self.template_dir = Path("templates")
    
    def generate_structure(self):
        """Package yapısını oluştur"""
        self.create_directories()
        self.generate_files()
        self.setup_venv()
        self.install_dev_tools()
```

### 🔧 Project 3: Import Analyzer
```python
class ImportAnalyzer:
    def analyze_project(self, project_path):
        """Proje import'larını analiz et"""
        imports = self.extract_imports(project_path)
        dependencies = self.build_dependency_graph(imports)
        return self.generate_report(dependencies)
```

## 🚀 İleri Seviye Konular

### 🎯 Advanced Package Development
- Binary extensions (C/C++)
- Cross-platform compatibility
- Performance optimization
- Memory management
- Threading ve multiprocessing

### 🔍 Import System Internals
- Import hooks ve finders
- Module compilation process
- Bytecode caching
- Import security considerations
- Custom loaders

### 📈 Enterprise Patterns
- Microservice package architecture
- Plugin ecosystems
- Configuration management
- Logging ve monitoring
- Deployment strategies

## 💡 Best Practices

### ✅ Modül Tasarımı
- Single responsibility principle
- Clear interfaces ve APIs
- Backward compatibility
- Error handling
- Documentation

### ✅ Package Development
- Semantic versioning
- Automated testing
- CI/CD pipelines
- Security scanning
- Performance monitoring

### ✅ Import Optimization
- Lazy loading strategies
- Import time minimization
- Dependency management
- Circular import prevention
- Performance profiling

## 🎯 Sonraki Adımlar

Bu bölümü tamamladıktan sonra:
1. **Object-Oriented Programming** - Sınıf tasarımı
2. **Functional Programming** - Fonksiyonel paradigmalar
3. **Async Programming** - Asenkron programlama
4. **Web Development** - Framework'ler
5. **Data Science** - NumPy, Pandas

## 📚 Ek Kaynaklar

- **PEP 420**: Implicit Namespace Packages
- **PEP 517/518**: Build system interface
- **Poetry Documentation**: Modern package management
- **PyPI Guide**: Package publishing
- **Tools**: black, flake8, mypy, pytest

---

🎯 **Hedef**: Professional Python package developer olun!

⚡ **Practice**: Kendi package'ınızı PyPI'da yayınlayın!

🚀 **Level Up**: Open source projelere katkıda bulunun!