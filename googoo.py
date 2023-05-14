def solution(n):
    str_len = n+5
    maxInt = int(str_len * (5000/2465) + 475)

    numberSet = [True] * maxInt

    numberSet[0] = numberSet[1] = False

    for number, isPrime in enumerate(numberSet):
        if isPrime and number <= (maxInt**(1/2)):
            for multiple in range(number**2, maxInt, number):
                numberSet[multiple] = False
    
    prime_str = "".join([str(x) for x,y in enumerate(numberSet) if y])
    return prime_str[n:n+5]

print(solution(3))

# check time
import time
start = time.time()
for n in range(10000):
    solution(n)
print(f"{time.time()-start}seconds")
#########################################################################################################################
# def solution(n):
#     str_len = n + 5
#     max_int = int(str_len * (5000 / 2465) + 475)

#     number_set = [True] * max_int
#     number_set[0] = number_set[1] = False

#     for number in range(2, int(max_int ** 0.5) + 1):
#         if number_set[number]:
#             for multiple in range(number ** 2, max_int, number):
#                 number_set[multiple] = False

#     prime_str = ''.join(str(x) for x, y in enumerate(number_set) if y)[2:]
#     return prime_str[n:n + 5]


# print(solution(3))

# # check time
# import time

# start = time.time()
# for n in range(10000):
#     solution(n)
# print(f"{time.time() - start} seconds")

########################################################################################################################

# def solution(n):
#     str_len = n + 5
#     max_int = int(str_len * (5000 / 2465) + 475)

#     number_set = bytearray(b'\x01' * max_int)
#     number_set[0] = number_set[1] = 0

#     count = 0
#     for number in range(2, max_int):
#         if number_set[number]:
#             count += 1
#             if count == n + 5:
#                 break
#             for multiple in range(number ** 2, max_int, number):
#                 number_set[multiple] = 0

#     prime_str = ''
#     for x in range(n, n + 5):
#         prime_str += str(next(i for i, b in enumerate(number_set[x:], x) if b))
#     return prime_str

# print(solution(3))

# # check time
# import time

# start = time.time()
# for n in range(10000):
#     solution(n)
# print(f"{time.time() - start} seconds")
