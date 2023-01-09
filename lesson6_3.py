# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]
exp_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def displace(input_list):
    n = int(input())
    first = input_list[:(n+1)]
    last = input_list[(n+1):]
    return last + first

print(displace(exp_list))

def shift_list(objs, shift):
    if abs(shift)  <= len(objs):
        odjs = objs[-shift: ] + objs[: -shift]
    else:
        shift -= (shift // len(objs)) * len(objs)
    return odjs