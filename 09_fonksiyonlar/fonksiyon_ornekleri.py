"""
Python Fonksiyon Örnekleri ve Uygulamaları

Bu dosya, Python fonksiyonlarının pratik kullanımını gösteren
kapsamlı örnekler içerir. Gerçek dünya problemlerini çözen
fonksiyonlar ve en iyi pratikleri öğreneceğiz.
"""

import math
import random
import time
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Union, Tuple
import json

# =============================================================================
# 1. TEMELİ KULLANILIŞLI FONKSİYONLAR
# =============================================================================

def hesap_makinesi(sayi1: float, sayi2: float, islem: str) -> float:
    """
    Basit hesap makinesi fonksiyonu
    
    Args:
        sayi1: İlk sayı
        sayi2: İkinci sayı
        islem: İşlem türü (+, -, *, /, **, %)
    
    Returns:
        İşlem sonucu
    
    Raises:
        ValueError: Geçersiz işlem için
        ZeroDivisionError: Sıfıra bölme için
    """
    islemler = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else None,
        '**': lambda x, y: x ** y,
        '%': lambda x, y: x % y if y != 0 else None
    }
    
    if islem not in islemler:
        raise ValueError(f"Desteklenmeyen işlem: {islem}")
    
    sonuc = islemler[islem](sayi1, sayi2)
    
    if sonuc is None:
        raise ZeroDivisionError("Sıfıra bölme hatası")
    
    return sonuc

print("=== Hesap Makinesi ===")
print(f"15 + 25 = {hesap_makinesi(15, 25, '+')}")
print(f"100 / 4 = {hesap_makinesi(100, 4, '/')}")
print(f"2 ** 8 = {hesap_makinesi(2, 8, '**')}")

def sicaklik_donusturucu(derece: float, kaynak: str, hedef: str) -> float:
    """
    Sıcaklık birimleri arası dönüşüm
    
    Args:
        derece: Dönüştürülecek sıcaklık değeri
        kaynak: Kaynak birim ('C', 'F', 'K')
        hedef: Hedef birim ('C', 'F', 'K')
    
    Returns:
        Dönüştürülmüş sıcaklık değeri
    """
    # Önce Celsius'a çevir
    if kaynak == 'F':
        celsius = (derece - 32) * 5/9
    elif kaynak == 'K':
        celsius = derece - 273.15
    else:  # 'C'
        celsius = derece
    
    # Sonra hedef birime çevir
    if hedef == 'F':
        return celsius * 9/5 + 32
    elif hedef == 'K':
        return celsius + 273.15
    else:  # 'C'
        return celsius

print("\n=== Sıcaklık Dönüştürücü ===")
print(f"100°C = {sicaklik_donusturucu(100, 'C', 'F'):.1f}°F")
print(f"32°F = {sicaklik_donusturucu(32, 'F', 'C'):.1f}°C")
print(f"0°C = {sicaklik_donusturucu(0, 'C', 'K'):.1f}K")

# =============================================================================
# 2. LİSTE VE STRING İŞLEMLERİ
# =============================================================================

