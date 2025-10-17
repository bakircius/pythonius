# Python Nesne Yönelimli Programlama (OOP)

Bu bölümde Python'da Nesne Yönelimli Programlama (Object-Oriented Programming) konularını kapsamlı bir şekilde öğreniyoruz. Sınıflar, nesneler, kalıtım, polimorfizm ve encapsulation gibi temel OOP kavramları ele alınacak.

## 📚 İçerik

### 1. oop_temelleri.py
- **Class ve Object Kavramları**: Sınıf tanımlama ve nesne oluşturma
- **Constructor (__init__)**: Nesne başlatma metodları
- **Instance Variables**: Nesne değişkenleri
- **Instance Methods**: Nesne metodları
- **Class Variables**: Sınıf değişkenleri
- **Class Methods**: Sınıf metodları
- **Static Methods**: Statik metodlar

### 2. encapsulation_ve_property.py
- **Encapsulation**: Veri gizleme ve kapsülleme
- **Private Attributes**: Özel nitelikler (_ ve __)
- **Getter ve Setter**: Erişim metodları
- **Property Decorator**: @property kullanımı
- **Data Validation**: Veri doğrulama
- **Access Control**: Erişim kontrolü

### 3. inheritance_kalitim.py
- **Inheritance Temelleri**: Kalıtım kavramı
- **Parent ve Child Classes**: Ebeveyn ve çocuk sınıflar
- **super() Fonksiyonu**: Üst sınıf erişimi
- **Method Overriding**: Metod ezme
- **Multiple Inheritance**: Çoklu kalıtım
- **MRO (Method Resolution Order)**: Metod çözümleme sırası

### 4. polymorphism_ve_abstraction.py
- **Polymorphism**: Çok biçimlilik
- **Method Overloading**: Metod aşırı yükleme
- **Duck Typing**: Python'da dinamik tipleme
- **Abstract Classes**: Soyut sınıflar
- **ABC (Abstract Base Classes)**: Soyut temel sınıflar
- **Interface Pattern**: Arayüz deseni

### 5. special_methods_magic.py
- **Magic Methods**: Özel metodlar (__str__, __repr__, vb.)
- **Operator Overloading**: Operatör aşırı yükleme
- **Comparison Methods**: Karşılaştırma metodları
- **Arithmetic Methods**: Aritmetik metodlar
- **Container Methods**: Konteyner metodları
- **Context Managers**: Bağlam yöneticileri

### 6. advanced_oop_patterns.py
- **Design Patterns**: Tasarım desenleri
- **Singleton Pattern**: Tekil nesne deseni
- **Factory Pattern**: Fabrika deseni
- **Observer Pattern**: Gözlemci deseni
- **Decorator Pattern**: Dekoratör deseni
- **Strategy Pattern**: Strateji deseni

## 🎯 Öğrenme Hedefleri

### Temel Seviye
- [ ] Class ve object kavramlarını anlama
- [ ] Constructor kullanımı
- [ ] Instance ve class variables arasındaki fark
- [ ] Method türlerini bilme
- [ ] Encapsulation prensiplerini uygulama

### Orta Seviye
- [ ] Inheritance kullanarak kod tekrarını azaltma
- [ ] Polymorphism ile esnek kod yazma
- [ ] Property decorator ile data validation
- [ ] Abstract classes ile interface tanımlama
- [ ] Special methods ile operator overloading

### İleri Seviye
- [ ] Multiple inheritance ve MRO anlama
- [ ] Design patterns uygulama
- [ ] Advanced OOP concepts
- [ ] Performance considerations
- [ ] Best practices uygulama

## 📝 Örnek Dosyalar

1. **oop_temelleri.py** - Class, object, constructor, methods
2. **encapsulation_ve_property.py** - Data hiding, property decorators
3. **inheritance_kalitim.py** - Inheritance, super(), method overriding
4. **polymorphism_ve_abstraction.py** - Polymorphism, abstract classes
5. **special_methods_magic.py** - Magic methods, operator overloading
6. **advanced_oop_patterns.py** - Design patterns ve advanced concepts

## 💡 Temel Kavramlar

### Class ve Object
Sınıf (class) bir şablon, nesne (object) ise bu şablondan üretilen örnektir. Sınıflar nitelikleri (attributes) ve davranışları (methods) tanımlar.

