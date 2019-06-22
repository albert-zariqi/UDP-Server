import socket
import datetime
import random
import math


def TIME():
    try:
        #Nxerrja e kohes aktuale si dhe ruajtja e saj ne nje variabel
        date = datetime.datetime.now()
        #Ndarja e kohes aktuale( dita, muaji, viti, ora, minutat, sekonda) dhe ruajtja e tyre ne variabla te vecanta
        day = date.day
        month = date.month
        year = date.year
        hour = date.hour
        minute = date.minute
        second = date.second
        #Dergimi i kohes ne formatin e lexueshem per njerezit
        return str(day) + "."+str(month)+"."+str(year)+" "+str(hour) + ":"+str(minute)+":"+str(second)
    except socket.error:
        print("Ka ndodhur nje gabim %s"%(socket.error))

def FIBONACCI(kerkesa):
    try:
        #Perpunimi i kerkeses se pranuar
        kerkesa = " ".join(kerkesa)
        kerkesa = kerkesa[9:]
        kerkesa = int(kerkesa)
        nr1 = 0
        nr2 = 1
        counter = 1
        #Gjetja e numrit FIBONACCI
        while(counter != kerkesa):
            nr3 = nr1 + nr2
            nr1 = nr2
            nr2 = nr3
            counter += 1
        #Kthimi i numrit FIBONACCI
        if(counter == 1):
            nr3 = nr2+nr1
            return nr3
        #Kthimi i numrit FIBONACCI
        else:
            return nr3
    except Exception as err:
        print("Ka ndodhur nje gabim! %s"%(str(err.args)))
        
def ZANORE(fjalia):
    try:
        #Perpunimi i kerkeses se pranuar
        fjalia = " ".join(fjalia)
        fjalia = fjalia[6:]
        fjalia = fjalia.lower()
        #Lista e cila permban zanoret
        zanoret = ['a','e','ë','i','o','u','y']
        counter = 0
        #Numerimi i zanoreve ne fjaline e dhene
        for karakteret in fjalia:
            for zanorja in zanoret:
                if(karakteret == zanorja):
                    counter +=1
        #Kthimi i nje teksti informues, qe tregon numrin e zanoreve ne fjaline e dhene
        return "Teksti i pranuar permban "+str(counter)+" zanore"
    except Exception as ex:
        print(ex.args)

def IPADDR(kerkesa):
    try:
        ip_Klientit = kerkesa[0]
        return ip_Klientit
    except Exception as err:
        print(err.args)

def PORTNR(kerkesa):
    try:
        porti_Klientit = kerkesa[1]
        return porti_Klientit
    except Exception as err:
        print(err.args)

def PRINTO(kerkesa):
    try:
        #Perpunimi i kerkeses
        kerkesa = " ".join(kerkesa)
        kerkesa = kerkesa[6:]
        #Largimi i hapesirave ne fillim dhe fund te fjalise
        kerkesa = kerkesa.strip(" ")
        #Dergimi i kerkeses se perpunuar
        return kerkesa
    except Exception as err:
        print(err.args)

def HOST():
    try:
        #Gjetja dhe ruajtja e emrit te hostit
        kerkesa = socket.gethostname()
        kerkesa = str(kerkesa)
        if(kerkesa != "None"):
            return kerkesa
        else:
            return "Emri i hostit nuk mund te gjendet!"
    except Exception as err:
        print(err.args)
        
