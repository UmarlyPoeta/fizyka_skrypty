# Podstawy mechaniki płynów — rozwiązania i nauka krok po kroku

Ten materiał jest zrobiony tak, żebyś miał **jednocześnie gotowe rozwiązania i sposób myślenia**, czyli:
- **co rozpoznać w zadaniu,**
- **jaki wzór dobrać,**
- **jak sprawdzić jednostki,**
- **jak policzyć wynik,**
- **jak interpretować odpowiedź.**

---

# 1. Szybka ściąga teoretyczna

## 1.1. Własności fizyczne płynów

### Gęstość
\[
\rho = \frac{m}{V}
\]

gdzie:
- \(\rho\) — gęstość \([kg/m^3]\)
- \(m\) — masa \([kg]\)
- \(V\) — objętość \([m^3]\)

### Lepkość dynamiczna
\[
\mu
\]

jednostka:
\[
Pa \cdot s = \frac{kg}{m \cdot s}
\]

### Lepkość kinematyczna
\[
\nu = \frac{\mu}{\rho}
\]

jednostka:
\[
m^2/s
\]

### Rozszerzalność objętościowa
Dla cieczy przy zmianie temperatury:
\[
V = V_0(1+\beta \Delta T)
\]

czyli gęstość można przybliżyć:
\[
\rho_2 = \frac{\rho_1}{1+\beta(T_2-T_1)}
\]

### Ściśliwość
Dla niewielkich zmian ciśnienia:
\[
\rho = \rho_0 \left(1+\kappa \Delta p\right)
\]

gdzie \(\kappa\) to współczynnik ściśliwości.

---

## 1.2. Ciśnienie

### Ciśnienie bezwzględne
\[
p_{abs} = p_{atm} + p_{nad}
\]

### Gdy mamy podciśnienie
\[
p_{abs} = p_{atm} - p_{pod}
\]

### Przeliczenia
- \(1\;hPa = 100\;Pa\)
- \(1\;kPa = 1000\;Pa\)
- \(1\;MPa = 10^6\;Pa\)
- \(1\;mmHg \approx 133.322\;Pa\)

### Ciśnienie hydrostatyczne
\[
p = \rho g h
\]

---

## 1.3. Równanie ciągłości przepływu

### Dla masy
\[
\dot m = \rho A v
\]

### Dla cieczy nieściśliwej
\[
Q = Av
\]

gdzie:
- \(Q\) — strumień objętości \([m^3/s]\)
- \(\dot m\) — strumień masy \([kg/s]\)
- \(A\) — pole przekroju \([m^2]\)
- \(v\) — prędkość \([m/s]\)

---

## 1.4. Równanie Bernoulliego

\[
p + \frac{1}{2}\rho v^2 + \rho g z = const
\]

W praktyce:
- \(p\) — energia ciśnienia,
- \(\frac{1}{2}\rho v^2\) — energia kinetyczna,
- \(\rho g z\) — energia położenia.

---

## 1.5. Liczba Reynoldsa

\[
Re = \frac{vD}{\nu}
\]

Interpretacja:
- \(Re < 2300\) — przepływ laminarny
- \(2300 \div 4000\) — zakres przejściowy
- \(Re > 4000\) — przepływ turbulentny

---

## 1.6. Opory przepływu

### Straty liniowe
\[
\Delta p = \lambda \frac{L}{D}\frac{\rho v^2}{2}
\]

### Straty miejscowe
\[
\Delta p = \zeta \frac{\rho v^2}{2}
\]

---

# 2. Jak rozwiązywać typowe zadania z mechaniki płynów

## Schemat myślenia

### Krok 1 — rozpoznaj typ zadania
Czy to jest zadanie z:
- ciśnienia,
- gęstości,
- gazu doskonałego,
- lepkości,
- ciągłości przepływu,
- Bernoulliego,
- Reynoldsa,
- strat ciśnienia?

### Krok 2 — wypisz dane
Zawsze zamień wszystko do SI:
- mm → m
- hPa → Pa
- mmHg → Pa
- °C → K, jeśli trzeba

### Krok 3 — wybierz wzór główny
Nie 10 wzorów naraz. Najpierw **jeden główny wzór**.

### Krok 4 — sprawdź, czy trzeba coś przeliczyć przed podstawieniem
Najczęściej:
- pole przekroju,
- ciśnienie absolutne,
- gęstość,
- temperaturę do Kelwinów.

### Krok 5 — policz i sprawdź sens
Np. jeśli dla powietrza wychodzi \(500\;m/s\), to trzeba się zastanowić, czy wynik ma sens fizyczny.

---

# 3. Zadania rozwiązane

---

## Zadanie 1

### Treść
W zbiorniku ciśnieniowym zmierzono za pomocą manometru nadciśnienie gazu wynoszące  
\[
\Delta p_1 = 200\;kPa
\]
Barometr wskazywał:
\[
p_{atm} = 1001\;hPa
\]
Ile wynosi ciśnienie bezwzględne \(p_1\) w zbiorniku?

### Co rozpoznać?
To jest klasyczne zadanie na:
- ciśnienie atmosferyczne,
- nadciśnienie,
- ciśnienie bezwzględne.

### Wzór
\[
p_{abs} = p_{atm} + \Delta p
\]

### Przeliczenie jednostek
\[
1001\;hPa = 100100\;Pa
\]
\[
200\;kPa = 200000\;Pa
\]

### Obliczenia
\[
p_1 = 100100 + 200000 = 300100\;Pa
\]

### Odpowiedź
\[
p_1 = 300100\;Pa = 300.1\;kPa
\]

### Jak to zapamiętać?
**Nadciśnienie dodajesz do atmosferycznego.**

---

## Zadanie 2

### Treść
W rurociągu podłączonym do pompy usuwającej powietrze z mikroskopu elektronowego, manometrem zmierzono ciśnienie  
\[
\Delta p_1 = 80\;hPa
\]
Barometr wskazywał:
\[
p_{atm} = 980\;hPa
\]
Ile wynosi ciśnienie bezwzględne w rurociągu?

### Co rozpoznać?
Tutaj chodzi o **podciśnienie**, bo pompa usuwa powietrze.

### Wzór
\[
p_{abs} = p_{atm} - \Delta p
\]

### Przeliczenia
\[
980\;hPa = 98000\;Pa
\]
\[
80\;hPa = 8000\;Pa
\]

### Obliczenia
\[
p = 98000 - 8000 = 90000\;Pa
\]

### Odpowiedź
\[
p = 90000\;Pa = 90\;kPa
\]

### Jak rozpoznać minus?
Jeśli urządzenie **wysysa**, **odsysa**, **usuwa powietrze**, to zwykle masz **podciśnienie**.

---

## Zadanie 3

### Treść
Obliczyć gęstość wody w temperaturze
\[
T_1 = 323\;K
\]
jeżeli znana jest gęstość w warunkach normalnych.

### Co rozpoznać?
Zmiana temperatury → zmiana objętości → zmiana gęstości.

### Wzór
\[
\rho_2 = \frac{\rho_1}{1+\beta(T_2-T_1)}
\]

### Założenia tablicowe
Przyjmijmy:
- \(\rho_1 = 998.2\;kg/m^3\) dla \(293\;K\)
- \(\beta = 2.1 \cdot 10^{-4}\;1/K\)

### Dane
\[
T_2 = 323\;K,\quad T_1 = 293\;K
\]
\[
\Delta T = 30\;K
\]

