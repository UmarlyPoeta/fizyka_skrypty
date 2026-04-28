import argparse
import csv
import math
import os
import re


def prompt_float(prompt):
	while True:
		raw = input(prompt).strip().replace(",", ".")
		try:
			return float(raw)
		except ValueError:
			print("Niepoprawna liczba. Sprobuj ponownie.")


def prompt_yes_no(prompt):
	while True:
		raw = input(prompt).strip().lower()
		if raw in ("t", "tak", "y", "yes"):
			return True
		if raw in ("n", "nie", "no"):
			return False
		print("Podaj t lub n.")


def prompt_choice(prompt, options):
	while True:
		print(prompt)
		for i, opt in enumerate(options, start=1):
			print(f"  {i}) {opt}")
		raw = input("Wybierz numer lub wpisz nazwe: ").strip().lower()
		for i, opt in enumerate(options, start=1):
			if raw == str(i) or raw == opt.lower():
				return opt
		print("Niepoprawny wybor.")


def parse_float_list(prompt):
	while True:
		raw = input(prompt).strip()
		if not raw:
			return []
		parts = re.findall(r"[-+]?\d+(?:[\.,]\d+)?", raw)
		if not parts:
			print("Niepoprawna lista liczb. Podaj liczby oddzielone spacjami.")
			continue
		try:
			return [float(p.replace(",", ".")) for p in parts]
		except ValueError:
			print("Niepoprawna lista liczb. Podaj liczby oddzielone spacjami.")


def parse_float(value):
	if value is None:
		return None
	raw = str(value).strip()
	if not raw:
		return None
	return float(raw.replace(",", "."))


def parse_bool(value, default=False):
	if value is None:
		return default
	raw = str(value).strip().lower()
	if raw in ("t", "tak", "y", "yes", "1", "true", "on"):
		return True
	if raw in ("n", "nie", "no", "0", "false", "off"):
		return False
	return default


def pressure_to_pa(value, unit):
	unit = unit.lower()
	if unit == "pa":
		return value
	if unit in ("hpa", "mbar"):
		return value * 100.0
	if unit == "kpa":
		return value * 1000.0
	if unit == "mmhg":
		return value * 133.322
	if unit == "mmh2o":
		return value * 9.80665
	raise ValueError("Nieznana jednostka cisnienia")


def length_to_m(value, unit):
	unit = unit.lower()
	if unit == "m":
		return value
	if unit == "mm":
		return value / 1000.0
	raise ValueError("Nieznana jednostka dlugosci")


def length_to_m_signed(value, unit):
	if value is None:
		return None
	sign = -1.0 if value < 0 else 1.0
	return sign * length_to_m(abs(value), unit)


def velocity_to_mps(value, unit):
	unit = unit.lower()
	if unit in ("m/s", "mps"):
		return value
	if unit in ("km/h", "kmh"):
		return value / 3.6
	raise ValueError("Nieznana jednostka predkosci")


def saturation_vapor_pressure_pa(t_c):
	return 610.94 * math.exp(17.625 * t_c / (t_c + 243.04))


def air_density(t_c, p_pa, rh_percent):
	t_k = t_c + 273.15
	e_s = saturation_vapor_pressure_pa(t_c)
	e = max(0.0, min(1.0, rh_percent / 100.0)) * e_s
	p_dry = max(0.0, p_pa - e)
	r_d = 287.058
	r_v = 461.495
	return p_dry / (r_d * t_k) + e / (r_v * t_k)


def air_dynamic_viscosity(t_c):
	t_k = t_c + 273.15
	mu0 = 1.716e-5
	t0 = 273.15
	s = 111.0
	return mu0 * ((t_k / t0) ** 1.5) * (t0 + s) / (t_k + s)


def velocity_from_dp(dp_pa, rho):
	if dp_pa < 0:
		print("Uwaga: dp < 0, ustawiam na 0.")
		dp_pa = 0.0
	return math.sqrt(2.0 * dp_pa / rho)


def log_chebyshev_positions(n_points):
	mapping = {
		3: [0.375, 0.825, 0.936],
		4: [0.331, 0.612, 0.800, 0.952],
		5: [0.287, 0.570, 0.689, 0.847, 0.962],
	}
	if n_points not in mapping:
		raise ValueError("Dozwolone: 3, 4 lub 5 punktow")
	return mapping[n_points]


