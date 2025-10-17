# Python String İşlemleri (Strings) - Kapsamlı Rehber

Bu bölüm Python'da string (metin) işlemlerini kapsamlı olarak ele alır. String oluşturma, formatlandırma, manipülasyon ve regex kullanımını öğreneceksiniz.

## 📚 Bölüm İçeriği

### 🎯 Öğrenme Hedefleri
- String oluşturma ve temel işlemler
- String metodlarını etkin kullanma
- Formatlandırma yöntemlerini öğrenme
- Regular expressions ile pattern matching
- Performance optimizasyonu
- Best practices ve yaygın hatalar

### 📂 Dosya Yapısı

#### 1. `temel_string_islemleri.py`
**Kapsam:** String temelleri ve temel işlemler
- String oluşturma yöntemleri
- İndeksleme ve slicing
- Temel string metodları
- String birleştirme ve bölme
- Temel formatlandırma
- Encoding ve Unicode
- String karşılaştırma
- Validasyon ve temizleme
- Performance ipuçları

**Örnek Kullanımlar:**
```python
# String oluşturma
ad = "Python"
mesaj = f"Merhaba {ad}!"

# Slicing
print(ad[0:3])  # "Pyt"

# Metodlar
print(ad.upper())  # "PYTHON"
print(ad.find('th'))  # 2
```

#### 2. `string_metodlari.py`
**Kapsam:** Tüm string metodlarının detaylı kullanımı
- Arama ve konum bulma metodları
- Kontrol metodları (boolean dönen)
- Dönüştürme metodları
- Değiştirme metodları
- Bölme ve birleştirme metodları
- Hizalama ve doldurma metodları
- Encoding/decoding metodları
- Özelleştirilmiş string sınıfları
- Metod zincirleme
- Performance karşılaştırması

**Örnek Kullanımlar:**
```python
# Gelişmiş metodlar
metin = "  Python Programming  "
print(metin.strip().title())  # "Python Programming"

# Özel string sınıfı
class GelismisString(str):
    def tersle(self):
        return self[::-1]
```

#### 3. `string_formatlama.py`
**Kapsam:** String formatlandırma yöntemleri ve manipülasyon
- % (printf-style) formatlandırma
- .format() metodu
- f-string (formatted string literals)
- Template strings
- Gelişmiş format teknikleri
- String manipülasyon teknikleri
- Validation ve parsing
- Performance ve best practices

**Örnek Kullanımlar:**
```python
# Farklı formatlandırma yöntemleri
ad, yas = "Ali", 25

# % formatting
mesaj1 = "Adım %s, yaşım %d" % (ad, yas)

# .format()
mesaj2 = "Adım {}, yaşım {}".format(ad, yas)

# f-string (önerilen)
mesaj3 = f"Adım {ad}, yaşım {yas}"
```

#### 4. `regex_patterns.py`
**Kapsam:** Regular expressions ile gelişmiş string işlemleri
- Regex temelleri ve sözdizimi
- Regex metodları (search, findall, sub, split)
- Gelişmiş pattern'lar ve groups
- Regex flags ve seçenekleri
- Pratik kullanım örnekleri
- Performance optimizasyonu
- Utility fonksiyonları

**Örnek Kullanımlar:**
```python
import re

# Email validasyonu
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
is_valid = bool(re.match(email_pattern, "user@domain.com"))

# Telefon numarası formatlandırma
phone = re.sub(r'(\d{4})(\d{3})(\d{4})', r'\1 \2 \3', "05551234567")
```

## 🛠️ Kurulum ve Çalıştırma

### Gereksinimler
- Python 3.6+ (f-string için)
- Standart kütüphane (re, string, datetime)

### Çalıştırma
```bash
# Temel string işlemleri
python temel_string_islemleri.py

# String metodları
python string_metodlari.py

# Formatlandırma
python string_formatlama.py

# Regex patterns
python regex_patterns.py
```

## 💡 Önemli Konular

### String Formatlandırma Yöntemleri
1. **% Formatting** (eski yöntem)
2. **.format()** (Python 2.7+)
3. **f-string** (Python 3.6+, önerilen)
4. **Template strings** (güvenli formatlandırma)

