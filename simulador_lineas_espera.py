import tkinter as tk
from tkinter import ttk
from tkinter import font

def calcular_tiempo_espera():
    # Obtener los datos ingresados
    tasa_llegada = float(tasa_llegada_entry.get())
    tasa_servicio = float(tasa_servicio_entry.get())
    num_servidores = int(num_servidores_entry.get())

    # Calcular la probabilidad de que no haya clientes en el sistema
    rho = tasa_llegada / (tasa_servicio * num_servidores)
    p0 = 1 / (sum([(rho ** k) / factorial(k) for k in range(num_servidores + 1)]) + (rho ** num_servidores) / (factorial(num_servidores) * (1 - rho / num_servidores)))

    # Calcular el número promedio de clientes en el sistema
    ls = rho * (1 - p0)

    # Calcular el tiempo promedio de espera en el sistema
    ws = ls / (tasa_llegada * (1 - p0))

    # Calcular el tiempo promedio de espera en la línea
    wq = ws - 1 / (tasa_servicio * num_servidores)

    # Mostrar los resultados
    resultado_label.config(text=f"Probabilidad de que no haya clientes en el sistema: {p0:.4f}\n"
                                f"Número promedio de clientes en el sistema: {ls:.4f}\n"
                                f"Tiempo promedio de espera en el sistema: {ws:.4f} horas\n"
                                f"Tiempo promedio de espera en la línea: {wq:.4f} horas")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Crear la ventana principal
root = tk.Tk()
root.title("Simulador de líneas de espera")
root.geometry("500x400")  # Establecer el tamaño de la ventana
root.configure(bg="#f0f0f0")  # Establecer el color de fondo

# Crear un estilo personalizado
style = ttk.Style()
style.theme_use("clam")  # Usar un tema atractivo

# Crear las etiquetas y entradas para los datos de entrada
tasa_llegada_label = ttk.Label(root, text="Tasa de llegada (clientes/hora):", font=("Arial", 12))
tasa_llegada_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
tasa_llegada_entry = ttk.Entry(root, font=("Arial", 12))
tasa_llegada_entry.grid(row=0, column=1, padx=10, pady=10)

tasa_servicio_label = ttk.Label(root, text="Tasa de servicio (clientes/hora/servidor):", font=("Arial", 12))
tasa_servicio_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
tasa_servicio_entry = ttk.Entry(root, font=("Arial", 12))
tasa_servicio_entry.grid(row=1, column=1, padx=10, pady=10)

num_servidores_label = ttk.Label(root, text="Número de servidores:", font=("Arial", 12))
num_servidores_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
num_servidores_entry = ttk.Entry(root, font=("Arial", 12))
num_servidores_entry.grid(row=2, column=1, padx=10, pady=10)

# Crear el botón para calcular
calcular_button = ttk.Button(root, text="Calcular", command=calcular_tiempo_espera, style="Accent.TButton")
calcular_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Crear la etiqueta para mostrar los resultados
resultado_label = ttk.Label(root, text="", font=("Arial", 12), wraplength=400, justify="left")
resultado_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()