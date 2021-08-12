import re
f = open("regex_sum_1025273.txt", "r")
txt = f.read()
ret = re.findall(r"[0-9]+", txt)

print("ret: ", ret, ", len: ", len(ret))

sum = 0
for it in ret:
    sum = sum + int(it)
print("sum: ", sum)

# sum = 0
# for line in f:
#     ret = re.findall('[0-9]+', line)
#     for it in ret:
#         sum = sum + int(it)

# print("sum: ", sum)
