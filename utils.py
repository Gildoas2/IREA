import base64

def respuesta_openai(client, file, mensaje):
    # Verificar si el archivo no es None
    if file is None:
        raise ValueError("El archivo proporcionado es None")

    try:
        # Leer el contenido del archivo
        file_content = file.read()
        
        # Transformar la imagen en base 64
        imagenbase64 = base64.b64encode(file_content).decode('utf-8')
    except Exception as e:
        raise ValueError(f"Error al procesar el archivo: {e}")

    chat_completions = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": mensaje},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{imagenbase64}"},
                    },
                ],
            }
        ],
        max_tokens=300,
    )
    return chat_completions.choices[0].message.content