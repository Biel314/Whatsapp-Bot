from flask import Flask, request, Response
from twilio_clients import client, my_phoneNumber, snd_phoneNumber
from twilio.twiml.messaging_response import MessagingResponse
from message_handler import mainMenu, deliveryMenu, sizeMenu, colorMenu, Bicicleta


# Instantiate the Flask Class
app = Flask(__name__)


# Debug handling variables (to reset the bot)
user = True
color = ""
size = ""
deliveryOpt = ""


# Initial Message
def sendInitialMessage():
    msg = client.messages.create(
        body=mainMenu,
        from_=my_phoneNumber,
        to=snd_phoneNumber,
    )

    # Debug
    print(msg.body)


# Handle the incoming messages
@app.route("/reply_wpp", methods=['POST'])
def reply_msg():

    # Get the input from whatsapp
    incomingMsg = request.form.get('Body', '').strip().lower()

    # The choosen option inside @menuHandling
    bike = Bicicleta("", "", "")

    # Create a new Twilio MessagingResponse
    resp = MessagingResponse()

    # Bot Logic
    match incomingMsg:
        case "1":
            resp.message(colorMenu)
            bike = menuHandling(incomingMsg)
            print("teste cor")
        case "2":
            resp.message(sizeMenu)
            bike = menuHandling(incomingMsg)
            print("teste tamanho")
        case "3":
            resp.message(deliveryMenu)
            bike = menuHandling(incomingMsg)
            print("teste delivery")
        case "4":
            resp.message(f"cor da bicicleta {bike.color} \n " +
                         f"tamanho {bike.size} \n " +
                         f"metodo de envio {bike.delivery}")
        case "9":
            resp.message("Finalizando...")
            bike = Bicicleta("", "", "")
            sendInitialMessage()
            print("teste 9")
        case _:
            print("opcao invalida")

    # Return the TwiML (as XML) response
    return Response(str(resp), mimetype='text/xml')


# Takes the user to the differente menus and define the attributes of the
# shopping order
def menuHandling(opt):
    # Get the input from whatsapp
    incomingMsg = request.form.get('Body', '').strip().lower()


def runApp():
    app.run(port=3000)


if __name__ == "__main__":
    runApp()