def liste_istatistikleri(sayilar: List[Union[int, float]]) -> Dict[str, float]:
    """
    Sayı listesi için detaylı istatistikler hesaplar
    
    Args:
        sayilar: Sayı listesi
    
    Returns:
        İstatistik bilgileri içeren sözlük
    """
    if not sayilar:
        return {"error": "Boş liste"}
    
    n = len(sayilar)
    sirali_liste = sorted(sayilar)
    
    return {
        "toplam": sum(sayilar),
        "ortalama": sum(sayilar) / n,
        "medyan": sirali_liste[n//2] if n % 2 == 1 else (sirali_liste[n//2-1] + sirali_liste[n//2]) / 2,
        "minimum": min(sayilar),
        "maksimum": max(sayilar),
        "aralık": max(sayilar) - min(sayilar),
        "standart_sapma": (sum((x - sum(sayilar)/n)**2 for x in sayilar) / n) ** 0.5,
        "eleman_sayisi": n
    }

test_sayilar = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
istatistikler = liste_istatistikleri(test_sayilar)

print("\n=== Liste İstatistikleri ===")
for anahtar, deger in istatistikler.items():
    print(f"{anahtar.replace('_', ' ').title()}: {deger:.2f}")

def metin_analizi(metin: str) -> Dict[str, Union[int, float, List[str]]]:
    """
    Metin analizi yapan fonksiyon
    
    Args:
        metin: Analiz edilecek metin
    
    Returns:
        Metin analiz sonuçları
    """
    kelimeler = metin.lower().split()
    kelime_sayilari = {}
    
    for kelime in kelimeler:
        # Noktalama işaretlerini temizle
        temiz_kelime = ''.join(c for c in kelime if c.isalnum())
        if temiz_kelime:
            kelime_sayilari[temiz_kelime] = kelime_sayilari.get(temiz_kelime, 0) + 1
    
    # En sık kullanılan kelimeleri bul
    en_sik_kelimeler = sorted(kelime_sayilari.items(), key=lambda x: x[1], reverse=True)[:5]
    
    return {
        "karakter_sayisi": len(metin),
        "kelime_sayisi": len(kelimeler),
        "cumle_sayisi": metin.count('.') + metin.count('!') + metin.count('?'),
        "paragraf_sayisi": metin.count('\n\n') + 1,
        "benzersiz_kelime_sayisi": len(kelime_sayilari),
        "ortalama_kelime_uzunlugu": sum(len(k) for k in kelimeler) / len(kelimeler) if kelimeler else 0,
        "en_sik_kelimeler": [f"{kelime}: {sayi}" for kelime, sayi in en_sik_kelimeler]
    }

ornek_metin = """
Python çok güçlü bir programlama dilidir. Python öğrenmek kolaydır.
Python ile web geliştirme, veri analizi ve makine öğrenmesi yapabilirsiniz.
Python topluluğu çok aktiftir. Python açık kaynak kodludur.
"""

metin_sonuclari = metin_analizi(ornek_metin)
print("\n=== Metin Analizi ===")
for anahtar, deger in metin_sonuclari.items():
    if isinstance(deger, list):
        print(f"{anahtar.replace('_', ' ').title()}:")
        for item in deger:
            print(f"  {item}")
    else:
        print(f"{anahtar.replace('_', ' ').title()}: {deger}")

# =============================================================================
# 3. TARİH VE ZAMAN FONKSİYONLARI
# =============================================================================

def yas_hesapla(dogum_tarihi: str) -> Dict[str, int]:
    """
    Doğum tarihinden yaş hesaplar
    
    Args:
        dogum_tarihi: 'YYYY-MM-DD' formatında doğum tarihi
    
    Returns:
        Yaş bilgileri (yıl, ay, gün)
    """
    dogum = datetime.strptime(dogum_tarihi, '%Y-%m-%d')
    bugun = datetime.now()
    
    yas_yil = bugun.year - dogum.year
    yas_ay = bugun.month - dogum.month
    yas_gun = bugun.day - dogum.day
    
    # Negatif değerleri düzelt
    if yas_gun < 0:
        yas_ay -= 1
        # Önceki ayın son günü
        onceki_ay = bugun.replace(day=1) - timedelta(days=1)
        yas_gun += onceki_ay.day
    
    if yas_ay < 0:
        yas_yil -= 1
        yas_ay += 12
    
    toplam_gun = (bugun - dogum).days
    
    return {
        "yil": yas_yil,
        "ay": yas_ay,
        "gun": yas_gun,
        "toplam_gun": toplam_gun,
        "toplam_hafta": toplam_gun // 7
    }

def calisma_gunu_hesapla(baslangic: str, bitis: str) -> Dict[str, int]:
    """
    İki tarih arasındaki çalışma günlerini hesaplar
    
    Args:
        baslangic: 'YYYY-MM-DD' formatında başlangıç tarihi
        bitis: 'YYYY-MM-DD' formatında bitiş tarihi
    
    Returns:
        Çalışma günü bilgileri
    """
    baslangic_tarih = datetime.strptime(baslangic, '%Y-%m-%d')
    bitis_tarih = datetime.strptime(bitis, '%Y-%m-%d')
    
    toplam_gun = 0
    calisma_gunu = 0
    hafta_sonu = 0
    
    current_date = baslangic_tarih
    while current_date <= bitis_tarih:
        toplam_gun += 1
        # 0=Pazartesi, 6=Pazar
        if current_date.weekday() < 5:  # Pazartesi-Cuma
            calisma_gunu += 1
        else:
            hafta_sonu += 1
        current_date += timedelta(days=1)
    
    return {
        "toplam_gun": toplam_gun,
        "calisma_gunu": calisma_gunu,
        "hafta_sonu": hafta_sonu,
        "hafta_sayisi": toplam_gun // 7
    }

print("\n=== Tarih Hesaplamaları ===")
yas_bilgisi = yas_hesapla("1990-05-15")
print(f"Yaş: {yas_bilgisi['yil']} yıl, {yas_bilgisi['ay']} ay, {yas_bilgisi['gun']} gün")
print(f"Toplam: {yas_bilgisi['toplam_gun']} gün ({yas_bilgisi['toplam_hafta']} hafta)")

calisma_bilgisi = calisma_gunu_hesapla("2024-01-01", "2024-12-31")
print(f"\n2024 yılı çalışma günleri: {calisma_bilgisi['calisma_gunu']}")
print(f"Hafta sonu günleri: {calisma_bilgisi['hafta_sonu']}")

# =============================================================================
# 4. DOSYA VE VERİ İŞLEMLERİ
# =============================================================================

def csv_oku_analiz_et(veri_listesi: List[Dict[str, str]]) -> Dict[str, any]:
    """
    CSV benzeri veri listesini analiz eder
    
    Args:
        veri_listesi: Sözlük listesi (her sözlük bir satır)
    
    Returns:
        Veri analiz sonuçları
    """
    if not veri_listesi:
        return {"error": "Boş veri"}
    
    # Sütun isimleri
    sutunlar = list(veri_listesi[0].keys())
    satir_sayisi = len(veri_listesi)
    
    # Sayısal sütunları belirle ve analiz et
    sayisal_analizler = {}
    
    for sutun in sutunlar:
        degerler = [satir[sutun] for satir in veri_listesi if satir[sutun]]
        
        # Sayısal değerleri kontrol et
        sayisal_degerler = []
        for deger in degerler:
            try:
                sayisal_degerler.append(float(deger))
            except ValueError:
                continue
        
        if sayisal_degerler:
            sayisal_analizler[sutun] = {
                "ortalama": sum(sayisal_degerler) / len(sayisal_degerler),
                "minimum": min(sayisal_degerler),
                "maksimum": max(sayisal_degerler),
                "toplam": sum(sayisal_degerler)
            }
    
    return {
        "satir_sayisi": satir_sayisi,
        "sutun_sayisi": len(sutunlar),
        "sutun_isimleri": sutunlar,
        "sayisal_analizler": sayisal_analizler
    }

# Örnek veri
ornek_veriler = [
    {"ad": "Ahmet", "yas": "25", "maas": "5000", "sehir": "İstanbul"},
    {"ad": "Ayşe", "yas": "30", "maas": "6000", "sehir": "Ankara"},
    {"ad": "Mehmet", "yas": "35", "maas": "7000", "sehir": "İzmir"},
    {"ad": "Fatma", "yas": "28", "maas": "5500", "sehir": "Bursa"}
]

veri_analizi = csv_oku_analiz_et(ornek_veriler)
print("\n=== Veri Analizi ===")
print(f"Satır sayısı: {veri_analizi['satir_sayisi']}")
print(f"Sütun sayısı: {veri_analizi['sutun_sayisi']}")
print(f"Sütunlar: {', '.join(veri_analizi['sutun_isimleri'])}")

for sutun, analiz in veri_analizi['sayisal_analizler'].items():
    print(f"\n{sutun.title()} analizi:")
    for metrik, deger in analiz.items():
        print(f"  {metrik.title()}: {deger:.2f}")

# =============================================================================
# 5. MATEMATİK VE ALGORİTMA FONKSİYONLARI
# =============================================================================

def asal_mi(sayi: int) -> bool:
    """Bir sayının asal olup olmadığını kontrol eder"""
    if sayi < 2:
        return False
    if sayi == 2:
        return True
    if sayi % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(sayi)) + 1, 2):
        if sayi % i == 0:
            return False
    return True

