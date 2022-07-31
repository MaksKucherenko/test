print ("Введите строку состоящею из цифр!")
spisok = [] 
stroka = input() 
if stroka.isnumeric(): 
    for i in stroka: 
        spisok.append(int(i)) 
    print(sum(spisok))   
else:
    print("Строка имеет символы или пробелы. Введите только цифры!")        





    
 
