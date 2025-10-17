"""
Python İleri Seviye Tarih ve Zaman İşlemleri

Bu dosya Python'da ileri seviye tarih ve zaman işlemlerini kapsar.
Relativedelta, timezone hesaplamaları, tarih parsing, 
iş günleri hesaplamaları ve özel takvim sistemlerini öğreneceğiz.
"""

import datetime
import calendar
from dateutil import parser, relativedelta, rrule
from dateutil.tz import tzlocal, gettz
import pytz
import locale
from collections import defaultdict
import json

# =============================================================================
# 1. RELATIVEDELTA İLE GELİŞMİŞ TARİH HESAPLAMalari
# =============================================================================

print("=== RelativeDelta ile Gelişmiş Tarih Hesaplamaları ===")

def relativedelta_ornekleri():
    """RelativeDelta ile gelişmiş tarih hesaplamaları"""
    
    print("🧮 RelativeDelta ile Gelişmiş İşlemler:")
    
    bugun = datetime.date.today()
    simdi = datetime.datetime.now()
    
    print(f"Bugün: {bugun}")
    
    # Basit relativedelta işlemleri
    bir_ay_sonra = bugun + relativedelta.relativedelta(months=1)
    uc_ay_once = bugun - relativedelta.relativedelta(months=3)
    bir_yil_sonra = bugun + relativedelta.relativedelta(years=1)
    
    print(f"1 ay sonra: {bir_ay_sonra}")
    print(f"3 ay önce: {uc_ay_once}")
    print(f"1 yıl sonra: {bir_yil_sonra}")
    
    # Karmaşık hesaplamalar
    karmasik = bugun + relativedelta.relativedelta(
        years=2, 
        months=3, 
        days=10, 
        hours=5, 
        minutes=30
    )
    print(f"Karmaşık hesaplama: {karmasik}")
    
    # Belirli güne ayarlama
    ayın_sonu = bugun + relativedelta.relativedelta(day=31)
    ayın_basi = bugun + relativedelta.relativedelta(day=1)
    yilin_sonu = bugun + relativedelta.relativedelta(month=12, day=31)
    
    print(f"Ayın sonu: {ayın_sonu}")
    print(f"Ayın başı: {ayın_basi}")
    print(f"Yılın sonu: {yilin_sonu}")
    
    print(f"\n📊 Yaş Hesaplamaları:")
    
    def detayli_yas_hesapla(dogum_tarihi):
        """Detaylı yaş hesaplaması"""
        bugun = datetime.date.today()
        
        # relativedelta ile hassas yaş hesaplama
        yas_delta = relativedelta.relativedelta(bugun, dogum_tarihi)
        
        # Bir sonraki doğum günü
        gelecek_yil = bugun.year if bugun.month < dogum_tarihi.month or \
                     (bugun.month == dogum_tarihi.month and bugun.day < dogum_tarihi.day) \
                     else bugun.year + 1
        
        try:
            next_birthday = dogum_tarihi.replace(year=gelecek_yil)
        except ValueError:  # 29 Şubat durumu
            next_birthday = dogum_tarihi.replace(year=gelecek_yil, day=28)
        
        kalan_delta = relativedelta.relativedelta(next_birthday, bugun)
        
        return {
            'yil': yas_delta.years,
            'ay': yas_delta.months,
            'gun': yas_delta.days,
            'dogum_gunune_kalan': {
                'ay': kalan_delta.months,
                'gun': kalan_delta.days
            },
            'toplam_gun': (bugun - dogum_tarihi).days,
            'toplam_ay': yas_delta.years * 12 + yas_delta.months
        }
    
    # Örnek yaş hesaplama
    dogum_tarihi = datetime.date(1990, 6, 15)
    yas_detay = detayli_yas_hesapla(dogum_tarihi)
    
    print(f"Doğum tarihi: {dogum_tarihi}")
    print(f"Yaş: {yas_detay['yil']} yıl, {yas_detay['ay']} ay, {yas_detay['gun']} gün")
    print(f"Doğum gününe kalan: {yas_detay['dogum_gunune_kalan']['ay']} ay, {yas_detay['dogum_gunune_kalan']['gun']} gün")
    print(f"Toplam: {yas_detay['toplam_gun']:,} gün, {yas_detay['toplam_ay']} ay")
    
    print(f"\n📈 Dönemsel Hesaplamalar:")
    
    def ceyrek_hesapla(tarih):
        """Çeyrek dönem hesaplama"""
        ceyrek = (tarih.month - 1) // 3 + 1
        ceyrek_baslangic = datetime.date(tarih.year, (ceyrek - 1) * 3 + 1, 1)
        
        # Çeyrek sonu
        if ceyrek < 4:
            ceyrek_sonu = datetime.date(tarih.year, ceyrek * 3 + 1, 1) - datetime.timedelta(days=1)
        else:
            ceyrek_sonu = datetime.date(tarih.year, 12, 31)
        
        return {
            'ceyrek': ceyrek,
            'baslangic': ceyrek_baslangic,
            'bitis': ceyrek_sonu,
            'gun_sayisi': (ceyrek_sonu - ceyrek_baslangic).days + 1
        }
    
    ceyrek_info = ceyrek_hesapla(bugun)
    print(f"Bu çeyrek: Q{ceyrek_info['ceyrek']} ({ceyrek_info['baslangic']} - {ceyrek_info['bitis']})")
    print(f"Çeyrek gün sayısı: {ceyrek_info['gun_sayisi']}")