### Obliczenia
\[
\rho_2 = \frac{998.2}{1+2.1\cdot10^{-4}\cdot30}
\]
\[
\rho_2 = \frac{998.2}{1.0063} \approx 991.95\;kg/m^3
\]

### Odpowiedź
\[
\rho_2 \approx 992\;kg/m^3
\]

### Co tu jest ważne?
Gdy temperatura rośnie:
- objętość rośnie,
- gęstość maleje.

---

## Zadanie 4

### Treść
Obliczyć gęstość wody przy ciśnieniu
\[
p_1 = 5\cdot10^5\;Pa
\]
jeżeli znana jest gęstość w warunkach normalnych.

### Co rozpoznać?
Zmiana ciśnienia wpływa na gęstość przez ściśliwość.

### Wzór
\[
\rho = \rho_0(1+\kappa \Delta p)
\]

### Założenia
Przyjmujemy:
- \(\rho_0 = 998.2\;kg/m^3\)
- \(\kappa = 4.6\cdot10^{-10}\;Pa^{-1}\)
- \(p_0 = 101325\;Pa\)

### Obliczenia
\[
\Delta p = 5\cdot10^5 - 101325 = 398675\;Pa
\]

\[
\rho = 998.2(1+4.6\cdot10^{-10}\cdot398675)
\]

\[
\rho \approx 998.2(1.0001834) \approx 998.38\;kg/m^3
\]

### Odpowiedź
\[
\rho \approx 998.4\;kg/m^3
\]

### Wniosek
Woda jest bardzo mało ściśliwa, więc zmiana gęstości jest niewielka.

---

## Zadanie 5

### Treść
Obliczyć masę dwutlenku węgla zawartą w zbiorniku o pojemności
\[
V = 20\;m^3
\]
przy ciśnieniu
\[
p = 1013\;hPa
\]

### Co rozpoznać?
Gaz w zbiorniku → równanie gazu doskonałego.

### Wzór
\[
pV = nRT
\]
oraz
\[
m = nM
\]

Po połączeniu:
\[
m = \frac{pVM}{RT}
\]

### Założenia
Przyjmuję:
- \(T = 293.15\;K\)
- \(M_{CO_2} = 0.04401\;kg/mol\)
- \(R = 8.314\;J/(mol\cdot K)\)

### Przeliczenie ciśnienia
\[
1013\;hPa = 101300\;Pa
\]

### Obliczenia
\[
m=\frac{101300\cdot20\cdot0.04401}{8.314\cdot293.15}
\]

\[
m \approx 36.6\;kg
\]

### Odpowiedź
\[
m \approx 36.6\;kg
\]

### Jak myśleć?
Jeśli masz:
- objętość zbiornika,
- ciśnienie,
- gaz,
to prawie zawsze sprawdzasz **gaz doskonały**.

---

## Zadanie 6

### Treść
O ile zwiększy się masa zbiornika o pojemności
\[
V=16\;m^3
\]
jeżeli na miejsce powietrza o ciśnieniu
\[
p_1=0.1\;MPa
\]
będzie wprowadzony metan o ciśnieniu
\[
p_2=2.5\;MPa
\]
i tej samej temperaturze
\[
T=298\;K
\]

### Co rozpoznać?
Porównanie mas dwóch gazów w tym samym zbiorniku.

### Wzór
\[
m=\frac{pVM}{RT}
\]

Liczymy:
- masę powietrza,
- masę metanu,
- różnicę.

### Dane
- \(V=16\;m^3\)
- \(T=298\;K\)
- \(M_{pow} = 0.02897\;kg/mol\)
- \(M_{CH_4} = 0.01604\;kg/mol\)
- \(p_1=0.1\cdot10^6\;Pa\)
- \(p_2=2.5\cdot10^6\;Pa\)

### Masa powietrza
\[
m_1=\frac{0.1\cdot10^6\cdot16\cdot0.02897}{8.314\cdot298}
\approx 18.7\;kg
\]

### Masa metanu
\[
m_2=\frac{2.5\cdot10^6\cdot16\cdot0.01604}{8.314\cdot298}
\approx 258.9\;kg
\]

### Przyrost masy
\[
\Delta m = m_2-m_1 = 258.9-18.7 = 240.2\;kg
\]

### Odpowiedź
\[
\Delta m \approx 240.2\;kg
\]

---

## Zadanie 7

### Treść
Lepkość dynamiczna nafty w temperaturze
\[
T_2=323\;K
\]
wynosi
\[
\mu = 5.884\cdot10^{-3}\;kg/(m\cdot s)
\]
Wyznaczyć lepkość kinematyczną, jeżeli gęstość w temperaturze
\[
T_1=293\;K
\]
wynosi
\[
\rho_1=800\;kg/m^3
\]
a współczynnik rozszerzalności objętościowej
\[
\beta=0.96\cdot10^{-3}\;1/K
\]

### Co rozpoznać?
Trzeba policzyć:
1. nową gęstość przy wyższej temperaturze,
2. potem skorzystać z:
\[
\nu=\frac{\mu}{\rho}
\]

### Krok 1 — gęstość w 323 K
\[
\rho_2 = \frac{\rho_1}{1+\beta(T_2-T_1)}
\]

\[
\rho_2 = \frac{800}{1+0.96\cdot10^{-3}\cdot30}
\]

\[
\rho_2 = \frac{800}{1.0288} \approx 777.6\;kg/m^3
\]

### Krok 2 — lepkość kinematyczna
\[
\nu=\frac{5.884\cdot10^{-3}}{777.6}
\approx 7.57\cdot10^{-6}\;m^2/s
\]

### Odpowiedź
\[
\nu \approx 7.57\cdot10^{-6}\;m^2/s
\]

---

## Zadanie 8

### Treść
Wyznaczyć gęstość wilgotnego powietrza o parametrach:
- nadciśnienie:
\[
\Delta p_1 = 50\;Pa
\]
- temperatura:
\[
t=20^\circ C
\]
- ciśnienie barometryczne:
\[
746.3\;mmHg
\]
- wilgotność względna:
\[
\varphi = 60\%
\]

### Co rozpoznać?
To jest wilgotne powietrze, więc:
- część ciśnienia daje suche powietrze,
- część daje para wodna.

### Wzór
\[
\rho = \frac{p_d}{R_dT}+\frac{p_v}{R_vT}
\]

gdzie:
- \(p_d\) — ciśnienie suchego powietrza,
- \(p_v\) — ciśnienie pary wodnej.

### Krok 1 — ciśnienie całkowite
\[
p_{atm}=746.3\cdot133.322 \approx 99498\;Pa
\]

\[
p = p_{atm}+50 = 99548\;Pa
\]

### Krok 2 — ciśnienie pary nasyconej dla \(20^\circ C\)
Przyjmujemy:
\[
p_{sat} \approx 2338\;Pa
\]

### Krok 3 — ciśnienie pary rzeczywistej
\[
p_v = \varphi p_{sat} = 0.60\cdot2338 \approx 1403\;Pa
\]

### Krok 4 — ciśnienie suchego powietrza
\[
p_d = p-p_v = 99548-1403 = 98145\;Pa
\]

### Krok 5 — podstawienie
\[
T=293.15\;K
\]
\[
R_d = 287.05\;J/(kg\cdot K)
\]
\[
R_v = 461.5\;J/(kg\cdot K)
\]

\[
\rho = \frac{98145}{287.05\cdot293.15}+\frac{1403}{461.5\cdot293.15}
\]

