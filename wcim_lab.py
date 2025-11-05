import numpy as np
import matplotlib.pyplot as plt

# Wczytanie danych z pliku (przecinek jako separator dziesiętny)
data = np.loadtxt('wcim.txt', skiprows=2, delimiter='\t', 
                  converters={i: lambda s: float(s.replace(',', '.')) 
                             for i in range(6)})

time = data[:, 0]  # Pierwsza kolumna to czas
temps = data[:, 1:]  # Kolumny: T2, T3, T4, T6, T8 (5 termopar)

# Zapisanie danych do pliku tpomiar.dat
# Format: czas, temperatura_2, temperatura_3, temperatura_4, temperatura_6, temperatura_8
tpomiar_data = np.column_stack([time, temps])
np.savetxt('tpomiar.dat', tpomiar_data, fmt='%.6f', delimiter='\t',
           header='czas [s]\tT2 [C]\tT3 [C]\tT4 [C]\tT6 [C]\tT8 [C]',
           comments='')

print("Plik tpomiar.dat został utworzony.")
print(f"Liczba punktów czasowych: {len(time)}")
print(f"Liczba termopar: {temps.shape[1]}")

# Pozycje termopar na pręcie (należy dostosować do rzeczywistych wartości)
# Pozycje dla termopar T2, T3, T4, T6, T8
positions = np.array([0.05, 0.10, 0.15, 0.20, 0.25])  # [m]

# Wybór momentu czasowego do analizy (np. stan ustalony - ostatni pomiar)
steady_state_temps = temps[-1, :]

# Dopasowanie modelu (wielomian stopnia 2)
degree = 2
coeffs = np.polyfit(positions, steady_state_temps, degree)

# Generowanie gładkiego rozkładu temperatury
x_model = np.linspace(positions[0], positions[-1], 100)
y_model = np.polyval(coeffs, x_model)

# Wizualizacja
plt.figure(figsize=(10, 6))
plt.plot(positions, steady_state_temps, 'ro', label='Pomiary (T2, T3, T4, T6, T8)', markersize=8)
plt.plot(x_model, y_model, 'b-', label=f'Model (wielomian st. {degree})')
plt.xlabel('Pozycja na pręcie [m]')
plt.ylabel('Temperatura [°C]')
plt.title('Rozkład temperatury wzdłuż nagrzewanego pręta')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('rozklad_temperatury.png', dpi=300)
plt.show()

# Wyświetlenie współczynników
print("\nWspółczynniki modelu (od najwyższego stopnia):")
print(coeffs)
print(f"\nRównanie: T(x) = {coeffs[0]:.2f}x² + {coeffs[1]:.2f}x + {coeffs[2]:.2f}")


