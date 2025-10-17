"""
Python Tarih/Zaman Pratik Uygulamaları ve Projeler

Bu dosya Python'da tarih/zaman konusunda pratik uygulamalar,
gerçek dünya projeleri ve kapsamlı örnekler içerir.
Kalendar uygulaması, log analizi, performans monitoring gibi
konuları ele alacağız.
"""

import datetime
from dateutil import rrule, parser
from dateutil.relativedelta import relativedelta
import pytz
import calendar
import json
import sqlite3
from collections import defaultdict, Counter
import re
import statistics
import threading
import time
from concurrent.futures import ThreadPoolExecutor
import csv

# =============================================================================
# 1. TAKVIM VE ETKİNLİK YÖNETİM SİSTEMİ
# =============================================================================

print("=== Takvim ve Etkinlik Yönetim Sistemi ===")

class EtkinlikTakvimi:
    """Kapsamlı etkinlik takvimi sistemi"""
    
    def __init__(self, timezone='UTC'):
        self.timezone = pytz.timezone(timezone)
        self.etkinlikler = {}
        self.recurring_rules = {}
        self.kategoriler = ['iş', 'kişisel', 'toplantı', 'tatil', 'diğer']
        self.etkinlik_id_counter = 1
    
    def etkinlik_ekle(self, baslik, baslangic, bitis, kategori='diğer', 
                     aciklama='', recurring=None, remind_before=None):
        """Yeni etkinlik ekle"""
        
        # Datetime objelerini timezone-aware yap
        if isinstance(baslangic, str):
            baslangic = parser.parse(baslangic)
        if isinstance(bitis, str):
            bitis = parser.parse(bitis)
        
        if baslangic.tzinfo is None:
            baslangic = self.timezone.localize(baslangic)
        if bitis.tzinfo is None:
            bitis = self.timezone.localize(bitis)
        
        etkinlik_id = f"event_{self.etkinlik_id_counter}"
        self.etkinlik_id_counter += 1
        
        etkinlik = {
            'id': etkinlik_id,
            'baslik': baslik,
            'baslangic': baslangic,
            'bitis': bitis,
            'kategori': kategori,
            'aciklama': aciklama,
            'olusturma_zamani': datetime.datetime.now(self.timezone),
            'remind_before': remind_before
        }
        
        self.etkinlikler[etkinlik_id] = etkinlik
        
        # Recurring rule varsa ekle
        if recurring:
            self.recurring_rules[etkinlik_id] = recurring
        
        return etkinlik_id
    
    def recurring_etkinlik_olustur(self, etkinlik_id, rule_type, interval=1, 
                                 count=None, until=None, weekdays=None):
        """Tekrarlayan etkinlik kuralı oluştur"""
        
        if etkinlik_id not in self.etkinlikler:
            return False, "Etkinlik bulunamadı"
        
        rule_map = {
            'daily': rrule.DAILY,
            'weekly': rrule.WEEKLY,
            'monthly': rrule.MONTHLY,
            'yearly': rrule.YEARLY
        }
        
        if rule_type not in rule_map:
            return False, "Geçersiz rule tipi"
        
        base_etkinlik = self.etkinlikler[etkinlik_id]
        
        # RRule parametreleri
        rule_params = {
            'freq': rule_map[rule_type],
            'interval': interval,
            'dtstart': base_etkinlik['baslangic']
        }
        
        if count:
            rule_params['count'] = count
        if until:
            rule_params['until'] = until
        if weekdays and rule_type == 'weekly':
            # Haftanın günleri (0=Pazartesi, 6=Pazar)
            rule_params['byweekday'] = weekdays
        
        rule = rrule.rrule(**rule_params)
        
        self.recurring_rules[etkinlik_id] = {
            'rule': rule,
            'type': rule_type,
            'interval': interval
        }
        
        return True, f"Recurring rule oluşturuldu: {rule_type} her {interval}"
    
    def tarih_araliginda_etkinlikler(self, baslangic_tarih, bitis_tarih):
        """Belirtilen tarih aralığındaki tüm etkinlikleri getir"""
        
        if isinstance(baslangic_tarih, str):
            baslangic_tarih = parser.parse(baslangic_tarih).date()
        if isinstance(bitis_tarih, str):
            bitis_tarih = parser.parse(bitis_tarih).date()
        
        etkinlikler = []
        
        for etkinlik_id, etkinlik in self.etkinlikler.items():
            
            # Normal etkinlik kontrolü
            etkinlik_tarihi = etkinlik['baslangic'].date()
            
            if baslangic_tarih <= etkinlik_tarihi <= bitis_tarih:
                etkinlikler.append(etkinlik)
            
            # Recurring etkinlik kontrolü
            if etkinlik_id in self.recurring_rules:
                rule_info = self.recurring_rules[etkinlik_id]
                rule = rule_info['rule']
                
                # Belirtilen aralıktaki occurrences
                for occurrence in rule:
                    occurrence_date = occurrence.date()
                    
                    if occurrence_date > bitis_tarih:
                        break
                    
                    if baslangic_tarih <= occurrence_date <= bitis_tarih:
                        # Recurring etkinlik kopyası oluştur
                        sure = etkinlik['bitis'] - etkinlik['baslangic']
                        recurring_etkinlik = etkinlik.copy()
                        recurring_etkinlik['baslangic'] = occurrence
                        recurring_etkinlik['bitis'] = occurrence + sure
                        recurring_etkinlik['recurring'] = True
                        etkinlikler.append(recurring_etkinlik)
        
        # Tarihe göre sırala
        etkinlikler.sort(key=lambda x: x['baslangic'])
        return etkinlikler
    
    def gunluk_agenda(self, tarih):
        """Belirtilen gün için agenda oluştur"""
        
        if isinstance(tarih, str):
            tarih = parser.parse(tarih).date()
        
        etkinlikler = self.tarih_araliginda_etkinlikler(tarih, tarih)
        
        agenda = {
            'tarih': tarih,
            'gun_adi': calendar.day_name[tarih.weekday()],
            'etkinlik_sayisi': len(etkinlikler),
            'etkinlikler': []
        }
        
        for etkinlik in etkinlikler:
            agenda_item = {
                'saat': etkinlik['baslangic'].strftime('%H:%M'),
                'baslik': etkinlik['baslik'],
                'sure': str(etkinlik['bitis'] - etkinlik['baslangic']),
                'kategori': etkinlik['kategori'],
                'recurring': etkinlik.get('recurring', False)
            }
            agenda['etkinlikler'].append(agenda_item)
        
        return agenda
    
    def cakisan_etkinlikler_bul(self, baslangic, bitis):
        """Belirtilen zaman aralığı ile çakışan etkinlikleri bul"""
        
        if isinstance(baslangic, str):
            baslangic = parser.parse(baslangic)
        if isinstance(bitis, str):
            bitis = parser.parse(bitis)
        
        cakisanlar = []
        
        # Geniş tarih aralığında etkinlikleri al
        arama_baslangic = baslangic.date() - datetime.timedelta(days=1)
        arama_bitis = bitis.date() + datetime.timedelta(days=1)
        
        tumunu_etkinlikler = self.tarih_araliginda_etkinlikler(arama_baslangic, arama_bitis)
        
        for etkinlik in tumunu_etkinlikler:
            # Çakışma kontrolü
            if (etkinlik['baslangic'] < bitis and etkinlik['bitis'] > baslangic):
                cakisanlar.append(etkinlik)
        
        return cakisanlar
    
    def musait_zaman_bul(self, tarih, sure_dakika, is_saatleri=(9, 17)):
        """Belirtilen günde müsait zamanları bul"""
        
        if isinstance(tarih, str):
            tarih = parser.parse(tarih).date()
        
        gun_baslangic = datetime.datetime.combine(
            tarih, datetime.time(is_saatleri[0], 0)
        )
        gun_bitis = datetime.datetime.combine(
            tarih, datetime.time(is_saatleri[1], 0)
        )
        
        gun_baslangic = self.timezone.localize(gun_baslangic)
        gun_bitis = self.timezone.localize(gun_bitis)
        
        # Gün içindeki etkinlikleri al
        etkinlikler = self.tarih_araliginda_etkinlikler(tarih, tarih)
        etkinlikler = [e for e in etkinlikler if e['baslangic'] >= gun_baslangic]
        
        # Boş zamanları hesapla
        musait_zamanlar = []
        
        if not etkinlikler:
            # Hiç etkinlik yoksa tüm gün müsait
            musait_zamanlar.append({
                'baslangic': gun_baslangic,
                'bitis': gun_bitis,
                'sure_dakika': (gun_bitis - gun_baslangic).total_seconds() / 60
            })
        else:
            # İlk etkinlik öncesi
            if etkinlikler[0]['baslangic'] > gun_baslangic:
                sure = (etkinlikler[0]['baslangic'] - gun_baslangic).total_seconds() / 60
                if sure >= sure_dakika:
                    musait_zamanlar.append({
                        'baslangic': gun_baslangic,
                        'bitis': etkinlikler[0]['baslangic'],
                        'sure_dakika': sure
                    })
            
            # Etkinlikler arası
            for i in range(len(etkinlikler) - 1):
                ara_baslangic = etkinlikler[i]['bitis']
                ara_bitis = etkinlikler[i + 1]['baslangic']
                
                sure = (ara_bitis - ara_baslangic).total_seconds() / 60
                if sure >= sure_dakika:
                    musait_zamanlar.append({
                        'baslangic': ara_baslangic,
                        'bitis': ara_bitis,
                        'sure_dakika': sure
                    })
            
            # Son etkinlik sonrası
            if etkinlikler[-1]['bitis'] < gun_bitis:
                sure = (gun_bitis - etkinlikler[-1]['bitis']).total_seconds() / 60
                if sure >= sure_dakika:
                    musait_zamanlar.append({
                        'baslangic': etkinlikler[-1]['bitis'],
                        'bitis': gun_bitis,
                        'sure_dakika': sure
                    })
        
        return musait_zamanlar