\[
\rho \approx 1.177\;kg/m^3
\]

### Odpowiedź
\[
\rho \approx 1.177\;kg/m^3
\]

### Dlaczego wilgotne powietrze bywa lżejsze?
Bo para wodna ma mniejszą masę molową niż suche powietrze.

---

## Zadanie 9 — Sutherland (EXCEL)

### Treść
Obliczyć lepkość dynamiczną powietrza w temperaturze \(20^\circ C\) korzystając z wzoru Sutherlanda.

### Wzór
\[
\mu(T)=\mu_0\left(\frac{T}{T_0}\right)^{3/2}\frac{T_0+S}{T+S}
\]

### Stałe dla powietrza
- \(\mu_0=1.716\cdot10^{-5}\;Pa\cdot s\)
- \(T_0=273.15\;K\)
- \(S=110.4\;K\)

### Dane
\[
T=293.15\;K
\]

### Obliczenia
\[
\mu=1.716\cdot10^{-5}\left(\frac{293.15}{273.15}\right)^{3/2}\frac{273.15+110.4}{293.15+110.4}
\]

\[
\mu \approx 1.81\cdot10^{-5}\;Pa\cdot s
\]

### Odpowiedź
\[
\mu \approx 1.81\cdot10^{-5}\;Pa\cdot s
\]

### Formuła do Excela
```excel
=1.716E-5*(293.15/273.15)^(3/2)*((273.15+110.4)/(293.15+110.4))
```
## 11. Równowaga ciśnień dla manometru wodnego mierzącego różnicę ciśnień między dwoma punktami rurociągu powietrznego

### O co chodzi
Trzeba **rozpisać bilans ciśnień** dla manometru różnicowego U-rurkowego z cieczą manometryczną (tu: wodą), podłączonego do dwóch punktów przewodu z powietrzem.

Oznaczmy:
- punkt 1 — ciśnienie `p1`
- punkt 2 — ciśnienie `p2`
- ciecz manometryczna: woda o gęstości `ρw`
- gaz w przewodzie: powietrze o gęstości `ρp`
- różnica poziomów cieczy manometrycznej: `h`

### Zasada
W tej samej cieczy, na tej samej wysokości, ciśnienia muszą być równe.

Jeżeli przechodzimy:
- **w dół** w cieczy: ciśnienie rośnie o `ρgh`
- **w górę** w cieczy: ciśnienie maleje o `ρgh`

### Równanie ogólne
Dla manometru z cieczą cięższą od gazu:

\[
p_1 - p_2 = (\rho_w - \rho_p) g h
\]

gdzie:
- `ρw` — gęstość wody
- `ρp` — gęstość powietrza
- `g = 9.81 m/s²`
- `h` — różnica poziomów słupów cieczy

### Uproszczenie praktyczne
Ponieważ:

\[
\rho_p \ll \rho_w
\]

to zwykle przyjmuje się:

\[
p_1 - p_2 \approx \rho_w g h
\]

### Wniosek
- jeśli poziom wody po stronie 2 jest wyżej niż po stronie 1, to `p1 > p2`
- jeśli poziom wody po stronie 1 jest wyżej niż po stronie 2, to `p2 > p1`

### Jak to rozwiązywać na kolokwium
1. Narysuj dwa punkty: `p1` i `p2`.
2. Zaznacz różnicę poziomów `h`.
3. Idź „po cieczy” od jednego punktu do drugiego.
4. Dodawaj `+ρgh`, gdy schodzisz w dół.
5. Odejmuj `-ρgh`, gdy idziesz w górę.
6. Zrównaj ciśnienia na tej samej wysokości.
7. Na końcu uprość do:
   \[
   \Delta p = (\rho_w - \rho_p)gh
   \]
   albo praktycznie:
   \[
   \Delta p \approx \rho_w g h
   \]

---

## 12. Obliczyć prędkość przepływu powietrza `v1` i `v2` w dwóch przekrojach przewodu

### Dane
- `D1 = 250 mm = 0.25 m`
- `D2 = 80 mm = 0.08 m`
- strumień masy:
  \[
  \dot{m} = 0.07\ \text{kg/s}
  \]
- gęstość powietrza:
  \[
  \rho = 1.2\ \text{kg/m}^3
  \]

### Szukane
- `v1`
- `v2`

### Wzory
Najpierw korzystamy z zależności:

\[
\dot{m} = \rho \dot{V}
\]

stąd:

\[
\dot{V} = \frac{\dot{m}}{\rho}
\]

oraz:

\[
\dot{V} = A v
\]

więc:

\[
v = \frac{\dot{V}}{A}
\]

Pole przekroju kołowego:

\[
A = \frac{\pi D^2}{4}
\]

### Krok 1. Strumień objętości
\[
\dot{V} = \frac{0.07}{1.2} = 0.05833\ \text{m}^3/\text{s}
\]

### Krok 2. Pole przekroju 1
\[
A_1 = \frac{\pi \cdot 0.25^2}{4}
\]

\[
A_1 \approx 0.04909\ \text{m}^2
\]

### Krok 3. Pole przekroju 2
\[
A_2 = \frac{\pi \cdot 0.08^2}{4}
\]

\[
A_2 \approx 0.005027\ \text{m}^2
\]

### Krok 4. Prędkości
\[
v_1 = \frac{0.05833}{0.04909} \approx 1.19\ \text{m/s}
\]

\[
v_2 = \frac{0.05833}{0.005027} \approx 11.60\ \text{m/s}
\]

### Odpowiedź
\[
v_1 \approx 1.19\ \text{m/s}
\]

\[
v_2 \approx 11.60\ \text{m/s}
\]

### Jak myśleć
To jest klasyczne zadanie z **równania ciągłości przepływu**:
- ten sam strumień masy płynie przez oba przekroje,
- mniejszy przekrój → większa prędkość.

---

## 13. Przewód powietrzny z podgrzewaniem — obliczyć prędkości na dwóch odcinkach

### Dane
Odcinek 1:
- średnica:
  \[
  D = 0.1\ \text{m}
  \]
- temperatura:
  \[
  t_1 = 20^\circ C \Rightarrow T_1 = 293\ \text{K}
  \]
- ciśnienie bezwzględne:
  \[
  p_1 = 200\ \text{kPa} = 200000\ \text{Pa}
  \]

Odcinek 2:
- przekrój prostokątny:
  \[
  b = 0.07\ \text{m}, \quad h = 0.05\ \text{m}
  \]
- temperatura:
  \[
  t_2 = 80^\circ C \Rightarrow T_2 = 353\ \text{K}
  \]
- ciśnienie bezwzględne:
  \[
  p_2 = 150\ \text{kPa} = 150000\ \text{Pa}
  \]

Dodatkowo:
- strumień masy:
  \[
  \dot{m} = 2\ \text{kg/s}
  \]

### Szukane
- `v1`
- `v2`

### Krok 1. Gęstość powietrza z równania gazu doskonałego
Korzystamy ze wzoru:

\[
\rho = \frac{p}{R T}
\]

dla powietrza:
\[
R = 287\ \text{J/(kg·K)}
\]

#### Odcinek 1
\[
\rho_1 = \frac{200000}{287 \cdot 293}
\approx 2.38\ \text{kg/m}^3
\]

#### Odcinek 2
\[
\rho_2 = \frac{150000}{287 \cdot 353}
\approx 1.48\ \text{kg/m}^3
\]

