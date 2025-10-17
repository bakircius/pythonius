"""
Python Zaman Dilimi İşlemleri ve Senkronizasyon

Bu dosya Python'da zaman dilimi yönetimi, dünya saatleri,
zaman senkronizasyonu ve ileri seviye timezone işlemlerini kapsar.
Global uygulamalar için kritik zaman yönetimi tekniklerini öğreneceğiz.
"""

import datetime
from dateutil import tz
import pytz
import time
import threading
from concurrent.futures import ThreadPoolExecutor
import json
from collections import defaultdict

# =============================================================================
# 1. ZAMAN DİLİMİ TEMELLERİ VE YÖNETIM
# =============================================================================

print("=== Zaman Dilimi Temelleri ve Yönetim ===")

def zaman_dilimi_temelleri():
    """Zaman dilimi temelleri ve yönetim"""
    
    print("🌍 Zaman Dilimi Temelleri:")
    
    # UTC temel zaman
    utc_now = datetime.datetime.utcnow()
    print(f"UTC Zaman: {utc_now}")
    
    # Yerel zaman
    local_now = datetime.datetime.now()
    print(f"Yerel Zaman: {local_now}")
    
    # Timezone aware UTC
    utc_aware = datetime.datetime.now(pytz.UTC)
    print(f"UTC (timezone aware): {utc_aware}")
    
    # Sistem timezone'u
    system_tz = tz.tzlocal()
    system_time = datetime.datetime.now(system_tz)
    print(f"Sistem timezone: {system_time}")
    
    print(f"\n🕐 Dünya Zaman Dilimleri:")
    
    # Major zaman dilimleri
    major_timezones = [
        ('UTC', 'UTC'),
        ('US/Eastern', 'New York'),
        ('US/Pacific', 'Los Angeles'),
        ('Europe/London', 'Londra'),
        ('Europe/Paris', 'Paris'),
        ('Europe/Istanbul', 'İstanbul'),
        ('Asia/Tokyo', 'Tokyo'),
        ('Asia/Shanghai', 'Şangay'),
        ('Asia/Dubai', 'Dubai'),
        ('Australia/Sydney', 'Sidney'),
        ('Pacific/Auckland', 'Auckland')
    ]
    
    base_time = datetime.datetime(2024, 6, 15, 12, 0, 0, tzinfo=pytz.UTC)
    
    print("Aynı anda dünya saatleri (UTC 12:00):")
    for tz_name, city in major_timezones:
        tz = pytz.timezone(tz_name)
        local_time = base_time.astimezone(tz)
        offset = local_time.strftime('%z')
        print(f"{city:12}: {local_time.strftime('%H:%M (%d.%m.%Y)')} (UTC{offset[:3]}:{offset[3:]})")
    
    print(f"\n🔄 Timezone Dönüşümleri:")
    
    # İstanbul zamanından diğer şehirlere
    istanbul_tz = pytz.timezone('Europe/Istanbul')
    istanbul_time = istanbul_tz.localize(datetime.datetime(2024, 6, 15, 15, 30, 0))
    
    print(f"İstanbul Zamanı: {istanbul_time.strftime('%H:%M (%d.%m.%Y %Z)')}")
    
    conversion_cities = [
        ('America/New_York', 'New York'),
        ('America/Los_Angeles', 'Los Angeles'),
        ('Europe/London', 'Londra'),
        ('Asia/Tokyo', 'Tokyo'),
        ('Australia/Sydney', 'Sidney')
    ]
    
    for tz_name, city in conversion_cities:
        tz = pytz.timezone(tz_name)
        converted = istanbul_time.astimezone(tz)
        print(f"{city:15}: {converted.strftime('%H:%M (%d.%m.%Y %Z)')}")
    
    print(f"\n📊 Timezone Bilgileri:")
    
    def timezone_info(tz_name):
        """Timezone hakkında detaylı bilgi"""
        tz = pytz.timezone(tz_name)
        now = datetime.datetime.now(tz)
        
        # DST bilgisi
        dst_offset = now.dst()
        is_dst = dst_offset.total_seconds() != 0
        
        # UTC offset
        utc_offset = now.utcoffset()
        offset_hours = utc_offset.total_seconds() / 3600
        
        return {
            'timezone': tz_name,
            'current_time': now,
            'utc_offset': offset_hours,
            'is_dst': is_dst,
            'dst_offset': dst_offset.total_seconds() / 3600 if dst_offset else 0,
            'tzname': now.tzname()
        }
    
    # Önemli timezone'lar hakkında bilgi
    important_zones = ['Europe/Istanbul', 'US/Eastern', 'US/Pacific', 'Asia/Tokyo']
    
    for zone in important_zones:
        info = timezone_info(zone)
        dst_status = "✅ DST" if info['is_dst'] else "❌ No DST"
        print(f"{zone:20}: UTC{info['utc_offset']:+.1f} {dst_status} ({info['tzname']})")

