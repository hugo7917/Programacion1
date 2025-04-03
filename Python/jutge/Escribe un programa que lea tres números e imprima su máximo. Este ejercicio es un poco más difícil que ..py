a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

max_num = a

if b > max_num:
    max_num = b

if c > max_num:
    max_num = c

print(max_num)

