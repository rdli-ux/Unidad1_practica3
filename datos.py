import json 

Archivo_Datos = "Inventario.json"
 
def cargar_datos():
    try:
        with open(Archivo_Datos, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def guardar_datos(inventario):
    with open(Archivo_Datos, "w", encoding="utf-8") as archivo:
        json.dump(inventario, archivo, indent=4, ensure_ascii=False)
        