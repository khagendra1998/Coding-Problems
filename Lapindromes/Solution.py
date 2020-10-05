def match(one,sec):
    m=list(map(str,one))
    n=list(map(str,sec))
    if sorted(m)==sorted(n):
        return "Yes"
    else:
        return "No"
for i in range(0,int(input())):
    s=str(input())
    l=len(s)
    if (l%2!=0):
        print(match(s[0:l//2],s[l//2+1:l]))
    else:
        print(match(s[0:l//2],s[l//2:l]))