
from flask import Flask, request
from twilio_clients import client, my_phoneNumber, snd_phoneNumber
from twilio.twiml.messaging_response import MessagingResponse
from message_handler import mainMenu, assistantMenu, otherMenu
from message_handler import gasMenu, rechargeMenu, Aerio


# Instantiate the Flask Class
app = Flask(__name__)

# Initial Message
def sendInitialMessage():
    msg = client.messages.create(
        body=mainMenu,
        from_=my_phoneNumber,
        to=snd_phoneNumber,
    )

    # Debug
    print(f"Sending Message to {snd_phoneNumber}, from {my_phoneNumber}")
    print(msg.body)


# Current user state (selecting the color, selecting the size, etc)
user_state = {}

# Handle the incoming messages
@app.route("/reply_wpp", methods=['POST'])
def reply_msg():
    sender = request.form.get('From')  # The phone number of the client
    # Get the input from whatsapp
    incomingMsg = request.form.get('Body', '').strip().lower()

    if sender not in user_state:
        user_state[sender] = {'aerio': Aerio("", "", "", ""), 'in_menu': True}

    aerio = user_state[sender]['aerio']

    # Create a new Twilio MessagingResponse
    resp = MessagingResponse()

    if user_state[sender].get('selecting_gas'):
        aerio = newGas(aerio, incomingMsg)
        user_state[sender]['selecting_gas'] = False

        resp.message(f"Cor {aerio.new} selecionada!\n{mainMenu}")
    elif user_state[sender].get('selecting_recharge'):
        aerio = rechargeGas(aerio, incomingMsg)
        user_state[sender]['selecting_recharge'] = False

        resp.message(f"Tamanho {aerio.recharge} selecionado!\n{mainMenu}")
    elif user_state[sender].get('selecting_assistant'):
        aerio = assistantGas(aerio, incomingMsg)
        user_state[sender]['selecting_assistant'] = False

        resp.message(f"Entrega por {aerio.assistant} selecionada!\n{mainMenu}")
    elif user_state[sender].get('selecting_other'):
        aerio = otherService(aerio, incomingMsg)
        user_state[sender]['selecting_other'] = False

        resp.message(f"Entrega por {aerio.other} selecionada!\n{mainMenu}")
    else:
        match incomingMsg:
            case "1":
                user_state[sender]['selecting_gas'] = True
                resp.message(gasMenu)
            case "2":
                user_state[sender]['selecting_recharge'] = True
                resp.message(rechargeMenu)
            case "3":
                user_state[sender]['selecting_assistant'] = True
                resp.message(assistantMenu)
            case "4":
                user_state[sender]['selecting_other'] = True
                resp.message(otherMenu)
            case "9":
                user_state[sender] = {'aerio': Aerio(
                    "", "", "", ""), 'in_menu': True}
                resp.message(
                    f"Conversa resetada. Digite uma opção: \n{mainMenu}")
            case "10":
                resp.message(
                    "Finalizando.."
                )

                #arrumar no futuro, saida ;D
            case _:
                resp.message("Opção inválida. " + mainMenu)

    return str(resp)


# Takes the user to the differente menus and define the attributes of the
# shopping order
def newGas(aerio, incomingMsg):

    match incomingMsg:
        case "1" | "gás de cozinha":
            aerio.new = "Cozinha"
            return aerio
        case "2" | "gás portátil":
            aerio.new = "Portatil"
            return aerio
        case "9" | "menu":
            aerio.new = ""
            return aerio


def rechargeGas(aerio, incomingMsg):

    match incomingMsg:
        case "1" | "gás de cozinha":
            aerio.recharge = "recargaCozinha"
            return aerio
        case "2" | "gás portatil":
            aerio.recharge = "recargaPortatil"
            return aerio
        case "3" | "gás de empilhadeira":
            aerio.recharge = "recargaEmpilhadeira"
            return aerio
        case "9" | "menu":
            aerio.other = ""
            return aerio

def assistantGas(aerio, incomingMsg):

    match incomingMsg:
        case "1" | "vazamentos":
            aerio.assistant = "Vazamento"
            return aerio
        case "2" | "montagem":
            aerio.assistant = "Montagem"
            return aerio
        case "3" | "outro":
            aerio.assistant = "Outro"
            return aerio
        case "9" | "menu":
            aerio.other = ""
            return aerio

def otherService(aerio, incomingMsg):

    match incomingMsg:
        case "1" | "sim":
            aerio.other = "Sim"
            return aerio
        case "9" | "não":
            aerio.other = ""
            return aerio


def runApp():
    app.run(port=3000)

