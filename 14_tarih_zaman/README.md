# Python Tarih ve Zaman İşlemleri

Bu klasör Python'da tarih ve zaman işlemleri konularını kapsamlı bir şekilde ele alır. Modern uygulamalarda kritik öneme sahip zaman yönetimi, timezone işlemleri ve performans analizi konularını öğrenebilirsiniz.

## 📚 İçerik

### 1. temel_tarih_zaman.py
- **Datetime Temelleri**: date, time, datetime sınıfları
- **Zaman Formatları**: strftime, strptime kullanımı
- **Zaman Hesaplamaları**: timedelta ile işlemler
- **Timezone Yönetimi**: pytz ile zaman dilimi işlemleri
- **Takvim İşlemleri**: calendar modülü kullanımı
- **Performans Ölçümü**: time modülü ile süre hesaplama

```python
# Temel datetime kullanımı
import datetime
import pytz

# Şimdiki zaman
now = datetime.datetime.now()
utc_now = datetime.datetime.utcnow()

# Timezone ile çalışma
istanbul_tz = pytz.timezone('Europe/Istanbul')
istanbul_time = datetime.datetime.now(istanbul_tz)
```

### 2. ileri_seviye_tarih.py
- **Relativedelta**: Gelişmiş tarih hesaplamaları
- **İş Günü Hesaplaması**: Tatil ve hafta sonu hesapları
- **Recurring Events**: Tekrarlayan etkinlik yönetimi
- **Natural Language**: Doğal dil ile tarih parsing
- **Veri Analizi**: Pandas ile zaman serisi analizi
- **Timezone Conversion**: Karmaşık timezone dönüşümleri

```python
# Gelişmiş tarih işlemleri
from dateutil.relativedelta import relativedelta
from dateutil import rrule

# 3 ay sonra
future_date = datetime.datetime.now() + relativedelta(months=3)

# Recurring pattern
rule = rrule.rrule(rrule.WEEKLY, byweekday=rrule.MO, count=10)
```

### 3. zaman_dilimi_yonetimi.py
- **Global Timezone**: Dünya zaman dilimleri yönetimi
- **DST Yönetimi**: Daylight Saving Time sorunları
- **Multi-User Systems**: Çoklu kullanıcı timezone koordinasyonu
- **Time Synchronization**: NTP ve zaman senkronizasyonu
- **Thread Safety**: Çoklu thread zaman yönetimi
- **Business Hours**: İş saati hesaplamaları

```python
# Global zaman yönetimi
class GlobalTimeManager:
    def __init__(self):
        self.user_timezones = {}
        self.default_tz = pytz.UTC
    
    def convert_for_user(self, utc_time, user_id):
        user_tz = self.user_timezones.get(user_id, self.default_tz)
        return utc_time.astimezone(user_tz)
```

### 4. pratik_uygulamalar.py
- **Event Calendar**: Kapsamlı etkinlik takvimi
- **Log Analysis**: Zaman bazlı log analizi
- **Performance Monitor**: Sistem performans izleme
- **Scheduling System**: Görev zamanlama sistemi
- **Time Series Analysis**: Zaman serisi istatistikleri
- **Anomaly Detection**: Zaman bazlı anomali tespiti

```python
# Etkinlik takvimi sistemi
class EventCalendar:
    def __init__(self, timezone='UTC'):
        self.timezone = pytz.timezone(timezone)
        self.events = {}
    
    def add_event(self, title, start, end, category='other'):
        # Etkinlik ekleme logic'i
        pass
    
    def find_conflicts(self, start, end):
        # Çakışma kontrolü
        pass
```

## 🎯 Öğrenme Hedefleri

### Temel Seviye
- [ ] Date, time, datetime objelerini kullanma
- [ ] Tarih formatlarını okuma ve yazma
- [ ] Temel zaman hesaplamaları yapma
- [ ] Timezone kavramını anlama
- [ ] Takvim işlemlerini gerçekleştirme

### Orta Seviye
- [ ] Relativedelta ile kompleks hesaplamalar
- [ ] İş günü ve tatil hesaplamaları
- [ ] Recurring pattern'lar oluşturma
- [ ] Timezone dönüşümleri yapma
- [ ] DST problemlerini çözme

### İleri Seviye
- [ ] Global zaman yönetimi sistemleri
- [ ] Multi-thread zaman işlemleri
- [ ] Performans monitoring sistemleri
- [ ] Log analizi ve anomali tespiti
- [ ] Production-ready zaman çözümleri