def collect_log_chebyshev(r_over_r_list, rho):
	print("\nPunkty Log-Czebyszew (r/R):")
	print(" ".join([f"{v:.3f}" for v in r_over_r_list]))

	data_kind = prompt_choice("Dane pomiarowe:", ["dp", "v"])
	if data_kind == "dp":
		unit = prompt_choice("Jednostka dp:", ["Pa", "hPa", "mbar", "mmH2O"])
	else:
		unit = prompt_choice("Jednostka v:", ["m/s", "km/h"])

	left = list(reversed(r_over_r_list))
	right = list(r_over_r_list)
	entries = []

	for i, r_over_r in enumerate(left, start=1):
		label = f"{len(left) - i + 1}g"
		value = prompt_float(f"{label} (r/R={r_over_r:.3f}) wartosc: ")
		entries.append((label, r_over_r, value))

	value = prompt_float("0 (os) wartosc: ")
	entries.append(("0", 0.0, value))

	for i, r_over_r in enumerate(right, start=1):
		label = f"{i}d"
		value = prompt_float(f"{label} (r/R={r_over_r:.3f}) wartosc: ")
		entries.append((label, r_over_r, value))

	results = []
	for label, r_over_r, value in entries:
		if data_kind == "dp":
			dp_pa = pressure_to_pa(value, unit)
			v = velocity_from_dp(dp_pa, rho)
		else:
			if unit == "km/h":
				v = value / 3.6
			else:
				v = value
			dp_pa = 0.5 * rho * v * v
		results.append(
			{
				"label": label,
				"r_over_r": r_over_r,
				"value": value,
				"dp_pa": dp_pa,
				"v": v,
			}
		)

	return results


def collect_profile_points(rho):
	print("\nProfil v(r):")
	print("Podaj r od osi w mm (np. 0 10 20 30). Enter bez danych pominie profil.")
	r_list = parse_float_list("r [mm]: ")
	if not r_list:
		return []

	data_kind = prompt_choice("Dane pomiarowe:", ["dp", "v"])
	if data_kind == "dp":
		unit = prompt_choice("Jednostka dp:", ["Pa", "hPa", "mbar", "mmH2O"])
	else:
		unit = prompt_choice("Jednostka v:", ["m/s", "km/h"])

	values = []
	for r_mm in r_list:
		value = prompt_float(f"r={r_mm} mm wartosc: ")
		if data_kind == "dp":
			dp_pa = pressure_to_pa(value, unit)
			v = velocity_from_dp(dp_pa, rho)
		else:
			if unit == "km/h":
				v = value / 3.6
			else:
				v = value
			dp_pa = 0.5 * rho * v * v
		values.append(
			{
				"r_mm": r_mm,
				"value": value,
				"dp_pa": dp_pa,
				"v": v,
			}
		)

	return values


def flow_regime(re):
	if re < 2300:
		return "laminarny"
	if re < 4000:
		return "przejsciowy"
	return "turbulentny"


def vavg_over_vmax_theory(re):
	if re <= 0:
		return None
	if re < 2300:
		return 0.5
	return 0.7106 * (re ** 0.0135)


def try_plot(profile, vmax, n_exp, out_path):
	try:
		import matplotlib.pyplot as plt
	except Exception:
		print("Brak matplotlib, pomijam wykres.")
		return

	xs = [i / 100.0 for i in range(0, 101)]
	v_lam = [vmax * (1.0 - x * x) for x in xs]

	v_turb = None
	if n_exp and n_exp > 0:
		v_turb = [vmax * ((1.0 - x) ** (1.0 / n_exp)) for x in xs]

	plt.figure(figsize=(7, 5))

	if profile:
		pr_x = [p["r_over_r"] for p in profile]
		pr_v = [p["v"] for p in profile]
		plt.scatter(pr_x, pr_v, label="pomiary", color="black")

	plt.plot(xs, v_lam, label="laminarny", color="tab:blue")
	if v_turb is not None:
		plt.plot(xs, v_turb, label="Prandtl", color="tab:red")

	plt.xlabel("r/R")
	plt.ylabel("v [m/s]")
	plt.title("Rozklad predkosci v(r)")
	plt.legend()
	plt.grid(True, alpha=0.3)
	plt.tight_layout()
	plt.savefig(out_path, dpi=150)
	plt.close()
	print(f"Zapisano wykres: {out_path}")


