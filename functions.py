def max_num(a,b,c):
    max_ab = a if a > b else b
    max = max_ab if max_ab > c else c
    return max

print(max_num(5,11,2))
print(max_num(1,2,4))
print(max_num(100,10,1))

def mult_list(li):
    tot = 1
    for i in li:
        tot *= i
    return tot

print(mult_list([3,10,7,4]))
print(mult_list([11,3,4,4]))
print(mult_list([6,2,4]))

def rev_string(didnt_we_do_this_already):
    return didnt_we_do_this_already[::-1]

print(rev_string("Hello World!"))
print(rev_string("Foo Bar"))
print(rev_string("Tis but a scratch"))

def num_within(num,min,max):
    return (num > min) & (num <= max)

print(num_within(3,2,4))
print(num_within(3,1,3))
print(num_within(10,2,5))

def pascal(n):
    row = [1]
    for i in range(n):
        print(row)
        nex = 1
        for num in range(i):
            hold = row[num + 1] 
            row[num + 1] += nex
            nex = hold
        row.append(1)

pascal(20)

input("Enter to exit")
