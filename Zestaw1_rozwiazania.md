# Zestaw 1 – Rozwiązania

---

## Zadanie 1 – Rzuty wektorów na oś x

Dane:
- $a_1 = 3$, $\alpha_1 = \pi/6$
- $a_2 = 2$, $\alpha_2 = 2\pi/3$
- $a_3 = 4$, $\alpha_3 = \pi/6$

Rzut wektora na oś x: $a_x = a \cdot \cos\alpha$

### a) Wektor $\vec{a_1}$
$$a_{1x} = a_1 \cdot \cos\alpha_1 = 3 \cdot \cos\frac{\pi}{6} = 3 \cdot \frac{\sqrt{3}}{2} = \frac{3\sqrt{3}}{2} \approx 2{,}60$$

### b) Wektor $\vec{a_2}$
Kąt $\alpha_2 = 2\pi/3 = 120°$ – wektor skierowany w II ćwiartce (powyżej osi x, w lewo względem y), ale patrząc na rysunek b), kąt jest mierzony od osi x do wektora **w kierunku przeciwnym do ruchu wskazówek zegara po stronie lewej**, co oznacza że składowa x jest ujemna:
$$a_{2x} = a_2 \cdot \cos\alpha_2 = 2 \cdot \cos\frac{2\pi}{3} = 2 \cdot \left(-\frac{1}{2}\right) = -1$$

### c) Wektor $\vec{a_3}$
Z rysunku c) wektor $\vec{a_3}$ jest skierowany **powyżej osi x** w II ćwiartce (kąt $\alpha_3 = \pi/6$ mierzony od ujemnej osi x), zatem:
$$a_{3x} = -a_3 \cdot \cos\alpha_3 = -4 \cdot \cos\frac{\pi}{6} = -4 \cdot \frac{\sqrt{3}}{2} = -2\sqrt{3} \approx -3{,}46$$

**Wyniki:**
| Wektor | Rzut na oś x |
|--------|-------------|
| $\vec{a_1}$ | $+\frac{3\sqrt{3}}{2} \approx +2{,}60$ |
| $\vec{a_2}$ | $-1$ |
| $\vec{a_3}$ | $-2\sqrt{3} \approx -3{,}46$ |

---

## Zadanie 2 – Iloczyn skalarny i wektorowy

Dane:
$$\vec{a} = 3\vec{i} + 2\vec{j} + 0\vec{k}, \quad \vec{b} = 2\vec{i} + 3\vec{j} + 0\vec{k}$$

### Iloczyn skalarny
$$\vec{a} \cdot \vec{b} = a_x b_x + a_y b_y + a_z b_z = 3 \cdot 2 + 2 \cdot 3 + 0 \cdot 0 = 6 + 6 + 0 = \boxed{12}$$

### Iloczyn wektorowy $\vec{d} = \vec{a} \times \vec{b}$

$$\vec{d} = \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\ 3 & 2 & 0 \\ 2 & 3 & 0 \end{vmatrix}$$

$$d_x = (2 \cdot 0 - 0 \cdot 3) = 0$$
$$d_y = -(3 \cdot 0 - 0 \cdot 2) = 0$$
$$d_z = (3 \cdot 3 - 2 \cdot 2) = 9 - 4 = 5$$

$$\boxed{\vec{d} = 5\vec{k}}$$

Wektor $\vec{d}$ jest prostopadły do płaszczyzny xy i skierowany zgodnie z osią z.

---

## Zadanie 3 – Iloczyn skalarny i wektorowy w przestrzeni 3D

Dane:
- $a = 3$, $\alpha_1 = \pi/6$, $\beta_1 = \pi/2$, $\gamma_1 = \pi/3$
- $b = 2$, $\alpha_2 = \pi/6$, $\beta_2 = \pi/3$, $\gamma_2 = \pi/2$

### Składowe wektorów

Składowe przez kąty kierunkowe: $v_x = v\cos\alpha$, $v_y = v\cos\beta$, $v_z = v\cos\gamma$

