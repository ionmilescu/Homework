def check_type(value):
    try:
        int(value)
        print('The value is an integer.')
    except ValueError:
        try:
            float(value)
            print('The value is a float.')
        except ValueError:
            print('The value is a string.')

value = input('Enter a value: ')
check_type(value)





    