zaman_dilimi_temelleri()

# =============================================================================
# 2. DAYLIGHT SAVING TIME (DST) YÖNETİMİ
# =============================================================================

print("\n=== Daylight Saving Time (DST) Yönetimi ===")

def dst_yonetimi():
    """DST geçişleri ve yönetimi"""
    
    print("🔄 DST Geçişleri ve Analizi:")
    
    def dst_gecisleri_bul(timezone_name, yil):
        """Belirtilen yıl için DST geçişlerini bul"""
        tz = pytz.timezone(timezone_name)
        
        # Yıl boyunca DST geçişlerini ara
        gecisler = []
        
        for ay in range(1, 13):
            for gun in range(1, 32):
                try:
                    # Her günü kontrol et
                    tarih = datetime.datetime(yil, ay, gun, 12, 0, 0)
                    localized = tz.localize(tarih, is_dst=None)
                    
                    # Önceki günle karşılaştır
                    if gun > 1:
                        onceki_tarih = datetime.datetime(yil, ay, gun-1, 12, 0, 0)
                        onceki_localized = tz.localize(onceki_tarih, is_dst=None)
                        
                        if localized.dst() != onceki_localized.dst():
                            gecis_turu = "Yaz saati başlangıcı" if localized.dst() > onceki_localized.dst() else "Yaz saati bitişi"
                            gecisler.append({
                                'tarih': tarih.date(),
                                'turu': gecis_turu,
                                'onceki_dst': onceki_localized.dst(),
                                'yeni_dst': localized.dst()
                            })
                
                except (ValueError, pytz.AmbiguousTimeError, pytz.NonExistentTimeError):
                    continue
        
        return gecisler
    
    # DST kullanan timezone'lar
    dst_zones = ['US/Eastern', 'Europe/London', 'Europe/Paris']
    
    for zone in dst_zones:
        print(f"\n{zone} DST Geçişleri (2024):")
        gecisler = dst_gecisleri_bul(zone, 2024)
        
        for gecis in gecisler:
            print(f"  {gecis['tarih']}: {gecis['turu']}")
    
    print(f"\n⚠️ DST Sorunları ve Çözümleri:")
    
    def dst_sorunlari_demo():
        """DST geçişlerinde yaşanan sorunları göster"""
        
        # US Eastern timezone'da DST geçişi
        eastern = pytz.timezone('US/Eastern')
        
        # Yaz saati başlangıcı (2024 Mart ikinci pazar)
        # 2:00 AM -> 3:00 AM (1 saat ileri)
        print("Yaz Saati Başlangıcı Problemi:")
        
        try:
            # 2:30 AM - bu saat mevcut değil!
            non_existent = eastern.localize(datetime.datetime(2024, 3, 10, 2, 30, 0))
        except pytz.NonExistentTimeError as e:
            print(f"  ❌ Hata: {e}")
        
        # Güvenli yöntem
        safe_time = eastern.localize(datetime.datetime(2024, 3, 10, 2, 30, 0), is_dst=False)
        print(f"  ✅ Güvenli: {safe_time} (is_dst=False kullanarak)")
        
        # Yaz saati bitişi (2024 Kasım ilk pazar)
        # 2:00 AM -> 1:00 AM (1 saat geri)
        print("\nYaz Saati Bitişi Problemi:")
        
        try:
            # 1:30 AM - bu saat iki kez yaşanır!
            ambiguous = eastern.localize(datetime.datetime(2024, 11, 3, 1, 30, 0))
        except pytz.AmbiguousTimeError as e:
            print(f"  ⚠️ Belirsizlik: {e}")
        
        # Her iki durumu da göster
        first_occurrence = eastern.localize(datetime.datetime(2024, 11, 3, 1, 30, 0), is_dst=True)
        second_occurrence = eastern.localize(datetime.datetime(2024, 11, 3, 1, 30, 0), is_dst=False)
        
        print(f"  ✅ İlk geçiş: {first_occurrence} (DST=True)")
        print(f"  ✅ İkinci geçiş: {second_occurrence} (DST=False)")
    
    dst_sorunlari_demo()
    
    print(f"\n🛡️ DST Güvenli Programlama:")
    
    class DSTGuvenliZaman:
        """DST güvenli zaman işlemleri"""
        
        @staticmethod
        def guvenli_localize(tz, dt, prefer_dst=True):
            """DST güvenli localization"""
            try:
                return tz.localize(dt)
            except pytz.NonExistentTimeError:
                # Var olmayan saat - is_dst kullan
                return tz.localize(dt, is_dst=prefer_dst)
            except pytz.AmbiguousTimeError:
                # Belirsiz saat - tercihe göre çöz
                return tz.localize(dt, is_dst=prefer_dst)
        
        @staticmethod
        def zaman_araliği_hesapla(baslangic, bitis, timezone_name):
            """DST geçişlerini dikkate alarak zaman aralığı hesapla"""
            tz = pytz.timezone(timezone_name)
            
            # Eğer naive datetime ise localize et
            if baslangic.tzinfo is None:
                baslangic = DSTGuvenliZaman.guvenli_localize(tz, baslangic)
            if bitis.tzinfo is None:
                bitis = DSTGuvenliZaman.guvenli_localize(tz, bitis)
            
            # UTC'ye çevir ve farkı hesapla
            baslangic_utc = baslangic.astimezone(pytz.UTC)
            bitis_utc = bitis.astimezone(pytz.UTC)
            
            return bitis_utc - baslangic_utc
        
        @staticmethod
        def is_saatleri_hesapla(tarih, timezone_name, baslangic_saat=9, bitis_saat=17):
            """DST dikkate alarak iş saatlerini hesapla"""
            tz = pytz.timezone(timezone_name)
            
            # İş günü başlangıç ve bitişi
            is_baslangic = DSTGuvenliZaman.guvenli_localize(
                tz, 
                datetime.datetime.combine(tarih, datetime.time(baslangic_saat, 0))
            )
            is_bitis = DSTGuvenliZaman.guvenli_localize(
                tz,
                datetime.datetime.combine(tarih, datetime.time(bitis_saat, 0))
            )
            
            # Gerçek iş saati hesapla
            sure = DSTGuvenliZaman.zaman_araliği_hesapla(is_baslangic, is_bitis, timezone_name)
            
            return {
                'baslangic': is_baslangic,
                'bitis': is_bitis,
                'sure_saat': sure.total_seconds() / 3600,
                'sure_dakika': sure.total_seconds() / 60
            }
    
    # DST güvenli işlem örnekleri
    test_tarihi = datetime.date(2024, 3, 10)  # DST geçiş günü
    normal_tarihi = datetime.date(2024, 6, 15)  # Normal gün
    
    print("DST Güvenli İş Saati Hesaplamaları:")
    
    for tarih, aciklama in [(test_tarihi, "DST Geçiş Günü"), (normal_tarihi, "Normal Gün")]:
        is_saati = DSTGuvenliZaman.is_saatleri_hesapla(tarih, 'US/Eastern')
        print(f"\n{aciklama} ({tarih}):")
        print(f"  Başlangıç: {is_saati['baslangic'].strftime('%H:%M %Z')}")
        print(f"  Bitiş: {is_saati['bitis'].strftime('%H:%M %Z')}")
        print(f"  Süre: {is_saati['sure_saat']:.1f} saat")

