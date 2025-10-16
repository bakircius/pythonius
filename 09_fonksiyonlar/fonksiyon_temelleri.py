# Fonksiyon Temelleri ve Tanımlama
# Python fonksiyonlarının temel kullanımı ve özellikleri

print("=== FONKSİYON TEMELLERİ VE TANIMLAMA ===\n")

print("1. TEMEL FONKSİYON TANIMLAMA:")
print("-" * 29)

# En basit fonksiyon
def selamla():
    """Basit selamlama fonksiyonu"""
    print("Merhaba!")

# Fonksiyonu çağırma
selamla()

# Parametreli fonksiyon
def kisisel_selamla(isim):
    """Kişisel selamlama fonksiyonu"""
    print(f"Merhaba {isim}!")

kisisel_selamla("Ali")
kisisel_selamla("Ayşe")

# Çoklu parametreli fonksiyon
def tam_selamla(isim, soyisim):
    """İsim ve soyisim ile selamlama"""
    print(f"Merhaba {isim} {soyisim}!")

tam_selamla("Ali", "Veli")

# Return değeri olan fonksiyon
def toplama(a, b):
    """İki sayıyı toplar"""
    sonuc = a + b
    return sonuc

# Fonksiyon sonucunu kullanma
sonuc = toplama(5, 3)
print(f"Toplama sonucu: {sonuc}")

# Direkt kullanım
print(f"7 + 4 = {toplama(7, 4)}")

print("\n2. PARAMETRE TİPLERİ:")
print("-" * 20)

# Varsayılan parametreler (default parameters)
def selamla_varsayilan(isim="Arkadaş", selam="Merhaba"):
    """Varsayılan değerli parametreler"""
    return f"{selam} {isim}!"

print(selamla_varsayilan())  # Tüm varsayılanlar
print(selamla_varsayilan("Ali"))  # Sadece isim
print(selamla_varsayilan("Veli", "Selam"))  # İkisi de belirtildi
print(selamla_varsayilan(selam="Hoş geldin"))  # Keyword argument

# DİKKAT: Mutable varsayılan parametreler
def kotu_ornek(liste=[]):  # YAPMAYIN!
    liste.append("yeni")
    return liste

print("Kötü örnek:")
print(kotu_ornek())  # ['yeni']
print(kotu_ornek())  # ['yeni', 'yeni'] - Sürpriz!

# Doğru yöntem
def iyi_ornek(liste=None):
    if liste is None:
        liste = []
    liste.append("yeni")
    return liste

print("İyi örnek:")
print(iyi_ornek())  # ['yeni']
print(iyi_ornek())  # ['yeni'] - Doğru!

# Pozisyonel argumentlar
def matematik_islem(sayi1, sayi2, islem="+"):
    """Temel matematik işlemleri"""
    if islem == "+":
        return sayi1 + sayi2
    elif islem == "-":
        return sayi1 - sayi2
    elif islem == "*":
        return sayi1 * sayi2
    elif islem == "/":
        return sayi1 / sayi2 if sayi2 != 0 else "Sıfıra bölme hatası"
    else:
        return "Geçersiz işlem"

print(f"5 + 3 = {matematik_islem(5, 3)}")
print(f"5 - 3 = {matematik_islem(5, 3, '-')}")
print(f"5 * 3 = {matematik_islem(5, 3, '*')}")
print(f"5 / 3 = {matematik_islem(5, 3, '/')}")

print("\n3. KEYWORD ARGUMENTS:")
print("-" * 21)

# Keyword arguments kullanımı
def kisi_bilgisi(isim, yas, sehir="Bilinmiyor", meslek="Bilinmiyor"):
    """Kişi bilgilerini formatlar"""
    return f"{isim}, {yas} yaşında, {sehir}'de yaşıyor, meslek: {meslek}"

# Pozisyonel kullanım
print(kisi_bilgisi("Ali", 25))

