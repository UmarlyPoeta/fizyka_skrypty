import matplotlib.pyplot as plt
from fpdf import FPDF
from ollama import chat
import textwrap

# Dane
nr = [i for i in range(1,7)]
hrb = [69.7, 64.5, 70.4, 67.3, 70.2, 72.7]
hv = [124, 115, 126, 120, 125, 131]


# Wykres
plt.figure(figsize=(8, 6))
plt.plot(epsilon, srednia_wielkosc_ziarna, marker='o', linestyle='-', color='b')
plt.xlabel('Wydłużenie ε')
plt.ylabel('Średnia wielkość ziarna')
plt.title('Średnia wielkość ziarna w funkcji wydłużenia ε')
plt.grid(True)
plt.savefig("wykres_twardosc.png")
plt.close()

# AI: wstęp teoretyczny
wstep_output = chat(model="llama3.2", messages=[
    {"role": "user", "content": """
Napisz wprowadzenie teoretyczne do badania wpływu warunków odkształcenia i wyżarzania na własności metali:
- Przemiany zachodzące podczas nagrzewania i chłodzenia stali
(przemiana austenityczna, perlityczna, bainityczna i martenzytyczna)
- Wyżarzanie i jego rodzaje
- Rodzaje ośrodków chłodzących
- Odpuszczanie stali i jego rodzaje
- Przemiany zachodzące podczas odpuszczania stali zahartowanej
- Przesycanie i starzenie
"""}
])
wstep = wstep_output['message']['content']

# AI: wnioski
wnioski_output = chat(model="llama3.2", messages=[
    {"role": "user", "content": "Dlaczego średnia wielkość ziarna maleje ze wzrostem wydłużenia epsilon?"}
])
wnioski = wnioski_output['message']['content']

# Czyszczenie znaków i zawijanie tekstu
for char in ["–", "—", "•", "“", "”", "*"]:
    wstep = wstep.replace(char, "")
    wnioski = wnioski.replace(char, "")

# Zawijanie linii (max 120 znaków)
wstep_wrapped = "\n".join(textwrap.wrap(wstep, width=120))
wnioski_wrapped = "\n".join(textwrap.wrap(wnioski, width=120))

# PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_left_margin(15)
pdf.set_right_margin(15)
pdf.add_page()

# Czcionka z UTF-8
font_path = "/usr/share/fonts/dejavu-sans-fonts/DejaVuSans.ttf"  # Ścieżka zależna od systemu
pdf.add_font("DejaVu", "", font_path)
pdf.set_font("DejaVu", "", 14)

# Nagłówek
pdf.cell(0, 10, "Laboratorium 6 – Patryk Kozłowski, grupa laboratoryjna nr 4", ln=True)

pdf.ln(10)
pdf.set_font("DejaVu", "", 12)
pdf.multi_cell(0, 8, wstep_wrapped)

pdf.ln(10)
pdf.image("wykres.png", w=180)

pdf.ln(10)
pdf.set_font("DejaVu", "", 12)
pdf.cell(0, 10, "Wnioski:", ln=True)

pdf.set_font("DejaVu", "", 12)
pdf.multi_cell(0, 8, wnioski_wrapped)

pdf.output("sprawozdanie.pdf")
