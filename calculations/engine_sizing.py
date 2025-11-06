import os
import yaml
import numpy as np
import matplotlib.pyplot as plt

def load_config(path='config.yaml'):
    with open(path, 'r') as f:
        cfg = yaml.safe_load(f)
    return cfg

def generate_engine_schematic(figures_dir='figures'):
    os.makedirs(figures_dir, exist_ok=True)
    plt.figure(figsize=(8,4))
    # простая иллюстрация: линия камеры → сопло
    plt.plot([0.1, 0.3, 0.5, 0.7, 0.9], [0.5, 0.6, 0.5, 0.4, 0.3], '-o', color='#2E86C1')
    plt.text(0.1, 0.5, "Oxidiser pump", ha='right', va='center')
    plt.text(0.3, 0.6, "Fuel pump", ha='right', va='bottom')
    plt.text(0.5, 0.5, "Combustion chamber", ha='center', va='center')
    plt.text(0.7, 0.4, "Nozzle throat", ha='left', va='bottom')
    plt.text(0.9, 0.3, "Nozzle exit", ha='left', va='center')
    plt.title("Simplified Liquid-Propellant Rocket Engine Schematic")
    plt.axis('off')
    plt.tight_layout()
    path = os.path.join(figures_dir, "engine_schematic.png")
    plt.savefig(path, dpi=300, facecolor='white')
    plt.close()
    print(f"Saved schematic: {path}")

def generate_nozzle_plot(cfg, figures_dir='figures'):
    os.makedirs(figures_dir, exist_ok=True)
    expansions = np.array(cfg.get('ae_at', [30, 60]))
    # Простейшая модель Isp
    isp_first = 300 + 0.5 * (expansions - 10)
    isp_upper = 420 + 0.6 * (expansions - 10)

    plt.figure(figsize=(8,5))
    plt.plot(expansions, isp_first, label='First stage (LOX + RP-1)', marker='o')
    plt.plot(expansions, isp_upper, label='Upper stage (LOX + LH₂)', marker='o')
    # отмечаем целевые значения, если они есть
    if len(expansions) >= 1:
        plt.axvline(expansions[0], color='grey', linestyle='--',
                    label=f"Target Ae/At ≈ {expansions[0]}")
    if len(expansions) >= 2:
        plt.axvline(expansions[1], color='grey', linestyle='--',
                    label=f"Target Ae/At ≈ {expansions[1]}")
    plt.xlabel('Nozzle Expansion Ratio (Ae/At)')
    plt.ylabel('Estimated Isp (s)')
    plt.title('Estimated Isp vs Nozzle Expansion Ratio')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    path = os.path.join(figures_dir, "nozzle_expansion_ratio_plot.png")
    plt.savefig(path, dpi=300, facecolor='white')
    plt.close()
    print(f"Saved nozzle plot: {path}")

def generate_tradeoff_table(figures_dir='figures'):
    os.makedirs(figures_dir, exist_ok=True)
    criteria = ['Relative mass', 'Tech maturity', 'Hermeticity / H₂ permeation risk', 'Production cost', 'Repairability']
    al_li = ['1.0×', 'High', 'Low risk', 'Moderate', 'Better']
    cfrp = ['0.70-0.85×', 'Medium/Low', 'Higher risk', 'Higher', 'Harder']
    table_data = list(zip(criteria, al_li, cfrp))

    fig, ax = plt.subplots(figsize=(8,4))
    ax.axis('tight')
    ax.axis('off')
    tbl = ax.table(cellText=table_data,
                   colLabels=['Criterion', 'Al-Li (baseline)', 'CFRP + liner'],
                   cellLoc='center', loc='center')
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(10)
    tbl.scale(1,1.5)
    plt.title('Material & Technology Trade-off: Al-Li vs CFRP+liner')
    plt.tight_layout()
    path = os.path.join(figures_dir, "tw_vs_mass_tradeoff_table.png")
    plt.savefig(path, dpi=300, facecolor='white')
    plt.close()
    print(f"Saved trade-off table: {path}")

def main():
    cfg = load_config('config.yaml')
    print("Loaded configuration:", cfg)
    generate_engine_schematic()
    generate_nozzle_plot(cfg)
    generate_tradeoff_table()
    print("All figures generated.")

if __name__ == '__main__':
    main()
