def swap_case(s):
    modified_string=""
    
    for char in s:
        if char.islower():
            modified_string += char.upper()
        elif char.isupper():
            modified_string += char.lower()
        else:  
            modified_string += char
    return modified_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
