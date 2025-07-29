class Aerio:
    def __init__(self, new, recharge, assistant, other):
        self.new = new
        self.recharge = recharge
        self.assistant = assistant
        self.other = other


mainMenu = """
*Olá caro Cliente, seja bem vindo ao assistente do ÓuGás*
*Somos a maior companhia de gás do Brasil, piscou o gás está em suas mãos*

Para melhorar o atendimento, precisarei coletar algumas informações suas, como *nome*, *telefone* e *endereço*
durante a escolha das opções!.

Não se preocupe, seus dados estão seguros e serão utilizados apenas para a compra do gás!!!.

Como podemos te ajudar? (digite apenas o numero da opção)
*1- Comprar um gás novo:* Enviaremos um gás novo em folha.
*2- Recarga de gás:* Realizaremos a coleta e a recarga do seu gás.
*3- Assistência técnica:* Enviareos uma equipe técnica especializada para resolvermos seu problema.
*4- Outro serviço*
*9- Resetar Bot*
*10- Finalizar...*
"""


gasMenu = """
Muito obrigado pela preferência conosco! :)

Por favor, escreva os dados solicitados em uma única mensagem e escolha uma das opções abaixo!

Escolha o tipo de gás!
*1- Gás de cozinha:* gás + botijão.
*2- Gás portátil:* gás + botijão.
*9- Voltar ao menu*
"""


rechargeMenu = """
Muito obrigado pela preferência conosco! :)

Por favor, escreva os dados solicitados em uma única mensagem e escolha uma das opções abaixo!

Escolha o tipo de gás para recarga!
*1- Gás de cozinha:* recarga.
*2- Gás portátil:* recarga.
*3- Gás de empilhadeira:* recarga.
*9- Voltar ao menu*
"""


assistantMenu = """
Muito obrigado pela preferência conosco! :)

Por favor, escreva os dados solicitados em uma única mensagem e escolha uma das opções abaixo!

*1- Vazamentos* 
*2- Montagem*
*3- Outra assistência*
*9- Voltar ao menu*
"""


otherMenu = """
Muito obrigado pela preferência conosco! :)

Para outras opções ligue para ########### (tel. fixo ou celular) ou ############# (apenas para tel. fixo). 
Ficarei feliz em te ajudar por lá!

Você deseja conversar com um atendente?
*1- Sim* 
*9- Não, voltar ao menu*
"""