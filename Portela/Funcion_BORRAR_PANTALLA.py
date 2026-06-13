
def limpiar_pantalla():
    # 'nt' corresponde a Windows
    if os.name == "nt":
        os.system("cls")
    # Para Linux y macOS
    else:
        os.system("clear")