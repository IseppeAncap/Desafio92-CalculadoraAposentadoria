Desafio 92 
    Desenvolva um programa que solicite o "nome", "ano de nascimento" e "carteira de trabalho" de uma pessoa,
e registre essas informações (juntamente com a "idade") em um dicionário. Caso a "CPTS" (Carteira de Trabalho)
não seja zero, o programa deve coletar também o ano de contratação e o salário. Em seguida, o programa deverá
calcular a idade da pessoa e prever a idade em que ela se aposentará.
    Ao final, o programa calculará a "idade da pessoa" e indicará em quantos anos ela atingirá a "aposentadoria".
    Observação: Considerar um tempo de trabalho de 35 anos.


Passo a passo

## 1ª ETAPA

    .Mensagens de boas-vindas, nome do programa e explicação.
------------------------------------------------------------------------------------
## 2ª ETAPA - Inicialização

    .Importar a Biblioteca Datetime.
    .Chamar o método now() para obter um objeto de data e atribuir a "data_atual".
    .Extrair o "ano" usando o método .year e atribuir ao ano atual para cálculos de idade posterior.
    .Declarar o dicionário vazio "formulário_seguridade_social".
----------------------------------------------------------------------------------------
## 3ª ETAPA - Coleta de informações sobre carreira e vida

    .Adicionar a chave "nome" e solicitar o nome ao usuário.
    .Solicitar o ano de nascimento.
    .Subtrair as variáveis: "ano atual" - "ano_nascimento" para obter a idade.
    .Adicionar ao dicionário um novo par chave:valor - idade e o valor.
    .ATENÇÃO: Usar um if para verificar se o valor da chave "CPTS" é igual a zero e, assim, não prosseguir
    coletando mais dados.
    .Usar um loop while True para evitar erros:
    .Adicionar outra chave ao dicionário - "contratação" - e solicitar o valor do par.
    .Se o ano de nascimento for maior que o ano de contratação, exibir uma mensagem de erro e continuar
    no loop.
    .Usar um else para quando os dados de contratação estiverem corretos e, então, usar um break para sair do loop.
    .Em seguida, adicionar ao dicionário o par chave:valor - "Salário" - e solicitar o seu valor.

## 4ª ETAPA - Cálculo da idade para aposentadoria

    .A lógica matemática para calcular a idade para aposentadoria é feita somando-se a idade no momento da contratação
    com a regra geral de previdência de um tempo mínimo de 35 anos.
    .Utilizar o valor da chave ['contratação'] e subtrair o valor da variável "ano de nascimento", atribuindo o resultado
    à variável idade_1emprego para obter a idade quando a pessoa assinou o seu primeiro contrato.
    .Somar "idade_1emprego" com "regra_previdenciaria" e atribuir o valor a "aposentadoria_pro_idade".
    .Por fim, adicionar o último par chave:valor - [aposentadoria] - e o valor "aposentadoria_pro_idade".

## 5ª ETAPA - Saída

    .Utilizar um loop for para iterar sobre os itens do dicionário e exibi-los.
 Exwmplo pratico 
 Seja, Bem vindo
:::::::::::::::::::: Calculadora de Aposentadoria ::::::::::::::::::::

Este programa realiza cálculos para determinar a idade em que um indivíduo, poderá se aposentar e utiliza uma estrutura de dicionário para armazenar informações, relevantese sobre sua carreira e trajetória profissional.

Nome: Maria
Ano nascimento: 1783
Carteira de Trabalho: (0 não têm) 344
Ano de Contratação: 1792
Salário:R$ 1000

-==--==--==--==--==--==--==--==--==--==-
    Analisando dados     
         . Nome têm o valor :Maria.
         . Idade têm o valor :240.
         . Cpts têm o valor :344.
         . Contratação têm o valor :1792.
         . Salário têm o valor :1000.00.
         . Aposentadoria têm o valor :44.
         
