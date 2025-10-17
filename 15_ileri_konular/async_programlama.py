"""
Python Asenkron Programlama - Comprehensive Guide

Bu dosyada async/await, asyncio, coroutine'ler, concurrent execution
ve asenkron programlamanın tüm yönleri detayıyla incelenecek.
"""

import asyncio
import aiohttp
import time
from datetime import datetime
from typing import List, Dict, Any, Callable, Optional, Awaitable
from concurrent.futures import ThreadPoolExecutor, as_completed
import json

# =============================================================================
# 1. TEMEL ASYNC/AWAIT KAVRAMI
# =============================================================================

print("=== Temel Async/Await Kavramı ===")

async def basit_async_fonksiyon():
    """En basit async fonksiyon örneği"""
    print("Async fonksiyon başladı")
    await asyncio.sleep(1)  # 1 saniye non-blocking bekleme
    print("Async fonksiyon tamamlandı")
    return "Sonuç"

async def sayac(isim: str, saniye: int):
    """Async sayaç fonksiyonu"""
    for i in range(saniye):
        print(f"{isim}: {i+1}")
        await asyncio.sleep(1)
    print(f"{isim} tamamlandı!")

async def temel_async_ornekleri():
    """Temel async örneklerini çalıştır"""
    print("Sıralı async çalışma:")
    result1 = await basit_async_fonksiyon()
    print(f"İlk sonuç: {result1}")
    
    result2 = await basit_async_fonksiyon()
    print(f"İkinci sonuç: {result2}")
    
    print("\nParalel async çalışma:")
    start_time = time.time()
    
    # Paralel çalışma
    task1 = asyncio.create_task(sayac("Task-1", 3))
    task2 = asyncio.create_task(sayac("Task-2", 2))
    task3 = asyncio.create_task(sayac("Task-3", 4))
    
    await asyncio.gather(task1, task2, task3)
    
    end_time = time.time()
    print(f"Toplam süre: {end_time - start_time:.2f} saniye")

# Temel örnekleri çalıştır
print("Async programlama başlatılıyor...")
asyncio.run(temel_async_ornekleri())

# =============================================================================
# 2. ASYNCIO GATHER VE TASK YÖNETİMİ  
# =============================================================================

print("\n=== AsyncIO Task Yönetimi ===")

async def veri_yukle(kaynak: str, sure: float) -> Dict[str, Any]:
    """Veri yükleme simülasyonu"""
    print(f"Veri yükleniyor: {kaynak}")
    await asyncio.sleep(sure)
    return {
        "kaynak": kaynak,
        "veri": f"Data from {kaynak}",
        "timestamp": datetime.now().isoformat(),
        "sure": sure
    }

async def veri_isle(veri: Dict[str, Any]) -> Dict[str, Any]:
    """Veri işleme simülasyonu"""
    print(f"Veri işleniyor: {veri['kaynak']}")
    await asyncio.sleep(0.5)  # İşlem süresi
    
    return {
        **veri,
        "islenmis": True,
        "islem_zamani": datetime.now().isoformat()
    }

async def task_yonetimi_ornekleri():
    """Task yönetimi örnekleri"""
    print("=== Asyncio Gather ===")
    
    # Gather ile paralel veri yükleme
    start_time = time.time()
    
    results = await asyncio.gather(
        veri_yukle("API-1", 2.0),
        veri_yukle("Database", 1.5),
        veri_yukle("File", 1.0),
        veri_yukle("Cache", 0.5)
    )
    
    end_time = time.time()
    print(f"Gather ile 4 kaynak: {end_time - start_time:.2f} saniye")
    
    # Sonuçları işle
    print("\n=== Veri İşleme Pipeline ===")
    processed_results = await asyncio.gather(*[
        veri_isle(result) for result in results
    ])
    
    for result in processed_results:
        print(f"{result['kaynak']}: {result['sure']}s yükleme + işleme")

# Task yönetimi örnekleri
asyncio.run(task_yonetimi_ornekleri())

