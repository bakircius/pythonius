"""
NumPy Temelleri - Array İşlemleri
NumPy kütüphanesinin temel özelliklerini ve array işlemlerini öğreniyoruz.
"""

import numpy as np
import matplotlib.pyplot as plt

print("=== NumPy Array İşlemleri ===\n")

# =============================================================================
# 1. ARRAY OLUŞTURMA
# =============================================================================

print("1. Array Oluşturma")
print("-" * 30)

# Liste'den array oluşturma
liste = [1, 2, 3, 4, 5]
arr1 = np.array(liste)
print(f"Liste'den array: {arr1}")
print(f"Array tipi: {type(arr1)}")
print(f"Element tipi: {arr1.dtype}")

# 2D array
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\n2D Array:\n{matrix}")

# Özel array'ler
zeros = np.zeros((3, 4))
ones = np.ones((2, 5))
eye = np.eye(3)  # Birim matrix
full = np.full((2, 3), 7)

print(f"\nSıfırlarla dolu array:\n{zeros}")
print(f"\nBirlerle dolu array:\n{ones}")
print(f"\nBirim matrix:\n{eye}")
print(f"\n7'lerle dolu array:\n{full}")

# Aralık array'leri
arange_arr = np.arange(0, 10, 2)  # 0'dan 10'a kadar 2'şer artırarak
linspace_arr = np.linspace(0, 1, 5)  # 0-1 arası 5 eşit parça

print(f"\nArange (0-10, 2'şer): {arange_arr}")
print(f"Linspace (0-1, 5 parça): {linspace_arr}")

# Random array'ler
np.random.seed(42)  # Tekrarlanabilir sonuçlar için
random_arr = np.random.random((3, 3))
randint_arr = np.random.randint(1, 10, (2, 4))
normal_arr = np.random.normal(0, 1, 10)  # Normal dağılım

print(f"\nRandom array:\n{random_arr}")
print(f"\nRandom integer array:\n{randint_arr}")
print(f"\nNormal dağılım: {normal_arr}")

# =============================================================================
# 2. ARRAY ÖZELLİKLERİ
# =============================================================================

print(f"\n2. Array Özellikleri")
print("-" * 30)

sample_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(f"Array:\n{sample_array}")
print(f"Şekil (shape): {sample_array.shape}")
print(f"Boyut sayısı (ndim): {sample_array.ndim}")
print(f"Toplam eleman sayısı (size): {sample_array.size}")
print(f"Veri tipi (dtype): {sample_array.dtype}")
print(f"Her elemanın boyutu (itemsize): {sample_array.itemsize} bytes")
print(f"Toplam bellek kullanımı (nbytes): {sample_array.nbytes} bytes")

# =============================================================================
# 3. ARRAY İNDEKSLEME VE DİLİMLEME
# =============================================================================

print(f"\n3. Array İndeksleme ve Dilimleme")
print("-" * 30)

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(f"Original array: {arr}")

# Temel indeksleme
print(f"İlk eleman: {arr[0]}")
print(f"Son eleman: {arr[-1]}")
print(f"2-5 arası: {arr[2:6]}")
print(f"Çift indeksler: {arr[::2]}")
print(f"Ters sırada: {arr[::-1]}")

# 2D array indeksleme
matrix2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\n2D Array:\n{matrix2d}")
print(f"1. satır: {matrix2d[0]}")
print(f"2. sütun: {matrix2d[:, 1]}")
print(f"Orta eleman: {matrix2d[1, 1]}")
print(f"Alt-sağ 2x2: \n{matrix2d[1:, 1:]}")

# Boolean indeksleme
condition = arr > 5
print(f"\n5'ten büyük olanlar: {arr[condition]}")
print(f"Çift sayılar: {arr[arr % 2 == 0]}")

# =============================================================================
# 4. MATEMATİKSEL İŞLEMLER
# =============================================================================

print(f"\n4. Matematiksel İşlemler")
print("-" * 30)

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(f"a: {a}")
print(f"b: {b}")

# Temel işlemler
print(f"Toplama: {a + b}")
print(f"Çıkarma: {a - b}")
print(f"Çarpma: {a * b}")
print(f"Bölme: {a / b}")
print(f"Üs alma: {a ** 2}")
print(f"Karekök: {np.sqrt(a)}")

# Skaler işlemler
print(f"\na + 10: {a + 10}")
print(f"a * 3: {a * 3}")

# Matematik fonksiyonları
angles = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])
print(f"\nAçılar (radyan): {angles}")
print(f"Sinüs: {np.sin(angles)}")
print(f"Kosinüs: {np.cos(angles)}")
print(f"Tanjant: {np.tan(angles)}")

# Logaritma ve üstel fonksiyonlar
numbers = np.array([1, 2, 4, 8, 16])
print(f"\nSayılar: {numbers}")
print(f"Doğal logaritma: {np.log(numbers)}")
print(f"10 tabanında log: {np.log10(numbers)}")
print(f"e üzeri x: {np.exp([1, 2, 3])}")

# =============================================================================
# 5. İSTATİSTİKSEL FONKSİYONLAR
# =============================================================================

print(f"\n5. İstatistiksel Fonksiyonlar")
print("-" * 30)

data = np.random.normal(50, 15, 1000)  # Ortalama 50, std 15, 1000 sample

print(f"Veri boyutu: {data.size}")
print(f"Minimum: {np.min(data):.2f}")
print(f"Maksimum: {np.max(data):.2f}")
print(f"Ortalama: {np.mean(data):.2f}")
print(f"Medyan: {np.median(data):.2f}")
print(f"Standart sapma: {np.std(data):.2f}")
print(f"Varyans: {np.var(data):.2f}")

