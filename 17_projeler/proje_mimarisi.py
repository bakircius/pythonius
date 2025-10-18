"""
Python Proje Mimarisi ve Yapısı - Comprehensive Guide
Large Scale Project Organization, Design Patterns, Clean Architecture

Bu dosyada büyük ölçekli Python projeleri için mimari patterns,
proje organizasyonu, dependency injection ve configuration management incelenecek.
"""

import os
import json
import logging
import asyncio
from pathlib import Path
from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any, Protocol, TypeVar, Generic
from dataclasses import dataclass, field
from contextlib import asynccontextmanager
from functools import lru_cache
import threading
from enum import Enum
import uuid
from datetime import datetime

# =============================================================================
# 1. PROJECT STRUCTURE PATTERNS
# =============================================================================

print("=== Project Structure Patterns ===")

class ProjectStructure:
    """Modern Python project structure example"""
    
    def __init__(self, project_name: str):
        self.project_name = project_name
        self.structure = {
            project_name: {
                "__init__.py": "",
                "api": {
                    "__init__.py": "",
                    "v1": {
                        "__init__.py": "",
                        "endpoints": {
                            "__init__.py": "",
                            "auth.py": "# Authentication endpoints",
                            "users.py": "# User management endpoints",
                            "products.py": "# Product endpoints"
                        },
                        "dependencies.py": "# FastAPI dependencies"
                    },
                    "middleware.py": "# Custom middleware"
                },
                "core": {
                    "__init__.py": "",
                    "config.py": "# Application configuration",
                    "security.py": "# Security utilities",
                    "database.py": "# Database connection",
                    "exceptions.py": "# Custom exceptions"
                },
                "services": {
                    "__init__.py": "",
                    "user_service.py": "# User business logic",
                    "product_service.py": "# Product business logic",
                    "email_service.py": "# Email service"
                },
                "repositories": {
                    "__init__.py": "",
                    "base.py": "# Base repository pattern",
                    "user_repository.py": "# User data access",
                    "product_repository.py": "# Product data access"
                },
                "models": {
                    "__init__.py": "",
                    "database": {
                        "__init__.py": "",
                        "user.py": "# SQLAlchemy User model",
                        "product.py": "# SQLAlchemy Product model"
                    },
                    "schemas": {
                        "__init__.py": "",
                        "user.py": "# Pydantic User schemas",
                        "product.py": "# Pydantic Product schemas"
                    }
                },
                "utils": {
                    "__init__.py": "",
                    "helpers.py": "# Utility functions",
                    "validators.py": "# Custom validators",
                    "decorators.py": "# Custom decorators"
                }
            },
            "tests": {
                "__init__.py": "",
                "unit": {
                    "__init__.py": "",
                    "test_services.py": "# Service unit tests",
                    "test_repositories.py": "# Repository tests"
                },
                "integration": {
                    "__init__.py": "",
                    "test_api.py": "# API integration tests"
                },
                "conftest.py": "# Pytest configuration"
            },
            "migrations": {
                "versions": {},
                "alembic.ini": "# Alembic configuration",
                "env.py": "# Migration environment"
            },
            "docker": {
                "Dockerfile": "# Main application Dockerfile",
                "docker-compose.yml": "# Development environment",
                "docker-compose.prod.yml": "# Production environment"
            },
            "scripts": {
                "start.py": "# Application startup script",
                "migrate.py": "# Database migration script",
                "seed.py": "# Database seeding script"
            },
            ".env.example": "# Environment variables template",
            ".gitignore": "# Git ignore rules",
            "pyproject.toml": "# Project configuration",
            "requirements.txt": "# Dependencies",
            "README.md": "# Project documentation"
        }
    
    def create_structure(self, base_path: str = "."):
        """Create project directory structure"""
        def create_recursive(structure: dict, current_path: Path):
            for name, content in structure.items():
                path = current_path / name
                
                if isinstance(content, dict):
                    path.mkdir(exist_ok=True)
                    create_recursive(content, path)
                else:
                    path.parent.mkdir(parents=True, exist_ok=True)
                    if not path.exists():
                        path.write_text(content)
        
        base = Path(base_path)
        create_recursive(self.structure, base)
        print(f"✅ Project structure created: {self.project_name}")
        return base / self.project_name
    
    def visualize_structure(self, indent: str = "") -> str:
        """Visualize project structure"""
        def format_recursive(structure: dict, level: int = 0) -> List[str]:
            lines = []
            items = list(structure.items())
            
            for i, (name, content) in enumerate(items):
                is_last = i == len(items) - 1
                prefix = "└── " if is_last else "├── "
                lines.append("│   " * level + prefix + name)
                
                if isinstance(content, dict) and content:
                    next_indent = "    " if is_last else "│   "
                    sub_lines = format_recursive(content, level + 1)
                    lines.extend(sub_lines)
            
            return lines
        
        lines = [self.project_name + "/"]
        lines.extend(format_recursive(self.structure[self.project_name]))
        return "\n".join(lines)

