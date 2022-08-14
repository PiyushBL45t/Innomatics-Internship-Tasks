def average(array):
    set_arr = set(array)
    avg = sum(set(set_arr))/len(set_arr)
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = map(int, ().split())
    result = average(arr)
    print(result)