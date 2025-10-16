# Küme (Set) Veri Tipi ve İşlemleri
# Python küme veri tipinin detaylı incelenmesi

print("=== KÜME (SET) VERİ TİPİ VE İŞLEMLERİ ===\n")

print("1. KÜME OLUŞTURMA:")
print("-" * 18)

# Boş küme
bos_kume = set()
print(f"Boş küme: {bos_kume}, tip: {type(bos_kume)}")

# DİKKAT: {} sözlük oluşturur, küme değil!
bos_sozluk = {}
print(f"Boş dict: {bos_sozluk}, tip: {type(bos_sozluk)}")

# Küme oluşturma yöntemleri
sayilar = {1, 2, 3, 4, 5}
print(f"Sayı kümesi: {sayilar}")

# set() fonksiyonu ile
liste_den = set([1, 2, 3, 3, 4, 4, 5])  # Tekrar eden elemanlara izin verilmez
print(f"Liste'den: {liste_den}")

string_den = set("Python")
print(f"String'den: {string_den}")

tuple_den = set((1, 2, 3, 2, 1))
print(f"Tuple'dan: {tuple_den}")

range_den = set(range(5))
print(f"Range'den: {range_den}")

# Karışık tip küme
karışık = {1, "metin", 3.14, True, (1, 2)}
print(f"Karışık küme: {karışık}")

# Mutable objeler küme elemanı olamaz
try:
    hatalı_kume = {1, 2, [3, 4]}  # Liste eklenemez
except TypeError as e:
    print(f"Hata: {e}")

print("\n2. KÜME ÖZELLİKLERİ:")
print("-" * 17)

# Unordered - sırasız
kume = {3, 1, 4, 1, 5, 9, 2, 6}
print(f"Sırasız küme: {kume}")

# Unique - tekil elemanlar
tekrar_eden = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
tekil_kume = set(tekrar_eden)
print(f"Tekrar eden liste: {tekrar_eden}")
print(f"Tekil küme: {tekil_kume}")

# Mutable - değiştirilebilir
kume.add(10)
print(f"10 eklendi: {kume}")

kume.remove(1)
print(f"1 silindi: {kume}")

# Hashable elemanlr gerekli
hashable_elemanlar = {1, "str", 3.14, True, None, (1, 2)}
print(f"Hashable elemanlar: {hashable_elemanlar}")

# Boyut
print(f"Küme uzunluğu: {len(kume)}")

print("\n3. KÜME TEMEL İŞLEMLERİ:")
print("-" * 24)

# Test kümeleri
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(f"A kümesi: {A}")
print(f"B kümesi: {B}")

# Üyelik kontrolü
print(f"3 A'da mı: {3 in A}")
print(f"6 A'da mı: {6 in A}")
print(f"9 B'de değil mi: {9 not in B}")

# Eleman ekleme
C = {1, 2, 3}
print(f"C başlangıç: {C}")

C.add(4)
print(f"add(4): {C}")

C.update([5, 6, 7])
print(f"update([5,6,7]): {C}")

C.update({8, 9})
print(f"update({{8,9}}): {C}")

C.update("abc")  # String'den karakterler
print(f"update('abc'): {C}")

# Eleman silme
print(f"\nSilme işlemleri - C: {C}")

C.remove(1)  # KeyError verip eleman yoksa
print(f"remove(1): {C}")

C.discard(2)  # Hata vermez eleman yoksa
print(f"discard(2): {C}")

C.discard(99)  # Olmayan eleman, hata yok
print(f"discard(99): {C}")

# pop() - rastgele eleman çıkar
eleman = C.pop()
print(f"pop(): {eleman}, kalan: {C}")

# clear() - tüm elemanları sil
D = {1, 2, 3}
D.clear()
print(f"clear() sonrası: {D}")

print("\n4. KÜME MATEMATİKSEL İŞLEMLERİ:")
print("-" * 30)

# Test kümeleri
X = {1, 2, 3, 4, 5}
Y = {4, 5, 6, 7, 8}
Z = {1, 2, 3}

print(f"X: {X}")
print(f"Y: {Y}")
print(f"Z: {Z}")

# Birleşim (Union)
birlesim1 = X | Y
birlesim2 = X.union(Y)
print(f"Birleşim X|Y: {birlesim1}")
print(f"union(Y): {birlesim2}")

# Çoklu birleşim
W = {9, 10}
coklu_birlesim = X.union(Y, Z, W)
print(f"Çoklu birleşim: {coklu_birlesim}")

# Kesişim (Intersection)
kesisim1 = X & Y
kesisim2 = X.intersection(Y)
print(f"Kesişim X&Y: {kesisim1}")
print(f"intersection(Y): {kesisim2}")