# Project structure demonstration
print("Modern Python project structure:")
project = ProjectStructure("ecommerce_api")
print(project.visualize_structure())

# =============================================================================
# 2. DEPENDENCY INJECTION CONTAINER
# =============================================================================

print("\n=== Dependency Injection Container ===")

T = TypeVar('T')

class Injectable(ABC):
    """Base class for injectable services"""
    pass

class ServiceLifetime(Enum):
    """Service lifetime enumeration"""
    SINGLETON = "singleton"
    TRANSIENT = "transient"
    SCOPED = "scoped"

@dataclass
class ServiceDescriptor:
    """Service registration descriptor"""
    service_type: type
    implementation: type
    lifetime: ServiceLifetime
    instance: Optional[Any] = None
    factory: Optional[callable] = None

class DIContainer:
    """Dependency Injection Container"""
    
    def __init__(self):
        self._services: Dict[type, ServiceDescriptor] = {}
        self._scoped_instances: Dict[str, Dict[type, Any]] = {}
        self._lock = threading.Lock()
    
    def register_singleton(self, service_type: type, implementation: type = None):
        """Register singleton service"""
        impl = implementation or service_type
        self._services[service_type] = ServiceDescriptor(
            service_type=service_type,
            implementation=impl,
            lifetime=ServiceLifetime.SINGLETON
        )
        print(f"📝 Registered singleton: {service_type.__name__}")
        return self
    
    def register_transient(self, service_type: type, implementation: type = None):
        """Register transient service"""
        impl = implementation or service_type
        self._services[service_type] = ServiceDescriptor(
            service_type=service_type,
            implementation=impl,
            lifetime=ServiceLifetime.TRANSIENT
        )
        print(f"📝 Registered transient: {service_type.__name__}")
        return self
    
    def register_scoped(self, service_type: type, implementation: type = None):
        """Register scoped service"""
        impl = implementation or service_type
        self._services[service_type] = ServiceDescriptor(
            service_type=service_type,
            implementation=impl,
            lifetime=ServiceLifetime.SCOPED
        )
        print(f"📝 Registered scoped: {service_type.__name__}")
        return self
    
    def register_factory(self, service_type: type, factory: callable):
        """Register factory function"""
        self._services[service_type] = ServiceDescriptor(
            service_type=service_type,
            implementation=None,
            lifetime=ServiceLifetime.TRANSIENT,
            factory=factory
        )
        print(f"📝 Registered factory: {service_type.__name__}")
        return self
    
    def resolve(self, service_type: type, scope_id: str = None) -> T:
        """Resolve service instance"""
        if service_type not in self._services:
            raise ValueError(f"Service {service_type.__name__} not registered")
        
        descriptor = self._services[service_type]
        
        # Factory resolution
        if descriptor.factory:
            return descriptor.factory(self)
        
        # Singleton resolution
        if descriptor.lifetime == ServiceLifetime.SINGLETON:
            if descriptor.instance is None:
                with self._lock:
                    if descriptor.instance is None:
                        descriptor.instance = self._create_instance(descriptor)
            return descriptor.instance
        
        # Scoped resolution
        if descriptor.lifetime == ServiceLifetime.SCOPED:
            if scope_id is None:
                raise ValueError("Scope ID required for scoped services")
            
            if scope_id not in self._scoped_instances:
                self._scoped_instances[scope_id] = {}
            
            if service_type not in self._scoped_instances[scope_id]:
                instance = self._create_instance(descriptor)
                self._scoped_instances[scope_id][service_type] = instance
            
            return self._scoped_instances[scope_id][service_type]
        
        # Transient resolution
        return self._create_instance(descriptor)
    
    def _create_instance(self, descriptor: ServiceDescriptor):
        """Create service instance with dependency injection"""
        implementation = descriptor.implementation
        
        # Get constructor parameters
        import inspect
        signature = inspect.signature(implementation.__init__)
        kwargs = {}
        
        for param_name, param in signature.parameters.items():
            if param_name == 'self':
                continue
            
            # Resolve dependencies
            if param.annotation != inspect.Parameter.empty:
                dependency = self.resolve(param.annotation)
                kwargs[param_name] = dependency
        
        return implementation(**kwargs)
    
    def create_scope(self) -> str:
        """Create new scope"""
        scope_id = str(uuid.uuid4())
        self._scoped_instances[scope_id] = {}
        return scope_id
    
    def dispose_scope(self, scope_id: str):
        """Dispose scope and cleanup instances"""
        if scope_id in self._scoped_instances:
            # Cleanup scoped instances if they have dispose method
            for instance in self._scoped_instances[scope_id].values():
                if hasattr(instance, 'dispose'):
                    instance.dispose()
            
            del self._scoped_instances[scope_id]
            print(f"🗑️  Disposed scope: {scope_id}")

