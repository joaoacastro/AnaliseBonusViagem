import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC9ca61c463dd895050b40f2ae32ff7653"
# Your Auth Token from twilio.com/console
auth_token  = "308165a134176d345cb9933b7b1dfb76"
client = Client(account_sid, auth_token)

# abrir os 6 arquivos em Excel
listaMeses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in listaMeses:
    tabelaVendas = pd.read_excel(f'{mes}.xlsx')

    if (tabelaVendas['Vendas'] >= 55000).any():
        vendedor = tabelaVendas.loc[tabelaVendas['Vendas'] >= 55000, 'Vendedor'].values[0]
        vendas = tabelaVendas.loc[tabelaVendas['Vendas'] >= 55000, 'Vendas'].values[0]

        print(f'No mês de {mes} bateram a meta de R$55.000,00! O vendedor {vendedor} vendeu um total de R${vendas}')
        message = client.messages.create(
            to="+5511972788335",
            from_="+18597108854",
            body=f'No mês de {mes} bateram a meta de R$55.000,00! O vendedor {vendedor} vendeu um total de R${vendas}')
        print(message.sid)