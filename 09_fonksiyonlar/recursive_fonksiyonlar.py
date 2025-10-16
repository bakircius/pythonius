# Recursive Fonksiyonlar (Özyineleme)
# Python'da recursive fonksiyonların detaylı incelenmesi

print("=== RECURSİVE FONKSİYONLAR (ÖZYİNELEME) ===\n")

print("1. RECURSİON KAVRAMI:")
print("-" * 23)

# En basit recursive fonksiyon
def say_geri(n):
    """n'den geriye doğru saymak"""
    if n <= 0:  # Base case (temel durum)
        print("Bitti!")
        return
    
    print(n)
    say_geri(n - 1)  # Recursive call (özyineli çağrı)

print("Geri sayma örneği:")
say_geri(5)

# Recursive fonksiyonun anatomy'si
def recursive_template(n):
    """Recursive fonksiyon şablonu"""
    # Base case - recursion'ı durduran koşul
    if n <= 0:
        return "base_value"
    
    # Recursive case - fonksiyonun kendini çağırması
    return "some_operation" + recursive_template(n - 1)

print("\nRecursive fonksiyon bileşenleri:")
print("1. Base case: Recursion'ı durduran koşul")
print("2. Recursive case: Fonksiyonun kendini çağırması")
print("3. Progress: Her çağrıda base case'e yaklaşma")

print("\n2. KLASİK RECURSİVE ÖRNEKLER:")
print("-" * 30)

# Faktöriyel hesaplama
def faktoriyel(n):
    """n! hesaplar"""
    # Base case
    if n <= 1:
        return 1
    
    # Recursive case
    return n * faktoriyel(n - 1)

print("Faktöriyel örnekleri:")
for i in range(6):
    print(f"{i}! = {faktoriyel(i)}")

# Fibonacci sayıları
def fibonacci(n):
    """n. Fibonacci sayısını bulur"""
    # Base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)

print("\nFibonacci sayıları:")
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")

# Üs alma (power)
def power(base, exponent):
    """base^exponent hesaplar"""
    # Base cases
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    
    # Recursive case
    return base * power(base, exponent - 1)

print(f"\nÜs alma örnekleri:")
print(f"2^5 = {power(2, 5)}")
print(f"3^4 = {power(3, 4)}")

# Sayıların toplamı
def sayi_toplami(n):
    """1'den n'e kadar sayıların toplamı"""
    if n <= 0:
        return 0
    return n + sayi_toplami(n - 1)

print(f"\n1'den 10'a kadar toplam: {sayi_toplami(10)}")

print("\n3. LİSTE İŞLEMLERİ İLE RECURSİON:")
print("-" * 33)

# Liste uzunluğu
def liste_uzunlugu(lst):
    """Liste uzunluğunu recursive olarak hesaplar"""
    if not lst:  # Boş liste
        return 0
    return 1 + liste_uzunlugu(lst[1:])  # İlk elemanı atla

test_liste = [1, 2, 3, 4, 5]
print(f"Liste: {test_liste}")
print(f"Uzunluk: {liste_uzunlugu(test_liste)}")

# Liste toplamı
def liste_toplami(lst):
    """Liste elemanlarının toplamı"""
    if not lst:
        return 0
    return lst[0] + liste_toplami(lst[1:])

print(f"Liste toplamı: {liste_toplami(test_liste)}")

# Liste maksimum
def liste_max(lst):
    """Liste'deki maksimum değer"""
    if len(lst) == 1:
        return lst[0]
    
    ilk = lst[0]
    geri_kalan_max = liste_max(lst[1:])
    
    return ilk if ilk > geri_kalan_max else geri_kalan_max

print(f"Liste maksimum: {liste_max(test_liste)}")

# Liste ters çevirme
def liste_ters(lst):
    """Liste'yi ters çevirir"""
    if len(lst) <= 1:
        return lst
    return [lst[-1]] + liste_ters(lst[:-1])

print(f"Ters liste: {liste_ters(test_liste)}")

