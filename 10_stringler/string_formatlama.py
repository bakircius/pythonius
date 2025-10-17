"""
Python String Formatlandırma ve Manipülasyon

Bu dosya Python'da string formatlandırma yöntemlerini (%, .format(), f-string)
ve gelişmiş string manipülasyon tekniklerini detaylı olarak ele alır.
Template strings, custom formatters ve ileri seviye teknikleri öğreneceğiz.
"""

import string
import datetime
from decimal import Decimal

# =============================================================================
# 1. % (PRINTF-STYLE) FORMATLANDİRMA
# =============================================================================

print("=== % (Printf-Style) Formatlandırma ===")

def printf_style_formatting():
    """Printf-style string formatlandırma"""
    
    print("📝 Temel % Formatlandırma:")
    
    # Temel tipler
    ad = "Ahmet"
    yas = 25
    boy = 175.5
    aktif = True
    
    print(f"String: 'Adım %s' % ad = {'Adım %s' % ad}")
    print(f"Integer: 'Yaşım %d' % yas = {'Yaşım %d' % yas}")
    print(f"Float: 'Boyum %.1f' % boy = {'Boyum %.1f' % boy}")
    print(f"Boolean: 'Aktif %s' % aktif = {'Aktif %s' % aktif}")
    
    print(f"\n🎯 Gelişmiş % Formatlandırma:")
    
    # Genişlik ve hizalama
    print(f"Sağa hizala: '%10s' % ad = {'%10s' % ad}")
    print(f"Sola hizala: '%-10s' % ad = {'%-10s' % ad}")
    print(f"Sıfır padding: '%05d' % yas = {'%05d' % yas}")
    
    # Ondalık hassasiyet
    pi = 3.14159265359
    print(f"2 ondalık: '%.2f' % pi = {'%.2f' % pi}")
    print(f"4 ondalık: '%.4f' % pi = {'%.4f' % pi}")
    print(f"Bilimsel: '%.2e' % (pi * 1000) = {'%.2e' % (pi * 1000)}")
    
    # Birden fazla değer
    print(f"\n🔢 Çoklu değerler:")
    mesaj = "Adım %s, yaşım %d, boyum %.1f cm" % (ad, yas, boy)
    print(f"Çoklu: {mesaj}")
    
    # Dictionary ile
    veriler = {'ad': ad, 'yas': yas, 'boy': boy}
    dict_mesaj = "Adım %(ad)s, yaşım %(yas)d, boyum %(boy).1f cm" % veriler
    print(f"Dictionary: {dict_mesaj}")
    
    print(f"\n🎨 Özel formatlar:")
    
    # Hexadecimal
    sayi = 255
    print(f"Hex (küçük): '%x' % sayi = {'%x' % sayi}")
    print(f"Hex (büyük): '%X' % sayi = {'%X' % sayi}")
    print(f"Octal: '%o' % sayi = {'%o' % sayi}")
    
    # Yüzde işareti
    oran = 75.5
    print(f"Yüzde: '%.1f%%' % oran = {'%.1f%%' % oran}")

printf_style_formatting()

# =============================================================================
# 2. .format() METODu
# =============================================================================

print("\n=== .format() Metodu ===")

