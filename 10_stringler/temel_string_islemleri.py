"""
Python String İşlemleri - Temel Konular

Bu dosya Python'da string (metin) işlemlerinin temellerini kapsar.
String oluşturma, indeksleme, slicing, temel string metodları
ve string formatting işlemlerini öğreneceğiz.
"""

# =============================================================================
# 1. STRİNG OLUŞTURMA VE TANIMLAMA
# =============================================================================

print("=== String Oluşturma ve Tanımlama ===")

def string_olusturma_ornekleri():
    """String oluşturma yöntemleri"""
    
    print("📝 String Oluşturma Yöntemleri:")
    
    # Tek tırnak ile
    tek_tirnak = 'Bu bir string'
    print(f"Tek tırnak: {tek_tirnak}")
    
    # Çift tırnak ile
    cift_tirnak = "Bu da bir string"
    print(f"Çift tırnak: {cift_tirnak}")
    
    # Üçlü tırnak ile (multiline)
    uclu_tirnak = """Bu çok satırlı
    bir string'dir.
    Birden fazla satır içerir."""
    print(f"Üçlü tırnak:\n{uclu_tirnak}")
    
    # Raw string (kaçış karakterleri ignore edilir)
    raw_string = r"Bu bir raw string\n\t(kaçış karakterleri çalışmaz)"
    print(f"Raw string: {raw_string}")
    
    # Boş string
    bos_string = ""
    print(f"Boş string uzunluğu: {len(bos_string)}")
    
    # String constructor ile
    constructor_string = str(12345)
    print(f"Constructor ile: {constructor_string} (tip: {type(constructor_string)})")
    
    # Unicode string
    unicode_string = "Türkçe karakterler: çğıöşü 🐍"
    print(f"Unicode: {unicode_string}")

string_olusturma_ornekleri()

# =============================================================================
# 2. STRİNG İNDEKSLEME VE SLİCİNG
# =============================================================================

print("\n=== String İndeksleme ve Slicing ===")

def string_indeksleme_ornekleri():
    """String indeksleme ve slicing örnekleri"""
    
    metin = "Python Programming"
    print(f"🎯 Örnek metin: '{metin}'")
    print(f"Uzunluk: {len(metin)}")
    
    print(f"\n📍 İndeksleme:")
    print(f"İlk karakter (0): '{metin[0]}'")
    print(f"Son karakter (-1): '{metin[-1]}'")
    print(f"5. karakter: '{metin[5]}'")
    print(f"Sondan 3. karakter (-3): '{metin[-3]}'")
    
    print(f"\n✂️ Slicing:")
    print(f"İlk 6 karakter [0:6]: '{metin[0:6]}'")
    print(f"7'den sona kadar [7:]: '{metin[7:]}'")
    print(f"Baştan 6'ya kadar [:6]: '{metin[:6]}'")
    print(f"Son 11 karakter [-11:]: '{metin[-11:]}'")
    print(f"2'den 8'e kadar [2:8]: '{metin[2:8]}'")
    
    print(f"\n🔄 Step ile slicing:")
    print(f"Her 2. karakter [::2]: '{metin[::2]}'")
    print(f"Ters çevir [::-1]: '{metin[::-1]}'")
    print(f"2'den 10'a 2'şer atlayarak [2:10:2]: '{metin[2:10:2]}'")
    
    # Güvenli indeksleme
    print(f"\n🛡️ Güvenli indeksleme:")
    try:
        karakter = metin[100]  # Hata verecek
    except IndexError as e:
        print(f"Hata: {e}")
    
    # Güvenli alternatif
    def guvenli_karakter(metin, index):
        """Güvenli karakter alma"""
        if 0 <= index < len(metin):
            return metin[index]
        return None
    
    print(f"Güvenli 100. karakter: {guvenli_karakter(metin, 100)}")
    print(f"Güvenli 5. karakter: {guvenli_karakter(metin, 5)}")

string_indeksleme_ornekleri()

# =============================================================================
# 3. TEMEL STRİNG METODLARİ
# =============================================================================

print("\n=== Temel String Metodları ===")

