# :> [!WARNING]-  ⚠️ AVISO! ⚠️ 
> 
> Esse é um branch de teste. Algumas funções podem não estar 100% funcionais. 
> Para garantir a funcionalidade total, fazer cloning ou pull da branch main.
>
> https://github.com/Biel314/Whatsapp-Bot/tree/main

---

# 📦 ÓuGás - WhatsApp Bot para Venda de Botijões de Gás  

**ÓuGás** é um sistema automatizado de atendimento via WhatsApp para revendedores de gás, desenvolvido em Python com a API da Twilio.  

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Twilio-F22F46?style=for-the-badge&logo=twilio&logoColor=white" alt="Twilio">
  <img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
</div>

## ✨ Funcionalidades  

- **Pedidos Automatizados**: Clientes solicitam botijões via mensagens no WhatsApp  
- **Banco de Dados JSON**: Armazena pedidos, clientes e histórico de vendas  
- **Respostas Inteligentes**: Reconhece intenções com processamento de linguagem natural (NLP básico)  
- **Multi-atendimento**: Gerencia vários clientes simultaneamente  

## 🛠️ Tecnologias  

| Componente       | Tecnologia          |  
|------------------|---------------------|  
| Backend          | Python 3.10+        |  
| API WhatsApp     | Twilio API          |  
| Armazenamento    | JSON                |  

## 📦 Estrutura do Projeto  

```
Whatsapp-Bot/  
├── data/  
│   ├── clients.json       # Dados dos clientes  
│   └── orders.json        # Histórico de pedidos  
├── src/  
│   ├── bot.py             # Lógica principal  
│   ├── message_handler.py # Processa mensagens  
│   └── twilio_client.py   # Configuração da API  
├── requirements.txt       # Dependências  
└── README.md              # Este arquivo  
```

## 🚀 Como Executar  

1. **Clone o repositório**:  
   ```bash
   git clone https://github.com/Biel314/Whatsapp-Bot  
   cd Whatsapp-Bot
    ```

2. **Instale as dependências**:  
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure as variáveis de ambiente**:  
   Crie um arquivo `.env` dentro de `src/` com:  
   ```
   TWILIO_ACCOUNT_SID="seu_sid_twilio"
   TWILIO_AUTH_TOKEN="seu_token_twilio"
   TWILIO_PHONE_NUMBER="whatsapp:+5511999999999"
   ```

4. **Execute o bot**:  
   ```bash
   python src/bot.py
   ```

## 🤖 Fluxo de Atendimento  

```mermaid
sequenceDiagram
    Cliente->>+GasBot: "Quero comprar um botijão"
    GasBot->>+Cliente: "Qual seu CEP para verificar entrega?"
    Cliente->>+GasBot: "01234-567"
    GasBot->>+Cliente: "Disponível! 13kg por R$90. Confirma?"
    Cliente->>+GasBot: "Sim"
    GasBot->>Sistema: Registra pedido no JSON
    GasBot->>+Cliente: "Pedido #123 confirmado! 🚚"
```

### ✨ Destaques Técnicos  
- **Twilio Webhooks**: Recebe mensagens em tempo real  
- **Padrão Factory**: Para criar diferentes respostas  
- **Logging**: Registro de todas as interações  

---

<div align="center">
  ✉️ Contato: <a href="mailto:gabrieldeoliveiralimasilva@gmail.com">gabrieldeoliveiralimasilva@gmail.com </a> <br> 
  🌐 Site: <a href="https://gabrielgit10110.github.io/">https://gabrielgit10110.github.io/ </a> <br>
  <br>
  ✉️ Contato: <a href="mailto:gabriel.sordonho@gmail.com">gabriel.sordonho@gmail.com </a>
   <br><br>
</div>  

**Nota**: Este projeto não é afiliado ao WhatsApp ou Twilio. Desenvolvido para fins educacionais/comerciais.  

---

## 📝 Licença  

Este projeto está sob licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.  
