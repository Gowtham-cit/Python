
def sum_diagonal(n,mat):

    c = sum(mat[i][i] for i in range(n))
    d = sum(mat[n-i-1][n-i-1] for i in range(n))
    return c + d

n = int(input())
mat = []
for i in range(n):
    a = [int(x) for x in input().split()]
    mat.append(a)
print(sum_diagonal(n,mat))