# Example services for DI demonstration
class IUserRepository(ABC):
    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[dict]:
        pass

class IEmailService(ABC):
    @abstractmethod
    def send_email(self, to: str, subject: str, body: str) -> bool:
        pass

class UserRepository(Injectable, IUserRepository):
    """User repository implementation"""
    
    def __init__(self):
        self.users = {
            1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
            2: {"id": 2, "name": "Bob", "email": "bob@example.com"}
        }
        print("🔧 UserRepository created")
    
    def get_by_id(self, user_id: int) -> Optional[dict]:
        return self.users.get(user_id)

class EmailService(Injectable, IEmailService):
    """Email service implementation"""
    
    def __init__(self):
        self.sent_emails = []
        print("📧 EmailService created")
    
    def send_email(self, to: str, subject: str, body: str) -> bool:
        email = {
            "to": to,
            "subject": subject,
            "body": body,
            "sent_at": datetime.now()
        }
        self.sent_emails.append(email)
        print(f"📤 Email sent to: {to}")
        return True

class UserService(Injectable):
    """User service with dependencies"""
    
    def __init__(self, user_repository: IUserRepository, email_service: IEmailService):
        self.user_repository = user_repository
        self.email_service = email_service
        print("👤 UserService created with dependencies")
    
    def notify_user(self, user_id: int, message: str) -> bool:
        user = self.user_repository.get_by_id(user_id)
        if user:
            return self.email_service.send_email(
                user["email"],
                "Notification",
                message
            )
        return False
    
    def get_user(self, user_id: int) -> Optional[dict]:
        return self.user_repository.get_by_id(user_id)

# Dependency injection demonstration
print("Dependency injection container örnekleri:")

container = DIContainer()

# Register services with different lifetimes
container.register_singleton(IUserRepository, UserRepository)
container.register_transient(IEmailService, EmailService)
container.register_scoped(UserService)

# Resolve services
print("\n1. Service resolution:")
user_service1 = container.resolve(UserService, "scope1")
user_service2 = container.resolve(UserService, "scope1")  # Same scope
user_service3 = container.resolve(UserService, "scope2")  # Different scope

print(f"Same scope services equal: {user_service1 is user_service2}")
print(f"Different scope services equal: {user_service1 is user_service3}")

# Use services
user = user_service1.get_user(1)
print(f"User found: {user}")
user_service1.notify_user(1, "Welcome to our platform!")

# =============================================================================
# 3. CONFIGURATION MANAGEMENT
# =============================================================================

print("\n=== Configuration Management ===")

class ConfigSource(ABC):
    """Configuration source interface"""
    
    @abstractmethod
    def load(self) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    def get_priority(self) -> int:
        pass

