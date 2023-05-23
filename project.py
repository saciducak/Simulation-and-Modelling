import numpy as np
import matplotlib.pyplot as plt

# Adım 1: L ve N değerlerini elde ederek, N tane çubuğu düz bir hat olarak konumlandırma
L = 10  # Örnek olarak L'i 10 olarak alalım
N = 5   # Örnek olarak N'i 5 olarak alalım

# Her bir çubuğun uzunluğunu hesaplayalım
length_per_bar = L / N

# Çubukların konumlarını saklamak için bir dizi oluşturalım
positions = np.zeros(N+1)  # N+1 çubuk için N+1 konum

for i in range(N+1):
    positions[i] = i * length_per_bar

# Adım 2: Simülasyon süresini belirleme
T = 100  # Örnek olarak T'yi 100 olarak alalım

# Adım 3: Her bir simülasyon adımında çubukları kopartma ve eklemeyi gerçekleştirme
def perform_simulation_step(positions):
    # Rastgele olarak sağ veya sol ucu seçelim
    selected_end = np.random.choice([0, N])

    # Seçilen çubuğu kopartalım
    selected_bar = positions[selected_end]
    positions = np.delete(positions, selected_end)

    # Çubuğu rastgele bir yönde ekleyelim
    new_position = selected_bar + np.random.uniform(-length_per_bar, length_per_bar)
    positions = np.insert(positions, selected_end, new_position)

    return positions

# Adım 4: Birinci çubuğun sol ucu ile son çubuğun sağ ucu arasındaki mesafenin zamanla değişimini kaydetme
distances = np.zeros(T+1)
distances[0] = positions[N] - positions[0]  # Başlangıç mesafesi

for t in range(T):
    positions = perform_simulation_step(positions)
    distances[t+1] = positions[N] - positions[0]

# Adım 5: Sistemin dengeye gelip gelmediğini zaman değişimine bakarak değerlendirme
def is_system_stable(distances):
    # Örnek bir değerlendirme işlemi
    threshold = 0.1  # Eşik değeri

    for t in range(1, T+1):
        if abs(distances[t] - distances[t-1]) > threshold:
            return False

    return True

system_stable = is_system_stable(distances)

# Adım 6: Denge durumları üzerinden ortalama uzaklığı belirleme
average_distance = np.mean(distances)

# Adım 7: Uzaklık için denge durumları üzerinden histogram oluşturma
plt.hist(distances, bins=10)
plt.xlabel('Mesafe')
plt.ylabel('Frekans')
plt.title('Mesafe Histogramı')
plt.show()


# Adım 8: Histogramın üzerinde en büyük olası uzaklık hesabını yapamadım.

# Adım 9:
# Şimdi kopartma-ekleme işlemi üzerinde kısıtlama koşullarını uygulayalım.
# Geçiş oranını yaklaşık %65 civarında tutmaya çalışacağız.

def perform_constrained_simulation_step(positions, d_lim, R):
    selected_end = np.random.choice([0, N])
    selected_bar = positions[selected_end]
    positions = np.delete(positions, selected_end)

    # Yeni konumu rastgele belirleme
    new_position = selected_bar + np.random.uniform(-length_per_bar, length_per_bar)

    # Kısıtlama koşulunu kontrol etme
    if abs(new_position - positions[selected_end-1]) > d_lim and abs(new_position - positions[selected_end+1]) > d_lim:
        positions = np.insert(positions, selected_end, new_position)
    else:
        if np.exp(-abs(new_position - positions[selected_end-1])) >= R:
            positions = np.insert(positions, selected_end, new_position)

    return positions

