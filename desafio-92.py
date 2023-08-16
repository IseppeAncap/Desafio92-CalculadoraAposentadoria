
# Definição de cores para outupt
reset = '\033[0m'
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
azul = '\033[34m'
magenta= '\033[35m'
ciano = '\033[36m'
## 1-ETAPA mensagens de boa vindas, nome do programa, e explicação.
print(f'{vermelho}Seja, Bem vindo')
print(f'{verde}{""::<20} {amarelo}{"Calculadora de Aposentadoria"}{verde} {""::<20}')
print(f'{ciano}\nEste programa realiza cálculos para determinar a idade em que um indivíduo', end=', ')
print(f'poderá se aposentar e utiliza uma estrutura de dicionário para armazenar informações, relevantes' ,end='')
print(f'e sobre sua carreira e trajetória profissional.{reset}')
print()
## 2 - ETAPA Inicializa 
import datetime
data_atual = datetime.datetime.now()
ano_atual = data_atual.year
formulário_seguridade_social = {}
regra_previdênciaria = 35
## 3-ETAPA Coleta de informaçoes sobre a carreira e vida
formulário_seguridade_social['Nome']= str(input(f'Nome: '))
ano_nascimento = int(input(f'Ano nascimento: '))
idade = ano_atual - ano_nascimento
formulário_seguridade_social['Idade'] = idade
formulário_seguridade_social['Cpts'] = int(input(f'Carteira de Trabalho: (0 não têm) '))
# Verificamos se o individúo possui Carteira de Trabalho!
if formulário_seguridade_social['Cpts']  == 0:
    print()# Quebra a linha caso ele não possua 
else:#  Coletamos a informaçẽes adiconais abaixo
    # Looṕ condição criada caso o ano de nascimento seja maior que ano da contratação.
    while True:
        formulário_seguridade_social['Contratação']=int(input(f'Ano de Contratação: '))
        if ano_nascimento > formulário_seguridade_social['Contratação']:
            print(f'Entrada Invalida\n Ano de nascimento não pode ser maior que contratação')# exibi mensagem de erro
        else:
            break # SAi do loop caso a entrada não cause conflito
    formulário_seguridade_social['Salário']=float(input(f'Salário:R$ '))
    formulário_seguridade_social['Salário']=f"{formulário_seguridade_social['Salário']:.2f}"
    ## 4-ETAPA Calculo da aposentadoria.
    idade_1emprego =  formulário_seguridade_social['Contratação'] - ano_nascimento
    aposentadoria_pro_idade= idade_1emprego +regra_previdênciaria
    formulário_seguridade_social['Aposentadoria']= aposentadoria_pro_idade
print()
print('-==-'*10)
## 5- ETAPA Saida
print(f'{"Analisando dados":^25}')
for k, v in formulário_seguridade_social.items():
    print(f'{".":>10}{amarelo} {k} {reset}têm o valor :{ciano}{v}{reset}.') 