### Krok 2. Pola przekrojów
#### Odcinek 1 — koło
\[
A_1 = \frac{\pi D^2}{4}
= \frac{\pi \cdot 0.1^2}{4}
\approx 0.007854\ \text{m}^2
\]

#### Odcinek 2 — prostokąt
\[
A_2 = b h = 0.07 \cdot 0.05 = 0.0035\ \text{m}^2
\]

### Krok 3. Korzystamy z zależności
\[
\dot{m} = \rho A v
\]

czyli:

\[
v = \frac{\dot{m}}{\rho A}
\]

#### Prędkość na odcinku 1
\[
v_1 = \frac{2}{2.38 \cdot 0.007854}
\approx 107.1\ \text{m/s}
\]

#### Prędkość na odcinku 2
\[
v_2 = \frac{2}{1.48 \cdot 0.0035}
\approx 386.1\ \text{m/s}
\]

### Odpowiedź
\[
v_1 \approx 107.1\ \text{m/s}
\]

\[
v_2 \approx 386.1\ \text{m/s}
\]

### Komentarz
Prędkość na drugim odcinku wyszła bardzo duża, bo:
- przekrój jest dużo mniejszy,
- gęstość jest mniejsza (wyższa temperatura i niższe ciśnienie).

### Schemat do takich zadań
1. Zamień temperatury na Kelwiny.
2. Oblicz gęstości z:
   \[
   \rho = \frac{p}{RT}
   \]
3. Oblicz pola przekrojów.
4. Użyj:
   \[
   v = \frac{\dot{m}}{\rho A}
   \]

---

## 14. Obliczyć prędkość przepływu powietrza na podstawie dwóch manometrów wodnych

### Dane
- temperatura powietrza:
  \[
  t = 20^\circ C
  \]
- pierwszy manometr:
  \[
  h_s = 16\ \text{mm} = 0.016\ \text{m}
  \]
- drugi manometr:
  \[
  h_c = 24\ \text{mm} = 0.024\ \text{m}
  \]

### Interpretacja
To typowe zadanie z rurką spiętrzającą / sondą Prandtla:
- `h_s` może oznaczać ciśnienie statyczne,
- `h_c` całkowite,
- różnica daje ciśnienie dynamiczne.

Zatem:

\[
\Delta h = h_c - h_s = 24 - 16 = 8\ \text{mm} = 0.008\ \text{m}
\]

### Krok 1. Ciśnienie dynamiczne
Ponieważ manometr jest wodny:

\[
p_d = \rho_w g \Delta h
\]

\[
p_d = 1000 \cdot 9.81 \cdot 0.008
= 78.48\ \text{Pa}
\]

### Krok 2. Równanie Bernoullego
Dla ciśnienia dynamicznego:

\[
p_d = \frac{\rho_p v^2}{2}
\]

stąd:

\[
v = \sqrt{\frac{2p_d}{\rho_p}}
\]

Dla powietrza przy `20^\circ C` przyjmujemy:
\[
\rho_p \approx 1.2\ \text{kg/m}^3
\]

### Krok 3. Obliczenie prędkości
\[
v = \sqrt{\frac{2 \cdot 78.48}{1.2}}
\]

\[
v = \sqrt{130.8} \approx 11.44\ \text{m/s}
\]

### Odpowiedź
\[
v \approx 11.4\ \text{m/s}
\]

### Jak rozpoznawać takie zadania
Jeśli masz:
- manometr statyczny,
- manometr całkowity,
to ich różnica daje **ciśnienie dynamiczne**:

\[
p_d = p_c - p_s
\]

a potem z Bernoulliego:

\[
v = \sqrt{\frac{2(p_c-p_s)}{\rho}}
\]

---

## 15. Wyznaczyć rozkład prędkości przepływającego powietrza w rurze o średnicy 160 mm

### Dane
- średnica rury:
  \[
  D = 160\ \text{mm} = 0.16\ \text{m}
  \]
- promień:
  \[
  R = 80\ \text{mm} = 0.08\ \text{m}
  \]
- temperatura:
  \[
  t = 20^\circ C
  \]
- nadciśnienie przed punktem pomiaru:
  \[
  \Delta p_1 = 50\ \text{Pa}
  \]
- ciśnienie barometryczne:
  \[
  p_{atm} = 746.3\ \text{mmHg}
  \]
- wilgotność względna:
  \[
  \varphi = 60\%
  \]

Tabela pomiarów:
| Punkt | r [mm] | pd [Pa] |
|---|---:|---:|
| 8g | 75.0 | 33.2 |
| 7g | 70.0 | 34.5 |
| 6g | 60.0 | 43.0 |
| 5g | 50.0 | 48.5 |
| 4g | 40.0 | 53.0 |
| 3g | 30.0 | 54.5 |
| 2g | 20.0 | 56.0 |
| 1g | 10.0 | 58.5 |
| oś | 0.0 | 60.5 |
| 1d | -10.0 | 59.5 |
| 2d | -20.0 | 58.0 |
| 3d | -30.0 | 55.0 |
| 4d | -40.0 | 52.5 |
| 5d | -50.0 | 48.5 |
| 6d | -60.0 | 39.0 |
| 7d | -70.0 | 35.0 |
| 8d | -75.0 | 34.3 |

### Cel
Dla każdego punktu trzeba policzyć lokalną prędkość z zależności:

\[
p_d = \frac{\rho v^2}{2}
\]

czyli:

\[
v(r) = \sqrt{\frac{2 p_d(r)}{\rho}}
\]

Najpierw trzeba wyznaczyć gęstość wilgotnego powietrza.

### Krok 1. Ciśnienie bezwzględne powietrza
Przeliczenie barometru:

\[
746.3\ \text{mmHg} \approx 99500\ \text{Pa}
\]

Dodajemy nadciśnienie:

\[
p \approx 99500 + 50 = 99550\ \text{Pa}
\]

### Krok 2. Gęstość wilgotnego powietrza
Dla `20^\circ C`:
- `T = 293.15 K`
- ciśnienie pary nasyconej wody:
  \[
  p_{sat} \approx 2338\ \text{Pa}
  \]
- przy wilgotności `60%`:
  \[
  p_v = 0.6 \cdot 2338 \approx 1403\ \text{Pa}
  \]

Ciśnienie suchego powietrza:
\[
p_a = 99550 - 1403 = 98147\ \text{Pa}
\]

Wzór:
\[
\rho = \frac{p_a}{R_a T} + \frac{p_v}{R_v T}
\]

gdzie:
- `R_a = 287 J/(kg·K)`
- `R_v = 461 J/(kg·K)`

Po podstawieniu:
\[
\rho \approx 1.18\ \text{kg/m}^3
\]

### Krok 3. Wzór roboczy
\[
v(r) = \sqrt{\frac{2p_d(r)}{1.18}}
\]

### Obliczenia
| Punkt | r [mm] | pd [Pa] | v [m/s] |
|---|---:|---:|---:|
| 8g | 75.0 | 33.2 | 7.50 |
| 7g | 70.0 | 34.5 | 7.65 |
| 6g | 60.0 | 43.0 | 8.54 |
| 5g | 50.0 | 48.5 | 9.07 |
| 4g | 40.0 | 53.0 | 9.48 |
| 3g | 30.0 | 54.5 | 9.61 |
| 2g | 20.0 | 56.0 | 9.74 |
| 1g | 10.0 | 58.5 | 9.96 |
| oś | 0.0 | 60.5 | 10.13 |
| 1d | -10.0 | 59.5 | 10.04 |
| 2d | -20.0 | 58.0 | 9.91 |
| 3d | -30.0 | 55.0 | 9.65 |
| 4d | -40.0 | 52.5 | 9.43 |
| 5d | -50.0 | 48.5 | 9.07 |
| 6d | -60.0 | 39.0 | 8.13 |
| 7d | -70.0 | 35.0 | 7.70 |
| 8d | -75.0 | 34.3 | 7.62 |

