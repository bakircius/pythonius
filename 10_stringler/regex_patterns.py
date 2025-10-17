"""
Python Regular Expressions (Regex) - Kapsamlı Rehber

Bu dosya Python'da regular expressions (düzenli ifadeler) kullanımını
detaylı olarak ele alır. Pattern matching, text processing ve 
gelişmiş string manipülasyon tekniklerini öğreneceğiz.
"""

import re
import string
from collections import defaultdict

# =============================================================================
# 1. REGEX TEMELLERİ VE SÖZDIZIMI
# =============================================================================

print("=== Regex Temelleri ve Sözdizimi ===")

def regex_temelleri():
    """Regular expressions temelleri"""
    
    print("🎯 Temel Regex Karakterleri:")
    
    # Basit pattern matching
    text = "Python programming language 2024"
    
    # Literal karakter eşleştirme
    pattern1 = "Python"
    match1 = re.search(pattern1, text)
    print(f"'{pattern1}' pattern: {match1.group() if match1 else 'Bulunamadı'}")
    
    # Nokta (.) - herhangi bir karakter
    pattern2 = "P.thon"
    match2 = re.search(pattern2, text)
    print(f"'{pattern2}' pattern: {match2.group() if match2 else 'Bulunamadı'}")
    
    # Yıldız (*) - sıfır veya daha fazla
    pattern3 = "prog.*ing"
    match3 = re.search(pattern3, text)
    print(f"'{pattern3}' pattern: {match3.group() if match3 else 'Bulunamadı'}")
    
    # Artı (+) - bir veya daha fazla
    pattern4 = "Pytho+"
    match4 = re.search(pattern4, text)
    print(f"'{pattern4}' pattern: {match4.group() if match4 else 'Bulunamadı'}")
    
    # Soru işareti (?) - sıfır veya bir
    pattern5 = "Pythons?"
    match5 = re.search(pattern5, text)
    print(f"'{pattern5}' pattern: {match5.group() if match5 else 'Bulunamadı'}")
    
    print(f"\n🔤 Karakter Sınıfları:")
    
    test_text = "ABC123def456GHI"
    
    # Köşeli parantez - karakter seti
    digits = re.findall(r'[0-9]', test_text)
    print(f"Rakamlar [0-9]: {digits}")
    
    uppercase = re.findall(r'[A-Z]', test_text)
    print(f"Büyük harfler [A-Z]: {uppercase}")
    
    lowercase = re.findall(r'[a-z]', test_text)
    print(f"Küçük harfler [a-z]: {lowercase}")
    
    # Olumsuzlama (^)
    not_digits = re.findall(r'[^0-9]', test_text)
    print(f"Rakam olmayanlar [^0-9]: {not_digits}")
    
    print(f"\n⚡ Hazır Karakter Sınıfları:")
    
    sample = "Hello 123 World! @#$"
    
    # \d - rakamlar
    digits = re.findall(r'\d', sample)
    print(f"\\d (rakamlar): {digits}")
    
    # \w - kelime karakterleri (harf, rakam, _)
    word_chars = re.findall(r'\w', sample)
    print(f"\\w (kelime karakterleri): {word_chars}")
    
    # \s - boşluk karakterleri
    spaces = re.findall(r'\s', sample)
    print(f"\\s (boşluk): {repr(spaces)}")
    
    # Büyük harfli versiyonlar (olumsuzlama)
    non_digits = re.findall(r'\D', "abc123def")
    print(f"\\D (rakam olmayanlar): {non_digits}")

regex_temelleri()

# =============================================================================
# 2. REGEX METODLARI VE KULLANIMI
# =============================================================================

print("\n=== Regex Metodları ve Kullanımı ===")

