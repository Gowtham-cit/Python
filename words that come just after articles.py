s=input().split()
articles=['a','an','the','A','An','The']
for i in s:
    if i in articles:
        print(s[s.index(i)+1],end=" ")
    
