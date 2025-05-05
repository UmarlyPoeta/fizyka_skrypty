import matplotlib.pyplot as plt
from fpdf import FPDF
from ollama import chat
import textwrap

# Dane
epsilon = [1, 2.5, 3.5, 5, 6]
wielkosc_ziarna = [1, 2.5, 5, 23.5, 60]
srednia_wielkosc_ziarna = [100 / i for i in wielkosc_ziarna]

# Wykres
plt.figure(figsize=(8, 6))
plt.plot(epsilon, srednia_wielkosc_ziarna, marker='o', linestyle='-', color='b')
plt.xlabel('Wydłużenie ε')
plt.ylabel('Średnia wielkość ziarna')
plt.title('Średnia wielkość ziarna w funkcji wydłużenia ε')
plt.grid(True)
plt.savefig("wykres.png")
plt.close()

# AI: wstęp teoretyczny
wstep_output = chat(model="llama3.2", messages=[
    {"role": "user", "content": """
Napisz wprowadzenie teoretyczne do badania wpływu warunków odkształcenia i wyżarzania na własności metali:
- Defekty struktury krystalicznej
- Zjawiska zachodzące kolejno podczas wygrzewania odkształconego materiału
- Co to jest temperatura rekrystalizacji i od czego zależy?
- Jak wielkość ziarna wpływa na własności metali?
- Co to jest temperatura przejścia w stan kruchy i od czego zależy?
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
pdf.cell(0, 10, "Laboratorium 5 – Patryk Kozłowski, grupa laboratoryjna nr 4", ln=True)

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
