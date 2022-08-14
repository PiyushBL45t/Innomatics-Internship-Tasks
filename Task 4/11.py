def print_formatted(number):
    l = len(str(bin(number)[2:]))
    for i in range(1, number+1):
        int_num = i
        oct_num = oct(i)
        hex_num = hex(i)
        bin_num = bin(i)
        print(str(i).rjust(l) + " " + oct_num[2:].rjust(l) + " "+ hex_num[2:].upper().rjust(l)+ " " + bin_num[2:].rjust(l))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