def read_lab_csv(path):
	meta = {}
	log_rows = []
	profile_rows = []

	with open(path, newline="", encoding="utf-8") as f:
		reader = csv.DictReader(f)
		if not reader.fieldnames:
			raise ValueError("Brak naglowka w CSV")
		for raw_row in reader:
			row = {k.strip().lower(): (v or "").strip() for k, v in raw_row.items()}
			section = row.get("section", "").lower()
			if not section:
				continue

			if section == "meta":
				key = row.get("key", "").lower()
				if not key:
					continue
				meta[key] = row.get("value", "")
				unit = row.get("unit", "")
				if unit:
					meta[f"{key}_unit"] = unit
				continue

			if section in ("log", "profile"):
				label = row.get("label", "")
				r_val = parse_float(row.get("r_m") or row.get("r") or row.get("r_mm"))
				r_unit = row.get("r_unit", "")
				if not r_unit and row.get("r_mm"):
					r_unit = "mm"
				dp_val = parse_float(row.get("dp") or row.get("dp_pa"))
				dp_unit = row.get("dp_unit") or row.get("unit") or "Pa"
				v_val = parse_float(row.get("v"))
				v_unit = row.get("v_unit") or "m/s"
				row_data = {
					"label": label,
					"r_val": r_val,
					"r_unit": r_unit,
					"dp_val": dp_val,
					"dp_unit": dp_unit,
					"v_val": v_val,
					"v_unit": v_unit,
				}
				if section == "log":
					log_rows.append(row_data)
				else:
					profile_rows.append(row_data)

	return meta, log_rows, profile_rows


def prepare_measurements(rows, rho, r_unit_default, d_m):
	prepared = []
	for row in rows:
		r_unit = row.get("r_unit") or r_unit_default or "m"
		r_val = row.get("r_val")
		if r_val is None:
			raise ValueError("Brak wartosci r w CSV")
		r_m = length_to_m_signed(r_val, r_unit)

		dp_val = row.get("dp_val")
		v_val = row.get("v_val")
		if dp_val is not None:
			dp_pa = pressure_to_pa(dp_val, row.get("dp_unit", "Pa"))
			v = velocity_from_dp(dp_pa, rho)
		elif v_val is not None:
			v = velocity_to_mps(v_val, row.get("v_unit", "m/s"))
			dp_pa = 0.5 * rho * v * v
		else:
			raise ValueError("Brak dp lub v w CSV")

		r_over_r = None
		if d_m and d_m > 0:
			r_over_r = abs(r_m) / (d_m / 2.0)

		prepared.append(
			{
				"label": row.get("label", ""),
				"r_m": r_m,
				"r_over_r": r_over_r,
				"dp_pa": dp_pa,
				"v": v,
			}
		)

	return prepared


def build_table(rows, headers, fields, formatters=None):
	formatters = formatters or {}
	lines = []
	lines.append("| " + " | ".join(headers) + " |")
	lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
	for row in rows:
		values = []
		for field in fields:
			value = row.get(field, "")
			if field in formatters:
				value = formatters[field](value)
			values.append(str(value))
		lines.append("| " + " | ".join(values) + " |")
	return "\n".join(lines)


