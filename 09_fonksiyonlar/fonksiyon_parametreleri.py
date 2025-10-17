"""
Python Fonksiyon Parametreleri - Detaylı Kılavuz

Bu dosya Python'da fonksiyon parametrelerinin tüm türlerini ve kullanımlarını kapsar.
Pozisyonel parametreler, anahtar kelime parametreleri, varsayılan değerler,
*args ve **kwargs gibi gelişmiş konuları öğreneceğiz.
"""

# =============================================================================
# 1. PARAMETRE TÜRLERİ
# =============================================================================

# 1.1 Pozisyonel Parametreler (Positional Parameters)
def kisiyi_tanit(ad, soyad, yas):
    """Pozisyonel parametrelerle kişi tanıtma"""
    return f"{ad} {soyad}, {yas} yaşında"

# Kullanım
print("=== Pozisyonel Parametreler ===")
print(kisiyi_tanit("Ahmet", "Yılmaz", 25))
print(kisiyi_tanit("Ayşe", "Kaya", 30))

# 1.2 Anahtar Kelime Parametreleri (Keyword Arguments)
def ogrenci_bilgisi(ad, soyad, yas, bolum="Belirsiz"):
    """Anahtar kelime parametreleri ile öğrenci bilgisi"""
    return f"{ad} {soyad} ({yas}), {bolum} bölümü"

print("\n=== Anahtar Kelime Parametreleri ===")
print(ogrenci_bilgisi("Mehmet", "Öz", 22))
print(ogrenci_bilgisi("Fatma", "Ak", 24, bolum="Bilgisayar Mühendisliği"))
print(ogrenci_bilgisi(ad="Ali", soyad="Veli", yas=26, bolum="Matematik"))

# =============================================================================
# 2. VARSAYILAN DEĞERLER (DEFAULT VALUES)
# =============================================================================

def selamla(isim, mesaj="Merhaba", noktalama="!"):
    """Varsayılan değerlerle selamlama"""
    return f"{mesaj} {isim}{noktalama}"

print("\n=== Varsayılan Değerler ===")
print(selamla("Ahmet"))
print(selamla("Ayşe", "İyi günler"))
print(selamla("Mehmet", "Hoş geldin", "."))

# ÖNEMLI: Varsayılan değer olarak mutable objeler kullanmayın!
# YANLIŞ KULLANIM:
def yanlis_liste_ekle(eleman, liste=[]):  # Bu tehlikeli!
    liste.append(eleman)
    return liste

# DOĞRU KULLANIM:
def dogru_liste_ekle(eleman, liste=None):
    if liste is None:
        liste = []
    liste.append(eleman)
    return liste

print("\n=== Varsayılan Değerler - Mutable Objeler ===")
print("Yanlış kullanım:")
print(yanlis_liste_ekle("a"))  # ['a']
print(yanlis_liste_ekle("b"))  # ['a', 'b'] - Beklenmedik!

print("\nDoğru kullanım:")
print(dogru_liste_ekle("x"))  # ['x']
print(dogru_liste_ekle("y"))  # ['y'] - Beklenen

# =============================================================================
# 3. *ARGS - DEĞİŞKEN SAYIDA POZİSYONEL PARAMETRE
# =============================================================================

def sayilari_topla(*sayilar):
    """Değişken sayıda sayıyı toplar"""
    toplam = 0
    for sayi in sayilar:
        toplam += sayi
    return toplam

print("\n=== *args Kullanımı ===")
print(f"Toplam: {sayilari_topla(1, 2, 3)}")
print(f"Toplam: {sayilari_topla(10, 20, 30, 40, 50)}")
print(f"Toplam: {sayilari_topla()}")  # 0

def gelismis_topla(carpan=1, *sayilar):
    """Çarpan ile birlikte toplama"""
    toplam = sum(sayilar)
    return toplam * carpan

print(f"Çarpanlı toplam: {gelismis_topla(2, 1, 2, 3, 4)}")

# Liste/tuple'ı *args olarak geçme
sayilar_listesi = [1, 2, 3, 4, 5]
print(f"Liste ile toplam: {sayilari_topla(*sayilar_listesi)}")

# =============================================================================
# 4. **KWARGS - DEĞİŞKEN SAYIDA ANAHTAR KELİME PARAMETRESİ
# =============================================================================

def kisi_profili(ad, soyad, **ek_bilgiler):
    """Kişi profili oluşturur"""
    profil = f"{ad} {soyad}\n"
    for anahtar, deger in ek_bilgiler.items():
        profil += f"{anahtar.title()}: {deger}\n"
    return profil

print("\n=== **kwargs Kullanımı ===")
print(kisi_profili("Ahmet", "Yılmaz", yas=30, meslek="Mühendis", sehir="İstanbul"))

