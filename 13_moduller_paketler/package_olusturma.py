"""
Python Package Oluşturma ve Yönetimi

Bu dosya Python'da package oluşturma, __init__.py kullanımı,
setup.py ile package dağıtımı ve modern package tools'larını ele alır.
"""

import os
import sys
import subprocess
import tempfile
import shutil
from pathlib import Path
import importlib
import json
from textwrap import dedent

# =============================================================================
# 1. PACKAGE YAPISI VE __INIT__.PY
# =============================================================================

print("=== Package Yapısı ve __init__.py ===")

def package_yapisi_ornegi():
    """Package yapısı ve __init__.py kullanımı"""
    
    print("📦 Python Package Nedir?")
    print("• Modülleri organize eden dizin yapısı")
    print("• __init__.py dosyası ile tanımlanır")
    print("• Hiyerarşik organizasyon sağlar")
    print("• Namespace oluşturur")
    
    # Geçici package oluştur
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        package_path = temp_path / "sample_package"
        
        print(f"\n🏗️ Örnek Package Oluşturma: {package_path.name}")
        
        # Package yapısını oluştur
        create_sample_package(package_path)
        
        # sys.path'e ekle
        sys.path.insert(0, str(temp_path))
        
        try:
            # Package'ı test et
            test_sample_package()
        finally:
            # sys.path'den kaldır
            if str(temp_path) in sys.path:
                sys.path.remove(str(temp_path))

def create_sample_package(package_path):
    """Örnek package yapısı oluştur"""
    
    # Ana package dizini
    package_path.mkdir(parents=True, exist_ok=True)
    
    # Subpackage dizinleri
    (package_path / "core").mkdir(exist_ok=True)
    (package_path / "utils").mkdir(exist_ok=True)
    (package_path / "data").mkdir(exist_ok=True)
    
    # Ana __init__.py
    main_init = '''"""
Sample Package - Örnek Python Package

Bu package Python package geliştirme örnekleri içerir.
"""

__version__ = "1.0.0"
__author__ = "Python Developer"
__email__ = "dev@example.com"

# Package seviyesinde import'lar
from .core.main import MainClass, main_function
from .utils.helpers import helper_function
from .data import DATA_VERSION

# __all__ ile public API tanımla
__all__ = [
    'MainClass',
    'main_function', 
    'helper_function',
    'DATA_VERSION'
]

# Package yüklendiğinde çalışacak kod
print(f"📦 {__name__} package loaded (v{__version__})")
'''
    
    (package_path / "__init__.py").write_text(dedent(main_init), encoding='utf-8')
    
    # Core subpackage
    core_init = '''"""
Core module - Ana işlevsellik
"""
from .main import MainClass, main_function
from .advanced import AdvancedClass

__all__ = ['MainClass', 'main_function', 'AdvancedClass']
'''
    
    (package_path / "core" / "__init__.py").write_text(dedent(core_init), encoding='utf-8')
    
    # Core main module
    core_main = '''"""
Ana core modülü
"""

class MainClass:
    """Ana sınıf"""
    
    def __init__(self, name="Main"):
        self.name = name
        self.version = "1.0.0"
    
    def get_info(self):
        """Bilgi döndür"""
        return f"MainClass: {self.name} v{self.version}"
    
    def process_data(self, data):
        """Veri işle"""
        if isinstance(data, list):
            return [item * 2 for item in data]
        elif isinstance(data, dict):
            return {k: v * 2 for k, v in data.items()}
        else:
            return str(data) * 2

def main_function(x, y=10):
    """Ana fonksiyon"""
    return x + y
'''
    
    (package_path / "core" / "main.py").write_text(dedent(core_main), encoding='utf-8')
    
    # Core advanced module
    core_advanced = '''"""
Gelişmiş core modülü
"""

class AdvancedClass:
    """Gelişmiş sınıf"""
    
    def __init__(self):
        self.features = ["advanced", "scalable", "efficient"]
    
    def get_features(self):
        return self.features
    
    def complex_operation(self, data):
        """Karmaşık işlem"""
        if not data:
            return None
        return {
            'input': data,
            'processed': len(str(data)),
            'features_count': len(self.features)
        }
'''
    
    (package_path / "core" / "advanced.py").write_text(dedent(core_advanced), encoding='utf-8')
    
    # Utils subpackage
    utils_init = '''"""
Utilities - Yardımcı fonksiyonlar
"""
from .helpers import helper_function, calculate
from .formatters import format_data

__all__ = ['helper_function', 'calculate', 'format_data']
'''
    
    (package_path / "utils" / "__init__.py").write_text(dedent(utils_init), encoding='utf-8')
    
    # Utils helpers
    utils_helpers = '''"""
Yardımcı fonksiyonlar
"""

def helper_function(text):
    """Yardımcı fonksiyon"""
    return f"Helper processed: {text}"

def calculate(a, b, operation="add"):
    """Hesaplama fonksiyonu"""
    operations = {
        "add": lambda x, y: x + y,
        "multiply": lambda x, y: x * y,
        "subtract": lambda x, y: x - y,
        "divide": lambda x, y: x / y if y != 0 else None
    }
    
    if operation in operations:
        return operations[operation](a, b)
    else:
        raise ValueError(f"Desteklenmeyen işlem: {operation}")
'''
    
    (package_path / "utils" / "helpers.py").write_text(dedent(utils_helpers), encoding='utf-8')
    
    # Utils formatters
    utils_formatters = '''"""
Veri formatlama fonksiyonları
"""

def format_data(data, format_type="json"):
    """Veri formatlama"""
    import json
    
    if format_type == "json":
        return json.dumps(data, indent=2, ensure_ascii=False)
    elif format_type == "str":
        return str(data)
    elif format_type == "repr":
        return repr(data)
    else:
        return str(data)
'''
    
    (package_path / "utils" / "formatters.py").write_text(dedent(utils_formatters), encoding='utf-8')
    
    # Data subpackage (sadece data içerir)
    data_init = '''"""
Data modülü - Sabit veriler
"""

DATA_VERSION = "2023.1"
SAMPLE_DATA = {
    "users": ["alice", "bob", "charlie"],
    "settings": {
        "debug": True,
        "max_connections": 100
    }
}

def get_sample_data():
    """Örnek veri döndür"""
    return SAMPLE_DATA.copy()
'''
    
    (package_path / "data" / "__init__.py").write_text(dedent(data_init), encoding='utf-8')
    
    print(f"   ✅ Package yapısı oluşturuldu")
    print(f"   📁 Ana package: {package_path.name}")
    print(f"   📁 Subpackages: core, utils, data")
    print(f"   📄 Modül sayısı: 6 adet")

