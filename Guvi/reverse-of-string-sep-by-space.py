def reverse_word(string):
    print(' '.join(i[::-1] for i in string.split()))
string = input()
reverse_word(string)