# =============================================================================
# 3. ASYNC CONTEXT MANAGERS
# =============================================================================

print("\n=== Async Context Managers ===")

class AsyncDatabaseConnection:
    """Async veritabanı bağlantısı context manager"""
    
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = None
    
    async def __aenter__(self):
        print(f"Async DB bağlantısı açılıyor: {self.db_name}")
        await asyncio.sleep(0.1)  # Bağlantı kurma simülasyonu
        self.connection = f"Connection to {self.db_name}"
        return self.connection
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f"Async DB bağlantısı kapatılıyor: {self.db_name}")
        await asyncio.sleep(0.1)  # Bağlantı kapatma simülasyonu
        self.connection = None

class AsyncFileManager:
    """Async dosya yönetici"""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.file_handle = None
    
    async def __aenter__(self):
        print(f"Async dosya açılıyor: {self.filename}")
        await asyncio.sleep(0.05)  # Dosya açma simülasyonu
        self.file_handle = f"Handle for {self.filename}"
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f"Async dosya kapatılıyor: {self.filename}")
        await asyncio.sleep(0.05)  # Dosya kapatma simülasyonu
        self.file_handle = None
    
    async def write(self, data: str):
        """Async yazma"""
        print(f"Async yazma: {data[:50]}...")
        await asyncio.sleep(0.1)

async def async_context_ornekleri():
    """Async context manager örnekleri"""
    print("=== Async Context Manager Kullanımı ===")
    
    # Async database operations
    async with AsyncDatabaseConnection("users_db") as conn:
        print(f"DB işlemi yapılıyor: {conn}")
        await asyncio.sleep(0.2)
        print("Query tamamlandı")
    
    # Async file operations
    async with AsyncFileManager("async_log.txt") as file_mgr:
        await file_mgr.write("Async log mesajı yazılıyor")
        await file_mgr.write("İkinci log mesajı")
    
    # Birden fazla async context
    async with AsyncDatabaseConnection("orders_db") as db_conn, \
               AsyncFileManager("orders.log") as log_file:
        print("Çoklu async context kullanımı")
        await asyncio.sleep(0.3)

# Async context manager örnekleri
asyncio.run(async_context_ornekleri())

# =============================================================================
# 4. ASYNC GENERATORS VE ITERATORS
# =============================================================================

print("\n=== Async Generators ve Iterators ===")

async def async_number_generator(start: int, end: int, delay: float = 0.1):
    """Async sayı üretici"""
    for i in range(start, end + 1):
        print(f"Generating: {i}")
        await asyncio.sleep(delay)
        yield i

async def async_data_stream(items: List[str]):
    """Async veri akışı"""
    for item in items:
        print(f"Processing item: {item}")
        await asyncio.sleep(0.2)
        yield {
            "item": item,
            "processed_at": datetime.now().isoformat(),
            "status": "processed"
        }

class AsyncCounter:
    """Async iterator sınıfı"""
    
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.current = start
    
    def __aiter__(self):
        return self
    
    async def __anext__(self):
        if self.current <= self.end:
            await asyncio.sleep(0.1)
            result = self.current
            self.current += 1
            return result
        else:
            raise StopAsyncIteration

async def async_generator_ornekleri():
    """Async generator örnekleri"""
    print("=== Async Generator Kullanımı ===")
    
    # Async generator iteration
    print("Async sayı üreticisi:")
    async for number in async_number_generator(1, 5, 0.2):
        print(f"Received: {number}")
    
    # Async data stream
    print("\nAsync veri akışı:")
    items = ["item1", "item2", "item3", "item4"]
    async for processed_data in async_data_stream(items):
        print(f"Stream result: {processed_data}")
    
    # Async iterator class
    print("\nAsync iterator sınıfı:")
    counter = AsyncCounter(10, 13)
    async for count in counter:
        print(f"Count: {count}")

# Async generator örnekleri
asyncio.run(async_generator_ornekleri())

# =============================================================================
# 5. ASYNCIO WEB CLIENT (aiohttp benzeri)
# =============================================================================

