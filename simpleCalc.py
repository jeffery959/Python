import time
animate = "..."
waiting= True
wait = 0
while waiting:
    if(wait % len(animate)==0):
        print("Loading", end="\r")
    
    print(" "+animate[wait % len(animate)], end=" ")
    
    
    wait +=1
    time.sleep(0.1)

def add(a, b):
    return a+b
def subtract(a, b):
    return a-b

def main():
    runing=True

    while runing:
        print("\n__Calculator__")
        print("1.Add numbers")
        print("2.Subtract numbers")
        print("3.Exit")
        choice = int(input("Select options(1-2): "))

        if choice == 3:
            

            runing = False
            print("Exiting...")
            return
    
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
        result= 0
     
        
            
        if choice == 1:        
            result=add(num1,num2)
            
            
        if choice == 2:         
            result=subtract(num1,num2)
        
       
        
       
        print("Answer is "+str(result))


main()