**Wektor $\vec{a}$:**
$$a_x = 3\cos\frac{\pi}{6} = 3 \cdot \frac{\sqrt{3}}{2} = \frac{3\sqrt{3}}{2}$$
$$a_y = 3\cos\frac{\pi}{2} = 0$$
$$a_z = 3\cos\frac{\pi}{3} = 3 \cdot \frac{1}{2} = \frac{3}{2}$$

$$\vec{a} = \frac{3\sqrt{3}}{2}\vec{i} + 0\vec{j} + \frac{3}{2}\vec{k}$$

**Wektor $\vec{b}$:**
$$b_x = 2\cos\frac{\pi}{6} = 2 \cdot \frac{\sqrt{3}}{2} = \sqrt{3}$$
$$b_y = 2\cos\frac{\pi}{3} = 2 \cdot \frac{1}{2} = 1$$
$$b_z = 2\cos\frac{\pi}{2} = 0$$

$$\vec{b} = \sqrt{3}\vec{i} + 1\vec{j} + 0\vec{k}$$

### Iloczyn skalarny
$$\vec{a} \cdot \vec{b} = \frac{3\sqrt{3}}{2} \cdot \sqrt{3} + 0 \cdot 1 + \frac{3}{2} \cdot 0 = \frac{3 \cdot 3}{2} = \frac{9}{2} = 4{,}5$$

$$\boxed{\vec{a} \cdot \vec{b} = 4{,}5}$$

### Iloczyn wektorowy $\vec{d} = \vec{a} \times \vec{b}$

$$\vec{d} = \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\ \frac{3\sqrt{3}}{2} & 0 & \frac{3}{2} \\ \sqrt{3} & 1 & 0 \end{vmatrix}$$

$$d_x = 0 \cdot 0 - \frac{3}{2} \cdot 1 = -\frac{3}{2}$$
$$d_y = -\left(\frac{3\sqrt{3}}{2} \cdot 0 - \frac{3}{2} \cdot \sqrt{3}\right) = -\left(-\frac{3\sqrt{3}}{2}\right) = \frac{3\sqrt{3}}{2}$$
$$d_z = \frac{3\sqrt{3}}{2} \cdot 1 - 0 \cdot \sqrt{3} = \frac{3\sqrt{3}}{2}$$

$$\boxed{\vec{d} = -\frac{3}{2}\vec{i} + \frac{3\sqrt{3}}{2}\vec{j} + \frac{3\sqrt{3}}{2}\vec{k}}$$

### Cosinusy kierunkowe $\vec{d}$

$$|\vec{d}| = \sqrt{\left(\frac{3}{2}\right)^2 + \left(\frac{3\sqrt{3}}{2}\right)^2 + \left(\frac{3\sqrt{3}}{2}\right)^2} = \sqrt{\frac{9}{4} + \frac{27}{4} + \frac{27}{4}} = \sqrt{\frac{63}{4}} = \frac{3\sqrt{7}}{2}$$

$$\cos\alpha_d = \frac{-3/2}{3\sqrt{7}/2} = \frac{-1}{\sqrt{7}} \approx -0{,}378$$
$$\cos\beta_d = \frac{3\sqrt{3}/2}{3\sqrt{7}/2} = \frac{\sqrt{3}}{\sqrt{7}} \approx 0{,}655$$
$$\cos\gamma_d = \frac{3\sqrt{3}/2}{3\sqrt{7}/2} = \frac{\sqrt{3}}{\sqrt{7}} \approx 0{,}655$$

---

## Zadanie 4 – Moment siły P względem punktu O

Dane:
- Punkt A: $x_A = 3$ m, $y_A = 2$ m
- Siła: $P = 100$ N, $\alpha = 60°$

### Składowe siły

$$P_x = P\cos\alpha = 100 \cdot \cos 60° = 100 \cdot 0{,}5 = 50 \text{ N}$$
$$P_y = P\sin\alpha = 100 \cdot \sin 60° = 100 \cdot \frac{\sqrt{3}}{2} \approx 86{,}6 \text{ N}$$

### Moment siły – algebraiczne dodawanie momentów składowych

Moment siły względem punktu O:
$$M_O = M_{O}(P_x) + M_{O}(P_y)$$

