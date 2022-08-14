def minion_game(string):
    res = string.isupper()
    vowels = 'aeiou'.upper()
    stuart = 0
    kevin = 0
    if res == True:
        length = len(string)
        for i in range(length):
            score = length - i
            if string[i] in vowels:
                kevin += score
            else:
                stuart += score
        if stuart == kevin:
            print('Draw')
        if stuart > kevin:
            print('Stuart', stuart)
        if stuart < kevin:
            print('Kevin', kevin)
        

if __name__ == '__main__':
    s = input()
    minion_game(s)