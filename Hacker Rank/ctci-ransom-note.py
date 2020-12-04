"""
https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
"""
#solution
#!/bin/python3

from collections import Counter

def checkMagazine(magazine, note):
    a = Counter(magazine)
    b = Counter(note)
    return "Yes" if ( a & b ) == b else "No"
    

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))