# Fark (Difference)
fark1 = X - Y
fark2 = X.difference(Y)
print(f"Fark X-Y: {fark1}")
print(f"difference(Y): {fark2}")

fark_ters = Y - X
print(f"Fark Y-X: {fark_ters}")

# Simetrik fark (Symmetric Difference)
simetrik1 = X ^ Y
simetrik2 = X.symmetric_difference(Y)
print(f"Simetrik X^Y: {simetrik1}")
print(f"symmetric_difference(Y): {simetrik2}")

print("\n5. KÜME KARŞILAŞTIRMA İŞLEMLERİ:")
print("-" * 31)

# Test kümeleri
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 3}
D = {4, 5, 6}

print(f"A: {A}")
print(f"B: {B}")
print(f"C: {C}")
print(f"D: {D}")

# Eşitlik
print(f"A == C: {A == C}")
print(f"A == B: {A == B}")

# Alt küme (Subset)
print(f"A ⊆ B (issubset): {A.issubset(B)}")
print(f"A <= B: {A <= B}")
print(f"B ⊆ A: {B.issubset(A)}")

# Gerçek alt küme (Proper subset)
print(f"A ⊂ B (proper subset): {A < B}")
print(f"A ⊂ C (proper subset): {A < C}")  # False, eşit oldukları için

# Üst küme (Superset)
print(f"B ⊇ A (issuperset): {B.issuperset(A)}")
print(f"B >= A: {B >= A}")

# Gerçek üst küme (Proper superset)
print(f"B ⊃ A (proper superset): {B > A}")

# Ayrık kümeler (Disjoint)
print(f"A ∩ D = ∅ (isdisjoint): {A.isdisjoint(D)}")
print(f"A ∩ B = ∅: {A.isdisjoint(B)}")

print("\n6. KÜME GÜNCELLEME İŞLEMLERİ:")
print("-" * 27)

# Test kümeleri
S1 = {1, 2, 3}
S2 = {3, 4, 5}
S3 = {1, 2, 3}

print(f"S1: {S1}")
print(f"S2: {S2}")

# update() / |= (birleşim güncelleme)
S1 |= S2  # S1 = S1 | S2
print(f"S1 |= S2: {S1}")

# intersection_update() / &= (kesişim güncelleme)
S1 = {1, 2, 3, 4, 5}
S1 &= S2  # S1 = S1 & S2
print(f"S1 &= S2: {S1}")

# difference_update() / -= (fark güncelleme)
S1 = {1, 2, 3, 4, 5}
S1 -= S2  # S1 = S1 - S2
print(f"S1 -= S2: {S1}")

# symmetric_difference_update() / ^= (simetrik fark güncelleme)
S1 = {1, 2, 3}
S1 ^= S2  # S1 = S1 ^ S2
print(f"S1 ^= S2: {S1}")

print("\n7. KÜME COMPREHENSION:")
print("-" * 21)

# Temel sözdizimi
kareler = {x**2 for x in range(10)}
print(f"Kareler: {kareler}")

# Koşullu comprehension
cift_kareler = {x**2 for x in range(10) if x % 2 == 0}
print(f"Çift kareler: {cift_kareler}")

# String işlemleri
kelimeler = ["python", "java", "go", "python", "java"]
tekil_kelimeler = {kelime.upper() for kelime in kelimeler}
print(f"Tekil kelimeler: {tekil_kelimeler}")

# Karmaşık işlemler
sayilar = range(1, 21)
asal_kume = {x for x in sayilar if all(x % i != 0 for i in range(2, int(x**0.5) + 1)) and x > 1}
print(f"Asal sayılar: {asal_kume}")

# İç içe comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
tum_elemanlar = {eleman for satir in matrix for eleman in satir}
print(f"Matrix elemanları: {tum_elemanlar}")

print("\n8. FROZENSET - DEĞİŞMEZ KÜME:")
print("-" * 28)

# frozenset oluşturma
normal_set = {1, 2, 3, 4}
frozen = frozenset([1, 2, 3, 4])
print(f"Normal set: {normal_set}")
print(f"Frozenset: {frozen}")

# frozenset immutable
try:
    frozen.add(5)  # AttributeError!
except AttributeError as e:
    print(f"frozenset değiştirilemez: {e}")

# frozenset hashable - sözlük anahtarı olabilir
set_dict = {
    frozenset([1, 2]): "küçük",
    frozenset([1, 2, 3, 4]): "büyük"
}
print(f"frozenset anahtarlar: {set_dict}")

# frozenset küme elemanı olabilir
kume_kumesi = {frozenset([1, 2]), frozenset([3, 4])}
print(f"Küme kümesi: {kume_kumesi}")

# frozenset işlemleri (yeni frozenset döner)
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])

birlesim = fs1 | fs2
print(f"frozenset birleşim: {birlesim}")