relativedelta_ornekleri()

# =============================================================================
# 2. İŞ GÜNLERİ VE TAKVİM HESAPLAMAlari
# =============================================================================

print("\n=== İş Günleri ve Takvim Hesaplamaları ===")

def is_gunleri_hesaplamalari():
    """İş günleri ve takvim hesaplamaları"""
    
    print("💼 İş Günleri Hesaplamaları:")
    
    def is_gunu_ekle(tarih, is_gun_sayisi):
        """Belirtilen iş günü kadar ilerlet"""
        current = tarih
        added_days = 0
        
        while added_days < is_gun_sayisi:
            current += datetime.timedelta(days=1)
            # Pazartesi=0, Pazar=6
            if current.weekday() < 5:  # Pazartesi-Cuma
                added_days += 1
        
        return current
    
    def is_gunu_cikar(tarih, is_gun_sayisi):
        """Belirtilen iş günü kadar geri git"""
        current = tarih
        subtracted_days = 0
        
        while subtracted_days < is_gun_sayisi:
            current -= datetime.timedelta(days=1)
            if current.weekday() < 5:
                subtracted_days += 1
        
        return current
    
    def is_gunleri_sayisi(baslangic, bitis):
        """İki tarih arası iş günü sayısı"""
        if baslangic > bitis:
            baslangic, bitis = bitis, baslangic
        
        is_gunleri = 0
        current = baslangic
        
        while current <= bitis:
            if current.weekday() < 5:
                is_gunleri += 1
            current += datetime.timedelta(days=1)
        
        return is_gunleri
    
    # Örnekler
    bugun = datetime.date.today()
    print(f"Bugün: {bugun}")
    
    bes_is_gunu_sonra = is_gunu_ekle(bugun, 5)
    uc_is_gunu_once = is_gunu_cikar(bugun, 3)
    
    print(f"5 iş günü sonra: {bes_is_gunu_sonra}")
    print(f"3 iş günü önce: {uc_is_gunu_once}")
    
    # İki tarih arası iş günleri
    proje_baslangic = datetime.date(2024, 3, 1)
    proje_bitis = datetime.date(2024, 3, 31)
    is_gun_sayisi = is_gunleri_sayisi(proje_baslangic, proje_bitis)
    
    print(f"\n📊 Proje Süresi Analizi:")
    print(f"Başlangıç: {proje_baslangic} ({['Pzt','Sal','Çar','Per','Cum','Cmt','Paz'][proje_baslangic.weekday()]})")
    print(f"Bitiş: {proje_bitis} ({['Pzt','Sal','Çar','Per','Cum','Cmt','Paz'][proje_bitis.weekday()]})")
    print(f"Toplam gün: {(proje_bitis - proje_baslangic).days + 1}")
    print(f"İş günü: {is_gun_sayisi}")
    print(f"Hafta sonu: {(proje_bitis - proje_baslangic).days + 1 - is_gun_sayisi}")
    
    print(f"\n🏖️ Tatil Günleri Yönetimi:")
    
    class TatilTakvimi:
        """Tatil günleri yönetim sınıfı"""
        
        def __init__(self):
            self.sabit_tatiller = {}
            self.hareketli_tatiller = {}
            self.ozel_tatiller = set()
        
        def sabit_tatil_ekle(self, ay, gun, aciklama):
            """Sabit tatil günü ekle"""
            self.sabit_tatiller[(ay, gun)] = aciklama
        
        def ozel_tatil_ekle(self, tarih, aciklama):
            """Özel tatil günü ekle"""
            self.ozel_tatiller.add((tarih, aciklama))
        
        def tatil_mi(self, tarih):
            """Belirtilen tarih tatil mi?"""
            # Hafta sonu kontrolü
            if tarih.weekday() >= 5:
                return True, "Hafta sonu"
            
            # Sabit tatil kontrolü
            if (tarih.month, tarih.day) in self.sabit_tatiller:
                return True, self.sabit_tatiller[(tarih.month, tarih.day)]
            
            # Özel tatil kontrolü
            for tatil_tarih, aciklama in self.ozel_tatiller:
                if tarih == tatil_tarih:
                    return True, aciklama
            
            return False, "İş günü"
        
        def calisma_gunleri_sayisi(self, baslangic, bitis):
            """Tatiller hariç çalışma günü sayısı"""
            sayac = 0
            current = baslangic
            
            while current <= bitis:
                is_tatil, _ = self.tatil_mi(current)
                if not is_tatil:
                    sayac += 1
                current += datetime.timedelta(days=1)
            
            return sayac
    
    # Türkiye tatil takvimi
    tr_takvim = TatilTakvimi()
    
    # Sabit tatiller
    tr_takvim.sabit_tatil_ekle(1, 1, "Yılbaşı")
    tr_takvim.sabit_tatil_ekle(4, 23, "Ulusal Egemenlik ve Çocuk Bayramı")
    tr_takvim.sabit_tatil_ekle(5, 1, "İşçi Bayramı")
    tr_takvim.sabit_tatil_ekle(5, 19, "Gençlik ve Spor Bayramı")
    tr_takvim.sabit_tatil_ekle(8, 30, "Zafer Bayramı")
    tr_takvim.sabit_tatil_ekle(10, 29, "Cumhuriyet Bayramı")
    
    # Özel tatiller (şirket tatilleri)
    tr_takvim.ozel_tatil_ekle(datetime.date(2024, 12, 24), "Noel Arifesi (Şirket Tatili)")
    tr_takvim.ozel_tatil_ekle(datetime.date(2024, 12, 31), "Yılbaşı Arifesi (Şirket Tatili)")
    
    # Test
    test_tarihleri = [
        datetime.date(2024, 1, 1),   # Yılbaşı
        datetime.date(2024, 4, 23),  # 23 Nisan
        datetime.date(2024, 5, 18),  # Cumartesi
        datetime.date(2024, 5, 20),  # Normal iş günü
    ]
    
    print("Tatil kontrolü:")
    for tarih in test_tarihleri:
        is_tatil, aciklama = tr_takvim.tatil_mi(tarih)
        status = "🏖️" if is_tatil else "💼"
        gun = ['Pzt','Sal','Çar','Per','Cum','Cmt','Paz'][tarih.weekday()]
        print(f"{status} {tarih} ({gun}): {aciklama}")
    
    # Aylık çalışma günü hesaplama
    mart_calisma = tr_takvim.calisma_gunleri_sayisi(
        datetime.date(2024, 3, 1),
        datetime.date(2024, 3, 31)
    )
    print(f"\nMart 2024 çalışma günü: {mart_calisma}")

