'''

for i in range(10,0,-1):
    for j in range(0,10):
        if(j>=i-1):
            print("* ", end= " ")
        else:
            print(" ",end=" ")

    print()



for i in range(0,10):

    for j in range(0,10):

        if(j>=i):

            print(" * ",end=" ")
        else:
            print(" ", end=" ")
    print()


for i in range(0,10):
    for j in range(0,i):
        print(j, end="")
    print()
  


for i in range():
    for j in range(0,10):
        if(j>=i):
        
            print(j,  end= " ")
        else:
            print(" ", end=" ")

    print()

    '''
def star():

    for i in range (0,10):
    
        for j in range(0,10):
            if (j>i):
                print(j, end="  ")
            else:
                print(" ",end="")
      
        print()
star()