class EnvironmentConfigSource(ConfigSource):
    """Environment variables configuration source"""
    
    def __init__(self, prefix: str = ""):
        self.prefix = prefix.upper()
    
    def load(self) -> Dict[str, Any]:
        config = {}
        for key, value in os.environ.items():
            if not self.prefix or key.startswith(self.prefix):
                # Convert environment variable to nested dict
                clean_key = key[len(self.prefix):] if self.prefix else key
                keys = clean_key.lower().split('_')
                
                current = config
                for k in keys[:-1]:
                    if k not in current:
                        current[k] = {}
                    current = current[k]
                
                # Try to convert to appropriate type
                try:
                    if value.lower() in ('true', 'false'):
                        current[keys[-1]] = value.lower() == 'true'
                    elif value.isdigit():
                        current[keys[-1]] = int(value)
                    elif '.' in value and value.replace('.', '').isdigit():
                        current[keys[-1]] = float(value)
                    else:
                        current[keys[-1]] = value
                except:
                    current[keys[-1]] = value
        
        return config
    
    def get_priority(self) -> int:
        return 100  # High priority

class JsonConfigSource(ConfigSource):
    """JSON file configuration source"""
    
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
    
    def load(self) -> Dict[str, Any]:
        if not self.file_path.exists():
            print(f"⚠️  Config file not found: {self.file_path}")
            return {}
        
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"❌ Error loading config file: {e}")
            return {}
    
    def get_priority(self) -> int:
        return 50  # Medium priority

class DefaultConfigSource(ConfigSource):
    """Default configuration values"""
    
    def __init__(self, defaults: Dict[str, Any]):
        self.defaults = defaults
    
    def load(self) -> Dict[str, Any]:
        return self.defaults.copy()
    
    def get_priority(self) -> int:
        return 1  # Lowest priority