# Yüzdelik dilimler
percentiles = [25, 50, 75, 90, 95]
for p in percentiles:
    print(f"{p}. yüzdelik: {np.percentile(data, p):.2f}")

# Korelasyon
x = np.random.randn(100)
y = 2 * x + np.random.randn(100) * 0.5  # x ile pozitif korelasyonlu
correlation = np.corrcoef(x, y)[0, 1]
print(f"\nKorelasyon katsayısı: {correlation:.3f}")

# =============================================================================
# 6. ARRAY ŞEKIL DEĞİŞTİRME
# =============================================================================

print(f"\n6. Array Şekil Değiştirme")
print("-" * 30)

original = np.arange(12)
print(f"Orijinal array: {original}")

# Reshape
reshaped_2d = original.reshape(3, 4)
reshaped_3d = original.reshape(2, 2, 3)

print(f"\n3x4 matrix:\n{reshaped_2d}")
print(f"\n2x2x3 tensor:\n{reshaped_3d}")

# Flatten
flattened = reshaped_2d.flatten()
print(f"\nDüzleştirilmiş: {flattened}")

# Transpose
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\nOrijinal matrix:\n{matrix}")
print(f"Transpose:\n{matrix.T}")

# =============================================================================
# 7. ARRAY BİRLEŞTİRME VE AYIRMA
# =============================================================================

print(f"\n7. Array Birleştirme ve Ayırma")
print("-" * 30)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

print(f"Array 1:\n{arr1}")
print(f"Array 2:\n{arr2}")

# Concatenate
h_concat = np.concatenate([arr1, arr2], axis=1)  # Yatay
v_concat = np.concatenate([arr1, arr2], axis=0)  # Dikey

print(f"\nYatay birleştirme:\n{h_concat}")
print(f"Dikey birleştirme:\n{v_concat}")

# Stack
stacked = np.stack([arr1, arr2], axis=0)
print(f"\nStack edilmiş (3D):\n{stacked}")

# Split
big_array = np.arange(12).reshape(3, 4)
print(f"\nBüyük array:\n{big_array}")

split_arrays = np.split(big_array, 3, axis=0)  # 3 parçaya böl
print(f"Bölünmüş arrays: {len(split_arrays)} parça")
for i, sub_arr in enumerate(split_arrays):
    print(f"Parça {i+1}: {sub_arr}")

# =============================================================================
# 8. PERFORMANS ÖRNEĞİ
# =============================================================================

print(f"\n8. Performans Karşılaştırması")
print("-" * 30)

import time

# Python list vs NumPy array performance
size = 1000000

# Python list ile işlem
start_time = time.time()
python_list = list(range(size))
python_result = [x * 2 for x in python_list]
python_time = time.time() - start_time

# NumPy array ile işlem
start_time = time.time()
numpy_array = np.arange(size)
numpy_result = numpy_array * 2
numpy_time = time.time() - start_time

print(f"Python list süresi: {python_time:.4f} saniye")
print(f"NumPy array süresi: {numpy_time:.4f} saniye")
print(f"NumPy {python_time/numpy_time:.1f}x daha hızlı!")

# =============================================================================
# 9. PRATİK UYGULAMA
# =============================================================================

print(f"\n9. Pratik Uygulama - Sinyal İşleme")
print("-" * 30)

# Sinüs dalgası oluşturma
t = np.linspace(0, 2*np.pi, 100)
frequency1 = 1
frequency2 = 3
signal1 = np.sin(frequency1 * t)
signal2 = 0.5 * np.sin(frequency2 * t)
combined_signal = signal1 + signal2

# Gürültü ekleme
noise = np.random.normal(0, 0.1, len(t))
noisy_signal = combined_signal + noise

print(f"Temiz sinyal ortalaması: {np.mean(combined_signal):.3f}")
print(f"Gürültülü sinyal ortalaması: {np.mean(noisy_signal):.3f}")
print(f"Sinyal-gürültü oranı: {np.std(combined_signal)/np.std(noise):.2f}")

# Basit filtreleme (moving average)
window_size = 5
filtered_signal = np.convolve(noisy_signal, np.ones(window_size)/window_size, mode='same')

print(f"Filtrelenmiş sinyal ortalaması: {np.mean(filtered_signal):.3f}")

# Görselleştirme
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(t, signal1, label='Sinyal 1')
plt.plot(t, signal2, label='Sinyal 2')
plt.title('Orijinal Sinyaller')
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(t, combined_signal)
plt.title('Birleştirilmiş Sinyal')
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(t, noisy_signal, alpha=0.7, label='Gürültülü')
plt.title('Gürültü Eklenmiş Sinyal')
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 4)
plt.plot(t, noisy_signal, alpha=0.5, label='Gürültülü')
plt.plot(t, filtered_signal, 'r-', linewidth=2, label='Filtrelenmiş')
plt.title('Filtrelenmiş Sinyal')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

print("\n🎯 NumPy Array İşlemleri Özeti:")
print("✅ Array oluşturma ve özellikleri")
print("✅ İndeksleme ve dilimleme")
print("✅ Matematiksel işlemler")
print("✅ İstatistiksel fonksiyonlar") 
print("✅ Şekil değiştirme işlemleri")
print("✅ Array birleştirme ve ayırma")
print("✅ Performans avantajları")
print("✅ Pratik sinyal işleme uygulaması")