def compute_from_csv(meta, log_rows, profile_rows):
	def meta_float(key, default=None, required=False):
		value = parse_float(meta.get(key))
		if value is None:
			if required:
				raise ValueError(f"Brak wartosci meta: {key}")
			return default
		return value

	def meta_unit(key, default=None):
		return meta.get(f"{key}_unit", default)

	t_c = meta_float("t", required=True)
	pb = meta_float("pb", required=True)
	pb_unit = meta_unit("pb", "Pa")
	rh = meta_float("rh", required=True)
	d_val = meta_float("d", required=True)
	d_unit = meta_unit("d", "m")
	ps = meta_float("ps", default=0.0)
	ps_unit = meta_unit("ps", "Pa")
	mu_override = meta_float("mu")
	r_unit_default = meta.get("r_unit", "m")

	pb_pa = pressure_to_pa(pb, pb_unit)
	ps_pa = pressure_to_pa(ps, ps_unit)
	p_abs = pb_pa + ps_pa
	d_m = length_to_m(d_val, d_unit)

	rho = air_density(t_c, p_abs, rh)
	mu = mu_override if mu_override is not None else air_dynamic_viscosity(t_c)
	nu = mu / rho

	log_points = prepare_measurements(log_rows, rho, r_unit_default, d_m)
	profile_points = prepare_measurements(profile_rows, rho, r_unit_default, d_m)

	include_axis = parse_bool(meta.get("log_include_axis"), default=True)
	def is_axis(row):
		if row.get("label", "").strip().startswith("0"):
			return True
		return abs(row.get("r_m", 1.0)) < 1e-9

	log_for_avg = [p for p in log_points if include_axis or not is_axis(p)]
	if not log_for_avg:
		raise ValueError("Brak punktow do obliczenia v_srednia")
	log_v = [p["v"] for p in log_for_avg]
	v_avg = sum(log_v) / len(log_v)

	v_axis = None
	for p in log_points:
		if is_axis(p):
			v_axis = p["v"]
			break
	if v_axis is None and profile_points:
		for p in profile_points:
			if abs(p.get("r_m", 1.0)) < 1e-9:
				v_axis = p["v"]
				break

	re_val = rho * v_avg * d_m / mu
	regime = flow_regime(re_val)

	prandtl_n = meta_float("prandtl_n")
	if prandtl_n is None and re_val >= 2300:
		prandtl_n = 1.66 * math.log10(re_val)

	ratio_theory = vavg_over_vmax_theory(re_val)

	vmax_source = "log_os"
	if v_axis and v_axis > 0:
		vmax = v_axis
	elif ratio_theory and ratio_theory > 0:
		vmax = v_avg / ratio_theory
		vmax_source = "z_v_srednia"
	else:
		vmax = max([p["v"] for p in log_points]) if log_points else v_avg
		vmax_source = "max_log"

	for p in profile_points:
		if p.get("r_over_r") is None:
			p["v_theory"] = None
			continue
			rr = min(max(p["r_over_r"], 0.0), 1.0)
			if re_val < 2300:
				p["v_theory"] = vmax * (1.0 - rr * rr)
			elif prandtl_n and prandtl_n > 0:
				p["v_theory"] = vmax * ((1.0 - rr) ** (1.0 / prandtl_n))
			else:
				p["v_theory"] = None

	ratio_meas = v_avg / v_axis if v_axis and v_axis > 0 else None

	return {
		"t_c": t_c,
		"pb_pa": pb_pa,
		"ps_pa": ps_pa,
		"p_abs": p_abs,
		"rh": rh,
		"d_m": d_m,
		"rho": rho,
		"mu": mu,
		"nu": nu,
		"v_avg": v_avg,
		"v_axis": v_axis,
		"re": re_val,
		"regime": regime,
		"prandtl_n": prandtl_n,
		"ratio_theory": ratio_theory,
		"ratio_meas": ratio_meas,
		"log_points": log_points,
		"profile_points": profile_points,
		"include_axis": include_axis,
		"vmax": vmax,
		"vmax_source": vmax_source,
	}