def regex_metodlari():
    """Regex metodları ve kullanımı"""
    
    text = "Python is powerful. Python is easy. Python version 3.11"
    
    print("🔍 re.search() - İlk eşleşmeyi bul:")
    
    # re.search() - ilk eşleşmeyi döner
    match = re.search(r'Python', text)
    if match:
        print(f"Bulundu: '{match.group()}' pozisyon {match.start()}-{match.end()}")
    
    # Groups ile
    email_text = "İletişim: john.doe@company.com veya jane@example.org"
    email_pattern = r'(\w+)@(\w+\.\w+)'
    email_match = re.search(email_pattern, email_text)
    if email_match:
        print(f"Email: {email_match.group()}")
        print(f"Kullanıcı: {email_match.group(1)}")
        print(f"Domain: {email_match.group(2)}")
    
    print(f"\n🔍 re.findall() - Tüm eşleşmeleri bul:")
    
    # re.findall() - tüm eşleşmeleri döner
    all_pythons = re.findall(r'Python', text)
    print(f"Tüm 'Python' kelimeler: {all_pythons}")
    
    # Groups ile findall
    all_emails = re.findall(email_pattern, email_text)
    print(f"Tüm email parts: {all_emails}")
    
    # Sayıları bulma
    numbers_text = "Fiyat: 150.50 TL, İndirim: %25, Toplam: 112.87 TL"
    numbers = re.findall(r'\d+\.?\d*', numbers_text)
    print(f"Sayılar: {numbers}")
    
    print(f"\n🔍 re.finditer() - Match objelerini iterator:")
    
    # re.finditer() - match objelerini iterator olarak döner
    for match in re.finditer(r'Python', text):
        print(f"'{match.group()}' found at {match.start()}-{match.end()}")
    
    print(f"\n🔄 re.sub() - Değiştirme:")
    
    # re.sub() - değiştirme
    replaced = re.sub(r'Python', 'Java', text)
    print(f"Python -> Java: {replaced}")
    
    # Sayılı değiştirme
    replaced_count = re.sub(r'Python', 'Java', text, count=2)
    print(f"İlk 2 değiştir: {replaced_count}")
    
    # Fonksiyon ile değiştirme
    def upper_match(match):
        return match.group().upper()
    
    replaced_func = re.sub(r'Python', upper_match, text)
    print(f"Fonksiyon ile: {replaced_func}")
    
    print(f"\n✂️ re.split() - Bölme:")
    
    # re.split() - bölme
    csv_data = "name,age,city;country|email"
    parts = re.split(r'[,;|]', csv_data)
    print(f"Bölme: {parts}")
    
    # Maksimum bölme
    limited_split = re.split(r'[,;|]', csv_data, maxsplit=2)
    print(f"Max 2 bölme: {limited_split}")

regex_metodlari()

# =============================================================================
# 3. GELİŞMİŞ REGEX PATTERNLERİ
# =============================================================================

print("\n=== Gelişmiş Regex Patterns ===")

def gelismis_patterns():
    """Gelişmiş regex pattern'ları"""
    
    print("🎯 Anchors (Bağlayıcılar):")
    
    text_lines = [
        "Python programming",
        "I love Python",
        "pythonic approach",
        "Programming with Python"
    ]
    
    # ^ - satır başı
    start_pattern = r'^Python'
    for line in text_lines:
        if re.search(start_pattern, line):
            print(f"Başlangıç: '{line}'")
    
    # $ - satır sonu
    end_pattern = r'Python$'
    for line in text_lines:
        if re.search(end_pattern, line):
            print(f"Bitiş: '{line}'")
    
    # \b - kelime sınırı
    print(f"\nKelime sınırı \\b:")
    text = "Python pythonic python-like"
    word_boundary = re.findall(r'\bpython\b', text, re.IGNORECASE)
    print(f"Tam kelime 'python': {word_boundary}")
    
    print(f"\n🔢 Quantifiers (Niceleyiciler):")
    
    # {n} - tam n kez
    phone = "Telefon: 0555-123-4567"
    exact_pattern = re.findall(r'\d{4}', phone)
    print(f"Tam 4 rakam: {exact_pattern}")
    
    # {n,m} - n ile m arası
    range_pattern = re.findall(r'\d{2,4}', phone)
    print(f"2-4 rakam: {range_pattern}")
    
    # {n,} - en az n kez
    min_pattern = re.findall(r'\d{3,}', phone)
    print(f"En az 3 rakam: {min_pattern}")
    
    print(f"\n🎯 Groups ve Captures:")
    
    # Gruplar
    log_line = "2024-03-15 14:30:25 ERROR: Database connection failed"
    log_pattern = r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+): (.+)'
    log_match = re.search(log_pattern, log_line)
    
    if log_match:
        print(f"Tarih: {log_match.group(1)}")
        print(f"Saat: {log_match.group(2)}")
        print(f"Level: {log_match.group(3)}")
        print(f"Mesaj: {log_match.group(4)}")
    
    # Named groups
    named_pattern = r'(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) (?P<level>\w+): (?P<message>.+)'
    named_match = re.search(named_pattern, log_line)
    
    if named_match:
        print(f"\nNamed groups:")
        print(f"Tarih: {named_match.group('date')}")
        print(f"Saat: {named_match.group('time')}")
        print(f"Level: {named_match.group('level')}")
        print(f"Mesaj: {named_match.group('message')}")
    
    # Non-capturing group
    non_capture = r'(?:Mr|Ms|Dr)\. (\w+)'
    names = ["Mr. Smith", "Ms. Johnson", "Dr. Brown"]
    for name in names:
        match = re.search(non_capture, name)
        if match:
            print(f"Sadece isim: {match.group(1)}")
    
    print(f"\n🔄 Lookahead ve Lookbehind:")
    
    # Positive lookahead (?=...)
    password = "password123"
    has_digit = re.search(r'(?=.*\d)', password)
    print(f"Rakam içeriyor: {bool(has_digit)}")
    
    # Negative lookahead (?!...)
    not_admin = re.findall(r'\b(?!admin)\w+', "user admin guest manager")
    print(f"Admin olmayan kelimeler: {not_admin}")
    
    # Positive lookbehind (?<=...)
    prices = "Price: $25.99, Cost: $15.50"
    dollar_amounts = re.findall(r'(?<=\$)\d+\.\d+', prices)
    print(f"Dolar miktarları: {dollar_amounts}")

