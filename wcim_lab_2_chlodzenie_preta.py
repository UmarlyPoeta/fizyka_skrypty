"""
Współczynnik wnikania ciepła przy promieniowaniu - WCIM Lab 1
"""

# Stała promieniowania ciała doskonale czarnego
C_S = 5.67  # W/(m^2 * K^4) - stała Stefana-Boltzmanna

def oblicz_alfa_promieniowanie(epsilon_s: float, T_s: float, T_ot: float) -> float:
    """
    Oblicza współczynnik wnikania ciepła przy promieniowaniu α_r
    na podstawie wzoru (15):
    
    α_r = ε_s * C_s * [(T_s/100)^4 - (T_ot/100)^4] / (T_s - T_ot)
    
    Parametry:
    ----------
    epsilon_s : float
        Zdolność emisji powierzchni pręta (emisyjność), wartość 0-1
    T_s : float
        Temperatura powierzchni pręta [K]
    T_ot : float
        Temperatura otoczenia (ścian) [K]
    
    Zwraca:
    -------
    float
        Współczynnik wnikania ciepła przy promieniowaniu [W/(m^2*K)]
    """
    if T_s == T_ot:
        return 0.0
    
    # Wzór (15)
    licznik = (T_s / 100) ** 4 - (T_ot / 100) ** 4
    mianownik = T_s - T_ot
    
    alfa_r = epsilon_s * C_S * (licznik / mianownik)
    
    return alfa_r


def oblicz_epsilon_zastepczy(epsilon_s: float, epsilon_ot: float, A: float, A_ot: float) -> float:
    """
    Oblicza zastępczą zdolność emisji między ścianką pręta a ścianami otaczającymi
    na podstawie wzoru Christiansena (14):
    
    ε_s-ot = 1 / (1/ε_s + (A/A_ot) * (1/ε_ot - 1))
    
    Parametry:
    ----------
    epsilon_s : float
        Zdolność emisji powierzchni pręta
    epsilon_ot : float
        Zdolność emisji ścian otaczających
    A : float
        Powierzchnia pręta [m^2]
    A_ot : float
        Powierzchnia ścian otaczających [m^2]
    
    Zwraca:
    -------
    float
        Zastępcza zdolność emisji
    """
    epsilon_zast = 1 / (1/epsilon_s + (A/A_ot) * (1/epsilon_ot - 1))
    return epsilon_zast


def oblicz_strumien_ciepla_promieniowanie(A: float, epsilon: float, T_s: float, T_ot: float) -> float:
    """
    Oblicza strumień ciepła przekazywany na drodze promieniowania
    na podstawie wzoru (11):
    
    Q_r = A * ε * C_s * [(T_s/100)^4 - (T_ot/100)^4]
    
    Parametry:
    ----------
    A : float
        Powierzchnia wymiany ciepła [m^2]
    epsilon : float
        Zdolność emisji (emisyjność)
    T_s : float
        Temperatura powierzchni [K]
    T_ot : float
        Temperatura otoczenia [K]
    
    Zwraca:
    -------
    float
        Strumień ciepła [W]
    """
    Q_r = A * epsilon * C_S * ((T_s/100)**4 - (T_ot/100)**4)
    return Q_r


if __name__ == "__main__":
    # Przykładowe obliczenia
    print("=" * 60)
    print("Współczynnik wnikania ciepła przy promieniowaniu")
    print("=" * 60)
    
    # Przykładowe dane
    epsilon_s = 0.85  # emisyjność powierzchni pręta
    T_s_celsius = 100  # temperatura pręta [°C]
    T_ot_celsius = 20  # temperatura otoczenia [°C]
    
    # Przeliczenie na Kelwiny
    T_s = T_s_celsius + 273.15  # [K]
    T_ot = T_ot_celsius + 273.15  # [K]
    
    # Obliczenia
    alfa_r = oblicz_alfa_promieniowanie(epsilon_s, T_s, T_ot)
    
    print(f"\nDane wejściowe:")
    print(f"  Emisyjność ε_s = {epsilon_s}")
    print(f"  Temperatura pręta T_s = {T_s_celsius}°C = {T_s:.2f} K")
    print(f"  Temperatura otoczenia T_ot = {T_ot_celsius}°C = {T_ot:.2f} K")
    print(f"\nWynik:")
    print(f"  Współczynnik wnikania ciepła α_r = {alfa_r:.4f} W/(m²·K)")