import openai

# Configura tu clave de API de OpenAI
openai.api_key = "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"

# Variable global para almacenar la última consulta
ultima_consulta = ""

def chatGPT_respuesta(consulta):
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
        return respuesta.choices[0].message['content'].strip()
    except Exception as e:
        print("Error al invocar el modelo de chatGPT:", e)
        return None

def main():
    global ultima_consulta  # Accede a la variable global

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
                ultima_consulta = consulta_usuario  # Actualiza la última consulta

                # Obtiene la respuesta de chatGPT
                respuesta_chatGPT = chatGPT_respuesta(consulta_usuario)

                if respuesta_chatGPT:
                    # Imprime la respuesta de chatGPT con el prefijo "chatGPT:"
                    print("chatGPT:", respuesta_chatGPT)
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
