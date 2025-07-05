import matplotlib.pyplot as plt
import numpy as np

materialy = ['TiN', 'SiC + 2%B$_4$', '50%Al$_2$O$_3$ + 50% Ti(CN)', 'WC / Co', 'Si$_3$N$_4$', 'Al$_2$I$_3$']
twardosc_hv1 = [1537.4, 2439.8, 1692.2, 1247, 1657, 1623]


materialy2 = ["WC + Co", "Al$_2$O$_3$"]
wymiary_mm = [[12.7,12.7, 4.7], [12.7,12.7, 4.7]]
wymiary_cm = [[i/10 for i in j] for j in wymiary_mm]
masy_g = [9.85, 3.10]
V = [i[0] * i[1] * i[2] for i in wymiary_cm]

e = [masy_g[i] / V[i] for i in range(len(masy_g))]



plt.figure(figsize=(8, 5))
plt.bar(materialy, twardosc_hv1, color='skyblue')
plt.xlabel('Materiał')
plt.ylabel('Twardość HV1 [kG/mm$^2$]')
plt.title('Twardość HV1 w zależności od materiału')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

print(wymiary_cm)
print(masy_g)
print(V)
print(e)