# Fonksiyon Kapsamları ve Global/Local Değişkenler
# Python'da fonksiyon scope'ları ve değişken yönetimi

print("=== FONKSİYON KAPAMLARI VE GLOBAL/LOCAL DEĞİŞKENLER ===\n")

print("1. SCOPE KAVRAMI:")
print("-" * 16)

# Global scope
global_variable = "Ben global bir değişkenim"

def scope_ornegi():
    # Local scope
    local_variable = "Ben local bir değişkenim"
    print(f"Fonksiyon içi - Local: {local_variable}")
    print(f"Fonksiyon içi - Global: {global_variable}")

print(f"Fonksiyon dışı - Global: {global_variable}")
scope_ornegi()

# Local değişkene dışarıdan erişim
try:
    print("Local değişkene erişim denemesi...")
    # print(local_variable)  # Bu satır NameError verir
    raise NameError("name 'local_variable' is not defined")
except NameError as e:
    print(f"Hata: {e}")

print(f"\nScope seviyeleri:")
print("1. Built-in scope - Python'un built-in fonksiyonları")
print("2. Global scope - Modül seviyesi")
print("3. Enclosing scope - İç içe fonksiyonlarda dış fonksiyon")
print("4. Local scope - Fonksiyon içi")

print("\n2. LEGB KURALI:")
print("-" * 14)

# Local, Enclosing, Global, Built-in
print("LEGB Kuralı: Local → Enclosing → Global → Built-in")

# Built-in scope
len_builtin = len  # Built-in len fonksiyonu

# Global scope
x = "global x"
len = "global len"  # Built-in len'i gölgeleme

def outer_function():
    # Enclosing scope
    x = "enclosing x"
    len = "enclosing len"
    
    def inner_function():
        # Local scope
        x = "local x"
        print(f"Inner function x: {x}")  # local x
        print(f"Inner function len: {len}")  # enclosing len
        print(f"Built-in len via len_builtin: {len_builtin([1,2,3])}")
    
    inner_function()
    print(f"Outer function x: {x}")  # enclosing x

outer_function()
print(f"Global x: {x}")  # global x

# Name resolution örneği
def name_resolution_test():
    # Burada x tanımlı değil, global x'e bakacak
    print(f"Name resolution: {x}")

name_resolution_test()

print("\n3. GLOBAL KEYWORD:")
print("-" * 18)

# Global değişken
counter = 0

def increment_wrong():
    """Yanlış yöntem - local counter oluşturur"""
    counter = counter + 1  # UnboundLocalError!
    return counter

def increment_correct():
    """Doğru yöntem - global keyword"""
    global counter
    counter = counter + 1
    return counter

print(f"Başlangıç counter: {counter}")

# Yanlış yöntem
try:
    increment_wrong()
except UnboundLocalError as e:
    print(f"Hata: {e}")

# Doğru yöntem
print(f"increment_correct(): {increment_correct()}")
print(f"Global counter: {counter}")

# Global değişken oluşturma
def create_global():
    """Fonksiyon içinde global değişken oluştur"""
    global new_global_var
    new_global_var = "Fonksiyon içinde oluşturuldu"

create_global()
print(f"Yeni global değişken: {new_global_var}")

# Çoklu global değişken
def manage_globals():
    """Çoklu global değişken yönetimi"""
    global var1, var2, var3
    var1 = "birinci"
    var2 = "ikinci" 
    var3 = "üçüncü"

manage_globals()
print(f"Global değişkenler: {var1}, {var2}, {var3}")

print("\n4. NONLOCAL KEYWORD:")
print("-" * 20)

