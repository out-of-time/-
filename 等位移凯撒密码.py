def enc(n):
    code=[]
    for i in range(len(n)):
        if 'A'<=n[i]<='Z' or 'a'<=n[i]<='z':
            c=n.upper()
            s=chr(ord('A')+(ord(c[i])-ord('A')+i+1)%26)
            code.append(s)
        else:
            code.append(n[i])
    return(''.join(code))
def dec(d):
    plaincode=[]
    for x in range(len(d)):
        if 'A'<=d[x]<='Z' or 'a'<=d[x]<='z':
            c=d.upper()
            s=chr(ord('A')+(ord(c[x])-ord('A')-x-1)%26)
            plaincode.append(s)
        else:
            plaincode.append(d[x])
    return(''.join(plaincode))
while True:
    try:
        ch=eval(input('只加密输入1，只解密输入2，加密又解密输入3：'))
        if ch==1:
            a=input('请输入明文：')
            print(enc(a))
            break
        elif ch==2:
            c=input('请输入暗文：')
            print(dec(c))
            break
        elif ch==3:
            a_a=input('请输入明文：')
            print(enc(a_a))
            c_c=input('请输入暗文；')
            print(dec(c_c))
            break
    except:
        print('输入错误，请重新输入')



