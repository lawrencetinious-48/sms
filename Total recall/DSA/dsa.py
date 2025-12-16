# fibonacci sequence using the for loop
# num1 = 0
# num2 = 1

# for i in range(18):
#     newnum = num1 + num2
#     print(newnum)

#     num1 = num2
#     num2 = newnum

# the fibonacci squence using the recursion 
# print(0)
# print(1)

# count = 2

# def fnumbers(num1, num2):
#     global count
#     if count <= 20:
#         newnum = num1 + num2
#         print(newnum)
#         num1 = num2
#         num2 = newnum

#         count += 1
#         fnumbers(num1, num2)
#     else:
#         return


# fnumbers(1,0)


count = 2

def fnumbers(num1, num2):
    global count
    if count <= 12:
        fn = num1 + num2
        print(fn)
        num1 = num2
        num2 = fn

        count += 1
        fnumbers(num1, num2)
    else:
        return 

fnumbers(0,1)