import numpy as np
import math

x = 1 
y = 5

distancia_cm = np.hypot(x, y) * 100
angulo_graus = np.degrees(np.arctan2(y,x))
print(distancia_cm)
print(angulo_graus)
print(" ")
dist = math.sqrt(x**2 + y**2)*100
angulo = math.atan2(y,x)*(180/math.pi)
print(dist)
print(angulo)