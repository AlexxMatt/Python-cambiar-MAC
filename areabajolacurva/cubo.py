import matplotlib.pyplot as plt
import numpy as np

# Definir la función
def f(x):
    return x**2

# Definir el intervalo de integración
a, b = 0, 3

# Calcular el área usando la regla del trapecio
n = 1000
x = np.linspace(a, b, n+1)
y = f(x)
h = (b-a)/n
area = (h/2)*(y[0] + 2*np.sum(y[1:n]) + y[n])

# Mostrar el resultado de la función y el área
print("Resultado de la función en x=2:", f(2))
print("Área bajo la curva:", area)

# Graficar la función y los puntos dentro y fuera de la curva
puntos_x = np.random.uniform(a, b, 1000)
puntos_y = np.random.uniform(0, 9, 1000)
puntos_dentro = puntos_y <= f(puntos_x)
puntos_fuera = puntos_y > f(puntos_x)

fig, ax = plt.subplots()
ax.scatter(puntos_x[puntos_dentro], puntos_y[puntos_dentro], c='b', alpha=0.5)
ax.scatter(puntos_x[puntos_fuera], puntos_y[puntos_fuera], c='r', alpha=0.5)
ax.plot(x, y, color='k')
ax.set_xlim([0, 3])
ax.set_ylim([0, 9])
plt.show()
