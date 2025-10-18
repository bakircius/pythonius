"""
Seaborn ile İleri Görselleştirme
Bu dosyada Seaborn kütüphanesi ile statistiksel grafikleri ve ileri görselleştirme tekniklerini öğreniyoruz.
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

print("=== Seaborn İleri Grafikler ===\n")

# Seaborn ayarları
sns.set_style("whitegrid")
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (12, 8)

# =============================================================================
# 1. VERİ SETİ HAZIRLAMA
# =============================================================================

print("1. Veri Seti Hazırlama")
print("-" * 30)

# Örnek veri setleri oluşturma
np.random.seed(42)

# İris benzeri veri seti
n_samples = 500
iris_data = pd.DataFrame({
    'petal_length': np.concatenate([
        np.random.normal(1.5, 0.3, n_samples//3),
        np.random.normal(4.0, 0.5, n_samples//3),
        np.random.normal(5.5, 0.7, n_samples//3 + n_samples%3)
    ]),
    'petal_width': np.concatenate([
        np.random.normal(0.3, 0.1, n_samples//3),
        np.random.normal(1.3, 0.3, n_samples//3),
        np.random.normal(2.0, 0.4, n_samples//3 + n_samples%3)
    ]),
    'sepal_length': np.concatenate([
        np.random.normal(5.0, 0.4, n_samples//3),
        np.random.normal(6.5, 0.5, n_samples//3),
        np.random.normal(7.2, 0.6, n_samples//3 + n_samples%3)
    ]),
    'species': ['setosa']*167 + ['versicolor']*167 + ['virginica']*166
})

# Satış veri seti
sales_data = pd.DataFrame({
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] * 3,
    'year': [2022]*12 + [2023]*12 + [2024]*12,
    'sales': np.random.uniform(10000, 50000, 36) + np.sin(np.arange(36)/6*np.pi)*5000,
    'region': ['North', 'South', 'East', 'West'] * 9,
    'product': ['A', 'B', 'C'] * 12
})

print(f"İris veri seti: {iris_data.shape}")
print(iris_data.head())

print(f"\nSatış veri seti: {sales_data.shape}")
print(sales_data.head())

# =============================================================================
# 2. DAĞILIM GRAFİKLERİ
# =============================================================================

print("\n2. Dağılım Grafikleri")
print("-" * 30)

fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Histogram ile KDE
sns.histplot(data=iris_data, x='petal_length', hue='species', kde=True, ax=axes[0,0])
axes[0,0].set_title('Histogram + KDE')

# Sadece KDE
sns.kdeplot(data=iris_data, x='petal_length', hue='species', ax=axes[0,1])
axes[0,1].set_title('Kernel Density Estimation')

# Distplot alternatifleri
for i, species in enumerate(iris_data['species'].unique()):
    subset = iris_data[iris_data['species'] == species]
    axes[1,0].hist(subset['petal_length'], alpha=0.7, label=species, bins=20)
axes[1,0].set_title('Çoklu Histogram')
axes[1,0].legend()

# Violin plot
sns.violinplot(data=iris_data, x='species', y='petal_length', ax=axes[1,1])
axes[1,1].set_title('Violin Plot')

plt.tight_layout()
plt.show()

# =============================================================================
# 3. İLİŞKİ GRAFİKLERİ
# =============================================================================

print("\n3. İlişki Grafikleri")
print("-" * 30)

# Scatter plot with regression
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
sns.scatterplot(data=iris_data, x='petal_length', y='petal_width', hue='species', s=100)
plt.title('Scatter Plot with Categories')

plt.subplot(1, 3, 2)
sns.regplot(data=iris_data, x='petal_length', y='petal_width', scatter_kws={'alpha':0.6})
plt.title('Regression Plot')

plt.subplot(1, 3, 3)
sns.residplot(data=iris_data, x='petal_length', y='petal_width')
plt.title('Residual Plot')

plt.tight_layout()
plt.show()

# Pairplot - Çok değişkenli ilişkiler
pairplot = sns.pairplot(iris_data, hue='species', diag_kind='kde', markers=['o', 's', 'D'])
pairplot.fig.suptitle('Pairplot - Tüm Değişken Çiftleri', y=1.02)
plt.show()

# =============================================================================
# 4. KATEGORİK VERİ GRAFİKLERİ
# =============================================================================

print("\n4. Kategorik Veri Grafikleri")
print("-" * 30)

fig, axes = plt.subplots(2, 3, figsize=(18, 12))

# Count plot
sns.countplot(data=sales_data, x='region', ax=axes[0,0])
axes[0,0].set_title('Count Plot')

# Bar plot
sns.barplot(data=sales_data, x='region', y='sales', ax=axes[0,1])
axes[0,1].set_title('Bar Plot (Ortalama)')

# Box plot
sns.boxplot(data=sales_data, x='region', y='sales', ax=axes[0,2])
axes[0,2].set_title('Box Plot')

# Violin plot
sns.violinplot(data=sales_data, x='region', y='sales', ax=axes[1,0])
axes[1,0].set_title('Violin Plot')

# Swarm plot
sns.swarmplot(data=iris_data, x='species', y='petal_length', ax=axes[1,1])
axes[1,1].set_title('Swarm Plot')

# Strip plot
sns.stripplot(data=iris_data, x='species', y='petal_length', jitter=True, ax=axes[1,2])
axes[1,2].set_title('Strip Plot')

plt.tight_layout()
plt.show()

# =============================================================================
# 5. KORELASYON VE ISITMA HARİTALARI
# =============================================================================

print("\n5. Korelasyon ve Isıtma Haritaları")
print("-" * 30)

# Korelasyon matrisi
numeric_iris = iris_data.select_dtypes(include=[np.number])
correlation_matrix = numeric_iris.corr()

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Basit heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, ax=axes[0])
axes[0].set_title('Korelasyon Matrisi')

# Clustermap
sns.clustermap(correlation_matrix, annot=True, cmap='viridis', figsize=(8, 6))
plt.title('Cluster Heatmap')

# Pivot table heatmap
pivot_sales = sales_data.pivot_table(values='sales', index='region', columns='product', aggfunc='mean')
sns.heatmap(pivot_sales, annot=True, fmt='.0f', cmap='YlOrRd', ax=axes[1])
axes[1].set_title('Pivot Table Heatmap')

# Mask ile üçgen heatmap
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
sns.heatmap(correlation_matrix, mask=mask, annot=True, cmap='RdYlBu_r', center=0, ax=axes[2])
axes[2].set_title('Üçgen Korelasyon Matrisi')

plt.tight_layout()
plt.show()

# =============================================================================
# 6. ZAMAN SERİSİ GÖRSELLEŞTİRME
# =============================================================================

print("\n6. Zaman Serisi Görselleştirme")
print("-" * 30)

# Zaman serisi verisi oluştur
dates = pd.date_range('2022-01-01', periods=365, freq='D')
ts_data = pd.DataFrame({
    'date': dates,
    'value': 100 + np.cumsum(np.random.randn(365) * 0.5) + 10 * np.sin(2 * np.pi * np.arange(365) / 365),
    'category': np.random.choice(['A', 'B', 'C'], 365)
})

fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Line plot
sns.lineplot(data=ts_data, x='date', y='value', ax=axes[0,0])
axes[0,0].set_title('Zaman Serisi Line Plot')
axes[0,0].tick_params(axis='x', rotation=45)

# Kategorili line plot
monthly_data = ts_data.groupby([ts_data['date'].dt.month, 'category'])['value'].mean().reset_index()
monthly_data.columns = ['month', 'category', 'value']
sns.lineplot(data=monthly_data, x='month', y='value', hue='category', ax=axes[0,1])
axes[0,1].set_title('Kategorili Aylık Trend')

# Area plot benzeri
ts_pivot = ts_data.pivot_table(values='value', index=ts_data['date'].dt.month, 
                              columns='category', aggfunc='mean').fillna(0)
axes[1,0].stackplot(ts_pivot.index, ts_pivot['A'], ts_pivot['B'], ts_pivot['C'], 
                   labels=['A', 'B', 'C'], alpha=0.7)
axes[1,0].set_title('Stacked Area Plot')
axes[1,0].legend(loc='upper left')
axes[1,0].set_xlabel('Ay')

# Rolling mean
ts_data['rolling_mean'] = ts_data['value'].rolling(window=30).mean()
sns.lineplot(data=ts_data, x='date', y='value', alpha=0.3, ax=axes[1,1])
sns.lineplot(data=ts_data, x='date', y='rolling_mean', color='red', ax=axes[1,1])
axes[1,1].set_title('30 Günlük Hareketli Ortalama')
axes[1,1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()

# =============================================================================
# 7. İSTATİSTİKSEL GRAFİKLER
# =============================================================================

print("\n7. İstatistiksel Grafikler")
print("-" * 30)

fig, axes = plt.subplots(2, 3, figsize=(18, 12))

# Q-Q Plot
from scipy import stats
sample_data = np.random.normal(0, 1, 100)
stats.probplot(sample_data, dist="norm", plot=axes[0,0])
axes[0,0].set_title('Q-Q Plot (Normal Distribution)')

# Box plot with statistical annotations
sns.boxplot(data=iris_data, x='species', y='petal_length', ax=axes[0,1])
axes[0,1].set_title('Box Plot with Outliers')

# Violin plot with inner quartiles
sns.violinplot(data=iris_data, x='species', y='petal_length', inner='quartile', ax=axes[0,2])
axes[0,2].set_title('Violin Plot with Quartiles')

# Bootstrap confidence intervals
sns.barplot(data=sales_data, x='region', y='sales', ci=95, ax=axes[1,0])
axes[1,0].set_title('Bar Plot with 95% CI')

# Regression with confidence bands
sns.regplot(data=iris_data, x='petal_length', y='sepal_length', ax=axes[1,1])
axes[1,1].set_title('Regression with Confidence Band')

# Residual plot
sns.residplot(data=iris_data, x='petal_length', y='sepal_length', ax=axes[1,2])
axes[1,2].set_title('Residual Plot')

plt.tight_layout()
plt.show()

# =============================================================================
# 8. ÇOK BOYUTLU VERİ GÖRSELLEŞTİRME
# =============================================================================

print("\n8. Çok Boyutlu Veri Görselleştirme")
print("-" * 30)

# FacetGrid ile çoklu grafikler
g = sns.FacetGrid(iris_data, col='species', margin_titles=True, height=4)
g.map(plt.hist, 'petal_length', alpha=0.7, bins=15)
g.fig.suptitle('Tür Bazında Petal Length Dağılımı', y=1.02)
plt.show()

# PairGrid ile özelleştirilmiş pairplot
g = sns.PairGrid(iris_data, hue='species')
g.map_diag(sns.histplot)
g.map_upper(sns.scatterplot)
g.map_lower(sns.kdeplot)
g.add_legend()
plt.show()

# Relplot ile ilişki keşfi
sns.relplot(data=sales_data, x='sales', y='sales', col='region', 
           hue='product', kind='scatter', col_wrap=2, height=4)
plt.show()

# =============================================================================
# 9. GELİŞMİŞ STİL VE TEMA AYARLARI
# =============================================================================

print("\n9. Gelişmiş Stil ve Tema Ayarları")
print("-" * 30)

# Farklı temalar
themes = ['whitegrid', 'darkgrid', 'white', 'dark', 'ticks']
fig, axes = plt.subplots(1, len(themes), figsize=(20, 4))

for i, theme in enumerate(themes):
    sns.set_style(theme)
    sns.boxplot(data=iris_data, x='species', y='petal_length', ax=axes[i])
    axes[i].set_title(f'Style: {theme}')

plt.tight_layout()
plt.show()

# Renk paletleri
plt.figure(figsize=(15, 10))

palettes = ['husl', 'viridis', 'rocket', 'mako', 'Set2', 'tab10']
for i, palette in enumerate(palettes):
    plt.subplot(2, 3, i+1)
    sns.barplot(data=sales_data.groupby('region')['sales'].mean().reset_index(), 
               x='region', y='sales', palette=palette)
    plt.title(f'Palette: {palette}')

plt.tight_layout()
plt.show()

# =============================================================================
# 10. İNTERAKTİF VE ANİMASYONLU GRAFİKLER (Seaborn + Matplotlib)
# =============================================================================

print("\n10. Gelişmiş Görselleştirme Teknikleri")
print("-" * 30)

# Subplot'lar ile karmaşık düzenlemeler
fig = plt.figure(figsize=(20, 15))

# Ana scatter plot
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=2, rowspan=2)
scatter = ax1.scatter(iris_data['petal_length'], iris_data['petal_width'], 
                     c=pd.Categorical(iris_data['species']).codes, 
                     s=100, alpha=0.6, cmap='viridis')
ax1.set_xlabel('Petal Length')
ax1.set_ylabel('Petal Width')
ax1.set_title('Ana Scatter Plot')

# Üst histogram
ax2 = plt.subplot2grid((3, 3), (0, 2))
for species in iris_data['species'].unique():
    subset = iris_data[iris_data['species'] == species]
    ax2.hist(subset['petal_width'], alpha=0.7, label=species, orientation='horizontal')
ax2.set_ylabel('Petal Width')
ax2.set_title('Width Dist.')

# Sağ histogram
ax3 = plt.subplot2grid((3, 3), (1, 2))
for species in iris_data['species'].unique():
    subset = iris_data[iris_data['species'] == species]
    ax3.hist(subset['petal_length'], alpha=0.7, label=species)
ax3.set_xlabel('Petal Length')
ax3.set_title('Length Dist.')

# Alt istatistikler
ax4 = plt.subplot2grid((3, 3), (2, 0), colspan=3)
stats_data = iris_data.groupby('species').agg({
    'petal_length': ['mean', 'std'],
    'petal_width': ['mean', 'std']
}).round(2)
stats_text = stats_data.to_string()
ax4.text(0.1, 0.5, stats_text, fontsize=10, fontfamily='monospace')
ax4.set_xlim(0, 1)
ax4.set_ylim(0, 1)
ax4.axis('off')
ax4.set_title('İstatistiksel Özetler')

plt.tight_layout()
plt.show()

# =============================================================================
# 11. ÖZEL GRAFİK TÜRLERİ
# =============================================================================

print("\n11. Özel Grafik Türleri")
print("-" * 30)

fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Joint plot benzeri manuel oluşturma
ax_main = axes[0,0]
sns.scatterplot(data=iris_data, x='petal_length', y='petal_width', 
               hue='species', ax=ax_main)
ax_main.set_title('Joint Distribution')

# Radar chart (örnek)
categories = ['Feature 1', 'Feature 2', 'Feature 3', 'Feature 4']
values = [4, 3, 5, 2, 4]  # İlk değeri sona da ekle (kapalı şekil için)
angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]  # Kapalı şekil için

ax_radar = plt.subplot(2, 2, 2, projection='polar')
ax_radar.plot(angles, values, 'o-', linewidth=2)
ax_radar.fill(angles, values, alpha=0.25)
ax_radar.set_xticks(angles[:-1])
ax_radar.set_xticklabels(categories)
ax_radar.set_title('Radar Chart')

# Sunburst benzeri (basitleştirilmiş)
sizes = [30, 25, 20, 15, 10]
colors = plt.cm.Set3(np.linspace(0, 1, len(sizes)))
axes[1,0].pie(sizes, colors=colors, autopct='%1.1f%%', startangle=90)
axes[1,0].set_title('Pie Chart')

# Waterfall chart benzeri
values = [100, -20, +30, -10, +15, -5]
cumulative = np.cumsum([0] + values[:-1])
bars = axes[1,1].bar(range(len(values)), values, bottom=cumulative)
axes[1,1].set_title('Waterfall-style Chart')
axes[1,1].set_xticks(range(len(values)))
axes[1,1].set_xticklabels(['Start', 'Change 1', 'Change 2', 'Change 3', 'Change 4', 'End'])

plt.tight_layout()
plt.show()

# =============================================================================
# 12. PERFORMANS VE OPTİMİZASYON
# =============================================================================

print("\n12. Büyük Veri Setleri için Optimizasyon")
print("-" * 30)

# Büyük veri seti simülasyonu
large_data = pd.DataFrame({
    'x': np.random.randn(50000),
    'y': np.random.randn(50000),
    'category': np.random.choice(['A', 'B', 'C', 'D'], 50000)
})

print(f"Büyük veri seti boyutu: {large_data.shape}")

# Hexbin plot (büyük veri için ideal)
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.hexbin(large_data['x'], large_data['y'], gridsize=50, cmap='Blues')
plt.colorbar(label='Count')
plt.title('Hexbin Plot (50K points)')

# Sampling ile scatter
plt.subplot(1, 3, 2)
sample_data = large_data.sample(1000)
sns.scatterplot(data=sample_data, x='x', y='y', hue='category', alpha=0.7)
plt.title('Sampled Scatter Plot (1K points)')

# Density plot
plt.subplot(1, 3, 3)
sns.kdeplot(data=large_data, x='x', y='y', cmap='viridis', fill=True)
plt.title('2D Density Plot')

plt.tight_layout()
plt.show()

print("\n🎯 Seaborn İleri Grafikler Özeti:")
print("✅ Dağılım grafikleri (histogram, KDE, violin)")
print("✅ İlişki grafikleri (scatter, regression, pairplot)")
print("✅ Kategorik veri grafikleri (box, bar, swarm)")
print("✅ Korelasyon ve ısıtma haritaları")
print("✅ Zaman serisi görselleştirme")
print("✅ İstatistiksel grafikler (Q-Q, residual)")
print("✅ Çok boyutlu veri (FacetGrid, PairGrid)")
print("✅ Gelişmiş stil ve tema ayarları")
print("✅ Karmaşık düzenlemeler (subplot2grid)")
print("✅ Özel grafik türleri (radar, waterfall)")
print("✅ Büyük veri optimizasyonu (hexbin, sampling)")
print("✅ Performans ve görsel kalite dengeleme")