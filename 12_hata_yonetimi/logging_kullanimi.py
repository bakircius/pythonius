"""
Python Logging Kullanımı

Bu dosya Python'da logging sistemini kapsamlı olarak ele alır.
Logger konfigürasyonu, formatters, handlers, log levels,
strukturel logging ve production logging best practices.
"""

import logging
import logging.config
import logging.handlers
import json
import sys
import os
import time
from datetime import datetime
from pathlib import Path
import traceback
from typing import Dict, Any, Optional
import threading
import queue

# =============================================================================
# 1. TEMEL LOGGİNG KURULUMU
# =============================================================================

print("=== Temel Logging Kurulumu ===")

def temel_logging_ornegi():
    """Temel logging kullanımı"""
    
    # Basit logging
    print("--- Basit Logging ---")
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Logger oluştur
    logger = logging.getLogger(__name__)
    
    # Farklı seviyeler
    logger.debug("Bu bir debug mesajı")
    logger.info("Bu bir info mesajı")
    logger.warning("Bu bir warning mesajı")
    logger.error("Bu bir error mesajı")
    logger.critical("Bu bir critical mesajı")
    
    print(f"\nLogger ismi: {logger.name}")
    print(f"Logger seviyesi: {logger.level}")
    print(f"Effective seviye: {logger.getEffectiveLevel()}")

temel_logging_ornegi()

# =============================================================================
# 2. LOG LEVELS VE CONFIGURATION
# =============================================================================

print("\n=== Log Levels ve Configuration ===")

def log_levels_ornegi():
    """Log levels detayları"""
    
    print("📊 Log Levels:")
    print(f"CRITICAL: {logging.CRITICAL}")
    print(f"ERROR: {logging.ERROR}")
    print(f"WARNING: {logging.WARNING}")
    print(f"INFO: {logging.INFO}")
    print(f"DEBUG: {logging.DEBUG}")
    
    # Custom logger
    custom_logger = logging.getLogger('custom_app')
    custom_logger.setLevel(logging.INFO)
    
    # Handler oluştur
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s | %(name)s | %(levelname)-8s | %(message)s'
    )
    handler.setFormatter(formatter)
    custom_logger.addHandler(handler)
    
    # Test mesajları
    custom_logger.debug("Debug mesajı (görünmeyecek)")
    custom_logger.info("Info mesajı")
    custom_logger.warning("Warning mesajı")
    custom_logger.error("Error mesajı")
    
    # Seviye değiştir
    print("\n--- Seviye DEBUG'a çevrildi ---")
    custom_logger.setLevel(logging.DEBUG)
    custom_logger.debug("Şimdi debug mesajı görünüyor")

log_levels_ornegi()

# =============================================================================
# 3. FORMATTERS VE HANDLERS
# =============================================================================

print("\n=== Formatters ve Handlers ===")

def formatters_handlers_ornegi():
    """Formatters ve handlers örnekleri"""
    
    # Temizlik için handlers'ları temizle
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    
    # Logger oluştur
    logger = logging.getLogger('format_test')
    logger.setLevel(logging.DEBUG)
    
    # Farklı formatters
    formatters = {
        'basit': logging.Formatter('%(levelname)s: %(message)s'),
        'detayli': logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
        ),
        'json_benzeri': logging.Formatter(
            '{"time": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}'
        )
    }
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatters['detayli'])
    logger.addHandler(console_handler)
    
    # Dosya handler
    file_handler = logging.FileHandler('app.log', encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatters['json_benzeri'])
    logger.addHandler(file_handler)
    
    # Test mesajları
    logger.debug("Debug mesajı (sadece dosyaya)")
    logger.info("Info mesajı (hem console hem dosya)")
    logger.warning("Warning mesajı")
    logger.error("Error mesajı")
    
    print("\n📁 Log dosyası oluşturuldu: app.log")
    
    # Dosyayı oku ve göster
    try:
        with open('app.log', 'r', encoding='utf-8') as f:
            print("Dosya içeriği:")
            print(f.read())
    except:
        pass

formatters_handlers_ornegi()

# =============================================================================
# 4. GELİŞMİŞ HANDLER TÜRLER
# =============================================================================

