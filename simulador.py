import tkinter
from tkinter import ttk
import math

def calcular_tiempo_espera():
    """
    Calcula y muestra el tiempo promedio de espera en el sistema de colas y otros parámetros.

    Obtiene los datos de entrada del usuario, realiza validaciones, calcula la probabilidad de que no haya clientes
    en el sistema, el número promedio de clientes en el sistema, el tiempo promedio de espera en el sistema, y el
    tiempo promedio de espera en la línea. Luego, muestra los resultados en la interfaz gráfica.
    """
    # Obtener los datos ingresados
    try:
        tasa_llegada = float(tasa_llegada_entry.get())
        tasa_servicio = float(tasa_servicio_entry.get())
        num_servidores = int(num_servidores_entry.get())
    except ValueError:
        resultado_label.config(text="Error: Por favor, ingresa valores numéricos válidos.")
        return

    # Validar las entradas del usuario
    if tasa_llegada < 0 or tasa_servicio <= 0 or num_servidores <= 0:
        resultado_label.config(text="Error: Las tasas deben ser positivas, y el número de servidores debe ser mayor que cero.")
        return

    # Calcular la probabilidad de que no haya clientes en el sistema
    rho = tasa_llegada / (tasa_servicio * num_servidores)
    if rho >= 1:
        resultado_label.config(text="El sistema está en estado crítico (rho >= 1). No se pueden calcular los tiempos de espera.")
        return

    p0 = 1 / (sum([(rho ** k) / math.factorial(k) for k in range(num_servidores + 1)]) +
              (rho ** num_servidores) / (math.factorial(num_servidores) * (1 - rho / num_servidores)))

    # Calcular el número promedio de clientes en el sistema
    ls = rho * (1 - p0)

    # Verificar si 1 - p0 es cero antes de la división
    if tasa_llegada * (1 - p0) == 0:
        resultado_label.config(text="Error: División por cero en el cálculo del tiempo de espera.")
        return

    # Calcular el tiempo promedio de espera en el sistema
    ws = ls / (tasa_llegada * (1 - p0))

    # Calcular el tiempo promedio de espera en la línea
    wq = ws - 1 / (tasa_servicio * num_servidores)

    # Mostrar los resultados
    resultado_label.config(text=f"Probabilidad de que no haya clientes en el sistema: {p0:.4f}\n"
                                f"Número promedio de clientes en el sistema: {ls:.4f}\n"
                                f"Tiempo promedio de espera en el sistema: {ws:.4f} horas\n"
                                f"Tiempo promedio de espera en la línea: {wq:.4f} horas")

# Crear la ventana principal
root = tkinter.Tk()
root.title("Simulador de líneas de espera")
root.geometry("800x600")
root.configure(bg="#f0f0f0")

# Usar un tema moderno
style = ttk.Style()
style.theme_use("alt")

# Personalizar colores y fuentes
style.configure("TLabel", background="#f0f0f0", foreground="#333333", font=("Segoe UI", 12))
style.configure("TEntry", fieldbackground="white", font=("Segoe UI", 12))
style.configure("TButton", font=("Segoe UI", 12))
style.map("TButton", background=[("active", "#4d9fe6"), ("!active", "#4d9fe6")])

# Crear las etiquetas y entradas para los datos de entrada
tasa_llegada_label = ttk.Label(root, text="Tasa de llegada (clientes/hora):")
tasa_llegada_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
tasa_llegada_entry = ttk.Entry(root)
tasa_llegada_entry.grid(row=0, column=1, padx=10, pady=10)

tasa_servicio_label = ttk.Label(root, text="Tasa de servicio (clientes/hora/servidor):")
tasa_servicio_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
tasa_servicio_entry = ttk.Entry(root)
tasa_servicio_entry.grid(row=1, column=1, padx=10, pady=10)

num_servidores_label = ttk.Label(root, text="Número de servidores:")
num_servidores_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
num_servidores_entry = ttk.Entry(root)
num_servidores_entry.grid(row=2, column=1, padx=10, pady=10)

# Crear el botón para calcular
calcular_button = ttk.Button(root, text="Calcular", command=calcular_tiempo_espera)
calcular_button.grid(row=3, column=0, columnspan=2, padx=10, pady=20)
calcular_button.configure(style='Accent.TButton')

# Crear la etiqueta para mostrar los resultados
resultado_frame = ttk.Frame(root, relief="groove", borderwidth=2, padding=10)
resultado_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
resultado_label = ttk.Label(resultado_frame, text="", font=("Segoe UI", 16), wraplength=700, justify="left")
resultado_label.pack()

# Mostrar información de los integrantes
integrantes_label = ttk.Label(root, text="Integrantes:\nÁlvarez García Damaris Lizet\nEsquivel Flores Jonathan\nOrtiz Ceballos Jorge", font=("Segoe UI", 14), background="#f0f0f0")
integrantes_label.grid(row=5, column=0, columnspan=2, padx=10, pady=20)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
