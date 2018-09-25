# data=[[1,2,3],
#       [4,5,6],
#       [7,7,7]]
#
# for j in range(len(data[0])):
#     # print(data[j])
#     for k in range(len(data)):
#         # print("====------88-------=")
#         print(data[k][j])


def num_to_list(num,n):
    alist=[]
    for i in range(n):
        alist.append(num)
    return alist
print(num_to_list(2,4))
