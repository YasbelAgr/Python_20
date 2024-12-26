def anagramas(str1, str2):
    str1 = str1.replace(' ', ' ').lower()
    str2 = str2.replace(' ', ' ').lower()

    if len(str1) != len(str2):
        return False
    else:
        str1_ord = sorted(str1)
        str2_ord = sorted(str2)

        return str1_ord == str2_ord
str1 = 'gato'
str2 = 'toga'
print(anagramas(str1, str2))