from cgi import print_arguments
from importlib.util import module_for_loader
from pkg_resources import require
import requests
import time

token = '5653459602:AAGfYmHO5fCgvCbuQ4kSZk58grInkepSiY0'
chat_id = '-1001776523782'

while True:
 
    url = 'https://blaze.com/api/roulette_games/recent'

    response = requests.get(url)

    r = response.json()

    lista = [x['roll'] for x in r ]

    def qualcor(x):
        if x == 0:
            return 'B'
            
        if x == 1:
            return 'V'
            
        if x == 2:
            return 'V'
            
        if x == 3:
            return 'V'
            
        if x == 4:
            return 'V'
            
        if x == 5:
            return 'V'
            
        if x == 6:
            return 'V'
            
        if x == 7:
            return 'V'
            
        if x == 8:
            return 'P'
           
        if x == 9:
            return 'P'
           
        if x == 10:
            return 'P'
           
        if x == 11:
            return 'P'
           
        if x == 12:
            return 'P'
           
        if x == 13:
            return 'P'
           
        if x == 14:
            return 'P'
           
    
    def qualnum(x):
        if x == 0:
            return '0'
       
        if x == 1:
            return '1'
            
        if x == 2:
            return '2'
         
        if x == 3:
            return '3'
            
        if x == 4:
            return '4'
            
        if x == 5:
            return '5'
            
        if x == 6:
            return '6'
            
        if x == 7:
            return '7'
            
        if x == 8:
            return '8'
            
        if x == 9:
            return '9'
            
        if x == 10:
            return '10'
            
        if x == 11:
            return '11'
            
        if x == 12:
            return '12'
            
        if x == 13:
            return '13'
            
        if x == 14:
            return '14'

    pd = lista[0:16]
        
    mapeando = map(qualcor, pd)
    mapeando2 = map(qualnum, pd)
      
    finalcor = list(mapeando)
    finalnum = list(mapeando2)
        
    print(finalcor)
    print(finalnum)
    
    def resultado(num):
        if num[0:7] == ['V', 'P', 'V', 'P', 'P', 'V', 'V']:
        
            text = '''Win no gale 1✅🐓'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)
            
            
        elif num[0:7] == ['P', 'P','V', 'P', 'P', 'V', 'V']:
        
            text = '''Loss 🔻'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(10)
           
           
        elif num[0:7] == ['B', 'V', 'P', 'V', 'V', 'P', 'P']:
        
            text = '''Win Branco ⚪️✅'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)
           
           
        elif num[0:7] == ['B', 'P', 'V', 'P', 'P', 'V', 'V']:
        
            text = '''Win Branco ⚪️✅'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(10)
           
            
        elif num[0:7] == ['P', 'V', 'P', 'V', 'V', 'P', 'P']:
        
            text = '''Win no gale 1✅🐓'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)
            
            
        elif num[0:7] == ['V', 'V','P', 'V', 'V', 'P', 'P']:
        
            text = '''Loss 🔻'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)
            
            
        elif num[0:7] == ['V', 'P', 'P', 'P', 'P', 'P', 'P']:
          
            text = '''Win no gale 1✅🐓'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)


        elif num[0:7] == ['P', 'V', 'V', 'V', 'V', 'V', 'V']:
          
            text = '''Win no gale 1✅🐓'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)


        elif num[0:7] == ['B', 'P', 'P', 'P', 'P', 'P', 'P']:
          
            text = '''Win Branco ⚪️✅'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)


        elif num[0:7] == ['B', 'V', 'V', 'V', 'V', 'V', 'V']:
          
            text = '''Win Branco ⚪️✅'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)    


        elif num[0:6] == ['P','P', 'V', 'V', 'P', 'P']:
        
            text = '''Win sem gale ✅😎'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)
            
            
        elif num[0:6] == ['V','P', 'V', 'V', 'P', 'P']:
        
            text = '''Atenção, vamos ao gale 1 🐓'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)
      
      
        elif num[0:6] == ['B','P', 'V', 'V', 'P', 'P']:
        
            text = '''Win Branco ⚪️✅'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)
            
            
        elif num[0:6] == ['V','V', 'P', 'P', 'V', 'V']:
        
            text = '''Win sem gale ✅😎'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)
            
           
        elif num[0:6] == ['B','V', 'P', 'P', 'V', 'V']:
        
            text = '''Win Branco ⚪️✅'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)
            
            
        elif num[0:6] == ['P','V', 'P', 'P', 'V', 'V']:
        
            text = '''Atenção, vamos ao gale 1 🐓'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)
      
      
        elif num[0:6] == ['B','V', 'P', 'P', 'V', 'V']:
        
            text = '''Win Branco ⚪️✅'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)
      

        elif num[0:6] == ['P', 'V', 'V', 'P', 'V', 'P']:
        
            text = '''Win no gale 1✅🐓'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)


        elif num[0:6] == ['B', 'V', 'V', 'P', 'V', 'P']:
        
            text = '''Win Branco ⚪️✅'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)  


        elif num[0:6] == ['V', 'P', 'P', 'V', 'P', 'V']:
        
            text = '''Win no gale 1✅🐓'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)


        elif num[0:6] == ['B', 'P', 'P', 'V', 'P', 'V']:
        
            text = '''Win Branco ⚪️✅'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)  


        elif num[0:6] == ['P', 'P', 'P', 'V', 'P', 'V']:
        
            text = '''Loss 🔻'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)


        elif num[0:6] == ['V', 'V', 'V', 'P', 'V', 'P']:
        
            text = '''Loss 🔻'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)      
        

        elif num[0:6] == ['V', 'P', 'P', 'P', 'P', 'P']:
          
            text = '''Win sem gale ✅😎'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)


        elif num[0:6] == ['P', 'V', 'V', 'V', 'V', 'V']:
          
            text = '''Win sem gale ✅😎'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)


        elif num[0:6] == ['B', 'P', 'P', 'P', 'P', 'P']:
          
            text = '''Win Branco ⚪️✅'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)


        elif num[0:6] == ['B', 'V', 'V', 'V', 'V', 'V']:
          
            text = '''Win Branco ⚪️✅'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)    
            

        elif num[0:6] == ['V', 'V', 'V', 'V', 'V', 'V']:
          
            text = '''Atenção, vamos ao gale 1 🐓'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)

       
        elif num[0:6] == ['P', 'P', 'P', 'P', 'P', 'P']:
          
            text = '''Atenção, vamos ao gale 1 🐓'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)


        elif num[0:5] == ['V', 'P', 'P', 'V', 'V']:
        
            text = '''
           ✅ Entrada confirmada entrar 🔴
            Proteger Branco ⚪️
            Fazer no máximo 1 Gale 🐓
            '''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)
            
      
        elif num[0:5] == ['P', 'V', 'V', 'P', 'P']:
        
            text = '''
           ✅ Entrada confirmada entrar ⚫
            Proteger Branco ⚪
            Fazer no máximo 1 Gale 🐓
            '''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)
        

        elif num[0:5] == ['P', 'V', 'P', 'V', 'P']:
        
            text = '''Win sem gale ✅😎'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)


        elif num[0:5] == ['B', 'V', 'P', 'V', 'P']:
        
            text = '''Win Branco ⚪️✅'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)    


        elif num[0:5] == ['V', 'V', 'P', 'V', 'P']:
        
            text = '''Atenção, vamos ao gale 1 🐓'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)    

        
        elif num[0:5] == ['V', 'P', 'V', 'P', 'V']:
        
            text = '''Win sem gale ✅😎'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)


        elif num[0:5] == ['P', 'P', 'V', 'P', 'V']:
        
            text = '''Atenção, vamos ao gale 1 🐓'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)


        elif num[0:5] == ['B', 'P', 'V', 'P', 'V']:
        
            text = '''Win Branco ⚪️✅'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)


        elif num[0:5] == ['V', 'P', 'P', 'P', 'P']:
          
            text = '''Entrada cancelada ❌'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)

        
        elif num[0:5] == ['P', 'V', 'V', 'V', 'V']:
          
            text = '''Entrada cancelada ❌'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)


        elif num[0:5] == ['P', 'P', 'P', 'P', 'P']:
          
            text = '''Entrada confirmada✅
            entrar 🔴
            proteger no ⚪️'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)


        elif num[0:5] == ['V', 'V', 'V', 'V', 'V']:
          
            text = '''Entrada confirmada✅
            entrar ⚫
            proteger no ⚪️'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)


        elif num[0:4] == ['V', 'V', 'P', 'P']:
          
            text = ''' 🔔 Atenção! possível entrada em breve'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)


        elif num[0:4] == ['P', 'P', 'P', 'P']:
          
            text = ''' 🔔 Atenção! possível entrada em breve'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)


        elif num[0:4] == ['V', 'V', 'V', 'V']:
          
            text = ''' 🔔 Atenção! possível entrada em breve'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)     
            
            
        elif num[0:4] == ['P', 'P', 'V', 'V']:
          
            text = ''' 🔔 Atenção! possível entrada em breve'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)
        
     
        elif num[0:4] == ['P', 'V', 'P', 'V']:
          
            text = '''Entrada confirmada✅
            entrar 🔴
            proteger no ⚪️
            '''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)
            
            
        elif num[0:4] == ['V', 'P', 'V', 'P']:
            text = '''
            Entrada confirmada✅
            entrar ⚫
            proteger no ⚪️
            '''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)


        elif num[0:4] == ['V', 'V', 'P', 'V']:
          
            text = '''Entrada cancelada ❌'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)
            
            
        elif num[0:4] == ['P', 'P', 'V', 'P']:
            text = '''Entrada cancelada ❌'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)


        elif num[0:3] == ['V', 'P', 'V']:
          
            text = '''🔔 Atenção! possível entrada em breve'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)


        elif num[0:3] == ['P', 'V', 'P']:
          
            text = '''🔔 Atenção! possível entrada em breve'''
            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            results = requests.get(url_base)
            time.sleep(20)    

    resultado(finalcor)
    time.sleep(15)