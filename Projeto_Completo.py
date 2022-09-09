import time
import pyttsx3
from influxdb import InfluxDBClient
from pyttsx3.drivers import sapi5

    
client = InfluxDBClient(host='10.206.15.2', port =8086)
client.switch_database('mydb')
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    if("Brazil" in voice.name or "Brasil" in voice.name or "Maria" in voice.name):
        engine.setProperty('voice',voice.id)
    
engine.say("Olá! eu irei te ajudar caso eu detecte algo fora dos padrões")
engine.runAndWait()
time.sleep(10)
print("entrou")
#Olá, o programa funciona da seguinte forma:
#"permissao"  a variável usada para verificar se o programa ja pode verificar alguma das condiçes, essa variável irá ser verdadeira
# quando ela valer "1", isso deve acontecer 30 minutos depois do primeiro alarme, para mudar a quantidade de tempo é só
# mudar o "if cont==30" para o numero de minutos que voce quiser. (o cont é um contador, cada um tem o seu, para contar
# os minutos que cada um tem para tocar o próximo alarme.
# a variável "num" é uma variável que pega o valor principal e altera ele, para fazer modificações para que depois o programa fale ele da forma certa
# primeiro ele é transformado em positivo para que o programa consiga ler, pois por algum motivo o "engine.say" não lê O "menos" "-", então eu verifico se é negativo ou não
# depois verifico se é inteiro ou não, caso queira usar dentro de qualquer uma das condições NÃO USE O "num" ele não representa o valor real, use a variável que está sendo usada na comparação
# o programa roda a cada 60 segundos, a cada 60 segundos passa 1 minuto, ou seja os contadores recebem mais no seu valor, representando 1 minuto
# "num" é o valor que copiamos da variavel que recebe o valor do servidor, transformamos ele em positivo caso seja negativo, pois o programa não consegue falar o "menos" do número negativo

permissaoTN2=1
cont1=0
permissaoTZ=1
cont2=0
permissaoTN=1
cont3=0
permissaoCO2=1
cont5=0
permissaoTQ=1
cont6=0
permissaoSuccao=1
cont7=0
permissaoTZ2=1
cont8=1
permissaoTN3=1
cont9=1
negativo=0
minutos=0


