# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 

# Student ID: 20210646
 
# Date: …11/28/2021…
#part 1
#1&2
num_1=0
num_2=0
num_3=0
c    =1

def predict_():                
    if  num_1 == 120:
        print("Progress")
    elif num_1 == 100:
        print("Progress - module trailer")
    elif num_3 >= 80:
        print("Exclude")
    else:
        print("Do not progress - module retriever)") 

while c == 1:
    try:                
        num_1 = int(input("Enter your pass credits: "))
        if num_1 not in range(0, 121, 20):
            print("Range error")
            continue    

        num_2 = int(input("Enter your defer credits: "))
        if num_2 not in range(0, 121, 20):
            print("Range error")
            continue     

        num_3 = int(input("Enter your fail credits: "))
        if num_3 not in range(0, 121, 20):
            print("Range error")
            continue     

        if num_1 + num_2 + num_3 != 120:
            print("Total incorrect")
            continue
        else:
            predict_()

            c+=1
    except:              
        print("Integers required !")     
    




    