def format_method():
    """String .format() metodu"""
    
    print("📝 Temel .format() Kullanımı:")
    
    ad = "Ayşe"
    yas = 30
    maas = 8500.75
    
    # Pozisyonel argümanlar
    mesaj1 = "Adım {}, yaşım {}".format(ad, yas)
    print(f"Pozisyonel: {mesaj1}")
    
    # İndeksli argümanlar
    mesaj2 = "Adım {0}, yaşım {1}, tekrar adım {0}".format(ad, yas)
    print(f"İndeksli: {mesaj2}")
    
    # İsimli argümanlar
    mesaj3 = "Adım {ad}, yaşım {yas}, maaşım {maas}".format(ad=ad, yas=yas, maas=maas)
    print(f"İsimli: {mesaj3}")
    
    # Karışık kullanım
    mesaj4 = "{0} {ad} yaşında, maaşı {1:.2f}".format(yas, maas, ad=ad)
    print(f"Karışık: {mesaj4}")
    
    print(f"\n🎯 Format Specifiers:")
    
    sayi = 1234.5678
    
    # Sayı formatları
    print(f"İnteger: '{{:d}}'.format(1234) = {'{:d}'.format(1234)}")
    print(f"Float: '{{:.2f}}'.format(sayi) = {'{:.2f}'.format(sayi)}")
    print(f"Exponential: '{{:.2e}}'.format(sayi) = {'{:.2e}'.format(sayi)}")
    print(f"Percentage: '{{:.1%}}'.format(0.755) = {'{:.1%}'.format(0.755)}")
    
    # Hizalama ve padding
    print(f"\n📐 Hizalama ve Padding:")
    metin = "Python"
    print(f"Merkez: '{{:^20}}'.format(metin) = '{metin:^20}'")
    print(f"Sol: '{{:<20}}'.format(metin) = '{metin:<20}'")
    print(f"Sağ: '{{:>20}}'.format(metin) = '{metin:>20}'")
    print(f"Özel char: '{{:*^20}}'.format(metin) = '{metin:*^20}'")
    
    # Sayı formatları
    print(f"\n🔢 Sayı Formatları:")
    big_number = 1234567
    print(f"Binlik ayırıcı: '{{:,}}'.format(big_number) = {big_number:,}")
    print(f"Binary: '{{:b}}'.format(255) = {255:b}")
    print(f"Hex: '{{:x}}'.format(255) = {255:x}")
    print(f"Octal: '{{:o}}'.format(255) = {255:o}")
    
    print(f"\n📊 Dictionary ve Object Formatting:")
    
    # Dictionary formatting
    person = {'ad': 'Mehmet', 'yas': 35, 'sehir': 'Ankara'}
    dict_format = "Adım {ad}, yaşım {yas}, şehrim {sehir}".format(**person)
    print(f"Dictionary: {dict_format}")
    
    # Attribute formatting
    class Person:
        def __init__(self, ad, yas):
            self.ad = ad
            self.yas = yas
    
    p = Person("Fatma", 28)
    attr_format = "Adım {p.ad}, yaşım {p.yas}".format(p=p)
    print(f"Attribute: {attr_format}")
    
    # List/tuple formatting
    sayilar = [1, 2, 3, 4, 5]
    list_format = "İlk üç sayı: {0[0]}, {0[1]}, {0[2]}".format(sayilar)
    print(f"List indexing: {list_format}")

format_method()

# =============================================================================
# 3. F-STRING (FORMATTED STRING LITERALS)
# =============================================================================

print("\n=== f-string (Formatted String Literals) ===")

