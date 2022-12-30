dest = {"Pittsburgh": "222 euro" ,
    "Los Angeles": "475 euro" , 
    "Ohio": "183 euro" ,
    "Chisinau": "300 euro" }


class InvalidDestinationError(Exception):
    pass

class RegistrationExemption(Exception):
    pass

class StopProgram(Exception):
    pass 



def plane_ride_cost(city):
   
    

    
      

    for key in dest:
            if city == key:
                return dest[key]
    raise InvalidDestinationError('Destination is not available')
        



def add_dest():
    name = input('Numele destinatiei')
    pret = input('Introdu pretul')
    if name in dest:
        raise RegistrationExemption('Already registered')
    
    dest[name] = pret
    
def change_price():
    name = input('Numele destinatiei')
    pret = input('Introdu pretul')
   
    if name in dest:
        dest[name] = pret
        print('Schimbarile au fost facut cu succes')
    elif name not in dest:
        raise RegistrationExemption('Destination does not exist')

  
    
def show_options():
    print('/n')
    print('Pentru a verifica pretul unei destinatii apasati 1 \n' 
            ' pentru a adauga o destinatie apasati 2 \n'
            ' pentru a schimba pretul destinatiei apasati 3 \n '
            ' ori orice alt buton pentru a parasi meniul \n ')
    opt = input('Selectati optiunea: ')
    if opt == 1:
        city = input('Enter a city: ')
        cost = plane_ride_cost(city)
        print(cost)
    elif opt == 2:
        add_dest()
    elif opt == 3:
        change_price()
    else:
        raise StopProgram()

while True:
   try:
       show_options()
   except RegistrationExemption as ex:
       print()
       print(ex)
       print()
   except StopProgram as ex:
       break
        