def temel_string_metodlari():
    """Temel string metodları örnekleri"""
    
    ornek_metin = "  Python Programming Language  "
    print(f"🎯 Örnek: '{ornek_metin}'")
    
    print(f"\n🧹 Temizleme metodları:")
    print(f"strip(): '{ornek_metin.strip()}'")
    print(f"lstrip(): '{ornek_metin.lstrip()}'")
    print(f"rstrip(): '{ornek_metin.rstrip()}'")
    
    temiz_metin = ornek_metin.strip()
    
    print(f"\n🔄 Büyük/küçük harf dönüşümleri:")
    print(f"lower(): '{temiz_metin.lower()}'")
    print(f"upper(): '{temiz_metin.upper()}'")
    print(f"title(): '{temiz_metin.title()}'")
    print(f"capitalize(): '{temiz_metin.capitalize()}'")
    print(f"swapcase(): '{temiz_metin.swapcase()}'")
    
    print(f"\n🔍 Arama metodları:")
    print(f"find('Python'): {temiz_metin.find('Python')}")
    print(f"find('Java'): {temiz_metin.find('Java')}")
    print(f"index('Programming'): {temiz_metin.index('Programming')}")
    print(f"count('g'): {temiz_metin.count('g')}")
    
    print(f"\n✅ Kontrol metodları:")
    print(f"startswith('Python'): {temiz_metin.startswith('Python')}")
    print(f"endswith('Language'): {temiz_metin.endswith('Language')}")
    print(f"isalpha(): '{temiz_metin.isalpha()}'")
    print(f"isdigit(): '{'123'.isdigit()}'")
    print(f"isalnum(): '{'abc123'.isalnum()}'")
    print(f"isspace(): '{' '.isspace()}'")
    
    print(f"\n🔄 Değiştirme metodları:")
    print(f"replace('Python', 'Java'): '{temiz_metin.replace('Python', 'Java')}'")
    print(f"replace('a', '@', 1): '{temiz_metin.replace('a', '@', 1)}'")

temel_string_metodlari()

# =============================================================================
# 4. STRİNG BİRLEŞTİRME VE BÖLME
# =============================================================================

print("\n=== String Birleştirme ve Bölme ===")

def string_birlestirme_bolme():
    """String birleştirme ve bölme işlemleri"""
    
    print("🔗 String Birleştirme Yöntemleri:")
    
    # + operatörü ile
    ad = "Ahmet"
    soyad = "Yılmaz"
    tam_ad = ad + " " + soyad
    print(f"+ operatörü: '{tam_ad}'")
    
    # += operatörü ile
    mesaj = "Merhaba"
    mesaj += " Dünya"
    mesaj += "!"
    print(f"+= operatörü: '{mesaj}'")
    
    # join() metodu ile (verimli)
    kelimeler = ["Python", "çok", "güçlü", "bir", "dildir"]
    cumle = " ".join(kelimeler)
    print(f"join() ile: '{cumle}'")
    
    # Farklı ayırıcılarla join
    print(f"Virgül ile: '{', '.join(kelimeler)}'")
    print(f"Tire ile: '{'-'.join(kelimeler)}'")
    print(f"Boş ile: '{' '.join(kelimeler)}'")
    
    print(f"\n✂️ String Bölme Yöntemleri:")
    
    metin = "elma,armut,kiraz,şeftali"
    print(f"Örnek: '{metin}'")
    
    # split() metodu
    meyveler = metin.split(",")
    print(f"split(','): {meyveler}")
    
    # Maksimum bölme sayısı
    iki_parca = metin.split(",", 1)
    print(f"split(',', 1): {iki_parca}")
    
    # Boşluk ile bölme (varsayılan)
    cumle = "Bu bir örnek cümledir"
    kelimeler = cumle.split()
    print(f"split() (boşluk): {kelimeler}")
    
    # rsplit() - sağdan bölme
    dosya_yolu = "/home/user/documents/file.txt"
    sag_bol = dosya_yolu.rsplit("/", 1)
    print(f"rsplit('/', 1): {sag_bol}")
    
    # splitlines() - satır bölme
    cok_satirli = "Birinci satır\nİkinci satır\nÜçüncü satır"
    satirlar = cok_satirli.splitlines()
    print(f"splitlines(): {satirlar}")
    
    # partition() - tek bölme
    email = "kullanici@domain.com"
    kullanici, at, domain = email.partition("@")
    print(f"partition('@'): kullanici='{kullanici}', domain='{domain}'")

string_birlestirme_bolme()

# =============================================================================
# 5. STRİNG FORMATLANDİRMA - TEMEL
# =============================================================================

print("\n=== String Formatlandırma - Temel ===")

