
# set data_type
s1={10,20,30,40,50,60,80,90,100}
print(s1)
print(type(s1))     #<class 'set'>
print(len(s1))
print("-----------------------")
s2={10,20,30,40,10,20,30}
print(s2)
print(len(s2))
print(type(s2))
print("---------------------------")
s3={}
print(s3)   #<class 'dict'>
print(type(s3))
print("--------------------------")

# add()

s1={10,20,30,40,50,60,70}
s1.add(100)
print(s1)   #{100, 70, 40, 10, 50, 20, 60, 30}

#clear()

s1.clear()
print(s1)       #set()

print("------------")

#example of difference

s1={10,20,30,40,50,60}
s2={30,40,50,60,70,80}
s3=s1.difference(s2)
print(s3)
print("--------------")

#example of update difference

s1={10,20,30,40}
s2={30,40,50,60}
print(s1)
print(s2)
s1.difference_update(s2)
print(s1)
print(s2)

#example of intersection

s1={10,20,30,40}
s2={30,40,50,60}
s3=s1.intersection(s2)
print(s3)
print("-----------")

#example of subset and superset

s1={10,20,30,40}
s2={30,40,50,60}
print(s1.issubset(s2))  #false
print(s1.issuperset(s2))    #false

print("----------------")

s1={10,20,30,40}
s2={30,40,10,20}
print(s1.issubset(s2))  #true
print(s1.issuperset(s2))    #true

print("-----------------")

s1={10,20,30,40,50,60,70}
s2={30,40,10,20}
print(s1.issubset(s2))      #false
print(s1.issuperset(s2))      #true
print("-------------------")

s1={10,20,30,40,50,60,70}
s2={30,40,10,20}
print(s2.issubset(s1))  #true
print(s2.issuperset(s1))    #false

print("------------------")

#copy()
s1={10,20,30,40,50}
s2=s1.copy()
print(type(s2))
print(s2)
print("------------------")
# pop()
s1={"bhushan","shubham"}
s1.pop()
print(s1)
print("---------------------")
#remove()

s1={10,20,30,40}
s1.remove(40)
print(s1)
print("-----------------------------")

#union
s1={10,20,30,40,50}
s2={50,60,70,80,90}
s1.union(s2)
print(s1)
print("----------")


