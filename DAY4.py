# def sunmnum(i,num):
#     if i>num:
#         return
    
#     print(i)
#     sunmnum(i+1,num)

# sunmnum(1,5)


# /*backtracking
# def sum(i,num):
#     if i>num:
#         return
    
#     sum(i+1,num)
#     print(i)

# # sum(0,5)
# def sum1(num):
#     if num<=0:
#         return 0
    
#     return num + sum1(num-1)

# print(sum1(3))

# # sum1(4)

# ........................................................................................................
# # # recursive reverse 
# ........................................................................................................



# num=[1,2,3,4,5,6,7,8,9,10]

# def reverse(num,left,right):
#     if left>=right:
#        return 
    
#     num[left],num[right]=num[right],num[left]
   
#     reverse(num,left+1,right-1)

# reverse(num,0,4)
# print(num)

# arr=[1,2,3,4,5,6,7,8,9,10]
# def reverse(arr,left,right):
#     if left>=right:
#         return
    
#     arr[left],arr[right]=arr[right],arr[left]
#     reverse(arr,left+1,right-1)
# left=int(input("ENTER  LEFT INDEX"))
# right=int(input("ENTER RIGHT INDEX"))
# reverse(arr,left,right)
# print(arr)

# # .............................................................................................
# # iterative palin
# word=input("ENTER WORD")
# wordlist=word.split()
# reversewrd
# # ..............................................................................................
# # recursive palindrome