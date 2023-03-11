# from datetime import datetime
# now= datetime.now()
# print(now)


# import calendar
# year=int(input("enter the year "))
# month=int(input("enter the month "))
# print(calendar.month(year,month))

# def document():
#     '''a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string '''

# print(document.__doc__)


# def diffrence(x):
    
#     if (x>17):
#       result=(x-17)*2
#     else:
#         result=17-x
#     return result
    
# print(diffrence(19))


# def distinct(no):
#     if len(no)==len(set(no)):
#         return print("no distinct elemnt")
#     else:
#        return print("have distinct element") 
     
# distinct([1,3,4,4])

# a=input("enter the string\n")

# laststring=a.replace("a[0]","$")
# print(laststring)





#  1- Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged 
# string1=input("enter a string\n")
# if (len(string1))>3:
#     if (string1.endswith("ing")):
#         print(string1+"ly")
#     else:
#         print(string1+"ing") 
# else:
#     print("empty string")


# 2-Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string

# string='The lyrics is not that  poor! The lyrics is not poor!'
# _not=string.find("not")
# _poor=string.find("poor")
    
# newstring=string.replace(string[_not:_poor+4],"good")
    
# print(newstring)


# a=["dhananjay","cat","mouse","tommy","exercise"]
# def longestLength(words):
#     finalList = []


     
#     for i in words:
#         finalList.append((len(i),i))
#     finalList.sort()
#     print(finalList)
#     print("The word with the longest length is:", finalList[-1][1],
#           " and ", finalList[3][-1])

# longestLength(a)
                    
                    
                    
                    # ---->  string

# Q (4) - replacing first charater into $ except fist charactor
# def replacing(strng):
#     strng=strng[0]+strng[1:].replace(strng[0],"$")
#     return strng
# print(replacing('restart'))


# Q (5)- swapping first two charactor of each string
# def charmix(x,y):
#     newx=y[0:2]+x[2:]
#     newy=x[0:2]+y[2:]
    
#     return newx,newy
# print(charmix('abc','xyz'))


# Q (6) adding ing and ly in the last oly when the length of string is greater than 3
# def add_string(strng):
#     if len(strng)>=3:
#         if strng.endswith('ing'):
#             return strng+'ly'
#         else:
#             return strng+'ing'
#     else:
#         return strng
# print(add_string('go'))


# Q (7) finding not follows the poor and replace it with good
# def not_poor(strng):
#     _not=strng.find('not')
#     _poor=strng.find('poor')
    
#     if _poor > _not and _poor>0 and _not>0:
#         result= strng.replace(strng[_not:_poor+4],'good')
#         return result  
#     else:
#         return "not able to found not and poor "  
# print(not_poor('the lyrics is not that poor'))




# def max_word(a):
#     max=len(a[0])
#     word='j'

#     for i in a:
#         if len(i)>max:
#             max= len(i)
#             word=i
    
#     return word,max
# print(max_word(['cat','goat','dog','dhananjay','pudina','lacca']))      
        



#                          LIST



#list=['cat','goat','dog','dhananjay','pudina','lacca']
# list=[10,5,40,80]
# max=list[0]
# for i in list:   
#     if i<max:
#         max=i
        
# print(max)










# def counting(list):
#     cunt=0
#     for i in list:
#       if len(i)>2 and i[0]==i[-1]:
#         cunt+=1
#     return cunt
        

# print(counting(['abc', 'xyz', 'aba', '1221','kjik']))

# u='ram'
# for i in range(len(u)):
#     print(u[i])
#     x= [10,50,40,60,50]
#     x+10
#     print(x)




# even=[]
# odd=[]
# def even_odd(list):
    
#     for i in list: 
#         if i%2==0:
#              even.append(i)
#         else:
#              odd.append(i)
    

# x=[1,5,8,7,10,5,6]
# even_odd(x)
# print("the list of even no = ",even)
# print("the list of odd no = ",odd)


# y=lambda a,b: a*b
# print(y(9,5))
# from functools import reduce

# numbers=[1,5,7,8,6,3,4]
# square=list(map(lambda x,y:x+y,numbers))
# print(square)



#wap rectangle area = side *side


# class area:
#     def __init__(self,side,length):
#         self.side=side
#         self.length=length
        
#     def avg(self):
#         result=self.side*self.length
#         return print(result)
   

# class student:
#     def __init__(self,m1,m2):
#         self.m1=m1
#         self.m2=m2
        
#     def __add__(self,other):
#         m1=self.m1+other.m1
        
#         return m1
    
# ram=student(40,60)
# shyam=student(50,40)
# geeta=student(30,70)

# print(ram+shyam)
    
    
# list1=[1,5,4,7]
# list2=[5,8,7,4]
# print(list1+list2)

# def isarmstrong():
#     user=int(input("enter the value\n"))
#     result=0
#     temp=user
#     while temp>0:
#         single=temp%10
#         print("single = ",single)
        
#         result+=single**3
#         print("result = ",result)
        
#         temp //=10
#         print("temp = ",temp)
        
#     if user==result:
#         print("is armstorng")
#     else:
#         print('not a armstrong')
        
# isarmstrong()

# class student:
#     pass
# class marks:
#     pass
# student1=student()
# marks1=marks()

# print(isinstance(student1,student))
# print(isinstance(marks1,student))

# print(issubclass(student,object))


# from datetime import datetime
# marji = now.strftime("%d/%m/%Y %H:%M:%S")
# print("date and time =", marji)



# class student:
  
        
#     def sum (self,a=None ,b=None,c=None):
        
#         result=0
        
#         if a!=None and b!= None and c!=None:
#             result= a+b+c
#         elif a!=None and b!= None:
#             result=a+b
#         else:
#             result=a
        
        
#         return result
# ram=student()

# print(ram.sum(40,60,40))

    
    
    
    
    
    