def build_report(meta, results, plot_path):
	group = meta.get("group", "")
	lab_date = meta.get("lab_date", "")
	receive_date = meta.get("receive_date", "")
	topic = meta.get("topic", "WYZNACZENIE ROZKLADU PREDKOSCI STRUGI W KANALE")
	names = meta.get("names", "")
	grade_notes = meta.get("grade_notes", "")
	wnioski = meta.get("wnioski", "")

	lines = []
	lines.append(f"Grupa lab: {group}")
	lines.append(f"Data wykonania: {lab_date}")
	lines.append(f"Data odbioru: {receive_date}")
	lines.append("")
	lines.append("Temat cwiczenia")
	lines.append("")
	lines.append(topic)
	lines.append("")
	lines.append("Imiona i nazwiska")
	lines.append("")
	lines.append(names)
	lines.append("")
	lines.append("Ocena i uwagi")
	lines.append("")
	lines.append(grade_notes)
	lines.append("")
	lines.append("# I. Cel cwiczenia")
	lines.append(
		"Celem cwiczenia jest zapoznanie sie z metoda pomiaru predkosci plynu "
		"przy pomocy rurki Prandtla oraz okreslenie rozkladu predkosci "
		"w przewodzie o przekroju kolowym."
	)
	lines.append("")
	lines.append("# II. Schemat stanowiska pomiarowego")
	lines.append("Rys. 1 Schemat stanowiska pomiarowego")
	lines.append(
		"W sklad stanowiska wchodzily: rurociag, rurka Prandtla, mikromanometr "
		"oraz skala pomiarowa. Medium robocze stanowilo powietrze tloczone "
		"przez wentylator z regulacja natezenia przeplywu."
	)
	lines.append(
		"Rurka Prandtla sluzyla do wyznaczania cisnienia dynamicznego, "
		"a jej pozycje ustawiano na skali pomiarowej, co pozwalalo na odczyt "
		"polozenia osi w przekroju. Odczyt cisnien realizowano mikromanometrem."
	)
	lines.append("")
	lines.append("Przyrzady pomiarowe:")
	lines.append("1. Mikromanometr HD 2114P.2")
	lines.append("")
	lines.append("Rys. 2 Mikromanometr HD 2114P.2")
	lines.append(
		"Przenosne urzadzenie do pomiaru cisnienia roznicowego, nad- i podcisnienia "
		"gazow nieagresywnych (zakres do 20 mbar)."
	)
	lines.append("")
	lines.append("2. Sonda Prandtla")
	lines.append("")
	lines.append("Rys. 3 Sonda Prandtla")
	lines.append(
		"Przyrzad pomiarowy zlozony z dwoch koncentrycznych rurek, umozliwiajacy "
		"pomiar cisnienia calkowitego i statycznego oraz wyznaczenie cisnienia dynamicznego."
	)
	lines.append("")
	lines.append("# III. Wyniki pomiarow w tabeli")
	lines.append("")
	lines.append("Metoda Log-Czebyszewa (predkosc srednia)")
	lines.append("")
	lines.append(
		build_table(
			results["log_points"],
			["L.p", "r [m]", "dp [Pa]", "v [m/s]"],
			["label", "r_m", "dp_pa", "v"],
			{
				"r_m": lambda v: f"{v:.4f}",
				"dp_pa": lambda v: f"{v:.2f}",
				"v": lambda v: f"{v:.3f}",
			},
		)
	)
	lines.append("")
	lines.append("Rozklad predkosci v=v(r)")
	lines.append("")
	if results["profile_points"]:
		lines.append(
			build_table(
				results["profile_points"],
				["L.p", "r [m]", "dp [Pa]", "v [m/s]"],
				["label", "r_m", "dp_pa", "v"],
				{
					"r_m": lambda v: f"{v:.4f}",
					"dp_pa": lambda v: f"{v:.2f}",
					"v": lambda v: f"{v:.3f}",
				},
			)
		)
	else:
		lines.append("Brak danych profilu v(r).")

	lines.append("")
	lines.append("# IV. Obliczenia")
	lines.append(
		"Dane wejsciowe: t = {t:.2f} C, pb = {pb:.2f} Pa, ps = {ps:.2f} Pa, "
		"phi = {rh:.1f} %, D = {d:.4f} m".format(
			t=results["t_c"],
			pb=results["pb_pa"],
			ps=results["ps_pa"],
			rh=results["rh"],
			d=results["d_m"],
		)
	)
	lines.append("")
	lines.append("Rzeczywiste parametry powietrza:")
	lines.append(
		"T = {t:.2f} K, p_abs = {p:.2f} Pa, rho = {rho:.4f} kg/m3, "
		"mu = {mu:.6e} Pa*s, nu = {nu:.6e} m2/s".format(
			t=results["t_c"] + 273.15,
			p=results["p_abs"],
			rho=results["rho"],
			mu=results["mu"],
			nu=results["nu"],
		)
	)
	lines.append("")
	lines.append("Log-Czebyszew:")
	lines.append(
		"v_srednia = {vavg:.3f} m/s (punkt 0 wliczony: {axis}), v_max = {vmax:.3f} m/s".format(
			vavg=results["v_avg"],
			axis="tak" if results["include_axis"] else "nie",
			vmax=results["vmax"],
		)
	)
	lines.append(
		"Re = {re:.0f} ({regime})".format(re=results["re"], regime=results["regime"])
	)
	if results["prandtl_n"] is not None:
		lines.append("n (Prandtl) = {:.2f}".format(results["prandtl_n"]))
	if results["ratio_theory"] is not None:
		lines.append("v_srednia/v_max (teoria) = {:.3f}".format(results["ratio_theory"]))
	if results["ratio_meas"] is not None:
		lines.append("v_srednia/v_max (pomiar) = {:.3f}".format(results["ratio_meas"]))

	lines.append("")
	lines.append("Teoretyczny rozklad predkosci (dla punktow profilu):")
	if results["profile_points"]:
		rows = []
		for p in results["profile_points"]:
			rows.append(
				{
					"label": p["label"],
					"r_over_r": p["r_over_r"],
					"v": p["v"],
					"v_theory": p.get("v_theory"),
				}
			)
		lines.append(
			build_table(
				rows,
				["L.p", "r/R", "v_zmierz [m/s]", "v_teoria [m/s]"],
				["label", "r_over_r", "v", "v_theory"],
				{
					"r_over_r": lambda v: "" if v is None else f"{v:.3f}",
					"v": lambda v: f"{v:.3f}",
					"v_theory": lambda v: "" if v is None else f"{v:.3f}",
				},
			)
		)
	else:
		lines.append("Brak danych profilu.")

	lines.append("")
	lines.append("# V. Wykres rozkladu predkosci")
	if plot_path:
		lines.append(f"![Rozklad predkosci]({plot_path})")
	else:
		lines.append("Brak wykresu (brak danych profilu).")

	lines.append("")
	lines.append("# VI. Wnioski")
	if wnioski:
		lines.append(wnioski)
	else:
		lines.append("Wpisz wnioski na podstawie uzyskanych wynikow.")

	return "\n".join(lines)


