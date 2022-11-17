from fastapi import FastAPI
from decouple import config
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


app = FastAPI(title="Notification Service")


@app.get("/")
def inicio():
    home_page="""
        <h3>Esta es la pagina principal</h3>
        <h4><a href='./docs'>ir a docs</a></h4>
    """
    return home_page


#implementacion gets
@app.get("/mailpassword")
def sendmailpassword(receivermail):
    destino = receivermail
    asunto = "Reestablecimiento password Mascota Feliz"
    mensaje = """
    <h1>Este es un correo de Reestablecimiento de contraseña</h1>
    """
   
    message = Mail(
    from_email='seguraedwin5@gmail.com',
    to_emails=destino,
    subject=asunto,
    html_content=mensaje)
    try:
        sg = SendGridAPIClient(config('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        return "Correo enviado"
    except Exception as e:
        print(e.message)
        return "Error enviando correo"