### Encapsulation (Kapsülleme)
Veriyi ve bu veri üzerinde çalışan metodları bir arada tutma ve dış dünyadan gizleme prensibidir. Python'da _ ve __ ile private members oluşturulur.

### Inheritance (Kalıtım)
Bir sınıfın başka bir sınıftan özelliklerini miras alması durumudur. Code reusability sağlar ve "is-a" ilişkisini temsil eder.

### Polymorphism (Çok Biçimlilik)
Aynı interface'i farklı sınıfların farklı şekillerde implement etmesi durumudur. Duck typing Python'da polymorphism'in temel şeklidir.

### Abstraction (Soyutlama)
Karmaşık implementasyon detaylarını gizleyerek sadece gerekli interface'i gösterme prensibidir. Abstract classes ile sağlanır.

## 📊 Pratik Örnekler

### 1. E-ticaret Sistemi
Ürün, kategori, müşteri ve sipariş sınıfları ile complete e-commerce domain modeling.

### 2. Oyun Geliştirme
Karakter, düşman, silah sınıfları ile inheritance ve polymorphism kullanımı.

### 3. Bankacılık Sistemi
Hesap, müşteri, işlem sınıfları ile encapsulation ve data validation.

### 4. Grafik Editörü
Shape hierarchy ile abstract classes ve method overriding.

### 5. Media Player
Strategy pattern ile farklı media format desteği.

## 🛠️ Kullanılan Konzeptler

### Core OOP Principles
- **Encapsulation**: Data hiding ve access control
- **Inheritance**: Code reuse ve is-a relationships
- **Polymorphism**: Interface consistency
- **Abstraction**: Complexity hiding

### Python Specific Features
- **Property decorators**: Pythonic getters/setters
- **Multiple inheritance**: Diamond problem çözümü
- **Magic methods**: Operator overloading
- **Duck typing**: Dynamic polymorphism

### Design Patterns
- **Creational**: Singleton, Factory, Builder
- **Structural**: Decorator, Adapter, Facade
- **Behavioral**: Observer, Strategy, Command

## ⚡ Best Practices

### Class Design
- Single Responsibility Principle uygulayın
- Clear naming conventions kullanın
- Docstrings ile documentation sağlayın
- Type hints ekleyin

### Inheritance
- Composition over inheritance tercih edin
- Liskov Substitution Principle'a uyun
- Deep inheritance hierarchies'den kaçının
- super() kullanımını tercih edin

### Encapsulation
- Public interface minimal tutun
- Data validation ekleyin
- Immutable objects düşünün
- Property decorators kullanın

## 🚨 Dikkat Edilecek Noktalar

### Multiple Inheritance
- Diamond problem'e dikkat edin
- MRO (Method Resolution Order) anlayın
- Mixin pattern kullanın
- super() call chain'i koruyun

### Performance
- __slots__ ile memory optimization
- Lazy initialization düşünün
- Unnecessary inheritance'dan kaçının
- Profiling yapın

### Code Maintenance
- Clear interfaces tanımlayın
- Backward compatibility düşünün
- Testing strategy planlayın
- Documentation güncel tutun

## 📈 İleri Seviye Konular

### 1. Metaclasses
Class creation process kontrolü ve customization.

### 2. Descriptors
Attribute access kontrolü ve reusable property logic.

### 3. Context Managers
Resource management için __enter__ ve __exit__ implementation.

### 4. Iterators ve Generators
Custom iteration protocols ve memory-efficient data processing.

### 5. Decorators
Function ve class decoration için advanced patterns.

## 🎯 Gerçek Dünya Uygulamaları

### 1. Web Framework
Django/Flask gibi frameworks'te OOP usage patterns.

### 2. GUI Applications
Tkinter, PyQt ile widget hierarchies ve event handling.

### 3. Data Analysis
Pandas, NumPy'da OOP ile data structures.

### 4. Game Development
Pygame ile game object hierarchies.

### 5. API Development
REST API'lerde resource modeling ve serialization.

## 📚 Ek Kaynaklar

### Kitaplar
- "Effective Python" - Brett Slatkin
- "Python Tricks" - Dan Bader
- "Architecture Patterns with Python" - Harry Percival

### Design Patterns
- Gang of Four Design Patterns
- Python-specific pattern implementations
- Refactoring.guru design patterns

Bu bölüm Python'da professional-level OOP skills kazanmanızı sağlar ve modern software development practices'ini öğretir.