def test_sample_package():
    """Oluşturulan package'ı test et"""
    
    print(f"\n🧪 Package Test Süreci:")
    
    try:
        # Ana package import
        import sample_package
        print(f"   ✅ Package imported: {sample_package.__name__}")
        print(f"   📌 Version: {sample_package.__version__}")
        print(f"   👤 Author: {sample_package.__author__}")
        
        # MainClass test
        main_obj = sample_package.MainClass("TestMain")
        print(f"   🏗️ MainClass: {main_obj.get_info()}")
        
        # Ana fonksiyon test
        result = sample_package.main_function(5, 15)
        print(f"   ⚙️ main_function(5, 15): {result}")
        
        # Helper fonksiyon test
        helper_result = sample_package.helper_function("test data")
        print(f"   🛠️ helper_function: {helper_result}")
        
        # Data version test
        print(f"   📊 Data version: {sample_package.DATA_VERSION}")
        
        # Subpackage test
        from sample_package.core import AdvancedClass
        advanced = AdvancedClass()
        print(f"   🚀 AdvancedClass features: {advanced.get_features()}")
        
        # Utility functions test
        from sample_package.utils import calculate, format_data
        calc_result = calculate(10, 3, "multiply")
        print(f"   🧮 calculate(10, 3, multiply): {calc_result}")
        
        # Data formatting test
        test_data = {"name": "test", "value": 42}
        formatted = format_data(test_data)
        print(f"   📋 Formatted data: {formatted[:50]}...")
        
        # Package docstring
        print(f"   📝 Package docstring: {sample_package.__doc__[:100]}...")
        
    except Exception as e:
        print(f"   ❌ Test hatası: {e}")

