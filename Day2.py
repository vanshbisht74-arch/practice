# n=[2,4,8,9,12,14,67,1,6,7]
# m=[1,2,3,4,5,8,9]
# hashmap=[0]*11

# for num in n:
#   hashmap[num]+=1

# for num in m:
#     if num<0 and num<10:
#         print(0)
#     else:
#         print(hashmap[num])
# n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
# m = [10, 11, 1, 9, 5, 67, 2]

# hash_list = [0] * 11

# for num in n:
#   hash_list[num] += 1

# for num in m:
#     if num < 1 or num > 10:
#         print(0)
#     else:
#         print(hash_list[num])

q="aabbccddeeee"
p=["a","b","c","d"]
hashmap=[0]*26
for ch in q:
    aschii_value=ord(ch)
    index=aschii_value-97
    hashmap[index]+=1
for ch in p:
    aschii_value=ord(ch)
    index=aschii_value-97
    print(hashmap[index])

