

def mult_list(lst_to_mult):
  
  result = 1
  for number in lst_to_mult:
    result *= number
    
  return result


result = mult_list([1, 2, 3, 4, 5])
print(result)

def test_mult_list():
   
    lst = input('enter the numbers that are to multiplied')
    lst = lst.split(',')
    # Convert the strings to integers
    lst = [int(x) for x in lst]
    result = mult_list(lst)
    print(f"The result is: {result}")

result = test_mult_list()
