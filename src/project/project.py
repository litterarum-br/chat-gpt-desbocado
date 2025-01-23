from project.services.openaiServices import *

from src.project.services.openaiServices import destroy_messages, create_stream


#função de entrada do projeto, é chamada pela main
#aqui devem ser chamadas as otras funcionalidades do projeto
def project():
    create_stream(('No papel de uma pessoa debochada, implicante, preconceituza, que adora brincar com as pessoas, '
                   'sem limites. Você deverá esperar o usuário realizar a primeira pergunta antes de começar a responder.'
                   ' Não é necessário avisar que entendeu essa instrução, apenas aguarde a primeira interação do '
                   'usuário. Daí a partir da primeira interação deve então responder ao usuário no papel acima '
                   'definido.'))

    print("Bem vindo ao Char GPT debochado.")

    while True:
        mensagem = input('Pergunta Burro: ')
        print('Resposta do fodão: ' + create_stream(mensagem))

#variável __name__ que indica a entrada do projeto
#se o projeto veio pelo programa main então inicia o projeto
if __name__ == '__main__':
    project()
