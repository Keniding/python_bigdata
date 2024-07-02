import json
import random
from datetime import datetime, timedelta

# Generar un nombre aleatorio
def generar_nombre():
    nombres = ["Juan", "María", "Carlos", "Ana", "Luis", "Sofía", "Miguel", "Lucía", "Pedro", "Elena"]
    apellidos = ["García", "Martínez", "Rodríguez", "López", "Sánchez", "Pérez", "Gómez", "Fernández", "González", "Ruiz"]
    return f"{random.choice(nombres)} {random.choice(apellidos)}"

# Generar un correo electrónico aleatorio
def generar_correo(nombre):
    dominios = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
    nombre_correo = nombre.lower().replace(" ", ".")
    return f"{nombre_correo}@{random.choice(dominios)}"

# Generar una fecha aleatoria con distribución normal
def generar_fecha_normal(inicio, fin):
    delta = fin - inicio
    media = delta.days / 2
    sigma = delta.days / 6  # Aproximadamente el 99.7% de los datos caerán dentro de ±3 sigma
    dias = int(random.normalvariate(media, sigma))
    dias = max(0, min(delta.days, dias))  # Asegurarse de que los días estén dentro del rango
    return inicio + timedelta(days=dias)

# Generar respuestas aleatorias de sí/no con distribución normal
def generar_respuesta_si_no():
    return random.choices(["Sí", "No"], weights=[0.7, 0.3])[0]  # 70% Sí, 30% No

# Generar una respuesta aleatoria para preguntas específicas
def generar_respuesta_especifica():
    respuestas = [
        "Me interesa aprender nuevas recetas.",
        "Quisiera recibir productos frescos a domicilio.",
        "Estoy buscando opciones saludables para mi dieta.",
        "Me gustaría recibir productos orgánicos.",
        "Estoy interesado en opciones vegetarianas.",
        "Quiero probar diferentes tipos de cocina.",
        "Estoy buscando ahorrar tiempo en la preparación de comidas.",
        "Me interesa la sostenibilidad y productos eco-friendly.",
        "Quisiera recibir recetas con instrucciones paso a paso.",
        "Estoy buscando opciones económicas para mi alimentación."
    ]
    return random.choice(respuestas)

# Generar un género aleatorio con distribución realista
def generar_genero():
    return random.choices(["Femenino", "Masculino", "Otro"], weights=[0.6, 0.35, 0.05])[0]  # 60% Femenino, 35% Masculino, 5% Otro

# Generar una edad aleatoria
def generar_edad():
    return random.randint(18, 65)

# Generar un número de teléfono aleatorio único
def generar_telefono(unicos):
    while True:
        telefono = f"+52 {random.randint(900000000, 999999999)}"
        if telefono not in unicos:
            unicos.add(telefono)
            return telefono

# Generar registros de formularios
def generar_registros(total_registros, inicio, fin):
    registros = []
    telefonos_unicos = set()
    for _ in range(total_registros):
        nombre = generar_nombre()
        fecha = generar_fecha_normal(inicio, fin)
        telefono = generar_telefono(telefonos_unicos)
        registro = {
            "datos_entrevistado": {
                "nombre": nombre,
                "correo": generar_correo(nombre),
                "fecha": fecha.strftime("%Y-%m-%d"),
                "genero": generar_genero(),
                "edad": generar_edad(),
                "telefono": telefono
            },
            "preguntas_filtro": {
                "interes_servicios_hellofresh": generar_respuesta_si_no(),
                "interes_productos_primarios": generar_respuesta_si_no(),
                "interes_cocinar_en_casa": generar_respuesta_si_no(),
                "frecuencia_cocina": random.choice(["Diario", "Semanal", "Mensual", "Ocasional"]),
                "preferencia_comida_casera": generar_respuesta_si_no()
            },
            "preguntas_especificas": {
                "interes_nuevas_recetas": generar_respuesta_especifica(),
                "interes_productos_frescos": generar_respuesta_especifica(),
                "interes_opciones_saludables": generar_respuesta_especifica(),
                "interes_productos_organicos": generar_respuesta_especifica(),
                "interes_opciones_vegetarianas": generar_respuesta_especifica()
            }
        }
        registros.append(registro)
    return registros

# Parámetros de generación
total_registros = 5000
inicio = datetime(datetime.now().year - 1, 1, 1)
fin = datetime.now()

# Generar los registros y guardarlos en un archivo JSON
registros = generar_registros(total_registros, inicio, fin)
with open("registros_hellofresh.json", "w", encoding="utf-8") as archivo:
    json.dump(registros, archivo, ensure_ascii=False, indent=4)

print(f"Se han generado {total_registros} registros de formularios.")
