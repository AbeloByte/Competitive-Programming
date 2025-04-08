def swap_case(s):
    lst = []
    for char in s:
        if char == char.lower():
            lst.append(char.upper())
        elif char == char.upper():
            lst.append(char.lower())
        
    return "".join(lst)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