kesisim = fs1 & fs2
print(f"frozenset kesişim: {kesisim}")

print("\n9. KÜME PERFORMANCE ANALİZİ:")
print("-" * 26)

import time

# Büyük veri setleri
n = 100000
büyük_liste = list(range(n))
büyük_küme = set(range(n))

print(f"{n} elemanlı veri yapıları:")

# Üyelik kontrolü performansı
# Liste'de arama (O(n))
start = time.time()
for i in range(1000):
    _ = i in büyük_liste
liste_arama = time.time() - start

# Küme'de arama (O(1))
start = time.time()
for i in range(1000):
    _ = i in büyük_küme
kume_arama = time.time() - start

print(f"Liste arama (1000 kez): {liste_arama*1000:.2f} ms")
print(f"Küme arama (1000 kez): {kume_arama*1000:.2f} ms")
print(f"Küme {liste_arama/kume_arama:.0f}x daha hızlı")

# Birleşim performansı
liste1 = list(range(5000))
liste2 = list(range(2500, 7500))
kume1 = set(range(5000))
kume2 = set(range(2500, 7500))

# Liste birleşimi (naive)
start = time.time()
liste_birlesim = list(set(liste1 + liste2))
liste_union_time = time.time() - start

# Küme birleşimi
start = time.time()
kume_birlesim = kume1 | kume2
kume_union_time = time.time() - start

print(f"Liste birleşim: {liste_union_time*1000:.2f} ms")
print(f"Küme birleşim: {kume_union_time*1000:.2f} ms")
print(f"Küme {liste_union_time/kume_union_time:.0f}x daha hızlı")

print("\n10. KÜME KULLANIM ALANLARI:")
print("-" * 24)

# 1. Tekil elemanlar bulma
veriler = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
tekil = list(set(veriler))
print(f"Tekil elemanlar: {tekil}")

# 2. Hızlı üyelik kontrolü
izinli_kullanicilar = {"admin", "user1", "user2", "moderator"}

def kullanici_yetkili_mi(kullanici):
    return kullanici in izinli_kullanicilar

print(f"admin yetkili: {kullanici_yetkili_mi('admin')}")
print(f"guest yetkili: {kullanici_yetkili_mi('guest')}")

# 3. Veri temizleme
kirli_veri = ["  Python  ", "Java", "  Python  ", "Go", "Java", "  C++  "]
temiz_veri = {veri.strip() for veri in kirli_veri}
print(f"Temiz veri: {temiz_veri}")

# 4. Kesişim analizi
takım_a = {"Ali", "Veli", "Ayşe", "Mehmet"}
takım_b = {"Veli", "Fatma", "Ahmet", "Ayşe"}

ortak_oyuncular = takım_a & takım_b
sadece_a = takım_a - takım_b
sadece_b = takım_b - takım_a

print(f"Ortak oyuncular: {ortak_oyuncular}")
print(f"Sadece A takımında: {sadece_a}")
print(f"Sadece B takımında: {sadece_b}")

# 5. İzin ve rol yönetimi
kullanici_rolleri = {
    "admin": {"read", "write", "delete", "admin"},
    "editor": {"read", "write"},
    "viewer": {"read"}
}

def kullanici_yapabilir_mi(kullanici, eylem):
    roller = kullanici_rolleri.get(kullanici, set())
    return eylem in roller

print(f"admin delete: {kullanici_yapabilir_mi('admin', 'delete')}")
print(f"viewer write: {kullanici_yapabilir_mi('viewer', 'write')}")

print("\n11. KÜME ALGORİTMA ÖRNEKLERİ:")
print("-" * 27)

# 1. Graf algoritması - komşuluk
graf = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

def komsular(dugum):
    return graf.get(dugum, set())

def ortak_komsular(dugum1, dugum2):
    return komsular(dugum1) & komsular(dugum2)

print(f"A'nın komşuları: {komsular('A')}")
print(f"B'nin komşuları: {komsular('B')}")
print(f"A-B ortak komşuları: {ortak_komsular('A', 'B')}")

# 2. Kelime analizi
def kelime_analizi(metin1, metin2):
    kelimeler1 = set(metin1.lower().split())
    kelimeler2 = set(metin2.lower().split())
    
    ortak = kelimeler1 & kelimeler2
    sadece1 = kelimeler1 - kelimeler2
    sadece2 = kelimeler2 - kelimeler1
    
    return {
        "ortak": ortak,
        "sadece_1": sadece1,
        "sadece_2": sadece2,
        "benzerlik": len(ortak) / len(kelimeler1 | kelimeler2)
    }

metin1 = "Python programlama dili çok güçlüdür"
metin2 = "Java programlama dili popülerdir"