class ConfigurationManager:
    """Configuration management system"""
    
    def __init__(self):
        self.sources: List[ConfigSource] = []
        self.config: Dict[str, Any] = {}
        self.change_callbacks: List[callable] = []
    
    def add_source(self, source: ConfigSource):
        """Add configuration source"""
        self.sources.append(source)
        self.sources.sort(key=lambda s: s.get_priority())
        print(f"📋 Added config source: {source.__class__.__name__}")
    
    def load_configuration(self):
        """Load configuration from all sources"""
        self.config = {}
        
        # Load from sources in priority order (lowest first)
        for source in self.sources:
            source_config = source.load()
            self._merge_config(self.config, source_config)
        
        print("⚙️  Configuration loaded")
        
        # Notify change callbacks
        for callback in self.change_callbacks:
            try:
                callback(self.config)
            except Exception as e:
                print(f"❌ Config change callback error: {e}")
    
    def _merge_config(self, target: dict, source: dict):
        """Merge configuration dictionaries"""
        for key, value in source.items():
            if key in target and isinstance(target[key], dict) and isinstance(value, dict):
                self._merge_config(target[key], value)
            else:
                target[key] = value
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value by key (supports dot notation)"""
        keys = key.split('.')
        current = self.config
        
        for k in keys:
            if isinstance(current, dict) and k in current:
                current = current[k]
            else:
                return default
        
        return current
    
    def get_section(self, section: str) -> Dict[str, Any]:
        """Get configuration section"""
        return self.get(section, {})
    
    def set(self, key: str, value: Any):
        """Set configuration value (runtime only)"""
        keys = key.split('.')
        current = self.config
        
        for k in keys[:-1]:
            if k not in current:
                current[k] = {}
            current = current[k]
        
        current[keys[-1]] = value
        
        # Notify callbacks
        for callback in self.change_callbacks:
            try:
                callback(self.config)
            except Exception as e:
                print(f"❌ Config change callback error: {e}")
    
    def on_change(self, callback: callable):
        """Register configuration change callback"""
        self.change_callbacks.append(callback)
    
    def validate_config(self, schema: Dict[str, Any]) -> List[str]:
        """Validate configuration against schema"""
        errors = []
        
        def validate_recursive(config_section: dict, schema_section: dict, path: str = ""):
            for key, expected_type in schema_section.items():
                current_path = f"{path}.{key}" if path else key
                
                if key not in config_section:
                    errors.append(f"Missing required key: {current_path}")
                    continue
                
                value = config_section[key]
                
                if isinstance(expected_type, dict):
                    if isinstance(value, dict):
                        validate_recursive(value, expected_type, current_path)
                    else:
                        errors.append(f"Expected dict at {current_path}, got {type(value).__name__}")
                elif not isinstance(value, expected_type):
                    errors.append(f"Expected {expected_type.__name__} at {current_path}, got {type(value).__name__}")
        
        validate_recursive(self.config, schema)
        return errors

# Configuration management demonstration
print("Configuration management örnekleri:")

# Create sample config files for testing
config_data = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "ecommerce"
    },
    "api": {
        "host": "0.0.0.0",
        "port": 8000,
        "debug": False
    },
    "redis": {
        "host": "localhost",
        "port": 6379
    }
}

# Write sample config (in real scenario, this would exist)
config_file = Path("app_config.json")
config_file.write_text(json.dumps(config_data, indent=2))

# Setup configuration manager
config_manager = ConfigurationManager()

# Add configuration sources
defaults = {
    "database": {"host": "localhost", "port": 5432},
    "api": {"host": "127.0.0.1", "port": 3000, "debug": True},
    "logging": {"level": "INFO"}
}

config_manager.add_source(DefaultConfigSource(defaults))
config_manager.add_source(JsonConfigSource("app_config.json"))
config_manager.add_source(EnvironmentConfigSource("MYAPP_"))

# Set some environment variables for testing
os.environ["MYAPP_API_PORT"] = "9000"
os.environ["MYAPP_DATABASE_PASSWORD"] = "secret123"
os.environ["MYAPP_API_DEBUG"] = "true"

# Load configuration
config_manager.load_configuration()

# Demonstrate configuration access
print(f"Database host: {config_manager.get('database.host')}")
print(f"API port: {config_manager.get('api.port')}")
print(f"Debug mode: {config_manager.get('api.debug')}")
print(f"Database password: {config_manager.get('database.password', 'not set')}")

# Configuration validation
schema = {
    "database": {
        "host": str,
        "port": int
    },
    "api": {
        "port": int,
        "debug": bool
    }
}

validation_errors = config_manager.validate_config(schema)
if validation_errors:
    print("⚠️  Configuration validation errors:")
    for error in validation_errors:
        print(f"  - {error}")
else:
    print("✅ Configuration validation passed")

# =============================================================================
# 4. LOGGING AND MONITORING
# =============================================================================

print("\n=== Logging and Monitoring ===")

import structlog
import time
from contextlib import contextmanager

class LogLevel(Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

@dataclass
class LogEntry:
    """Structured log entry"""
    timestamp: datetime
    level: LogLevel
    message: str
    logger_name: str
    context: Dict[str, Any] = field(default_factory=dict)
    correlation_id: Optional[str] = None
    user_id: Optional[str] = None

class LogProcessor:
    """Log processor interface"""
    
    def process(self, entry: LogEntry):
        pass

class ConsoleLogProcessor(LogProcessor):
    """Console log output processor"""
    
    def __init__(self, colored: bool = True):
        self.colored = colored
        self.colors = {
            LogLevel.DEBUG: "\033[36m",     # Cyan
            LogLevel.INFO: "\033[32m",      # Green
            LogLevel.WARNING: "\033[33m",   # Yellow
            LogLevel.ERROR: "\033[31m",     # Red
            LogLevel.CRITICAL: "\033[35m",  # Magenta
        }
        self.reset = "\033[0m"
    
    def process(self, entry: LogEntry):
        timestamp = entry.timestamp.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        
        if self.colored:
            color = self.colors.get(entry.level, "")
            level_str = f"{color}{entry.level.value:<8}{self.reset}"
        else:
            level_str = f"{entry.level.value:<8}"
        
        context_str = ""
        if entry.context:
            context_items = [f"{k}={v}" for k, v in entry.context.items()]
            context_str = f" [{', '.join(context_items)}]"
        
        correlation_str = f" [corr_id={entry.correlation_id}]" if entry.correlation_id else ""
        user_str = f" [user={entry.user_id}]" if entry.user_id else ""
        
        message = f"{timestamp} {level_str} {entry.logger_name}: {entry.message}{context_str}{correlation_str}{user_str}"
        print(message)

class FileLogProcessor(LogProcessor):
    """File log output processor"""
    
    def __init__(self, file_path: str, max_size: int = 10 * 1024 * 1024):
        self.file_path = Path(file_path)
        self.max_size = max_size
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
    
    def process(self, entry: LogEntry):
        # Rotate file if needed
        if self.file_path.exists() and self.file_path.stat().st_size > self.max_size:
            backup_path = self.file_path.with_suffix(f".{int(time.time())}.bak")
            self.file_path.rename(backup_path)
        
        log_data = {
            "timestamp": entry.timestamp.isoformat(),
            "level": entry.level.value,
            "logger": entry.logger_name,
            "message": entry.message,
            "context": entry.context,
            "correlation_id": entry.correlation_id,
            "user_id": entry.user_id
        }
        
        with open(self.file_path, 'a', encoding='utf-8') as f:
            f.write(json.dumps(log_data) + '\n')

class StructuredLogger:
    """Structured logger implementation"""
    
    def __init__(self, name: str):
        self.name = name
        self.processors: List[LogProcessor] = []
        self.context: Dict[str, Any] = {}
        self.correlation_id: Optional[str] = None
        self.user_id: Optional[str] = None
    
    def add_processor(self, processor: LogProcessor):
        """Add log processor"""
        self.processors.append(processor)
    
    def with_context(self, **kwargs) -> 'StructuredLogger':
        """Create logger with additional context"""
        new_logger = StructuredLogger(self.name)
        new_logger.processors = self.processors
        new_logger.context = {**self.context, **kwargs}
        new_logger.correlation_id = self.correlation_id
        new_logger.user_id = self.user_id
        return new_logger
    
    def with_correlation(self, correlation_id: str) -> 'StructuredLogger':
        """Create logger with correlation ID"""
        new_logger = StructuredLogger(self.name)
        new_logger.processors = self.processors
        new_logger.context = self.context.copy()
        new_logger.correlation_id = correlation_id
        new_logger.user_id = self.user_id
        return new_logger
    
    def with_user(self, user_id: str) -> 'StructuredLogger':
        """Create logger with user ID"""
        new_logger = StructuredLogger(self.name)
        new_logger.processors = self.processors
        new_logger.context = self.context.copy()
        new_logger.correlation_id = self.correlation_id
        new_logger.user_id = user_id
        return new_logger
    
    def _log(self, level: LogLevel, message: str, **kwargs):
        """Internal logging method"""
        entry = LogEntry(
            timestamp=datetime.now(),
            level=level,
            message=message,
            logger_name=self.name,
            context={**self.context, **kwargs},
            correlation_id=self.correlation_id,
            user_id=self.user_id
        )
        
        for processor in self.processors:
            try:
                processor.process(entry)
            except Exception as e:
                print(f"Log processor error: {e}")
    
    def debug(self, message: str, **kwargs):
        self._log(LogLevel.DEBUG, message, **kwargs)
    
    def info(self, message: str, **kwargs):
        self._log(LogLevel.INFO, message, **kwargs)
    
    def warning(self, message: str, **kwargs):
        self._log(LogLevel.WARNING, message, **kwargs)
    
    def error(self, message: str, **kwargs):
        self._log(LogLevel.ERROR, message, **kwargs)
    
    def critical(self, message: str, **kwargs):
        self._log(LogLevel.CRITICAL, message, **kwargs)

class MetricsCollector:
    """Application metrics collector"""
    
    def __init__(self):
        self.counters: Dict[str, int] = {}
        self.gauges: Dict[str, float] = {}
        self.histograms: Dict[str, List[float]] = {}
        self.timers: Dict[str, List[float]] = {}
        self._lock = threading.Lock()
    
    def increment(self, name: str, value: int = 1, tags: Dict[str, str] = None):
        """Increment counter metric"""
        with self._lock:
            key = self._make_key(name, tags)
            self.counters[key] = self.counters.get(key, 0) + value
    
    def set_gauge(self, name: str, value: float, tags: Dict[str, str] = None):
        """Set gauge metric value"""
        with self._lock:
            key = self._make_key(name, tags)
            self.gauges[key] = value
    
    def record_histogram(self, name: str, value: float, tags: Dict[str, str] = None):
        """Record histogram value"""
        with self._lock:
            key = self._make_key(name, tags)
            if key not in self.histograms:
                self.histograms[key] = []
            self.histograms[key].append(value)
    
    def record_timer(self, name: str, duration: float, tags: Dict[str, str] = None):
        """Record timer duration"""
        with self._lock:
            key = self._make_key(name, tags)
            if key not in self.timers:
                self.timers[key] = []
            self.timers[key].append(duration)
    
    @contextmanager
    def timer(self, name: str, tags: Dict[str, str] = None):
        """Timer context manager"""
        start_time = time.time()
        try:
            yield
        finally:
            duration = time.time() - start_time
            self.record_timer(name, duration, tags)
    
    def _make_key(self, name: str, tags: Dict[str, str] = None) -> str:
        """Create metric key with tags"""
        if not tags:
            return name
        
        tag_string = ",".join(f"{k}={v}" for k, v in sorted(tags.items()))
        return f"{name};{tag_string}"
    
    def get_metrics(self) -> Dict[str, Any]:
        """Get all collected metrics"""
        with self._lock:
            metrics = {
                "counters": self.counters.copy(),
                "gauges": self.gauges.copy(),
                "histograms": {},
                "timers": {}
            }
            
            # Calculate histogram statistics
            for key, values in self.histograms.items():
                if values:
                    metrics["histograms"][key] = {
                        "count": len(values),
                        "sum": sum(values),
                        "min": min(values),
                        "max": max(values),
                        "avg": sum(values) / len(values)
                    }
            
            # Calculate timer statistics
            for key, durations in self.timers.items():
                if durations:
                    metrics["timers"][key] = {
                        "count": len(durations),
                        "sum": sum(durations),
                        "min": min(durations),
                        "max": max(durations),
                        "avg": sum(durations) / len(durations)
                    }
            
            return metrics

# Logging and monitoring demonstration
print("Logging and monitoring örnekleri:")

# Setup structured logging
logger = StructuredLogger("ecommerce.api")
logger.add_processor(ConsoleLogProcessor(colored=True))
logger.add_processor(FileLogProcessor("logs/app.log"))

# Setup metrics
metrics = MetricsCollector()

# Simulate application activity
correlation_id = str(uuid.uuid4())
user_logger = logger.with_correlation(correlation_id).with_user("user123")

user_logger.info("User login attempt", email="user@example.com")
metrics.increment("login_attempts", tags={"status": "success"})

# Simulate API request processing
api_logger = user_logger.with_context(endpoint="/api/v1/products")

with metrics.timer("api_request_duration", tags={"endpoint": "/api/v1/products"}):
    api_logger.info("Processing request")
    time.sleep(0.1)  # Simulate processing
    
    # Simulate database query
    db_logger = api_logger.with_context(operation="select")
    with metrics.timer("database_query_duration", tags={"operation": "select"}):
        db_logger.debug("Executing database query", query="SELECT * FROM products WHERE active = true")
        time.sleep(0.05)  # Simulate DB query
    
    api_logger.info("Request completed", response_size=1024)

metrics.increment("api_requests", tags={"endpoint": "/api/v1/products", "status": "200"})
metrics.set_gauge("active_connections", 42)

# Show collected metrics
print("\nCollected metrics:")
all_metrics = metrics.get_metrics()
for metric_type, metric_data in all_metrics.items():
    if metric_data:
        print(f"\n{metric_type.upper()}:")
        for name, value in metric_data.items():
            print(f"  {name}: {value}")

# Cleanup test files
config_file.unlink(missing_ok=True)
Path("logs").rmdir() if Path("logs").exists() else None

print("\n" + "="*60)
print("PROJE MİMARİSİ VE YAPISI TAMAMLANDI")
print("="*60)

print("\nKonular Özeti:")
print("1. Modern Python project structure")
print("2. Dependency Injection Container")
print("3. Configuration Management System")
print("4. Structured Logging ve Monitoring")
print("5. Clean Architecture Principles")
print("6. Production-ready Patterns")

print("\nBir sonraki dosya: restful_api_gelistirme.py")