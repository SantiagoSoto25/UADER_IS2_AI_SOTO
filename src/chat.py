import openai

# Configura tu clave de API de OpenAI
openai.api_key = "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"

def chatGPT_respuesta(consulta):
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

def main():
    # Solicita la consulta al usuario
    consulta_usuario = input("Por favor, ingresa tu consulta: ")

    # Verifica si la consulta tiene texto
    if consulta_usuario.strip():
        # Imprime la consulta del usuario con el prefijo "You:"
        print("You:", consulta_usuario)

        # Obtiene la respuesta de chatGPT
        respuesta_chatGPT = chatGPT_respuesta(consulta_usuario)

        # Imprime la respuesta de chatGPT con el prefijo "chatGPT:"
        print("chatGPT:", respuesta_chatGPT)
    else:
        print("La consulta está vacía. Por favor, ingresa una consulta válida.")

if __name__ == "__main__":
    main()
