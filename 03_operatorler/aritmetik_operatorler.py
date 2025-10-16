# Aritmetik Operatörler
# Python'daki matematiksel işlem operatörleri

print("=== ARİTMETİK OPERATÖRLER ===\n")

# Test değerleri
a = 10
b = 3
print(f"a = {a}, b = {b}\n")

print("1. TEMEL ARİTMETİK OPERATÖRLER:")
print("-" * 35)

# Toplama (+)
toplam = a + b
print(f"a + b = {a} + {b} = {toplam}")

# Çıkarma (-)
fark = a - b
print(f"a - b = {a} - {b} = {fark}")

# Çarpma (*)
carpim = a * b
print(f"a * b = {a} * {b} = {carpim}")

# Bölme (/) - Her zaman float döner
bolum = a / b
print(f"a / b = {a} / {b} = {bolum}")

print("\n2. ÖZEL ARİTMETİK OPERATÖRLER:")
print("-" * 35)

# Taban bölme (//) - Sonucun tam sayı kısmı
taban_bolme = a // b
print(f"a // b = {a} // {b} = {taban_bolme}")
print("  // operatörü: Bölümün tam sayı kısmını verir")

# Mod (%) - Bölümden kalan
kalan = a % b
print(f"a % b = {a} % {b} = {kalan}")
print("  % operatörü: Bölümden kalanı verir")

# Üs alma (**)
us = a ** b
print(f"a ** b = {a} ** {b} = {us}")
print("  ** operatörü: Üs alma işlemi")

print("\n3. NEGATİF SAYILARLA ÖRNEKLER:")
print("-" * 32)

x = -7
y = 3
print(f"x = {x}, y = {y}")

print(f"x + y = {x} + {y} = {x + y}")
print(f"x - y = {x} - {y} = {x - y}")
print(f"x * y = {x} * {y} = {x * y}")
print(f"x / y = {x} / {y} = {x / y}")
print(f"x // y = {x} // {y} = {x // y}")
print(f"x % y = {x} % {y} = {x % y}")

print("\n4. ONDALIKLI SAYILARLA ÖRNEKLER:")
print("-" * 34)

m = 15.5
n = 4.2
print(f"m = {m}, n = {n}")

print(f"m + n = {m} + {n} = {m + n}")
print(f"m - n = {m} - {n} = {m - n}")
print(f"m * n = {m} * {n} = {m * n}")
print(f"m / n = {m} / {n} = {m / n:.2f}")
print(f"m // n = {m} // {n} = {m // n}")
print(f"m % n = {m} % {n} = {m % n:.2f}")

print("\n5. OPERATÖR ÖNCELİĞİ:")
print("-" * 22)

# Matematiksel öncelik kuralları geçerli
sonuc1 = 2 + 3 * 4
sonuc2 = (2 + 3) * 4
sonuc3 = 2 ** 3 * 4
sonuc4 = 2 * 3 ** 2

print(f"2 + 3 * 4 = {sonuc1} (çarpma önce)")
print(f"(2 + 3) * 4 = {sonuc2} (parantez önce)")
print(f"2 ** 3 * 4 = {sonuc3} (üs alma önce)")
print(f"2 * 3 ** 2 = {sonuc4} (üs alma önce)")

print("\nOperatör öncelik sırası (yüksekten düşüğe):")
print("1. ** (üs alma)")
print("2. *, /, //, % (çarpma, bölme)")
print("3. +, - (toplama, çıkarma)")
print("4. Parantezler her zaman önceliklidir")

print("\n6. ÖZEL KULLANIM ÖRNEKLERİ:")
print("-" * 28)

# Çift/tek sayı kontrolü
sayi = 17
if sayi % 2 == 0:
    print(f"{sayi} çift sayıdır")
else:
    print(f"{sayi} tek sayıdır")

# Sayının kaç basamaklı olduğunu bulma
sayi = 12345
basamak_sayisi = len(str(sayi))
print(f"{sayi} sayısı {basamak_sayisi} basamaklıdır")

# Bir sayının rakamları toplamı
sayi = 1234
rakam_toplami = sum(int(rakam) for rakam in str(sayi))
print(f"{sayi} sayısının rakamları toplamı: {rakam_toplami}")

# Faktoriyel hesaplama (basit)
n = 5
faktoriyel = 1
temp_n = n
while temp_n > 0:
    faktoriyel *= temp_n
    temp_n -= 1
print(f"{n}! = {faktoriyel}")

print("\n7. HATA ÖRNEKLERİ:")
print("-" * 17)

print("DİKKAT: Bu hatalar koda yazılırsa program çöker!")
print("# ZeroDivisionError örnekleri:")
print("# 10 / 0        # Sıfıra bölme hatası")
print("# 10 // 0       # Sıfıra bölme hatası") 
print("# 10 % 0        # Sıfıra bölme hatası")

# Güvenli bölme örneği
def guvenli_bolme(bolunen, bolen):
    if bolen == 0:
        return "Sıfıra bölme hatası!"
    return bolunen / bolen

print(f"\nGüvenli bölme: 10/2 = {guvenli_bolme(10, 2)}")
print(f"Güvenli bölme: 10/0 = {guvenli_bolme(10, 0)}")

print("\n=== ARİTMETİK OPERATÖR ÖZETİ ===")
print("+   : Toplama")
print("-   : Çıkarma")
print("*   : Çarpma")
print("/   : Bölme (float sonuç)")
print("//  : Taban bölme (int sonuç)")
print("%   : Mod (kalan)")
print("**  : Üs alma")