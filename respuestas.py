import difflib

def cargar_preguntas_y_respuestas(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        contenido = file.read()
    
    # Dividir el contenido en bloques de preguntas y respuestas
    bloques = contenido.split('\n\n')
    
    # Crear una lista de tuplas (pregunta, respuesta)
    qa_list = []
    for bloque in bloques:
        lineas = bloque.strip().split('\n')
        pregunta = lineas[0].strip()
        respuestas = [linea.strip() for linea in lineas[1:] if linea.strip().endswith('*')]
        respuesta_correcta = '\n'.join(respuestas).strip()
        qa_list.append((pregunta, respuesta_correcta))
    
    return qa_list

def encontrar_respuesta(qa_list, pregunta):
    mejor_coincidencia = None
    mayor_similitud = 0.0
    for qa in qa_list:
        similitud = difflib.SequenceMatcher(None, pregunta.lower(), qa[0].lower()).ratio()
        if similitud > mayor_similitud:
            mayor_similitud = similitud
            mejor_coincidencia = qa
    if mayor_similitud > 0.5:  # Umbral de similitud, ajustar según sea necesario
        return mejor_coincidencia[1]
    return "Pregunta no encontrada."

# Ruta al archivo de preguntas y respuestas
file_path = 'respuestas.txt'

# Cargar preguntas y respuestas
qa_list = cargar_preguntas_y_respuestas(file_path)

# Solicitar pregunta al usuario
while True:
    pregunta = input("Ingrese su pregunta (o 'salir' para terminar): ")
    if pregunta.lower() == 'salir':
        break
    respuesta = encontrar_respuesta(qa_list, pregunta)
    print("Pregunta:", pregunta)
    if respuesta != "Pregunta no encontrada.":
        print("Respuestas correctas:")
        for linea in respuesta.split('\n'):
            print(f"* {linea}")
    else:
        print(respuesta)
    print()  # Espacio adicional para mejor legibilidad