def asal_sayilar(limit: int) -> List[int]:
    """Belirtilen limite kadar asal sayıları döndürür"""
    return [sayi for sayi in range(2, limit + 1) if asal_mi(sayi)]

def fibonacci_dizisi(n: int) -> List[int]:
    """İlk n Fibonacci sayısını döndürür"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    
    return fib

def ebob_ekok(a: int, b: int) -> Tuple[int, int]:
    """İki sayının EBOB ve EKOK'unu hesaplar"""
    def ebob(x, y):
        while y:
            x, y = y, x % y
        return x
    
    ebob_sonuc = ebob(abs(a), abs(b))
    ekok_sonuc = abs(a * b) // ebob_sonuc
    
    return ebob_sonuc, ekok_sonuc

print("\n=== Matematik Fonksiyonları ===")
print(f"100'e kadar asal sayılar: {len(asal_sayilar(100))} adet")
print(f"İlk 10 asal: {asal_sayilar(100)[:10]}")

print(f"\nİlk 10 Fibonacci sayısı: {fibonacci_dizisi(10)}")

ebob_sonuc, ekok_sonuc = ebob_ekok(48, 18)
print(f"\n48 ve 18'in EBOB'u: {ebob_sonuc}")
print(f"48 ve 18'in EKOK'u: {ekok_sonuc}")

