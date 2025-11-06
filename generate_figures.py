import os
import numpy as np
import matplotlib.pyplot as plt

# Убедимся, что папка figures/ существует
figures_dir = "figures"
os.makedirs(figures_dir, exist_ok=True)

# 1. Engine schematic (упрощённая иллюстрация)
plt.figure(figsize=(8,4))
plt.plot([0.1, 0.3, 0.5, 0.7, 0.9], [0.5, 0.6, 0.5, 0.4, 0.3], '-o', color='#2E86C1')
plt.text(0.1, 0.5, "Oxidiser pump", ha='right', va='center')
plt.text(0.3, 0.6, "Fuel pump", ha='right', va='bottom')
plt.text(0.5, 0.5, "Combustion chamber", ha='center', va='center')
plt.text(0.7, 0.4, "Nozzle throat", ha='left', va='bottom')
plt.text(0.9, 0.3, "Nozzle exit", ha='left', va='center')
plt.title("Simplified Liquid-Propellant Rocket Engine Schematic")
plt.axis('off')
plt.tight_layout()
plt.savefig(os.path.join(figures_dir, "engine_schematic.png"), dpi=300, facecolor='white')
plt.close()

# 2. Nozzle expansion ratio vs estimated Isp
expansions = np.array([10,20,30,40,50,60,70])
isp_first = 300 + 0.5*(expansions - 10)      # упрощённая зависимость
isp_upper = 420 + 0.6*(expansions - 10)

plt.figure(figsize=(8,5))
plt.plot(expansions, isp_first, label='First stage (LOX+RP-1)', marker='o')
plt.plot(expansions, isp_upper, label='Upper stage (LOX+LH₂)', marker='o')
plt.axvline(30, color='grey', linestyle='--', label='Target Ae/At (first stage)')
plt.axvline(60, color='grey', linestyle='--', label='Target Ae/At (upper stage)')
plt.xlabel('Nozzle Expansion Ratio Ae/At')
plt.ylabel('Estimated Isp (s)')
plt.title('Estimated Isp vs Nozzle Expansion Ratio')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(figures_dir, "nozzle_expansion_ratio_plot.png"), dpi=300, facecolor='white')
plt.close()

# 3. T/W vs mass trade-off table as image
labels = ['Criterion', 'Al-Li (baseline)', 'CFRP + liner']
criteria = ['Relative mass', 'Tech maturity', 'Hermeticity/permeation risk', 'Production cost', 'Repairability']
al_li = ['1.0×', 'High', 'Low risk', 'Moderate', 'Better']
cfrp = ['0.70-0.85×', 'Medium/Low', 'Higher risk', 'Higher', 'Harder']
table_data = []
for crit, a, c in zip(criteria, al_li, cfrp):
    table_data.append([crit, a, c])

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
plt.savefig(os.path.join(figures_dir, "tw_vs_mass_tradeoff_table.png"), dpi=300, facecolor='white')
plt.close()