package_yapisi_ornegi()

# =============================================================================
# 2. SETUP.PY VE PACKAGE DAĞITIMI
# =============================================================================

print("\n=== Setup.py ve Package Dağıtımı ===")

def setup_py_ornegi():
    """Setup.py oluşturma ve package dağıtımı"""
    
    print("📦 Setup.py Nedir?")
    print("• Package metadata ve build konfigürasyonu")
    print("• pip install ile kurulum için gerekli")
    print("• PyPI'a upload için kullanılır")
    print("• Dependencies tanımlar")
    
    # Örnek setup.py içeriği
    setup_py_content = '''"""
Setup script for sample package
"""
from setuptools import setup, find_packages

# README dosyasını oku
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Requirements dosyasını oku
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="sample-package",
    version="1.0.0",
    author="Python Developer",
    author_email="dev@example.com",
    description="Örnek Python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/username/sample-package",
    project_urls={
        "Bug Tracker": "https://github.com/username/sample-package/issues",
        "Documentation": "https://sample-package.readthedocs.io/",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.910",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=1.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "sample-cli=sample_package.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "sample_package": ["data/*.json", "templates/*.html"],
    },
)
'''
    
    print(f"\n📄 Örnek setup.py içeriği:")
    lines = setup_py_content.strip().split('\n')
    for i, line in enumerate(lines[:30], 1):  # İlk 30 satır
        print(f"   {i:2d}: {line}")
    if len(lines) > 30:
        print(f"   ... (+{len(lines)-30} satır daha)")
    
    # Requirements.txt örneği
    requirements_content = '''# Production dependencies
requests>=2.25.0
click>=8.0.0
pydantic>=1.8.0

# Optional dependencies  
numpy>=1.20.0; extra == "scientific"
pandas>=1.3.0; extra == "scientific"
'''
    
    print(f"\n📄 requirements.txt örneği:")
    for i, line in enumerate(requirements_content.strip().split('\n'), 1):
        print(f"   {i}: {line}")
    
    # Manifest.in örneği
    manifest_content = '''include README.md
include LICENSE
include requirements.txt
recursive-include sample_package/data *.json
recursive-include sample_package/templates *.html
recursive-exclude * __pycache__
recursive-exclude * *.py[co]
'''
    
    print(f"\n📄 MANIFEST.in örneği:")
    for i, line in enumerate(manifest_content.strip().split('\n'), 1):
        print(f"   {i}: {line}")

setup_py_ornegi()

# =============================================================================
# 3. MODERN PACKAGE TOOLS (PYPROJECT.TOML)
# =============================================================================

print("\n=== Modern Package Tools ===")