print("\n=== Gelişmiş Handler Türleri ===")

def gelismis_handlers_ornegi():
    """Gelişmiş handler türleri"""
    
    logger = logging.getLogger('advanced_handlers')
    logger.setLevel(logging.DEBUG)
    
    # Rotating file handler
    print("--- Rotating File Handler ---")
    rotating_handler = logging.handlers.RotatingFileHandler(
        'rotating.log',
        maxBytes=1024,  # 1KB (test için küçük)
        backupCount=3,
        encoding='utf-8'
    )
    rotating_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
    ))
    logger.addHandler(rotating_handler)
    
    # Test için çok mesaj yaz
    for i in range(10):
        logger.info(f"Bu rotating log mesajı {i+1}")
    
    # Time-based rotating handler
    print("\n--- Time-based Rotating Handler ---")
    time_handler = logging.handlers.TimedRotatingFileHandler(
        'timed.log',
        when='S',  # Her saniye (test için)
        interval=1,
        backupCount=3,
        encoding='utf-8'
    )
    time_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(message)s'
    ))
    
    # Memory handler
    print("\n--- Memory Handler ---")
    memory_handler = logging.handlers.MemoryHandler(
        capacity=5,  # 5 mesaj buffer'la
        target=console_handler if 'console_handler' in locals() else None
    )
    
    # SMTP handler (simülasyon)
    print("\n--- SMTP Handler (Simülasyon) ---")
    print("SMTP Handler e-mail göndermek için kullanılır")
    print("Örnek: SMTPHandler('localhost', 'from@domain.com', ['to@domain.com'], 'Error')")
    
    # Syslog handler (Unix/Linux)
    if sys.platform != 'win32':
        print("\n--- Syslog Handler ---")
        try:
            syslog_handler = logging.handlers.SysLogHandler(address='/dev/log')
            syslog_handler.setFormatter(logging.Formatter(
                'Python: %(name)s - %(levelname)s - %(message)s'
            ))
            logger.addHandler(syslog_handler)
            logger.info("Syslog test mesajı")
            print("Syslog mesajı gönderildi")
        except:
            print("Syslog kullanılamıyor")

gelismis_handlers_ornegi()

# =============================================================================
# 5. STRUCTURED LOGGING
# =============================================================================

print("\n=== Structured Logging ===")

class JSONFormatter(logging.Formatter):
    """JSON formatında log formatter"""
    
    def format(self, record):
        log_entry = {
            'timestamp': datetime.fromtimestamp(record.created).isoformat(),
            'level': record.levelname,
            'logger': record.name,
            'message': record.getMessage(),
            'module': record.module,
            'function': record.funcName,
            'line': record.lineno,
        }
        
        # Extra alanları ekle
        if hasattr(record, 'user_id'):
            log_entry['user_id'] = record.user_id
        if hasattr(record, 'request_id'):
            log_entry['request_id'] = record.request_id
        if hasattr(record, 'extra_data'):
            log_entry['extra_data'] = record.extra_data
        
        # Exception bilgisi
        if record.exc_info:
            log_entry['exception'] = {
                'type': record.exc_info[0].__name__,
                'message': str(record.exc_info[1]),
                'traceback': traceback.format_exception(*record.exc_info)
            }
        
        return json.dumps(log_entry, ensure_ascii=False)

def structured_logging_ornegi():
    """Structured logging örneği"""
    
    # JSON logger setup
    json_logger = logging.getLogger('json_app')
    json_logger.setLevel(logging.INFO)
    
    # JSON handler
    json_handler = logging.StreamHandler()
    json_handler.setFormatter(JSONFormatter())
    json_logger.addHandler(json_handler)
    
    # Basit mesaj
    json_logger.info("Uygulama başladı")
    
    # Extra bilgilerle
    json_logger.info(
        "Kullanıcı giriş yaptı",
        extra={
            'user_id': 12345,
            'request_id': 'req-abc-123',
            'extra_data': {
                'ip': '192.168.1.1',
                'user_agent': 'Mozilla/5.0...'
            }
        }
    )
    
    # Exception ile
    try:
        result = 1 / 0
    except Exception as e:
        json_logger.error(
            "Matematik hatası oluştu",
            exc_info=True,
            extra={'user_id': 12345, 'operation': 'division'}
        )