# Eleman arama
def eleman_ara(lst, aranan):
    """Liste'de eleman arar"""
    if not lst:
        return False
    if lst[0] == aranan:
        return True
    return eleman_ara(lst[1:], aranan)

print(f"3 var mı: {eleman_ara(test_liste, 3)}")
print(f"7 var mı: {eleman_ara(test_liste, 7)}")

print("\n4. STRING İŞLEMLERİ İLE RECURSİON:")
print("-" * 34)

# String ters çevirme
def string_ters(s):
    """String'i ters çevirir"""
    if len(s) <= 1:
        return s
    return s[-1] + string_ters(s[:-1])

test_string = "Python"
print(f"String: {test_string}")
print(f"Ters: {string_ters(test_string)}")

# Palindrome kontrolü
def palindrome_mu(s):
    """String palindrome mu kontrol eder"""
    # Küçük harfe çevir ve boşlukları temizle
    s = s.lower().replace(" ", "")
    
    if len(s) <= 1:
        return True
    
    if s[0] != s[-1]:
        return False
    
    return palindrome_mu(s[1:-1])

test_kelimeler = ["radar", "python", "level", "a man a plan a canal panama"]
print(f"\nPalindrome kontrolleri:")
for kelime in test_kelimeler:
    print(f"'{kelime}': {palindrome_mu(kelime)}")

# Karakter sayma
def karakter_say(s, char):
    """String'de belirli karakteri sayar"""
    if not s:
        return 0
    
    count = 1 if s[0] == char else 0
    return count + karakter_say(s[1:], char)

print(f"\n'programming' içinde 'r' sayısı: {karakter_say('programming', 'r')}")

# String içinde substring arama
def substring_ara(ana_string, alt_string):
    """Ana string içinde alt string arar"""
    if len(alt_string) > len(ana_string):
        return False
    
    if ana_string.startswith(alt_string):
        return True
    
    if len(ana_string) == 0:
        return False
    
    return substring_ara(ana_string[1:], alt_string)

print(f"'python' içinde 'th' var mı: {substring_ara('python', 'th')}")

print("\n5. MATEMATIK İŞLEMLERİ:")
print("-" * 22)

# En büyük ortak bölen (GCD)
def gcd(a, b):
    """Euclid algoritması ile EBOB"""
    if b == 0:
        return a
    return gcd(b, a % b)

print(f"GCD(48, 18): {gcd(48, 18)}")
print(f"GCD(56, 42): {gcd(56, 42)}")

# Binary search
def binary_search(lst, target, left=0, right=None):
    """Sıralı listede binary search"""
    if right is None:
        right = len(lst) - 1
    
    if left > right:
        return -1  # Bulunamadı
    
    mid = (left + right) // 2
    
    if lst[mid] == target:
        return mid
    elif lst[mid] > target:
        return binary_search(lst, target, left, mid - 1)
    else:
        return binary_search(lst, target, mid + 1, right)

sirali_liste = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(f"Sıralı liste: {sirali_liste}")
print(f"7'nin indeksi: {binary_search(sirali_liste, 7)}")
print(f"12'nin indeksi: {binary_search(sirali_liste, 12)}")