Moment składowej $P_x$ (ramię = $y_A = 2$ m, obrót zgodnie ze wskazówkami zegara → ujemny):
$$M_O(P_x) = -P_x \cdot y_A = -50 \cdot 2 = -100 \text{ N·m}$$

Moment składowej $P_y$ (ramię = $x_A = 3$ m, obrót przeciwnie do wskazówek zegara → dodatni):
$$M_O(P_y) = +P_y \cdot x_A = 86{,}6 \cdot 3 = 259{,}8 \text{ N·m}$$

$$\boxed{M_O = -100 + 259{,}8 = 159{,}8 \text{ N·m}}$$

Moment jest dodatni – obrót **przeciwnie do ruchu wskazówek zegara**.

---

## Zadanie 5 – Moment siły P względem punktu O

Dane:
- Punkt A: $x_A = -3$ m, $y_A = 4$ m
- Siła: $P = 200$ N, $\alpha = 210°$

### Składowe siły (wzory redukcyjne)

$\alpha = 210° = 180° + 30°$, zatem:
$$P_x = P\cos 210° = -P\cos 30° = -200 \cdot \frac{\sqrt{3}}{2} = -100\sqrt{3} \approx -173{,}2 \text{ N}$$
$$P_y = P\sin 210° = -P\sin 30° = -200 \cdot 0{,}5 = -100 \text{ N}$$

### Postać wektorowa

$$\vec{r}_A = -3\vec{i} + 4\vec{j} \text{ (m)}$$
$$\vec{P} = -100\sqrt{3}\,\vec{i} - 100\vec{j} \text{ (N)}$$

### Metoda 1: Dodawanie algebraiczne momentów

$$M_O(P_x) = -P_x \cdot y_A = -(-173{,}2) \cdot 4 = +692{,}8 \text{ N·m}$$
$$M_O(P_y) = +P_y \cdot x_A = (-100) \cdot (-3) = +300 \text{ N·m}$$

$$\boxed{M_O = 692{,}8 + 300 = 992{,}8 \approx 993 \text{ N·m}}$$

### Metoda 2: Iloczyn wektorowy $\vec{M}_O = \vec{r}_A \times \vec{P}$

$$\vec{M}_O = \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\ -3 & 4 & 0 \\ -100\sqrt{3} & -100 & 0 \end{vmatrix}$$

$$M_z = (-3)(-100) - (4)(-100\sqrt{3}) = 300 + 400\sqrt{3} \approx 300 + 692{,}8 = 992{,}8 \text{ N·m}$$

$$\boxed{\vec{M}_O \approx 992{,}8\,\vec{k} \text{ N·m}}$$

Obie metody dają zgodny wynik ✓

---

## Zadanie 6 – Moment siły względem punktu O i punktu B

Dane:
$$\vec{P} = -4\vec{i} + 5\vec{j} - 4\vec{k} \text{ (N)}$$
$$\vec{r}_A = 4\vec{i} + 0\vec{j} + 4\vec{k} \text{ (m)}$$
Punkt B: $(4, 5, 4)$

### Moment względem O

$$\vec{M}_O = \vec{r}_A \times \vec{P} = \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\ 4 & 0 & 4 \\ -4 & 5 & -4 \end{vmatrix}$$

$$M_x = 0 \cdot (-4) - 4 \cdot 5 = -20$$
$$M_y = -(4 \cdot (-4) - 4 \cdot (-4)) = -(-16 + 16) = 0$$
$$M_z = 4 \cdot 5 - 0 \cdot (-4) = 20$$

$$\boxed{\vec{M}_O = -20\vec{i} + 0\vec{j} + 20\vec{k} \text{ (N·m)}}$$

### Moment względem punktu B(4, 5, 4)

Wektor od B do A:
$$\vec{r}_{BA} = \vec{r}_A - \vec{r}_B = (4-4)\vec{i} + (0-5)\vec{j} + (4-4)\vec{k} = 0\vec{i} - 5\vec{j} + 0\vec{k}$$

$$\vec{M}_B = \vec{r}_{BA} \times \vec{P} = \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\ 0 & -5 & 0 \\ -4 & 5 & -4 \end{vmatrix}$$