analiz = kelime_analizi(metin1, metin2)
print(f"Kelime analizi:")
print(f"  Ortak: {analiz['ortak']}")
print(f"  Sadece 1: {analiz['sadece_1']}")
print(f"  Sadece 2: {analiz['sadece_2']}")
print(f"  Benzerlik: {analiz['benzerlik']:.2f}")

# 3. Bloom filter simülasyonu (basit)
class SimpleBloomFilter:
    def __init__(self, size=100):
        self.size = size
        self.bits = set()
    
    def _hash(self, item):
        return [hash(str(item) + str(i)) % self.size for i in range(3)]
    
    def add(self, item):
        for h in self._hash(item):
            self.bits.add(h)
    
    def might_contain(self, item):
        return all(h in self.bits for h in self._hash(item))

bloom = SimpleBloomFilter()
bloom.add("python")
bloom.add("java")

print(f"Bloom filter:")
print(f"  'python' var mı: {bloom.might_contain('python')}")
print(f"  'go' var mı: {bloom.might_contain('go')}")

print("\n12. KÜME HATALARI VE ÇÖZÜMLER:")
print("-" * 27)

# 1. Mutable eleman hatası
try:
    hatalı = {[1, 2, 3]}  # Liste hashable değil
except TypeError as e:
    print(f"Mutable eleman hatası: {e}")

# Çözüm: tuple kullan
doğru = {(1, 2, 3)}
print(f"Doğru kullanım: {doğru}")

# 2. Empty set notasyonu
boş_sözlük = {}  # Bu sözlük!
boş_küme = set()  # Bu küme!
print(f"Boş sözlük: {boş_sözlük}, tip: {type(boş_sözlük)}")
print(f"Boş küme: {boş_küme}, tip: {type(boş_küme)}")

# 3. Set değişirken iterasyon
test_set = {1, 2, 3, 4, 5}
# YANLIŞ
try:
    for item in test_set:
        if item % 2 == 0:
            test_set.remove(item)  # RuntimeError!
except RuntimeError as e:
    print(f"İterasyon hatası: {e}")

# DOĞRU
test_set = {1, 2, 3, 4, 5}
silinecekler = {item for item in test_set if item % 2 == 0}
test_set -= silinecekler
print(f"Güvenli silme: {test_set}")

print("\n13. KÜME EN İYİ PRATİKLER:")
print("-" * 26)

print("✓ Küme KULLAN:")
print("  • Hızlı üyelik kontrolü gerektiğinde")
print("  • Tekil elemanlar istediğinizde")
print("  • Matematiksel küme işlemleri için")
print("  • Büyük veri setlerinde arama")

print("\n✗ Küme KULLANMA:")
print("  • Sıra önemli ise")
print("  • Index erişimi gerekirse")
print("  • Tekrar eden elemanlar istiyorsanız")
print("  • Mutable elemanlar varsa")

# Performans karşılaştırması
def performance_test():
    import random
    
    # Test verisi
    data = [random.randint(1, 1000) for _ in range(10000)]
    
    # Liste ile tekil bulma
    start = time.time()
    unique_list = []
    for item in data:
        if item not in unique_list:
            unique_list.append(item)
    list_time = time.time() - start
    
    # Set ile tekil bulma
    start = time.time()
    unique_set = set(data)
    set_time = time.time() - start
    
    print(f"\n10000 elemanda tekil bulma:")
    print(f"Liste yöntemi: {list_time*1000:.2f} ms")
    print(f"Set yöntemi: {set_time*1000:.2f} ms")
    print(f"Set {list_time/set_time:.0f}x daha hızlı")

performance_test()

print("\n=== KÜME ÖZETİ ===")
print("Özellikler:")
print("  • Mutable (değiştirilebilir)")
print("  • Unordered (sırasız)")
print("  • Unique elements (tekil elemanlar)")
print("  • Hashable elements only")
print("  • O(1) average üyelik kontrolü")
print()
print("Temel işlemler:")
print("  • add(item) - eleman ekle")
print("  • remove(item) - eleman sil (KeyError)")
print("  • discard(item) - eleman sil (hata yok)")
print("  • pop() - rastgele eleman çıkar")
print("  • clear() - tümünü sil")
print()
print("Matematiksel işlemler:")
print("  • | union - birleşim")
print("  • & intersection - kesişim")
print("  • - difference - fark")
print("  • ^ symmetric_difference - simetrik fark")
print()
print("Karşılaştırma:")
print("  • <= subset - alt küme")
print("  • >= superset - üst küme")
print("  • < proper subset - gerçek alt küme")
print("  • > proper superset - gerçek üst küme")
print("  • isdisjoint() - ayrık mı")
print()
print("Kullanım alanları:")
print("  • Tekil elemanlar")
print("  • Hızlı arama")
print("  • Matematiksel işlemler")
print("  • Veri analizi")
print("  • Graf algoritmaları")