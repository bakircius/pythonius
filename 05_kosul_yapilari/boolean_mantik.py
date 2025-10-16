# Boolean Mantık ve Truth Değerleri
# Python'da mantıksal değerlerin nasıl çalıştığı

print("=== BOOLEAN MANTIK VE TRUTH DEĞERLERİ ===\n")

print("1. TEMEL BOOLEAN DEĞERLERİ:")
print("-" * 28)

# Temel boolean değerler
dogru = True
yanlis = False

print(f"dogru = {dogru} (tip: {type(dogru)})")
print(f"yanlis = {yanlis} (tip: {type(yanlis)})")

# Boolean'ların sayısal karşılıkları
print(f"\nSayısal karşılıklar:")
print(f"int(True) = {int(True)}")
print(f"int(False) = {int(False)}")
print(f"True + True = {True + True}")
print(f"True * 5 = {True * 5}")

print("\n2. TRUTH DEĞERLERİ (TRUTHY/FALSY):")
print("-" * 36)

print("Falsy değerler (False gibi davranır):")
falsy_degerler = [
    False, 0, 0.0, 0j,  # Boolean ve sayısal
    "", '', """""",     # Boş stringler
    [], {}, set(),      # Boş koleksiyonlar
    None               # None değeri
]

for deger in falsy_degerler:
    print(f"bool({deger!r:>10}) = {bool(deger)}")

print("\nTruthy değerler (True gibi davranır):")
truthy_degerler = [
    True, 1, -1, 3.14,          # Boolean ve sıfır olmayan sayılar
    "merhaba", "0", " ",        # Boş olmayan stringler
    [1], {"a": 1}, {1},         # Dolu koleksiyonlar
    [0], {"": ""}, {0}          # İçi boş bile olsa var olan yapılar
]

for deger in truthy_degerler:
    print(f"bool({deger!r:>15}) = {bool(deger)}")

print("\n3. KOŞULLARDA TRUTH DEĞERİ KULLANIMI:")
print("-" * 37)

# Değişkenlerin truth değerlerini kontrol etme
def kontrol_et(deger):
    if deger:
        print(f"{deger!r} → Truthy")
    else:
        print(f"{deger!r} → Falsy")

test_degerleri = [
    42, 0, "Python", "", [1, 2], [], 
    {"key": "value"}, {}, None, True, False
]

print("Koşullarda truth değeri kontrolü:")
for deger in test_degerleri:
    kontrol_et(deger)

print("\n4. PRATİK KULLANIM ÖRNEKLERİ:")
print("-" * 28)

# Liste boş kontrolü
def liste_islemleri():
    liste = [1, 2, 3]
    
    # Pythonic yol
    if liste:
        print(f"Liste dolu: {liste}")
    else:
        print("Liste boş")
    
    # Uzun yol (önerilmez)
    if len(liste) > 0:
        print("Liste dolu (uzun yöntem)")

liste_islemleri()

# String boş kontrolü
def string_kontrol():
    kullanici_adi = ""
    
    # Pythonic yol
    if kullanici_adi:
        print(f"Hoşgeldin {kullanici_adi}")
    else:
        print("Lütfen kullanıcı adı girin")
    
    # Uzun yol (önerilmez)
    if len(kullanici_adi) > 0:
        print("Kullanıcı adı var (uzun yöntem)")

string_kontrol()

# None kontrolü
def none_kontrol():
    deger = None
    
    # Pythonic yol
    if deger:
        print(f"Değer: {deger}")
    else:
        print("Değer tanımlanmamış")
    
    # Özel None kontrolü
    if deger is None:
        print("Değer kesinlikle None")
    elif deger is not None:
        print("Değer None değil")

none_kontrol()

print("\n5. MANTIKSAL OPERATÖRLER VE TRUTH:")
print("-" * 34)

# and operatörü ile truth değerleri
print("AND operatörü örnekleri:")
print(f"True and 'merhaba' = {True and 'merhaba'}")
print(f"False and 'merhaba' = {False and 'merhaba'}")
print(f"[] and 'merhaba' = {[] and 'merhaba'}")
print(f"[1,2] and 'merhaba' = {[1,2] and 'merhaba'}")

# or operatörü ile truth değerleri
print("\nOR operatörü örnekleri:")
print(f"False or 'varsayılan' = {False or 'varsayılan'}")
print(f"'' or 'varsayılan' = {'' or 'varsayılan'}")
print(f"0 or 'varsayılan' = {0 or 'varsayılan'}")
print(f"'değer' or 'varsayılan' = {'değer' or 'varsayılan'}")

# not operatörü
print("\nNOT operatörü örnekleri:")
print(f"not True = {not True}")
print(f"not False = {not False}")
print(f"not [] = {not []}")
print(f"not [1,2] = {not [1,2]}")
print(f"not '' = {not ''}")
print(f"not 'merhaba' = {not 'merhaba'}")

print("\n6. KISA DEVRE DEĞERLENDİRME:")
print("-" * 30)

# and için kısa devre
print("AND kısa devre örnekleri:")

def test_fonksiyon():
    print("Fonksiyon çağrıldı!")
    return True

# İlk koşul False olduğu için fonksiyon çağrılmaz
sonuc1 = False and test_fonksiyon()
print(f"False and test_fonksiyon() = {sonuc1}")

