

mySentence = 'loves the color'

color_list = ['red','blue','green','pink','teal','black']

testarray = ['one','two','three','four']

def color_function(name):
    lst = []
    for i in color_list:
        msg = "{} {} {}".format(name,mySentence,i)
        lst.append(msg)
    return lst

def get_name():
    go = True
    while go:
        name = input('What is your name? ')
        if name == '':
            print('You need to provide your name!')
        elif name == 'Danny':
            print('Hi Danny')
        else:
            go = False
    lst = color_function(name)
    for i in lst:
        print(i)


def testfunction():
    for i in testarray:
        print(i)

def testcount():
    x = testarray.count("one")
    print(x)

def testsort():
    testarray.sort()
    print(testarray)

#testsort()

x = lambda t: t*10
print(x(10))


