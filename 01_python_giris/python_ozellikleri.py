# Python'un Temel Özellikleri
# Bu dosya Python dilinin temel özelliklerini gösterir

print("=== PYTHON'UN TEMEl ÖZELLİKLERİ ===\n")

# 1. Python Yorumlayıcı Dil (Interpreted Language)
print("1. Python yorumlayıcı bir dildir")
print("   Kod satır satır çalıştırılır\n")

# 2. Dinamik Tip Sistemi
print("2. Dinamik tip sistemi:")
degisken = 42
print(f"   degisken = {degisken} (tip: {type(degisken)})")
degisken = "Merhaba"
print(f"   degisken = {degisken} (tip: {type(degisken)})")
degisken = [1, 2, 3]
print(f"   degisken = {degisken} (tip: {type(degisken)})\n")

# 3. Girintileme (Indentation) ile Kod Blokları
print("3. Girintileme ile kod blokları:")
if True:
    print("   Bu satır girintili")
    print("   Bu da aynı blokta")
print("   Bu satır ana seviyede\n")

# 4. Büyük/Küçük Harf Duyarlılığı (Case Sensitive)
print("4. Büyük/küçük harf duyarlılığı:")
isim = "Python"
Isim = "PYTHON"
print(f"   isim = {isim}")
print(f"   Isim = {Isim}")
print("   Bu iki değişken farklıdır!\n")

# 5. Kolay Okunabilir Syntax
print("5. Kolay okunabilir söz dizimi:")
sayilar = [1, 2, 3, 4, 5]
for sayi in sayilar:
    if sayi % 2 == 0:
        print(f"   {sayi} çift sayıdır")
    else:
        print(f"   {sayi} tek sayıdır")

print("\n=== PYTHON'UN AVANTAJLARI ===")
print("✓ Öğrenmesi kolay")
print("✓ Geniş kütüphane desteği") 
print("✓ Platform bağımsız")
print("✓ Açık kaynak kodlu")
print("✓ Büyük topluluk desteği")