print("\n=== Async Web Client Simülasyonu ===")

class MockResponse:
    """Mock HTTP response"""
    
    def __init__(self, url: str, status: int, data: Dict[str, Any]):
        self.url = url
        self.status = status
        self.data = data
    
    async def json(self):
        """JSON response"""
        await asyncio.sleep(0.1)  # Parsing delay
        return self.data
    
    async def text(self):
        """Text response"""
        await asyncio.sleep(0.05)
        return json.dumps(self.data)

async def mock_http_get(url: str) -> MockResponse:
    """Mock HTTP GET isteği"""
    print(f"HTTP GET: {url}")
    
    # Simulated network delay
    delay = 0.5 + (hash(url) % 100) / 200  # 0.5-1.0 saniye
    await asyncio.sleep(delay)
    
    # Mock response data
    mock_data = {
        "url": url,
        "timestamp": datetime.now().isoformat(),
        "delay": delay,
        "data": f"Response from {url}"
    }
    
    return MockResponse(url, 200, mock_data)

async def fetch_multiple_urls(urls: List[str]) -> List[Dict[str, Any]]:
    """Birden fazla URL'den paralel veri çek"""
    print(f"Fetching {len(urls)} URLs...")
    
    # Paralel HTTP istekleri
    tasks = [mock_http_get(url) for url in urls]
    responses = await asyncio.gather(*tasks)
    
    # JSON parse et
    results = []
    for response in responses:
        json_data = await response.json()
        results.append(json_data)
    
    return results

async def web_scraping_pipeline(urls: List[str]):
    """Web scraping pipeline"""
    print("=== Web Scraping Pipeline ===")
    
    start_time = time.time()
    
    # Batch processing
    batch_size = 3
    all_results = []
    
    for i in range(0, len(urls), batch_size):
        batch = urls[i:i + batch_size]
        print(f"\nProcessing batch {i//batch_size + 1}: {len(batch)} URLs")
        
        batch_results = await fetch_multiple_urls(batch)
        all_results.extend(batch_results)
        
        # Batch arası kısa bekleme
        await asyncio.sleep(0.2)
    
    end_time = time.time()
    
    print(f"\nTotal results: {len(all_results)}")
    print(f"Total time: {end_time - start_time:.2f} seconds")
    
    return all_results

async def async_web_ornekleri():
    """Async web client örnekleri"""
    urls = [
        "https://api1.example.com/data",
        "https://api2.example.com/users",
        "https://api3.example.com/posts",
        "https://api4.example.com/comments",
        "https://api5.example.com/products",
        "https://api6.example.com/orders",
        "https://api7.example.com/analytics"
    ]
    
    results = await web_scraping_pipeline(urls)
    
    # Results summary
    print(f"\n=== Results Summary ===")
    for result in results[:3]:  # İlk 3 sonucu göster
        print(f"URL: {result['url']}, Delay: {result['delay']:.3f}s")

# Async web örnekleri
asyncio.run(async_web_ornekleri())

# =============================================================================
# 6. ASYNC ERROR HANDLING VE TIMEOUT
# =============================================================================

print("\n=== Async Error Handling ve Timeout ===")

async def hata_verebilecek_fonksiyon(isim: str, basari_orani: float = 0.7):
    """Belirli oranda hata verebilecek async fonksiyon"""
    await asyncio.sleep(0.5)
    
    import random
    if random.random() > basari_orani:
        raise Exception(f"{isim} işleminde hata oluştu")
    
    return f"{isim} başarılı"

async def timeout_ornegi(sure: float):
    """Timeout örneği için yavaş fonksiyon"""
    print(f"Yavaş işlem başlatılıyor ({sure}s)...")
    await asyncio.sleep(sure)
    return f"İşlem {sure} saniyede tamamlandı"