gelismis_patterns()

# =============================================================================
# 4. REGEX FLAGS VE SEÇENEKLER
# =============================================================================

print("\n=== Regex Flags ve Seçenekler ===")

def regex_flags():
    """Regex flags ve seçenekleri"""
    
    text = """PYTHON Programming
    python development
    Python is GREAT"""
    
    print("🚩 Regex Flags:")
    
    # re.IGNORECASE (re.I) - büyük/küçük harf duyarsız
    case_insensitive = re.findall(r'python', text, re.IGNORECASE)
    print(f"Case insensitive: {case_insensitive}")
    
    # re.MULTILINE (re.M) - çok satırlı mod
    start_lines = re.findall(r'^python', text, re.MULTILINE | re.IGNORECASE)
    print(f"Satır başı 'python': {start_lines}")
    
    # re.DOTALL (re.S) - . karakteri \n ile eşleşir
    multiline_text = "Start\nMiddle\nEnd"
    dotall_match = re.search(r'Start.*End', multiline_text, re.DOTALL)
    print(f"DOTALL match: {dotall_match.group() if dotall_match else 'None'}")
    
    # re.VERBOSE (re.X) - whitespace ve yorum
    verbose_pattern = re.compile(r'''
        (\d{4})         # Yıl
        -               # Ayırıcı
        (\d{2})         # Ay
        -               # Ayırıcı
        (\d{2})         # Gün
    ''', re.VERBOSE)
    
    date_string = "Bugün 2024-03-15 tarihi"
    verbose_match = verbose_pattern.search(date_string)
    if verbose_match:
        print(f"VERBOSE pattern: {verbose_match.groups()}")
    
    print(f"\n⚙️ Compile ve Performance:")
    
    # Pattern compile etme
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    
    emails_text = """
    İletişim bilgileri:
    john@example.com
    invalid.email
    jane.doe@company.org
    test@domain.co.uk
    """
    
    compiled_emails = email_pattern.findall(emails_text)
    print(f"Compiled pattern emails: {compiled_emails}")
    
    # Match object özellikleri
    match = email_pattern.search(emails_text)
    if match:
        print(f"Match string: {match.string[:50]}...")
        print(f"Match span: {match.span()}")
        print(f"Match groups: {match.groups()}")

regex_flags()

# =============================================================================
# 5. PRATIKTE REGEX KULLANIMI
# =============================================================================

print("\n=== Pratikte Regex Kullanımı ===")

