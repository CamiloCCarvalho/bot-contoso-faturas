
from botcity.core import DesktopBot
from features.botfeat import *
import pandas as pd
from pandas import DataFrame
import os

# Define bot_studio problema com imagens
def not_found(label):
    print(f"Element not found: {label}")



# Variaveis usadas no projeto
path_app = fr'C:\Program Files (x86)\Contoso, Inc\Contoso Invoicing\LegacyInvoicingApp.exe'
name_file_main: str = f'Contoso+Coffee+Shop+Invoices'
path_to_file = (os.getcwd()) + fr'\files'
wait_low = 100
wait_mid = 500
wait_long = 3000

# Leitura da planilha necessaria do processo
tabela_main: DataFrame = pd.read_excel(fr'{path_to_file}\{name_file_main}.xlsx')

# Instancia do Bot usado
bot = DesktopBot()

# Navega até o app
bot.execute(path_app)
bot.wait(wait_long)
bot.maximize_window()
# Acessa a aba de processo necessaria
if not bot.find( "aba_invoices", matching=0.97, waiting_time=10000):
    not_found("aba_invoices")
bot.click()



def contoso_faturas(data, nome_conta, contato_email, montante, status):

    # Inicia processo repetitivo LOOP
    if not bot.find( "icon_nova_entry", matching=0.97, waiting_time=10000):
        not_found("icon_nova_entry")
    bot.click()
    
    if not bot.find( "label_date", matching=0.97, waiting_time=10000):
        not_found("label_date")
    bot.click_relative(72, 6)
    bot.type_keys(['home'])
    bot.type_keys(['shift', 'end'])

    bot_paste_l(bot, data)
    bot.tab(wait_low)
    bot_paste_l(bot, nome_conta)
    bot.tab(wait_low)
    bot_paste_l(bot, contato_email)
    bot.tab(wait_low)
    bot_paste_l(bot, montante)

    if not bot.find( "label_status", matching=0.97, waiting_time=10000):
        not_found("label_status")
    bot.click_relative(88, 5)
    
    # Ponto de decisão baseado na fatura
    if status == 'Uninvoiced':
        if not bot.find( "opt_uninvoiced", matching=0.97, waiting_time=10000):
            not_found("opt_uninvoiced")
        bot.click_relative(66, 32)

    elif status == 'Invoiced':
        if not bot.find( "opt_invoiced", matching=0.97, waiting_time=10000):
            not_found("opt_invoiced")
        bot.click_relative(65, 53)

    else:   
        if not bot.find( "opt_paid", matching=0.97, waiting_time=10000):
            not_found("opt_paid")
        bot.click_relative(68, 72)
    
    if not bot.find( "btn_save", matching=0.97, waiting_time=10000):
        not_found("btn_save")
    bot.click()
    # END






# Função responsavel por iniciar o bot
if __name__ == '__main__':

    for coluna in tabela_main.itertuples():
        contoso_faturas(str(coluna[1]), str(coluna[2]), str(coluna[3]), str(coluna[4]), str(coluna[5]))

    bot.alt_f4()

