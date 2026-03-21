# num=int(input("Enter a number: "))
# # count=0
# # while num>0:
# #     num=num//10
# #     count=count+1

# # print(count)
# # n=int(input("Enter a number: "))
# # num1=n
# # rev=""
# # while num1>0:
# #     digit=num1%10
# #     rev=rev+str(digit)
# #     num1=num1//10

# # if n==int(rev):
# #     print("Palindrome")
# # else:
# #     print("Not Palindrome")
# num=[1,2,3,4,5,1]
# freqmap={}
# for i in range(len(num)):
#     if num[i] in freqmap:
#         freqmap[num[i]] += 1
#     else:
#         freqmap[num[i]] = 1
# print(freqmap)