structured_logging_ornegi()

# =============================================================================
# 6. CONTEXT VE THREAD-SAFE LOGGING
# =============================================================================

print("\n=== Context ve Thread-Safe Logging ===")

class ContextFilter(logging.Filter):
    """Context bilgilerini ekleyen filter"""
    
    def __init__(self):
        super().__init__()
        self.context = threading.local()
    
    def set_context(self, **kwargs):
        """Context bilgilerini ayarla"""
        for key, value in kwargs.items():
            setattr(self.context, key, value)
    
    def clear_context(self):
        """Context'i temizle"""
        self.context = threading.local()
    
    def filter(self, record):
        """Log record'a context bilgilerini ekle"""
        # Context bilgilerini record'a ekle
        for key, value in self.context.__dict__.items():
            setattr(record, key, value)
        return True

def context_logging_ornegi():
    """Context-aware logging örneği"""
    
    # Context logger setup
    context_logger = logging.getLogger('context_app')
    context_logger.setLevel(logging.INFO)
    
    # Context filter
    context_filter = ContextFilter()
    
    # Handler with context
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(
        '%(asctime)s | %(request_id)s | %(user_id)s | %(levelname)s | %(message)s'
    ))
    handler.addFilter(context_filter)
    context_logger.addHandler(handler)
    
    # Context ayarla
    context_filter.set_context(
        request_id='req-123',
        user_id='user-456'
    )
    
    context_logger.info("Request başladı")
    context_logger.info("Veritabanı sorgusu")
    context_logger.info("Response gönderildi")
    
    # Context değiştir
    context_filter.set_context(
        request_id='req-789',
        user_id='user-101'
    )
    
    context_logger.info("Yeni request başladı")

context_logging_ornegi()

# =============================================================================
# 7. ASYNC VE QUEUE-BASED LOGGING
# =============================================================================

print("\n=== Queue-Based Logging ===")

def queue_logging_ornegi():
    """Queue-based logging örneği"""
    
    # Log queue oluştur
    log_queue = queue.Queue()
    
    # Queue handler
    queue_handler = logging.handlers.QueueHandler(log_queue)
    
    # Queue listener
    file_handler = logging.FileHandler('queue.log', encoding='utf-8')
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    ))
    
    queue_listener = logging.handlers.QueueListener(
        log_queue, file_handler
    )
    
    # Logger setup
    queue_logger = logging.getLogger('queue_app')
    queue_logger.addHandler(queue_handler)
    queue_logger.setLevel(logging.INFO)
    
    # Listener'ı başlat
    queue_listener.start()
    
    try:
        # Test mesajları
        for i in range(5):
            queue_logger.info(f"Queue mesajı {i+1}")
        
        print("Queue-based log mesajları gönderildi")
        
        # Queue'yu işle
        time.sleep(0.1)  # Listener'ın işlemesi için bekle
        
    finally:
        # Temizlik
        queue_listener.stop()

queue_logging_ornegi()

# =============================================================================
# 8. CONFIGURATION FİLE İLE SETUP
# =============================================================================

print("\n=== Configuration File ile Setup ===")