# =============================================================================
# 6. OYUN VE EĞLENCELİ FONKSİYONLAR
# =============================================================================

def sayi_tahmin_oyunu(min_sayi: int = 1, max_sayi: int = 100) -> Dict[str, any]:
    """
    Sayı tahmin oyunu simülasyonu
    
    Args:
        min_sayi: Minimum sayı
        max_sayi: Maksimum sayı
    
    Returns:
        Oyun sonuç bilgileri
    """
    hedef = random.randint(min_sayi, max_sayi)
    tahminler = []
    
    # Otomatik tahmin algoritması (binary search)
    alt_sinir = min_sayi
    ust_sinir = max_sayi
    
    while True:
        tahmin = (alt_sinir + ust_sinir) // 2
        tahminler.append(tahmin)
        
        if tahmin == hedef:
            break
        elif tahmin < hedef:
            alt_sinir = tahmin + 1
        else:
            ust_sinir = tahmin - 1
    
    return {
        "hedef_sayi": hedef,
        "tahmin_sayisi": len(tahminler),
        "tahminler": tahminler,
        "basarili": True
    }

def zar_simulasyonu(zar_sayisi: int = 2, atim_sayisi: int = 1000) -> Dict[str, any]:
    """
    Zar atma simülasyonu
    
    Args:
        zar_sayisi: Atılacak zar sayısı
        atim_sayisi: Toplam atım sayısı
    
    Returns:
        Simülasyon sonuçları
    """
    sonuclar = []
    toplam_dagilim = {}
    
    for _ in range(atim_sayisi):
        zarlar = [random.randint(1, 6) for _ in range(zar_sayisi)]
        toplam = sum(zarlar)
        sonuclar.append(toplam)
        toplam_dagilim[toplam] = toplam_dagilim.get(toplam, 0) + 1
    
    # İstatistikler
    ortalama = sum(sonuclar) / len(sonuclar)
    en_sik_toplam = max(toplam_dagilim.items(), key=lambda x: x[1])
    
    return {
        "zar_sayisi": zar_sayisi,
        "atim_sayisi": atim_sayisi,
        "ortalama_toplam": ortalama,
        "minimum_toplam": min(sonuclar),
        "maksimum_toplam": max(sonuclar),
        "en_sik_toplam": en_sik_toplam[0],
        "en_sik_frekans": en_sik_toplam[1],
        "toplam_dagilim": dict(sorted(toplam_dagilim.items()))
    }

