import numpy as np
import matplotlib.pyplot as plt

# базовые данные
Pc = 20e6            # Pa, камера сгорания
Ae_At_first = 30     # расширение первой ступени
Ae_At_upper = 60     # расширение верхней ступени
TW_target = 80       # Тяга/масса, Н/кг

# Пример простого графика зависимости расширения сопла
expansions = np.array([10, 20, 30, 40, 50, 60, 70])
isp_first = 300 + 0.5*(expansions - 10)    # упрощённый пример зависимости Isp от Ae/At
isp_upper = 420 + 0.6*(expansions - 10)

plt.figure(figsize=(8,5))
plt.plot(expansions, isp_first, label='First Stage (LOX+RP-1)')
plt.plot(expansions, isp_upper, label='Upper Stage (LOX+LH2)')
plt.axvline(Ae_At_first, color='grey', linestyle='--')
plt.axvline(Ae_At_upper, color='grey', linestyle='--')
plt.xlabel('Nozzle Expansion Ratio Ae/At')
plt.ylabel('Estimated Isp (s)')
plt.title('Estimated Isp vs Nozzle Expansion Ratio')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('../figures/nozzle_expansion_ratio_plot.png', dpi=300)
plt.show()
