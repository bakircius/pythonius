"""
Matplotlib ile Temel Görselleştirme
Bu dosyada Matplotlib kütüphanesi ile çeşitli grafik türlerini öğreniyoruz.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

print("=== Matplotlib Temel Grafikler ===\n")

# Matplotlib ayarları
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10
plt.style.use('seaborn-v0_8')  # Güzel görünüm için

# =============================================================================
# 1. TEMEL ÇİZGİ GRAFİĞİ
# =============================================================================

print("1. Temel Çizgi Grafiği")
print("-" * 30)

# Örnek veri
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='sin(x)', color='blue', linewidth=2)
plt.plot(x, y2, label='cos(x)', color='red', linestyle='--', linewidth=2)

plt.title('Sinüs ve Kosinüs Fonksiyonları', fontsize=16, fontweight='bold')
plt.xlabel('x değerleri', fontsize=12)
plt.ylabel('y değerleri', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# =============================================================================
# 2. NOKTA GRAFİĞİ (SCATTER PLOT)
# =============================================================================

print("2. Nokta Grafiği (Scatter Plot)")
print("-" * 30)

# Rastgele veri oluşturma
np.random.seed(42)
n = 100
x = np.random.randn(n)
y = 2 * x + np.random.randn(n) * 0.5
colors = np.random.rand(n)
sizes = 1000 * np.random.rand(n)

plt.figure(figsize=(10, 6))
scatter = plt.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap='viridis')
plt.colorbar(scatter, label='Renk Değeri')

plt.title('Scatter Plot Örneği', fontsize=16)
plt.xlabel('X Değerleri', fontsize=12)
plt.ylabel('Y Değerleri', fontsize=12)
plt.grid(True, alpha=0.3)

# Trend çizgisi ekleme
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x, p(x), "r--", alpha=0.8, linewidth=2, label='Trend Çizgisi')
plt.legend()
plt.show()

# =============================================================================
# 3. BAR GRAFİĞİ
# =============================================================================

print("3. Bar Grafiği")
print("-" * 30)

# Kategori verileri
kategoriler = ['Python', 'Java', 'JavaScript', 'C++', 'C#', 'PHP']
populerite = [85, 65, 75, 45, 55, 40]
renkler = ['#3776ab', '#f89820', '#f7df1e', '#00599c', '#239120', '#777bb4']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Dikey bar grafiği
bars1 = ax1.bar(kategoriler, populerite, color=renkler, alpha=0.7, edgecolor='black')
ax1.set_title('Programlama Dilleri Popülerlik (Dikey)', fontsize=14)
ax1.set_ylabel('Popülerite Skoru', fontsize=12)
ax1.set_ylim(0, 100)

# Değerleri çubukların üzerine yaz
for bar, value in zip(bars1, populerite):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
             str(value), ha='center', va='bottom', fontweight='bold')

# Yatay bar grafiği
bars2 = ax2.barh(kategoriler, populerite, color=renkler, alpha=0.7, edgecolor='black')
ax2.set_title('Programlama Dilleri Popülerlik (Yatay)', fontsize=14)
ax2.set_xlabel('Popülerite Skoru', fontsize=12)
ax2.set_xlim(0, 100)

# Değerleri çubukların yanına yaz
for bar, value in zip(bars2, populerite):
    ax2.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
             str(value), ha='left', va='center', fontweight='bold')

plt.tight_layout()
plt.show()

# =============================================================================
# 4. HİSTOGRAM
# =============================================================================

print("4. Histogram")
print("-" * 30)

# Normal dağılım verisi
np.random.seed(42)
data1 = np.random.normal(100, 15, 1000)  # ortalama=100, std=15
data2 = np.random.normal(120, 20, 1000)  # ortalama=120, std=20

plt.figure(figsize=(12, 6))

# Alt grafikler
plt.subplot(1, 2, 1)
plt.hist(data1, bins=30, alpha=0.7, color='skyblue', edgecolor='black', density=True)
plt.title('Normal Dağılım 1 (μ=100, σ=15)', fontsize=12)
plt.xlabel('Değerler')
plt.ylabel('Yoğunluk')
plt.axvline(data1.mean(), color='red', linestyle='--', linewidth=2, label=f'Ortalama: {data1.mean():.1f}')
plt.legend()

plt.subplot(1, 2, 2)
plt.hist([data1, data2], bins=30, alpha=0.7, label=['Dağılım 1', 'Dağılım 2'], 
         color=['skyblue', 'lightcoral'], edgecolor='black')
plt.title('İki Dağılımın Karşılaştırması', fontsize=12)
plt.xlabel('Değerler')
plt.ylabel('Frekans')
plt.legend()

plt.tight_layout()
plt.show()

# =============================================================================
# 5. PİE CHART (DAİRE GRAFİĞİ)
# =============================================================================

print("5. Pie Chart (Daire Grafiği)")
print("-" * 30)

# Pie chart verileri
labels = ['Desktop', 'Mobile', 'Tablet', 'TV', 'Diğer']
sizes = [45, 30, 15, 7, 3]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']
explode = (0.1, 0, 0, 0, 0)  # İlk dilimi ayır

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Basit pie chart
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
        startangle=90, explode=explode)
ax1.set_title('Cihaz Kullanım Dağılımı', fontsize=14)

# Donut chart
wedges, texts, autotexts = ax2.pie(sizes, labels=labels, colors=colors, 
                                  autopct='%1.1f%%', startangle=90,
                                  pctdistance=0.85)
# Ortasına çember çiz (donut effect)
centre_circle = plt.Circle((0,0), 0.70, fc='white')
ax2.add_artist(centre_circle)
ax2.set_title('Donut Chart', fontsize=14)

plt.tight_layout()
plt.show()

# =============================================================================
# 6. KUTU GRAFİĞİ (BOX PLOT)
# =============================================================================

print("6. Kutu Grafiği (Box Plot)")
print("-" * 30)

# Farklı dağılımlara sahip veriler
np.random.seed(42)
normal_data = np.random.normal(50, 10, 200)
skewed_data = np.random.gamma(2, 10, 200)
uniform_data = np.random.uniform(20, 80, 200)

data_sets = [normal_data, skewed_data, uniform_data]
labels = ['Normal', 'Çarpık', 'Düzgün']

plt.figure(figsize=(10, 6))
box_plot = plt.boxplot(data_sets, labels=labels, patch_artist=True,
                      boxprops=dict(facecolor='lightblue', alpha=0.7),
                      medianprops=dict(color='red', linewidth=2))

plt.title('Farklı Dağılımların Box Plot Karşılaştırması', fontsize=14)
plt.ylabel('Değerler', fontsize=12)
plt.grid(True, alpha=0.3)

# İstatistikleri yazdır
for i, data in enumerate(data_sets):
    print(f"{labels[i]} dağılım istatistikleri:")
    print(f"  Ortalama: {np.mean(data):.2f}")
    print(f"  Medyan: {np.median(data):.2f}")
    print(f"  Std: {np.std(data):.2f}")
    print()

plt.show()

# =============================================================================
# 7. ZAMAN SERİSİ GRAFİĞİ
# =============================================================================

print("7. Zaman Serisi Grafiği")
print("-" * 30)

# Tarih aralığı oluştur
start_date = datetime(2023, 1, 1)
dates = [start_date + timedelta(days=x) for x in range(365)]

# Trend + mevsimsel + gürültü
trend = np.linspace(100, 150, 365)
seasonal = 20 * np.sin(2 * np.pi * np.arange(365) / 365.25 * 4)  # 4 mevsim
noise = np.random.normal(0, 5, 365)
sales = trend + seasonal + noise

# DataFrame oluştur
df_time = pd.DataFrame({
    'Date': dates,
    'Sales': sales
})

# Hareketli ortalamalar
df_time['MA_7'] = df_time['Sales'].rolling(window=7).mean()
df_time['MA_30'] = df_time['Sales'].rolling(window=30).mean()

plt.figure(figsize=(15, 8))
plt.plot(df_time['Date'], df_time['Sales'], alpha=0.3, color='gray', label='Günlük Satış')
plt.plot(df_time['Date'], df_time['MA_7'], color='blue', linewidth=2, label='7 Günlük Ortalama')
plt.plot(df_time['Date'], df_time['MA_30'], color='red', linewidth=2, label='30 Günlük Ortalama')

plt.title('Satış Zaman Serisi Analizi', fontsize=16)
plt.xlabel('Tarih', fontsize=12)
plt.ylabel('Satış Miktarı', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# =============================================================================
# 8. ALT GRAFİKLER (SUBPLOTS)
# =============================================================================

print("8. Alt Grafikler (Subplots)")
print("-" * 30)

# 2x2 alt grafik düzeni
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# 1. Alt grafik - Sinüs dalgası
x = np.linspace(0, 4*np.pi, 100)
axes[0, 0].plot(x, np.sin(x), 'b-', linewidth=2)
axes[0, 0].set_title('Sinüs Dalgası')
axes[0, 0].grid(True)

# 2. Alt grafik - Random scatter
x_rand = np.random.randn(50)
y_rand = np.random.randn(50)
axes[0, 1].scatter(x_rand, y_rand, alpha=0.6)
axes[0, 1].set_title('Random Scatter Plot')
axes[0, 1].grid(True)

# 3. Alt grafik - Bar chart
categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 78]
axes[1, 0].bar(categories, values, color=['red', 'green', 'blue', 'orange'])
axes[1, 0].set_title('Kategori Değerleri')

# 4. Alt grafik - Histogram
data_hist = np.random.normal(0, 1, 1000)
axes[1, 1].hist(data_hist, bins=30, alpha=0.7, color='purple')
axes[1, 1].set_title('Normal Dağılım Histogramı')

plt.tight_layout()
plt.show()

# =============================================================================
# 9. 3D GRAFİKLER
# =============================================================================

print("9. 3D Grafikler")
print("-" * 30)

from mpl_toolkits.mplot3d import Axes3D

# 3D Surface plot
fig = plt.figure(figsize=(15, 5))

# 3D Scatter plot
ax1 = fig.add_subplot(131, projection='3d')
n = 100
x3d = np.random.randn(n)
y3d = np.random.randn(n)
z3d = x3d**2 + y3d**2
ax1.scatter(x3d, y3d, z3d, c=z3d, cmap='viridis')
ax1.set_title('3D Scatter Plot')

# 3D Surface plot
ax2 = fig.add_subplot(132, projection='3d')
x_surf = np.linspace(-5, 5, 50)
y_surf = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x_surf, y_surf)
Z = np.sin(np.sqrt(X**2 + Y**2))
ax2.plot_surface(X, Y, Z, cmap='coolwarm', alpha=0.8)
ax2.set_title('3D Surface Plot')

# 3D Wireframe
ax3 = fig.add_subplot(133, projection='3d')
ax3.plot_wireframe(X, Y, Z, alpha=0.6)
ax3.set_title('3D Wireframe')

plt.tight_layout()
plt.show()

# =============================================================================
# 10. GRAFİK ÖZELLEŞTİRME
# =============================================================================

print("10. Grafik Özelleştirme")
print("-" * 30)

# Gelişmiş özelleştirme örneği
fig, ax = plt.subplots(figsize=(12, 8))

# Veri
x = np.linspace(0, 10, 100)
y1 = np.exp(-x/3) * np.cos(2*np.pi*x)
y2 = np.exp(-x/5)

# Grafikler
line1 = ax.plot(x, y1, 'b-', linewidth=3, label='Sönümlü Sinüs')
line2 = ax.plot(x, y2, 'r--', linewidth=2, label='Üstel Azalma')
ax.fill_between(x, 0, y2, alpha=0.3, color='red', label='Alan')

# Özelleştirmeler
ax.set_title('Gelişmiş Grafik Özelleştirme Örneği', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Zaman (s)', fontsize=14, fontweight='bold')
ax.set_ylabel('Genlik', fontsize=14, fontweight='bold')

# Grid özelleştirme
ax.grid(True, linestyle=':', alpha=0.7)
ax.set_facecolor('#f8f8f8')

# Legend özelleştirme
ax.legend(loc='upper right', frameon=True, shadow=True, borderpad=1)

# Eksen sınırları
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)

# Anotasyon ekleme
max_idx = np.argmax(y1)
ax.annotate(f'Maksimum: ({x[max_idx]:.2f}, {y1[max_idx]:.2f})',
           xy=(x[max_idx], y1[max_idx]), xytext=(x[max_idx]+2, y1[max_idx]+0.3),
           arrowprops=dict(arrowstyle='->', color='black'),
           fontsize=12, bbox=dict(boxstyle="round,pad=0.3", facecolor='yellow', alpha=0.7))

# Spines (çerçeve) özelleştirme
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)

plt.tight_layout()
plt.show()

# =============================================================================
# 11. RENK PALETLERİ VE STİLLER
# =============================================================================

print("11. Renk Paletleri ve Stiller")
print("-" * 30)

# Farklı stiller
styles = ['default', 'classic', 'seaborn-v0_8-darkgrid', 'ggplot']
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
axes = axes.ravel()

x = np.linspace(0, 10, 100)

for i, style in enumerate(styles):
    plt.style.use(style)
    
    axes[i].plot(x, np.sin(x), label='sin(x)')
    axes[i].plot(x, np.cos(x), label='cos(x)')
    axes[i].set_title(f'Style: {style}')
    axes[i].legend()
    axes[i].grid(True)

plt.tight_layout()
plt.show()

# Stil sıfırlama
plt.style.use('default')

# =============================================================================
# 12. İNTERAKTİF ÖZELLİKLER
# =============================================================================

print("12. Grafik Kaydetme")
print("-" * 30)

# Örnek grafik oluştur ve kaydet
plt.figure(figsize=(10, 6))
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x), 'b-', linewidth=2, label='sin(x)')
plt.plot(x, np.cos(x), 'r--', linewidth=2, label='cos(x)')
plt.title('Trigonometrik Fonksiyonlar')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

# Farklı formatlarda kaydetme
plt.savefig('trigonometric_functions.png', dpi=300, bbox_inches='tight')
plt.savefig('trigonometric_functions.pdf', bbox_inches='tight')
print("Grafik 'trigonometric_functions.png' ve 'trigonometric_functions.pdf' olarak kaydedildi")

plt.show()

print("\n🎯 Matplotlib Temel Grafikler Özeti:")
print("✅ Çizgi grafikleri (Line plots)")
print("✅ Nokta grafikleri (Scatter plots)")
print("✅ Bar grafikleri (dikey/yatay)")
print("✅ Histogramlar")
print("✅ Pie chartlar (daire grafikleri)")
print("✅ Box plotlar (kutu grafikleri)")
print("✅ Zaman serisi grafikleri")
print("✅ Alt grafikler (subplots)")
print("✅ 3D grafikler")
print("✅ Grafik özelleştirme")
print("✅ Stil ve renk paletleri")
print("✅ Grafik kaydetme")