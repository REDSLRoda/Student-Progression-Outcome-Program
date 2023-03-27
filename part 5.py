# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 

# Student ID: 20210646
 
# Date: …11/28/2021…
c     =0
loop=""
list1=[]


def yy():
   
     if num_1== 120:
         list2 =[]
         list2.append('progress')
         list2.append(num_1)
         list2.append(num_2)
         list2.append(num_3)
         list1.append(list2)
         list2 =[]

         for i in list1:
             print(i)
         
     elif num_1 == 100:
         list3 =[]
         list3.append('trailer')
         list3.append(num_1)
         list3.append(num_2)
         list3.append(num_3)
         list1.append(list3)
         list3 =[]

         for i in list1:
             print(i)
            

     elif num_3>= 80:
         list4 =[]
         list4.append('exclude')
         list4.append(num_1)
         list4.append(num_2)
         list4.append(num_3)
         list1.append(list4)
         list4 =[]
  
         for i in list1:
             print(i)
     else:
         list5=[]
         list5.append('retriver')
         list5.append(num_1)
         list5.append(num_2)
         list5.append(num_3)
         list1.append(list5)
         list5 =[]
         
         for i in list1:
             print(i)

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
            yy()
            c+=1
            loop=input('Press Q to quit.\nPress y to continue.\n')
        
    except:                
        print("Integers required")
        
target={39:None,91:None,93:None}


def main():
   
    outfile = open('data.txt' , 'w')
   
    fname = (str(list1[0]).translate(target))
    sname = (str(list1[1:2]).translate(target))
    tname = (str(list1[2:3]).translate(target))
    xname = (str(list1[3:4]).translate(target))
    yname = (str(list1[4:5]).translate(target))
    zname = (str(list1[5:6]).translate(target))
    vname = (str(list1[6:7]).translate(target))
    hname = (str(list1[7:8]).translate(target))
    jname = (str(list1[8:9]).translate(target))
    kname = (str(list1[9:10]).translate(target))
    
    outfile.write(fname + "\n")
    outfile.write(sname + "\n")
    outfile.write(tname + "\n")
    outfile.write(xname + "\n")
    outfile.write(yname + "\n")
    outfile.write(zname + "\n")
    outfile.write(vname + "\n")
    outfile.write(hname + "\n")
    outfile.write(jname + "\n")
    outfile.write(kname + "\n")
    
    outfile.close()

    
main()



outfile= open('data.txt' , 'r')
for line in  outfile:
    print(line)


  
outfile.close()    

