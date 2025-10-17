"""
Python Context Manager'lar - Comprehensive Guide

Bu dosyada context manager'ların derinlemesine incelemesi, custom context manager'lar,
contextlib modülü kullanımı ve pratik uygulamalar bulacaksınız.
"""

import contextlib
import tempfile
import os
import sqlite3
import threading
import time
from datetime import datetime
import logging

# =============================================================================
# 1. TEMEL CONTEXT MANAGER KAVRAMI
# =============================================================================

print("=== Context Manager Nedir? ===")
print("""
Context Manager, Python'da 'with' statement ile kullanılan bir protokoldür.
Kaynakların (dosya, veritabanı bağlantısı, network socket vb.) otomatik olarak
açılması ve kapatılması için kullanılır.

İki özel metod içerir:
- __enter__(): Kaynak açılırken çalışır
- __exit__(): Kaynak kapatılırken çalışır (hata olsa da olmasa da)
""")

# Temel dosya context manager örneği
print("Dosya context manager örneği:")
with open('ornek_dosya.txt', 'w', encoding='utf-8') as file:
    file.write('Context manager ile dosya yazma')
    print("Dosya açık ve yazılabilir")
print("Dosya otomatik olarak kapatıldı")

# =============================================================================
# 2. CUSTOM CONTEXT MANAGER CLASS
# =============================================================================

class FileManager:
    """Custom file context manager"""
    
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
        print(f"FileManager oluşturuldu: {filename} ({mode})")
    
    def __enter__(self):
        print(f"Dosya açılıyor: {self.filename}")
        self.file = open(self.filename, self.mode, encoding='utf-8')
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Dosya kapatılıyor: {self.filename}")
        if self.file:
            self.file.close()
        
        # Exception handling
        if exc_type is not None:
            print(f"Hata oluştu: {exc_type.__name__}: {exc_value}")
            return False  # Exception'ı yeniden raise et
        
        print("İşlem başarıyla tamamlandı")
        return True

class TimedOperation:
    """İşlem süresini ölçen context manager"""
    
    def __init__(self, operation_name="İşlem"):
        self.operation_name = operation_name
        self.start_time = None
    
    def __enter__(self):
        print(f"{self.operation_name} başladı...")
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.time()
        duration = end_time - self.start_time
        
        if exc_type is None:
            print(f"{self.operation_name} tamamlandı: {duration:.4f} saniye")
        else:
            print(f"{self.operation_name} hatayla sonlandı: {duration:.4f} saniye")
            print(f"Hata: {exc_type.__name__}: {exc_value}")
        
        return False  # Exception'ı suppress etme

print("\n=== Custom Context Manager Class ===")

# FileManager kullanımı
with FileManager('test_custom.txt', 'w') as f:
    f.write('Custom context manager ile yazım')

# TimedOperation kullanımı  
with TimedOperation("Veri işleme"):
    time.sleep(0.1)
    result = sum(range(1000000))
    print(f"Hesaplama sonucu: {result}")

# Hata durumunda TimedOperation
print("\nHata durumunda:")
try:
    with TimedOperation("Hatalı işlem"):
        time.sleep(0.05)
        raise ValueError("Örnek hata")
except ValueError as e:
    print(f"Yakalanan hata: {e}")

# =============================================================================
# 3. CONTEXTLİB İLE CONTEXT MANAGER
# =============================================================================

@contextlib.contextmanager
def simple_context():
    """contextlib.contextmanager decorator ile basit context manager"""
    print("Context başlatılıyor...")
    try:
        yield "Context içinde değer"
    finally:
        print("Context temizleniyor...")

@contextlib.contextmanager
def temporary_directory():
    """Geçici dizin oluşturan context manager"""
    temp_dir = tempfile.mkdtemp()
    print(f"Geçici dizin oluşturuldu: {temp_dir}")
    
    try:
        yield temp_dir
    finally:
        # Geçici dizini temizle
        import shutil
        shutil.rmtree(temp_dir)
        print(f"Geçici dizin temizlendi: {temp_dir}")

