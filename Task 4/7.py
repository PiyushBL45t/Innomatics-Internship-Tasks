def check_str(string):
    print(any(a.isalnum() for a in string))
    print(any(a.isalpha() for a in string))
    print(any(a.isdigit() for a in string))
    print(any(a.islower() for a in string))
    print(any(a.isupper() for a in string))
    
if __name__ == '__main__':
    s = input()
    check_str(s)
        