# Sayının basamaklarının toplamı
def basamak_toplami(n):
    """Sayının basamaklarının toplamı"""
    if n < 10:
        return n
    return n % 10 + basamak_toplami(n // 10)

print(f"1234'ün basamak toplamı: {basamak_toplami(1234)}")

# Sayıyı binary'ye çevirme
def binary_cevirici(n):
    """Sayıyı binary'ye çevirir"""
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return binary_cevirici(n // 2) + str(n % 2)

print(f"10'un binary'si: {binary_cevirici(10)}")
print(f"25'in binary'si: {binary_cevirici(25)}")

print("\n6. AĞAÇ YAPILARI İLE RECURSİON:")
print("-" * 31)

# Basit binary tree
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Tree traversal (dolaşma)
def inorder_traversal(root):
    """In-order tree traversal"""
    if root is None:
        return []
    
    result = []
    result.extend(inorder_traversal(root.left))
    result.append(root.value)
    result.extend(inorder_traversal(root.right))
    
    return result

def preorder_traversal(root):
    """Pre-order tree traversal"""
    if root is None:
        return []
    
    result = [root.value]
    result.extend(preorder_traversal(root.left))
    result.extend(preorder_traversal(root.right))
    
    return result

# Tree oluşturma
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Tree traversal örnekleri:")
print(f"In-order: {inorder_traversal(root)}")
print(f"Pre-order: {preorder_traversal(root)}")

# Tree yüksekliği
def tree_height(root):
    """Tree'nin yüksekliğini hesaplar"""
    if root is None:
        return 0
    
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    
    return 1 + max(left_height, right_height)

print(f"Tree yüksekliği: {tree_height(root)}")

# Tree'de eleman arama
def tree_search(root, target):
    """Tree'de eleman arar"""
    if root is None:
        return False
    
    if root.value == target:
        return True
    
    return tree_search(root.left, target) or tree_search(root.right, target)

print(f"Tree'de 5 var mı: {tree_search(root, 5)}")
print(f"Tree'de 7 var mı: {tree_search(root, 7)}")

print("\n7. RECURSİON PROBLEMLERİ VE ÇÖZÜMLERİ:")
print("-" * 39)

# Stack overflow problemi
def sonsuz_recursion(n):
    """Tehlikeli - sonsuz recursion!"""
    # return sonsuz_recursion(n)  # YAPMAYIN!
    pass

print("Stack overflow riski:")
print("- Base case olmayan fonksiyonlar")
print("- Base case'e hiç ulaşmayan fonksiyonlar")
print("- Çok derin recursion")

# Python recursion limit
import sys
print(f"Python recursion limit: {sys.getrecursionlimit()}")

# Recursion limit test
def deep_recursion(n):
    if n <= 0:
        return 0
    return 1 + deep_recursion(n - 1)

# Güvenli test
try:
    result = deep_recursion(1000)  # Genelde sorun yok
    print(f"1000 derinlik: {result}")
except RecursionError as e:
    print(f"Recursion hatası: {e}")

# Fibonacci performance problemi
def fib_slow(n):
    """Yavaş fibonacci - exponential time"""
    if n <= 1:
        return n
    return fib_slow(n - 1) + fib_slow(n - 2)

# Memoization ile hızlandırma
def fib_memo(n, memo={}):
    """Memoized fibonacci - linear time"""
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

import time

# Performance karşılaştırması
n = 35
print(f"\nFibonacci({n}) performance:")

start = time.time()
slow_result = fib_slow(n)
slow_time = time.time() - start

start = time.time()
fast_result = fib_memo(n)
fast_time = time.time() - start

print(f"Yavaş version: {slow_time:.3f} saniye")
print(f"Memoized version: {fast_time:.6f} saniye")
print(f"Hızlanma: {slow_time/fast_time:.0f}x")

print("\n8. TAIL RECURSİON:")
print("-" * 17)

# Normal recursion (tail olmayan)
def factorial_normal(n):
    """Normal factorial"""
    if n <= 1:
        return 1
    return n * factorial_normal(n - 1)  # Çarpma işlemi return'den sonra

# Tail recursion
def factorial_tail(n, accumulator=1):
    """Tail recursive factorial"""
    if n <= 1:
        return accumulator
    return factorial_tail(n - 1, n * accumulator)  # Son işlem recursive çağrı

print(f"Normal factorial(5): {factorial_normal(5)}")
print(f"Tail factorial(5): {factorial_tail(5)}")

# Tail recursive sum
def sum_tail(lst, acc=0):
    """Tail recursive sum"""
    if not lst:
        return acc
    return sum_tail(lst[1:], acc + lst[0])

print(f"Tail sum: {sum_tail([1, 2, 3, 4, 5])}")

# Not: Python tail recursion optimization yapmaz!
print("\nNot: Python tail recursion optimization desteklemez")

print("\n9. RECURSİON vs İTERATİON:")
print("-" * 28)

# Factorial iterative
def factorial_iterative(n):
    """Iterative factorial"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Performance karşılaştırması
n = 20

start = time.time()
for _ in range(10000):
    recursive_result = faktoriyel(n)
recursive_time = time.time() - start

start = time.time()
for _ in range(10000):
    iterative_result = factorial_iterative(n)
iterative_time = time.time() - start

print(f"Factorial({n}) 10000 kez:")
print(f"Recursive: {recursive_time*1000:.2f} ms")
print(f"Iterative: {iterative_time*1000:.2f} ms")
print(f"Iterative {recursive_time/iterative_time:.1f}x daha hızlı")

# Bellek kullanımı
print(f"\nBellek kullanımı:")
print("Recursive: O(n) stack space")
print("Iterative: O(1) space")

print("\n10. RECURSİVE PATTERNS:")
print("-" * 23)

# Divide and conquer
def merge_sort(lst):
    """Merge sort - divide and conquer"""
    if len(lst) <= 1:
        return lst
    
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    
    return merge(left, right)

def merge(left, right):
    """İki sıralı listeyi birleştirir"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

unsorted = [64, 34, 25, 12, 22, 11, 90]
sorted_list = merge_sort(unsorted)
print(f"Merge sort: {unsorted} -> {sorted_list}")

# Backtracking örneği - N-Queens problem (basit)
def is_safe(board, row, col):
    """N-Queens için güvenli pozisyon kontrolü"""
    n = len(board)
    
    # Aynı sütun kontrolü
    for i in range(row):
        if board[i] == col:
            return False
    
    # Diagonal kontrolü
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False
    
    return True

def solve_nqueens(board, row):
    """N-Queens recursive çözümü"""
    n = len(board)
    
    if row == n:
        return True
    
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            if solve_nqueens(board, row + 1):
                return True
    
    return False

# 4x4 board için N-Queens
n = 4
board = [-1] * n
if solve_nqueens(board, 0):
    print(f"\n{n}-Queens çözümü: {board}")
    print("Board:")
    for i in range(n):
        row = [". "] * n
        row[board[i]] = "Q "
        print("".join(row))

print("\n11. RECURSİVE DEBUGGING:")
print("-" * 24)

def debug_factorial(n, depth=0):
    """Debug mesajları ile factorial"""
    indent = "  " * depth
    print(f"{indent}factorial({n}) çağrıldı")
    
    if n <= 1:
        print(f"{indent}Base case: return 1")
        return 1
    
    print(f"{indent}Recursive çağrı: factorial({n-1})")
    result = n * debug_factorial(n - 1, depth + 1)
    print(f"{indent}factorial({n}) = {n} * factorial({n-1}) = {result}")
    
    return result

print("Debug factorial(4):")
debug_factorial(4)

print("\n=== RECURSİVE FONKSİYONLAR ÖZETİ ===")
print("Temel bileşenler:")
print("  • Base case - recursion'ı durduran koşul")
print("  • Recursive case - kendini çağırma")
print("  • Progress - base case'e yaklaşma")
print()
print("Avantajları:")
print("  • Elegant ve sade kod")
print("  • Doğal problem çözümü (tree, graph)")
print("  • Mathematical problems için ideal")
print("  • Divide-and-conquer algorithms")
print()
print("Dezavantajları:")
print("  • Stack overflow riski")
print("  • Memory overhead")
print("  • Performance (çoğu durumda)")
print("  • Debugging zorluğu")
print()
print("Ne zaman kullan:")
print("  ✓ Tree/graph traversal")
print("  ✓ Divide-and-conquer")
print("  ✓ Mathematical sequences")
print("  ✓ Backtracking problems")
print()
print("Optimization teknikleri:")
print("  • Memoization")
print("  • Tail recursion (Python'da limited)")
print("  • Iterative alternatifler")
print("  • Dynamic programming")