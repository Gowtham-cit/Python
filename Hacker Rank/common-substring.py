"""
https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
"""
#solution
def twoStrings(s1, s2):
    return 'YES' if set(s1) & set(s2) else 'NO'