# Etkinlik takvimi demo
print("📅 Etkinlik Takvimi Sistemi:")

takvim = EtkinlikTakvimi('Europe/Istanbul')

# Örnek etkinlikler ekle
etkinlikler_data = [
    {
        'baslik': 'Takım Toplantısı',
        'baslangic': '2024-06-17 09:00',
        'bitis': '2024-06-17 10:30',
        'kategori': 'iş',
        'aciklama': 'Haftalık takım toplantısı'
    },
    {
        'baslik': 'Proje Sunumu',
        'baslangic': '2024-06-17 14:00',
        'bitis': '2024-06-17 15:00',
        'kategori': 'iş'
    },
    {
        'baslik': 'Doktor Randevusu',
        'baslangic': '2024-06-17 16:30',
        'bitis': '2024-06-17 17:00',
        'kategori': 'kişisel'
    }
]

for etkinlik_data in etkinlikler_data:
    etkinlik_id = takvim.etkinlik_ekle(**etkinlik_data)
    print(f"Etkinlik eklendi: {etkinlik_id}")

# Recurring etkinlik ekle
recurring_id = takvim.etkinlik_ekle(
    'Spor',
    '2024-06-17 18:00',
    '2024-06-17 19:00',
    'kişisel'
)

# Her pazartesi, çarşamba, cuma (0=Pazartesi, 2=Çarşamba, 4=Cuma)
takvim.recurring_etkinlik_olustur(
    recurring_id, 
    'weekly', 
    interval=1, 
    count=10,
    weekdays=[0, 2, 4]
)

