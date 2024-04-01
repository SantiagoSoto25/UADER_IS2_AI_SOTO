import argparse
import openai

# Configura tu clave de API de OpenAI
openai.api_key = 'tu-clave-de-api'

# Variable global para almacenar el buffer de conversación
buffer_conversacion = []
ultima_consulta = ""

def chatGPT_respuesta(consulta):
    global ultima_consulta  # Accede a la variable global
    try:
        # Envía la consulta al modelo de chatGPT
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "user", "content": consulta}
            ],
            temperature=0.7,
            max_tokens=150
        )
        ultima_consulta = consulta  # Actualiza la última consulta
        return respuesta.choices[0].message['content'].strip()
    except Exception as e:
        print("Error al invocar el modelo de chatGPT:", e)
        return None

def main():
    global buffer_conversacion  # Accede a la variable global
    global ultima_consulta  # Accede a la variable global

    # Configura el parser de argumentos de línea de comandos
    parser = argparse.ArgumentParser(description='ChatGPT')
    parser.add_argument('--convers', action='store_true', help='Activa el modo de conversación')
    args = parser.parse_args()

    if args.convers:
        print("Modo de conversación activado.")
    else:
        print("Modo de conversación desactivado.")

    while True:
        try:
            # Solicita la consulta al usuario
            consulta_usuario = input("Por favor, ingresa tu consulta (o 'exit' para salir): ")

            # Verifica si el usuario quiere salir
            if consulta_usuario.lower() == 'exit':
                print("Saliendo del programa...")
                break

            # Verifica si la consulta tiene texto
            if consulta_usuario.strip():
                # Imprime la consulta del usuario con el prefijo "You:"
                print("You:", consulta_usuario)
                
                # Agrega la consulta al buffer de conversación
                buffer_conversacion.append(consulta_usuario)

                # Obtiene la respuesta de chatGPT usando la última consulta o todas las anteriores
                respuesta_chatGPT = chatGPT_respuesta("\n".join(buffer_conversacion))

                if respuesta_chatGPT:
                    # Imprime la respuesta de chatGPT con el prefijo "chatGPT:"
                    print("chatGPT:", respuesta_chatGPT)

                    # Agrega la respuesta de chatGPT al buffer de conversación para reenviarla en próximas consultas
                    buffer_conversacion.append(respuesta_chatGPT)
                else:
                    print("No se pudo obtener una respuesta del modelo.")
            else:
                print("La consulta está vacía. Por favor, ingresa una consulta válida.")
        except KeyboardInterrupt:
            # Captura la excepción de interrupción del teclado (cursor Up)
            print("\nEditando última consulta:", ultima_consulta)
            consulta_usuario = input("Edita tu consulta o presiona 'Enter' para enviar la misma: ")
            if consulta_usuario.strip():
                ultima_consulta = consulta_usuario  # Actualiza la última consulta con la nueva
            continue
        except Exception as e:
            print("Error en la ejecución del programa:", e)

if __name__ == "__main__":
    main()