# Keyword kullanımı
print(kisi_bilgisi("Veli", 30, sehir="İstanbul"))
print(kisi_bilgisi("Ayşe", 28, meslek="Mühendis"))

# Karışık kullanım
print(kisi_bilgisi("Mehmet", 35, meslek="Doktor", sehir="Ankara"))

# Keyword-only arguments (Python 3+)
def gelismis_hesaplama(x, y, *, method="ortalama", precision=2):
    """* sonrası sadece keyword argument"""
    if method == "ortalama":
        sonuc = (x + y) / 2
    elif method == "carpim":
        sonuc = x * y
    else:
        sonuc = x + y
    
    return round(sonuc, precision)

print(f"Ortalama: {gelismis_hesaplama(10, 20)}")
print(f"Çarpım: {gelismis_hesaplama(10, 20, method='carpim')}")
# print(gelismis_hesaplama(10, 20, "carpim"))  # HATA! Keyword gerekli

print("\n4. *ARGS VE **KWARGS:")
print("-" * 22)

# *args - değişken sayıda pozisyonel arguman
def toplam_hesapla(*sayilar):
    """Herhangi sayıda sayıyı toplar"""
    return sum(sayilar)

print(f"Toplam (2 sayı): {toplam_hesapla(5, 3)}")
print(f"Toplam (4 sayı): {toplam_hesapla(1, 2, 3, 4)}")
print(f"Toplam (6 sayı): {toplam_hesapla(10, 20, 30, 40, 50, 60)}")

# **kwargs - değişken sayıda keyword arguman
def profil_olustur(**bilgiler):
    """Profil bilgilerini işler"""
    print("Profil Bilgileri:")
    for anahtar, deger in bilgiler.items():
        print(f"  {anahtar}: {deger}")

profil_olustur(isim="Ali", yas=25, sehir="İstanbul")
profil_olustur(isim="Veli", meslek="Mühendis", telefon="555-1234")