def modern_package_tools():
    """Modern package araçları ve pyproject.toml"""
    
    print("🚀 Modern Python Package Development:")
    print("• pyproject.toml (PEP 517/518)")
    print("• Poetry: Dependency management")
    print("• setuptools-scm: Version management")
    print("• build: Universal build tool")
    print("• twine: PyPI upload")
    
    # pyproject.toml örneği
    pyproject_content = '''[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "sample-package"
version = "1.0.0"
authors = [
    {name = "Python Developer", email = "dev@example.com"},
]
description = "Örnek Python package"
readme = "README.md"
license = {text = "MIT"}
requires-python = ">=3.8"
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
]
keywords = ["example", "package", "tutorial"]
dependencies = [
    "requests>=2.25.0",
    "click>=8.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=6.0",
    "black>=21.0",
    "flake8>=3.8",
    "mypy>=0.910",
]
docs = [
    "sphinx>=4.0",
    "sphinx-rtd-theme>=1.0",
]

[project.urls]
Homepage = "https://github.com/username/sample-package"
Documentation = "https://sample-package.readthedocs.io/"
Repository = "https://github.com/username/sample-package.git"
"Bug Tracker" = "https://github.com/username/sample-package/issues"

[project.scripts]
sample-cli = "sample_package.cli:main"

[tool.setuptools]
packages = ["sample_package"]

[tool.setuptools.package-data]
sample_package = ["data/*.json", "templates/*.html"]

[tool.black]
line-length = 88
target-version = ['py38']
include = '\\.pyi?$'

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]

[tool.mypy]
python_version = "3.8"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
'''
    
    print(f"\n📄 pyproject.toml örneği:")
    lines = pyproject_content.strip().split('\n')
    for i, line in enumerate(lines[:25], 1):  # İlk 25 satır
        print(f"   {i:2d}: {line}")
    if len(lines) > 25:
        print(f"   ... (+{len(lines)-25} satır daha)")
    
    # Poetry kullanımı
    print(f"\n🎭 Poetry Kullanımı:")
    poetry_commands = [
        "poetry new sample-package",
        "poetry add requests",
        "poetry add --group dev pytest black",
        "poetry install",
        "poetry build",
        "poetry publish"
    ]
    
    for i, cmd in enumerate(poetry_commands, 1):
        print(f"   {i}. {cmd}")
    
    # Package build süreci
    print(f"\n🔨 Package Build Süreci:")
    build_steps = [
        "1. pyproject.toml veya setup.py hazırla",
        "2. README.md ve LICENSE ekle", 
        "3. Version'u güncelle",
        "4. python -m build (wheel ve sdist)",
        "5. twine check dist/*",
        "6. twine upload --repository testpypi dist/*",
        "7. Test installation",
        "8. twine upload dist/* (production)"
    ]
    
    for step in build_steps:
        print(f"   {step}")

modern_package_tools()

# =============================================================================
# 4. VIRTUAL ENVIRONMENT VE DEPENDENCY MANAGEMENT
# =============================================================================

print("\n=== Virtual Environment ve Dependencies ===")

def virtual_environment_ornegi():
    """Virtual environment ve dependency management"""
    
    print("🌐 Virtual Environment Nedir?")
    print("• İzole Python ortamı")
    print("• Package conflict'lerini önler")
    print("• Proje başına farklı dependencies")
    print("• Üretim ortamı simülasyonu")
    
    print(f"\n🛠️ Virtual Environment Araçları:")
    
    # venv (built-in)
    print("1. 📦 venv (Python built-in):")
    venv_commands = [
        "python -m venv myenv",
        "source myenv/bin/activate  # Linux/Mac",
        "myenv\\Scripts\\activate.bat  # Windows",
        "pip install package_name",
        "deactivate"
    ]
    for cmd in venv_commands:
        print(f"   • {cmd}")
    
    # virtualenv
    print("\n2. 🔧 virtualenv:")
    virtualenv_commands = [
        "pip install virtualenv",
        "virtualenv myenv",
        "source myenv/bin/activate",
        "pip install -r requirements.txt"
    ]
    for cmd in virtualenv_commands:
        print(f"   • {cmd}")
    
    # conda
    print("\n3. 🐍 conda:")
    conda_commands = [
        "conda create -n myenv python=3.9",
        "conda activate myenv",
        "conda install package_name",
        "conda env export > environment.yml"
    ]
    for cmd in conda_commands:
        print(f"   • {cmd}")
    
    # pipenv
    print("\n4. 🧪 pipenv:")
    pipenv_commands = [
        "pip install pipenv",
        "pipenv install requests",
        "pipenv install pytest --dev",
        "pipenv shell",
        "pipenv lock"
    ]
    for cmd in pipenv_commands:
        print(f"   • {cmd}")
    
    # Dependency management best practices
    print(f"\n📋 Dependency Management Best Practices:")
    best_practices = [
        "requirements.txt için exact versions kullanın",
        "requirements-dev.txt ile dev dependencies ayırın",
        "pip-tools ile dependency resolution",
        "Security audit için pip-audit kullanın",
        "License compatibility kontrol edin",
        "Dependency graph analizi yapın",
        "Automated dependency updates (Dependabot)"
    ]
    
    for i, practice in enumerate(best_practices, 1):
        print(f"   {i}. {practice}")

virtual_environment_ornegi()

