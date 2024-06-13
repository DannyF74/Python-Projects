def testfunc():
    var1 = input("\nPlease enter your first name: ")
    var2 = input("\nPlease enter your last name: ")
    return var1,var2

def names():
    go = True
    while go:
        var1,var2 = testfunc()
        try:
            var3 = int(var1) + int(var2)
            go = False
        except:
            print("Please use numeric characters")
        finally:
            print("Moving on...")
    print("Welcome to my program {}".format(var3))
            
if __name__ == "__main__":
    names()
