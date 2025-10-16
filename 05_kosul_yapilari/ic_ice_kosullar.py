# İç İçe Koşullar (Nested If)
# Koşulların içinde başka koşullar

print("=== İÇ İÇE KOŞUL YAPILARI ===\n")

print("1. BASIT İÇ İÇE IF:")
print("-" * 20)

# Temel iç içe yapı
yas = 20
lisans = True
print(f"Yaş: {yas}, Lisans: {lisans}")

if yas >= 18:
    print("Yaş uygun")
    if lisans:
        print("Ehliyet alabilir")
    else:
        print("Önce lisans kursuna gitmelidir")
else:
    print("Yaş uygun değil")

print("\n2. ÜÇ SEVİYELİ İÇ İÇE YAPI:")
print("-" * 27)

# Kredi başvuru sistemi
yas = 25
gelir = 4000
kredi_notu = 750
print(f"Yaş: {yas}, Gelir: {gelir}, Kredi Notu: {kredi_notu}")

if yas >= 18:
    print("✓ Yaş kontrolü geçti")
    if gelir >= 3000:
        print("✓ Gelir kontrolü geçti")
        if kredi_notu >= 700:
            print("✓ Kredi notu uygun")
            print("🎉 KREDİ BAŞVURUSU ONAYLANDI!")
        else:
            print("✗ Kredi notu yetersiz (min 700)")
            print("❌ Kredi başvurusu reddedildi")
    else:
        print("✗ Gelir yetersiz (min 3000)")
        print("❌ Kredi başvurusu reddedildi")
else:
    print("✗ Yaş uygun değil (min 18)")
    print("❌ Kredi başvurusu reddedildi")

print("\n3. KARMAŞIK İÇ İÇE YAPI:")
print("-" * 24)

# Üniversite bölüm yerleştirme
matematik_puani = 85
fen_puani = 78
dil_puani = 92
tercih = "mühendislik"

print(f"Matematik: {matematik_puani}, Fen: {fen_puani}, Dil: {dil_puani}")
print(f"Tercih: {tercih}")

if tercih == "mühendislik":
    print("Mühendislik bölümü kontrolü:")
    if matematik_puani >= 80:
        if fen_puani >= 75:
            print("✓ Mühendislik için uygun")
            if matematik_puani >= 90 and fen_puani >= 85:
                print("🌟 Bilgisayar Mühendisliği önerisi")
            elif matematik_puani >= 85:
                print("🔧 Makine Mühendisliği önerisi")
            else:
                print("⚡ Elektrik Mühendisliği önerisi")
        else:
            print("✗ Fen puanı yetersiz")
    else:
        print("✗ Matematik puanı yetersiz")

elif tercih == "tıp":
    print("Tıp fakültesi kontrolü:")
    if fen_puani >= 85:
        if matematik_puani >= 75:
            print("✓ Tıp için uygun")
        else:
            print("✗ Matematik puanı yetersiz")
    else:
        print("✗ Fen puanı yetersiz")

elif tercih == "edebiyat":
    print("Edebiyat fakültesi kontrolü:")
    if dil_puani >= 80:
        print("✓ Edebiyat için uygun")
        if dil_puani >= 90:
            print("📚 Türk Dili ve Edebiyatı önerisi")
        else:
            print("🌍 Coğrafya önerisi")
    else:
        print("✗ Dil puanı yetersiz")

print("\n4. İÇ İÇE IF-ELSE KARMA:")
print("-" * 24)

# Hava durumu aktivite önerisi
hava = "güneşli"
sicaklik = 25
ruzgar = False
print(f"Hava: {hava}, Sıcaklık: {sicaklik}°C, Rüzgarlı: {ruzgar}")

if hava == "güneşli":
    print("Güneşli hava 🌞")
    if sicaklik > 20:
        print("Sıcaklık ideal")
        if not ruzgar:
            print("🏖️ Piknik için mükemmel!")
            print("🚴 Bisiklet gezisi yapabilirsiniz")
        else:
            print("🎯 Uçurtma uçurmak için harika!")
    else:
        print("Biraz serin")
        if ruzgar:
            print("🧥 Rüzgarlık giyin")
        else:
            print("☕ Açık havada kahve içilebilir")
            
elif hava == "yağmurlu":
    print("Yağmurlu hava 🌧️")
    if sicaklik > 15:
        print("🏠 İç mekan aktiviteleri önerisi:")
        print("📖 Kitap okuma")
        print("🎬 Film izleme")
    else:
        print("🔥 Sıcak içecek için ideal")
        
else:
    print("😶‍🌫️ Belirsiz hava durumu")

print("\n5. KULLANICI YETKİ SİSTEMİ:")
print("-" * 26)

# Çok seviyeli yetki kontrolü
kullanici_tipi = "admin"
aktif = True
ip_guvenli = True
iki_faktor = True