def f_string_formatting():
    """f-string formatlandırma (Python 3.6+)"""
    
    print("🚀 f-string - Modern Formatlandırma:")
    
    ad = "Ali"
    yas = 27
    maas = 9500.50
    aktif = True
    
    # Temel kullanım
    print(f"Temel: Adım {ad}, yaşım {yas}")
    
    # Hesaplama
    print(f"Hesaplama: {yas} + 5 = {yas + 5}")
    print(f"Çarpma: {maas} * 12 = {maas * 12:,.2f}")
    
    # Fonksiyon çağırma
    print(f"Fonksiyon: {ad.upper()}, uzunluk: {len(ad)}")
    
    print(f"\n🎨 f-string Format Specifiers:")
    
    # Sayı formatları
    pi = 3.14159265359
    print(f"2 ondalık: {pi:.2f}")
    print(f"4 ondalık: {pi:.4f}")
    print(f"Bilimsel: {pi:.2e}")
    print(f"Yüzde: {0.75:.1%}")
    
    # Hizalama
    print(f"Sol hizalı: '{ad:<15}'")
    print(f"Sağ hizalı: '{ad:>15}'")
    print(f"Merkez: '{ad:^15}'")
    print(f"Doldurma: '{ad:*^15}'")
    
    # Sayı formatları
    big_num = 1234567890
    print(f"Binlik ayraç: {big_num:,}")
    print(f"Binary: {255:b}")
    print(f"Hex: {255:x}")
    print(f"Hex (büyük): {255:X}")
    
    print(f"\n🔧 Gelişmiş f-string Kullanımı:")
    
    # Conditional expression
    durum = "aktif" if aktif else "pasif"
    print(f"Durum: {durum}")
    
    # Nested f-strings
    precision = 3
    print(f"Pi {precision} ondalık: {pi:.{precision}f}")
    
    # Dictionary access
    person = {'ad': 'Zeynep', 'yas': 32}
    print(f"Dictionary: {person['ad']} {person['yas']} yaşında")
    
    # List/tuple access
    renkler = ['kırmızı', 'yeşil', 'mavi']
    print(f"Renkler: {renkler[0]}, {renkler[1]}, {renkler[2]}")
    
    # Method chaining
    metin = "python programming"
    print(f"Transformed: {metin.title().replace(' ', '_')}")
    
    print(f"\n📅 Tarih ve Zaman Formatları:")
    
    now = datetime.datetime.now()
    print(f"Tarih: {now:%Y-%m-%d}")
    print(f"Zaman: {now:%H:%M:%S}")
    print(f"Tam: {now:%Y-%m-%d %H:%M:%S}")
    print(f"Türkçe: {now:%d.%m.%Y %H:%M}")
    
    # Custom format
    dogum = datetime.date(1990, 5, 15)
    print(f"Doğum tarihi: {dogum:%d %B %Y}")

f_string_formatting()

# =============================================================================
# 4. TEMPLATE STRINGS
# =============================================================================

print("\n=== Template Strings ===")

def template_strings():
    """String Template kullanımı"""
    
    print("📋 Template String Kullanımı:")
    
    # Basit template
    template = string.Template("Merhaba $ad, yaşınız $yas")
    
    # substitute() ile değiştirme
    result1 = template.substitute(ad="Ahmet", yas=25)
    print(f"substitute(): {result1}")
    
    # Dictionary ile
    veriler = {'ad': 'Ayşe', 'yas': 30}
    result2 = template.substitute(veriler)
    print(f"Dictionary ile: {result2}")
    
    # safe_substitute() - eksik değişkenler için güvenli
    template2 = string.Template("$ad $soyad $yas yaşında")
    result3 = template2.safe_substitute(ad="Mehmet", yas=35)
    print(f"safe_substitute(): {result3}")  # $soyad kalır
    
    print(f"\n🔧 Özel Template Delimiters:")
    
    # Özel delimiter
    class CustomTemplate(string.Template):
        delimiter = '#'
    
    custom_template = CustomTemplate("Merhaba #ad, bugün #tarih")
    custom_result = custom_template.substitute(
        ad="Ali",
        tarih=datetime.date.today().strftime("%d.%m.%Y")
    )
    print(f"Özel delimiter: {custom_result}")
    
    print(f"\n📝 Template Kullanım Alanları:")
    
    # Email template
    email_template = string.Template("""
Sayın $ad $soyad,

$tarih tarihinde $konu konulu başvurunuz alınmıştır.
Başvuru numaranız: $basvuru_no

Takip için: $url?id=$basvuru_no

İyi günler,
$sirket
""")
    
    email_data = {
        'ad': 'Ahmet',
        'soyad': 'Yılmaz',
        'tarih': '15.03.2024',
        'konu': 'İş Başvurusu',
        'basvuru_no': 'BS2024001',
        'url': 'https://sirket.com/takip',
        'sirket': 'ABC Şirketi'
    }
    
    email = email_template.substitute(email_data)
    print(f"Email template:")
    print(email)
    
    # SQL template
    sql_template = string.Template("""
SELECT $columns
FROM $table
WHERE $condition
ORDER BY $order_by
LIMIT $limit
""")
    
    sql_query = sql_template.substitute(
        columns="ad, soyad, yas",
        table="kullanicilar",
        condition="yas > 18",
        order_by="ad",
        limit=10
    )
    print(f"SQL template:")
    print(sql_query)