$$M_x = (-5)(-4) - 0 \cdot 5 = 20$$
$$M_y = -(0 \cdot (-4) - 0 \cdot (-4)) = 0$$
$$M_z = 0 \cdot 5 - (-5)(-4) = 0 - 20 = -20$$

$$\boxed{\vec{M}_B = 20\vec{i} + 0\vec{j} - 20\vec{k} \text{ (N·m)}}$$

---

## Zadanie 7 – Moment siły (układ sferyczny)

Dane:
- $P = 3$ N, $\delta = \pi/4$, $\varphi = \pi/3$
- Punkt B: $B(0, 2, 0)$, punkt O: $(0,0,0)$

### Składowe siły w układzie sferycznym → kartezjańskim

W układzie sferycznym kąt $\delta$ to kąt od osi z (zenitalny), $\varphi$ to kąt azymutalny w płaszczyźnie xy:

$$P_x = P\sin\delta\cos\varphi = 3 \cdot \sin\frac{\pi}{4} \cdot \cos\frac{\pi}{3} = 3 \cdot \frac{\sqrt{2}}{2} \cdot \frac{1}{2} = \frac{3\sqrt{2}}{4}$$

$$P_y = P\sin\delta\sin\varphi = 3 \cdot \frac{\sqrt{2}}{2} \cdot \frac{\sqrt{3}}{2} = \frac{3\sqrt{6}}{4}$$

$$P_z = P\cos\delta = 3 \cdot \cos\frac{\pi}{4} = \frac{3\sqrt{2}}{2}$$

$$\vec{P} = \frac{3\sqrt{2}}{4}\vec{i} + \frac{3\sqrt{6}}{4}\vec{j} + \frac{3\sqrt{2}}{2}\vec{k}$$

### Wektor położenia B względem O

$$\vec{r}_B = 0\vec{i} + 2\vec{j} + 0\vec{k}$$

### Moment względem O

$$\vec{M}_O = \vec{r}_B \times \vec{P} = \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\ 0 & 2 & 0 \\ \frac{3\sqrt{2}}{4} & \frac{3\sqrt{6}}{4} & \frac{3\sqrt{2}}{2} \end{vmatrix}$$

$$M_x = 2 \cdot \frac{3\sqrt{2}}{2} - 0 \cdot \frac{3\sqrt{6}}{4} = 3\sqrt{2}$$

$$M_y = -\left(0 \cdot \frac{3\sqrt{2}}{2} - 0 \cdot \frac{3\sqrt{2}}{4}\right) = 0$$

$$M_z = 0 \cdot \frac{3\sqrt{6}}{4} - 2 \cdot \frac{3\sqrt{2}}{4} = -\frac{3\sqrt{2}}{2}$$

$$\boxed{\vec{M}_O = 3\sqrt{2}\,\vec{i} + 0\,\vec{j} - \frac{3\sqrt{2}}{2}\,\vec{k} \approx 4{,}24\,\vec{i} - 2{,}12\,\vec{k} \text{ (N·m)}}$$

---

## Zadanie 8 – Środek ciężkości trójkąta prostokątnego

Trójkąt prostokątny o wymiarach $b$ (podstawa) i $h$ (wysokość), z prawym kątem w początku układu.

Środek ciężkości wyznaczamy metodą całkowania. Wycinamy poziomy pasek o szerokości $b_y$ i wysokości $dy$ na wysokości $y$.

Z podobieństwa trójkątów:
$$b_y = b \cdot \frac{h - y}{h}$$

Pole elementu:
$$dA = b_y \, dy = \frac{b(h-y)}{h} \, dy$$

Całkowite pole:
$$A = \int_0^h \frac{b(h-y)}{h} \, dy = \frac{b}{h}\left[hy - \frac{y^2}{2}\right]_0^h = \frac{b}{h} \cdot \frac{h^2}{2} = \frac{bh}{2}$$

### Współrzędna $y_c$

$$M_x = \int_0^h y \, dA = \int_0^h y \cdot \frac{b(h-y)}{h} \, dy = \frac{b}{h}\int_0^h (hy - y^2) \, dy = \frac{b}{h}\left[\frac{hy^2}{2} - \frac{y^3}{3}\right]_0^h = \frac{b}{h} \cdot \frac{h^3}{6} = \frac{bh^2}{6}$$