dst_yonetimi()

# =============================================================================
# 3. GLOBAL UYGULAMA ZAMAN YÖNETİMİ
# =============================================================================

print("\n=== Global Uygulama Zaman Yönetimi ===")

def global_zaman_yonetimi():
    """Global uygulamalar için zaman yönetimi"""
    
    print("🌐 Global Zaman Yönetimi:")
    
    class GlobalZamanYoneticisi:
        """Global uygulamalar için zaman yöneticisi"""
        
        def __init__(self, default_timezone='UTC'):
            self.default_tz = pytz.timezone(default_timezone)
            self.user_timezones = {}
            self.server_timezone = 'UTC'
        
        def kullanici_timezone_ayarla(self, user_id, timezone_name):
            """Kullanıcı timezone'unu ayarla"""
            try:
                tz = pytz.timezone(timezone_name)
                self.user_timezones[user_id] = tz
                return True, f"Timezone {timezone_name} olarak ayarlandı"
            except pytz.UnknownTimeZoneError:
                return False, f"Bilinmeyen timezone: {timezone_name}"
        
        def utc_kaydet(self, dt=None):
            """Veritabanına kayıt için UTC zaman"""
            if dt is None:
                dt = datetime.datetime.utcnow()
            
            if dt.tzinfo is None:
                dt = pytz.UTC.localize(dt)
            
            return dt.astimezone(pytz.UTC)
        
        def kullanici_zamani_goster(self, user_id, utc_time):
            """UTC zamanı kullanıcının timezone'unda göster"""
            user_tz = self.user_timezones.get(user_id, self.default_tz)
            
            if utc_time.tzinfo is None:
                utc_time = pytz.UTC.localize(utc_time)
            
            return utc_time.astimezone(user_tz)
        
        def toplanti_zamani_koordine_et(self, user_ids, utc_time):
            """Çoklu kullanıcı için toplantı zamanını göster"""
            koordinasyon = {}
            
            for user_id in user_ids:
                local_time = self.kullanici_zamani_goster(user_id, utc_time)
                koordinasyon[user_id] = {
                    'local_time': local_time,
                    'timezone': str(local_time.tzinfo),
                    'is_business_hours': self.is_saati_mi(local_time)
                }
            
            return koordinasyon
        
        def is_saati_mi(self, dt):
            """Belirtilen zaman iş saati mi?"""
            # Hafta sonu kontrolü
            if dt.weekday() >= 5:
                return False
            
            # Saat kontrolü (09:00-17:00)
            return 9 <= dt.hour < 17
        
        def en_iyi_toplanti_zamani_bul(self, user_ids, tarih, sure_saat=1):
            """Tüm kullanıcılar için en uygun toplantı zamanını bul"""
            # Tarih başlangıcı UTC'de
            utc_baslangic = datetime.datetime.combine(
                tarih, datetime.time(0, 0), tzinfo=pytz.UTC
            )
            
            uygun_saatler = []
            
            # Her saati kontrol et
            for saat in range(24):
                test_zamani = utc_baslangic + datetime.timedelta(hours=saat)
                koordinasyon = self.toplanti_zamani_koordine_et(user_ids, test_zamani)
                
                # Tüm kullanıcılar iş saatinde mi?
                tumunu_uygun = all(
                    info['is_business_hours'] 
                    for info in koordinasyon.values()
                )
                
                if tumunu_uygun:
                    uygun_saatler.append({
                        'utc_time': test_zamani,
                        'koordinasyon': koordinasyon
                    })
            
            return uygun_saatler
    
    # Global zaman yöneticisi test
    gzm = GlobalZamanYoneticisi()
    
    # Kullanıcıları kaydet
    users = [
        ('user1', 'Europe/Istanbul'),
        ('user2', 'US/Eastern'),
        ('user3', 'Asia/Tokyo'),
        ('user4', 'Australia/Sydney')
    ]
    
    for user_id, tz_name in users:
        success, message = gzm.kullanici_timezone_ayarla(user_id, tz_name)
        print(f"{user_id}: {message}")
    
    # Toplantı zamanı koordinasyonu
    print(f"\n📅 Toplantı Zamanı Koordinasyonu:")
    
    utc_meeting = datetime.datetime(2024, 6, 15, 14, 0, tzinfo=pytz.UTC)  # UTC 14:00
    koordinasyon = gzm.toplanti_zamani_koordine_et(['user1', 'user2', 'user3', 'user4'], utc_meeting)
    
    print(f"UTC Toplantı Zamanı: {utc_meeting.strftime('%Y-%m-%d %H:%M UTC')}")
    
    for user_id, info in koordinasyon.items():
        status = "✅ İş Saati" if info['is_business_hours'] else "❌ İş Dışı"
        print(f"{user_id}: {info['local_time'].strftime('%H:%M (%d.%m.%Y)')} {status}")
    
    # En uygun toplantı zamanları
    print(f"\n🎯 En Uygun Toplantı Zamanları:")
    
    uygun_zamanlar = gzm.en_iyi_toplanti_zamani_bul(
        ['user1', 'user2', 'user3', 'user4'], 
        datetime.date(2024, 6, 17)  # Pazartesi
    )
    
    if uygun_zamanlar:
        print("Tüm kullanıcılar için uygun saatler:")
        for uygun in uygun_zamanlar[:3]:  # İlk 3'ü göster
            utc_time = uygun['utc_time']
            print(f"\nUTC {utc_time.strftime('%H:%M')}:")
            for user_id, info in uygun['koordinasyon'].items():
                print(f"  {user_id}: {info['local_time'].strftime('%H:%M')}")
    else:
        print("Tüm kullanıcılar için uygun zaman bulunamadı.")
    
    print(f"\n📊 Zaman Dilimi Çakışma Analizi:")
    
    def cakisma_analizi(timezone_pairs):
        """İki timezone arası çakışma analizi"""
        cakismalar = []
        
        for tz1_name, tz2_name in timezone_pairs:
            tz1 = pytz.timezone(tz1_name)
            tz2 = pytz.timezone(tz2_name)
            
            # İş saati çakışmasını hesapla
            base_date = datetime.date(2024, 6, 17)  # Pazartesi
            
            cakisan_saatler = []
            
            for saat in range(24):
                # Birinci timezone'da iş saati mi?
                dt1 = datetime.datetime.combine(base_date, datetime.time(saat, 0))
                dt1_local = tz1.localize(dt1)
                
                # İkinci timezone'da karşılık gelen saat
                dt2_utc = dt1_local.astimezone(pytz.UTC)
                dt2_local = dt2_utc.astimezone(tz2)
                
                # Her ikisi de iş saatinde mi?
                if (9 <= dt1_local.hour < 17 and dt1_local.weekday() < 5 and
                    9 <= dt2_local.hour < 17 and dt2_local.weekday() < 5):
                    cakisan_saatler.append({
                        'tz1_saat': dt1_local.strftime('%H:%M'),
                        'tz2_saat': dt2_local.strftime('%H:%M')
                    })
            
            cakismalar.append({
                'tz1': tz1_name,
                'tz2': tz2_name,
                'cakisan_saatler': cakisan_saatler
            })
        
        return cakismalar
    
    # Önemli timezone çiftleri
    timezone_pairs = [
        ('Europe/Istanbul', 'US/Eastern'),
        ('Asia/Tokyo', 'US/Pacific'),
        ('Europe/London', 'Asia/Shanghai')
    ]
    
    cakisma_sonuclari = cakisma_analizi(timezone_pairs)
    
    for sonuc in cakisma_sonuclari:
        print(f"\n{sonuc['tz1']} ↔ {sonuc['tz2']}:")
        if sonuc['cakisan_saatler']:
            print(f"  Çakışan iş saatleri ({len(sonuc['cakisan_saatler'])} saat):")
            for cakisma in sonuc['cakisan_saatler'][:5]:  # İlk 5'i göster
                print(f"    {cakisma['tz1_saat']} ↔ {cakisma['tz2_saat']}")
        else:
            print("  İş saati çakışması yok")

