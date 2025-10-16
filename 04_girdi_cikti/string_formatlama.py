# String Formatlaması
# Python'da string formatlama yöntemleri

print("=== STRING FORMATLAMASI ===\n")

# Test verileri
isim = "Ahmet"
soyisim = "Yılmaz"
yas = 25
maas = 5500.75
pi = 3.14159

print("1. % FORMATLAMASI (ESKİ YÖNTEM):")
print("-" * 34)

# Temel % formatlaması
print("İsim: %s" % isim)
print("Yaş: %d" % yas)
print("Maaş: %.2f" % maas)

# Çoklu değer formatlaması
print("Ad: %s, Soyad: %s, Yaş: %d" % (isim, soyisim, yas))

# Farklı format kodları
print("\nFormat kodları:")
print("%%s - String: %s" % "merhaba")
print("%%d - Integer: %d" % 42)
print("%%f - Float: %f" % pi)
print("%%.2f - 2 ondalık: %.2f" % pi)
print("%%10s - 10 karakter genişlik: '%10s'" % "test")
print("%%-10s - Sola hizalı: '%-10s'" % "test")

print("\n2. .format() YÖNTEM​İ:")
print("-" * 21)

# Temel format() kullanımı
print("İsim: {}".format(isim))
print("İsim: {}, Yaş: {}".format(isim, yas))

# İndeks ile format
print("Yaş: {1}, İsim: {0}".format(isim, yas))

# İsim ile format
print("İsim: {ad}, Soyisim: {soyad}".format(ad=isim, soyad=soyisim))

# Karışık format
print("{0} {soyad} {1} yaşında".format(isim, yas, soyad=soyisim))

print("\nFormat özellikleri:")
print("Sayı formatı: {:.2f}".format(pi))
print("Yüzde: {:.1%}".format(0.856))
print("Genişlik: '{:10}'".format("test"))
print("Sağa hizalı: '{:>10}'".format("test"))
print("Sola hizalı: '{:<10}'".format("test"))
print("Ortala: '{:^10}'".format("test"))
print("Sıfır ile doldur: '{:08d}'".format(42))

print("\n3. f-STRING (MODERN YÖNTEM):")
print("-" * 29)

# Temel f-string kullanımı
print(f"İsim: {isim}")
print(f"İsim: {isim}, Yaş: {yas}")
print(f"Tam bilgi: {isim} {soyisim} {yas} yaşında")

# İfadelerle f-string
print(f"5 yıl sonra yaşı: {yas + 5}")
print(f"İsim uzunluğu: {len(isim)}")
print(f"Büyük harf: {isim.upper()}")

# Format özellikleriyle f-string
print(f"Pi sayısı: {pi:.3f}")
print(f"Maaş: {maas:,.2f} TL")
print(f"Yüzde: {0.856:.1%}")
print(f"Sağa hizalı: '{isim:>15}'")
print(f"Sola hizalı: '{isim:<15}'")
print(f"Ortalı: '{isim:^15}'")

print("\n4. SAYISAL FORMATLAMA:")
print("-" * 22)

sayi = 1234567.89
print(f"Sayı: {sayi}")
print(f"Virgüllerle: {sayi:,}")
print(f"2 ondalık: {sayi:.2f}")
print(f"Bilimsel: {sayi:.2e}")
print(f"Yüzde: {sayi:.0%}")

# Para formatlaması
fiyat = 1250.5
print(f"\nFiyat formatları:")
print(f"Temel: {fiyat}")
print(f"TL ile: {fiyat:.2f} TL")
print(f"Virgüllü: {fiyat:,.2f} TL")
print(f"Genişlik: {fiyat:>10.2f} TL")

print("\n5. TARİH VE SAAT FORMATLAMASI:")
print("-" * 31)

from datetime import datetime
simdi = datetime.now()

print(f"Ham tarih: {simdi}")
print(f"Kısa tarih: {simdi.strftime('%d.%m.%Y')}")
print(f"Uzun tarih: {simdi.strftime('%d %B %Y')}")
print(f"Saat: {simdi.strftime('%H:%M:%S')}")
print(f"Tam format: {simdi.strftime('%d.%m.%Y %H:%M')}")

# f-string içinde format
print(f"Bugün: {simdi:%d.%m.%Y}")
print(f"Şu an: {simdi:%H:%M}")

print("\n6. ÇOKLU SATIR FORMATLAMASI:")
print("-" * 30)

# Çoklu satır string
mesaj = f"""
Merhaba {isim} {soyisim}!

Sizin bilgileriniz:
- Yaş: {yas}
- Maaş: {maas:,.2f} TL
- Durumunuz: {'Genç' if yas < 30 else 'Olgun'}

İyi günler dileriz!
"""
print(mesaj)

print("\n7. ÖZEL FORMATLAMA ÖRNEKLERİ:")
print("-" * 30)

# Tablo formatlaması
print(f"{'İsim':<12} {'Yaş':<5} {'Maaş':<10}")
print("-" * 30)
print(f"{isim:<12} {yas:<5} {maas:<10.2f}")
print(f"{'Mehmet':<12} {30:<5} {6000.00:<10.2f}")
print(f"{'Ayşe':<12} {28:<5} {5200.50:<10.2f}")

# Koşullu formatlama
durum = "Başarılı" if yas > 18 else "Başarısız"
print(f"\nDurum: {durum}")
print(f"Renk kodu: {durum.upper() if durum == 'Başarılı' else durum.lower()}")

# Dinamik genişlik
genislik = 15
print(f"Dinamik genişlik: '{isim:>{genislik}}'")

print("\n8. HATA ÖRNEKLERİ VE ÇÖZÜMLER:")
print("-" * 30)

print("Yaygın hatalar:")
print("1. Sayı formatını string'e uygulama")
# print(f"{'123':d}")  # Hata verir!

print("2. Eksik süslü parantez")
# print(f"İsim: {isim")  # Hata verir!

print("3. Format özelliklerini karıştırma")
# print(f"{isim:.2f}")  # String'e float formatı!

print("\nDoğru kullanım:")
print(f"String: {isim}")
print(f"Sayı: {yas:d}")
print(f"Float: {pi:.2f}")

print("\n9. PERFORMANS KARŞILAŞTIRMASI:")
print("-" * 30)

print("Hız sıralaması (hızdan yavaşa):")
print("1. f-string (en hızlı)")
print("2. .format() (orta)")
print("3. % formatting (en yavaş)")
print()
print("Önerimiz: Modern Python'da f-string kullanın!")

print("\n=== FORMAT YÖNTEM ÖZETİ ===")
print("% formatting:")
print("  'İsim: %s, Yaş: %d' % (isim, yas)")
print()
print(".format():")
print("  'İsim: {}, Yaş: {}'.format(isim, yas)")
print("  'İsim: {ad}, Yaş: {yas}'.format(ad=isim, yas=yas)")
print()
print("f-string (önerilen):")
print("  f'İsim: {isim}, Yaş: {yas}'")
print("  f'Pi: {pi:.2f}'")
print()
print("Format kodları:")
print("  :d   → integer")
print("  :f   → float")
print("  :.2f → 2 ondalık")
print("  :>10 → sağa hizalı, 10 karakter")
print("  :<10 → sola hizalı, 10 karakter")
print("  :^10 → ortalı, 10 karakter")