def config_file_logging():
    """Configuration file ile logging setup"""
    
    # YAML-style config (dict olarak)
    LOGGING_CONFIG = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
            },
            'detailed': {
                'format': '%(asctime)s [%(levelname)s] %(name)s %(filename)s:%(lineno)d: %(message)s'
            },
            'json': {
                'class': '__main__.JSONFormatter'
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'INFO',
                'formatter': 'standard',
                'stream': 'ext://sys.stdout'
            },
            'file': {
                'class': 'logging.FileHandler',
                'level': 'DEBUG',
                'formatter': 'detailed',
                'filename': 'config_app.log',
                'encoding': 'utf-8'
            },
            'rotating': {
                'class': 'logging.handlers.RotatingFileHandler',
                'level': 'INFO',
                'formatter': 'standard',
                'filename': 'rotating_config.log',
                'maxBytes': 1024,
                'backupCount': 3,
                'encoding': 'utf-8'
            }
        },
        'loggers': {
            'app': {
                'level': 'DEBUG',
                'handlers': ['console', 'file'],
                'propagate': False
            },
            'app.database': {
                'level': 'INFO',
                'handlers': ['file', 'rotating'],
                'propagate': False
            }
        },
        'root': {
            'level': 'WARNING',
            'handlers': ['console']
        }
    }
    
    # Configuration'ı uygula
    logging.config.dictConfig(LOGGING_CONFIG)
    
    # Test loggers
    app_logger = logging.getLogger('app')
    db_logger = logging.getLogger('app.database')
    
    app_logger.debug("App debug mesajı")
    app_logger.info("App info mesajı")
    app_logger.warning("App warning mesajı")
    
    db_logger.info("Database bağlantısı kuruldu")
    db_logger.warning("Slow query tespit edildi")
    
    print("Configuration-based logging test edildi")

config_file_logging()

# =============================================================================
# 9. PRODUCTİON LOGGING BEST PRACTICES
# =============================================================================

print("\n=== Production Logging Best Practices ===")

class ProductionLogger:
    """Production-ready logger sınıfı"""
    
    def __init__(self, app_name: str, log_dir: str = "logs"):
        self.app_name = app_name
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)
        
        self.setup_loggers()
    
    def setup_loggers(self):
        """Production logger'ları kur"""
        
        # Formatters
        self.formatters = {
            'json': JSONFormatter(),
            'human': logging.Formatter(
                '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s'
            ),
            'detailed': logging.Formatter(
                '%(asctime)s | %(levelname)-8s | %(name)s | '
                '%(filename)s:%(lineno)d | %(funcName)s | %(message)s'
            )
        }
        
        # Handlers
        self.handlers = {}
        
        # Console handler (development)
        if os.getenv('ENVIRONMENT', 'development') == 'development':
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatters['human'])
            console_handler.setLevel(logging.INFO)
            self.handlers['console'] = console_handler
        
        # Application log
        app_handler = logging.handlers.RotatingFileHandler(
            self.log_dir / f'{self.app_name}.log',
            maxBytes=10*1024*1024,  # 10MB
            backupCount=10,
            encoding='utf-8'
        )
        app_handler.setFormatter(self.formatters['json'])
        app_handler.setLevel(logging.INFO)
        self.handlers['app'] = app_handler
        
        # Error log
        error_handler = logging.handlers.RotatingFileHandler(
            self.log_dir / f'{self.app_name}_error.log',
            maxBytes=10*1024*1024,
            backupCount=10,
            encoding='utf-8'
        )
        error_handler.setFormatter(self.formatters['detailed'])
        error_handler.setLevel(logging.ERROR)
        self.handlers['error'] = error_handler
        
        # Access log
        access_handler = logging.handlers.TimedRotatingFileHandler(
            self.log_dir / f'{self.app_name}_access.log',
            when='midnight',
            interval=1,
            backupCount=30,
            encoding='utf-8'
        )
        access_handler.setFormatter(self.formatters['json'])
        self.handlers['access'] = access_handler
    
    def get_logger(self, name: str, level: int = logging.INFO) -> logging.Logger:
        """Logger al"""
        logger = logging.getLogger(f'{self.app_name}.{name}')
        logger.setLevel(level)
        
        # Handlers ekle
        for handler in self.handlers.values():
            if handler not in logger.handlers:
                logger.addHandler(handler)
        
        return logger
    
    def get_access_logger(self) -> logging.Logger:
        """Access logger al"""
        logger = logging.getLogger(f'{self.app_name}.access')
        logger.setLevel(logging.INFO)
        logger.addHandler(self.handlers['access'])
        return logger

