# Karşılaştırma Operatörleri
# İki değeri karşılaştırmak için kullanılan operatörler

print("=== KARŞILAŞTIRMA OPERATÖRLERİ ===\n")

# Test değerleri
a = 10
b = 5
c = 10
d = 15

print(f"Test değerleri: a = {a}, b = {b}, c = {c}, d = {d}\n")

print("1. TEMEL KARŞILAŞTIRMA OPERATÖRLERİ:")
print("-" * 40)

# Eşitlik (==)
print(f"a == b → {a} == {b} → {a == b}")
print(f"a == c → {a} == {c} → {a == c}")
print("  == operatörü: Eşit mi?")

# Eşitsizlik (!=)
print(f"\na != b → {a} != {b} → {a != b}")
print(f"a != c → {a} != {c} → {a != c}")
print("  != operatörü: Eşit değil mi?")

# Küçüktür (<)
print(f"\na < b → {a} < {b} → {a < b}")
print(f"b < a → {b} < {a} → {b < a}")
print("  < operatörü: Küçük mü?")

# Büyüktür (>)
print(f"\na > b → {a} > {b} → {a > b}")
print(f"b > a → {b} > {a} → {b > a}")
print("  > operatörü: Büyük mü?")

# Küçük eşit (<=)
print(f"\na <= c → {a} <= {c} → {a <= c}")
print(f"a <= b → {a} <= {b} → {a <= b}")
print("  <= operatörü: Küçük veya eşit mi?")

# Büyük eşit (>=)
print(f"\na >= c → {a} >= {c} → {a >= c}")
print(f"a >= d → {a} >= {d} → {a >= d}")
print("  >= operatörü: Büyük veya eşit mi?")

print("\n2. FARKLI VERİ TİPLERİYLE KARŞILAŞTIRMA:")
print("-" * 42)

# Sayılar arası
sayi_int = 5
sayi_float = 5.0
print(f"int vs float: {sayi_int} == {sayi_float} → {sayi_int == sayi_float}")

# String karşılaştırma
str1 = "python"
str2 = "Python"
str3 = "python"
print(f"\nString karşılaştırma:")
print(f"'{str1}' == '{str2}' → {str1 == str2}")
print(f"'{str1}' == '{str3}' → {str1 == str3}")
print("DİKKAT: Büyük/küçük harf önemli!")

# String alfabetik sıralama
print(f"\nAlfabetik sıralama:")
print(f"'a' < 'b' → {'a' < 'b'}")
print(f"'apple' < 'banana' → {'apple' < 'banana'}")
print(f"'Apple' < 'apple' → {'Apple' < 'apple'}")

print("\n3. BOOLEAN DEĞERLERLE KARŞILAŞTIRMA:")
print("-" * 36)

bool1 = True
bool2 = False
print(f"True == 1 → {bool1 == 1}")
print(f"False == 0 → {bool2 == 0}")
print(f"True > False → {bool1 > bool2}")
print("DİKKAT: True=1, False=0 değerinde")

print("\n4. NONE İLE KARŞILAŞTIRMA:")
print("-" * 27)

deger = None
print(f"None == None → {deger == None}")
print(f"None == 0 → {None == 0}")
print(f"None == '' → {None == ''}")
print(f"None == False → {None == False}")

print("\n5. LİSTE KARŞILAŞTIRMA:")
print("-" * 22)

liste1 = [1, 2, 3]
liste2 = [1, 2, 3]
liste3 = [1, 2, 4]
liste4 = [1, 2]

print(f"{liste1} == {liste2} → {liste1 == liste2}")
print(f"{liste1} == {liste3} → {liste1 == liste3}")
print(f"{liste1} > {liste4} → {liste1 > liste4}")
print("Liste karşılaştırma eleman eleman yapılır")

print("\n6. KARŞILAŞTIRMA ZİNCİRİ:")
print("-" * 26)

x = 5
print(f"x = {x}")
print(f"1 < x < 10 → {1 < x < 10}")
print(f"1 < x < 3 → {1 < x < 3}")
print(f"x == 5 == 5 → {x == 5 == 5}")

# Karmaşık zincir
print(f"0 < x <= 10 > 8 → {0 < x <= 10 > 8}")

print("\n7. KARŞILAŞTIRMA İLE KOŞUL YAPILARI:")
print("-" * 36)

yas = 18
print(f"Yaş: {yas}")

if yas >= 18:
    print("Reşit")
else:
    print("Reşit değil")

# Çoklu karşılaştırma
not_degeri = 85
print(f"\nNot: {not_degeri}")

if not_degeri >= 90:
    print("Harf notu: A")
elif not_degeri >= 80:
    print("Harf notu: B")
elif not_degeri >= 70:
    print("Harf notu: C")
elif not_degeri >= 60:
    print("Harf notu: D")
else:
    print("Harf notu: F")

print("\n8. KARŞILAŞTIRMA FONKSİYONLARI:")
print("-" * 31)

# min() ve max() fonksiyonları
sayilar = [3, 7, 1, 9, 4]
print(f"Sayılar: {sayilar}")
print(f"En küçük: {min(sayilar)}")
print(f"En büyük: {max(sayilar)}")

# sorted() fonksiyonu
print(f"Sıralı hali: {sorted(sayilar)}")

print("\n9. ÖZEL DURUMLAR:")
print("-" * 17)

# Float hassasiyet sorunu
print("Float hassasiyet problemi:")
print(f"0.1 + 0.2 == 0.3 → {0.1 + 0.2 == 0.3}")
print(f"0.1 + 0.2 = {0.1 + 0.2}")

# Çözüm: round() kullanmak
print(f"round(0.1 + 0.2, 1) == 0.3 → {round(0.1 + 0.2, 1) == 0.3}")

# Farklı tiplerle karşılaştırma hatası
print("\nFarklı tipler:")
# print("10" > 5)  # Bu TypeError verir!

print("\n=== KARŞILAŞTIRMA OPERATÖR ÖZETİ ===")
print("==  : Eşit mi?")
print("!=  : Eşit değil mi?")
print("<   : Küçük mü?")
print(">   : Büyük mü?")
print("<=  : Küçük veya eşit mi?")
print(">=  : Büyük veya eşit mi?")
print()
print("DİKKAT:")
print("- Karşılaştırma sonucu her zaman bool (True/False)")
print("- String karşılaştırma büyük/küçük harf duyarlı")
print("- Farklı tipler karşılaştırılırken dikkat!")