async def async_error_handling():
    """Async error handling örnekleri"""
    print("=== Async Error Handling ===")
    
    # Try-except with async
    try:
        result = await hata_verebilecek_fonksiyon("Test", 0.3)  # Yüksek hata oranı
        print(f"Başarı: {result}")
    except Exception as e:
        print(f"Hata yakalandı: {e}")
    
    # Gather with return_exceptions
    print("\nGather ile hata yönetimi:")
    results = await asyncio.gather(
        hata_verebilecek_fonksiyon("Task1", 0.8),
        hata_verebilecek_fonksiyon("Task2", 0.3),
        hata_verebilecek_fonksiyon("Task3", 0.9),
        return_exceptions=True
    )
    
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"Task{i+1} hata: {result}")
        else:
            print(f"Task{i+1} başarı: {result}")
    
    # Timeout handling
    print("\n=== Timeout Handling ===")
    
    try:
        # 2 saniye timeout ile 3 saniyelik işlem
        result = await asyncio.wait_for(timeout_ornegi(3.0), timeout=2.0)
        print(f"Timeout sonucu: {result}")
    except asyncio.TimeoutError:
        print("İşlem timeout'a uğradı!")
    
    try:
        # 3 saniye timeout ile 1 saniyelik işlem
        result = await asyncio.wait_for(timeout_ornegi(1.0), timeout=3.0)
        print(f"Başarılı sonuç: {result}")
    except asyncio.TimeoutError:
        print("Bu timeout'a uğramayacak")

# Error handling örnekleri
asyncio.run(async_error_handling())

# =============================================================================
# 7. ASYNC WORKER POOL PATTERN
# =============================================================================

print("\n=== Async Worker Pool Pattern ===")

class AsyncWorkerPool:
    """Async worker pool implementation"""
    
    def __init__(self, max_workers: int = 5):
        self.max_workers = max_workers
        self.semaphore = asyncio.Semaphore(max_workers)
        self.active_tasks = set()
    
    async def submit_task(self, coro):
        """Task submit et"""
        async with self.semaphore:
            task = asyncio.create_task(coro)
            self.active_tasks.add(task)
            try:
                result = await task
                return result
            finally:
                self.active_tasks.remove(task)
    
    async def map(self, func, items):
        """Async map operation"""
        tasks = []
        for item in items:
            task = asyncio.create_task(
                self.submit_task(func(item))
            )
            tasks.append(task)
        
        return await asyncio.gather(*tasks, return_exceptions=True)
    
    async def shutdown(self):
        """Pool'u kapat"""
        if self.active_tasks:
            print(f"Waiting for {len(self.active_tasks)} active tasks...")
            await asyncio.gather(*self.active_tasks, return_exceptions=True)

async def cpu_bound_simulation(item: int) -> Dict[str, Any]:
    """CPU-bound işlem simülasyonu"""
    print(f"Processing item {item}")
    
    # Simulated CPU work
    await asyncio.sleep(0.3 + (item % 3) * 0.1)
    
    return {
        "item": item,
        "result": item ** 2,
        "processed_at": datetime.now().isoformat()
    }

async def worker_pool_ornekleri():
    """Worker pool örnekleri"""
    print("=== Async Worker Pool ===")
    
    # Worker pool oluştur
    pool = AsyncWorkerPool(max_workers=3)
    
    # İşlenecek items
    items = list(range(1, 11))  # 1-10 arası sayılar
    
    start_time = time.time()
    
    # Paralel processing
    results = await pool.map(cpu_bound_simulation, items)
    
    end_time = time.time()
    
    # Sonuçları analiz et
    successful_results = [r for r in results if not isinstance(r, Exception)]
    failed_results = [r for r in results if isinstance(r, Exception)]
    
    print(f"\nWorker pool sonuçları:")
    print(f"Toplam işlem: {len(items)}")
    print(f"Başarılı: {len(successful_results)}")
    print(f"Başarısız: {len(failed_results)}")
    print(f"Toplam süre: {end_time - start_time:.2f} saniye")
    
    # Pool'u kapat
    await pool.shutdown()

# Worker pool örnekleri
asyncio.run(worker_pool_ornekleri())

