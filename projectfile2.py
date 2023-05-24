import numpy as np
import matplotlib.pyplot as plt

# Parametreleri tanımlama
L = 10  # Çubuk uzunluğu
N = 5   # Çubuk sayısı
T = 100 # Simülasyon süresi
d_lim = 2.0 # Kısıtlama mesafesi
R = 0.65   # Geçiş kabul oranı

# Çubukların başlangıç konumlarını düz bir hat olarak konumlandırma
positions = np.linspace(0, L, N+1)

# Çubuk konumlarını saklamak için bir dizi oluşturma
positions_history = np.zeros((T+1, N+1))
positions_history[0] = positions

# Geçiş sayacını ve kabul sayacını sıfırlama
transition_count = 0
accepted_count = 0

# Simülasyon adımlarını gerçekleştirme
for t in range(1, T+1):
    # Rastgele olarak bir çubuk seçme
    selected_bar = np.random.choice([0, N])

    # Seçilen çubuğu koparma ve diğer uca ekleme
    if selected_bar == 0:
        positions = np.roll(positions, -1)
    else:
        positions = np.roll(positions, 1)

    # İki çubuk arasındaki mesafeleri hesaplama
    distances = np.diff(positions)

    # Kısıtlama kontrolü ve geçiş kabulü
    if np.all(distances >= d_lim):
        transition_count += 1
        accepted_count += 1
    else:
        for i in range(N-1):
            if distances[i] < d_lim:
                if np.exp(-distances[i]) >= R:
                    transition_count += 1
                    accepted_count += 1
                    break

    # Çubuk konumlarını saklama
    positions_history[t] = positions

# Geçiş kabul oranını hesaplama
acceptance_rate = accepted_count / transition_count

# Sonuçları ve grafikleri görüntüleme
print("Sistem Özellikleri:")
print(f"Çubuk Uzunluğu (L): {L}")
print(f"Çubuk Sayısı (N): {N}")
print(f"Simülasyon Süresi (T): {T}")
print(f"Kısıtlama Mesafesi (d_lim): {d_lim}")
print(f"Geçiş Kabul Oranı (R): {R}")
print(f"Geçiş Sayısı: {transition_count}")
print(f"Kabul Sayısı: {accepted_count}")
print(f"Geçiş Kabul Oranı: {acceptance_rate:.2%}")

# Çubuk konumlarının zamanla değişimini gösteren grafik
time_steps = np.arange(T+1)
plt.figure(figsize=(8, 6))
for i in range(N+1):
    plt.plot(time_steps, positions_history[:, i], label=f"Bar {i}")
plt.xlabel("Zaman")
plt.ylabel("Konum")
plt.title("Çubuk Konumlarının Zamanla Değişimi")
plt.legend()
plt.grid(True)
plt.show()