$$y_c = \frac{M_x}{A} = \frac{bh^2/6}{bh/2} = \frac{h}{3}$$

### Współrzędna $x_c$

Z symetrii (lub analogicznym całkowaniem):
$$\boxed{x_c = \frac{b}{3}, \quad y_c = \frac{h}{3}}$$

---

## Zadanie 9 – Środek ciężkości figury złożonej z 3 figur

Z rysunku figura składa się z 3 prostokątów. Odczytując wymiary:

- **Figura 1** (lewy dolny prostokąt): szerokość 2 cm, wysokość 2 cm  
  $A_1 = 2 \cdot 2 = 4$ cm², $x_1 = 1$ cm, $y_1 = 1$ cm

- **Figura 2** (górny środkowy prostokąt): szerokość 6 cm, wysokość 2 cm  
  $A_2 = 6 \cdot 2 = 12$ cm², $x_2 = 3$ cm, $y_2 = 3$ cm (odczytać z rysunku)

- **Figura 3** (prawy środkowy prostokąt): szerokość 2 cm, wysokość 3 cm  
  $A_3 = 2 \cdot 3 = 6$ cm², $x_3 = 5$ cm, $y_3 = 1{,}5$ cm

> *Uwaga: dokładne współrzędne centroidów zależą od precyzyjnego odczytu wymiarów z rysunku.*

### Wzory na środek ciężkości figury złożonej

$$x_c = \frac{\sum A_i x_i}{\sum A_i}, \qquad y_c = \frac{\sum A_i y_i}{\sum A_i}$$

$$A_{total} = A_1 + A_2 + A_3 = 4 + 12 + 6 = 22 \text{ cm}^2$$

$$x_c = \frac{4 \cdot 1 + 12 \cdot 3 + 6 \cdot 5}{22} = \frac{4 + 36 + 30}{22} = \frac{70}{22} \approx 3{,}18 \text{ cm}$$

$$y_c = \frac{4 \cdot 1 + 12 \cdot 3 + 6 \cdot 1{,}5}{22} = \frac{4 + 36 + 9}{22} = \frac{49}{22} \approx 2{,}23 \text{ cm}$$

$$\boxed{x_c \approx 3{,}18 \text{ cm}, \quad y_c \approx 2{,}23 \text{ cm}}$$

---

## Zadanie 10 – Środek ciężkości figury ograniczonej parabolą

Figura ograniczona: $y = kx^2$, $x = h$, $y = 0$.

### Pole figury

$$A = \int_0^h kx^2 \, dx = k \cdot \frac{h^3}{3} = \frac{kh^3}{3}$$

### Współrzędna $x_c$

$$M_y = \int_0^h x \cdot kx^2 \, dx = k\int_0^h x^3 \, dx = k \cdot \frac{h^4}{4} = \frac{kh^4}{4}$$

$$x_c = \frac{M_y}{A} = \frac{kh^4/4}{kh^3/3} = \frac{3h}{4}$$

### Współrzędna $y_c$

Środek elementarnego paska pionowego na wysokości $y_c^{elem} = \frac{kx^2}{2}$:

$$M_x = \int_0^h \frac{kx^2}{2} \cdot kx^2 \, dx = \frac{k^2}{2}\int_0^h x^4 \, dx = \frac{k^2}{2} \cdot \frac{h^5}{5} = \frac{k^2 h^5}{10}$$

$$y_c = \frac{M_x}{A} = \frac{k^2 h^5/10}{kh^3/3} = \frac{3kh^2}{10}$$

Ponieważ $y_{max} = kh^2$:

$$\boxed{x_c = \frac{3h}{4}, \quad y_c = \frac{3}{10}kh^2 = \frac{3}{10}y_{max}}$$

---

## Zadanie 11 – Środek ciężkości wycinka koła

Wycinek koła o promieniu $R$ i kącie środkowym $2\alpha$ (symetrycznie względem osi x).

### Pole wycinka elementarnego

$$dA = \frac{R^2}{2} \, d\varphi$$

### Całkowite pole

$$A = \int_{-\alpha}^{\alpha} \frac{R^2}{2} \, d\varphi = \frac{R^2}{2} \cdot 2\alpha = R^2\alpha$$