print(f"Recurring etkinlik oluşturuldu: {recurring_id}")

# Günlük agenda
agenda = takvim.gunluk_agenda('2024-06-17')
print(f"\n📋 {agenda['tarih']} ({agenda['gun_adi']}) Agenda:")
print(f"Toplam {agenda['etkinlik_sayisi']} etkinlik")

for etkinlik in agenda['etkinlikler']:
    recurring_icon = "🔄" if etkinlik['recurring'] else ""
    print(f"  {etkinlik['saat']} - {etkinlik['baslik']} ({etkinlik['kategori']}) {recurring_icon}")

# Müsait zamanları bul
musait_zamanlar = takvim.musait_zaman_bul('2024-06-17', 60)  # 60 dakikalık boş alan
print(f"\n⏰ 60+ Dakika Müsait Zamanlar:")
for zaman in musait_zamanlar:
    print(f"  {zaman['baslangic'].strftime('%H:%M')} - {zaman['bitis'].strftime('%H:%M')} ({zaman['sure_dakika']:.0f} dk)")

# =============================================================================
# 2. LOG ANALİZİ VE ZAMAN BAZLI İSTATİSTİKLER
# =============================================================================

print("\n=== Log Analizi ve Zaman Bazlı İstatistikler ===")

class LogAnalyzer:
    """Log dosyalarının zaman bazlı analizi"""
    
    def __init__(self):
        self.logs = []
        self.log_patterns = {
            'apache': r'(\S+) \S+ \S+ \[([^\]]+)\] "([^"]*)" (\d+) (\d+|-)',
            'nginx': r'(\S+) - - \[([^\]]+)\] "([^"]*)" (\d+) (\d+) "([^"]*)" "([^"]*)"',
            'python': r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}),\d+ - (\w+) - (.+)',
            'syslog': r'(\w{3} \d{1,2} \d{2}:\d{2}:\d{2}) (\S+) (.+)'
        }
    
    def log_parse_et(self, log_line, log_type='apache'):
        """Log satırını parse et"""
        
        if log_type not in self.log_patterns:
            return None
        
        pattern = self.log_patterns[log_type]
        match = re.match(pattern, log_line)
        
        if not match:
            return None
        
        if log_type == 'apache':
            ip, timestamp_str, request, status, size = match.groups()
            
            # Timestamp parse
            try:
                timestamp = datetime.datetime.strptime(
                    timestamp_str, '%d/%b/%Y:%H:%M:%S %z'
                )
            except:
                timestamp = parser.parse(timestamp_str)
            
            return {
                'timestamp': timestamp,
                'ip': ip,
                'request': request,
                'status': int(status),
                'size': int(size) if size != '-' else 0,
                'type': log_type
            }
        
        elif log_type == 'python':
            timestamp_str, level, message = match.groups()
            
            timestamp = datetime.datetime.strptime(
                timestamp_str, '%Y-%m-%d %H:%M:%S'
            )
            
            return {
                'timestamp': timestamp,
                'level': level,
                'message': message,
                'type': log_type
            }
        
        return None
    
    def log_dosyasi_yukle(self, dosya_yolu, log_type='apache'):
        """Log dosyasını yükle ve parse et"""
        
        try:
            with open(dosya_yolu, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    parsed = self.log_parse_et(line.strip(), log_type)
                    if parsed:
                        parsed['line_number'] = line_num
                        self.logs.append(parsed)
            
            return len(self.logs), "Log dosyası başarıyla yüklendi"
        
        except Exception as e:
            return 0, f"Hata: {e}"
    
    def ornek_log_verisi_olustur(self, kayit_sayisi=1000):
        """Örnek log verisi oluştur"""
        
        import random
        
        # Örnek IP adresleri
        ips = ['192.168.1.10', '10.0.0.5', '203.0.113.15', '198.51.100.25']
        
        # Örnek requests
        requests = [
            'GET / HTTP/1.1',
            'GET /api/users HTTP/1.1',
            'POST /login HTTP/1.1',
            'GET /static/css/style.css HTTP/1.1',
            'GET /products/123 HTTP/1.1',
            'POST /api/data HTTP/1.1'
        ]
        
        # Örnek status kodları
        status_codes = [200, 200, 200, 200, 404, 500, 301, 302]  # 200 daha sık
        
        # Log kayıtları oluştur
        base_time = datetime.datetime.now() - datetime.timedelta(days=7)
        
        for i in range(kayit_sayisi):
            # Rastgele zaman (son 7 gün)
            time_offset = random.uniform(0, 7 * 24 * 3600)  # 7 gün saniye
            log_time = base_time + datetime.timedelta(seconds=time_offset)
            
            log_entry = {
                'timestamp': log_time,
                'ip': random.choice(ips),
                'request': random.choice(requests),
                'status': random.choice(status_codes),
                'size': random.randint(100, 5000),
                'type': 'apache',
                'line_number': i + 1
            }
            
            self.logs.append(log_entry)
        
        # Zamana göre sırala
        self.logs.sort(key=lambda x: x['timestamp'])
        
        return kayit_sayisi
    
    def saatlik_istatistikler(self):
        """Saatlik log istatistikleri"""
        
        saatlik_sayilar = defaultdict(int)
        saatlik_hatalar = defaultdict(int)
        saatlik_trafik = defaultdict(int)
        
        for log in self.logs:
            saat = log['timestamp'].hour
            saatlik_sayilar[saat] += 1
            saatlik_trafik[saat] += log.get('size', 0)
            
            if log.get('status', 200) >= 400:
                saatlik_hatalar[saat] += 1
        
        return {
            'saatlik_sayilar': dict(saatlik_sayilar),
            'saatlik_hatalar': dict(saatlik_hatalar),
            'saatlik_trafik': dict(saatlik_trafik)
        }
    
    def gunluk_trend_analizi(self, gun_sayisi=7):
        """Günlük trend analizi"""
        
        if not self.logs:
            return {}
        
        # Son N günü analiz et
        son_tarih = max(log['timestamp'] for log in self.logs).date()
        baslangic_tarih = son_tarih - datetime.timedelta(days=gun_sayisi-1)
        
        gunluk_stats = defaultdict(lambda: {
            'toplam_istek': 0,
            'hata_sayisi': 0,
            'trafik': 0,
            'benzersiz_ip': set()
        })
        
        for log in self.logs:
            log_tarih = log['timestamp'].date()
            
            if baslangic_tarih <= log_tarih <= son_tarih:
                stats = gunluk_stats[log_tarih]
                stats['toplam_istek'] += 1
                stats['trafik'] += log.get('size', 0)
                stats['benzersiz_ip'].add(log.get('ip', 'unknown'))
                
                if log.get('status', 200) >= 400:
                    stats['hata_sayisi'] += 1
        
        # Set'leri sayıya çevir
        for tarih, stats in gunluk_stats.items():
            stats['benzersiz_ip'] = len(stats['benzersiz_ip'])
            
            # Hata oranı hesapla
            if stats['toplam_istek'] > 0:
                stats['hata_orani'] = stats['hata_sayisi'] / stats['toplam_istek'] * 100
            else:
                stats['hata_orani'] = 0
        
        return dict(gunluk_stats)
    
    def anomali_tespit_et(self, metrik='toplam_istek', threshold_multiplier=2.0):
        """Anomali tespiti (basit statistical approach)"""
        
        gunluk_data = self.gunluk_trend_analizi()
        
        if len(gunluk_data) < 3:
            return []
        
        # Metrik değerlerini al
        values = [stats[metrik] for stats in gunluk_data.values()]
        
        # İstatistiksel eşik hesapla
        mean_value = statistics.mean(values)
        std_value = statistics.stdev(values) if len(values) > 1 else 0
        
        upper_threshold = mean_value + (threshold_multiplier * std_value)
        lower_threshold = max(0, mean_value - (threshold_multiplier * std_value))
        
        # Anomalileri bul
        anomaliler = []
        
        for tarih, stats in gunluk_data.items():
            value = stats[metrik]
            
            if value > upper_threshold:
                anomaliler.append({
                    'tarih': tarih,
                    'tip': 'yüksek',
                    'metrik': metrik,
                    'değer': value,
                    'ortalama': mean_value,
                    'eşik': upper_threshold
                })
            elif value < lower_threshold:
                anomaliler.append({
                    'tarih': tarih,
                    'tip': 'düşük',
                    'metrik': metrik,
                    'değer': value,
                    'ortalama': mean_value,
                    'eşik': lower_threshold
                })
        
        return anomaliler

# Log analyzer demo
print("📊 Log Analizi Sistemi:")

analyzer = LogAnalyzer()

# Örnek veri oluştur
kayit_sayisi = analyzer.ornek_log_verisi_olustur(500)
print(f"✅ {kayit_sayisi} örnek log kaydı oluşturuldu")

# Saatlik istatistikler
saatlik_stats = analyzer.saatlik_istatistikler()
print(f"\n⏰ Saatlik İstatistikler (En Yoğun 5 Saat):")

# En yoğun saatleri bul
sorted_hours = sorted(
    saatlik_stats['saatlik_sayilar'].items(),
    key=lambda x: x[1],
    reverse=True
)

for saat, sayı in sorted_hours[:5]:
    hata_sayisi = saatlik_stats['saatlik_hatalar'].get(saat, 0)
    trafik_mb = saatlik_stats['saatlik_trafik'].get(saat, 0) / (1024 * 1024)
    
    print(f"  {saat:02d}:00 - {sayı:3d} istek, {hata_sayisi:2d} hata, {trafik_mb:.1f} MB")

# Günlük trend analizi
gunluk_trends = analyzer.gunluk_trend_analizi()
print(f"\n📈 Günlük Trend Analizi:")

for tarih in sorted(gunluk_trends.keys()):
    stats = gunluk_trends[tarih]
    print(f"  {tarih}: {stats['toplam_istek']} istek, "
          f"{stats['hata_orani']:.1f}% hata, "
          f"{stats['benzersiz_ip']} benzersiz IP")

# Anomali tespiti
anomaliler = analyzer.anomali_tespit_et('toplam_istek')
print(f"\n🚨 Anomali Tespiti:")

if anomaliler:
    for anomali in anomaliler:
        tip_icon = "⬆️" if anomali['tip'] == 'yüksek' else "⬇️"
        print(f"  {tip_icon} {anomali['tarih']}: {anomali['değer']} "
              f"(ortalama: {anomali['ortalama']:.1f})")
else:
    print("  Anomali tespit edilmedi")

# =============================================================================
# 3. PERFORMANS MONİTORİNG SİSTEMİ
# =============================================================================

print("\n=== Performans Monitoring Sistemi ===")

class PerformansMonitor:
    """Sistem ve uygulama performans monitoring"""
    
    def __init__(self):
        self.metrikler = defaultdict(list)
        self.aktif_olcumler = {}
        self.lock = threading.Lock()
        self.monitoring_aktif = False
        self.monitoring_thread = None
        self.thresholds = {
            'cpu_usage': 80.0,
            'memory_usage': 85.0,
            'response_time': 1000.0,  # ms
            'error_rate': 5.0  # %
        }
    
    def metrik_ekle(self, metrik_adi, deger, timestamp=None):
        """Metrik değeri ekle"""
        
        if timestamp is None:
            timestamp = datetime.datetime.now()
        
        with self.lock:
            self.metrikler[metrik_adi].append({
                'timestamp': timestamp,
                'value': deger
            })
            
            # Son 1000 ölçümü sakla
            if len(self.metrikler[metrik_adi]) > 1000:
                self.metrikler[metrik_adi] = self.metrikler[metrik_adi][-1000:]
    
    def olcum_baslat(self, islem_adi):
        """Performance ölçümü başlat"""
        
        olcum_id = f"{islem_adi}_{int(time.time() * 1000000)}"
        
        with self.lock:
            self.aktif_olcumler[olcum_id] = {
                'islem_adi': islem_adi,
                'baslangic': time.perf_counter(),
                'start_time': datetime.datetime.now()
            }
        
        return olcum_id
    
    def olcum_bitir(self, olcum_id):
        """Performance ölçümü bitir"""
        
        bitis_zamani = time.perf_counter()
        
        with self.lock:
            if olcum_id in self.aktif_olcumler:
                olcum = self.aktif_olcumler.pop(olcum_id)
                sure_ms = (bitis_zamani - olcum['baslangic']) * 1000
                
                # Response time metriği ekle
                self.metrik_ekle(
                    f"response_time_{olcum['islem_adi']}",
                    sure_ms,
                    olcum['start_time']
                )
                
                return sure_ms
        
        return None
    
    def sistem_metrikleri_simule_et(self):
        """Sistem metriklerini simüle et (gerçekte psutil kullanılır)"""
        
        import random
        
        # CPU usage
        cpu_base = 45 + 20 * abs(datetime.datetime.now().hour - 12) / 12
        cpu_noise = random.uniform(-10, 10)
        cpu_usage = max(0, min(100, cpu_base + cpu_noise))
        
        # Memory usage
        memory_base = 60
        memory_trend = (datetime.datetime.now().hour % 4) * 5
        memory_usage = memory_base + memory_trend + random.uniform(-5, 5)
        
        # Disk I/O
        disk_io = random.uniform(10, 100)
        
        # Network
        network_rx = random.uniform(1, 50)  # MB/s
        network_tx = random.uniform(0.5, 20)  # MB/s
        
        return {
            'cpu_usage': cpu_usage,
            'memory_usage': memory_usage,
            'disk_io': disk_io,
            'network_rx': network_rx,
            'network_tx': network_tx
        }
    
    def monitoring_baslat(self, interval_saniye=5):
        """Sürekli monitoring başlat"""
        
        def monitor_worker():
            while self.monitoring_aktif:
                try:
                    # Sistem metriklerini al
                    sistem_metrikleri = self.sistem_metrikleri_simule_et()
                    
                    for metrik, deger in sistem_metrikleri.items():
                        self.metrik_ekle(metrik, deger)
                    
                    # Threshold kontrolü
                    self.threshold_kontrol_et()
                    
                    time.sleep(interval_saniye)
                
                except Exception as e:
                    print(f"Monitoring hatası: {e}")
                    break
        
        self.monitoring_aktif = True
        self.monitoring_thread = threading.Thread(target=monitor_worker, daemon=True)
        self.monitoring_thread.start()
        
        return "Monitoring başlatıldı"
    
    def monitoring_durdur(self):
        """Monitoring durdur"""
        
        self.monitoring_aktif = False
        if self.monitoring_thread:
            self.monitoring_thread.join(timeout=1)
        
        return "Monitoring durduruldu"
    
    def threshold_kontrol_et(self):
        """Threshold değerlerini kontrol et"""
        
        uyarilar = []
        
        for metrik, threshold in self.thresholds.items():
            if metrik in self.metrikler and self.metrikler[metrik]:
                son_deger = self.metrikler[metrik][-1]['value']
                
                if son_deger > threshold:
                    uyarilar.append({
                        'metrik': metrik,
                        'deger': son_deger,
                        'threshold': threshold,
                        'timestamp': datetime.datetime.now()
                    })
        
        if uyarilar:
            self.uyari_gonder(uyarilar)
        
        return uyarilar
    
    def uyari_gonder(self, uyarilar):
        """Uyarı gönder"""
        
        for uyari in uyarilar:
            print(f"🚨 UYARI: {uyari['metrik']} = {uyari['deger']:.1f} "
                  f"(threshold: {uyari['threshold']:.1f})")
    
    def metrik_istatistikleri(self, metrik_adi, son_n_dakika=60):
        """Metrik istatistikleri hesapla"""
        
        if metrik_adi not in self.metrikler:
            return None
        
        # Son N dakikanın verilerini al
        cutoff_time = datetime.datetime.now() - datetime.timedelta(minutes=son_n_dakika)
        
        son_veriler = [
            m for m in self.metrikler[metrik_adi]
            if m['timestamp'] >= cutoff_time
        ]
        
        if not son_veriler:
            return None
        
        values = [m['value'] for m in son_veriler]
        
        return {
            'count': len(values),
            'min': min(values),
            'max': max(values),
            'mean': statistics.mean(values),
            'median': statistics.median(values),
            'stdev': statistics.stdev(values) if len(values) > 1 else 0,
            'current': values[-1] if values else None,
            'timestamp_range': {
                'start': son_veriler[0]['timestamp'],
                'end': son_veriler[-1]['timestamp']
            }
        }
    
    def performans_raporu(self):
        """Kapsamlı performans raporu"""
        
        rapor = {
            'rapor_zamani': datetime.datetime.now(),
            'metrikler': {}
        }
        
        # Tüm metriklerin istatistiklerini hesapla
        for metrik_adi in self.metrikler.keys():
            stats = self.metrik_istatistikleri(metrik_adi, 60)
            if stats:
                rapor['metrikler'][metrik_adi] = stats
        
        return rapor

# Performance monitor demo
print("📈 Performans Monitoring Sistemi:")

monitor = PerformansMonitor()

# Monitoring başlat
print(f"✅ {monitor.monitoring_baslat(1)}")  # Her 1 saniyede bir

# Birkaç saniye bekle
print("⏳ 5 saniye veri toplama...")
time.sleep(5)

# Örnek işlem ölçümleri
def ornek_islem_1():
    """Örnek işlem 1"""
    time.sleep(random.uniform(0.1, 0.3))
    return "İşlem 1 tamamlandı"

def ornek_islem_2():
    """Örnek işlem 2"""
    time.sleep(random.uniform(0.05, 0.2))
    return "İşlem 2 tamamlandı"

# İşlemleri ölç
print("📊 İşlem performans ölçümleri:")

import random  # random import ekle

for i in range(5):
    # İşlem 1
    olcum_id1 = monitor.olcum_baslat("ornek_islem_1")
    sonuc1 = ornek_islem_1()
    sure1 = monitor.olcum_bitir(olcum_id1)
    
    # İşlem 2
    olcum_id2 = monitor.olcum_baslat("ornek_islem_2")
    sonuc2 = ornek_islem_2()
    sure2 = monitor.olcum_bitir(olcum_id2)
    
    print(f"  İşlem 1: {sure1:.1f}ms, İşlem 2: {sure2:.1f}ms")

# Performans raporu
rapor = monitor.performans_raporu()
print(f"\n📋 Performans Raporu ({rapor['rapor_zamani'].strftime('%H:%M:%S')}):")

for metrik, stats in rapor['metrikler'].items():
    if stats['count'] > 0:
        print(f"  {metrik}:")
        print(f"    Ortalama: {stats['mean']:.2f}")
        print(f"    Min/Max: {stats['min']:.2f}/{stats['max']:.2f}")
        print(f"    Güncel: {stats['current']:.2f}")

# Monitoring durdur
monitor.monitoring_durdur()
print(f"\n✅ Monitoring durduruldu")

print("\n🎯 Pratik Uygulamalar Tamamlandı!")
print("✅ Etkinlik takvim sistemi oluşturuldu!")
print("✅ Log analizi ve istatistik sistemi geliştirildi!")
print("✅ Performans monitoring sistemi kuruldu!")
print("✅ Gerçek dünya zaman yönetimi senaryoları uygulandı!")

print("\n💡 İleri Seviye Zaman Yönetimi İpuçları:")
print("✅ Etkinlik çakışmalarını önlemek için overlap kontrolü yapın")
print("✅ Log analizi için regex patterns optimize edin")
print("✅ Performans metriklerini real-time dashboard'da gösterin")
print("✅ Anomali tespiti için machine learning algoritmaları kullanın")
print("✅ Zaman serisi verilerini veritabanında efficient saklayın")

print("\n⚡ Production Önerileri:")
print("• Büyük log dosyaları için streaming processing kullanın")
print("• Monitoring metrikleri için time-series database (InfluxDB) tercih edin")
print("• Alerting sistemi için threshold-based ve ML-based yaklaşımları birleştirin")
print("• Etkinlik takvimi için iCal standardını destekleyin")
print("• Timezone conversion'lar için cache mekanizması ekleyin")

print("\n✅ Python tarih/zaman pratik uygulamaları öğrenildi!")