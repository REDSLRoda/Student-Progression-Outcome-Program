# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 

# Student ID: 20210646
 
# Date: …11/28/2021…
 

#3 multiple outcomes &  Histogram
num_1 = 0
num_2 = 0
num_3 = 0
c     = 0
loop =""
progress=[0,0,0,0]

print('Staff Version with Histogram','\n')
def predict():     

     if num_1== 120:
         print("Progress")
         progress[0] = progress[0] + 1
  
     elif num_1 == 100:
         print("Progress - module trailer")
         progress[1] = progress[1] + 1

     elif num_3>= 80:
         print("Exclude")
         progress[3] = progress[3] + 1

     else: 
         print("Do not progress - module retriver")
         progress[2] = progress[2] + 1

def histogram():               

    print('Progress  :',progress[0],'*'* progress[0])
    print('Trailing  :',progress[1],'*'* progress[1])
    print('Retriever :',progress[2],'*'* progress[2])
    print('Excluded  :',progress[3],'*'* progress[3], '\n')
    print('\n', c, ' outcomes in total')
         
while loop.upper()!="Q":
    try:                      
        num_1=int(input("Enter your pass credits: "))
        if num_1 not in range (0,121,20):
            print("Range error !")
            continue           
        
        num_2=int(input("Enter your defer credits: "))
        if num_2 not in range (0,121,20):
            print("Range error !")
            continue            
        
        num_3=int(input("Enter your fail credits: "))
        if num_3 not in range (0,121,20):
            print("Range error !")
            continue            

        if num_1+num_2+num_3 !=120:
            print("Total incorrect")
            continue

        else:
            predict()
            c+=1
            loop=input('Press Q to quit.\nPress y to continue.\n')
       
    except:
         print ("Integer required ")
else:
    histogram()
    





    

    


    
    
   
  
        
  
    

    
    
    

   
