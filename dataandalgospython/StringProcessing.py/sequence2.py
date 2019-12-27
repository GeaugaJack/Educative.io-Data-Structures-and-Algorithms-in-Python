def normalize_str(input_str):
    input_str = input_str.replace(" ", "")
    return input_str.lower()

def is_unique_1(input_str):
    d = dict()
    for i in input_str:
        if i in d:
            return False
        else:
            d[i] = 1
    return True

def is_unique_2(input_str):
    return len(set(input_str)) == len(input_str)

def is_unique_3(input_str):
    alpha = "abcedefghijklmnopqrstuvwxyz"
    for i in input_str:
        if i in alpha:
            alpha = alpha.replace(i, "")
        else:
            return False
    return True


unique_str = "AbCDefG"
non_unique_str = "non Unique STR"

unique_str = normalize_str(unique_str)
non_unique_str = normalize_str(non_unique_str) 
print("Unique String")
print(unique_str)
print("Non-Unique String")
print(non_unique_str, "\n")

print("Solution 1 where input string is unique string")
print(is_unique_1(unique_str))
print("Solution 1 where input string is non-unique string")
print(is_unique_1(non_unique_str), "\n")


print("Solution 2 where input string is unique string")
print(is_unique_2(unique_str))
print("Solution 2 where input string is non-unique string")
print(is_unique_2(non_unique_str), "\n")