def veritabani_baglanti(**ayarlar):
    """Veritabanı bağlantı ayarları"""
    varsayilan_ayarlar = {
        'host': 'localhost',
        'port': 5432,
        'username': 'user',
        'password': 'password'
    }
    
    # Varsayılan ayarları güncelle
    varsayilan_ayarlar.update(ayarlar)
    
    return f"Bağlantı: {varsayilan_ayarlar['username']}@{varsayilan_ayarlar['host']}:{varsayilan_ayarlar['port']}"

print(veritabani_baglanti())
print(veritabani_baglanti(host="192.168.1.1", port=3306))

# Sözlük'ü **kwargs olarak geçme
ayarlar = {'host': 'server.com', 'username': 'admin', 'password': 'secret123'}
print(veritabani_baglanti(**ayarlar))

# =============================================================================
# 5. *ARGS VE **KWARGS BİRLİKTE KULLANIMI
# =============================================================================

def evrensel_fonksiyon(*args, **kwargs):
    """Her türlü parametreyi kabul eden fonksiyon"""
    print(f"Pozisyonel parametreler: {args}")
    print(f"Anahtar kelime parametreleri: {kwargs}")

print("\n=== *args ve **kwargs Birlikte ===")
evrensel_fonksiyon(1, 2, 3, ad="Ahmet", yas=25)

def log_mesaji(seviye, mesaj, *detaylar, **metadata):
    """Gelişmiş log fonksiyonu"""
    log = f"[{seviye}] {mesaj}"
    
    if detaylar:
        log += f" | Detaylar: {', '.join(map(str, detaylar))}"
    
    if metadata:
        meta_str = ", ".join([f"{k}={v}" for k, v in metadata.items()])
        log += f" | Metadata: {meta_str}"
    
    return log

print(log_mesaji("ERROR", "Bağlantı hatası", "Timeout", "Network", modul="db", lineno=42))

# =============================================================================
# 6. PARAMETRE SIRASI VE KURALLAR
# =============================================================================