is_gunleri_hesaplamalari()

# =============================================================================
# 3. RECURRING DATES VE PERIYODIK OLAYLAR
# =============================================================================

print("\n=== Recurring Dates ve Periyodik Olaylar ===")

def periyodik_olaylar():
    """Periyodik olaylar ve tekrarlayan tarihler"""
    
    print("🔄 Periyodik Olaylar (dateutil.rrule):")
    
    # Temel recurring rules
    baslangic = datetime.date(2024, 1, 1)
    
    # Günlük tekrar
    gunluk = list(rrule.rrule(
        rrule.DAILY,
        dtstart=baslangic,
        count=5  # İlk 5 gün
    ))
    
    print("Günlük tekrar (5 gün):")
    for tarih in gunluk:
        print(f"  {tarih.date()}")
    
    # Haftalık tekrar (pazartesi)
    haftalik = list(rrule.rrule(
        rrule.WEEKLY,
        dtstart=baslangic,
        byweekday=rrule.MO,  # Pazartesi
        count=4
    ))
    
    print(f"\nHaftalık tekrar (Pazartesi, 4 hafta):")
    for tarih in haftalik:
        print(f"  {tarih.date()} (Pazartesi)")
    
    # Aylık tekrar (ayın 15'i)
    aylik = list(rrule.rrule(
        rrule.MONTHLY,
        dtstart=datetime.date(2024, 1, 15),
        count=6
    ))
    
    print(f"\nAylık tekrar (ayın 15'i, 6 ay):")
    for tarih in aylik:
        print(f"  {tarih.date()}")
    
    # Karmaşık kurallar
    print(f"\n🎯 Karmaşık Recurring Rules:")
    
    # Her ayın 2. pazartesi
    ikinci_pazartesi = list(rrule.rrule(
        rrule.MONTHLY,
        dtstart=datetime.date(2024, 1, 1),
        byweekday=rrule.MO(2),  # 2. pazartesi
        count=12
    ))
    
    print("Her ayın 2. pazartesi (12 ay):")
    for tarih in ikinci_pazartesi:
        print(f"  {tarih.date()}")
    
    # İş günleri (pazartesi-cuma)
    is_gunleri = list(rrule.rrule(
        rrule.WEEKLY,
        dtstart=datetime.date(2024, 3, 4),  # Pazartesi
        byweekday=(rrule.MO, rrule.TU, rrule.WE, rrule.TH, rrule.FR),
        count=10  # 10 iş günü
    ))
    
    print(f"\nİş günleri (10 gün):")
    for tarih in is_gunleri:
        gun_adi = ['Pzt','Sal','Çar','Per','Cum','Cmt','Paz'][tarih.weekday()]
        print(f"  {tarih.date()} ({gun_adi})")
    
    # Çeyrek dönem toplantıları (her 3 ayda bir, ayın ilk pazartesi)
    ceyrek_toplantilar = list(rrule.rrule(
        rrule.MONTHLY,
        dtstart=datetime.date(2024, 1, 1),
        interval=3,  # Her 3 ayda bir
        byweekday=rrule.MO(1),  # İlk pazartesi
        count=4
    ))
    
    print(f"\nÇeyrek toplantılar (ayın ilk pazartesi):")
    for tarih in ceyrek_toplantilar:
        print(f"  {tarih.date()}")
    
    print(f"\n📊 Periyodik Olay Yöneticisi:")
    
    class PeriyodikOlayYoneticisi:
        """Periyodik olayları yöneten sınıf"""
        
        def __init__(self):
            self.olaylar = []
        
        def olay_ekle(self, ad, rrule_obj, aciklama=""):
            """Periyodik olay ekle"""
            self.olaylar.append({
                'ad': ad,
                'rule': rrule_obj,
                'aciklama': aciklama
            })
        
        def gelecek_olaylar(self, gun_sayisi=30):
            """Gelecek N gün içindeki olaylar"""
            bugun = datetime.date.today()
            bitis = bugun + datetime.timedelta(days=gun_sayisi)
            
            olaylar = []
            
            for olay in self.olaylar:
                olay_tarihleri = olay['rule'].between(
                    datetime.datetime.combine(bugun, datetime.time.min),
                    datetime.datetime.combine(bitis, datetime.time.max),
                    inc=True
                )
                
                for tarih in olay_tarihleri:
                    olaylar.append({
                        'tarih': tarih.date(),
                        'ad': olay['ad'],
                        'aciklama': olay['aciklama']
                    })
            
            # Tarihe göre sırala
            olaylar.sort(key=lambda x: x['tarih'])
            return olaylar
    
    # Örnek periyodik olaylar
    yonetici = PeriyodikOlayYoneticisi()
    
    # Haftalık toplantı (her pazartesi)
    haftalik_toplanti = rrule.rrule(
        rrule.WEEKLY,
        dtstart=datetime.datetime.now(),
        byweekday=rrule.MO
    )
    yonetici.olay_ekle("Haftalık Toplantı", haftalik_toplanti, "Takım toplantısı")
    
    # Aylık rapor (ayın son cuma)
    aylik_rapor = rrule.rrule(
        rrule.MONTHLY,
        dtstart=datetime.datetime.now(),
        byweekday=rrule.FR(-1)  # Son cuma
    )
    yonetici.olay_ekle("Aylık Rapor", aylik_rapor, "Performans raporu hazırlama")
    
    # Çeyrek değerlendirme
    ceyrek_degerlendirme = rrule.rrule(
        rrule.MONTHLY,
        dtstart=datetime.datetime.now(),
        interval=3,
        bymonthday=15
    )
    yonetici.olay_ekle("Çeyrek Değerlendirme", ceyrek_degerlendirme, "Performans değerlendirmesi")
    
    gelecek_olaylar = yonetici.gelecek_olaylar(30)
    
    print(f"Gelecek 30 gün içindeki olaylar:")
    for olay in gelecek_olaylar:
        gun = ['Pzt','Sal','Çar','Per','Cum','Cmt','Paz'][olay['tarih'].weekday()]
        print(f"  {olay['tarih']} ({gun}): {olay['ad']} - {olay['aciklama']}")

