from dotenv import load_dotenv, find_dotenv
import openai
from pyexpat.errors import messages

#Função que recebe uma mensage, pergunta ao chat gpt e retorna a resposta
#message - Obrigatório - É a pergunta ou mensagem a ser aplicada pelo usuário ao chat gpt
#model - Modelo a ser usado pelo chat gpt, quando não informado usa o modelo gpt-3.5-turbo-0125
#max_token - Número máximo de tokens a serem usados pelo chat gpt, quanto maior, maior é a resposta.
#            quado não informado o default é 1000
#temperature - Representa o quão o chat gpt irá criar, os valores pode ser 0 (nenhuma criatividade),
#              1 (criatividade média) e 2 (muito criativo). O valor default é 1
def create_messages(message, model='gpt-3.5-turbo-0125', max_token=1000, temperature = 1):
    messages.append({'role': 'user', 'content': message})
    resposta = client.chat.completions.create(
        messages = messages
        , model = model
        , max_tokens = max_token
        , temperature = temperature
    )
    messages.append({'role': 'assistant', 'content': resposta.choices[0].message.content})
    return resposta.choices[0].message.content

#função para iniciar uma nova interação com o chat gpt
def destroy_messages():
    messages = []

#Função que recebe uma mensage, pergunta ao chat gpt e retorna a resposta
#message - Obrigatório - É a pergunta ou mensagem a ser aplicada pelo usuário ao chat gpt
#model - Modelo a ser usado pelo chat gpt, quando não informado usa o modelo gpt-3.5-turbo-0125
#max_token - Número máximo de tokens a serem usados pelo chat gpt, quanto maior, maior é a resposta.
#            quado não informado o default é 1000
#temperature - Representa o quão o chat gpt irá criar, os valores pode ser 0 (nenhuma criatividade),
#              1 (criatividade média) e 2 (muito criativo). O valor default é 1
def create_stream(message, model='gpt-3.5-turbo-0125', max_token=1000, temperature = 1):
    messages.append({'role': 'user', 'content': message})
    resposta = client.chat.completions.create(
        messages = messages
        , model = model
        , max_tokens = max_token
        , temperature = temperature
        , stream = True
    )
    resposta_completa = ''
    for stream in resposta:
        texto = stream.choices[0].delta.content
        if texto:
            resposta_completa += texto

    messages.append({'role': 'assistant', 'content': resposta_completa})
    return resposta_completa

#busca no dotenv a chave de utilização da API do OpenAI e inicia o cliente
_ = load_dotenv(find_dotenv())
client = openai.Client()

messages = []