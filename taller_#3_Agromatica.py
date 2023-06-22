from pathlib import Path

Lv_NombreArchivo = Path("C:/Agromatica_A1/22062023_02.txt")

with Lv_NombreArchivo.open(mode="w") as file:
    file.write("esta es mi segundo archivo de texto\n")
    file.write("esta es mi primer linea de archivo de texto\n")
    file.write("\testa es mi segunda linea de archivo de texto")

# con el metodo with no necesito cerrar el archivo close.file ya no es necesario.