periyodik_olaylar()

# =============================================================================
# 4. AKILLI TARİH PARSING VE DOĞAL DİL İŞLEME
# =============================================================================

print("\n=== Akıllı Tarih Parsing ve Doğal Dil İşleme ===")

def akilli_tarih_parsing():
    """Akıllı tarih parsing ve doğal dil işleme"""
    
    print("🧠 Akıllı Tarih Parsing (dateutil.parser):")
    
    # Çeşitli formatlarda tarih string'leri
    tarih_strings = [
        "2024-03-15",
        "15/03/2024",
        "March 15, 2024",
        "15 Mar 2024",
        "2024-03-15T14:30:45",
        "15.03.2024 14:30",
        "March 15th, 2024 2:30 PM",
        "today",
        "tomorrow",
        "next monday",
        "in 2 weeks",
        "3 days ago"
    ]
    
    print("Çeşitli format parsing:")
    for tarih_str in tarih_strings[:7]:  # İlk 7'si parse edilebilir
        try:
            parsed = parser.parse(tarih_str)
            print(f"'{tarih_str}' -> {parsed}")
        except (ValueError, parser.ParserError) as e:
            print(f"'{tarih_str}' -> Hata: {e}")
    
    print(f"\n🔤 Doğal Dil Tarih İşleme:")
    
    class DoğalDilTarih:
        """Doğal dil tarih işlemcisi"""
        
        def __init__(self):
            self.bugun = datetime.date.today()
            self.simdi = datetime.datetime.now()
        
        def parse_dogal_dil(self, metin):
            """Doğal dil metni tarih olarak parse et"""
            metin = metin.lower().strip()
            
            # Bugün, yarın, dün
            if metin in ['bugün', 'today']:
                return self.bugun
            elif metin in ['yarın', 'tomorrow']:
                return self.bugun + datetime.timedelta(days=1)
            elif metin in ['dün', 'yesterday']:
                return self.bugun - datetime.timedelta(days=1)
            
            # Gelecek/geçmiş hafta
            elif 'gelecek hafta' in metin or 'next week' in metin:
                return self.bugun + datetime.timedelta(weeks=1)
            elif 'geçen hafta' in metin or 'last week' in metin:
                return self.bugun - datetime.timedelta(weeks=1)
            
            # Sayısal ifadeler
            elif 'gün sonra' in metin or 'days from now' in metin:
                import re
                match = re.search(r'(\d+)', metin)
                if match:
                    gun_sayisi = int(match.group(1))
                    return self.bugun + datetime.timedelta(days=gun_sayisi)
            
            elif 'gün önce' in metin or 'days ago' in metin:
                import re
                match = re.search(r'(\d+)', metin)
                if match:
                    gun_sayisi = int(match.group(1))
                    return self.bugun - datetime.timedelta(days=gun_sayisi)
            
            # Ay isimleri
            elif 'ocak' in metin:
                return datetime.date(self.bugun.year, 1, 1)
            elif 'şubat' in metin:
                return datetime.date(self.bugun.year, 2, 1)
            # ... diğer aylar
            
            # Standart parsing'e geri dön
            try:
                return parser.parse(metin).date()
            except:
                return None
        
        def relative_tarih_aci(self, tarih):
            """Tarihin bugüne göre açıklaması"""
            if isinstance(tarih, str):
                tarih = self.parse_dogal_dil(tarih)
            
            if tarih is None:
                return "Geçersiz tarih"
            
            fark = (tarih - self.bugun).days
            
            if fark == 0:
                return "Bugün"
            elif fark == 1:
                return "Yarın"
            elif fark == -1:
                return "Dün"
            elif fark > 0:
                if fark < 7:
                    return f"{fark} gün sonra"
                elif fark < 30:
                    hafta = fark // 7
                    return f"{hafta} hafta sonra"
                else:
                    ay = fark // 30
                    return f"{ay} ay sonra"
            else:
                fark = abs(fark)
                if fark < 7:
                    return f"{fark} gün önce"
                elif fark < 30:
                    hafta = fark // 7
                    return f"{hafta} hafta önce"
                else:
                    ay = fark // 30
                    return f"{ay} ay önce"
    
    # Doğal dil parsing testi
    dogal_parser = DoğalDilTarih()
    
    dogal_ifadeler = [
        "bugün",
        "yarın", 
        "dün",
        "5 gün sonra",
        "3 gün önce",
        "gelecek hafta",
        "2024-06-15"
    ]
    
    print("Doğal dil parsing:")
    for ifade in dogal_ifadeler:
        parsed_tarih = dogal_parser.parse_dogal_dil(ifade)
        relative_aci = dogal_parser.relative_tarih_aci(parsed_tarih)
        print(f"'{ifade}' -> {parsed_tarih} ({relative_aci})")
    
    print(f"\n📅 Akıllı Tarih Formatter:")
    
    class AkilliTarihFormatter:
        """Akıllı tarih formatlandırıcı"""
        
        @staticmethod
        def format_user_friendly(tarih):
            """Kullanıcı dostu tarih formatı"""
            if isinstance(tarih, str):
                tarih = parser.parse(tarih)
            
            bugun = datetime.date.today()
            if isinstance(tarih, datetime.datetime):
                tarih_date = tarih.date()
            else:
                tarih_date = tarih
            
            fark = (tarih_date - bugun).days
            
            # Yakın tarihler için özel format
            if fark == 0:
                if isinstance(tarih, datetime.datetime):
                    return f"Bugün {tarih.strftime('%H:%M')}"
                return "Bugün"
            elif fark == 1:
                if isinstance(tarih, datetime.datetime):
                    return f"Yarın {tarih.strftime('%H:%M')}"
                return "Yarın"
            elif fark == -1:
                if isinstance(tarih, datetime.datetime):
                    return f"Dün {tarih.strftime('%H:%M')}"
                return "Dün"
            elif 0 < fark <= 7:
                gun_adi = ['Pazartesi','Salı','Çarşamba','Perşembe','Cuma','Cumartesi','Pazar'][tarih_date.weekday()]
                if isinstance(tarih, datetime.datetime):
                    return f"{gun_adi} {tarih.strftime('%H:%M')}"
                return gun_adi
            else:
                # Uzak tarihler için standart format
                if isinstance(tarih, datetime.datetime):
                    return tarih.strftime("%d.%m.%Y %H:%M")
                return tarih_date.strftime("%d.%m.%Y")
        
        @staticmethod
        def format_iş_baglami(tarih):
            """İş bağlamında tarih formatı"""
            bugun = datetime.date.today()
            if isinstance(tarih, datetime.datetime):
                tarih_date = tarih.date()
            else:
                tarih_date = tarih
            
            # Haftanın günü
            gun_adi = ['Pzt','Sal','Çar','Per','Cum','Cmt','Paz'][tarih_date.weekday()]
            
            # Bu hafta/gelecek hafta/geçen hafta
            hafta_farki = (tarih_date - bugun).days // 7
            
            if hafta_farki == 0:
                prefix = "Bu hafta"
            elif hafta_farki == 1:
                prefix = "Gelecek hafta"
            elif hafta_farki == -1:
                prefix = "Geçen hafta"
            else:
                return tarih_date.strftime("%d.%m.%Y")
            
            return f"{prefix} {gun_adi} ({tarih_date.strftime('%d.%m')})"
    
    # Test formatları
    test_tarihleri = [
        datetime.date.today(),
        datetime.date.today() + datetime.timedelta(days=1),
        datetime.date.today() + datetime.timedelta(days=3),
        datetime.date.today() + datetime.timedelta(days=10),
        datetime.datetime.now() + datetime.timedelta(hours=2)
    ]
    
    print("Akıllı formatlar:")
    for tarih in test_tarihleri:
        user_friendly = AkilliTarihFormatter.format_user_friendly(tarih)
        is_baglami = AkilliTarihFormatter.format_iş_baglami(tarih)
        print(f"{tarih} -> UF: {user_friendly}, İş: {is_baglami}")