global_zaman_yonetimi()

# =============================================================================
# 4. ZAMAN SENKRONIZASYONU VE NTP
# =============================================================================

print("\n=== Zaman Senkronizasyonu ve NTP ===")

def zaman_senkronizasyonu():
    """Zaman senkronizasyonu ve NTP işlemleri"""
    
    print("⏰ Zaman Senkronizasyonu:")
    
    class ZamanSenkronizatoru:
        """Zaman senkronizasyon araçları"""
        
        def __init__(self):
            self.referans_sunucular = [
                'time.google.com',
                'pool.ntp.org', 
                'time.cloudflare.com'
            ]
            self.son_senkronizasyon = None
            self.offset = 0  # Yerel saatle fark (saniye)
        
        def sistem_zamani_al(self):
            """Sistem zamanı al"""
            return datetime.datetime.now()
        
        def utc_zamani_al(self):
            """UTC zamanı al"""
            return datetime.datetime.utcnow()
        
        def zaman_farki_hesapla(self, zaman1, zaman2):
            """İki zaman arasındaki farkı hesapla"""
            if isinstance(zaman1, str):
                zaman1 = datetime.datetime.fromisoformat(zaman1)
            if isinstance(zaman2, str):
                zaman2 = datetime.datetime.fromisoformat(zaman2)
            
            return abs((zaman1 - zaman2).total_seconds())
        
        def zaman_drift_tespit_et(self, referans_zaman):
            """Zaman kayması tespit et"""
            sistem_zamani = self.sistem_zamani_al()
            fark = self.zaman_farki_hesapla(sistem_zamani, referans_zaman)
            
            # 1 saniyeden fazla fark varsa drift var
            if fark > 1.0:
                return True, fark
            return False, fark
        
        def senkronizasyon_gerekli_mi(self, max_drift_saniye=30):
            """Senkronizasyon gerekli mi kontrol et"""
            if self.son_senkronizasyon is None:
                return True, "İlk senkronizasyon"
            
            # Son senkronizasyondan ne kadar zaman geçti?
            gecen_sure = (datetime.datetime.now() - self.son_senkronizasyon).total_seconds()
            
            if gecen_sure > 3600:  # 1 saat
                return True, f"Son senkronizasyon: {gecen_sure/3600:.1f} saat önce"
            
            return False, f"Son senkronizasyon: {gecen_sure/60:.1f} dakika önce"
        
        def mock_ntp_sorgula(self):
            """Mock NTP sorgusu (gerçek NTP simülasyonu)"""
            # Gerçek uygulamada ntplib kullanılır
            import random
            
            # Simüle edilmiş NTP yanıtı
            simdi = datetime.datetime.utcnow()
            # Küçük bir rastgele offset ekle
            offset = random.uniform(-0.1, 0.1)  # ±100ms
            
            return {
                'server_time': simdi + datetime.timedelta(seconds=offset),
                'offset': offset,
                'delay': random.uniform(0.01, 0.05),  # Network delay
                'success': True
            }
        
        def senkronizasyon_yap(self):
            """Zaman senkronizasyonu yap"""
            print("Zaman senkronizasyonu başlatılıyor...")
            
            basarili_sorgular = []
            
            for server in self.referans_sunucular:
                try:
                    # Mock NTP sorgusu
                    ntp_response = self.mock_ntp_sorgula()
                    
                    if ntp_response['success']:
                        basarili_sorgular.append(ntp_response)
                        print(f"  ✅ {server}: offset {ntp_response['offset']:+.3f}s")
                    
                except Exception as e:
                    print(f"  ❌ {server}: {e}")
            
            if basarili_sorgular:
                # Ortalama offset hesapla
                ortalama_offset = sum(s['offset'] for s in basarili_sorgular) / len(basarili_sorgular)
                self.offset = ortalama_offset
                self.son_senkronizasyon = datetime.datetime.now()
                
                return True, f"Senkronizasyon başarılı. Offset: {ortalama_offset:+.3f}s"
            else:
                return False, "Tüm sunucular başarısız"
        
        def duzeltilmis_zaman(self):
            """Offset ile düzeltilmiş sistem zamanı"""
            return datetime.datetime.now() + datetime.timedelta(seconds=self.offset)
    
    # Zaman senkronizatoru test
    senkronizator = ZamanSenkronizatoru()
    
    # İlk durum kontrolü
    gerekli, neden = senkronizator.senkronizasyon_gerekli_mi()
    print(f"Senkronizasyon gerekli: {gerekli} - {neden}")
    
    # Senkronizasyon yap
    basarili, mesaj = senkronizator.senkronizasyon_yap()
    print(f"Senkronizasyon sonucu: {mesaj}")
    
    # Düzeltilmiş zamanı göster
    sistem_zamani = senkronizator.sistem_zamani_al()
    duzeltilmis = senkronizator.duzeltilmis_zaman()
    
    print(f"\nSistem zamanı: {sistem_zamani}")
    print(f"Düzeltilmiş zaman: {duzeltilmis}")
    print(f"Fark: {(duzeltilmis - sistem_zamani).total_seconds():.3f} saniye")
    
    print(f"\n📊 Zaman Doğruluğu Monitoring:")
    
    class ZamanDogrlukMonitor:
        """Zaman doğruluğu izleme"""
        
        def __init__(self):
            self.olcumler = []
            self.uyari_esigi = 1.0  # saniye
            self.kritik_esigi = 5.0  # saniye
        
        def olcum_ekle(self, sistem_zamani, referans_zamani, kaynak="NTP"):
            """Yeni ölçüm ekle"""
            if isinstance(sistem_zamani, str):
                sistem_zamani = datetime.datetime.fromisoformat(sistem_zamani)
            if isinstance(referans_zamani, str):
                referans_zamani = datetime.datetime.fromisoformat(referans_zamani)
            
            fark = (sistem_zamani - referans_zamani).total_seconds()
            
            olcum = {
                'zaman': datetime.datetime.now(),
                'sistem_zamani': sistem_zamani,
                'referans_zamani': referans_zamani,
                'fark': fark,
                'kaynak': kaynak
            }
            
            self.olcumler.append(olcum)
            
            # Eski ölçümleri temizle (son 100 ölçüm)
            if len(self.olcumler) > 100:
                self.olcumler = self.olcumler[-100:]
            
            return self.durum_analizi(olcum)
        
        def durum_analizi(self, olcum):
            """Durum analizi yap"""
            fark = abs(olcum['fark'])
            
            if fark > self.kritik_esigi:
                return "🔴 KRİTİK", f"Zaman farkı {fark:.2f}s (>{self.kritik_esigi}s)"
            elif fark > self.uyari_esigi:
                return "🟡 UYARI", f"Zaman farkı {fark:.2f}s (>{self.uyari_esigi}s)"
            else:
                return "🟢 NORMAL", f"Zaman farkı {fark:.3f}s"
        
        def istatistikler(self):
            """İstatistiksel analiz"""
            if not self.olcumler:
                return "Ölçüm yok"
            
            farklar = [abs(o['fark']) for o in self.olcumler]
            
            return {
                'toplam_olcum': len(self.olcumler),
                'ortalama_fark': sum(farklar) / len(farklar),
                'max_fark': max(farklar),
                'min_fark': min(farklar),
                'son_olcum': self.olcumler[-1]['zaman']
            }
    
    # Monitoring test
    monitor = ZamanDogrlukMonitor()
    
    # Simüle edilmiş ölçümler
    import random
    for i in range(10):
        sistem = datetime.datetime.now()
        # Rastgele offset ekle
        offset = random.uniform(-0.5, 2.0)
        referans = sistem + datetime.timedelta(seconds=offset)
        
        durum, mesaj = monitor.olcum_ekle(sistem, referans)
        print(f"Ölçüm {i+1:2d}: {durum} - {mesaj}")
        
        time.sleep(0.1)  # Kısa bekleme
    
    # İstatistikler
    stats = monitor.istatistikler()
    print(f"\n📈 Monitoring İstatistikleri:")
    print(f"Toplam ölçüm: {stats['toplam_olcum']}")
    print(f"Ortalama fark: {stats['ortalama_fark']:.3f}s")
    print(f"Maksimum fark: {stats['max_fark']:.3f}s")
    print(f"Minimum fark: {stats['min_fark']:.3f}s")