template_strings()

# =============================================================================
# 5. GELİŞMİŞ FORMAT TEKNİKLERİ
# =============================================================================

print("\n=== Gelişmiş Format Teknikleri ===")

def gelismis_format_teknikleri():
    """Gelişmiş string formatlandırma teknikleri"""
    
    print("🎯 Conditional Formatting:")
    
    # Koşullu formatlandırma
    def format_status(aktif):
        return f"{'✅ Aktif' if aktif else '❌ Pasif'}"
    
    users = [
        {'ad': 'Ali', 'aktif': True},
        {'ad': 'Ayşe', 'aktif': False},
        {'ad': 'Mehmet', 'aktif': True}
    ]
    
    for user in users:
        print(f"{user['ad']:10} - {format_status(user['aktif'])}")
    
    print(f"\n📊 Tablo Formatlandırma:")
    
    # Tablo formatı
    products = [
        {'ad': 'Laptop', 'fiyat': 15000, 'stok': 5},
        {'ad': 'Mouse', 'fiyat': 150, 'stok': 25},
        {'ad': 'Klavye', 'fiyat': 300, 'stok': 12},
        {'ad': 'Monitor', 'fiyat': 2500, 'stok': 8}
    ]
    
    # Header
    print(f"{'Ürün':<12} {'Fiyat':>8} {'Stok':>6}")
    print("-" * 30)
    
    # Rows
    for product in products:
        print(f"{product['ad']:<12} {product['fiyat']:>8,} {product['stok']:>6}")
    
    print(f"\n💰 Para Formatları:")
    
    # Para formatları
    amounts = [1234.56, 0.50, 1000000.75, -500.25]
    
    for amount in amounts:
        # Türk Lirası formatı
        tl_format = f"{amount:,.2f} ₺"
        
        # Pozitif/negatif renklendirme (konsol için)
        if amount >= 0:
            print(f"Tutar: {tl_format:>15}")
        else:
            print(f"Tutar: {tl_format:>15} (Borç)")
    
    print(f"\n🌍 Çok Dilli Formatlar:")
    
    # Çok dilli formatlar
    messages = {
        'tr': "Merhaba {ad}, {tarih} tarihinde {miktar:.2f} ₺ ödemeniz var.",
        'en': "Hello {ad}, you have a payment of ${miktar:.2f} on {tarih}.",
        'de': "Hallo {ad}, Sie haben eine Zahlung von {miktar:.2f}€ am {tarih}."
    }
    
    data = {
        'ad': 'Ahmet',
        'tarih': '15.03.2024',
        'miktar': 150.75
    }
    
    for lang, template in messages.items():
        formatted = template.format(**data)
        print(f"{lang.upper()}: {formatted}")
    
    print(f"\n🎨 Özel Format Sınıfları:")
    
    # Özel format sınıfı
    class ColorFormat:
        """Renkli metin formatları"""
        
        COLORS = {
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            'purple': '\033[95m',
            'cyan': '\033[96m',
            'white': '\033[97m',
            'end': '\033[0m'
        }
        
        @classmethod
        def color(cls, text, color):
            return f"{cls.COLORS.get(color, '')}{text}{cls.COLORS['end']}"
        
        @classmethod
        def success(cls, text):
            return cls.color(f"✅ {text}", 'green')
        
        @classmethod
        def error(cls, text):
            return cls.color(f"❌ {text}", 'red')
        
        @classmethod
        def warning(cls, text):
            return cls.color(f"⚠️ {text}", 'yellow')
        
        @classmethod
        def info(cls, text):
            return cls.color(f"ℹ️ {text}", 'blue')
    
    # Kullanım
    print(ColorFormat.success("İşlem başarılı!"))
    print(ColorFormat.error("Bir hata oluştu!"))
    print(ColorFormat.warning("Dikkat gerekli!"))
    print(ColorFormat.info("Bilgi mesajı"))