### Współrzędna $x_c$ (oś symetrii)

Współrzędna x środka elementu: $x = \frac{2}{3}R\cos\varphi$

$$M_y = \int_{-\alpha}^{\alpha} \frac{2}{3}R\cos\varphi \cdot \frac{R^2}{2} \, d\varphi = \frac{R^3}{3}\int_{-\alpha}^{\alpha}\cos\varphi \, d\varphi = \frac{R^3}{3} \cdot 2\sin\alpha = \frac{2R^3\sin\alpha}{3}$$

$$x_c = \frac{M_y}{A} = \frac{2R^3\sin\alpha/3}{R^2\alpha}$$

$$\boxed{x_c = \frac{2R\sin\alpha}{3\alpha}}$$

Współrzędna $y_c = 0$ (z symetrii figury względem osi x).

---

## Zadanie 12 – Środek ciężkości figury płaskiej (prostokąt z wycięciem)

Z rysunku: prostokąt o wymiarach $40 \times 40$, z trójkątem lub prostokątem $15 \times 40$ na górze (odczytać z rysunku). Przyjmując prostokąt $40 \times 55$ z odcięciem prostokąta $15 \times 40$:

Na podstawie rysunku: prostokąt $40 \times 40$ z zaznaczonym wymiarem $15$ w górnej części.

Zakładam figurę jako prostokąt $40 \times (40+15) = 40 \times 55$ minus prostokąt $40 \times 15$ (górny kawałek odpowiada innemu kształtowi – odczytując rysunek jest to pełny prostokąt $40 \times 40$ z trapezem/trójkątem o wysokości 15 na górze).

**Przyjmując figurę złożoną z prostokąta i trójkąta:**

- Prostokąt: $A_1 = 40 \times 40 = 1600$, $y_1 = 20$
- Trójkąt (na górze): $A_2 = \frac{1}{2} \times 40 \times 15 = 300$, $y_2 = 40 + 5 = 45$

$$A = 1600 + 300 = 1900$$

$$y_c = \frac{1600 \cdot 20 + 300 \cdot 45}{1900} = \frac{32000 + 13500}{1900} = \frac{45500}{1900} \approx 23{,}9$$

$$x_c = \frac{40}{2} = 20 \text{ (oś symetrii)}$$

$$\boxed{x_c = 20, \quad y_c \approx 23{,}9}$$

---

## Zadanie 13 – Środek ciężkości figury złożonej

Z rysunku (wymiary w jednostkach):

Figura składa się z:
- **Prostokąta dolnego**: $3 \times 2$ (szerokość 3, wysokość 2, od y=1 do y=3), x od 1 do 4
- **Trójkąta górnego**: podstawa 3, wysokość 3, od y=3 do y=6, x od 1 do 4 (trapez/trójkąt)
- **Paska dolnego**: $5 \times 1$ (szerokość 5, od x=1 do x=6, y=0 do y=1)

Na podstawie rysunku z zaznaczonymi wymiarami $1, 3, 2$ (poziome) i $1, 2, 3, 3$ (pionowe):

**Figura 1** – prostokąt $3 \times 3$ (x: 1→4, y: 1→4):
$$A_1 = 9, \quad x_1 = 2{,}5, \quad y_1 = 2{,}5$$

**Figura 2** – trójkąt (podstawa 3, wysokość 3, x: 1→4, y: 4→9... ):

Dokładna interpretacja wymaga precyzyjnego odczytu rysunku. Stosując ogólną metodę:

$$x_c = \frac{\sum A_i x_i}{\sum A_i}, \qquad y_c = \frac{\sum A_i y_i}{\sum A_i}$$

Każdą figurę składową sprowadzamy do prostokąta lub trójkąta, wyznaczamy jej pole i współrzędne centroidu, następnie sumujemy zgodnie z powyższymi wzorami.

> **Uwaga:** Precyzyjne rozwiązanie zadań 9, 12 i 13 wymaga dokładnego odczytu wymiarów z oryginalnego rysunku. Zaprezentowana metoda obliczeniowa jest poprawna – należy podstawić odczytane wartości do powyższych wzorów.
