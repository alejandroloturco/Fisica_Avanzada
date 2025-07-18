import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
import numpy as np
import time

def simular_datos(t, vot):
    #voltaje entre 0 y 5V (2.5)
    #voltaje entre -2.5 y 2.5V (0)
    señal_x = 2.5 * np.sin(2 * np.pi * 1 * t) + vot + 0.05 * np.random.randn()
    señal_y = 2.5 * np.sin(2 * np.pi * 1 * t + np.pi/4)+ vot + 0.05 * np.random.randn()

    return señal_x, señal_y

def actualizar(vot = 0):
    def update(frame):
        t_actual = time.time() - t0
        val_x, val_y = simular_datos(t_actual, float(vot))
        buffer_x.append(val_x)
        buffer_y.append(val_y)
        linea1.set_data(xdata, list(buffer_x))
        linea2.set_data(xdata, list(buffer_y))
        return linea1, linea2
    return update

frecuencia_muestreo = 125  # Hz
tiempo_ventana = 2  # segundos
n_muestras = frecuencia_muestreo * tiempo_ventana
t0 = time.time()

buffer_x = deque([0.0]*n_muestras, maxlen=n_muestras)
buffer_y = deque([0.0]*n_muestras, maxlen=n_muestras)       


while True:
    print("\n")
    print("Esperando a que se inicie la simulación...")
    print("Se realizara una simulacion.")
    print("1 - Valores entre 0V y 5V")
    print("2 - Valores entre -2.5V y 2.5V")
    print("3 - Salir")
    val = int(input("Seleccione una opción: "))
    fig, ax = plt.subplots()
    linea1, = ax.plot([],[], label='Derivación X')
    linea2, = ax.plot([],[], label='Derivación Y')
    ax.set_ylim(-2.5, 5.5)
    ax.set_xlim(0, tiempo_ventana)
    ax.set_title("Simulación de señales de derivaciones X y Y")
    ax.set_xlabel("Tiempo (s)")
    ax.set_ylabel("Voltaje (V)")
    ax.legend()
    xdata = [i / frecuencia_muestreo for i in range(n_muestras)]

    if val == 1:
        ani = animation.FuncAnimation(fig, actualizar(vot='2.5'), interval=1000/frecuencia_muestreo, blit=True)
        plt.tight_layout()
        plt.show()
        print("\n")
        print(" Simulacion realizada con valores entre 0V y 5V")
        
    elif val == 2:
        ani = animation.FuncAnimation(fig, actualizar(), interval=1000/frecuencia_muestreo, blit=True)
        plt.tight_layout()
        plt.show()
        print("\n")
        print(" Simulacion realizada con valores entre 0V y 5V")
                
    elif val == 3:
        print("Saliendo de la simulación...")
        break
    else:
        continue