def parametre_sirasi(zorunlu, varsayilan="default", *args, **kwargs):
    """Doğru parametre sırası örneği"""
    print(f"Zorunlu: {zorunlu}")
    print(f"Varsayılan: {varsayilan}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

print("\n=== Parametre Sırası ===")
parametre_sirasi("test", "özel", 1, 2, 3, ek1="değer1", ek2="değer2")

# =============================================================================
# 7. KEYWORD-ONLY PARAMETRELER (Python 3+)
# =============================================================================

def dosya_oku(dosya_adi, *, encoding="utf-8", mod="r"):
    """Keyword-only parametreler ile dosya okuma"""
    print(f"Dosya: {dosya_adi}")
    print(f"Encoding: {encoding}")
    print(f"Mod: {mod}")

print("\n=== Keyword-Only Parametreler ===")
dosya_oku("test.txt")
dosya_oku("data.csv", encoding="latin-1", mod="rb")

# =============================================================================
# 8. POSITIONAL-ONLY PARAMETRELER (Python 3.8+)
# =============================================================================

def matematik_islem(a, b, /, operator="+"):
    """Positional-only parametreler ile matematik işlem"""
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b if b != 0 else "Sıfıra bölme hatası"

print("\n=== Positional-Only Parametreler ===")
print(f"5 + 3 = {matematik_islem(5, 3)}")
print(f"10 * 2 = {matematik_islem(10, 2, operator='*')}")

# =============================================================================
# 9. PARAMETRE TİPLERİNİN BİRLEŞİMİ
# =============================================================================

def tam_ornek(zorunlu, /, standart, varsayilan="default", *args, keyword_only, **kwargs):
    """Tüm parametre türlerinin birleşimi"""
    return {
        'zorunlu': zorunlu,
        'standart': standart,
        'varsayilan': varsayilan,
        'args': args,
        'keyword_only': keyword_only,
        'kwargs': kwargs
    }

print("\n=== Tüm Parametre Türleri ===")
sonuc = tam_ornek(
    "pos_only",           # positional-only
    "standart_deger",     # standart
    "ozel_varsayilan",    # varsayılan değeri değiştir
    "extra1", "extra2",   # *args
    keyword_only="zorunlu_kw",  # keyword-only
    ek1="değer1", ek2="değer2"  # **kwargs
)

for anahtar, deger in sonuc.items():
    print(f"{anahtar}: {deger}")

# =============================================================================
# 10. PRATİK ÖRNEKLER
# =============================================================================

# Email gönderme fonksiyonu
def email_gonder(alici, konu, icerik, *, cc=None, bcc=None, ek_dosyalar=None, oncelik="normal"):
    """Email gönderme fonksiyonu"""
    email = {
        'to': alici,
        'subject': konu,
        'body': icerik,
        'priority': oncelik
    }
    
    if cc:
        email['cc'] = cc
    if bcc:
        email['bcc'] = bcc
    if ek_dosyalar:
        email['attachments'] = ek_dosyalar
    
    return f"Email gönderildi: {email}"

print("\n=== Pratik Örnek: Email Gönderme ===")
print(email_gonder(
    "user@example.com",
    "Test Mesajı",
    "Bu bir test mesajıdır.",
    cc=["manager@example.com"],
    oncelik="yüksek"
))

# Veritabanı sorgu fonksiyonu
def veritabani_sorgula(sorgu, *parametreler, **secenekler):
    """Veritabanı sorgu fonksiyonu"""
    ayarlar = {
        'timeout': 30,
        'cache': True,
        'debug': False
    }
    ayarlar.update(secenekler)
    
    return {
        'query': sorgu,
        'parameters': parametreler,
        'options': ayarlar
    }

print("\n=== Pratik Örnek: Veritabanı Sorgulama ===")
sorgu_sonucu = veritabani_sorgula(
    "SELECT * FROM users WHERE age > ? AND city = ?",
    25, "İstanbul",
    timeout=60,
    debug=True
)
print(f"Sorgu: {sorgu_sonucu}")

# =============================================================================
# 11. PERFORMANS İPUÇLARI
# =============================================================================

# Fonksiyon çağrı performansı
import time

def performans_testi():
    """Parametre geçirme performansı"""
    
    def basit_fonksiyon(a, b, c):
        return a + b + c
    
    def args_fonksiyon(*args):
        return sum(args)
    
    def kwargs_fonksiyon(**kwargs):
        return sum(kwargs.values())
    
    # Test verileri
    test_sayisi = 100000
    
    # Basit parametre geçirme
    start = time.time()
    for _ in range(test_sayisi):
        basit_fonksiyon(1, 2, 3)
    basit_sure = time.time() - start
    
    # *args kullanımı
    start = time.time()
    for _ in range(test_sayisi):
        args_fonksiyon(1, 2, 3)
    args_sure = time.time() - start
    
    # **kwargs kullanımı
    start = time.time()
    for _ in range(test_sayisi):
        kwargs_fonksiyon(a=1, b=2, c=3)
    kwargs_sure = time.time() - start
    
    print(f"\n=== Performans Test Sonuçları ({test_sayisi} çağrı) ===")
    print(f"Basit parametreler: {basit_sure:.4f} saniye")
    print(f"*args kullanımı: {args_sure:.4f} saniye ({args_sure/basit_sure:.2f}x)")
    print(f"**kwargs kullanımı: {kwargs_sure:.4f} saniye ({kwargs_sure/basit_sure:.2f}x)")

# performans_testi()  # Çok fazla çıktı üretmesin diye yorum satırında

# =============================================================================
# 12. EN İYİ PRATİKLER
# =============================================================================

print("\n=== En İyi Pratikler ===")

# 1. Anlaşılır parametre isimleri kullanın
def iyi_ornek(kullanici_adi, parola, oturum_suresi=3600):
    """Anlaşılır parametre isimleri"""
    pass

# 2. Varsayılan değerler için None kullanın (mutable objeler için)
def liste_islemci(veriler, islemler=None):
    if islemler is None:
        islemler = ['temizle', 'sirala']
    return veriler

# 3. Type hints kullanın (modern Python)
from typing import List, Dict, Optional, Union

def gelismis_fonksiyon(
    sayilar: List[int],
    carpan: float = 1.0,
    secenekler: Optional[Dict[str, Union[str, int]]] = None
) -> List[float]:
    """Type hints ile gelişmiş fonksiyon"""
    if secenekler is None:
        secenekler = {}
    
    return [sayi * carpan for sayi in sayilar]

# 4. Docstring'lerde parametreleri belgelendirin
def belgelendirilmis_fonksiyon(veri: str, format_tipi: str = "json") -> dict:
    """
    Veriyi belirtilen formatta işler.
    
    Args:
        veri (str): İşlenecek veri
        format_tipi (str): Veri formatı ('json', 'xml', 'csv')
    
    Returns:
        dict: İşlenmiş veri sözlüğü
    
    Raises:
        ValueError: Desteklenmeyen format tipi için
    """
    if format_tipi not in ['json', 'xml', 'csv']:
        raise ValueError(f"Desteklenmeyen format: {format_tipi}")
    
    return {'data': veri, 'format': format_tipi}

print("✓ Fonksiyon parametreleri detaylı olarak öğrenildi!")
print("✓ *args ve **kwargs kullanımı öğrenildi!")
print("✓ Parametre türleri ve sıralaması öğrenildi!")
print("✓ En iyi pratikler ve performans ipuçları öğrenildi!")