## 📊 Pratik Örnekler

### 1. Etkinlik Planlayıcısı
```python
# Müsait zaman bulma
def find_available_slots(calendar, date, duration_minutes):
    daily_events = calendar.get_events_for_date(date)
    business_start = 9  # 09:00
    business_end = 17   # 17:00
    
    available_slots = []
    # Implementation...
    return available_slots
```

### 2. Log Analizi
```python
# Zaman bazlı log istatistikleri
def analyze_hourly_traffic(logs):
    hourly_stats = defaultdict(int)
    
    for log in logs:
        hour = log['timestamp'].hour
        hourly_stats[hour] += 1
    
    return dict(hourly_stats)
```

### 3. Performance Monitor
```python
# Süre ölçümü decorator
def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__}: {(end-start)*1000:.2f}ms")
        return result
    return wrapper
```

## 🛠️ Kullanılan Kütüphaneler

### Standart Kütüphaneler
- `datetime`: Temel tarih/zaman işlemleri
- `calendar`: Takvim hesaplamaları
- `time`: Zaman ölçümü ve bekleme
- `threading`: Thread-safe zaman işlemleri

### Harici Kütüphaneler
- `pytz`: Timezone yönetimi
- `dateutil`: Gelişmiş tarih işlemleri
- `pandas`: Zaman serisi analizi (optional)

```bash
# Gerekli kütüphaneleri yükle
pip install pytz python-dateutil pandas
```

## ⚡ Performans İpuçları

### Timezone İşlemleri
```python
# ✅ İyi: UTC'de sakla, display'de dönüştür
utc_time = datetime.utcnow()
user_time = utc_time.replace(tzinfo=pytz.UTC).astimezone(user_tz)

# ❌ Kötü: Her seferinde timezone hesapla
local_time = datetime.now()  # Timezone bilgisi yok
```

### Büyük Veri Setleri
```python
# ✅ İyi: Pandas ile vectorized işlemler
df['datetime'] = pd.to_datetime(df['timestamp'])
hourly_stats = df.groupby(df['datetime'].dt.hour).size()

# ❌ Kötü: Loop ile tek tek işlem
hourly_stats = {}
for record in records:
    hour = parse_datetime(record['timestamp']).hour
    hourly_stats[hour] = hourly_stats.get(hour, 0) + 1
```

## 🚨 Dikkat Edilecek Noktalar

### DST Geçişleri
- Non-existent times (2:30 AM DST başlangıcında)
- Ambiguous times (1:30 AM DST bitişinde iki kez yaşanır)
- `is_dst` parametresini kullanın

### Thread Safety
- Datetime objeler immutable, güvenli
- Global state'i korumak için lock kullanın
- Time measurement'ta perf_counter tercih edin

### Timezone Best Practices
- Veri saklarken UTC kullanın
- User interface'de local time gösterin
- Timezone conversion'ları cache'leyin

## 📈 İleri Seviye Konular

### 1. High-Performance Time Series
- InfluxDB ile time series storage
- Pandas resample ile downsampling
- NumPy datetime64 ile hızlı işlemler

### 2. Distributed Systems
- Vector clocks for distributed events
- NTP synchronization monitoring
- Clock drift detection and correction

### 3. Business Logic
- Holiday calendars (country-specific)
- Business day calculations
- SLA monitoring with time constraints

## 🎯 Gerçek Dünya Uygulamaları

### 1. E-ticaret Sitesi
- Order timestamp tracking
- Delivery time estimation
- Customer timezone handling

### 2. Log Monitoring
- Real-time log analysis
- Performance bottleneck detection
- Anomaly detection in time series

### 3. Scheduling System
- Meeting coordination across timezones
- Recurring task management
- Resource availability tracking

## 📚 Ek Kaynaklar

### Dokumentasyon
- [Python datetime docs](https://docs.python.org/3/library/datetime.html)
- [pytz documentation](https://pytz.sourceforge.net/)
- [dateutil documentation](https://dateutil.readthedocs.io/)

### Önemli RFC'ler
- RFC 3339: Date and Time on the Internet
- RFC 5545: Internet Calendaring and Scheduling (iCalendar)

Bu klasördeki tüm dosyalar, Python'da tarih ve zaman işlemlerinin her yönünü kapsar ve gerçek dünya projelerinde doğrudan kullanılabilir çözümler sunar.