def KONVERTO(kerkesa):
    try:
        #Perpunimi i kerkeses
        if(kerkesa[1]=="CelsiusToKelvin"):
            try:
                kerkesa = " ".join(kerkesa)
                kerkesa = kerkesa[24:]
                #Perfitimi i vleres per konvertim
                celsius = float(kerkesa)
                #Formula per gjetjen e vleres se konvertuar
                kelvin = celsius + 273
                #Kthimi i vleres se konvertuar
                return kelvin
            except Exception as e:
                print("Something bad happened %s"%(str(e.args)))
                #Ngjajshem veprojme edhe per konvertimet e tjera
        elif(kerkesa[1]=="CelsiusToFahrenheit"):
            try:
                kerkesa = " ".join(kerkesa)
                kerkesa = kerkesa[28:]
                celsius = float(kerkesa)
                fahrenheit = celsius * (9/5) + 32
                return fahrenheit
            except Exception as err:
                print("Something bad happened %s"%(str(err.args)))
        elif(kerkesa[1] == "KelvinToFahrenheit"):
            try:
                kerkesa = " ".join(kerkesa)
                kerkesa = kerkesa[27:]
                kelvin = float(kerkesa)
                fahrenheit = (kelvin - 273)*(9/5) + 32
                return fahrenheit
            except Exception as err:
                print("Something bad happened %s"%(str(err.args)))
                return 0
        elif(kerkesa[1] == "KelvinToCelsius"):
            try:
                kerkesa = " ".join(kerkesa)
                kerkesa = kerkesa[24:]
                kelvin = float(kerkesa)
                celsius = kelvin - 273
                return celsius
            except Exception as err:
                print("Something bad happened %s"%(str(err.args)))
                return 0 
        elif(kerkesa[1] == "FahrenheitToCelsius"):
            try:
                kerkesa = " ".join(kerkesa)
                kerkesa = kerkesa[28:]
                fahrenheit = float(kerkesa)
                celsius = (fahrenheit - 32)*(5/9)
                return celsius
            except Exception as err:
                print("Something bad happened %s"%(str(err.args)))
                return 0
        elif(kerkesa[1] == "FahrenheitToKelvin"):
            try:
                kerkesa = " ".join(kerkesa)
                kerkesa = kerkesa[27:]
                fahrenheit = float(kerkesa)
                kelvin = (fahrenheit - 32)*(5/9) + 273
                return kelvin
            except Exception as err:
                print("Something bad happened %s"%(str(err.args)))
                return 0
        elif(kerkesa[1] == "PoundToKilogram"):
            try:
                kerkesa = " ".join(kerkesa)
                kerkesa = kerkesa[24:]
                pound = float(kerkesa)
                kilogram = pound * 0.454
                return kilogram
            except Exception as err:
                print("Something bad happened %s"% (str(err.args)))
                return 0
        elif(kerkesa[1] == "KilogramToPound"):
            try:
                kerkesa = " ".join(kerkesa)
                kerkesa = kerkesa[24:]
                kilogram = float(kerkesa)
                pound = kilogram / 0.454
                return pound
            except Exception as err:
                print("Something bad happened %s"%(str(err.args)))
                return 0
        else:
            return "Bad request"
    except Exception as err:
        print(err.args)

def LOJA():
    try:
        #krijimi i nje counteri
        counter = 0
        #krijimi i nje variable ku vendoset numrat random
        numbers = ""
        #gjenerimi i 20 numrave random dhe ruajtja e tyre ne variablen numbers
        while (counter != 20):
            if(counter != 19):
                numbers +=str(random.randint(0,99))+", "
            else:
                numbers +=str(random.randint(0,99))
            counter +=1
        #kthimi i 20 numrave te gjeneruar random
        return numbers
    except Exception as err:
        print("Something bad happend %s"%(str(err.args)))

def ENKRIPTIMI(fjalia):
    try:
        #Perpunimi i fjalise
        fjalia = fjalia.upper()
        fjalia = fjalia.strip(" ")
        fjalia = fjalia[11:]
        #Gjenerimi i celesit ne forme te stringut i cili gjendet ne fund te kerkeses
        for i in fjalia:
            celesi = i
        #kthimi i celesit ne formatin 'int' nga stringu
        celesi = int(celesi)
        #Largimi i celesit nga fjalia per enkriptim 
        fjalia = fjalia[:-1]
        #Zevendsimi i tab-ave me nga nje hapsire te vetme
        fjalia = fjalia.replace("\\T"," ")
        fjalia =  fjalia.strip()
        print(fjalia)
        #Kthimi i fjalise ne varg
        vargu = list(fjalia)
        #Enkriptimi i fjalise me metoden e CAESARIT
        for i in range(0,len(vargu)):
            if(vargu[i] == " "):
                continue
            else:
                vargu[i] = chr((ord(vargu[i]) - ord('A') + celesi)%26 + ord('A'))
        #Kthimi i fjalise se enkriptuar nga vargu ne string
        perfundimtarja = ''.join(vargu)
        #Dergimi i fjalise se enkriptuar
        return perfundimtarja
    except Exception as err:
        print(err.args)

def PALINDROMET(kerkesa):
    try:
        #Perpunimi i kerkeses
        kerkesa = " ".join(kerkesa)
        kerkesa = kerkesa[11:]
        var = str(kerkesa)
        var = var.replace(" ","")
        var = var.lower()
        #Kthimi i fjales ne varg
        lista1 = list(var)
        lista2 = []
        j = len(lista1) - 1
        #Mbushja e listes se dyte te krijuar me karakteret e listes se pare duke filluar nga fundi i listes se pare (reverse)
        for i in range(0,len(lista1)):
            lista2.append(lista1[j])
            j -=1
        #Kthimi i listes se dyte ne string
        str1 = "".join(lista2)
        #Kontrollimi i fjales a eshte palindrom apo jo, dhe dergimi i pergjigjes
        if(str1 == var):
            return "Fjala e dhene eshte palindrom!"
        else:
            return "Fjala e dhene nuk eshte palindrom!"
    except Exception as err:
        print(err.args)