def praktik_regex_ornekleri():
    """Pratik regex kullanım örnekleri"""
    
    print("📧 Email Validasyon:")
    
    def email_validator(email):
        """Email validasyon fonksiyonu"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    test_emails = [
        "user@example.com",
        "test.email@domain.co.uk",
        "invalid.email",
        "user@",
        "@domain.com",
        "user.name+tag@example.com"
    ]
    
    for email in test_emails:
        valid = email_validator(email)
        status = "✅" if valid else "❌"
        print(f"{status} {email}")
    
    print(f"\n📞 Telefon Numarası Formatting:")
    
    def format_phone(phone):
        """Telefon numarasını formatla"""
        # Sadece rakamları al
        digits = re.sub(r'\D', '', phone)
        
        # Türkiye telefon formatı
        if len(digits) == 11 and digits.startswith('0'):
            return re.sub(r'(\d{4})(\d{3})(\d{4})', r'\1 \2 \3', digits)
        elif len(digits) == 10:
            return re.sub(r'(\d{3})(\d{3})(\d{4})', r'0\1 \2 \3', digits)
        
        return phone  # Formatlanamadı
    
    phones = [
        "05551234567",
        "0 555 123 45 67",
        "(555) 123-4567",
        "555.123.4567",
        "invalid"
    ]
    
    for phone in phones:
        formatted = format_phone(phone)
        print(f"{phone:15} -> {formatted}")
    
    print(f"\n🌐 URL Extraction:")
    
    def extract_urls(text):
        """Metinden URL'leri çıkar"""
        url_pattern = r'https?://[^\s<>"{}|\\^`\[\]]+'
        return re.findall(url_pattern, text)
    
    text_with_urls = """
    Şu siteleri ziyaret edin:
    https://www.python.org
    http://github.com/python
    https://docs.python.org/3/
    Geçersiz: htp://invalid.url
    """
    
    urls = extract_urls(text_with_urls)
    print("Bulunan URL'ler:")
    for url in urls:
        print(f"  {url}")
    
    print(f"\n📝 Log Parsing:")
    
    def parse_apache_log(log_line):
        """Apache log satırını parse et"""
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
    
    log_lines = [
        '192.168.1.1 - - [25/Dec/2023:10:00:00 +0000] "GET /index.html HTTP/1.1" 200 2326',
        '10.0.0.1 - - [25/Dec/2023:10:01:00 +0000] "POST /login HTTP/1.1" 302 -',
        '203.0.113.1 - - [25/Dec/2023:10:02:00 +0000] "GET /favicon.ico HTTP/1.1" 404 287'
    ]
    
    for log_line in log_lines:
        parsed = parse_apache_log(log_line)
        if parsed:
            print(f"IP: {parsed['ip']:15} Status: {parsed['status']} URL: {parsed['url']}")
    
    print(f"\n💳 Credit Card Masking:")
    
    def mask_credit_card(text):
        """Kredi kartı numaralarını maskele"""
        # 16 haneli kredi kartı pattern'ı
        pattern = r'\b(\d{4})[\s-]?(\d{4})[\s-]?(\d{4})[\s-]?(\d{4})\b'
        
        def replace_func(match):
            return f"{match.group(1)} **** **** {match.group(4)}"
        
        return re.sub(pattern, replace_func, text)
    
    sensitive_text = """
    Müşteri bilgileri:
    Kart 1: 1234 5678 9012 3456
    Kart 2: 4567-8901-2345-6789
    Kart 3: 9876543210123456
    """
    
    masked_text = mask_credit_card(sensitive_text)
    print("Maskelenmiş metin:")
    print(masked_text)

praktik_regex_ornekleri()

# =============================================================================
# 6. REGEX PERFORMANCE VE OPTİMİZASYON
# =============================================================================

print("\n=== Regex Performance ve Optimizasyon ===")