akilli_tarih_parsing()

# =============================================================================
# 5. TARİH VERİ ANALİZİ VE RAPORLAMA
# =============================================================================

print("\n=== Tarih Veri Analizi ve Raporlama ===")

def tarih_veri_analizi():
    """Tarih veri analizi ve raporlama"""
    
    print("📊 Tarih Veri Analizi:")
    
    # Örnek veri seti
    import random
    
    def örnek_veri_üret():
        """Örnek tarih verisi üret"""
        veriler = []
        baslangic = datetime.date(2024, 1, 1)
        
        for i in range(100):
            # Rastgele tarih (2024 yılı içinde)
            rastgele_gun = random.randint(0, 365)
            tarih = baslangic + datetime.timedelta(days=rastgele_gun)
            
            # Rastgele değer
            deger = random.randint(100, 1000)
            
            veriler.append({
                'tarih': tarih,
                'deger': deger,
                'kategori': random.choice(['A', 'B', 'C'])
            })
        
        return veriler
    
    veri_seti = örnek_veri_üret()
    
    print(f"Örnek veri seti: {len(veri_seti)} kayıt")
    
    # Tarih bazlı gruplama
    class TarihAnalizi:
        """Tarih analiz araçları"""
        
        @staticmethod
        def aylik_gruplama(veriler):
            """Verileri aylık grupla"""
            aylik_grup = defaultdict(list)
            
            for veri in veriler:
                ay_anahtari = (veri['tarih'].year, veri['tarih'].month)
                aylik_grup[ay_anahtari].append(veri)
            
            return dict(aylik_grup)
        
        @staticmethod
        def haftalik_gruplama(veriler):
            """Verileri haftalık grupla"""
            haftalik_grup = defaultdict(list)
            
            for veri in veriler:
                # Haftanın başlangıcı (pazartesi)
                hafta_baslangici = veri['tarih'] - datetime.timedelta(days=veri['tarih'].weekday())
                haftalik_grup[hafta_baslangici].append(veri)
            
            return dict(haftalik_grup)
        
        @staticmethod
        def gun_bazli_analiz(veriler):
            """Haftanın günlerine göre analiz"""
            gun_analizi = defaultdict(list)
            
            for veri in veriler:
                gun_adi = ['Pazartesi','Salı','Çarşamba','Perşembe','Cuma','Cumartesi','Pazar'][veri['tarih'].weekday()]
                gun_analizi[gun_adi].append(veri['deger'])
            
            # İstatistikler hesapla
            sonuclar = {}
            for gun, degerler in gun_analizi.items():
                sonuclar[gun] = {
                    'sayim': len(degerler),
                    'toplam': sum(degerler),
                    'ortalama': sum(degerler) / len(degerler) if degerler else 0,
                    'min': min(degerler) if degerler else 0,
                    'max': max(degerler) if degerler else 0
                }
            
            return sonuclar
        
        @staticmethod
        def mevsim_analizi(veriler):
            """Mevsimsel analiz"""
            def mevsim_bul(tarih):
                ay = tarih.month
                if ay in [12, 1, 2]:
                    return "Kış"
                elif ay in [3, 4, 5]:
                    return "İlkbahar"
                elif ay in [6, 7, 8]:
                    return "Yaz"
                else:
                    return "Sonbahar"
            
            mevsim_grup = defaultdict(list)
            
            for veri in veriler:
                mevsim = mevsim_bul(veri['tarih'])
                mevsim_grup[mevsim].append(veri['deger'])
            
            # İstatistikler
            sonuclar = {}
            for mevsim, degerler in mevsim_grup.items():
                sonuclar[mevsim] = {
                    'sayim': len(degerler),
                    'ortalama': sum(degerler) / len(degerler) if degerler else 0
                }
            
            return sonuclar
    
    # Analizleri çalıştır
    aylik_grup = TarihAnalizi.aylik_gruplama(veri_seti)
    gun_analizi = TarihAnalizi.gun_bazli_analiz(veri_seti)
    mevsim_analizi = TarihAnalizi.mevsim_analizi(veri_seti)
    
    print(f"\n📅 Aylık Veri Dağılımı:")
    for (yil, ay), veriler in sorted(aylik_grup.items()):
        ay_adi = ['', 'Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran',
                  'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık'][ay]
        toplam = sum(v['deger'] for v in veriler)
        ortalama = toplam / len(veriler)
        print(f"{ay_adi} {yil}: {len(veriler)} kayıt, Toplam: {toplam}, Ortalama: {ortalama:.1f}")
    
    print(f"\n📊 Günlük Analiz:")
    for gun, stats in gun_analizi.items():
        print(f"{gun:10}: {stats['sayim']:3d} kayıt, Ort: {stats['ortalama']:6.1f}")
    
    print(f"\n🌍 Mevsimsel Analiz:")
    for mevsim, stats in mevsim_analizi.items():
        print(f"{mevsim:10}: {stats['sayim']} kayıt, Ortalama: {stats['ortalama']:.1f}")
    
    print(f"\n📈 Tarih Bazlı Raporlama:")
    
    class TarihRaporlayici:
        """Tarih bazlı rapor oluşturucu"""
        
        @staticmethod
        def trend_analizi(veriler, period='monthly'):
            """Trend analizi"""
            if period == 'monthly':
                gruplar = TarihAnalizi.aylik_gruplama(veriler)
                sorted_keys = sorted(gruplar.keys())
                
                print("Aylık Trend:")
                onceki_ortalama = None
                
                for key in sorted_keys:
                    yil, ay = key
                    ay_adi = ['', 'Oca', 'Şub', 'Mar', 'Nis', 'May', 'Haz',
                              'Tem', 'Ağu', 'Eyl', 'Eki', 'Kas', 'Ara'][ay]
                    
                    degerler = [v['deger'] for v in gruplar[key]]
                    ortalama = sum(degerler) / len(degerler)
                    
                    if onceki_ortalama is not None:
                        degisim = ((ortalama - onceki_ortalama) / onceki_ortalama) * 100
                        trend = "📈" if degisim > 0 else "📉" if degisim < 0 else "➡️"
                        print(f"  {ay_adi} {yil}: {ortalama:6.1f} {trend} ({degisim:+.1f}%)")
                    else:
                        print(f"  {ay_adi} {yil}: {ortalama:6.1f}")
                    
                    onceki_ortalama = ortalama
        
        @staticmethod
        def özet_rapor(veriler):
            """Özet rapor oluştur"""
            if not veriler:
                return "Veri yok"
            
            # Tarih aralığı
            min_tarih = min(v['tarih'] for v in veriler)
            max_tarih = max(v['tarih'] for v in veriler)
            
            # İstatistikler
            degerler = [v['deger'] for v in veriler]
            
            rapor = f"""
📊 VERİ ANALİZİ RAPORU
{'=' * 50}

📅 Tarih Aralığı: {min_tarih} - {max_tarih}
📈 Toplam Kayıt: {len(veriler):,}
📊 Veri Aralığı: {(max_tarih - min_tarih).days} gün

💹 İSTATİSTİKLER
Toplam Değer: {sum(degerler):,}
Ortalama: {sum(degerler)/len(degerler):,.2f}
Minimum: {min(degerler):,}
Maksimum: {max(degerler):,}

📅 GÜNLÜK ANALİZ
"""
            
            gun_stats = TarihAnalizi.gun_bazli_analiz(veriler)
            for gun, stats in gun_stats.items():
                rapor += f"{gun:10}: {stats['sayim']:3d} kayıt (Ort: {stats['ortalama']:6.1f})\n"
            
            return rapor
    
    # Raporları oluştur
    TarihRaporlayici.trend_analizi(veri_seti)
    
    print(TarihRaporlayici.özet_rapor(veri_seti))