def EKKUADRATIK(kerkesa):
    try:
        #Marrja e konstanteve (a, b, c) te ekuacionit kuadratik dhe kthimi i tyre nga tipi stringu ne float
        a = float(kerkesa[1])
        b = float(kerkesa[2])
        c = float(kerkesa[3])
        #Perfitimi i diskriminantes te ekuacionit te dhene
        d = math.sqrt(math.pow(b,2) - 4*a*c)
        #Zgjidhjet e dy ekuacionit
        x1 = ((-b)+d)/(2*a)
        x2 = ((-b)-d)/(2*a)
        return "Zgjidhjet e ekuacionit kuadratik "+str(a)+"x^2 + ("+str(b)+")x + (" + str(c)+") jane " + str(x1)+" dhe "+str(x2)
    except Exception as err:
        print("Something bad happened! %s" % (str(err.args)))
        return "Zgjidhjet jane imagjinare(komplekse)!"

#Porti i serverit
serverPort = 11000
#Zgjedhja e protokollit per komunikim, krijimi i nje socket-i
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#Bashkangjitja e adrese protokollit (ip adresa, porti)
serverSocket.bind(('localhost',serverPort))

print('Serveri u startua ne ip adresen %s dhe ndegjone kerkesat ne portin %s'%(socket.gethostbyname('localhost'),serverPort))
print("Serveri i gatshem te pranoj kerkesa: ")
while 1:
    try:
            #Pranimi i mesazhit nga klienti
                message, clientAddress = serverSocket.recvfrom(128)
                #perpunimi i mesazhit te derguar nga klienti, dhe kthimi i pergjigjes tek klienti permes funksionit sendto
                modMessage = str(message)
                modMessage = modMessage[2:]
                modMessage = modMessage[:-1]
                modMessage = modMessage.replace("\\t"," ")
                modMessage = modMessage.replace("   "," ")
                modMessage = modMessage.replace("  "," ")
                modMessage = modMessage.split(" ")
                kerkesa = " ".join(modMessage)
                if(modMessage[0] == "IPADDR"):
                    pergjigja = IPADDR(clientAddress)
                    pergjigja01 = "IP Adresa e klientit eshte " + str(pergjigja)
                    serverSocket.sendto(str.encode(pergjigja01),clientAddress)
                elif(modMessage[0] == "PORTNR"):
                    pergjigja = PORTNR(clientAddress)
                    pergjigja01 = "Klienti eshte duke perdorur portin " + str(pergjigja)
                    serverSocket.sendto(str.encode(pergjigja01),clientAddress)
                elif(modMessage[0] == "LOJA"):
                    pergjigja = LOJA()
                    serverSocket.sendto(str.encode(pergjigja),clientAddress)
                elif(modMessage[0] == "PALINDROMET"):
                    pergjigja = PALINDROMET(modMessage)
                    serverSocket.sendto(str.encode(pergjigja),clientAddress)
                elif(modMessage[0] == "EKKUADRATIK"):
                    pergjigja = EKKUADRATIK(modMessage)
                    serverSocket.sendto(str.encode(pergjigja),clientAddress)
                elif(modMessage[0] == "FIBONACCI"):
                    pergjigja = FIBONACCI(modMessage)
                    pergjigja = str(pergjigja)
                    serverSocket.sendto(str.encode(pergjigja),clientAddress)
                
                elif(modMessage[0] == "ZANORE"):
                    pergjigja = ZANORE(modMessage)
                    serverSocket.sendto(str.encode(pergjigja),clientAddress)
                elif(modMessage[0] == "PRINTO"):
                    pergjigja = PRINTO(modMessage)
                    serverSocket.sendto(str.encode(pergjigja),clientAddress)
                elif(modMessage[0] == "HOST"):
                    pergjigja = HOST()
                    pergjigja01 = "Emri i hostit eshte " + pergjigja
                    serverSocket.sendto(str.encode(pergjigja01),clientAddress)
                
                elif(modMessage[0] == "KONVERTO"):
                    pergjigja = KONVERTO(modMessage)
                    pergjigja = str(pergjigja)
                    serverSocket.sendto(str.encode(pergjigja),clientAddress)

                elif(modMessage[0] == "TIME"):
                    pergjigja = TIME()
                    serverSocket.sendto(str.encode("Koha aktuale eshte " + pergjigja),clientAddress)
                elif(modMessage[0] == "ENKRIPTIMI"):
            
                    pergjigja = ENKRIPTIMI(kerkesa)
                    serverSocket.sendto(str.encode(str(pergjigja)),clientAddress)
                else:
                    serverSocket.sendto(str.encode("BAD REQUEST!"),clientAddress)
    except Exception as err:
        print(err.args)


        