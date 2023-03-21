import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Define the input variable range
squareMeters = np.arange(0, 180)

# Define the fuzzy sets for the input variable
squareMetersLow = fuzz.trapmf(squareMeters, [0, 0, 15, 30])
squareMetersMedium = fuzz.trimf(squareMeters, [20, 45, 75])
squareMetersHigh = fuzz.trapmf(squareMeters, [60, 90, 180, 180])

# Plot the membership functions for the input variable
plt.figure(figsize=(8, 4))
plt.plot(squareMeters, squareMetersLow, 'b', linewidth=1.5, label='Low')
plt.plot(squareMeters, squareMetersMedium, 'g', linewidth=1.5, label='Medium')
plt.plot(squareMeters, squareMetersHigh, 'r', linewidth=1.5, label='High')
plt.title('Kambario dydis')
plt.ylabel('abc')
plt.xlabel('Kambario dydis. kv. m.')
plt.legend()
plt.show()