# =============================================================================
# 5. PACKAGE TESTING VE CI/CD
# =============================================================================

print("\n=== Package Testing ve CI/CD ===")

def package_testing_ornegi():
    """Package testing ve continuous integration"""
    
    print("🧪 Package Testing Stratejisi:")
    
    # Test yapısı
    test_structure = '''
package_name/
├── src/
│   └── package_name/
│       ├── __init__.py
│       └── main.py
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   ├── test_integration.py
│   └── conftest.py
├── docs/
├── .github/
│   └── workflows/
│       └── ci.yml
├── pyproject.toml
├── README.md
└── .gitignore
'''
    
    print("📁 Test Klasör Yapısı:")
    print(test_structure)
    
    # pytest configuration
    pytest_config = '''# conftest.py
import pytest
from package_name import create_app

@pytest.fixture
def app():
    """Test app fixture"""
    return create_app(testing=True)

@pytest.fixture
def client(app):
    """Test client fixture"""
    return app.test_client()

# Test örneği
def test_main_function():
    from package_name.main import main_function
    result = main_function(5, 10)
    assert result == 15

def test_main_class():
    from package_name.main import MainClass
    obj = MainClass("test")
    assert obj.name == "test"
    assert "test" in obj.get_info()
'''
    
    print("🧪 pytest Configuration:")
    for i, line in enumerate(pytest_config.strip().split('\n'), 1):
        print(f"   {i:2d}: {line}")
    
    # GitHub Actions CI
    github_actions = '''name: CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, "3.10", "3.11"]

    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -e .[dev]
    
    - name: Lint with flake8
      run: |
        flake8 src tests
    
    - name: Type check with mypy
      run: |
        mypy src
    
    - name: Test with pytest
      run: |
        pytest --cov=package_name --cov-report=xml
    
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
'''
    
    print(f"\n🔄 GitHub Actions CI örneği:")
    lines = github_actions.strip().split('\n')
    for i, line in enumerate(lines[:20], 1):
        print(f"   {i:2d}: {line}")
    print(f"   ... (+{len(lines)-20} satır daha)")
    
    # Pre-commit hooks
    print(f"\n🪝 Pre-commit Hooks (.pre-commit-config.yaml):")
    precommit_config = '''repos:
  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
      - id: black
        language_version: python3

  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.3.0
    hooks:
      - id: mypy
'''
    
    for i, line in enumerate(precommit_config.strip().split('\n'), 1):
        print(f"   {i:2d}: {line}")

package_testing_ornegi()

# =============================================================================
# 6. PACKAGE DOCUMENTATION
# =============================================================================

print("\n=== Package Documentation ===")

def package_documentation():
    """Package dokumentasyonu oluşturma"""
    
    print("📚 Documentation Best Practices:")
    
    # README.md template
    readme_template = '''# Package Name

[![CI](https://github.com/username/package/workflows/CI/badge.svg)](https://github.com/username/package/actions)
[![Coverage](https://codecov.io/gh/username/package/branch/main/graph/badge.svg)](https://codecov.io/gh/username/package)
[![PyPI](https://img.shields.io/pypi/v/package-name.svg)](https://pypi.org/project/package-name/)

Package açıklaması ve ana özellikler.

## Installation

```bash
pip install package-name
```

## Quick Start

```python
from package_name import MainClass

# Basic usage
obj = MainClass()
result = obj.process()
```

## Features

- ✅ Feature 1
- ✅ Feature 2  
- ✅ Feature 3

## Documentation

Full documentation: https://package-name.readthedocs.io/

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)

## License

MIT License - see [LICENSE](LICENSE)
'''
    
    print("📄 README.md Template:")
    for i, line in enumerate(readme_template.strip().split('\n')[:15], 1):
        print(f"   {i:2d}: {line}")
    print("   ... (devamı)")
    
    # Sphinx documentation
    print(f"\n📖 Sphinx Documentation:")
    sphinx_commands = [
        "pip install sphinx sphinx-rtd-theme",
        "sphinx-quickstart docs",
        "# docs/conf.py düzenle",
        "sphinx-apidoc -o docs/source src/package_name",
        "cd docs && make html"
    ]
    
    for i, cmd in enumerate(sphinx_commands, 1):
        print(f"   {i}. {cmd}")
    
    # Docstring format
    print(f"\n📝 Docstring Format (Google Style):")
    docstring_example = '''def process_data(data, format_type="json", validate=True):
    """Process input data and return formatted result.
    
    Args:
        data: Input data to process (list, dict, or str)
        format_type: Output format ("json", "xml", "csv")
        validate: Whether to validate input data
    
    Returns:
        Processed and formatted data as string
        
    Raises:
        ValueError: If data format is not supported
        TypeError: If data type is invalid
        
    Examples:
        >>> process_data([1, 2, 3], "json")
        '[1, 2, 3]'
        
        >>> process_data({"name": "test"}, "xml")
        '<root><name>test</name></root>'
    """
    pass
'''
    
    for i, line in enumerate(docstring_example.strip().split('\n'), 1):
        print(f"   {i:2d}: {line}")