def regex_performance():
    """Regex performance ve optimizasyon teknikleri"""
    
    import time
    
    print("⚡ Performance Optimizasyonu:")
    
    # Test data
    test_text = "Python " * 1000 + "Java " * 500 + "C++ " * 300
    
    # Compiled vs non-compiled pattern
    pattern_string = r'\bPython\b'
    compiled_pattern = re.compile(pattern_string)
    
    # Non-compiled test
    start = time.perf_counter()
    for _ in range(1000):
        re.findall(pattern_string, test_text)
    non_compiled_time = time.perf_counter() - start
    
    # Compiled test
    start = time.perf_counter()
    for _ in range(1000):
        compiled_pattern.findall(test_text)
    compiled_time = time.perf_counter() - start
    
    print(f"Non-compiled: {non_compiled_time:.6f}s")
    print(f"Compiled:     {compiled_time:.6f}s")
    print(f"Speedup:      {non_compiled_time / compiled_time:.2f}x")
    
    print(f"\n💡 Optimization Tips:")
    
    tips = [
        "✅ Tekrar kullanılan pattern'ları compile edin",
        "✅ Specific pattern'ları general pattern'lara tercih edin",
        "✅ Anchors (^, $) kullanarak arama alanını sınırlayın",
        "✅ Non-capturing groups (?:...) kullanın",
        "✅ Possessive quantifiers kullanın (+?, *?, ??)",
        "✅ Character classes yerine literal karakterler tercih edin",
        "✅ Lookahead/lookbehind'ı gereksiz kullanmayın",
        "✅ Büyük metinlerde chunk'lara bölün"
    ]
    
    for tip in tips:
        print(tip)
    
    print(f"\n🐌 Yavaş Pattern'lar:")
    
    # Catastrophic backtracking örneği
    print("⚠️ Dikkat: Catastrophic backtracking")
    
    slow_patterns = [
        r'(a+)+b',              # Çok yavaş!
        r'(a*)*',               # Çok yavaş!
        r'(\w+)+\s',           # Yavaş
        r'.*.*.*=.*',          # Yavaş
    ]
    
    better_patterns = [
        r'a+b',                # Daha iyi
        r'a*',                 # Daha iyi
        r'\w+\s',              # Daha iyi
        r'[^=]*=.*',           # Daha iyi
    ]
    
    print("Yavaş pattern'lar ve alternatifleri:")
    for slow, better in zip(slow_patterns, better_patterns):
        print(f"❌ {slow:15} -> ✅ {better}")
    
    print(f"\n🔧 Debugging Regex:")
    
    def debug_regex(pattern, text, description=""):
        """Regex debug helper"""
        print(f"\n🔍 Debug: {description}")
        print(f"Pattern: {pattern}")
        print(f"Text: {text[:50]}{'...' if len(text) > 50 else ''}")
        
        try:
            compiled = re.compile(pattern)
            matches = compiled.finditer(text)
            
            for i, match in enumerate(matches, 1):
                print(f"Match {i}: '{match.group()}' at {match.span()}")
                if match.groups():
                    print(f"  Groups: {match.groups()}")
                if i >= 5:  # Limit output
                    remaining = len(compiled.findall(text)) - 5
                    if remaining > 0:
                        print(f"  ... and {remaining} more matches")
                    break
                    
        except re.error as e:
            print(f"❌ Regex Error: {e}")
    
    # Debug examples
    debug_regex(r'\b\w{4,}\b', "Python is a powerful programming language", 
                "4+ letter words")
    
    debug_regex(r'(\w+)@(\w+\.\w+)', "Contact: john@example.com or admin@site.org", 
                "Email parsing")

regex_performance()

# =============================================================================
# 7. REGEX UTILITIES VE HELPER FUNCTIONS
# =============================================================================

print("\n=== Regex Utilities ve Helper Functions ===")