print(f"Tip: {kullanici_tipi}, Aktif: {aktif}, Güvenli IP: {ip_guvenli}, 2FA: {iki_faktor}")

if aktif:
    print("✓ Kullanıcı aktif")
    if ip_guvenli:
        print("✓ IP adresi güvenli")
        if kullanici_tipi == "admin":
            print("👑 Admin yetkisi tespit edildi")
            if iki_faktor:
                print("🔐 İki faktörlü doğrulama başarılı")
                print("🎯 TÜM YETKİLERE ERİŞİM SAĞLANDI")
                print("  - Kullanıcı yönetimi")
                print("  - Sistem ayarları")
                print("  - Veri yönetimi")
            else:
                print("⚠️ İki faktörlü doğrulama gerekli")
                print("📱 Telefona kod gönderildi")
        elif kullanici_tipi == "moderator":
            print("🛡️ Moderatör yetkisi")
            print("📝 İçerik yönetimi erişimi")
        else:
            print("👤 Normal kullanıcı")
            print("📄 Sadece okuma yetkisi")
    else:
        print("🚫 Güvenli olmayan IP adresi")
        print("🔒 Erişim engellendi")
else:
    print("❌ Kullanıcı hesabı pasif")

print("\n6. OYUN SKORU DEĞERLENDİRME:")
print("-" * 29)

# Oyun performans analizi
puan = 8500
level = 15
bonus = True
zaman = 120  # saniye

print(f"Puan: {puan}, Level: {level}, Bonus: {bonus}, Süre: {zaman}s")

if puan >= 5000:
    print("🎮 İyi performans!")
    if level >= 10:
        print("🏆 Deneyimli oyuncu")
        if bonus:
            print("⭐ Bonus aktif!")
            if zaman <= 150:
                print("⚡ Hızlı tamamlama bonusu!")
                final_puan = puan * 1.5
                print(f"🎯 Final puan: {final_puan}")
                if final_puan >= 10000:
                    print("👑 EFSANE PERFORMANS!")
                else:
                    print("🥇 MÜKEMMEL PERFORMANS!")
            else:
                print("⏰ Zaman bonusu yok")
                final_puan = puan * 1.2
                print(f"📊 Final puan: {final_puan}")
        else:
            print("😐 Bonus aktif değil")
    else:
        print("🔰 Acemi seviye")
else:
    print("📉 Düşük performans")

print("\n7. ALIŞVERİŞ İNDİRİM SİSTEMİ:")
print("-" * 29)

# Karmaşık indirim hesaplama
toplam_tutar = 250
uye_tipi = "gold"
kargo_ucretsiz_limit = 200
kampanya_kodu = "INDIRIM20"

print(f"Tutar: {toplam_tutar}₺, Üye: {uye_tipi}, Kampanya: {kampanya_kodu}")

if toplam_tutar >= 100:
    print("✓ Minimum alışveriş tutarı")
    if uye_tipi in ["gold", "platinum"]:
        print(f"✓ {uye_tipi.title()} üyelik avantajı")
        if uye_tipi == "platinum":
            indirim_orani = 0.20
            print("💎 Platinum indirim: %20")
        else:
            indirim_orani = 0.15
            print("🥇 Gold indirim: %15")
            
        if kampanya_kodu == "INDIRIM20":
            print("🎟️ Kampanya kodu geçerli (+%5)")
            indirim_orani += 0.05
            
        indirim_tutari = toplam_tutar * indirim_orani
        final_tutar = toplam_tutar - indirim_tutari
        
        print(f"💰 İndirim tutarı: {indirim_tutari:.2f}₺")
        print(f"💸 Ödenecek tutar: {final_tutar:.2f}₺")
        
        if final_tutar >= kargo_ucretsiz_limit:
            print("🚚 Kargo ücretsiz!")
        else:
            kargo_ucreti = 15
            final_tutar += kargo_ucreti
            print(f"📦 Kargo ücreti: {kargo_ucreti}₺")
            print(f"🧾 Toplam: {final_tutar:.2f}₺")
    else:
        print("👤 Standart üyelik - indirim yok")
else:
    print("❌ Minimum alışveriş tutarı 100₺")

print("\n=== İÇ İÇE KOŞUL İPUÇLARI ===")
print("✓ Doğru Yaklaşım:")
print("  - Mantıklı sıralama yapın")
print("  - Girintileri doğru kullanın")
print("  - Her seviyeyi açık yorumlayın")
print("  - Çok derin yapmayın (max 4-5 seviye)")
print()
print("✗ Kaçınılması Gerekenler:")
print("  - Çok fazla iç içe yapı")
print("  - Karmaşık mantık")
print("  - Anlaşılması zor koşullar")
print("  - Gereksiz tekrarlar")
print()
print("💡 Alternatif Çözümler:")
print("  - Fonksiyonlar kullanın")
print("  - Early return pattern")
print("  - elif zinciri tercih edin")
print("  - Boolean değişkenler kullanın")