print("\n=== Oyun Fonksiyonları ===")
oyun_sonucu = sayi_tahmin_oyunu(1, 1000)
print(f"Sayı tahmin oyunu: {oyun_sonucu['tahmin_sayisi']} tahminde {oyun_sonucu['hedef_sayi']} bulundu")

zar_sonucu = zar_simulasyonu(2, 10000)
print(f"\nZar simülasyonu (2 zar, 10000 atım):")
print(f"Ortalama toplam: {zar_sonucu['ortalama_toplam']:.2f}")
print(f"En sık çıkan toplam: {zar_sonucu['en_sik_toplam']} ({zar_sonucu['en_sik_frekans']} kez)")

# =============================================================================
# 7. ŞİFRELEME VE GÜVENLİK FONKSİYONLARI
# =============================================================================

def sifre_olustur(uzunluk: int = 12, ozel_karakter: bool = True) -> str:
    """
    Güvenli şifre oluşturur
    
    Args:
        uzunluk: Şifre uzunluğu
        ozel_karakter: Özel karakter kullanımı
    
    Returns:
        Oluşturulan şifre
    """
    import string
    
    karakterler = string.ascii_letters + string.digits
    if ozel_karakter:
        karakterler += "!@#$%^&*"
    
    # En az 1 büyük harf, 1 küçük harf, 1 rakam garantisi
    sifre = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits)
    ]
    
    if ozel_karakter:
        sifre.append(random.choice("!@#$%^&*"))
    
    # Kalan karakterleri ekle
    for _ in range(len(sifre), uzunluk):
        sifre.append(random.choice(karakterler))
    
    # Karıştır
    random.shuffle(sifre)
    return ''.join(sifre)

def sifre_gucunu_kontrol_et(sifre: str) -> Dict[str, any]:
    """
    Şifre gücünü analiz eder
    
    Args:
        sifre: Kontrol edilecek şifre
    
    Returns:
        Şifre güç analizi
    """
    import string
    
    puan = 0
    kriterler = {
        "uzunluk_yeterli": len(sifre) >= 8,
        "buyuk_harf": any(c.isupper() for c in sifre),
        "kucuk_harf": any(c.islower() for c in sifre),
        "rakam": any(c.isdigit() for c in sifre),
        "ozel_karakter": any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in sifre),
        "cok_uzun": len(sifre) >= 12
    }
    
    puan = sum(kriterler.values())
    
    if puan <= 2:
        guc = "Çok Zayıf"
    elif puan <= 3:
        guc = "Zayıf"
    elif puan <= 4:
        guc = "Orta"
    elif puan <= 5:
        guc = "Güçlü"
    else:
        guc = "Çok Güçlü"
    
    return {
        "sifre_gucu": guc,
        "puan": puan,
        "maksimum_puan": 6,
        "kriterler": kriterler,
        "oneriler": [
            "En az 8 karakter kullanın" if not kriterler["uzunluk_yeterli"] else None,
            "Büyük harf ekleyin" if not kriterler["buyuk_harf"] else None,
            "Küçük harf ekleyin" if not kriterler["kucuk_harf"] else None,
            "Rakam ekleyin" if not kriterler["rakam"] else None,
            "Özel karakter ekleyin" if not kriterler["ozel_karakter"] else None,
            "12+ karakter daha güvenli" if not kriterler["cok_uzun"] else None
        ]
    }

print("\n=== Güvenlik Fonksiyonları ===")
ornek_sifre = sifre_olustur(16, True)
print(f"Oluşturulan şifre: {ornek_sifre}")