package_documentation()

# =============================================================================
# 7. PACKAGE SECURITY VE BEST PRACTICES
# =============================================================================

print("\n=== Package Security ve Best Practices ===")

def package_security():
    """Package güvenlik ve en iyi pratikler"""
    
    print("🔒 Package Security Checklist:")
    
    security_items = [
        "Dependency vulnerability scanning (pip-audit)",
        "Code quality checks (flake8, pylint)",
        "Type checking (mypy)",
        "Security linting (bandit)",
        "License compatibility check",
        "Secrets scanning (.env, API keys)",
        "SAST (Static Application Security Testing)",
        "Package signing (GPG)"
    ]
    
    for i, item in enumerate(security_items, 1):
        print(f"   {i}. ✅ {item}")
    
    # Security tools
    print(f"\n🛡️ Security Tools:")
    security_tools = {
        "pip-audit": "pip install pip-audit && pip-audit",
        "bandit": "pip install bandit && bandit -r src/",
        "safety": "pip install safety && safety check",
        "semgrep": "pip install semgrep && semgrep --config=auto src/",
    }
    
    for tool, command in security_tools.items():
        print(f"   • {tool}: {command}")
    
    # .gitignore template
    print(f"\n📝 .gitignore Template:")
    gitignore_content = '''# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# IDE
.vscode/
.idea/
*.swp
*.swo

# Testing
.coverage
.pytest_cache/
.tox/
htmlcov/

# Documentation
docs/_build/
'''
    
    for i, line in enumerate(gitignore_content.strip().split('\n')[:15], 1):
        print(f"   {i:2d}: {line}")
    print("   ... (devamı)")
    
    # Best practices summary
    print(f"\n🏆 Package Development Best Practices:")
    best_practices = [
        "Semantic versioning (SemVer) kullanın",
        "Changelog.md tutun (Keep a Changelog format)",
        "Code coverage %80+ hedefleyin",
        "Documentation'ı güncel tutun",
        "Breaking changes'i açık belirtin",
        "Backward compatibility'yi koruyun",
        "Performance benchmarks yapın",
        "Community guidelines oluşturun"
    ]
    
    for i, practice in enumerate(best_practices, 1):
        print(f"   {i}. {practice}")

package_security()

print("\n💡 Package Development İpuçları:")
print("✅ Küçük, odaklanmış package'lar oluşturun")
print("✅ Dependency'leri minimal tutun")
print("✅ API stability'yi koruyun")
print("✅ Comprehensive testing yapın")
print("✅ Clear documentation yazın")
print("✅ Community feedback'i dinleyin")
print("✅ Security best practices uygulayın")

print("\n🚀 İleri Seviye Konular:")
print("• Binary extensions (C/C++)")
print("• Package namespaces")
print("• Plugin systems")
print("• Packaging for different platforms")
print("• Performance optimization")

print("\n✅ Python package oluşturma öğrenildi!")
print("✅ Modern package tools öğrenildi!")
print("✅ CI/CD ve testing pipeline'ı öğrenildi!")
print("✅ Package security ve best practices öğrenildi!")