# *args ve **kwargs birlikte
def esnek_fonksiyon(zorunlu_param, *args, **kwargs):
    """Esnek parametre alan fonksiyon"""
    print(f"Zorunlu: {zorunlu_param}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

esnek_fonksiyon("test", 1, 2, 3, isim="Ali", yas=25)

# Unpacking arguments
sayilar = [1, 2, 3, 4, 5]
print(f"Liste unpacking: {toplam_hesapla(*sayilar)}")

bilgiler = {"isim": "Ayşe", "yas": 28, "sehir": "Ankara"}
profil_olustur(**bilgiler)

print("\n5. RETURN DÖNDÜRMESİ:")
print("-" * 20)

# Tek değer döndürme
def kare_al(sayi):
    """Sayının karesini alır"""
    return sayi ** 2

print(f"5'in karesi: {kare_al(5)}")

# Çoklu değer döndürme (tuple)
def matematik_operasyonlar(a, b):
    """Temel matematik işlemlerini yapar"""
    toplam = a + b
    fark = a - b
    carpim = a * b
    bolum = a / b if b != 0 else None
    return toplam, fark, carpim, bolum

# Unpacking ile alma
t, f, c, b = matematik_operasyonlar(10, 3)
print(f"10 ve 3: toplam={t}, fark={f}, çarpım={c}, bölüm={b}")

# Tuple olarak alma
sonuclar = matematik_operasyonlar(8, 2)
print(f"Tüm sonuçlar: {sonuclar}")

# Koşullu return
def mutlak_deger(sayi):
    """Sayının mutlak değerini alır"""
    if sayi >= 0:
        return sayi
    else:
        return -sayi

print(f"|-5| = {mutlak_deger(-5)}")
print(f"|7| = {mutlak_deger(7)}")

# Erken return
def bolen_bul(sayi, max_bolen=10):
    """Sayının bölenlerini bulur"""
    bolenler = []
    for i in range(1, min(sayi + 1, max_bolen + 1)):
        if sayi % i == 0:
            bolenler.append(i)
        
        # Erken çıkış koşulu
        if len(bolenler) >= 5:
            return bolenler
    
    return bolenler

print(f"12'nin bölenleri: {bolen_bul(12)}")

# None return (varsayılan)
def yan_etki_fonksiyon(liste, eleman):
    """Yan etki yapar, değer döndürmez"""
    liste.append(eleman)
    # return None (implicit)

liste = [1, 2, 3]
sonuc = yan_etki_fonksiyon(liste, 4)
print(f"Liste: {liste}, return değeri: {sonuc}")

print("\n6. DOCSTRİNG VE ANNOTATIONS:")
print("-" * 29)

# Detailed docstring
def gelismis_hesaplama(x, y, operation="add"):
    """
    İki sayı üzerinde matematik işlem yapar.
    
    Args:
        x (float): İlk sayı
        y (float): İkinci sayı
        operation (str): İşlem tipi ('add', 'subtract', 'multiply', 'divide')
    
    Returns:
        float: İşlem sonucu
    
    Raises:
        ValueError: Geçersiz işlem tipi
        ZeroDivisionError: Sıfıra bölme
    
    Examples:
        >>> gelismis_hesaplama(5, 3)
        8.0
        >>> gelismis_hesaplama(10, 2, 'divide')
        5.0
    """
    if operation == "add":
        return float(x + y)
    elif operation == "subtract":
        return float(x - y)
    elif operation == "multiply":
        return float(x * y)
    elif operation == "divide":
        if y == 0:
            raise ZeroDivisionError("Sıfıra bölme hatası")
        return float(x / y)
    else:
        raise ValueError(f"Geçersiz işlem: {operation}")

# Docstring'e erişim
print("Fonksiyon dökümantasyonu:")
print(gelismis_hesaplama.__doc__)

# Type annotations (Python 3.5+)
def tip_belirtili_fonksiyon(isim: str, yas: int, aktif: bool = True) -> str:
    """Type annotations ile fonksiyon"""
    durum = "aktif" if aktif else "pasif"
    return f"{isim} ({yas} yaş) - {durum}"

print(f"Tip belirtili: {tip_belirtili_fonksiyon('Ali', 25)}")

# Karmaşık type annotations
from typing import List, Dict, Optional, Union

def liste_isle(sayilar: List[int], carpan: Optional[int] = None) -> List[int]:
    """Liste işleme fonksiyonu"""
    if carpan is None:
        return sayilar
    return [sayi * carpan for sayi in sayilar]

print(f"Liste işleme: {liste_isle([1, 2, 3, 4], 2)}")

def sozluk_birlesitir(dict1: Dict[str, int], dict2: Dict[str, int]) -> Dict[str, int]:
    """İki sözlüğü birleştirir"""
    sonuc = dict1.copy()
    sonuc.update(dict2)
    return sonuc

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
print(f"Sözlük birleştirme: {sozluk_birlesitir(d1, d2)}")

print("\n7. YEREL VE GLOBAL DEĞİŞKENLER:")
print("-" * 31)

# Global değişken
global_sayac = 0

def sayac_artir():
    """Global sayacı artırır"""
    global global_sayac
    global_sayac += 1
    return global_sayac

print(f"Sayaç: {sayac_artir()}")
print(f"Sayaç: {sayac_artir()}")
print(f"Global sayaç: {global_sayac}")

# Local değişken
def yerel_degisken_test():
    """Yerel değişken örneği"""
    yerel_sayi = 10
    print(f"Fonksiyon içi: {yerel_sayi}")
    return yerel_sayi

sonuc = yerel_degisken_test()
print(f"Fonksiyon dışı: {sonuc}")
# print(yerel_sayi)  # NameError!

# Shadowing (gölgeleme)
x = "global"

def golgeleme_test():
    x = "local"  # Global x'i gölgeler
    print(f"Fonksiyon içi x: {x}")

print(f"Global x: {x}")
golgeleme_test()
print(f"Hala global x: {x}")

# nonlocal keyword
def dis_fonksiyon():
    dis_degisken = "dış"
    
    def ic_fonksiyon():
        nonlocal dis_degisken
        dis_degisken = "değişti"
        print(f"İç fonksiyon: {dis_degisken}")
    
    print(f"Önce: {dis_degisken}")
    ic_fonksiyon()
    print(f"Sonra: {dis_degisken}")

dis_fonksiyon()

print("\n8. FONKSİYON SCOPE VE LEGB KURALI:")
print("-" * 32)

# LEGB: Local, Enclosing, Global, Built-in
builtin_len = len  # Built-in function

global_var = "Global"

def dis_fonksiyon():
    enclosing_var = "Enclosing"
    
    def ic_fonksiyon():
        local_var = "Local"
        
        print(f"Local: {local_var}")
        print(f"Enclosing: {enclosing_var}")
        print(f"Global: {global_var}")
        print(f"Built-in len: {builtin_len([1, 2, 3])}")
    
    ic_fonksiyon()

dis_fonksiyon()

# Name resolution örneği
x = "global x"

def test_scope():
    # x = "local x"  # Bu satırı açarsanız local olur
    print(f"Fonksiyon içi x: {x}")

test_scope()

print("\n9. FONKSİYONLAR BİRİNCİ SINIF OBJELER:")
print("-" * 37)

# Fonksiyonları değişkene atama
def selamla(isim):
    return f"Merhaba {isim}!"

selam_fonksiyonu = selamla  # Fonksiyonu değişkene ata
print(selam_fonksiyonu("Ali"))

# Fonksiyonları parametre olarak geçme
def islem_yap(fonksiyon, deger):
    """Verilen fonksiyonu değere uygular"""
    return fonksiyon(deger)

def kare_al(x):
    return x ** 2

def kup_al(x):
    return x ** 3

print(f"5'in karesi: {islem_yap(kare_al, 5)}")
print(f"3'ün küpü: {islem_yap(kup_al, 3)}")

# Fonksiyonları listede saklama
matematik_fonksiyonlari = [kare_al, kup_al, lambda x: x * 2]

for i, func in enumerate(matematik_fonksiyonlari):
    print(f"Fonksiyon {i}: 4 -> {func(4)}")

# Fonksiyon döndüren fonksiyon
def carpan_olustur(carpan):
    """Belirli sayıyla çarpan fonksiyon oluşturur"""
    def carpma_fonksiyonu(sayi):
        return sayi * carpan
    return carpma_fonksiyonu

ikiye_carp = carpan_olustur(2)
uce_carp = carpan_olustur(3)

print(f"5 * 2 = {ikiye_carp(5)}")
print(f"5 * 3 = {uce_carp(5)}")

print("\n10. LAMBDA FONKSİYONLARI:")
print("-" * 24)

# Basit lambda
kare = lambda x: x ** 2
print(f"Lambda kare 6: {kare(6)}")

# Çoklu parametre
toplam = lambda x, y: x + y
print(f"Lambda toplam: {toplam(5, 3)}")

# Koşullu lambda
mutlak = lambda x: x if x >= 0 else -x
print(f"Lambda mutlak -7: {mutlak(-7)}")

# Lambda with default parameter
selamla_lambda = lambda isim="Arkadaş": f"Merhaba {isim}!"
print(selamla_lambda())
print(selamla_lambda("Ali"))

# Lambda'ları veri yapılarında kullanma
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map() ile
kareler = list(map(lambda x: x ** 2, sayilar))
print(f"Kareler: {kareler}")

# filter() ile
ciftler = list(filter(lambda x: x % 2 == 0, sayilar))
print(f"Çiftler: {ciftler}")

# sorted() ile
kelimeler = ["python", "java", "go", "javascript"]
uzunluga_gore = sorted(kelimeler, key=lambda x: len(x))
print(f"Uzunluğa göre: {uzunluga_gore}")

# Lambda'nın sınırları
# Bu YAPILAMAZ (statements):
# if_lambda = lambda x: if x > 0: print("pozitif")  # HATA!

# Bu da YAPILAMAZ (complex logic):
# Karmaşık logic için normal fonksiyon kullanın

print("\n11. FONKSİYON PERFORMANSI:")
print("-" * 24)

import time

# Fonksiyon çağırma overhead'ı
def basit_toplam(a, b):
    return a + b

# Fonksiyon vs inline
sayilar1 = list(range(10000))
sayilar2 = list(range(10000))

# Fonksiyon ile
start = time.time()
sonuc1 = [basit_toplam(a, b) for a, b in zip(sayilar1, sayilar2)]
func_time = time.time() - start

# Inline ile
start = time.time()
sonuc2 = [a + b for a, b in zip(sayilar1, sayilar2)]
inline_time = time.time() - start

print(f"Fonksiyon ile: {func_time*1000:.2f} ms")
print(f"Inline ile: {inline_time*1000:.2f} ms")
print(f"Overhead: {((func_time - inline_time) / inline_time * 100):.1f}%")

# Lambda vs normal function
normal_func = lambda x: x * 2

def normal_fonksiyon(x):
    return x * 2

test_data = list(range(10000))

# Lambda performansı
start = time.time()
lambda_sonuc = list(map(normal_func, test_data))
lambda_time = time.time() - start

# Normal fonksiyon performansı
start = time.time()
func_sonuc = list(map(normal_fonksiyon, test_data))
normal_time = time.time() - start

print(f"Lambda: {lambda_time*1000:.2f} ms")
print(f"Normal fonksiyon: {normal_time*1000:.2f} ms")

print("\n12. FONKSİYON DEBUGGING:")
print("-" * 22)

def debug_ornegi(x, y):
    """Debug örnekleri"""
    print(f"Giriş: x={x}, y={y}")
    
    # Ara sonuç
    ara_sonuc = x * 2
    print(f"Ara sonuç: {ara_sonuc}")
    
    # Final sonuç
    final_sonuc = ara_sonuc + y
    print(f"Final sonuç: {final_sonuc}")
    
    return final_sonuc

sonuc = debug_ornegi(5, 3)

# Assertion kullanımı
def bolme_guvenli(a, b):
    """Güvenli bölme fonksiyonu"""
    assert b != 0, "Bölen sıfır olamaz!"
    assert isinstance(a, (int, float)), "a sayı olmalı"
    assert isinstance(b, (int, float)), "b sayı olmalı"
    
    return a / b

print(f"Güvenli bölme: {bolme_guvenli(10, 2)}")

try:
    bolme_guvenli(10, 0)
except AssertionError as e:
    print(f"Assertion hatası: {e}")

print("\n=== FONKSİYON TEMELLERİ ÖZETİ ===")
print("Fonksiyon tanımlama:")
print("  def function_name(parameters):")
print("      \"\"\"docstring\"\"\"")
print("      # function body")
print("      return value")
print()
print("Parametre tipleri:")
print("  • Pozisyonel parametreler")
print("  • Keyword parametreler")
print("  • Varsayılan parametreler")
print("  • *args (variable positional)")
print("  • **kwargs (variable keyword)")
print()
print("Scope kuralları:")
print("  • LEGB: Local → Enclosing → Global → Built-in")
print("  • global keyword - global değişken değiştirme")
print("  • nonlocal keyword - enclosing değişken değiştirme")
print()
print("En iyi pratikler:")
print("  • Açıklayıcı isimler kullanın")
print("  • Docstring yazın")
print("  • Type annotations ekleyin")
print("  • Mutable default parameters kullanmayın")
print("  • Tek sorumluluk prensibi")
print("  • Return değeri tutarlı olsun")