### Odpowiedź
Rozkład prędkości jest największy przy osi i maleje ku ściankom, co jest zgodne z fizyką przepływu w rurze.

### Jak zrobić to w Excelu
1. W kolumnie A wpisz `r [mm]`.
2. W kolumnie B wpisz `pd [Pa]`.
3. W komórce z gęstością wpisz `1.18`.
4. W kolumnie C wpisz wzór:
   ```excel
   =PIERWIASTEK(2*B2/1,18)

````md
### Jak zrobić to w Excelu
1. W kolumnie A wpisz `r [mm]`.
2. W kolumnie B wpisz `pd [Pa]`.
3. W komórce z gęstością wpisz `1.18`.
4. W kolumnie C wpisz wzór:
   ```excel
   =PIERWIASTEK(2*B2/1,18)
````

albo w angielskim Excelu:

```excel
=SQRT(2*B2/1.18)
```

5. Przeciągnij wzór w dół dla wszystkich punktów.
6. Zrób wykres `v(r)` jako wykres punktowy lub liniowy.

---

## 16. Wyznaczyć prędkość średnią metodą Log-Czebyszewa wg PN-ISO 5221

### Dane

* średnica rury: `D = 160 mm`
* promień rury: `R = 80 mm`
* ciśnienie barometryczne: `750 mmHg`
* wilgotność względna: `φ = 65%`
* temperatura powietrza: `t = 20°C`

Punkty pomiarowe dla `r/R`:

* `0.375`
* `0.825`
* `0.936`

Wartości pomiarów ciśnienia dynamicznego:

| Punkt  | `pd [Pa]` |
| ------ | --------: |
| 3g     |      35.5 |
| 2g     |      37.6 |
| 1g     |      43.5 |
| 0 - oś |      50.3 |
| 1d     |      45.5 |
| 2d     |      38.5 |
| 3d     |      35.9 |

### O co chodzi w tej metodzie

W metodzie Log-Czebyszewa mierzy się prędkość w kilku ściśle określonych punktach przekroju rury, a potem średnią prędkość liczy się jako średnią arytmetyczną prędkości lokalnych w tych punktach.

Najpierw z ciśnienia dynamicznego liczymy prędkość lokalną:

[
v_i = \sqrt{\frac{2p_{d,i}}{\rho}}
]

### Krok 1. Przyjęcie gęstości powietrza

Dla warunków:

* `t = 20°C`
* `p ≈ 750 mmHg`
* `φ = 65%`

można przyjąć w przybliżeniu:

[
\rho \approx 1.17\ \text{kg/m}^3
]

### Krok 2. Obliczenie prędkości w punktach pomiarowych

#### Punkt 3g

[
v_{3g} = \sqrt{\frac{2\cdot 35.5}{1.17}} \approx 7.79\ \text{m/s}
]

#### Punkt 2g

[
v_{2g} = \sqrt{\frac{2\cdot 37.6}{1.17}} \approx 8.02\ \text{m/s}
]

#### Punkt 1g

[
v_{1g} = \sqrt{\frac{2\cdot 43.5}{1.17}} \approx 8.62\ \text{m/s}
]

#### Oś

[
v_0 = \sqrt{\frac{2\cdot 50.3}{1.17}} \approx 9.27\ \text{m/s}
]

#### Punkt 1d

[
v_{1d} = \sqrt{\frac{2\cdot 45.5}{1.17}} \approx 8.82\ \text{m/s}
]

#### Punkt 2d

[
v_{2d} = \sqrt{\frac{2\cdot 38.5}{1.17}} \approx 8.11\ \text{m/s}
]

#### Punkt 3d

[
v_{3d} = \sqrt{\frac{2\cdot 35.9}{1.17}} \approx 7.84\ \text{m/s}
]

### Krok 3. Obliczenie prędkości średniej

[
v_{śr} = \frac{v_{3g}+v_{2g}+v_{1g}+v_0+v_{1d}+v_{2d}+v_{3d}}{7}
]

[
v_{śr} = \frac{7.79+8.02+8.62+9.27+8.82+8.11+7.84}{7}
]

[
v_{śr} \approx 8.35\ \text{m/s}
]

### Odpowiedź

[
v_{śr} \approx 8.35\ \text{m/s}
]

### Jak to robić na egzaminie

1. Zapisz wzór:
   [
   v_i = \sqrt{\frac{2p_{d,i}}{\rho}}
   ]
2. Oblicz każdą prędkość lokalną.
3. Zrób średnią arytmetyczną z tych prędkości.
4. To jest wynik końcowy.

### Jak zrobić to w Excelu

W kolumnach możesz wpisać:

* kolumna A: punkt
* kolumna B: `pd [Pa]`
* kolumna C: `v [m/s]`

Wzór w Excelu:

```excel
=PIERWIASTEK(2*B2/1,17)
```

Średnia:

```excel
=ŚREDNIA(C2:C8)
```

W angielskim Excelu:

```excel
=SQRT(2*B2/1.17)
```

oraz:

```excel
=AVERAGE(C2:C8)
```

---

## 17. Woda do celów grzewczych o temperaturze 90°C płynie rurociągiem z prędkością `v = 0.0034 m/s`. Przy jakiej średnicy przewodu zaczyna się przepływ turbulentny?

### Dane

* prędkość:
  [
  v = 0.0034\ \text{m/s}
  ]
* lepkość kinematyczna:
  [
  \nu = 0.296 \cdot 10^{-6}\ \text{m}^2/\text{s}
  ]

### Szukane

* średnica graniczna `D`

### Teoria

Warunek początku przepływu turbulentnego w rurze wyznaczamy z liczby Reynoldsa:

[
Re = \frac{vD}{\nu}
]

Dla przepływu w rurze granica przejścia z laminarnego do turbulentnego jest przyjmowana jako:

[
Re_{kr} \approx 2300
]

Na granicy:
[
2300 = \frac{vD}{\nu}
]

stąd:
[
D = \frac{2300\nu}{v}
]

### Obliczenia

[
D = \frac{2300 \cdot 0.296\cdot 10^{-6}}{0.0034}
]

[
D \approx 0.200\ \text{m}
]

### Odpowiedź

[
D \approx 0.20\ \text{m} = 200\ \text{mm}
]

### Interpretacja

* dla średnic mniejszych niż `200 mm` przepływ będzie laminarny,
* dla średnicy około `200 mm` zaczyna się obszar przejściowy,
* dla większych średnic łatwiej osiągnąć turbulencję.

### Schemat do zapamiętania

Jeżeli pytają: „przy jakiej średnicy zaczyna się turbulencja?”, to:

1. bierzesz:
   [
   Re_{kr} = 2300
   ]
2. korzystasz z:
   [
   Re = \frac{vD}{\nu}
   ]
3. wyznaczasz:
   [
   D = \frac{Re_{kr}\nu}{v}
   ]

---

