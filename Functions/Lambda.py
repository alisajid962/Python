# sum = lambda x,y:x+y
# div = lambda x,y:x/y
# print(sum(2,3))
# print(div(7,7))
# l1 =[1,2,3,4,5,6]
# l2=[1,2,3,4,5,6]
# sum = lambda a,b:a+b
# sum(l1,l2)
# print("Using the function: ",sum)
# sum_of_list= map(sum,l1,l2)
# print("Using map: ",tuple(sum_of_list))
# l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# sqr=lambda x:x**2 if x%2!=0 else x
# sqrlist=list(map(sqr,l))
# print(sqrlist)
# print(l1+l2)
# ===================================
# To ADD 10 to all the elements in the list
l4 = [1,2,3,4,5,6,7,8,9,0,10,11,12,13]
map_list=map(lambda x:x+10,l4)
print(list(map_list))
# ==================
# to remove number using filter
l5=[1,2,3,-10,-11,23,-34]
map_list1=map(lambda x:x>0,l5)
fil_list1=filter(lambda x:x>0,l5)
print(list(fil_list1))