# İlk koşul True olduğu için fonksiyon çağrılır
print("\nİkinci test:")
sonuc2 = True and test_fonksiyon()
print(f"True and test_fonksiyon() = {sonuc2}")

# or için kısa devre
print("\nOR kısa devre örnekleri:")

# İlk koşul True olduğu için fonksiyon çağrılmaz
sonuc3 = True or test_fonksiyon()
print(f"True or test_fonksiyon() = {sonuc3}")

print("\nİkinci test:")
# İlk koşul False olduğu için fonksiyon çağrılır
sonuc4 = False or test_fonksiyon()
print(f"False or test_fonksiyon() = {sonuc4}")

print("\n7. VARSAYILAN DEĞER ATAMA:")
print("-" * 27)

# or operatörü ile varsayılan değer
kullanici_adi = ""
isim = kullanici_adi or "Misafir"
print(f"İsim: '{isim}'")

# Çoklu varsayılan değer
ad = ""
soyad = None
takma_ad = "CoolUser"
gosterilen_isim = ad or soyad or takma_ad or "Anonim"
print(f"Gösterilen isim: '{gosterilen_isim}'")

# and operatörü ile güvenli erişim
liste = [1, 2, 3, 4, 5]
ilk_eleman = liste and liste[0]
print(f"İlk eleman: {ilk_eleman}")

boş_liste = []
ilk_eleman_bos = boş_liste and boş_liste[0]  # IndexError oluşmaz
print(f"Boş liste ilk eleman: {ilk_eleman_bos}")

print("\n8. TİP DÖNÜŞÜMÜ VE BOOLEAN:")
print("-" * 27)

# Explicit boolean dönüşümü
print("Açık boolean dönüşümü:")
degerler = [1, 0, "text", "", [1], [], None]
for deger in degerler:
    print(f"bool({deger!r}) = {bool(deger)}")

# Implicit boolean dönüşümü (koşullarda)
print("\nÖrtük boolean dönüşümü:")
for deger in degerler:
    durum = "Truthy" if deger else "Falsy"
    print(f"{deger!r} → {durum}")

print("\n9. KARMAŞIK BOOLEAN İFADELER:")
print("-" * 30)

# Çoklu koşul örneği
yas = 25
gelir = 5000
kredi_notu = 750
is_deneyimi = True

# Karmaşık koşul
kredi_uygun = (
    yas >= 18 and 
    gelir >= 3000 and 
    kredi_notu >= 700 and 
    is_deneyimi
)

print(f"Kredi uygunluğu: {kredi_uygun}")

# Koşul parçalama
yas_uygun = yas >= 18
gelir_uygun = gelir >= 3000
kredi_uygun_2 = kredi_notu >= 700

print(f"Yaş uygun: {yas_uygun}")
print(f"Gelir uygun: {gelir_uygun}")
print(f"Kredi notu uygun: {kredi_uygun_2}")
print(f"İş deneyimi: {is_deneyimi}")

final_karar = yas_uygun and gelir_uygun and kredi_uygun_2 and is_deneyimi
print(f"Final karar: {final_karar}")

print("\n10. DEBUGGING VE TEST:")
print("-" * 20)

# Boolean ifadeleri test etme
def test_boolean_ifade(ifade, beklenen):
    sonuc = bool(ifade)
    durum = "✓" if sonuc == beklenen else "✗"
    print(f"{durum} bool({ifade!r}) = {sonuc} (beklenen: {beklenen})")

print("Boolean test örnekleri:")
test_boolean_ifade(1, True)
test_boolean_ifade(0, False)
test_boolean_ifade("", False)
test_boolean_ifade("0", True)  # Dikkat: string "0" truthy!
test_boolean_ifade([], False)
test_boolean_ifade([0], True)  # Dikkat: [0] truthy!

print("\n11. COMMON PATTERNS:")
print("-" * 18)

# Guard clause pattern
def process_data(data):
    if not data:
        print("Veri yok, işlem iptal")
        return
    
    if not isinstance(data, list):
        print("Veri liste değil")
        return
    
    print(f"Veri işleniyor: {data}")

process_data([])
process_data("string")
process_data([1, 2, 3])

# Default value pattern
def get_user_name(user_data):
    return user_data.get("name") or "Anonim Kullanıcı"

user1 = {"name": "Ahmet"}
user2 = {"name": ""}
user3 = {}

print(f"\nKullanıcı 1: {get_user_name(user1)}")
print(f"Kullanıcı 2: {get_user_name(user2)}")
print(f"Kullanıcı 3: {get_user_name(user3)}")

print("\n=== BOOLEAN MANTIK ÖZETİ ===")
print("Falsy değerler:")
print("  False, 0, 0.0, '', [], {}, set(), None")
print()
print("Truthy değerler:")
print("  Falsy olmayan her şey (True, 1, 'text', [1], vb.)")
print()
print("Kısa devre değerlendirme:")
print("  and: İlk falsy değeri döner")
print("  or:  İlk truthy değeri döner")
print()
print("Pratik kullanım:")
print("  if liste:          # Liste boş mu?")
print("  name = name or 'default'  # Varsayılan değer")
print("  if not data:       # Veri yok mu?")
print()
print("DİKKAT:")
print("  • '0', [0], {0} truthy'dir!")
print("  • bool() vs koşul aynı sonucu verir")
print("  • is None vs == None farkı önemli")