while True:
    try:
        erro1=1
        result2 = client.query('SELECT last("temperatura_etanol_zero") FROM "Utilidades" GROUP BY "last"')
        result3 = client.query('SELECT last("temperatura_etanol_negativo") FROM "Utilidades" GROUP BY "last"')
        result5 = client.query('SELECT last("Producao_Instantanea_CO2") FROM "UtilidadesCO2" GROUP BY "last"')
        result6 = client.query('SELECT last("Nivel_TQ_Agua") FROM "Utilidades" GROUP BY "last"')
        result7 = client.query('SELECT last("pressao_succao_negativo") FROM "Utilidades" GROUP BY "last"')
    except Exception as e:
        print(e)
        erro1=0
        time.sleep(30)
    
    
        
    if(erro1==1):
        points = result2.get_points()
        for item in points:
            Temp_etanol_zero = item['last']
            Temp_etanol_zero = round(Temp_etanol_zero,2)
            print("Temp_etanol_zero: "+str(Temp_etanol_zero))
     
     
        points = result3.get_points()
        for item in points:
            Temp_etanol_negativo = item['last']
            Temp_etanol_negativo = round(Temp_etanol_negativo,2)
            print("Temp_etanol_negativo: "+str(Temp_etanol_negativo))
     
       
        points = result5.get_points()
        for item in points:
            CO2= item['last']
            CO2 = round(CO2,2)
            print("CO2: "+str(CO2))
     
        points = result6.get_points()
        for item in points:
            nivelTQ = item['last']
            nivelTQ = round(nivelTQ,2)
            print("Nivel tanque: "+str(nivelTQ))
     
        points = result7.get_points()
        
        for item in points:
            press_succao_negativo = item['last']
            press_succao_negativo = round(press_succao_negativo,2)
            print("press_succao_negativo: "+str(press_succao_negativo))
       
    
        if(permissaoCO2==0):
            cont5=cont5+1
        
        if(cont5==30):
            permissaoCO2=1
            cont5=cont5+1
        
        num=CO2
    
        if(permissaoCO2==1):
            if(CO2 < 10):
                permissaoCO2=0
                cont5=0
                print("CO2 FALOU!")
            
                if(num<0):
                    num= (num-(num)) + (-(num))
                    print(num)
                    negativo=1
                else:
                    negativo=0    
    

                if(negativo==1):
                    engine.say("usina de c ó dois parada!")
                    engine.runAndWait()
                else:
                    engine.say("usina de c ó dois parada!")
                    engine.runAndWait()
        
            
    
    
    
        if(permissaoTQ==0):
            cont6=cont6+1
        
        if(cont6==30):
            permissaoTQ=1
            cont6=cont6+1
        
        num=nivelTQ
    
        if(permissaoTQ==1):
            if(nivelTQ<35):
                permissaoTQ=0
                cont6=0
                print("tanque FALOU!")
                
            
                if(num<0):
                
                    num= (num-(num)) + (-(num))
                    print(num)
                    negativo=1
                else:
                    negativo=0
    

    

                if(negativo==1):
                    engine.say("Atenção! O nível do tanque de água está baixo!  o nível atual do tanque de água é de: menos"+str(num)+"porcento")
                    engine.runAndWait()
            
                else:
                    engine.say("Atenção! O nível do tanque de água está baixo!  o nível atual do tanque de água é de: "+str(num)+"porcento")
                    engine.runAndWait()
        
                   
        if(permissaoTZ==0):
            cont2=cont2+1
        
        if(cont2==30):
            permissaoTZ=1
            cont2=cont2+1
        
        num=Temp_etanol_zero
        if(permissaoTZ==1):
            if(Temp_etanol_zero>=1.1 and Temp_etanol_zero<1.5):
                permissaoTZ=0
                cont2=0
                print("temp etanol zero FALOU!")
                
                if(num<0):
                
                    num= (num-(num)) + (-(num))
                    print(num)
                    negativo=1
                else:
                    negativo=0

               
                if(negativo==1):
                    engine.say("Atenção! Temperatura do etanol zero elevada. A temperatura atual é de menos"+str(num)+"graus Celsius")
                    engine.runAndWait()
                else:
                    engine.say("Atenção! Temperatura do etanol zero elevada. A temperatura atual é de "+str(num)+"graus Celsius")
                    engine.runAndWait()
            
    
    
   
    
        if(permissaoTZ2==0):
            cont8=cont8+1
        
        if(cont8==15):
            permissaoTZ2=1
            cont8=cont8+1
        
        num=Temp_etanol_zero
        if(permissaoTZ2==1):
            if(Temp_etanol_zero>=1.5):
                permissaoTZ2=0
                cont8=0
                print("temp etanol zero2 FALOU!")
                if(num<0):
                
                    num= (num-(num)) + (-(num))
                    print(num)
                    negativo=1
                else:
                    negativo=0


    
                if(negativo==1):
                    engine.say("Atenção! Temperatura do etanol zero elevada. A temperatura atual é de menos"+str(num)+"graus Celsius")
                    engine.runAndWait()
                else:
                    engine.say("Atenção! Temperatura do etanol zero elevada. A temperatura atual é de "+str(num)+"graus Celsius")
                    engine.runAndWait()
    
            
    
    
        if(permissaoTN==0):
            cont3=cont3+1
        
        if(cont3==30):
            permissaoTN=1
            cont3=cont3+1
        
        num=Temp_etanol_negativo
        if(permissaoTN==1):
            if(Temp_etanol_negativo>=-2.5 and Temp_etanol_negativo<=-2.2):
                permissaoTN=0
                cont3=0
                print("temp etanol negativo FALOU!")

                if(num<0):
                    num= (num-(num)) + (-(num))
                    print(num)
                    negativo=1
                else:
                    negativo=0

    
                if(negativo==1):
                    engine.say("ATENÇÃO! Sistema Negativo com temperatura elevada, a temperatura atual é de menos"+str(num)+"graus celsius")
                    engine.runAndWait()
                else:
                    engine.say("ATENÇÃO! Sistema Negativo com temperatura elevada, a temperatura atual é de "+str(num)+"graus celsius")
                    engine.runAndWait()
    
    
    
        if(permissaoTN2==0):
            cont1=cont1+1
        
        if(cont1==30):
            permissaoTN2=1
            cont1=cont1+1
        
        num=Temp_etanol_negativo
    
        if(permissaoTN2==1):
            if(Temp_etanol_negativo >= -2.1):
                permissaoTN2=0
                cont1=0
                print("temp etanol negativo 2 FALOU!")
               
            
                if(num<0):
                
                    num= (num-(num)) + (-(num))
                    print(num)
                    negativo=1
                else:
                    negativo=0

                if(negativo==1):
                    engine.say("ATENÇÃO! Sistema Negativo com temperatura elevada, a temperatura atual é de menos"+str(num)+"graus celsius")
                    engine.runAndWait()
                else:
                    engine.say("ATENÇÃO! Sistema Negativo com temperatura elevada, a temperatura atual é de "+str(num)+"graus celsius")
                    engine.runAndWait()

              
    
        if(permissaoTN3==0):
            cont9=cont9+1
        
        if(cont9==30):
            permissaoTN3=1
            cont9=cont9+1
        
        num=Temp_etanol_negativo
        if(permissaoTN3==1):
            if(Temp_etanol_negativo < -3.6):
                permissaoTN3=0
                cont9=0
                
                print("temp etanol negativo 3 FALOU!")
                if(num<0):
                
                    num= (num-(num)) + (-(num))
                    print(num)
                    negativo=1
                else:
                    negativo=0

                if(negativo==1):
                    engine.say("ATENÇÃO! Temperatura do sistema negativo está baixa, vamos economizar energia? A temperatura atual é de menos"+str(num)+"graus celsius")
                    engine.runAndWait()
                else:
                    engine.say("ATENÇÃO! Temperatura do sistema negativo está baixa, vamos economizar energia? A temperatura atual é de"+str(num)+"graus celsius")
                    engine.runAndWait()
    

             
    
        if(permissaoSuccao==0):
            cont7=cont7+1
        
        if(cont7==30):
            
            permissaoSuccao=1
            cont7=cont7+1
        
        num=press_succao_negativo
        if(permissaoSuccao==1):
            if(press_succao_negativo>2.8):
                permissaoSuccao=0
                cont7=0
                print("pressão sucção negativo FALOU!")
                
            
                if(num<0):
                
                    num= (num-(num)) + (-(num))
                    print(num)
                    negativo=1
                else:
                    negativo=0

                
                if(negativo==1):
            
                    engine.say("Provável desarme no sistema menos 3! Estamos em CHÃTIDÁÁUM? O valor de pressão sucção Negativo é de: menos"+str(num))
                    engine.runAndWait()
                else:
                    engine.say("Provável desarme no sistema menos 3! Estamos em CHÃTIDÁÁUM? O valor de pressão sucção Negativo é de: "+str(num))
                    engine.runAndWait()
    
        print("min:")
        print(minutos)
       
    
        minutos=minutos+1
        time.sleep(65)