gelismis_format_teknikleri()

# =============================================================================
# 6. STRİNG MANİPÜLASYON TEKNİKLERİ
# =============================================================================

print("\n=== String Manipülasyon Teknikleri ===")

def string_manipulation_teknikleri():
    """Gelişmiş string manipülasyon teknikleri"""
    
    print("🔧 Gelişmiş String İşlemleri:")
    
    # Text cleaning pipeline
    def clean_text(text):
        """Metin temizleme pipeline'ı"""
        import re
        
        # HTML etiketlerini kaldır
        text = re.sub(r'<[^>]+>', '', text)
        
        # Çoklu boşlukları tek boşluğa çevir
        text = re.sub(r'\s+', ' ', text)
        
        # Özel karakterleri temizle
        text = re.sub(r'[^\w\s-]', '', text)
        
        # Baş ve son boşlukları kaldır
        text = text.strip()
        
        return text
    
    dirty_text = "<p>Bu   bir    <strong>test</strong> metnidir!!!   </p>"
    clean = clean_text(dirty_text)
    print(f"Orijinal: {dirty_text}")
    print(f"Temiz: {clean}")
    
    print(f"\n📝 Text Normalization:")
    
    # Text normalization
    def normalize_text(text):
        """Metin normalleştirme"""
        # Türkçe karakterleri İngilizce'ye çevir
        tr_chars = "çğıöşüÇĞIÖŞÜ"
        en_chars = "cgiosuCGIOSU"
        
        translation = str.maketrans(tr_chars, en_chars)
        normalized = text.translate(translation)
        
        # Küçük harfe çevir
        normalized = normalized.lower()
        
        # Sadece alfanumerik karakterler ve boşluk bırak
        import re
        normalized = re.sub(r'[^a-z0-9\s]', '', normalized)
        
        return normalized
    
    turkish_text = "Çok güzel bir gün! İstanbul'da hava çok güzel."
    normalized = normalize_text(turkish_text)
    print(f"Türkçe: {turkish_text}")
    print(f"Normalized: {normalized}")
    
    print(f"\n🔄 String Transformations:")
    
    # String dönüşümleri
    def transform_text(text, transformations):
        """Metin dönüşümleri uygula"""
        for transform in transformations:
            text = transform(text)
        return text
    
    # Dönüşüm fonksiyonları
    transformations = [
        str.strip,
        str.lower,
        lambda x: x.replace(' ', '_'),
        lambda x: x.replace('ı', 'i'),
        lambda x: x.replace('ğ', 'g'),
        lambda x: x.replace('ş', 's'),
        lambda x: x.replace('ç', 'c'),
        lambda x: x.replace('ö', 'o'),
        lambda x: x.replace('ü', 'u')
    ]
    
    test_text = "  Çok Güzel Bir Şehir  "
    transformed = transform_text(test_text, transformations)
    print(f"Orijinal: '{test_text}'")
    print(f"Transformed: '{transformed}'")
    
    print(f"\n🎭 Text Masking:")
    
    # Metin maskeleme
    def mask_email(email):
        """Email adresini maskele"""
        if '@' not in email:
            return email
        
        local, domain = email.split('@')
        if len(local) <= 2:
            masked_local = '*' * len(local)
        else:
            masked_local = local[0] + '*' * (len(local) - 2) + local[-1]
        
        return f"{masked_local}@{domain}"
    
    def mask_phone(phone):
        """Telefon numarasını maskele"""
        digits_only = ''.join(c for c in phone if c.isdigit())
        if len(digits_only) >= 7:
            return digits_only[:3] + '*' * (len(digits_only) - 6) + digits_only[-3:]
        return '*' * len(digits_only)
    
    def mask_credit_card(card):
        """Kredi kartı numarasını maskele"""
        digits_only = ''.join(c for c in card if c.isdigit())
        if len(digits_only) == 16:
            return f"{digits_only[:4]} **** **** {digits_only[-4:]}"
        return '*' * len(digits_only)
    
    # Test masking
    test_data = [
        ("Email", "ahmet.yilmaz@email.com", mask_email),
        ("Telefon", "0555 123 4567", mask_phone),
        ("Kredi Kartı", "1234 5678 9012 3456", mask_credit_card)
    ]
    
    for data_type, original, mask_func in test_data:
        masked = mask_func(original)
        print(f"{data_type}: {original} -> {masked}")