## 18. Wyznaczyć rozkład prędkości `v(r)` powietrza w rurze o średnicy `D = 160 mm`. Objętościowe natężenie przepływu wynosi `V̇ = 1.9311·10^-4 m^3/s`. W jakiej odległości `r` od osi prędkość jest równa prędkości średniej?

### Dane

* średnica rury:
  [
  D = 160\ \text{mm} = 0.16\ \text{m}
  ]
* promień:
  [
  R = \frac{D}{2} = 0.08\ \text{m}
  ]
* objętościowe natężenie przepływu:
  [
  \dot{V} = 1.9311 \cdot 10^{-4}\ \text{m}^3/\text{s}
  ]

### Założenie

To zadanie standardowo rozwiązuje się przy założeniu przepływu laminarnego w rurze kołowej.

Dla przepływu laminarnego profil prędkości ma postać paraboliczną:

[
v(r) = v_{max}\left(1-\frac{r^2}{R^2}\right)
]

oraz:
[
v_{max} = 2v_{śr}
]

### Krok 1. Obliczenie pola przekroju

[
A = \frac{\pi D^2}{4}
]

[
A = \frac{\pi \cdot 0.16^2}{4} \approx 0.02011\ \text{m}^2
]

### Krok 2. Obliczenie prędkości średniej

[
v_{śr} = \frac{\dot{V}}{A}
]

[
v_{śr} = \frac{1.9311\cdot10^{-4}}{0.02011} \approx 0.00960\ \text{m/s}
]

### Krok 3. Obliczenie prędkości maksymalnej

[
v_{max} = 2v_{śr} = 2 \cdot 0.00960 = 0.0192\ \text{m/s}
]

### Krok 4. Rozkład prędkości

Podstawiamy do wzoru parabolicznego:

[
v(r) = 0.0192\left(1-\frac{r^2}{0.08^2}\right)
]

To jest szukany rozkład prędkości.

### Krok 5. Gdzie prędkość lokalna jest równa średniej?

Szukamy takiego `r`, że:

[
v(r) = v_{śr}
]

czyli:

[
0.0192\left(1-\frac{r^2}{0.08^2}\right)=0.00960
]

Dzielimy stronami przez `0.0192`:

[
1-\frac{r^2}{0.08^2}=0.5
]

[
\frac{r^2}{0.08^2}=0.5
]

[
r^2=0.5\cdot 0.08^2
]

[
r=0.08\sqrt{0.5}
]

[
r \approx 0.0566\ \text{m}
]

### Odpowiedź

Rozkład prędkości:
[
v(r) = 0.0192\left(1-\frac{r^2}{0.08^2}\right)\ \text{m/s}
]

Odległość od osi, dla której:
[
v(r)=v_{śr}
]
wynosi:
[
r \approx 0.0566\ \text{m} = 56.6\ \text{mm}
]

### Jak to rozwiązywać zawsze

Jeśli masz przepływ laminarny w rurze:

1. liczysz:
   [
   v_{śr}=\frac{\dot{V}}{A}
   ]
2. potem:
   [
   v_{max}=2v_{śr}
   ]
3. wpisujesz do:
   [
   v(r)=v_{max}\left(1-\frac{r^2}{R^2}\right)
   ]
4. jeśli pytają, gdzie `v(r)=vśr`, to podstawiasz i rozwiązujesz równanie.

### Excel

W komórce z promieniem wpisz `0.08`, a w kolumnie z `r` podawaj wartości w metrach.

Wzór:

```excel
=0,0192*(1-(A2^2)/(0,08^2))
```

W angielskim Excelu:

```excel
=0.0192*(1-(A2^2)/(0.08^2))
```

---

## 19. Wyznaczyć rozkład prędkości `v(r)` powietrza w rurze o średnicy `D = 160 mm`, dla parametrów z zadań 15 i 16. W jakiej odległości `r` od osi prędkość jest równa prędkości średniej?

### O co chodzi

Tutaj trzeba połączyć wyniki z dwóch poprzednich zadań:

* z zadania 15 mamy lokalny rozkład ciśnienia dynamicznego `pd(r)` i z niego lokalne prędkości `v(r)`,
* z zadania 16 mamy prędkość średnią `vśr`.

Czyli:

1. liczysz albo bierzesz z zadania 15 wartości `v(r)`,
2. bierzesz z zadania 16 wartość `vśr`,
3. sprawdzasz, dla którego `r` zachodzi:
   [
   v(r) = v_{śr}
   ]

### Dane z zadania 15

Prędkości lokalne były w przybliżeniu:

| `r [mm]` | `v(r) [m/s]` |
| -------: | -----------: |
|       75 |         7.50 |
|       70 |         7.65 |
|       60 |         8.54 |
|       50 |         9.07 |
|       40 |         9.48 |
|       30 |         9.61 |
|       20 |         9.74 |
|       10 |         9.96 |
|        0 |        10.13 |
|      -10 |        10.04 |
|      -20 |         9.91 |
|      -30 |         9.65 |
|      -40 |         9.43 |
|      -50 |         9.07 |
|      -60 |         8.13 |
|      -70 |         7.70 |
|      -75 |         7.62 |

### Dane z zadania 16

[
v_{śr} \approx 8.35\ \text{m/s}
]

### Szukamy miejsca, gdzie

[
v(r)=8.35\ \text{m/s}
]

Patrzymy w tabelę:

* dla `r = 60 mm`, `v = 8.54 m/s`
* dla `r = 70 mm`, `v = 7.65 m/s`

Zatem punkt, gdzie `v = 8.35 m/s`, leży pomiędzy `60 mm` a `70 mm`.

### Interpolacja liniowa

Bierzemy punkty:

* `(60,\ 8.54)`
* `(70,\ 7.65)`

Szukamy `r` dla `v = 8.35`.

Wzór interpolacyjny:
[
r = r_1 + \frac{v-v_1}{v_2-v_1}(r_2-r_1)
]

Podstawiamy:
[
r = 60 + \frac{8.35-8.54}{7.65-8.54}\cdot(70-60)
]

[
r = 60 + \frac{-0.19}{-0.89}\cdot 10
]

[
r \approx 60 + 2.13 = 62.1\ \text{mm}
]

Ze względu na symetrię przekroju otrzymujemy dwa punkty:
[
r \approx \pm 62\ \text{mm}
]

### Odpowiedź

Prędkość równa średniej występuje w przybliżeniu w odległości:
[
r \approx 62\ \text{mm}
]
od osi rury, po obu stronach przekroju.

### Jak to zrobić w Excelu

1. W jednej kolumnie wpisz `r`.
2. W drugiej wpisz `v(r)`.
3. Obok wpisz wartość `vśr = 8.35`.
4. Znajdź dwa sąsiednie punkty, między którymi `v(r)` przechodzi przez `8.35`.
5. Użyj interpolacji liniowej.

Przykładowo:

```excel
=60+((8,35-8,54)/(7,65-8,54))*(70-60)
```

W angielskim Excelu:

```excel
=60+((8.35-8.54)/(7.65-8.54))*(70-60)
```

---

## 20. Przez przewód z poziomym kolankiem przepływa woda. Spadek ciśnienia wynosił `Δp = 10 Pa`. Średnica przewodu `d = 30 mm`, natężenie przepływu `V̇ = 1.5 dm^3/s`. Obliczyć współczynnik straty lokalnej kolanka.

### Dane

* spadek ciśnienia:
  [
  \Delta p = 10\ \text{Pa}
  ]
* średnica:
  [
  d = 30\ \text{mm} = 0.03\ \text{m}
  ]