def string_formatlama_temel():
    """Temel string formatlandırma yöntemleri"""
    
    ad = "Ayşe"
    yas = 25
    maas = 5500.75
    
    print("📝 String Formatlandırma Yöntemleri:")
    
    # % formatting (eski yöntem)
    print("\n1. % Formatting:")
    mesaj1 = "Adım %s, yaşım %d" % (ad, yas)
    print(f"Basit: {mesaj1}")
    
    mesaj2 = "Maaş: %.2f TL" % maas
    print(f"Ondalık: {mesaj2}")
    
    mesaj3 = "Ad: %-10s Yaş: %3d" % (ad, yas)
    print(f"Hizalama: '{mesaj3}'")
    
    # .format() metodu
    print("\n2. .format() Metodu:")
    mesaj4 = "Adım {}, yaşım {}".format(ad, yas)
    print(f"Basit: {mesaj4}")
    
    mesaj5 = "Adım {0}, yaşım {1}, tekrar adım {0}".format(ad, yas)
    print(f"İndeksli: {mesaj5}")
    
    mesaj6 = "Adım {ad}, yaşım {yas}".format(ad=ad, yas=yas)
    print(f"İsimli: {mesaj6}")
    
    # f-string (Python 3.6+, önerilen)
    print("\n3. f-string (önerilen):")
    mesaj7 = f"Adım {ad}, yaşım {yas}"
    print(f"Basit: {mesaj7}")
    
    mesaj8 = f"Maaş: {maas:.2f} TL"
    print(f"Ondalık: {mesaj8}")
    
    mesaj9 = f"Ad: {ad:10} Yaş: {yas:3d}"
    print(f"Hizalama: '{mesaj9}'")
    
    # f-string ile hesaplama
    print(f"\n🧮 f-string ile hesaplama:")
    a, b = 15, 4
    print(f"{a} + {b} = {a + b}")
    print(f"{a} / {b} = {a / b:.3f}")
    print(f"Kare: {a}² = {a**2}")
    
    # f-string ile fonksiyon çağırma
    print(f"\n⚙️ f-string ile fonksiyon:")
    metin = "python"
    print(f"Büyük harf: {metin.upper()}")
    print(f"Uzunluk: {len(metin)}")
    print(f"Ters: {metin[::-1]}")

string_formatlama_temel()

# =============================================================================
# 6. STRİNG ENCODING VE UNICODE
# =============================================================================

print("\n=== String Encoding ve Unicode ===")

def string_encoding_unicode():
    """String encoding ve Unicode işlemleri"""
    
    print("🌍 Unicode ve Encoding:")
    
    # Unicode string
    turkce_metin = "Türkçe karakterler: çğıöşü"
    print(f"Türkçe metin: {turkce_metin}")
    
    # String'i bytes'a çevirme (encoding)
    utf8_bytes = turkce_metin.encode('utf-8')
    print(f"UTF-8 bytes: {utf8_bytes}")
    
    ascii_bytes = turkce_metin.encode('ascii', errors='ignore')
    print(f"ASCII (ignore): {ascii_bytes}")
    
    ascii_replace = turkce_metin.encode('ascii', errors='replace')
    print(f"ASCII (replace): {ascii_replace}")
    
    # bytes'ı string'e çevirme (decoding)
    geri_cevrilen = utf8_bytes.decode('utf-8')
    print(f"Geri çevrilmiş: {geri_cevrilen}")
    
    print(f"\n🔤 Unicode kod noktaları:")
    print(f"'A' karakter kodu: {ord('A')}")
    print(f"'ç' karakter kodu: {ord('ç')}")
    print(f"Kod 65: '{chr(65)}'")
    print(f"Kod 231: '{chr(231)}'")
    
    # Unicode escape
    print(f"\n🔣 Unicode escape:")
    unicode_escape = "Unicode: \u0041\u0042\u0043"  # ABC
    print(f"Unicode escape: {unicode_escape}")
    
    emoji = "Python \U0001F40D"  # 🐍
    print(f"Emoji: {emoji}")
    
    # Karakter analizi
    print(f"\n🔍 Karakter analizi:")
    for char in "Aç1":
        print(f"'{char}': ASCII={ord(char)}, isalpha={char.isalpha()}, isdigit={char.isdigit()}")

string_encoding_unicode()

# =============================================================================
# 7. STRİNG KARŞILAŞTIRMA VE SIRALAMA
# =============================================================================

print("\n=== String Karşılaştırma ve Sıralama ===")