string_manipulation_teknikleri()

# =============================================================================
# 7. STRİNG VALİDASYON VE PARSE
# =============================================================================

print("\n=== String Validasyon ve Parse ===")

def string_validation_parse():
    """String validasyon ve parse işlemleri"""
    
    print("✅ Gelişmiş Validasyon:")
    
    import re
    
    # Regex patterns
    patterns = {
        'email': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        'phone_tr': r'^(\+90|0)?[5][0-9]{9}$',
        'tc_kimlik': r'^[1-9][0-9]{10}$',
        'iban_tr': r'^TR\d{2}\s?\d{4}\s?\d{4}\s?\d{4}\s?\d{4}\s?\d{4}\s?\d{2}$',
        'ipv4': r'^(\d{1,3}\.){3}\d{1,3}$',
        'url': r'^https?://[^\s/$.?#].[^\s]*$'
    }
    
    def validate_with_regex(text, pattern_name):
        """Regex ile validasyon"""
        pattern = patterns.get(pattern_name)
        if not pattern:
            return False, "Pattern bulunamadı"
        
        if re.match(pattern, text):
            return True, "Geçerli"
        else:
            return False, "Geçersiz format"
    
    # Test verisi
    test_data = [
        ("email", "user@domain.com"),
        ("email", "invalid.email"),
        ("phone_tr", "05551234567"),
        ("phone_tr", "123456"),
        ("tc_kimlik", "12345678901"),
        ("iban_tr", "TR12 3456 7890 1234 5678 9012 34"),
        ("ipv4", "192.168.1.1"),
        ("url", "https://www.example.com")
    ]
    
    for pattern_name, test_value in test_data:
        is_valid, message = validate_with_regex(test_value, pattern_name)
        status = "✅" if is_valid else "❌"
        print(f"{status} {pattern_name}: {test_value} - {message}")
    
    print(f"\n🔍 String Parsing:")
    
    # URL parsing
    def parse_url(url):
        """URL'yi parse et"""
        import urllib.parse
        parsed = urllib.parse.urlparse(url)
        return {
            'scheme': parsed.scheme,
            'netloc': parsed.netloc,
            'path': parsed.path,
            'params': parsed.params,
            'query': parsed.query,
            'fragment': parsed.fragment
        }
    
    url = "https://www.example.com/path?param1=value1&param2=value2#section"
    parsed_url = parse_url(url)
    print(f"URL: {url}")
    for key, value in parsed_url.items():
        print(f"  {key}: {value}")
    
    # Log parsing
    def parse_log_line(log_line):
        """Log satırını parse et"""
        # Apache log format
        pattern = r'(\S+) \S+ \S+ \[([\w:/]+\s[+\-]\d{4})\] "(\S+) (\S+) (\S+)" (\d{3}) (\d+)'
        match = re.match(pattern, log_line)
        
        if match:
            return {
                'ip': match.group(1),
                'timestamp': match.group(2),
                'method': match.group(3),
                'url': match.group(4),
                'protocol': match.group(5),
                'status': int(match.group(6)),
                'size': int(match.group(7))
            }
        return None
    
    log_line = '192.168.1.1 - - [25/Dec/2023:10:00:00 +0000] "GET /index.html HTTP/1.1" 200 2326'
    parsed_log = parse_log_line(log_line)
    if parsed_log:
        print(f"\nLog parsing:")
        for key, value in parsed_log.items():
            print(f"  {key}: {value}")

