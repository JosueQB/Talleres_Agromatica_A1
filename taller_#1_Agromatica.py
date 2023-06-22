import os
Lv_Ruta = "C:/Agromatica_A1"

try:
    os.mkdir(Lv_Ruta)
    print("Direcctorio creado exitosamente.")
except OSError as OErr:
    print(f"Error al generar el archivo:, Err:{OErr}")