* natężenie przepływu:
  [
  \dot{V} = 1.5\ \text{dm}^3/\text{s} = 1.5\cdot 10^{-3}\ \text{m}^3/\text{s}
  ]
* gęstość wody:
  [
  \rho = 1000\ \text{kg/m}^3
  ]

### Szukane

* współczynnik straty lokalnej `ζ`

### Teoria

Dla strat miejscowych:
[
\Delta p = \zeta \frac{\rho v^2}{2}
]

Stąd:
[
\zeta = \frac{2\Delta p}{\rho v^2}
]

Najpierw trzeba obliczyć prędkość przepływu.

### Krok 1. Pole przekroju

[
A=\frac{\pi d^2}{4}
]

[
A=\frac{\pi \cdot 0.03^2}{4} \approx 7.07\cdot 10^{-4}\ \text{m}^2
]

### Krok 2. Prędkość

[
v=\frac{\dot{V}}{A}
]

[
v=\frac{1.5\cdot10^{-3}}{7.07\cdot10^{-4}} \approx 2.12\ \text{m/s}
]

### Krok 3. Współczynnik straty lokalnej

[
\zeta=\frac{2\cdot 10}{1000\cdot (2.12)^2}
]

[
\zeta \approx \frac{20}{4494} \approx 0.00445
]

### Odpowiedź

[
\zeta \approx 0.0045
]

### Uwaga

Wynik jest bardzo mały jak na typowe kolanko, więc możliwe, że w danych jest bardzo mały spadek ciśnienia albo to wynik czysto ćwiczeniowy. Matematycznie obliczenie jest poprawne.

### Schemat

1. liczysz prędkość z:
   [
   v=\frac{\dot{V}}{A}
   ]
2. podstawiasz do:
   [
   \Delta p=\zeta \frac{\rho v^2}{2}
   ]
3. wyznaczasz `ζ`.

---

## 21. W poziomym przewodzie o średnicy `d = 25 mm` zmierzono ciśnienie w dwóch przekrojach odległych o `L = 8 m`. Spadek ciśnienia wynosił `Δp = 2 Pa`. Obliczyć współczynnik strat na tarcie `λ`, jeśli prędkość wody w przewodzie `v = 1.5 m/s`.

### Dane

* średnica:
  [
  d = 25\ \text{mm} = 0.025\ \text{m}
  ]
* długość przewodu:
  [
  L = 8\ \text{m}
  ]
* spadek ciśnienia:
  [
  \Delta p = 2\ \text{Pa}
  ]
* prędkość:
  [
  v = 1.5\ \text{m/s}
  ]
* gęstość wody:
  [
  \rho = 1000\ \text{kg/m}^3
  ]

### Szukane

* współczynnik strat na tarcie `λ`

### Teoria

Dla strat liniowych w przewodzie prostym obowiązuje wzór Darcy’ego-Weisbacha:

[
\Delta p = \lambda \frac{L}{d}\frac{\rho v^2}{2}
]

Stąd:
[
\lambda = \frac{2\Delta p, d}{L\rho v^2}
]

### Obliczenia

[
\lambda = \frac{2\cdot 2 \cdot 0.025}{8\cdot 1000 \cdot 1.5^2}
]

[
\lambda = \frac{0.1}{18000}
]

[
\lambda \approx 5.56\cdot 10^{-6}
]

### Odpowiedź

[
\lambda \approx 5.6 \cdot 10^{-6}
]

### Uwaga

To również jest bardzo mała wartość jak na rzeczywisty przepływ wody w przewodzie, więc najpewniej dane są ćwiczeniowe albo w spadku ciśnienia powinno być coś większego. Sam tok obliczeń jest poprawny.

### Jak rozpoznawać

Jeśli masz:

* długość przewodu,
* średnicę,
* spadek ciśnienia,
* prędkość,

to prawie na pewno używasz:
[
\Delta p = \lambda \frac{L}{d}\frac{\rho v^2}{2}
]

---

## 22. Wyznaczyć wartość współczynnika strat miejscowych oraz współczynnika strat na tarcie dla danych pomiarowych z tabeli

### Uwaga

To zadanie jest bezpośrednio związane z tabelą podaną poniżej i w praktyce łączy się z zadaniem 23. Z tabeli odczytujemy spadki nadciśnienia pomiędzy kolejnymi punktami pomiarowymi dla:

* elementów miejscowych, np. kolan,
* odcinka prostego przewodu.

### Dane z tabeli

| L.p. | Nazwa                | Wielkość charakterystyczna | Nr punktu 1 | `Δp1 [Pa]` | Nr punktu 2 | `Δp2 [Pa]` |
| ---- | -------------------- | -------------------------- | ----------: | ---------: | ----------: | ---------: |
| 1    | 2 x Kolano 45° R 0.2 | —                          |           1 |        220 |           2 |        213 |
| 2    | Odcinek 1            | `L = 5.82 m`               |           2 |        213 |           3 |        200 |
| 3    | 2 x Kolano 90° R 0.5 | —                          |           3 |        200 |           4 |        194 |
| 4    | Kolano 90° R 0.2     | —                          |           8 |        110 |           9 |        103 |

### Krok 1. Spadki ciśnienia na elementach

#### Dwa kolana 45°

[
\Delta p = 220 - 213 = 7\ \text{Pa}
]

#### Odcinek prosty

[
\Delta p = 213 - 200 = 13\ \text{Pa}
]

#### Dwa kolana 90°

[
\Delta p = 200 - 194 = 6\ \text{Pa}
]

#### Jedno kolano 90°

[
\Delta p = 110 - 103 = 7\ \text{Pa}
]

### Co dalej?

Żeby policzyć:

* współczynnik straty miejscowej `ζ`,
* współczynnik tarcia `λ`,

trzeba jeszcze znać:

* średnicę przewodu `d`,
* prędkość przepływu `v`,
* gęstość płynu `ρ`.

Bez tych danych można rozpisać wzory i policzyć same spadki ciśnienia, ale nie uzyska się liczbowych wartości `ζ` i `λ`.

### Wzory

#### Dla strat miejscowych

[
\zeta = \frac{2\Delta p}{\rho v^2}
]

Jeżeli dany element występuje dwa razy, to współczynnik pojedynczego elementu:
[
\zeta_{1\ elementu} = \frac{1}{2}\cdot \frac{2\Delta p}{\rho v^2}
= \frac{\Delta p}{\rho v^2}
]

#### Dla strat liniowych

[
\lambda = \frac{2\Delta p, d}{L\rho v^2}
]

### Wynik ogólny

* dla `2 × kolano 45°`:
  [
  \zeta_{2\times45} = \frac{2\cdot 7}{\rho v^2}
  ]

* dla jednego kolana `45°`:
  [
  \zeta_{45} = \frac{7}{\rho v^2}
  ]

* dla `2 × kolano 90°`:
  [
  \zeta_{2\times90} = \frac{2\cdot 6}{\rho v^2}
  ]

* dla jednego kolana `90°` w tym układzie:
  [
  \zeta_{90} = \frac{6}{\rho v^2}
  ]

* dla pojedynczego kolana `90° R=0.2`:
  [
  \zeta = \frac{2\cdot 7}{\rho v^2}
  ]

* dla odcinka prostego:
  [
  \lambda = \frac{2\cdot 13 \cdot d}{5.82\cdot \rho v^2}
  ]

### Odpowiedź

Z samych danych tabelarycznych można wyznaczyć:

* spadki ciśnienia na elementach,
* wzory na `ζ` i `λ`.

Do obliczenia wartości liczbowych potrzebne są jeszcze `ρ`, `v` i `d`.

### Excel

Jeżeli masz `ρ`, `v`, `d` w osobnych komórkach, to np. dla strat miejscowych:

```excel
=2*7/(rho*v^2)
```

a dla strat liniowych:

```excel
=2*13*d/(5,82*rho*v^2)
```

---

## 23. Tabela pomiarowa — interpretacja i sposób liczenia

### Tabela

| L.p. | Nazwa                       | Wielkość charakterystyczna | Nr punktu pomiarowego | Wartość nadciśnienia `Δpn` |
| ---- | --------------------------- | -------------------------- | --------------------: | -------------------------: |
| 1    | 2 × Kolano `45°`, `R = 0.2` | —                          |                     1 |                        220 |
|      |                             |                            |                     2 |                        213 |
| 2    | Odcinek 1                   | `L = 5.82`                 |                     2 |                        213 |
|      |                             |                            |                     3 |                        200 |
| 3    | 2 × Kolano `90°`, `R = 0.5` | —                          |                     3 |                        200 |
|      |                             |                            |                     4 |                        194 |
| 4    | Kolano `90°`, `R = 0.2`     | —                          |                     8 |                        110 |
|      |                             |                            |                     9 |                        103 |

### Jak to interpretować

Każdy element instalacji ma przypisane dwa punkty pomiarowe. Różnica nadciśnień między tymi punktami to strata ciśnienia na tym elemencie:

[
\Delta p = \Delta p_{n,,wejście} - \Delta p_{n,,wyjście}
]

### Obliczenia spadków

#### Element 1: 2 × kolano 45°

[
\Delta p_1 = 220 - 213 = 7\ \text{Pa}
]

#### Element 2: odcinek prosty

[
\Delta p_2 = 213 - 200 = 13\ \text{Pa}
]

#### Element 3: 2 × kolano 90°

[
\Delta p_3 = 200 - 194 = 6\ \text{Pa}
]

#### Element 4: kolano 90°

[
\Delta p_4 = 110 - 103 = 7\ \text{Pa}
]

### Jak z tego liczyć współczynniki

#### Dla elementu miejscowego

[
\zeta = \frac{\Delta p}{\frac{\rho v^2}{2}}
= \frac{2\Delta p}{\rho v^2}
]

#### Dla przewodu prostego

[
\lambda = \frac{\Delta p}{\frac{L}{d}\frac{\rho v^2}{2}}
= \frac{2\Delta p d}{L\rho v^2}
]

### Gdy elementów są dwa takie same

Jeżeli spadek `Δp` dotyczy dwóch identycznych kolan, to współczynnik jednego wynosi połowę współczynnika całego zestawu.

Przykład:
[
\zeta_{2,kolan} = \frac{2\Delta p}{\rho v^2}
]

a dla jednego kolana:
[
\zeta_{1,kolana} = \frac{1}{2}\zeta_{2,kolan}
]

### Co trzeba mieć, żeby dokończyć zadanie liczbowo

Potrzebne są jeszcze:

* `ρ`
* `v`
* `d`

Bez tych danych można poprawnie policzyć tylko same spadki ciśnienia i przygotować wzory końcowe.

### Jak to zrobić w Excelu

Załóżmy:

* `B2` — ciśnienie przed elementem,
* `C2` — ciśnienie za elementem,
* `F1` — gęstość `ρ`,
* `F2` — prędkość `v`,
* `F3` — średnica `d`,
* `F4` — długość `L`.

Spadek ciśnienia:

```excel
=B2-C2
```

Współczynnik straty miejscowej:

```excel
=2*(B2-C2)/($F$1*$F$2^2)
```

Współczynnik strat liniowych:

```excel
=2*(B2-C2)*$F$3/($F$4*$F$1*$F$2^2)
```

---

## Podsumowanie najważniejszych wzorów z zadań 11–23

### 1. Manometr różnicowy

[
p_1-p_2 = (\rho_m-\rho_g)gh
]

dla gazu i cieczy ciężkiej zwykle:
[
p_1-p_2 \approx \rho_m gh
]

### 2. Równanie ciągłości

[
\dot{m}=\rho A v
]

[
\dot{V}=A v
]

### 3. Pole przekroju

Koło:
[
A=\frac{\pi D^2}{4}
]

Prostokąt:
[
A=b h
]

### 4. Gaz doskonały

[
\rho=\frac{p}{RT}
]

### 5. Prędkość z ciśnienia dynamicznego

[
p_d=\frac{\rho v^2}{2}
]

[
v=\sqrt{\frac{2p_d}{\rho}}
]

### 6. Liczba Reynoldsa

[
Re=\frac{vD}{\nu}
]

### 7. Granica turbulencji

[
Re_{kr}\approx 2300
]

### 8. Profil laminarny w rurze

[
v(r)=v_{max}\left(1-\frac{r^2}{R^2}\right)
]

[
v_{max}=2v_{śr}
]

### 9. Straty miejscowe

[
\Delta p = \zeta \frac{\rho v^2}{2}
]

[
\zeta=\frac{2\Delta p}{\rho v^2}
]

### 10. Straty liniowe

[
\Delta p=\lambda \frac{L}{d}\frac{\rho v^2}{2}
]

[
\lambda=\frac{2\Delta p d}{L\rho v^2}
]

---

## Jak uczyć się rozwiązywania takich zadań

Najlepsza kolejność myślenia:

1. **Rozpoznaj temat zadania**

   * manometr,
   * równanie ciągłości,
   * Bernoulli,
   * Reynolds,
   * profil prędkości,
   * straty ciśnienia.

2. **Wypisz dane w SI**

   * mm na m,
   * hPa na Pa,
   * °C na K, jeśli trzeba,
   * dm³/s na m³/s.

3. **Dobierz wzór główny**

   * manometr:
     [
     \Delta p=\rho gh
     ]
   * przepływ:
     [
     \dot{m}=\rho A v
     ]
   * sonda Prandtla:
     [
     v=\sqrt{\frac{2p_d}{\rho}}
     ]
   * straty:
     [
     \Delta p=\zeta\frac{\rho v^2}{2}
     \quad \text{lub} \quad
     \Delta p=\lambda\frac{L}{d}\frac{\rho v^2}{2}
     ]

4. **Policz krok po kroku**

   * najpierw wielkości pomocnicze,
   * potem wynik końcowy.

5. **Sprawdź fizycznie wynik**

   * mniejszy przekrój powinien dawać większą prędkość,
   * przy osi rury prędkość jest największa,
   * współczynniki strat nie powinny wychodzić ujemne,
   * ciśnienie powinno spadać zgodnie z przepływem.

---

## Co warto umieć na pamięć

* `A = πD²/4`
* `ṁ = ρAv`
* `v = √(2pd/ρ)`
* `Re = vD/ν`
* `Δp = ζρv²/2`
* `Δp = λ(L/d)ρv²/2`
* dla przepływu laminarnego:
  [
  v_{max}=2v_{śr}
  ]

---

## Uwaga końcowa

W zadaniach 20–23 część wyników liczbowych wychodzi nietypowo mała. To nie oznacza błędu rachunkowego — po prostu takie są dane wejściowe. Na kolokwium najważniejsze jest:

* poprawne rozpoznanie modelu,
* dobry wzór,
* poprawne jednostki,
* logiczny tok liczenia.

```
```
