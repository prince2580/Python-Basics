#Q1
# def square_root(num): 
#         a = num 
#         b = 1
#         it = 0.00000001
#         while((a - b) > it): 
#             a = (a + b)/2
#             b = num / a
      
#         return a
  
# num = 4
# print("Square root of", num, "is",round(square_root(num), 4)) 


#Q2
# def divide_num(arr):
#     i=0
#     for x in arr:
#         arr[i]/=2
#         i+=1

# arr=[2,4,6,8,10]
# divide_num(arr)
# print(arr)




# Q3
# def find_fruit(a,str):
#     i=0
#     for x in a:
#         if(x==str):
#             print('index= ', i)
#             return
#         i+=1

#     else:
#       print("-1")
#       return   

# fruits=['mango','apple','banana','berry']
# name='mango'
# find_fruit(fruits,name)  