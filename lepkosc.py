import math

srednica_kulki_mm = [4.40, 3.37, 4.14, 3.41, 4.27, 4.43, 4.24, 4.38, 4.41, 4.39]
masa_kulki_g = [0.263, 0.273, 0.447, 0.172, 0.472, 0.268, 0.244, 0.393, 0.110, 0.269]
czas_spadku_s = [7.69, 7.56, 4.78, 9.41, 6.44, 7.60, 8.25, 7.38, 14.78, 7.68]

h = 0.45
promien_kulki_mm = [i /2 for i in srednica_kulki_mm]
g = 9.81
pi = math.pi
gestosc_cieczy = 1.26

promien_kulki_m = [i / 1000 for i in promien_kulki_mm]
masa_kulki_kg = [i / 1000 for i in masa_kulki_g]

V_kulki = [4 / 3 * pi * (i ** 3) for i in promien_kulki_m]

gestosc_kulki = [masa_kulki_kg[i] / V_kulki[i] for i in range(len(masa_kulki_kg))]

wsp_lepkosci = [(2 * (promien_kulki_m[i] ** 2) * g * (gestosc_kulki[i] - gestosc_cieczy) * czas_spadku_s[i]) / (9 * h) for i in range(len(promien_kulki_m))]


print(wsp_lepkosci)

srednia_wsp_lepkosci = sum(wsp_lepkosci) / len(wsp_lepkosci)

n = 10

niepewnosc_wsp_lepkosci = math.sqrt(sum([(i - srednia_wsp_lepkosci) ** 2 for i in wsp_lepkosci]) / (n * (n - 1)))



#print(srednia_wsp_lepkosci)
#print(niepewnosc_wsp_lepkosci)
print(promien_kulki_m)
print(czas_spadku_s)
print(gestosc_cieczy)
