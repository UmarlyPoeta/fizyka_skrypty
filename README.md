# Fizyka Skrypty

A collection of Python scripts for physics laboratory data analysis and visualization. These scripts were created to process experimental data and generate reports for various physics experiments.

## Overview

This repository contains computational tools for analyzing physics laboratory measurements, including:
- Material properties (Young's modulus, hardness, viscosity)
- Electrical measurements (Wheatstone bridge)
- Crystal structure and defects analysis
- Electric field modeling

## Scripts

### 1. `modul_younga.py`
Calculates Young's modulus for different wire materials (brass and steel).
- Processes force and elongation measurements
- Generates force-elongation plots
- Calculates average wire diameter and material properties

### 2. `materialy_ceramiczne.py`
Analyzes hardness of ceramic materials.
- Plots hardness (HV1) for various ceramic materials (TiN, SiC, Al₂O₃, WC/Co, Si₃N₄)
- Calculates density for WC + Co and Al₂O₃ samples
- Uses bar charts for visualization

### 3. `twardosc.py`
Hardness measurements analysis with automated report generation.
- Processes HRB and HV hardness data
- Generates plots showing grain size vs. strain
- Uses AI (Ollama) to generate theoretical introduction and conclusions
- Creates PDF reports with results

### 4. `lepkosc.py`
Viscosity coefficient calculation using falling ball method.
- Calculates viscosity from ball diameter, mass, and fall time
- Computes average viscosity and uncertainty
- Processes multiple measurements for statistical analysis

### 5. `defekty.py`
Crystal structure defects and grain size analysis.
- Analyzes grain size as a function of strain (ε)
- Generates plots showing relationship between deformation and grain size
- Uses AI to generate theoretical background about crystal defects
- Creates comprehensive PDF reports

### 6. `mostek.py`
Wheatstone bridge resistance calculations.
- Calculates unknown resistance (Rx) from bridge measurements
- Processes multiple measurement series
- Computes mean values and uncertainties
- Performs series/parallel resistance calculations

### 7. `modelowanie_pola_elektrycznego.py`
Electric field modeling (template/placeholder for future implementation).

## Dependencies

The scripts require the following Python packages:

```
matplotlib
numpy
scipy
fpdf
ollama (for AI-generated reports in some scripts)
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/UmarlyPoeta/fizyka_skrypty.git
cd fizyka_skrypty
```

2. Install required packages:
```bash
pip install matplotlib numpy scipy fpdf
```

3. (Optional) Install Ollama for AI-generated report sections:
```bash
# Follow instructions at https://ollama.ai/
```

## Usage

Each script can be run independently:

```bash
python modul_younga.py
python materialy_ceramiczne.py
python twardosc.py
python lepkosc.py
python defekty.py
python mostek.py
```

Some scripts (like `defekty.py` and `twardosc.py`) require Ollama to be running for AI-generated content:
```bash
ollama serve  # In a separate terminal
python defekty.py
```

## Data Files

- `dane_modul.txt` - Input data file for Young's modulus calculations

## Output

Scripts generate various outputs:
- **Plots**: PNG files (e.g., `wykres.png`, `wykres2.png`)
- **Reports**: PDF files with experimental data, plots, and conclusions (e.g., `sprawozdanie.pdf`)
- **Console output**: Calculated values and statistics

## Notes

- Some scripts contain hardcoded experimental data
- Font paths for PDF generation may need adjustment based on your system
- AI-generated sections use the Llama 3.2 model via Ollama

## Author

Patryk Kozłowski (grupa laboratoryjna nr 4)

## License

This project is provided as-is for educational purposes.