sifre_analizi = sifre_gucunu_kontrol_et(ornek_sifre)
print(f"Şifre gücü: {sifre_analizi['sifre_gucu']} ({sifre_analizi['puan']}/{sifre_analizi['maksimum_puan']})")

# =============================================================================
# 8. PERFORMANS VE BENCHMARK FONKSİYONLARI
# =============================================================================

def fonksiyon_performans_test(func, *args, tekrar_sayisi: int = 1000, **kwargs):
    """
    Fonksiyon performansını ölçer
    
    Args:
        func: Test edilecek fonksiyon
        *args: Fonksiyon pozisyonel parametreleri
        tekrar_sayisi: Test tekrar sayısı
        **kwargs: Fonksiyon anahtar kelime parametreleri
    
    Returns:
        Performans test sonuçları
    """
    import time
    import gc
    
    # Garbage collection
    gc.collect()
    
    sureler = []
    
    for _ in range(tekrar_sayisi):
        baslangic = time.perf_counter()
        try:
            sonuc = func(*args, **kwargs)
        except Exception as e:
            return {"error": f"Fonksiyon hatası: {e}"}
        bitis = time.perf_counter()
        sureler.append(bitis - baslangic)
    
    ortalama_sure = sum(sureler) / len(sureler)
    min_sure = min(sureler)
    max_sure = max(sureler)
    
    return {
        "fonksiyon_adi": func.__name__,
        "tekrar_sayisi": tekrar_sayisi,
        "ortalama_sure": ortalama_sure * 1000,  # ms
        "minimum_sure": min_sure * 1000,  # ms
        "maksimum_sure": max_sure * 1000,  # ms
        "toplam_sure": sum(sureler) * 1000,  # ms
        "saniye_basina_cagri": 1 / ortalama_sure if ortalama_sure > 0 else float('inf')
    }

# Test fonksiyonları
def hizli_toplama(n):
    return sum(range(n))

def yavas_toplama(n):
    toplam = 0
    for i in range(n):
        toplam += i
    return toplam

print("\n=== Performans Testleri ===")
hizli_test = fonksiyon_performans_test(hizli_toplama, 1000, tekrar_sayisi=1000)
yavas_test = fonksiyon_performans_test(yavas_toplama, 1000, tekrar_sayisi=1000)

print(f"Hızlı toplama ortalama: {hizli_test['ortalama_sure']:.4f} ms")
print(f"Yavaş toplama ortalama: {yavas_test['ortalama_sure']:.4f} ms")
print(f"Hız farkı: {yavas_test['ortalama_sure'] / hizli_test['ortalama_sure']:.2f}x")

# =============================================================================
# 9. YARDIMCI VE GENEL AMAÇLI FONKSİYONLAR
# =============================================================================

def json_prettify(veri: any) -> str:
    """JSON verisini güzel formatta döndürür"""
    return json.dumps(veri, indent=2, ensure_ascii=False, default=str)

def liste_parcala(liste: List[any], parca_boyutu: int) -> List[List[any]]:
    """Listeyi belirtilen boyutta parçalara böler"""
    return [liste[i:i + parca_boyutu] for i in range(0, len(liste), parca_boyutu)]

def benzersiz_sirali_liste(liste: List[any]) -> List[any]:
    """Listeden benzersiz elemanları sıralı olarak döndürür"""
    return sorted(list(set(liste)))

def derin_birlestir(dict1: Dict, dict2: Dict) -> Dict:
    """İki sözlüğü derinlemesine birleştirir"""
    sonuc = dict1.copy()
    
    for anahtar, deger in dict2.items():
        if anahtar in sonuc and isinstance(sonuc[anahtar], dict) and isinstance(deger, dict):
            sonuc[anahtar] = derin_birlestir(sonuc[anahtar], deger)
        else:
            sonuc[anahtar] = deger
    
    return sonuc

print("\n=== Yardımcı Fonksiyonlar ===")