def regex_utilities():
    """Regex utility fonksiyonları"""
    
    print("🛠️ Regex Utility Sınıfı:")
    
    class RegexUtils:
        """Regex utility fonksiyonları"""
        
        # Compiled patterns
        EMAIL_PATTERN = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        PHONE_PATTERN = re.compile(r'(\+90|0)?[5-9]\d{2}[\s-]?\d{3}[\s-]?\d{4}')
        URL_PATTERN = re.compile(r'https?://[^\s<>"{}|\\^`\[\]]+')
        IPV4_PATTERN = re.compile(r'\b(\d{1,3}\.){3}\d{1,3}\b')
        DATE_PATTERN = re.compile(r'\b(\d{1,2})[./\-](\d{1,2})[./\-](\d{4})\b')
        
        @classmethod
        def extract_emails(cls, text):
            """Email adreslerini çıkar"""
            return cls.EMAIL_PATTERN.findall(text)
        
        @classmethod
        def extract_phones(cls, text):
            """Telefon numaralarını çıkar"""
            return cls.PHONE_PATTERN.findall(text)
        
        @classmethod
        def extract_urls(cls, text):
            """URL'leri çıkar"""
            return cls.URL_PATTERN.findall(text)
        
        @classmethod
        def extract_ips(cls, text):
            """IP adreslerini çıkar"""
            return cls.IPV4_PATTERN.findall(text)
        
        @classmethod
        def extract_dates(cls, text):
            """Tarihleri çıkar"""
            return cls.DATE_PATTERN.findall(text)
        
        @classmethod
        def clean_whitespace(cls, text):
            """Boşlukları temizle"""
            return re.sub(r'\s+', ' ', text.strip())
        
        @classmethod
        def remove_html_tags(cls, text):
            """HTML etiketlerini kaldır"""
            return re.sub(r'<[^>]+>', '', text)
        
        @classmethod
        def mask_sensitive(cls, text):
            """Hassas bilgileri maskele"""
            # Credit card masking
            text = re.sub(r'\b(\d{4})[\s-]?(\d{4})[\s-]?(\d{4})[\s-]?(\d{4})\b', 
                         r'\1 **** **** \4', text)
            
            # Phone masking
            text = re.sub(r'\b0(\d{3})(\d{3})(\d{4})\b', 
                         r'0\1***\3', text)
            
            # Email masking
            text = re.sub(r'\b(\w{1,3})\w*@(\w+\.\w+)', 
                         r'\1***@\2', text)
            
            return text
        
        @classmethod
        def validate_format(cls, text, format_type):
            """Format validasyonu"""
            patterns = {
                'email': cls.EMAIL_PATTERN,
                'phone': cls.PHONE_PATTERN,
                'url': cls.URL_PATTERN,
                'ipv4': cls.IPV4_PATTERN
            }
            
            pattern = patterns.get(format_type)
            if pattern:
                return bool(pattern.match(text))
            return False
    
    # Test RegexUtils
    sample_text = """
    İletişim Bilgileri:
    Email: john.doe@company.com
    Telefon: 0555 123 4567
    Website: https://www.company.com
    IP: 192.168.1.1
    Tarih: 15/03/2024
    
    Hassas bilgiler:
    Kart: 1234 5678 9012 3456
    """
    
    print("📧 Emails:", RegexUtils.extract_emails(sample_text))
    print("📞 Phones:", RegexUtils.extract_phones(sample_text))
    print("🌐 URLs:", RegexUtils.extract_urls(sample_text))
    print("🖥️ IPs:", RegexUtils.extract_ips(sample_text))
    print("📅 Dates:", RegexUtils.extract_dates(sample_text))
    
    print(f"\n🎭 Masked text:")
    print(RegexUtils.mask_sensitive(sample_text))
    
    print(f"\n✅ Validation tests:")
    test_cases = [
        ("email", "user@domain.com"),
        ("email", "invalid.email"),
        ("phone", "05551234567"),
        ("url", "https://example.com"),
        ("ipv4", "192.168.1.1")
    ]
    
    for format_type, test_value in test_cases:
        valid = RegexUtils.validate_format(test_value, format_type)
        status = "✅" if valid else "❌"
        print(f"{status} {format_type}: {test_value}")
    
    print(f"\n📊 Text Statistics:")
    
    def text_statistics(text):
        """Metin istatistikleri"""
        stats = {
            'total_chars': len(text),
            'words': len(re.findall(r'\b\w+\b', text)),
            'sentences': len(re.findall(r'[.!?]+', text)),
            'paragraphs': len(re.findall(r'\n\s*\n', text)) + 1,
            'emails': len(RegexUtils.extract_emails(text)),
            'urls': len(RegexUtils.extract_urls(text)),
            'phones': len(RegexUtils.extract_phones(text)),
            'numbers': len(re.findall(r'\b\d+\.?\d*\b', text))
        }
        return stats
    
    stats = text_statistics(sample_text)
    print("Metin istatistikleri:")
    for key, value in stats.items():
        print(f"  {key}: {value}")

regex_utilities()

print("\n🎉 Regular Expressions Tamamlandı!")
print("\n📚 Bu bölümde öğrenilenler:")
print("✅ Regex temel sözdizimi ve karakterler")
print("✅ Regex metodları (search, findall, sub, split)")
print("✅ Gelişmiş pattern'lar ve groups")
print("✅ Regex flags ve seçenekleri")
print("✅ Pratik kullanım örnekleri")
print("✅ Performance optimizasyonu")
print("✅ Utility fonksiyonları ve best practices")

print("\n💡 Regex İpuçları:")
print("• Raw strings (r'') kullanın")
print("• Tekrar kullanılan pattern'ları compile edin")
print("• Test ve debug araçları kullanın")
print("• Catastrophic backtracking'den kaçının")
print("• Specific pattern'ları tercih edin")
print("• Named groups kullanarak okunabilirliği artırın")

print("\n🔗 Sonraki adımlar:")
print("• Advanced text processing")
print("• Natural language processing")
print("• Web scraping ile regex kullanımı")
print("• Log analysis ve monitoring")
print("• Data validation ve cleaning")