zaman_senkronizasyonu()

# =============================================================================
# 5. ÇOKLU THREAD VE ZAMAN YÖNETİMİ
# =============================================================================

print("\n=== Çoklu Thread ve Zaman Yönetimi ===")

def coklu_thread_zaman():
    """Çoklu thread ortamında zaman yönetimi"""
    
    print("🧵 Çoklu Thread Zaman Yönetimi:")
    
    class ThreadSafeZamanYoneticisi:
        """Thread-safe zaman yöneticisi"""
        
        def __init__(self):
            self._lock = threading.Lock()
            self.thread_zamanlari = {}
            self.global_baslangic = time.time()
        
        def thread_zaman_kaydet(self, thread_id=None):
            """Thread zamanını kaydet"""
            if thread_id is None:
                thread_id = threading.current_thread().ident
            
            with self._lock:
                self.thread_zamanlari[thread_id] = {
                    'baslangic': time.time(),
                    'islem_sayisi': 0,
                    'toplam_sure': 0
                }
        
        def islem_baslat(self, thread_id=None):
            """İşlem başlat"""
            if thread_id is None:
                thread_id = threading.current_thread().ident
            
            return time.perf_counter()
        
        def islem_bitir(self, baslangic_zamani, thread_id=None):
            """İşlem bitir ve süreyi kaydet"""
            if thread_id is None:
                thread_id = threading.current_thread().ident
            
            sure = time.perf_counter() - baslangic_zamani
            
            with self._lock:
                if thread_id in self.thread_zamanlari:
                    self.thread_zamanlari[thread_id]['islem_sayisi'] += 1
                    self.thread_zamanlari[thread_id]['toplam_sure'] += sure
            
            return sure
        
        def thread_istatistikleri(self):
            """Thread istatistikleri"""
            with self._lock:
                return dict(self.thread_zamanlari)
    
    # Thread-safe zaman yöneticisi test
    zaman_yoneticisi = ThreadSafeZamanYoneticisi()
    
    def worker_function(worker_id, islem_sayisi):
        """Worker thread fonksiyonu"""
        thread_id = threading.current_thread().ident
        zaman_yoneticisi.thread_zaman_kaydet(thread_id)
        
        print(f"Worker {worker_id} başladı (Thread ID: {thread_id})")
        
        for i in range(islem_sayisi):
            # İşlem simülasyonu
            baslangic = zaman_yoneticisi.islem_baslat(thread_id)
            
            # Rastgele süre bekle
            import random
            time.sleep(random.uniform(0.1, 0.5))
            
            sure = zaman_yoneticisi.islem_bitir(baslangic, thread_id)
            
            if i % 2 == 0:  # Her 2 işlemde bir rapor
                print(f"  Worker {worker_id} - İşlem {i+1}: {sure:.3f}s")
        
        print(f"Worker {worker_id} tamamlandı")
    
    # Çoklu thread test
    print("Çoklu thread performans testi başlatılıyor...")
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = []
        
        # 3 worker başlat
        for i in range(3):
            future = executor.submit(worker_function, i+1, 3)
            futures.append(future)
        
        # Tüm thread'lerin bitmesini bekle
        for future in futures:
            future.result()
    
    # İstatistikleri göster
    print(f"\n📊 Thread İstatistikleri:")
    stats = zaman_yoneticisi.thread_istatistikleri()
    
    for thread_id, stat in stats.items():
        ortalama = stat['toplam_sure'] / stat['islem_sayisi'] if stat['islem_sayisi'] > 0 else 0
        print(f"Thread {thread_id}:")
        print(f"  İşlem sayısı: {stat['islem_sayisi']}")
        print(f"  Toplam süre: {stat['toplam_sure']:.3f}s")
        print(f"  Ortalama süre: {ortalama:.3f}s")
    
    print(f"\n⏱️ Eş Zamanlı Zaman Ölçümü:")
    
    def es_zamanli_olcum():
        """Eş zamanlı zaman ölçümü örneği"""
        
        def task_with_timing(task_name, duration):
            """Zamanlı görev"""
            start_time = time.perf_counter()
            thread_id = threading.current_thread().name
            
            print(f"{task_name} başladı (Thread: {thread_id})")
            time.sleep(duration)
            
            end_time = time.perf_counter()
            elapsed = end_time - start_time
            
            print(f"{task_name} tamamlandı - Süre: {elapsed:.2f}s (Thread: {thread_id})")
            return elapsed
        
        # Farklı sürelerde görevler
        tasks = [
            ("Görev A", 1.0),
            ("Görev B", 1.5),
            ("Görev C", 0.8),
            ("Görev D", 1.2)
        ]
        
        # Seri çalıştırma
        print("Seri Çalıştırma:")
        seri_baslangic = time.perf_counter()
        
        for task_name, duration in tasks:
            task_with_timing(task_name, duration)
        
        seri_sure = time.perf_counter() - seri_baslangic
        print(f"Seri toplam süre: {seri_sure:.2f}s")
        
        print(f"\nParalel Çalıştırma:")
        
        # Paralel çalıştırma
        paralel_baslangic = time.perf_counter()
        
        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = [
                executor.submit(task_with_timing, task_name, duration)
                for task_name, duration in tasks
            ]
            
            # Tüm görevlerin bitmesini bekle
            for future in futures:
                future.result()
        
        paralel_sure = time.perf_counter() - paralel_baslangic
        print(f"Paralel toplam süre: {paralel_sure:.2f}s")
        
        speedup = seri_sure / paralel_sure
        print(f"Hızlanma oranı: {speedup:.1f}x")
    
    es_zamanli_olcum()