# =============================================================================
# 8. ASYNC/SYNC INTEGRATION
# =============================================================================

print("\n=== Async/Sync Integration ===")

def sync_heavy_computation(n: int) -> int:
    """Sync CPU-heavy computation"""
    print(f"Sync computation for {n}")
    time.sleep(1)  # Blocking operation
    return sum(i * i for i in range(n))

async def async_sync_integration():
    """Async ve sync kod entegrasyonu"""
    print("=== Async/Sync Integration ===")
    
    # ThreadPoolExecutor ile sync kodu async'te çalıştır
    loop = asyncio.get_event_loop()
    
    # Tek sync operation
    print("Tek sync operation:")
    result = await loop.run_in_executor(None, sync_heavy_computation, 1000)
    print(f"Sync result: {result}")
    
    # Paralel sync operations
    print("\nParalel sync operations:")
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = []
        for i in range(1, 6):
            future = loop.run_in_executor(executor, sync_heavy_computation, i * 500)
            futures.append(future)
        
        results = await asyncio.gather(*futures)
    
    end_time = time.time()
    
    print(f"Paralel sync sonuçları: {results}")
    print(f"Paralel sync süresi: {end_time - start_time:.2f} saniye")

# Async/sync integration
asyncio.run(async_sync_integration())

# =============================================================================
# 9. ASYNC EVENT SYSTEM
# =============================================================================

print("\n=== Async Event System ===")

class AsyncEventEmitter:
    """Async event emitter"""
    
    def __init__(self):
        self.listeners: Dict[str, List[Callable]] = {}
    
    def on(self, event: str, callback: Callable):
        """Event listener ekle"""
        if event not in self.listeners:
            self.listeners[event] = []
        self.listeners[event].append(callback)
    
    async def emit(self, event: str, *args, **kwargs):
        """Event emit et"""
        if event in self.listeners:
            tasks = []
            for callback in self.listeners[event]:
                if asyncio.iscoroutinefunction(callback):
                    task = asyncio.create_task(callback(*args, **kwargs))
                    tasks.append(task)
                else:
                    # Sync callback'i async context'te çalıştır
                    loop = asyncio.get_event_loop()
                    task = loop.run_in_executor(None, callback, *args, **kwargs)
                    tasks.append(task)
            
            if tasks:
                await asyncio.gather(*tasks, return_exceptions=True)

class AsyncLogger:
    """Async logger"""
    
    async def log_message(self, level: str, message: str):
        """Async log mesajı"""
        await asyncio.sleep(0.1)  # Async I/O simulation
        timestamp = datetime.now().isoformat()
        print(f"[{timestamp}] {level}: {message}")

class AsyncNotificationService:
    """Async bildirim servisi"""
    
    async def send_notification(self, user: str, message: str):
        """Async bildirim gönder"""
        await asyncio.sleep(0.2)  # Network delay simulation
        print(f"Notification sent to {user}: {message}")

async def event_system_ornekleri():
    """Event system örnekleri"""
    print("=== Async Event System ===")
    
    # Event emitter oluştur
    emitter = AsyncEventEmitter()
    logger = AsyncLogger()
    notification_service = AsyncNotificationService()
    
    # Event listeners tanımla
    emitter.on('user_login', logger.log_message)
    emitter.on('user_login', notification_service.send_notification)
    
    async def user_activity_handler(activity: str, user: str):
        """User activity handler"""
        await asyncio.sleep(0.05)
        print(f"Activity recorded: {user} -> {activity}")
    
    emitter.on('user_activity', user_activity_handler)
    
    # Events emit et
    print("Emitting events...")
    
    await emitter.emit('user_login', 'INFO', 'User logged in successfully', 'john_doe')
    await emitter.emit('user_activity', 'page_view', 'john_doe')
    await emitter.emit('user_activity', 'button_click', 'john_doe')

# Event system örnekleri
asyncio.run(event_system_ornekleri())

# =============================================================================
# 10. ASYNC PERFORMANCE MONITORING
# =============================================================================

print("\n=== Async Performance Monitoring ===")

