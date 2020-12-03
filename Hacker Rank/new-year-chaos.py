"""
https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
"""
#solution

def minimumBribes(q):
    ans = 0
    
    q = [i-1 for i in q]
    
    for i, p in enumerate(q):
        
        if p - i > 2:
            print("Too chaotic")
            return
        for j in range(max(p-1, 0), i):
            if q[j] > p:
                ans += 1
    print(ans)
    

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