def outer_function():
    """Enclosing scope örneği"""
    outer_var = "enclosing değişken"
    
    def inner_without_nonlocal():
        """nonlocal kullanmayan iç fonksiyon"""
        outer_var = "local değişken"  # Yeni local değişken
        print(f"Inner without nonlocal: {outer_var}")
    
    def inner_with_nonlocal():
        """nonlocal kullanan iç fonksiyon"""
        nonlocal outer_var
        outer_var = "değiştirilmiş enclosing"  # Enclosing değişkeni değiştir
        print(f"Inner with nonlocal: {outer_var}")
    
    print(f"Önce outer_var: {outer_var}")
    
    inner_without_nonlocal()
    print(f"After without nonlocal: {outer_var}")  # Değişmedi
    
    inner_with_nonlocal()
    print(f"After with nonlocal: {outer_var}")  # Değişti

outer_function()

# Nested nonlocal
def level1():
    var = "level1"
    
    def level2():
        nonlocal var
        var = "level2"
        
        def level3():
            nonlocal var
            var = "level3"
            print(f"Level3: {var}")
        
        level3()
        print(f"Level2: {var}")
    
    level2()
    print(f"Level1: {var}")

print(f"\nNested nonlocal örneği:")
level1()

print("\n5. DEĞİŞKEN SHADOWING (GÖLGELEMESİ):")
print("-" * 36)

# Global değişken
name = "Global Ali"

def shadowing_example():
    """Değişken gölgeleme örneği"""
    name = "Local Veli"  # Global name'i gölgeler
    print(f"Fonksiyon içi name: {name}")
    
    def inner_function():
        name = "Inner Ayşe"  # Outer name'i gölgeler
        print(f"İç fonksiyon name: {name}")
    
    inner_function()
    print(f"Fonksiyon içi name (inner'dan sonra): {name}")

print(f"Global name: {name}")
shadowing_example()
print(f"Global name (değişmedi): {name}")

# Built-in gölgeleme
print(f"\nBuilt-in gölgeleme:")
print(f"Built-in len: {len([1, 2, 3])}")

def shadow_builtin():
    len = "Gölgelenmiş len"
    print(f"Local len: {len}")
    # print(len([1, 2, 3]))  # TypeError! String çağrılamaz

shadow_builtin()
print(f"Built-in len (geri döndü): {len([1, 2, 3])}")

# Tehlikeli gölgeleme
list = "Bu list'i gölgeler!"  # YAPMAYIN!

def use_list():
    # list() kullanamayız artık bu scope'ta
    try:
        new_list = list([1, 2, 3])  # TypeError!
    except TypeError as e:
        print(f"Gölgeleme hatası: {e}")

use_list()

# Gölgelemeyi kaldır
del list

print("\n6. CLOSURE (KAPANMA) KAVRAMI:")
print("-" * 28)

def outer_closure(x):
    """Closure oluşturan fonksiyon"""
    def inner_closure(y):
        # x'i closure ile yakalar
        return x + y
    return inner_closure

# Closure fonksiyonları oluştur
add_10 = outer_closure(10)
add_5 = outer_closure(5)

print(f"add_10(3): {add_10(3)}")  # 10 + 3 = 13
print(f"add_5(7): {add_5(7)}")    # 5 + 7 = 12

# Closure'ın yakaladığı değişkenler
print(f"add_10 closure: {add_10.__closure__}")
print(f"add_10 yakalanan değer: {add_10.__closure__[0].cell_contents}")

# Değişken closure
def make_counter():
    """Counter oluşturan closure"""
    count = 0
    
    def counter():
        nonlocal count
        count += 1
        return count
    
    return counter

counter1 = make_counter()
counter2 = make_counter()

print(f"\nClosure counter örneği:")
print(f"Counter1: {counter1()}, {counter1()}, {counter1()}")
print(f"Counter2: {counter2()}, {counter2()}")

# Çoklu closure
def make_multiplier(n):
    """Çarpan fonksiyonları oluşturan closure"""
    def multiply(x):
        return x * n
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(f"double(4): {double(4)}")
print(f"triple(4): {triple(4)}")

print("\n7. DEFAULT PARAMETER PITFALLS:")
print("-" * 30)

