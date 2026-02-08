# Two-resistor debounce time calculator
R1 = 10000    # ohms series resistor
R2 = 100000      # ohms pullup resistor
C  = 1e-6       # farads

t_ms = (R1 * R2 / (R1 + R2)) * C * 1000
print(f"Debounce time: {t_ms:.2f} ms")

#test