### Performance İpuçları
- f-string en hızlı formatlandırma yöntemi
- join() ile string birleştirme
- Compiled regex pattern'ları kullanma
- String immutability'yi göz önünde bulundurma

### Best Practices
- f-string kullanın (Python 3.6+)
- Regex yerine string metodlarını tercih edin
- Unicode ve encoding'e dikkat edin
- User input validasyonu yapın
- Raw strings kullanın (regex için)

## 🔧 Pratik Örnekler

### 1. Email Validasyonu
```python
import re

def email_gecerli_mi(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
```

### 2. Telefon Formatlandırma
```python
def telefon_formatla(telefon):
    rakamlar = re.sub(r'\D', '', telefon)
    if len(rakamlar) == 11:
        return f"{rakamlar[:4]} {rakamlar[4:7]} {rakamlar[7:]}"
    return telefon
```

### 3. Metin Temizleme
```python
def metin_temizle(metin):
    # HTML etiketlerini kaldır
    temiz = re.sub(r'<[^>]+>', '', metin)
    # Çoklu boşlukları tek boşluğa çevir
    temiz = re.sub(r'\s+', ' ', temiz)
    return temiz.strip()
```

### 4. Hassas Bilgi Maskeleme
```python
def kredi_karti_maskele(kart_no):
    rakamlar = re.sub(r'\D', '', kart_no)
    if len(rakamlar) == 16:
        return f"{rakamlar[:4]} **** **** {rakamlar[-4:]}"
    return kart_no
```

## 📊 Performance Karşılaştırması

| Yöntem | Hız | Kullanım |
|--------|-----|----------|
| f-string | En hızlı | Python 3.6+ |
| .format() | Orta | Genel amaçlı |
| % formatting | Yavaş | Eski kod |
| Template | En yavaş | Güvenlik |

## ⚠️ Yaygın Hatalar

1. **+ operatörü ile çok string birleştirme**
   ```python
   # Yanlış
   result = ""
   for item in items:
       result += str(item)
   
   # Doğru
   result = "".join(str(item) for item in items)
   ```

2. **Encoding belirtmeden dosya okuma**
   ```python
   # Yanlış
   with open('file.txt') as f:
       content = f.read()
   
   # Doğru
   with open('file.txt', encoding='utf-8') as f:
       content = f.read()
   ```

3. **User input'u doğrudan format string'e koyma**
   ```python
   # Güvenlik riski
   user_input = "user input"
   formatted = f"Hello {user_input}"
   
   # Güvenli
   template = string.Template("Hello $name")
   formatted = template.safe_substitute(name=user_input)
   ```

## 🎯 İleri Seviye Konular

1. **Unicode Normalization**
2. **Locale-specific String Operations**
3. **Memory-efficient String Processing**
4. **Custom String Classes**
5. **Text Mining ve NLP**

## 🔗 İlgili Konular

- **Dosya İşlemleri:** Text dosyalarını okuma/yazma
- **Web Scraping:** HTML/XML parsing
- **Data Validation:** Form validation
- **Logging:** Log formatlandırma
- **I18n/L10n:** Uluslararasılaştırma

## 📝 Alıştırmalar

### Başlangıç Seviyesi
1. Kullanıcıdan alınan metni temizleyen fonksiyon yazın
2. Email ve telefon validasyonu yapan program geliştirin
3. String formatlandırma yöntemlerini karşılaştırın

### Orta Seviye
1. Log dosyası parser'ı yazın
2. HTML etiketlerini kaldıran temizleyici geliştirin
3. Çoklu dil desteği olan formatter oluşturun

### İleri Seviye
1. Performance-optimized string processor yazın
2. Custom regex-based text analyzer geliştirin
3. Memory-efficient büyük dosya işleyici oluşturun

## 📚 Ek Kaynaklar

- [Python String Documentation](https://docs.python.org/3/library/string.html)
- [Regular Expressions HOWTO](https://docs.python.org/3/howto/regex.html)
- [Unicode HOWTO](https://docs.python.org/3/howto/unicode.html)
- [String Formatting Guide](https://docs.python.org/3/library/string.html#format-specification-mini-language)

---

**Not:** Bu bölüm Python string işlemlerinin kapsamlı bir rehberidir. Her dosyayı sırayla çalıştırarak konuları pekiştirin ve örnekleri kendi projelerinizde kullanın.