string_validation_parse()

# =============================================================================
# 8. PERFORMANS VE BEST PRACTICES
# =============================================================================

print("\n=== Performance ve Best Practices ===")

def performance_best_practices():
    """String formatlandırma performance ve best practices"""
    
    import time
    
    print("⚡ Performance Comparison:")
    
    # Test data
    name = "Ahmet"
    age = 25
    salary = 5500.75
    
    # Performance test
    def test_performance(iterations=10000):
        """Format performansını test et"""
        
        # % formatting
        start = time.perf_counter()
        for _ in range(iterations):
            result = "Adım %s, yaşım %d, maaşım %.2f" % (name, age, salary)
        percent_time = time.perf_counter() - start
        
        # .format()
        start = time.perf_counter()
        for _ in range(iterations):
            result = "Adım {}, yaşım {}, maaşım {:.2f}".format(name, age, salary)
        format_time = time.perf_counter() - start
        
        # f-string
        start = time.perf_counter()
        for _ in range(iterations):
            result = f"Adım {name}, yaşım {age}, maaşım {salary:.2f}"
        fstring_time = time.perf_counter() - start
        
        return percent_time, format_time, fstring_time
    
    percent_time, format_time, fstring_time = test_performance()
    
    print(f"% formatting: {percent_time:.6f}s")
    print(f".format():    {format_time:.6f}s")
    print(f"f-string:     {fstring_time:.6f}s")
    
    # En hızlı olanı bul
    times = [('% formatting', percent_time), ('.format()', format_time), ('f-string', fstring_time)]
    fastest = min(times, key=lambda x: x[1])
    
    print(f"\nEn hızlı: {fastest[0]}")
    
    print(f"\n💡 Best Practices:")
    
    best_practices = [
        "✅ Python 3.6+ için f-string kullanın",
        "✅ Template string'leri user input için kullanın",
        "✅ Çok sayıda formatlandırma için caching düşünün",
        "✅ Regex yerine string metodlarını tercih edin",
        "✅ join() ile string concatenation yapın",
        "✅ Validasyon için try-except kullanın",
        "✅ Unicode karakterlerle dikkatli olun",
        "✅ Memory-intensive uygulamalarda string interning'i araştırın"
    ]
    
    for practice in best_practices:
        print(practice)
    
    print(f"\n⚠️ Yaygın Hatalar:")
    
    common_mistakes = [
        "❌ + operatörü ile çok sayıda string birleştirmek",
        "❌ User input'u doğrudan format string'e koymak",
        "❌ Encoding belirtmeden dosya okumak",
        "❌ Regex için ham string kullanmamak",
        "❌ Exception handling yapmadan index() kullanmak",
        "❌ Case-sensitive karşılaştırma yapmak",
        "❌ Strip() kullanmadan user input işlemek"
    ]
    
    for mistake in common_mistakes:
        print(mistake)

performance_best_practices()

print("\n🎉 String Formatlandırma ve Manipülasyon Tamamlandı!")
print("\n📚 Bu bölümde öğrenilenler:")
print("✅ % (printf-style) formatlandırma")
print("✅ .format() metodu ve format specifiers")
print("✅ f-string (modern formatlandırma)")
print("✅ Template strings güvenli formatlandırma")
print("✅ Gelişmiş format teknikleri")
print("✅ String manipülasyon ve transformation")
print("✅ Validation ve parsing teknikleri")
print("✅ Performance optimizasyonu")
print("✅ Best practices ve yaygın hatalar")

print("\n🔗 Sonraki adımlar:")
print("• Regular expressions ile gelişmiş pattern matching")
print("• Uluslararasılaştırma (i18n) ve lokalizasyon")
print("• Text processing ve natural language processing")
print("• Database string operations")
print("• Web scraping ve text extraction")