def production_logging_ornegi():
    """Production logging örneği"""
    
    # Production logger setup
    prod_logger_manager = ProductionLogger('myapp')
    
    # Farklı logger'lar
    app_logger = prod_logger_manager.get_logger('main')
    db_logger = prod_logger_manager.get_logger('database')
    api_logger = prod_logger_manager.get_logger('api')
    access_logger = prod_logger_manager.get_access_logger()
    
    # Test mesajları
    app_logger.info("Uygulama başlatıldı")
    
    db_logger.info("Veritabanı bağlantısı kuruldu")
    db_logger.warning("Slow query: SELECT * FROM users")
    
    api_logger.info("API endpoint çağrıldı")
    api_logger.error("Authentication başarısız")
    
    # Access log
    access_logger.info("API request", extra={
        'method': 'GET',
        'path': '/api/users',
        'status_code': 200,
        'response_time': 0.15,
        'user_id': 12345
    })
    
    print("Production logging örnekleri oluşturuldu")

production_logging_ornegi()

# =============================================================================
# 10. MONITORING VE ALERTING
# =============================================================================

print("\n=== Monitoring ve Alerting ===")

class LogMonitor:
    """Log monitoring sınıfı"""
    
    def __init__(self):
        self.error_count = 0
        self.warning_count = 0
        self.start_time = time.time()
    
    def check_log_health(self, log_file: str) -> Dict[str, Any]:
        """Log dosyası sağlığını kontrol et"""
        health_report = {
            'file': log_file,
            'exists': False,
            'size_mb': 0,
            'last_modified': None,
            'error_rate': 0,
            'warning_rate': 0
        }
        
        try:
            path = Path(log_file)
            if path.exists():
                health_report['exists'] = True
                health_report['size_mb'] = path.stat().st_size / (1024 * 1024)
                health_report['last_modified'] = datetime.fromtimestamp(
                    path.stat().st_mtime
                ).isoformat()
                
                # Son 100 satırı analiz et
                with open(path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()[-100:]
                
                error_lines = [l for l in lines if 'ERROR' in l or 'CRITICAL' in l]
                warning_lines = [l for l in lines if 'WARNING' in l]
                
                health_report['error_rate'] = len(error_lines) / len(lines) if lines else 0
                health_report['warning_rate'] = len(warning_lines) / len(lines) if lines else 0
        
        except Exception as e:
            health_report['error'] = str(e)
        
        return health_report

def monitoring_ornegi():
    """Log monitoring örneği"""
    
    monitor = LogMonitor()
    
    # Bazı log dosyalarını kontrol et
    log_files = ['app.log', 'config_app.log', 'queue.log']
    
    for log_file in log_files:
        health = monitor.check_log_health(log_file)
        print(f"\n📊 {log_file} sağlık raporu:")
        
        if health['exists']:
            print(f"   ✅ Dosya var")
            print(f"   📏 Boyut: {health['size_mb']:.2f} MB")
            print(f"   🕒 Son değişiklik: {health['last_modified']}")
            print(f"   ⚠️  Warning oranı: {health['warning_rate']:.1%}")
            print(f"   ❌ Error oranı: {health['error_rate']:.1%}")
            
            # Alert kontrolleri
            if health['error_rate'] > 0.1:  # %10'dan fazla error
                print("   🚨 ALERT: Yüksek error oranı!")
            
            if health['size_mb'] > 100:  # 100MB'dan büyük
                print("   🚨 ALERT: Log dosyası çok büyük!")
        else:
            print(f"   ❌ Dosya bulunamadı")

monitoring_ornegi()

print("\n💡 Logging Best Practices:")
print("✅ Structured logging (JSON) kullanın")
print("✅ Log levels'ı doğru kullanın")
print("✅ Sensitive bilgileri loglamayın")
print("✅ Context bilgilerini ekleyin")
print("✅ Log rotation kullanın")
print("✅ Monitoring ve alerting kurun")
print("✅ Performance'ı unutmayın")
print("✅ Thread-safe logging kullanın")

print("\n🛠️  Production Logging Checklist:")
print("• JSON formatında structured logs")
print("• Request ID tracking")
print("• Error aggregation")
print("• Log shipping (ELK, Fluentd)")
print("• Metrics ve alerts")
print("• Security logging")
print("• Performance profiling")

print("\n✅ Python logging sistemi öğrenildi!")
print("✅ Advanced handlers ve formatters öğrenildi!")
print("✅ Production logging best practices öğrenildi!")
print("✅ Monitoring ve alerting teknikleri öğrenildi!")