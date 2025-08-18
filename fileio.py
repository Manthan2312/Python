# f=open('test.txt','r')
# # print(f)
# content=f.read()
# print(content)
# f.close()




# f=open("test1.txt",'w')
# f.write("Hello world from manthan\n")
# f.close()


# f=open("test1.txt",'a')
# f.write("Hello world from manthan\n")
# f.close()

# with open('test1.txt','a') as f:
#     f.write("mANTHAN_RUST")



# f=open('test1.txt','r')
# for i in f:
#     print(i) 
    
    
# f.close()


# f = open('test1.txt', 'r')


# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)

# f.close()

# o=open('test.txt','r')
# list_marks=[]
# for i in o:
#     list_marks.append(i)
#     print(i)


# print(list_marks)


# list_marks=['1232\n','4\n',"XSN\n"]


# o=open('test.txt','w')
# o.writelines(list_marks)
# o.close() 


# with open('test1.txt','a') as f:
#   f.write("mANTHAN_RUST\n")
  
with open("test1.txt",'r') as m:
    # print(m.read()) print from the file data 

    m.seek(10) 
    # seek function do the skip the number of the words you entered in the brackets
   
    print(m.tell())
    # tell function call print the where you are in the file which number of character you point right now

    
    print(m.read())