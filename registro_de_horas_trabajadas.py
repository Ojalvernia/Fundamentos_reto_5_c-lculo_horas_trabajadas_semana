# Función para validar el ingreso de horas
def solicitar_horas(dia):
    while True:
        try:
            horas = float(input(f"Horas trabajadas el {dia}: "))

            if horas < 0:
                print("Error: No se permiten valores negativos.")
            elif horas > 24:
                print("Error: No se pueden registrar más de 24 horas en un día.")
            else:
                return horas

        except ValueError:
            print("Error: Debe ingresar únicamente valores numéricos.")


# Función para calcular el total de horas semanales
def calcular_horas_semanales(horas):
    return sum(horas)


# Función para clasificar la jornada laboral
def clasificar_jornada(total_horas):
    if total_horas > 40:
        return "Sobretiempo"
    else:
        return "Horario estándar"


# Matriz para almacenar la información de los trabajadores
trabajadores = []

# Captura de datos de 4 trabajadores
for i in range(4):
    print(f"\n--- Trabajador {i + 1} ---")

    nombre = input("Ingrese el nombre del trabajador: ")

    lunes = solicitar_horas("lunes")
    martes = solicitar_horas("martes")
    miercoles = solicitar_horas("miércoles")
    jueves = solicitar_horas("jueves")
    viernes = solicitar_horas("viernes")

    trabajadores.append([
        nombre,
        lunes,
        martes,
        miercoles,
        jueves,
        viernes
    ])

# Mostrar reporte final
print("\n" + "=" * 80)
print("REPORTE DE HORAS TRABAJADAS")
print("=" * 80)

print(f"{'Nombre':<20}{'Lunes':>8}{'Martes':>8}{'Miér.':>8}{'Jueves':>8}{'Viernes':>8}{'Total':>10}{'Estado':>20}")
print("-" * 80)

for trabajador in trabajadores:
    nombre = trabajador[0]
    horas = trabajador[1:]

    total_horas = calcular_horas_semanales(horas)
    clasificacion = clasificar_jornada(total_horas)

    print(
        f"{nombre:<20}"
        f"{horas[0]:>8.1f}"
        f"{horas[1]:>8.1f}"
        f"{horas[2]:>8.1f}"
        f"{horas[3]:>8.1f}"
        f"{horas[4]:>8.1f}"
        f"{total_horas:>10.1f}"
        f"{clasificacion:>20}"
    )

print("=" * 80)