coklu_thread_zaman()

print("\n💡 Zaman Dilimi ve Senkronizasyon İpuçları:")
print("✅ UTC'yi veri saklama için temel zaman olarak kullanın")
print("✅ Kullanıcı arayüzlerinde yerel zaman gösterin")
print("✅ DST geçişlerini dikkate alın")
print("✅ Global uygulamalarda timezone-aware datetime kullanın")
print("✅ NTP ile sistem zamanını düzenli senkronize edin")
print("✅ Thread-safe zaman işlemleri yapın")
print("✅ Zaman farkı hesaplamalarında UTC kullanın")

print("\n⚠️ Dikkat Edilecek Noktalar:")
print("• DST geçişlerinde NonExistentTime ve AmbiguousTime hatalarına dikkat edin")
print("• Farklı sistemler arası zaman senkronizasyonunu göz önünde bulundurun")
print("• Network gecikmeleri zaman hesaplamalarını etkileyebilir")
print("• Thread-safe olmayan zaman işlemleri race condition'a neden olabilir")
print("• Kullanıcı timezone tercihlerini güvenli saklayın")

print("\n✅ Python zaman dilimi yönetimi öğrenildi!")
print("✅ DST geçişleri ve sorunları öğrenildi!")
print("✅ Global zaman koordinasyonu öğrenildi!")
print("✅ Zaman senkronizasyonu teknikleri öğrenildi!")
print("✅ Çoklu thread zaman yönetimi öğrenildi!")