class AsyncPerformanceMonitor:
    """Async performance monitor"""
    
    def __init__(self):
        self.metrics: Dict[str, List[float]] = {}
        self.active_operations: Dict[str, datetime] = {}
    
    async def start_operation(self, operation_name: str):
        """Operation başlat"""
        self.active_operations[operation_name] = datetime.now()
    
    async def end_operation(self, operation_name: str):
        """Operation bitir"""
        if operation_name in self.active_operations:
            start_time = self.active_operations[operation_name]
            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()
            
            if operation_name not in self.metrics:
                self.metrics[operation_name] = []
            
            self.metrics[operation_name].append(duration)
            del self.active_operations[operation_name]
            
            return duration
        return None
    
    async def get_statistics(self, operation_name: str) -> Optional[Dict[str, float]]:
        """İstatistikleri al"""
        if operation_name not in self.metrics or not self.metrics[operation_name]:
            return None
        
        durations = self.metrics[operation_name]
        return {
            'count': len(durations),
            'total': sum(durations),
            'average': sum(durations) / len(durations),
            'min': min(durations),
            'max': max(durations)
        }

async def monitored_operation(name: str, duration: float, monitor: AsyncPerformanceMonitor):
    """İzlenen async operation"""
    await monitor.start_operation(name)
    
    try:
        print(f"Executing {name}...")
        await asyncio.sleep(duration)
        result = f"{name} completed successfully"
        
    finally:
        actual_duration = await monitor.end_operation(name)
        print(f"{name} took {actual_duration:.3f} seconds")
    
    return result

async def performance_monitoring_ornekleri():
    """Performance monitoring örnekleri"""
    print("=== Async Performance Monitoring ===")
    
    monitor = AsyncPerformanceMonitor()
    
    # Çeşitli operations çalıştır
    operations = [
        ("database_query", 0.5),
        ("api_call", 0.8),
        ("file_processing", 0.3),
        ("database_query", 0.4),  # İkinci DB query
        ("api_call", 0.9),        # İkinci API call
        ("cache_operation", 0.1),
        ("database_query", 0.6),  # Üçüncü DB query
    ]
    
    # Operations'ları paralel çalıştır
    tasks = []
    for name, duration in operations:
        task = asyncio.create_task(
            monitored_operation(name, duration, monitor)
        )
        tasks.append(task)
    
    results = await asyncio.gather(*tasks)
    
    # Performance istatistiklerini göster
    print("\n=== Performance Statistics ===")
    operation_types = set(name for name, _ in operations)
    
    for op_type in operation_types:
        stats = await monitor.get_statistics(op_type)
        if stats:
            print(f"\n{op_type}:")
            print(f"  Count: {stats['count']}")
            print(f"  Average: {stats['average']:.3f}s")
            print(f"  Min: {stats['min']:.3f}s")
            print(f"  Max: {stats['max']:.3f}s")
            print(f"  Total: {stats['total']:.3f}s")

# Performance monitoring örnekleri
asyncio.run(performance_monitoring_ornekleri())

print("\n" + "="*50)
print("ASYNC PROGRAMLAMA TAMAMLANDI")
print("="*50)

print("\nAsync Programming Özeti:")
print("1. Temel async/await syntax")
print("2. AsyncIO task yönetimi ve gather")
print("3. Async context managers (__aenter__, __aexit__)")
print("4. Async generators ve iterators")
print("5. Async web client patterns")
print("6. Error handling ve timeout management")
print("7. Worker pool patterns")
print("8. Async/sync code integration")
print("9. Event-driven async architecture")
print("10. Performance monitoring ve metrics")

print("\nÖnemli Notlar:")
print("- async/await I/O bound işlemler için idealdir")
print("- CPU bound işlemler için ThreadPoolExecutor kullanın")
print("- await sadece async fonksiyonlar içinde kullanılabilir")
print("- asyncio.run() ile async fonksiyonları çalıştırın")
print("- Async context manager'lar kaynak yönetimi için kritik")