# Liste parçalama örneği
buyuk_liste = list(range(1, 26))
parcalar = liste_parcala(buyuk_liste, 5)
print(f"25 elemanlı liste 5'erli parçalara bölündü: {len(parcalar)} parça")

# Benzersiz sıralı liste
karisik_liste = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
benzersiz = benzersiz_sirali_liste(karisik_liste)
print(f"Karışık liste: {karisik_liste}")
print(f"Benzersiz sıralı: {benzersiz}")

# Sözlük birleştirme
dict1 = {"a": 1, "b": {"x": 10, "y": 20}}
dict2 = {"b": {"y": 30, "z": 40}, "c": 3}
birlesik = derin_birlestir(dict1, dict2)
print(f"Birleşik sözlük: {json_prettify(birlesik)}")

# =============================================================================
# 10. EN İYİ PRATİKLER VE ÖRNEKLER
# =============================================================================

print("\n=== En İyi Pratikler ===")

def en_iyi_pratik_ornegi(
    zorunlu_parametre: str,
    opsiyonel_parametre: Optional[str] = None,
    *args,
    **kwargs
) -> Dict[str, any]:
    """
    En iyi pratikleri gösteren örnek fonksiyon
    
    Bu fonksiyon şunları gösterir:
    - Type hints kullanımı
    - Detaylı docstring
    - Parametre validasyonu
    - Hata yönetimi
    - Logging
    - Return type consistency
    
    Args:
        zorunlu_parametre: Zorunlu string parametresi
        opsiyonel_parametre: Opsiyonel string parametresi
        *args: Değişken sayıda pozisyonel parametre
        **kwargs: Değişken sayıda anahtar kelime parametresi
    
    Returns:
        İşlem sonuç bilgileri içeren sözlük
    
    Raises:
        ValueError: Geçersiz parametre değeri için
        TypeError: Yanlış tip için
    
    Example:
        >>> sonuc = en_iyi_pratik_ornegi("test", "opsiyonel")
        >>> print(sonuc['durum'])
        'basarili'
    """
    # Parametre validasyonu
    if not isinstance(zorunlu_parametre, str):
        raise TypeError("zorunlu_parametre string olmalı")
    
    if not zorunlu_parametre.strip():
        raise ValueError("zorunlu_parametre boş olamaz")
    
    if opsiyonel_parametre is not None and not isinstance(opsiyonel_parametre, str):
        raise TypeError("opsiyonel_parametre None veya string olmalı")
    
    # İşlem yapımı
    try:
        sonuc = {
            "durum": "basarili",
            "zorunlu_parametre": zorunlu_parametre,
            "opsiyonel_parametre": opsiyonel_parametre,
            "args_sayisi": len(args),
            "kwargs_sayisi": len(kwargs),
            "islem_zamani": datetime.now().isoformat()
        }
        
        # Opsiyonel işlemler
        if args:
            sonuc["args_listesi"] = list(args)
        
        if kwargs:
            sonuc["kwargs_listesi"] = dict(kwargs)
        
        return sonuc
        
    except Exception as e:
        # Hata durumunda tutarlı format
        return {
            "durum": "hata",
            "hata_mesaji": str(e),
            "hata_tipi": type(e).__name__,
            "islem_zamani": datetime.now().isoformat()
        }

# En iyi pratik örneği kullanımı
ornek_sonuc = en_iyi_pratik_ornegi(
    "test verisi",
    "opsiyonel veri",
    1, 2, 3,
    anahtar1="değer1",
    anahtar2="değer2"
)

print("En iyi pratik örneği sonucu:")
print(json_prettify(ornek_sonuc))

print("\n" + "="*50)
print("✅ Kapsamlı fonksiyon örnekleri tamamlandı!")
print("✅ Gerçek dünya uygulamaları öğrenildi!")
print("✅ En iyi pratikler ve performans optimizasyonu öğrenildi!")
print("✅ Hata yönetimi ve validasyon teknikleri öğrenildi!")
print("="*50)