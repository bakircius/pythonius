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

### 2. ileri_seviye_tarih.py
- **Relativedelta**: Gelişmiş tarih hesaplamaları
- **İş Günü Hesaplaması**: Tatil ve hafta sonu hesapları
- **Recurring Events**: Tekrarlayan etkinlik yönetimi
- **Natural Language**: Doğal dil ile tarih parsing
- **Veri Analizi**: Pandas ile zaman serisi analizi
- **Timezone Conversion**: Karmaşık timezone dönüşümleri

### 3. zaman_dilimi_yonetimi.py
- **Global Timezone**: Dünya zaman dilimleri yönetimi
- **DST Yönetimi**: Daylight Saving Time sorunları
- **Multi-User Systems**: Çoklu kullanıcı timezone koordinasyonu
- **Time Synchronization**: NTP ve zaman senkronizasyonu
- **Thread Safety**: Çoklu thread zaman yönetimi
- **Business Hours**: İş saati hesaplamaları

### 4. pratik_uygulamalar.py
- **Event Calendar**: Kapsamlı etkinlik takvimi
- **Log Analysis**: Zaman bazlı log analizi
- **Performance Monitor**: Sistem performans izleme
- **Scheduling System**: Görev zamanlama sistemi
- **Time Series Analysis**: Zaman serisi istatistikleri
- **Anomaly Detection**: Zaman bazlı anomali tespiti

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
Etkinlik takvimi sistemi ile müsait zaman slotları bulma, çakışmaları tespit etme ve otomatik planlama yapma özelliği.

### 2. Log Analizi
Zaman bazlı log istatistikleri, trafik analizi ve performans değerlendirmesi için comprehensive araçlar.

### 3. Performance Monitor
Süre ölçümü, benchmarking ve sistem performansı izleme için decorator ve monitoring araçları.

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

Gerekli kütüphaneleri yüklemek için:
```bash
pip install pytz python-dateutil pandas
```

## ⚡ Performans İpuçları

### Timezone İşlemleri
- UTC'de sakla, display'de dönüştür
- Her seferinde timezone hesaplamaktan kaçın
- Timezone bilgisi olmayan datetime'ler kullanmayın

### Büyük Veri Setleri
- Pandas ile vectorized işlemler tercih edin
- Loop ile tek tek işlem yapmaktan kaçının
- Zaman serisi analizi için optimize edilmiş yöntemler kullanın

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