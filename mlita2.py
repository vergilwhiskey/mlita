def Polynom():
    Construct()
    Tail()


def Construct():
    global string, i, error
    print("Proceeding Construct")
    if string[i] == '1':
        i += 1
    elif string[i] in "xyz":
        Symbol()
        TYPE1()
    elif string[i] == '(':
        i += 1
        Bracket()
        if string[i] == ')':
            i += 1
            Multiply()
            TYPE2();
        else:
            error = True
            exit("Error: no closing bracket in construct")
    else:
        error = True
        exit("Error: Construct")



def Tail():
    global string, i, error
    print("Proceeding tail")

    if string[i] == "+":
        i += 1
        Construct()
        Tail()
    #else:
    #    exit("Error: tail")



def TYPE1():
    global string, i, error
    print("Proceeding TYPE1")
    if string[i] == ')':
        i += 1
        Bracket()
        if string[i] == ')':
            i += 1
            TYPE1()
        else:
            error = True
            exit("Error: No cloign bracking in TYPE1")
    elif string[i] in "xyz":
        Symbol()
        TYPE1()   
    #else:
        #exit("Error: TYPE1") 



def TYPE2():
    global string, i, error
    print("Proceeding TYPE2")

    if string[i] == '(':#???????????????????????????????????????????????????????
        i += 1
        Bracket()
        if string[i] == ')':
            i += 1
            TYPE1();
        else:
            error = True
            exit("Error: no closing bracket in TYPE2")
    elif string[i] in "xyz":
        Symbol()
        TYPE1()
    else:
        error = True
        exit("Error: unneded brackets")


def Bracket():
    global string, i, error
    print("Proceeding Bracket")
    Construct()
    if string[i] == "+":
        i += 1
        Construct()
        Tail()
    else: 
        error = True
        exit("Error: unneded bracket in Bracket")


def Symbol():
    global string, i, error
    print("Proceeding Symbol")
    if string[i] in 'xyz':
        i += 1
    else:
        error = True
        exit("Error: unknown variable")


def Multiply():
    global string, i, error
    print("Proceeding Multiply")
    if string[i] == "*":
        i += 1
    #else: 
    #    exit("Error: Multiply")

if __name__ == '__main__':
    string = (input('Введите строку: ')) 

    i = 0
    Polynom()

    print("Correct string!!!")