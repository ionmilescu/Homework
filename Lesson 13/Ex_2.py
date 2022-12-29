class InvalidDestinationError(Exception):
    pass

def plane_ride_cost(city):
   
    dest = {"Pittsburgh": "222 euro" ,
    "Los Angeles": "475 euro" , 
    "Ohio": "183 euro" ,
    "Chisinau": "300 euro" }

    
      

    for key in dest:
            if city == key:
                return dest[key]
    raise InvalidDestinationError('Destination is not available')

city = input('Enter a city: ')
cost = plane_ride_cost(city)
print(cost)