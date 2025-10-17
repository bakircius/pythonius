"""
Python Tarih ve Zaman İşlemleri - Temel Konular

Bu dosya Python'da tarih ve zaman işlemlerinin temellerini kapsar.
datetime, date, time modüllerini kullanarak tarih oluşturma, 
formatlandırma, hesaplama ve dönüştürme işlemlerini öğreneceğiz.
"""

import datetime
import time
import calendar
from dateutil import parser, relativedelta
import pytz

# =============================================================================
# 1. DATETIME MODÜLÜ TEMELLERİ
# =============================================================================

print("=== Datetime Modülü Temelleri ===")

def datetime_temelleri():
    """Datetime modülü temel kullanımı"""
    
    print("📅 Temel Tarih ve Zaman Nesneleri:")
    
    # Şu anki tarih ve zaman
    simdi = datetime.datetime.now()
    print(f"Şu an: {simdi}")
    
    # Sadece tarih
    bugun = datetime.date.today()
    print(f"Bugün: {bugun}")
    
    # Sadece zaman
    su_an_zaman = datetime.time(14, 30, 45)
    print(f"Belirli zaman: {su_an_zaman}")
    
    # Manuel tarih oluşturma
    belirli_tarih = datetime.datetime(2024, 3, 15, 14, 30, 45)
    print(f"Belirli tarih: {belirli_tarih}")
    
    # Date nesnesi oluşturma
    tarih = datetime.date(2024, 12, 31)
    print(f"Sadece tarih: {tarih}")
    
    # Time nesnesi oluşturma
    zaman = datetime.time(23, 59, 59, 999999)  # mikrosaniye dahil
    print(f"Detaylı zaman: {zaman}")
    
    print(f"\n🔢 Datetime Bileşenleri:")
    
    dt = datetime.datetime.now()
    print(f"Yıl: {dt.year}")
    print(f"Ay: {dt.month}")
    print(f"Gün: {dt.day}")
    print(f"Saat: {dt.hour}")
    print(f"Dakika: {dt.minute}")
    print(f"Saniye: {dt.second}")
    print(f"Mikrosaniye: {dt.microsecond}")
    print(f"Haftanın günü (0=Pazartesi): {dt.weekday()}")
    print(f"ISO haftanın günü (1=Pazartesi): {dt.isoweekday()}")
    
    print(f"\n📊 Tarih Bilgileri:")
    
    # Yılın günü
    print(f"Yılın {dt.timetuple().tm_yday}. günü")
    
    # Haftanın adı
    gun_adlari = ['Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma', 'Cumartesi', 'Pazar']
    print(f"Bugün: {gun_adlari[dt.weekday()]}")
    
    # Ayın adı
    ay_adlari = ['', 'Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran',
                 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık']
    print(f"Bu ay: {ay_adlari[dt.month]}")

datetime_temelleri()

# =============================================================================
# 2. TARİH VE ZAMAN FORMATLANDİRMA
# =============================================================================

print("\n=== Tarih ve Zaman Formatlandırma ===")

def tarih_formatlama():
    """Tarih ve zaman formatlandırma işlemleri"""
    
    print("📝 strftime() - Tarih Formatlandırma:")
    
    dt = datetime.datetime.now()
    
    # Temel formatlar
    print(f"Tam format: {dt.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Sadece tarih: {dt.strftime('%d.%m.%Y')}")
    print(f"Sadece zaman: {dt.strftime('%H:%M')}")
    print(f"12 saat formatı: {dt.strftime('%I:%M %p')}")
    
    # Detaylı formatlar
    print(f"\n🎨 Çeşitli Format Örnekleri:")
    formatlar = [
        ("%Y-%m-%d", "ISO formatı"),
        ("%d/%m/%Y", "Türkiye formatı"),
        ("%B %d, %Y", "İngilizce uzun"),
        ("%d %b %Y", "Kısa ay adı"),
        ("%A, %B %d, %Y", "Tam gün ve ay adı"),
        ("%Y-%m-%d %H:%M:%S", "Veritabanı formatı"),
        ("%d.%m.%Y %H:%M", "Türkçe tarih-saat"),
        ("%Y%m%d_%H%M%S", "Dosya adı formatı")
    ]
    
    for format_str, aciklama in formatlar:
        formatted = dt.strftime(format_str)
        print(f"{aciklama:20}: {formatted}")
    
    print(f"\n📥 strptime() - String'den Tarih Parsing:")
    
    # String'den tarih oluşturma
    tarih_strings = [
        ("2024-03-15", "%Y-%m-%d"),
        ("15.03.2024", "%d.%m.%Y"),
        ("15/03/2024 14:30", "%d/%m/%Y %H:%M"),
        ("March 15, 2024", "%B %d, %Y"),
        ("2024-03-15T14:30:45", "%Y-%m-%dT%H:%M:%S")
    ]
    
    for tarih_str, format_str in tarih_strings:
        try:
            parsed = datetime.datetime.strptime(tarih_str, format_str)
            print(f"'{tarih_str}' -> {parsed}")
        except ValueError as e:
            print(f"Hata: {tarih_str} - {e}")
    
    print(f"\n🌍 Locale Ayarları ile Formatlandırma:")
    
    # Türkçe ay ve gün isimleri için özel fonksiyon
    def turkce_format(dt):
        """Türkçe tarih formatlandırma"""
        turkce_aylar = [
            '', 'Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran',
            'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık'
        ]
        
        turkce_gunler = [
            'Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 
            'Cuma', 'Cumartesi', 'Pazar'
        ]
        
        return {
            'gun': turkce_gunler[dt.weekday()],
            'ay': turkce_aylar[dt.month],
            'yil': dt.year,
            'gun_sayi': dt.day
        }
    
    tr_tarih = turkce_format(dt)
    print(f"Türkçe: {tr_tarih['gun']}, {tr_tarih['gun_sayi']} {tr_tarih['ay']} {tr_tarih['yil']}")

tarih_formatlama()

# =============================================================================
# 3. TARİH ARİTMETİĞİ VE HESAPLAMALAR
# =============================================================================

print("\n=== Tarih Aritmetiği ve Hesaplamalar ===")

def tarih_hesaplamalari():
    """Tarih hesaplamaları ve aritmetiği"""
    
    print("🧮 Tarih Aritmetiği - timedelta:")
    
    bugun = datetime.date.today()
    simdi = datetime.datetime.now()
    
    print(f"Bugün: {bugun}")
    
    # timedelta ile hesaplamalar
    bir_hafta = datetime.timedelta(days=7)
    on_gun = datetime.timedelta(days=10)
    iki_saat = datetime.timedelta(hours=2)
    otuz_dakika = datetime.timedelta(minutes=30)
    
    print(f"Bir hafta sonra: {bugun + bir_hafta}")
    print(f"10 gün önce: {bugun - on_gun}")
    print(f"2 saat sonra: {simdi + iki_saat}")
    print(f"30 dakika önce: {simdi - otuz_dakika}")
    
    # Karmaşık hesaplamalar
    karmasik_delta = datetime.timedelta(
        days=15,
        hours=3,
        minutes=45,
        seconds=30,
        milliseconds=500
    )
    
    gelecek = simdi + karmasik_delta
    print(f"Karmaşık hesaplama: {gelecek}")
    
    print(f"\n📊 İki Tarih Arası Fark:")
    
    # İki tarih arası fark
    dogum_tarihi = datetime.date(1990, 5, 15)
    yas_delta = bugun - dogum_tarihi
    
    print(f"Doğum tarihi: {dogum_tarihi}")
    print(f"Yaş (gün): {yas_delta.days} gün")
    print(f"Yaş (yıl): {yas_delta.days // 365} yıl (yaklaşık)")
    
    # Çalışma günleri hesaplama
    def calismagunsayisi(baslangic, bitis):
        """İki tarih arası çalışma günü sayısı"""
        gunler = 0
        current = baslangic
        
        while current <= bitis:
            if current.weekday() < 5:  # 0-4 = Pazartesi-Cuma
                gunler += 1
            current += datetime.timedelta(days=1)
        
        return gunler
    
    proje_baslangic = datetime.date(2024, 3, 1)  # Cuma
    proje_bitis = datetime.date(2024, 3, 15)     # Cuma
    
    toplam_gun = (proje_bitis - proje_baslangic).days + 1
    calisma_gunu = calismagunsayisi(proje_baslangic, proje_bitis)
    
    print(f"\nProje süresi:")
    print(f"Başlangıç: {proje_baslangic}")
    print(f"Bitiş: {proje_bitis}")
    print(f"Toplam gün: {toplam_gun}")
    print(f"Çalışma günü: {calisma_gunu}")
    
    print(f"\n🔢 Yaş Hesaplama Fonksiyonu:")
    
    def yas_hesapla(dogum_tarihi):
        """Detaylı yaş hesaplama"""
        bugun = datetime.date.today()
        
        yas = bugun.year - dogum_tarihi.year
        
        # Doğum günü henüz gelmedi mi?
        if bugun.month < dogum_tarihi.month or \
           (bugun.month == dogum_tarihi.month and bugun.day < dogum_tarihi.day):
            yas -= 1
        
        # Bir sonraki doğum günü
        try:
            next_birthday = dogum_tarihi.replace(year=bugun.year + 1)
        except ValueError:  # 29 Şubat durumu
            next_birthday = dogum_tarihi.replace(year=bugun.year + 1, day=28)
        
        days_to_birthday = (next_birthday - bugun).days
        
        return {
            'yas': yas,
            'dogum_gunu_kalan': days_to_birthday,
            'toplam_gun': (bugun - dogum_tarihi).days
        }
    
    ornek_dogum = datetime.date(1990, 12, 25)
    yas_bilgi = yas_hesapla(ornek_dogum)
    
    print(f"Doğum tarihi: {ornek_dogum}")
    print(f"Yaş: {yas_bilgi['yas']}")
    print(f"Doğum gününe kalan gün: {yas_bilgi['dogum_gunu_kalan']}")
    print(f"Toplam yaşanmış gün: {yas_bilgi['toplam_gun']:,}")

tarih_hesaplamalari()

# =============================================================================
# 4. ZAMAN DİLİMLERİ (TIMEZONE)
# =============================================================================

print("\n=== Zaman Dilimleri (Timezone) ===")

def zaman_dilimleri():
    """Zaman dilimi işlemleri"""
    
    print("🌍 Zaman Dilimi İşlemleri:")
    
    # UTC zaman
    utc_now = datetime.datetime.utcnow()
    print(f"UTC zaman: {utc_now}")
    
    # Timezone aware datetime
    utc_tz = pytz.UTC
    aware_utc = utc_tz.localize(utc_now)
    print(f"UTC (timezone aware): {aware_utc}")
    
    # Farklı zaman dilimleri
    zaman_dilimleri_list = [
        ('Europe/Istanbul', 'Türkiye'),
        ('America/New_York', 'New York'),
        ('Europe/London', 'Londra'),
        ('Asia/Tokyo', 'Tokyo'),
        ('Australia/Sydney', 'Sidney'),
        ('America/Los_Angeles', 'Los Angeles')
    ]
    
    print(f"\n🕐 Dünya Saatleri:")
    for tz_name, sehir in zaman_dilimleri_list:
        tz = pytz.timezone(tz_name)
        local_time = aware_utc.astimezone(tz)
        print(f"{sehir:15}: {local_time.strftime('%H:%M:%S (%d.%m.%Y)')}")
    
    print(f"\n🔄 Zaman Dilimi Dönüşümleri:")
    
    # İstanbul zamanı oluştur
    istanbul_tz = pytz.timezone('Europe/Istanbul')
    istanbul_time = istanbul_tz.localize(datetime.datetime(2024, 6, 15, 14, 30, 0))
    
    print(f"İstanbul zamanı: {istanbul_time}")
    
    # Diğer şehirlere dönüştür
    donusum_sehirler = [
        ('America/New_York', 'New York'),
        ('Europe/Paris', 'Paris'),
        ('Asia/Dubai', 'Dubai'),
        ('Asia/Shanghai', 'Şangay')
    ]
    
    for tz_name, sehir in donusum_sehirler:
        tz = pytz.timezone(tz_name)
        converted = istanbul_time.astimezone(tz)
        print(f"{sehir:10}: {converted.strftime('%H:%M (%d.%m.%Y %Z)')}")
    
    print(f"\n⏰ Çalışma Saatleri Kontrolü:")
    
    def calisma_saati_mi(dt, timezone_str='Europe/Istanbul'):
        """Belirtilen zaman diliminde çalışma saati mi?"""
        tz = pytz.timezone(timezone_str)
        if dt.tzinfo is None:
            dt = tz.localize(dt)
        else:
            dt = dt.astimezone(tz)
        
        # Hafta sonu kontrolü
        if dt.weekday() >= 5:  # Cumartesi=5, Pazar=6
            return False, "Hafta sonu"
        
        # Saat kontrolü (09:00-18:00)
        if dt.hour < 9 or dt.hour >= 18:
            return False, "Çalışma saati dışı"
        
        return True, "Çalışma saati"
    
    # Test zamanları
    test_zamanlari = [
        datetime.datetime(2024, 6, 17, 14, 30),  # Pazartesi 14:30
        datetime.datetime(2024, 6, 17, 8, 30),   # Pazartesi 08:30
        datetime.datetime(2024, 6, 17, 19, 30),  # Pazartesi 19:30
        datetime.datetime(2024, 6, 15, 14, 30),  # Cumartesi 14:30
    ]
    
    for test_time in test_zamanlari:
        is_working, reason = calisma_saati_mi(test_time)
        status = "✅" if is_working else "❌"
        gun = ['Pzt', 'Sal', 'Çar', 'Per', 'Cum', 'Cmt', 'Paz'][test_time.weekday()]
        print(f"{status} {gun} {test_time.strftime('%H:%M')}: {reason}")

zaman_dilimleri()

# =============================================================================
# 5. TAKVİM İŞLEMLERİ
# =============================================================================

print("\n=== Takvim İşlemleri ===")

def takvim_islemleri():
    """Calendar modülü ile takvim işlemleri"""
    
    print("📅 Calendar Modülü İşlemleri:")
    
    # Ay takvimi
    yil, ay = 2024, 3
    print(f"\n{yil} yılının {ay}. ayı:")
    print(calendar.month(yil, ay))
    
    # Yıl takvimi
    print(f"\n{yil} yılı takvimi:")
    print(calendar.calendar(yil))
    
    print(f"\n📊 Takvim Bilgileri:")
    
    # Ayın kaç günü var?
    gun_sayilari = []
    for ay in range(1, 13):
        gun_sayisi = calendar.monthrange(yil, ay)[1]
        ay_adi = calendar.month_name[ay]
        gun_sayilari.append((ay, ay_adi, gun_sayisi))
        print(f"{ay:2d}. {ay_adi:9}: {gun_sayisi:2d} gün")
    
    # Artık yıl kontrolü
    print(f"\n🔄 Artık Yıl Kontrolü:")
    test_yillari = [2020, 2021, 2022, 2023, 2024]
    
    for yil in test_yillari:
        artik = calendar.isleap(yil)
        status = "✅ Artık" if artik else "❌ Normal"
        print(f"{yil}: {status} yıl")
    
    # Artık yıllar arası gün sayısı
    def artik_yillar_arasi(baslangic, bitis):
        """Belirtilen yıllar arasındaki artık yıl sayısı"""
        return calendar.leapdays(baslangic, bitis)
    
    artik_sayi = artik_yillar_arasi(2020, 2030)
    print(f"\n2020-2030 arası artık yıl sayısı: {artik_sayi}")
    
    print(f"\n📆 Özel Günler Hesaplama:")
    
    def ay_gun_numarasi(yil, ay, hangi_gun, kacinci):
        """Ayın kaçıncı günü? (örn: 2. pazartesi)"""
        # hangi_gun: 0=Pazartesi, 6=Pazar
        # kacinci: 1, 2, 3, 4 veya -1 (son)
        
        # Ayın ilk günü
        ilk_gun = datetime.date(yil, ay, 1)
        
        if kacinci == -1:  # Son
            # Ayın son günü
            son_gun = calendar.monthrange(yil, ay)[1]
            for gun in range(son_gun, 0, -1):
                tarih = datetime.date(yil, ay, gun)
                if tarih.weekday() == hangi_gun:
                    return tarih
        else:  # 1., 2., 3., 4.
            sayac = 0
            for gun in range(1, 32):
                try:
                    tarih = datetime.date(yil, ay, gun)
                    if tarih.weekday() == hangi_gun:
                        sayac += 1
                        if sayac == kacinci:
                            return tarih
                except ValueError:
                    break
        
        return None
    
    # Örnekler
    print("2024 yılı özel günler:")
    
    # Mart'ın 2. pazartesi
    ikinci_pazartesi = ay_gun_numarasi(2024, 3, 0, 2)
    print(f"Mart'ın 2. pazartesi: {ikinci_pazartesi}")
    
    # Kasım'ın son perşembesi
    son_persembe = ay_gun_numarasi(2024, 11, 3, -1)
    print(f"Kasım'ın son perşembesi: {son_persembe}")
    
    print(f"\n🏖️ Tatil Günleri Hesaplama:")
    
    def turkiye_resmi_tatiller(yil):
        """Türkiye'nin sabit resmi tatilleri"""
        tatiller = {
            f"{yil}-01-01": "Yılbaşı",
            f"{yil}-04-23": "Ulusal Egemenlik ve Çocuk Bayramı",
            f"{yil}-05-01": "İşçi Bayramı",
            f"{yil}-05-19": "Gençlik ve Spor Bayramı",
            f"{yil}-08-30": "Zafer Bayramı",
            f"{yil}-10-29": "Cumhuriyet Bayramı"
        }
        
        return tatiller
    
    tatiller_2024 = turkiye_resmi_tatiller(2024)
    
    print("2024 Türkiye resmi tatilleri:")
    for tarih_str, tatil_adi in tatiller_2024.items():
        tarih = datetime.datetime.strptime(tarih_str, "%Y-%m-%d").date()
        gun_adi = ['Pzt', 'Sal', 'Çar', 'Per', 'Cum', 'Cmt', 'Paz'][tarih.weekday()]
        print(f"{tarih.strftime('%d.%m.%Y')} ({gun_adi}): {tatil_adi}")

takvim_islemleri()

# =============================================================================
# 6. ZAMAN ÖLÇÜMÜ VE PERFORMANCE
# =============================================================================

print("\n=== Zaman Ölçümü ve Performance ===")

def zaman_olcumu():
    """Zaman ölçümü ve performance işlemleri"""
    
    print("⏱️ Zaman Ölçümü Yöntemleri:")
    
    # time.time() ile ölçüm
    print("\n1. time.time() ile ölçüm:")
    start_time = time.time()
    
    # Simülasyon: Yoğun hesaplama
    total = 0
    for i in range(1000000):
        total += i
    
    end_time = time.time()
    elapsed = end_time - start_time
    print(f"İşlem süresi: {elapsed:.6f} saniye")
    
    # time.perf_counter() ile daha hassas ölçüm
    print("\n2. time.perf_counter() ile ölçüm:")
    start_perf = time.perf_counter()
    
    # Simülasyon: String işlemi
    result = ""
    for i in range(10000):
        result += str(i)
    
    end_perf = time.perf_counter()
    elapsed_perf = end_perf - start_perf
    print(f"String işlem süresi: {elapsed_perf:.6f} saniye")
    
    # Context manager ile zaman ölçümü
    print("\n3. Context Manager ile ölçüm:")
    
    class ZamanOlcer:
        """Zaman ölçüm context manager'ı"""
        
        def __init__(self, aciklama="İşlem"):
            self.aciklama = aciklama
            
        def __enter__(self):
            self.start = time.perf_counter()
            return self
            
        def __exit__(self, exc_type, exc_val, exc_tb):
            self.end = time.perf_counter()
            self.elapsed = self.end - self.start
            print(f"{self.aciklama} süresi: {self.elapsed:.6f} saniye")
    
    # Kullanım örneği
    with ZamanOlcer("Liste comprehension"):
        squares = [i**2 for i in range(100000)]
    
    with ZamanOlcer("For döngüsü"):
        squares2 = []
        for i in range(100000):
            squares2.append(i**2)
    
    print(f"\n📊 Tarih İşlemleri Performance:")
    
    # Farklı tarih işlemlerinin performansı
    def performance_test():
        """Tarih işlemleri performance testi"""
        
        iterations = 100000
        
        # datetime.now() performance
        with ZamanOlcer(f"{iterations:,} datetime.now()"):
            for _ in range(iterations):
                dt = datetime.datetime.now()
        
        # String formatting performance
        dt = datetime.datetime.now()
        with ZamanOlcer(f"{iterations:,} strftime()"):
            for _ in range(iterations):
                formatted = dt.strftime("%Y-%m-%d %H:%M:%S")
        
        # String parsing performance
        date_string = "2024-03-15 14:30:45"
        with ZamanOlcer(f"{iterations:,} strptime()"):
            for _ in range(iterations):
                parsed = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    
    performance_test()
    
    print(f"\n⏰ Uykuya Yatırma ve Bekletme:")
    
    def geri_sayim(saniye):
        """Geri sayım fonksiyonu"""
        print(f"\n{saniye} saniye geri sayım başlıyor...")
        for i in range(saniye, 0, -1):
            print(f"{i}...", end=" ", flush=True)
            time.sleep(1)
        print("Tamamlandı! ✅")
    
    # 3 saniye geri sayım (kısa test)
    geri_sayim(3)
    
    print(f"\n🔔 Periyodik Görevler:")
    
    def periyodik_gorev_simulator():
        """Periyodik görev simülatörü"""
        print("\nPeriyodik görev simülatörü (5 saniye):")
        
        start_time = time.time()
        last_print = start_time
        counter = 0
        
        while time.time() - start_time < 5:  # 5 saniye çalış
            current_time = time.time()
            
            # Her saniye bir mesaj yazdır
            if current_time - last_print >= 1:
                counter += 1
                now_formatted = datetime.datetime.now().strftime("%H:%M:%S")
                print(f"[{now_formatted}] Görev #{counter} çalıştı")
                last_print = current_time
            
            time.sleep(0.1)  # CPU'yu meşgul etme
        
        print("Periyodik görev tamamlandı! ✅")
    
    periyodik_gorev_simulator()

zaman_olcumu()

print("\n💡 Tarih ve Zaman İşlemleri İpuçları:")
print("✅ datetime modülünü temel işlemler için kullanın")
print("✅ pytz ile timezone işlemlerini yapın")
print("✅ strftime/strptime ile formatlandırma yapın")
print("✅ timedelta ile tarih hesaplamaları yapın")
print("✅ calendar modülü ile takvim işlemlerini yapın")
print("✅ time.perf_counter() ile hassas zaman ölçümü yapın")
print("✅ Context manager ile zaman ölçümü otomatikleştirin")

print("\n⚠️ Dikkat Edilecek Noktalar:")
print("• Timezone-aware datetime kullanın (özellikle global uygulamalarda)")
print("• UTC zaman ile çalışmayı tercih edin")
print("• Artık yıl hesaplamalarını göz önünde bulundurun")
print("• Performance-critical uygulamalarda datetime işlemlerini optimize edin")
print("• Kullanıcı input'larını doğru format ile parse edin")

print("\n✅ Python tarih ve zaman temel işlemleri öğrenildi!")
print("✅ Datetime formatlandırma ve parsing öğrenildi!")
print("✅ Zaman dilimi işlemleri öğrenildi!")
print("✅ Takvim hesaplamaları öğrenildi!")
print("✅ Performance ölçümü teknikleri öğrenildi!")