# Mutable default parameter problemi
def problem_function(item, lst=[]):
    """PROBLEMLİ - mutable default parameter"""
    lst.append(item)
    return lst

print("Mutable default parameter problemi:")
print(f"İlk çağrı: {problem_function('a')}")
print(f"İkinci çağrı: {problem_function('b')}")  # Sürpriz!
print(f"Üçüncü çağrı: {problem_function('c')}")  # Daha da sürpriz!

# Doğru yöntem
def correct_function(item, lst=None):
    """DOĞRU - None default, içerde oluştur"""
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(f"\nDoğru yöntem:")
print(f"İlk çağrı: {correct_function('a')}")
print(f"İkinci çağrı: {correct_function('b')}")
print(f"Üçüncü çağrı: {correct_function('c')}")

# Default parameter evaluation time
import time

def time_default(t=time.time()):
    """Zamanı default parameter olarak yakalar"""
    return t

print(f"\nDefault parameter evaluation:")
print(f"İlk çağrı: {time_default()}")
time.sleep(1)
print(f"1 saniye sonra: {time_default()}")  # Aynı zaman!

# Doğru yöntem
def time_correct(t=None):
    if t is None:
        t = time.time()
    return t

print(f"\nDoğru yöntem:")
print(f"İlk çağrı: {time_correct()}")
time.sleep(1)
print(f"1 saniye sonra: {time_correct()}")  # Farklı zaman

print("\n8. FUNCTION ATTRIBUTES VE NAMESPACE:")
print("-" * 35)

def function_with_attributes():
    """Öznitelikleri olan fonksiyon"""
    return "Hello World"

# Fonksiyona öznitelik ekleme
function_with_attributes.version = "1.0"
function_with_attributes.author = "Python Developer"
function_with_attributes.call_count = 0

def counting_function():
    """Çağrı sayısını tutan fonksiyon"""
    counting_function.call_count += 1
    return f"Bu fonksiyon {counting_function.call_count} kez çağrıldı"

counting_function.call_count = 0

print(f"Fonksiyon öznitelikleri:")
print(f"Version: {function_with_attributes.version}")
print(f"Author: {function_with_attributes.author}")

print(f"\nÇağrı sayacı:")
print(counting_function())
print(counting_function())
print(counting_function())

# Fonksiyon namespace'i
print(f"\nFonksiyon namespace:")
print(f"Function name: {function_with_attributes.__name__}")
print(f"Function doc: {function_with_attributes.__doc__}")
print(f"Function dict: {function_with_attributes.__dict__}")

print("\n9. GLOBAL VE LOCAL BUILTİNS:")
print("-" * 27)

def inspect_namespaces():
    """Namespace'leri incele"""
    local_var = "local"
    
    print(f"Locals: {locals()}")
    print(f"Globals keys: {list(globals().keys())[:10]}...")  # İlk 10
    
    # Built-ins
    import builtins
    print(f"Builtins: {dir(builtins)[:10]}...")  # İlk 10

inspect_namespaces()

# Global namespace manipulation
def modify_global_namespace():
    """Global namespace'i değiştir"""
    globals()['dynamic_var'] = "Dinamik olarak oluşturuldu"

modify_global_namespace()
print(f"Dinamik değişken: {globals().get('dynamic_var', 'Bulunamadı')}")

# Local namespace manipulation
def modify_local_namespace():
    """Local namespace'i değiştir"""
    locals()['local_dynamic'] = "Bu çalışmayabilir"
    # locals() read-only kabul edilir!
    print(f"Locals: {locals()}")

modify_local_namespace()

print("\n10. SCOPE DEBUGGING VE İNCELEME:")
print("-" * 30)