@contextlib.contextmanager
def database_transaction(db_path):
    """Veritabanı transaction context manager"""
    conn = sqlite3.connect(db_path)
    print("Veritabanı bağlantısı açıldı")
    
    try:
        conn.execute("BEGIN")
        print("Transaction başlatıldı")
        yield conn
        conn.commit()
        print("Transaction commit edildi")
    except Exception as e:
        conn.rollback()
        print(f"Transaction rollback edildi: {e}")
        raise
    finally:
        conn.close()
        print("Veritabanı bağlantısı kapatıldı")

print("\n=== contextlib ile Context Manager ===")

# Basit context manager
with simple_context() as value:
    print(f"Context içindeki değer: {value}")

# Geçici dizin context manager
with temporary_directory() as temp_dir:
    # Geçici dosya oluştur
    temp_file = os.path.join(temp_dir, 'temp_file.txt')
    with open(temp_file, 'w') as f:
        f.write('Geçici dosya içeriği')
    print(f"Geçici dosya oluşturuldu: {temp_file}")

# Veritabanı transaction
db_file = 'test.db'
with database_transaction(db_file) as conn:
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT
        )
    ''')
    conn.execute("INSERT INTO users (name, email) VALUES (?, ?)", 
                ("Ali", "ali@example.com"))

# =============================================================================
# 4. RESOURCE MANAGEMENT CONTEXT MANAGER'LAR
# =============================================================================

class LockManager:
    """Thread lock context manager"""
    
    def __init__(self, lock, timeout=10):
        self.lock = lock
        self.timeout = timeout
        self.acquired = False
    
    def __enter__(self):
        print(f"Lock alınmaya çalışılıyor (timeout: {self.timeout}s)...")
        self.acquired = self.lock.acquire(timeout=self.timeout)
        
        if not self.acquired:
            raise TimeoutError(f"Lock {self.timeout} saniyede alınamadı")
        
        print("Lock başarıyla alındı")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.acquired:
            self.lock.release()
            print("Lock serbest bırakıldı")

class MemoryMonitor:
    """Bellek kullanımını izleyen context manager"""
    
    def __init__(self):
        self.initial_memory = 0
        self.final_memory = 0
    
    def _get_memory_usage(self):
        """Mevcut bellek kullanımını al"""
        try:
            import psutil
            process = psutil.Process(os.getpid())
            return process.memory_info().rss / 1024 / 1024  # MB
        except ImportError:
            return 0  # psutil yoksa 0 döndür
    
    def __enter__(self):
        self.initial_memory = self._get_memory_usage()
        print(f"Başlangıç bellek kullanımı: {self.initial_memory:.2f} MB")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.final_memory = self._get_memory_usage()
        memory_diff = self.final_memory - self.initial_memory
        print(f"Son bellek kullanımı: {self.final_memory:.2f} MB")
        print(f"Bellek farkı: {memory_diff:+.2f} MB")

class LoggingContext:
    """Loglama için context manager"""
    
    def __init__(self, logger_name, level=logging.INFO):
        self.logger = logging.getLogger(logger_name)
        self.level = level
        self.start_time = None
    
    def __enter__(self):
        self.start_time = datetime.now()
        self.logger.log(self.level, f"İşlem başladı: {self.start_time}")
        return self.logger
    
    def __exit__(self, exc_type, exc_value, traceback):
        end_time = datetime.now()
        duration = (end_time - self.start_time).total_seconds()
        
        if exc_type is None:
            self.logger.log(self.level, f"İşlem tamamlandı: {duration:.3f}s")
        else:
            self.logger.error(f"İşlem hatayla sonlandı: {duration:.3f}s - {exc_value}")

print("\n=== Resource Management Context Manager'lar ===")

# Logging yapılandırması
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(message)s')

# Lock manager örneği
lock = threading.Lock()

def worker_function(worker_id, lock):
    """Worker fonksiyonu"""
    with LockManager(lock, timeout=5):
        print(f"Worker {worker_id} critical section'da çalışıyor...")
        time.sleep(1)
        print(f"Worker {worker_id} işini tamamladı")

# İki thread aynı anda lock almaya çalışsın
import threading
thread1 = threading.Thread(target=worker_function, args=(1, lock))
thread2 = threading.Thread(target=worker_function, args=(2, lock))

thread1.start()
time.sleep(0.1)  # İkinci thread biraz geciksin
thread2.start()

thread1.join()
thread2.join()

# Memory monitor örneği
print("\nBellek monitörü:")
with MemoryMonitor():
    # Bellek kullanan işlem
    big_list = [i for i in range(100000)]
    print(f"Büyük liste oluşturuldu: {len(big_list)} eleman")
    del big_list

# Logging context örneği
print("\nLogging context:")
with LoggingContext("my_app.database") as logger:
    logger.info("Veritabanı işlemi başlatılıyor")
    time.sleep(0.2)
    logger.info("Veri sorgulanıyor")
    time.sleep(0.1)
    logger.info("İşlem tamamlandı")

# =============================================================================
# 5. NESTED CONTEXT MANAGER'LAR
# =============================================================================

@contextlib.contextmanager
def multiple_files(*filenames):
    """Birden fazla dosyayı açan context manager"""
    files = []
    try:
        for filename in filenames:
            file = open(filename, 'w', encoding='utf-8')
            files.append(file)
            print(f"Dosya açıldı: {filename}")
        yield files
    finally:
        for file in files:
            file.close()
            print(f"Dosya kapatıldı: {file.name}")

class ConnectionPool:
    """Basit connection pool context manager"""
    
    def __init__(self, max_connections=5):
        self.max_connections = max_connections
        self.connections = []
        self.active_connections = 0
    
    def __enter__(self):
        if self.active_connections >= self.max_connections:
            raise Exception("Connection pool dolu")
        
        connection_id = f"conn_{self.active_connections + 1}"
        self.connections.append(connection_id)
        self.active_connections += 1
        print(f"Connection alındı: {connection_id} ({self.active_connections}/{self.max_connections})")
        return connection_id
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.connections:
            connection = self.connections.pop()
            self.active_connections -= 1
            print(f"Connection iade edildi: {connection} ({self.active_connections}/{self.max_connections})")

print("\n=== Nested Context Manager'lar ===")

# Çoklu dosya context manager
with multiple_files('file1.txt', 'file2.txt', 'file3.txt') as files:
    for i, file in enumerate(files):
        file.write(f'Dosya {i+1} içeriği')

# Connection pool kullanımı
pool = ConnectionPool(max_connections=2)

with pool as conn1:
    print(f"Connection 1 kullanılıyor: {conn1}")
    
    with pool as conn2:
        print(f"Connection 2 kullanılıyor: {conn2}")
        
        # Üçüncü connection deneyelim (hata vermeli)
        try:
            with pool as conn3:
                print(f"Connection 3: {conn3}")
        except Exception as e:
            print(f"Beklenen hata: {e}")

# =============================================================================
# 6. CONTEXTLIB UTILITIES
# =============================================================================

print("\n=== contextlib Utilities ===")

# contextlib.suppress - belirli hataları yoksay
print("contextlib.suppress örneği:")
with contextlib.suppress(FileNotFoundError):
    with open('olmayan_dosya.txt', 'r') as f:
        content = f.read()
print("FileNotFoundError yoksayıldı")

# contextlib.redirect_stdout - çıktıyı yönlendir
print("\ncontextlib.redirect_stdout örneği:")
from io import StringIO

output_buffer = StringIO()
with contextlib.redirect_stdout(output_buffer):
    print("Bu çıktı buffer'a gidecek")
    print("Bu da buffer'a gidecek")

captured_output = output_buffer.getvalue()
print(f"Yakalanan çıktı: '{captured_output.strip()}'")

# contextlib.closing - close() metodunu otomatik çağır
print("\ncontextlib.closing örneği:")
class CustomResource:
    def __init__(self, name):
        self.name = name
        print(f"Resource oluşturuldu: {name}")
    
    def close(self):
        print(f"Resource kapatıldı: {self.name}")
    
    def do_work(self):
        return f"İş yapılıyor: {self.name}"

with contextlib.closing(CustomResource("MyResource")) as resource:
    result = resource.do_work()
    print(result)

# =============================================================================
# 7. EXCEPTION HANDLING İN CONTEXT MANAGERS
# =============================================================================

@contextlib.contextmanager
def exception_logging():
    """Exception'ları loglayan context manager"""
    print("Exception logging başlatıldı")
    try:
        yield
    except Exception as e:
        print(f"Exception yakalandı ve loglandı: {type(e).__name__}: {e}")
        raise  # Exception'ı yeniden raise et
    finally:
        print("Exception logging temizlendi")

@contextlib.contextmanager
def graceful_error_handling(default_return=None):
    """Hataları zarif şekilde ele alan context manager"""
    try:
        yield
    except Exception as e:
        print(f"Hata zarif şekilde ele alındı: {e}")
        if default_return is not None:
            return default_return

class RetryContext:
    """Hata durumunda retry yapan context manager"""
    
    def __init__(self, max_retries=3, delay=1):
        self.max_retries = max_retries
        self.delay = delay
        self.attempt = 0
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None and self.attempt < self.max_retries:
            self.attempt += 1
            print(f"Deneme {self.attempt}/{self.max_retries} başarısız: {exc_value}")
            time.sleep(self.delay)
            return True  # Exception'ı suppress et, tekrar dene
        return False  # Exception'ı raise et

print("\n=== Exception Handling in Context Managers ===")

# Exception logging
with exception_logging():
    try:
        result = 10 / 2
        print(f"Başarılı işlem: {result}")
    except:
        pass

print()
with exception_logging():
    try:
        result = 10 / 0  # ZeroDivisionError
    except ZeroDivisionError:
        print("Sıfıra bölme hatası yakalandı")

# Graceful error handling
print("\nGraceful error handling:")
with graceful_error_handling(default_return="Varsayılan değer"):
    print("Bu çalışacak")

# =============================================================================
# 8. PERFORMANCE CONTEXT MANAGER'LAR
# =============================================================================

class PerformanceProfiler:
    """Performance profiling context manager"""
    
    def __init__(self, operation_name="Operation"):
        self.operation_name = operation_name
        self.start_time = None
        self.start_memory = 0
    
    def _get_memory(self):
        try:
            import psutil
            return psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024
        except ImportError:
            return 0
    
    def __enter__(self):
        self.start_time = time.perf_counter()
        self.start_memory = self._get_memory()
        print(f"[PROFILER] {self.operation_name} başlatılıyor...")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.perf_counter()
        end_memory = self._get_memory()
        
        duration = (end_time - self.start_time) * 1000  # ms
        memory_diff = end_memory - self.start_memory
        
        print(f"[PROFILER] {self.operation_name} tamamlandı:")
        print(f"  Süre: {duration:.2f} ms")
        print(f"  Bellek farkı: {memory_diff:+.2f} MB")

@contextlib.contextmanager
def cpu_intensive_context():
    """CPU yoğun işlemler için context manager"""
    import threading
    original_priority = threading.current_thread()
    
    print("CPU yoğun mod başlatılıyor...")
    try:
        # Yüksek öncelik ayarla (platform bağımlı)
        yield
    finally:
        print("CPU yoğun mod sonlandırılıyor...")

print("\n=== Performance Context Manager'lar ===")

# Performance profiler
with PerformanceProfiler("Liste işlemleri"):
    # CPU yoğun işlem
    numbers = [i**2 for i in range(100000)]
    result = sum(numbers)
    print(f"İşlem sonucu: {len(numbers)} eleman, toplam: {result}")

# =============================================================================
# 9. PRATIK UYGULAMA: WEB SCRAPING CONTEXT MANAGER
# =============================================================================

@contextlib.contextmanager
def web_session(base_url, timeout=30, retries=3):
    """Web scraping için session context manager"""
    print(f"Web session başlatılıyor: {base_url}")
    
    # Simulate session setup
    session = {
        'base_url': base_url,
        'timeout': timeout,
        'retries': retries,
        'requests_made': 0
    }
    
    try:
        yield session
    except Exception as e:
        print(f"Web session hatası: {e}")
        raise
    finally:
        print(f"Web session kapatılıyor. Toplam istek: {session['requests_made']}")

def make_request(session, endpoint):
    """Simulated web request"""
    session['requests_made'] += 1
    print(f"İstek yapılıyor: {session['base_url']}{endpoint}")
    time.sleep(0.1)  # Simulate network delay
    return f"Response from {endpoint}"

print("\n=== Web Scraping Context Manager ===")

with web_session("https://api.example.com") as session:
    response1 = make_request(session, "/users")
    response2 = make_request(session, "/posts")
    response3 = make_request(session, "/comments")
    
    print(f"Responses alındı: {session['requests_made']} istek")

# =============================================================================
# 10. COMPLEX CONTEXT MANAGER: DATABASE POOL
# =============================================================================

class DatabasePool:
    """Gelişmiş database connection pool"""
    
    def __init__(self, db_path, max_connections=5):
        self.db_path = db_path
        self.max_connections = max_connections
        self.connections = []
        self.active_connections = set()
        self.lock = threading.Lock()
    
    def _create_connection(self):
        """Yeni connection oluştur"""
        conn_id = f"conn_{len(self.connections) + 1}"
        connection = {
            'id': conn_id,
            'created_at': datetime.now(),
            'db_path': self.db_path
        }
        return connection
    
    @contextlib.contextmanager
    def get_connection(self):
        """Connection context manager"""
        with self.lock:
            # Mevcut connection var mı?
            available_conn = None
            for conn in self.connections:
                if conn['id'] not in self.active_connections:
                    available_conn = conn
                    break
            
            # Yeni connection oluştur
            if available_conn is None:
                if len(self.connections) < self.max_connections:
                    available_conn = self._create_connection()
                    self.connections.append(available_conn)
                else:
                    raise Exception("Connection pool dolu")
            
            self.active_connections.add(available_conn['id'])
            print(f"Connection alındı: {available_conn['id']}")
        
        try:
            yield available_conn
        finally:
            with self.lock:
                self.active_connections.remove(available_conn['id'])
                print(f"Connection iade edildi: {available_conn['id']}")

print("\n=== Complex Database Pool Context Manager ===")

# Database pool kullanımı
db_pool = DatabasePool("example.db", max_connections=2)

def database_worker(worker_id, pool):
    """Database worker fonksiyonu"""
    try:
        with pool.get_connection() as conn:
            print(f"Worker {worker_id} veritabanı işlemi yapıyor...")
            time.sleep(0.5)  # Simulate database work
            print(f"Worker {worker_id} işlemini tamamladı")
    except Exception as e:
        print(f"Worker {worker_id} hatası: {e}")

# Birden fazla worker çalıştır
workers = []
for i in range(3):  # 3 worker, 2 connection limit
    worker = threading.Thread(target=database_worker, args=(i+1, db_pool))
    workers.append(worker)
    worker.start()

for worker in workers:
    worker.join()

print("\n" + "="*50)
print("CONTEXT MANAGER'LAR TAMAMLANDI")
print("="*50)

# Temizlik
cleanup_files = [
    'ornek_dosya.txt', 'test_custom.txt', 'test.db', 
    'file1.txt', 'file2.txt', 'file3.txt'
]

for file in cleanup_files:
    try:
        os.remove(file)
        print(f"Temizlendi: {file}")
    except FileNotFoundError:
        pass

print("\nContext Manager Türleri Özeti:")
print("1. Class-based context manager'lar (__enter__, __exit__)")
print("2. @contextmanager decorator ile function-based")
print("3. Resource management (dosya, lock, memory)")
print("4. Exception handling context manager'ları")
print("5. Performance monitoring context manager'ları")
print("6. Nested ve complex context manager'lar")
print("7. contextlib utilities (suppress, redirect, closing)")
print("8. Database pool ve connection management")