def string_karsilastirma():
    """String karşılaştırma ve sıralama işlemleri"""
    
    print("⚖️ String Karşılaştırma:")
    
    # Temel karşılaştırma
    str1 = "Python"
    str2 = "python"
    str3 = "Python"
    
    print(f"'{str1}' == '{str2}': {str1 == str2}")
    print(f"'{str1}' == '{str3}': {str1 == str3}")
    print(f"'{str1}' < '{str2}': {str1 < str2}")  # ASCII karşılaştırma
    
    # Büyük/küçük harf duyarsız karşılaştırma
    print(f"\n🔄 Büyük/küçük harf duyarsız:")
    print(f"lower() ile: {str1.lower() == str2.lower()}")
    print(f"casefold() ile: {str1.casefold() == str2.casefold()}")
    
    # Türkçe karakterlerle
    tr1 = "İstanbul"
    tr2 = "istanbul"
    print(f"Türkçe lower(): {tr1.lower() == tr2}")
    print(f"Türkçe casefold(): {tr1.casefold() == tr2.casefold()}")
    
    print(f"\n📊 String Sıralama:")
    sehirler = ["İstanbul", "ankara", "İzmir", "Bursa", "adana"]
    print(f"Orijinal: {sehirler}")
    
    # Varsayılan sıralama (ASCII)
    ascii_sirali = sorted(sehirler)
    print(f"ASCII sırası: {ascii_sirali}")
    
    # Büyük/küçük harf duyarsız sıralama
    buyukluk_duyarsiz = sorted(sehirler, key=str.lower)
    print(f"Büyüklük duyarsız: {buyukluk_duyarsiz}")
    
    # Ters sıralama
    ters_sirali = sorted(sehirler, reverse=True)
    print(f"Ters sıra: {ters_sirali}")
    
    # Uzunluğa göre sıralama
    uzunluk_sirali = sorted(sehirler, key=len)
    print(f"Uzunluğa göre: {uzunluk_sirali}")
    
    print(f"\n🔍 String içinde arama:")
    metin = "Python programlama dili çok güçlüdür"
    
    # in operatörü
    print(f"'Python' in metin: {'Python' in metin}")
    print(f"'Java' in metin: {'Java' in metin}")
    
    # Büyük/küçük harf duyarsız arama
    aranan = "PYTHON"
    print(f"'{aranan}' duyarsız arama: {aranan.lower() in metin.lower()}")

string_karsilastirma()

# =============================================================================
# 8. STRİNG VALİDASYON VE TEMİZLEME
# =============================================================================

print("\n=== String Validasyon ve Temizleme ===")

def string_validasyon_temizleme():
    """String validasyon ve temizleme işlemleri"""
    
    print("✅ String Validasyon:")
    
    def email_valid_mi(email):
        """Basit email validasyonu"""
        return "@" in email and "." in email.split("@")[-1]
    
    def telefon_valid_mi(telefon):
        """Basit telefon validasyonu"""
        # Sadece rakam ve +, -, (, ), boşluk kabul et
        temiz_telefon = telefon.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
        if temiz_telefon.startswith("+"):
            temiz_telefon = temiz_telefon[1:]
        return temiz_telefon.isdigit() and 10 <= len(temiz_telefon) <= 15
    
    def tc_kimlik_valid_mi(tc):
        """TC kimlik no validasyonu"""
        if not tc.isdigit() or len(tc) != 11:
            return False
        if tc[0] == '0':
            return False
        
        # Basit checksum kontrolü
        tek_toplam = sum(int(tc[i]) for i in range(0, 9, 2))
        cift_toplam = sum(int(tc[i]) for i in range(1, 8, 2))
        
        if (tek_toplam * 7 - cift_toplam) % 10 != int(tc[9]):
            return False
        
        if (tek_toplam + cift_toplam + int(tc[9])) % 10 != int(tc[10]):
            return False
        
        return True
    
    # Test örnekleri
    test_emails = ["user@domain.com", "invalid.email", "test@", "@domain.com"]
    test_telefonlar = ["+90 555 123 4567", "555-123-4567", "abcd", "123"]
    test_tc = ["12345678901", "98765432101", "12345678902"]
    
    print("📧 Email validasyon:")
    for email in test_emails:
        print(f"  {email:15} : {email_valid_mi(email)}")
    
    print("\n📞 Telefon validasyon:")
    for telefon in test_telefonlar:
        print(f"  {telefon:15} : {telefon_valid_mi(telefon)}")
    
    print("\n🆔 TC Kimlik validasyon:")
    for tc in test_tc:
        print(f"  {tc:15} : {tc_kimlik_valid_mi(tc)}")
    
    print(f"\n🧹 String Temizleme:")
    
    def temizle_metin(metin):
        """Metni temizle"""
        # Baş ve sondaki boşlukları kaldır
        temiz = metin.strip()
        
        # Çoklu boşlukları tek boşluğa çevir
        import re
        temiz = re.sub(r'\s+', ' ', temiz)
        
        # Özel karakterleri kaldır (sadece harf, rakam, boşluk bırak)
        temiz = ''.join(char for char in temiz if char.isalnum() or char.isspace())
        
        return temiz
    
    def sadece_rakamlar(metin):
        """Sadece rakamları al"""
        return ''.join(char for char in metin if char.isdigit())
    
    def sadece_harfler(metin):
        """Sadece harfleri al"""
        return ''.join(char for char in metin if char.isalpha())
    
    # Test
    kirli_metin = "   Merhaba!!! Dünya...  123   $$$ Test  "
    print(f"Orijinal: '{kirli_metin}'")
    print(f"Temizlenmiş: '{temizle_metin(kirli_metin)}'")
    print(f"Sadece rakamlar: '{sadece_rakamlar(kirli_metin)}'")
    print(f"Sadece harfler: '{sadece_harfler(kirli_metin)}'")