def debug_scope():
    """Scope debugging araçları"""
    local_var = "debug local"
    
    # Değişken varlığını kontrol etme
    print(f"'local_var' locals'da: {'local_var' in locals()}")
    print(f"'global_variable' globals'da: {'global_variable' in globals()}")
    
    # vars() kullanımı
    print(f"vars() (locals ile aynı): {vars()}")
    
    # dir() ile isim listesi
    print(f"dir() sonucu: {dir()}")

debug_scope()

# Scope inspector fonksiyonu
def scope_inspector():
    """Kapsamlı scope analizi"""
    local_var = "inspector local"
    
    def inner():
        inner_var = "inner local"
        
        print("=== SCOPE ANALYSIS ===")
        print(f"Local scope: {list(locals().keys())}")
        
        # Enclosing scope (outer function'dan)
        print(f"'local_var' erişilebilir: {'local_var' in dir()}")
        
        # Global scope
        print(f"Global 'global_variable': {'global_variable' in globals()}")
        
        # Built-in scope
        import builtins
        print(f"Built-in 'len': {'len' in dir(builtins)}")
    
    inner()

scope_inspector()

print("\n11. BEST PRACTİCES VE COMMON MİSTAKES:")
print("-" * 37)

print("✓ İYİ PRATİKLER:")
print("1. Global değişkenleri minimal kullanın")
print("2. Açık scope tanımlamaları (global/nonlocal)")
print("3. Mutable default parameters kullanmayın")
print("4. Built-in'leri gölgelemeyin")
print("5. Closure'ları akıllıca kullanın")

print("\n✗ YAYGN HATALAR:")
print("1. Mutable default parameters")
print("2. Late binding closures")
print("3. Global state bağımlılığı")
print("4. Built-in shadowing")
print("5. UnboundLocalError")

# Late binding closure problemi
functions = []
for i in range(5):
    functions.append(lambda x: x + i)  # i hep 4 olacak!

print(f"\nLate binding problemi:")
for j, func in enumerate(functions):
    print(f"Function {j}: {func(1)}")  # Hepsi 5 (1+4)

# Çözüm: Default parameter
functions_fixed = []
for i in range(5):
    functions_fixed.append(lambda x, i=i: x + i)  # i'yi yakala

print(f"Düzeltilmiş version:")
for j, func in enumerate(functions_fixed):
    print(f"Function {j}: {func(1)}")

# Performance considerations
def performance_test():
    """Global vs local erişim performansı"""
    global_var = "global"
    
    import time
    
    # Local access
    local_var = "local"
    start = time.time()
    for _ in range(100000):
        _ = local_var
    local_time = time.time() - start
    
    # Global access
    start = time.time()
    for _ in range(100000):
        _ = global_variable
    global_time = time.time() - start
    
    print(f"\n100.000 erişim performansı:")
    print(f"Local: {local_time*1000:.2f} ms")
    print(f"Global: {global_time*1000:.2f} ms")
    print(f"Global {global_time/local_time:.1f}x daha yavaş")

performance_test()

print("\n=== SCOPE VE DEĞİŞKEN YÖNETİMİ ÖZETİ ===")
print("LEGB Kuralı:")
print("  1. Local - Fonksiyon içi")
print("  2. Enclosing - İç içe fonksiyonlarda dış")
print("  3. Global - Modül seviyesi")
print("  4. Built-in - Python built-ins")
print()
print("Keyword'ler:")
print("  • global - global değişken değiştirme")
print("  • nonlocal - enclosing değişken değiştirme")
print()
print("Closure:")
print("  • İç fonksiyon dış fonksiyon değişkenlerini yakalar")
print("  • Değişken yaşam süresini uzatır")
print("  • Factory pattern'lerde kullanılır")
print()
print("Dikkat edilmesi gerekenler:")
print("  • Mutable default parameters")
print("  • Late binding closures")
print("  • Built-in shadowing")
print("  • Global state dependency")
print()
print("Performance:")
print("  • Local > Enclosing > Global > Built-in")
print("  • Global değişkenleri minimal kullanın")
print("  • Closure overhead'ını göz önünde bulundurun")