def run_csv_mode(csv_path, out_path):
	meta, log_rows, profile_rows = read_lab_csv(csv_path)
	results = compute_from_csv(meta, log_rows, profile_rows)

	plot_path = ""
	if results["profile_points"]:
		plot_path = "rozklad_predkosci.png"
		try_plot(results["profile_points"], results["vmax"], results["prandtl_n"], plot_path)

	report = build_report(meta, results, plot_path)
	with open(out_path, "w", encoding="utf-8") as f:
		f.write(report)

	print(f"Zapisano sprawozdanie: {out_path}")


def run_interactive():
	print("Mechanika plynow - Prandtl - rozklad predkosci")

	t_c = prompt_float("Temperatura powietrza t [C]: ")
	p_val = prompt_float("Cisnienie barometryczne pb (wartosc): ")
	p_unit = prompt_choice("Jednostka pb:", ["Pa", "hPa", "mbar", "mmHg", "kPa"])
	rh = prompt_float("Wilgotnosc wzgledna phi [%]: ")
	d_val = prompt_float("Srednica przewodu D (wartosc): ")
	d_unit = prompt_choice("Jednostka D:", ["m", "mm"])

	p_pa = pressure_to_pa(p_val, p_unit)
	d_m = length_to_m(d_val, d_unit)

	rho = air_density(t_c, p_pa, rh)
	mu = air_dynamic_viscosity(t_c)
	nu = mu / rho

	print("\n--- Parametry powietrza ---")
	print(f"rho = {rho:.4f} kg/m3")
	print(f"mu  = {mu:.6e} Pa*s")
	print(f"nu  = {nu:.6e} m2/s")

	n_points = int(prompt_choice("Liczba punktow Log-Czebyszew:", ["3", "4", "5"]))
	r_over_r_list = log_chebyshev_positions(n_points)

	log_data = collect_log_chebyshev(r_over_r_list, rho)
	v_list = [x["v"] for x in log_data]
	v_avg = sum(v_list) / len(v_list)
	v_axis = None
	for x in log_data:
		if x["label"] == "0":
			v_axis = x["v"]
			break

	re = rho * v_avg * d_m / mu
	regime = flow_regime(re)
	n_exp = 1.66 * math.log10(re) if re >= 2300 else None
	ratio_theory = vavg_over_vmax_theory(re)
	ratio_meas = v_avg / v_axis if v_axis and v_axis > 0 else None

	print("\n--- Log-Czebyszew ---")
	for x in log_data:
		print(
			f"{x['label']:>3} r/R={x['r_over_r']:.3f} "
			f"dp={x['dp_pa']:.2f} Pa v={x['v']:.3f} m/s"
		)
	print(f"v_srednia = {v_avg:.3f} m/s")
	if v_axis is not None:
		print(f"v_max (os) = {v_axis:.3f} m/s")
	print(f"Re = {re:.0f} ({regime})")
	if n_exp is not None:
		print(f"n (Prandtl) = {n_exp:.2f}")
	if ratio_theory is not None:
		print(f"v_srednia/v_max (teoria) = {ratio_theory:.3f}")
	if ratio_meas is not None:
		print(f"v_srednia/v_max (pomiar) = {ratio_meas:.3f}")

	profile_raw = collect_profile_points(rho)
	profile = []
	if profile_raw:
		r_max = d_m / 2.0
		for p in profile_raw:
			r_m = p["r_mm"] / 1000.0
			profile.append(
				{
					"r_mm": p["r_mm"],
					"r_over_r": r_m / r_max,
					"dp_pa": p["dp_pa"],
					"v": p["v"],
				}
			)

		print("\n--- Profil v(r) ---")
		for p in profile:
			print(
				f"r={p['r_mm']:.1f} mm r/R={p['r_over_r']:.3f} "
				f"dp={p['dp_pa']:.2f} Pa v={p['v']:.3f} m/s"
			)

	if prompt_yes_no("\nZapisac wyniki do CSV? [t/n]: "):
		base = "mechanika_plynow_wyniki"
		with open(f"{base}_log.csv", "w", newline="") as f:
			w = csv.writer(f)
			w.writerow(["label", "r_over_r", "dp_pa", "v"])
			for x in log_data:
				w.writerow([x["label"], x["r_over_r"], f"{x['dp_pa']:.6f}", f"{x['v']:.6f}"])

		created = [f"{base}_log.csv", f"{base}_podsumowanie.txt"]
		if profile:
			with open(f"{base}_profil.csv", "w", newline="") as f:
				w = csv.writer(f)
				w.writerow(["r_mm", "r_over_r", "dp_pa", "v"])
				for p in profile:
					w.writerow([p["r_mm"], f"{p['r_over_r']:.6f}", f"{p['dp_pa']:.6f}", f"{p['v']:.6f}"])
			created.insert(1, f"{base}_profil.csv")

		with open(f"{base}_podsumowanie.txt", "w") as f:
			f.write("Parametry powietrza\n")
			f.write(f"rho={rho:.6f} kg/m3\n")
			f.write(f"mu={mu:.6e} Pa*s\n")
			f.write(f"nu={nu:.6e} m2/s\n")
			f.write("\nLog-Czebyszew\n")
			f.write(f"v_srednia={v_avg:.6f} m/s\n")
			if v_axis is not None:
				f.write(f"v_max_os={v_axis:.6f} m/s\n")
			f.write(f"Re={re:.2f}\n")
			f.write(f"regime={regime}\n")
			if n_exp is not None:
				f.write(f"n_prandtl={n_exp:.6f}\n")
			if ratio_theory is not None:
				f.write(f"ratio_theory={ratio_theory:.6f}\n")
			if ratio_meas is not None:
				f.write(f"ratio_meas={ratio_meas:.6f}\n")

		print("Zapisano: " + ", ".join(created))

	if profile and prompt_yes_no("Zrobic wykres v(r)? [t/n]: "):
		if v_axis and v_axis > 0:
			vmax_for_plot = v_axis
		elif ratio_theory and ratio_theory > 0:
			vmax_for_plot = v_avg / ratio_theory
		else:
			vmax_for_plot = v_avg
		try_plot(profile, vmax_for_plot, n_exp, "rozklad_predkosci.png")


def main():
	parser = argparse.ArgumentParser(
		description="Mechanika plynow - Prandtl (interaktywnie lub z CSV)"
	)
	parser.add_argument("--csv", dest="csv_path", help="Sciezka do pliku CSV z danymi")
	parser.add_argument(
		"--out",
		dest="out_path",
		default="sprawozdanie_lab1.md",
		help="Sciezka do pliku sprawozdania (MD)",
	)
	args = parser.parse_args()

	if args.csv_path:
		run_csv_mode(args.csv_path, args.out_path)
	else:
		run_interactive()


if __name__ == "__main__":
	main()