string_validasyon_temizleme()

# =============================================================================
# 9. STRİNG PERFORMANS İPUÇLARI
# =============================================================================

print("\n=== String Performance İpuçları ===")

def string_performance():
    """String performance ipuçları"""
    
    print("⚡ String Performance Tips:")
    
    import time
    
    # String concatenation performance
    def test_concat_plus():
        """+ operatörü ile birleştirme"""
        result = ""
        for i in range(1000):
            result += str(i)
        return result
    
    def test_concat_join():
        """join() ile birleştirme"""
        parts = []
        for i in range(1000):
            parts.append(str(i))
        return "".join(parts)
    
    def test_concat_format():
        """f-string ile birleştirme"""
        parts = [str(i) for i in range(1000)]
        return "".join(parts)
    
    # Performance test
    print("\n🏎️ Concatenation Performance Test:")
    
    start = time.perf_counter()
    result1 = test_concat_plus()
    time1 = time.perf_counter() - start
    
    start = time.perf_counter()
    result2 = test_concat_join()
    time2 = time.perf_counter() - start
    
    print(f"+ operatörü: {time1:.6f} saniye")
    print(f"join(): {time2:.6f} saniye")
    print(f"join() {time1/time2:.1f}x daha hızlı")
    
    print(f"\n💡 Performance İpuçları:")
    tips = [
        "Çok sayıda string birleştirme için join() kullanın",
        "String formatting için f-string tercih edin",
        "Büyük/küçük harf dönüşümlerini cache'leyin",
        "Regex yerine basit string metodları kullanın (mümkünse)",
        "String immutable'dır, gereksiz kopyalama yapmayın",
        "in operatörü çoğu durumda find()'dan hızlıdır",
        "startswith() ve endswith() slice'dan hızlıdır"
    ]
    
    for i, tip in enumerate(tips, 1):
        print(f"{i}. {tip}")
    
    print(f"\n📝 String Memory Usage:")
    
    # String interning
    a = "Python"
    b = "Python"
    c = "Py" + "thon"
    
    print(f"a is b: {a is b}")  # True (interned)
    print(f"a is c: {a is c}")  # True (optimized)
    
    # Büyük string'ler interned olmaz
    big_a = "Python" * 100
    big_b = "Python" * 100
    print(f"big_a is big_b: {big_a is big_b}")  # False

string_performance()

print("\n💡 String İşlemleri İpuçları:")
print("✅ f-string kullanın (Python 3.6+)")
print("✅ join() ile çoklu birleştirme yapın")
print("✅ strip() ile gereksiz boşlukları temizleyin")
print("✅ startswith()/endswith() ile kontrol yapın")
print("✅ String metodlarını zincirleyebilirsiniz")
print("✅ Unicode ve encoding'e dikkat edin")
print("✅ Validasyon fonksiyonları yazın")

print("\n⚠️ Dikkat Edilecek Noktalar:")
print("• String'ler immutable'dır (değiştirilemez)")
print("• + operatörü çok kullanımda yavaştır")
print("• Büyük/küçük harf duyarlılığına dikkat edin")
print("• Unicode karakterlerle çalışırken encoding belirtin")
print("• Regex kullanmadan önce basit string metodlarını deneyin")

print("\n✅ Python string temel işlemleri öğrenildi!")
print("✅ String formatlandırma yöntemleri öğrenildi!")
print("✅ Encoding ve Unicode işlemleri öğrenildi!")
print("✅ Performance optimizasyonu teknikleri öğrenildi!")