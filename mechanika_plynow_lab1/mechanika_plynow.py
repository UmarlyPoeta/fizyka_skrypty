import csv
import math
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


def main():
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


if __name__ == "__main__":
	main()