tarih_veri_analizi()

print("\n💡 İleri Seviye Tarih İşlemleri İpuçları:")
print("✅ relativedelta ile hassas tarih hesaplamaları yapın")
print("✅ dateutil.rrule ile periyodik olayları yönetin")
print("✅ İş günü hesaplamalarında tatilleri göz önünde bulundurun")
print("✅ Doğal dil parsing ile user-friendly arayüzler oluşturun")
print("✅ Tarih bazlı veri analizi ile trendleri takip edin")
print("✅ Timezone-aware datetime kullanın")
print("✅ Performance için tarih hesaplamalarını cache'leyin")

print("\n⚠️ Dikkat Edilecek Noktalar:")
print("• Artık yıl hesaplamalarında relativedelta kullanın")
print("• Farklı takvim sistemlerini (hijri, vs.) göz önünde bulundurun")
print("• Kullanıcı girdilerini validate edin")
print("• Büyük veri setlerinde tarih işlemlerini optimize edin")
print("• DST (Daylight Saving Time) geçişlerini göz önünde bulundurun")

print("\n✅ Python ileri seviye tarih ve zaman işlemleri öğrenildi!")
print("✅ Periyodik olay yönetimi öğrenildi!")
print("✅ İş günü hesaplamaları öğrenildi!")
print("✅ Doğal dil tarih parsing öğrenildi!")
print("✅ Tarih veri analizi teknikleri öğrenildi!")