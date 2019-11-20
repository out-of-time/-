fr=open('d:\手机文件\文件\工作.CSV','r')
fw=open('score.csv','w')
ls=[]
ls_1=[]
ls_2=[]
ls_3=[]
a,b,c=0,0,1
ch,ma,en=0,0,0
for line in fr:
    line=line.replace('\n','')
    ls.append(line.split(','))
ls[0].append('总分')    
for i in range(1,len(ls)):
    ls_1.append(ls[i][1])
    ch=eval(ls[i][1])+ch
    ls_2.append(ls[i][2])
    ma=eval(ls[i][2])+ma
    ls_3.append(ls[i][3])
    en=eval(ls[i][3])+en
    for j in range(1,len(ls[i])):
        a=eval(ls[i][j])+a
    ls[i].append(str(a))
    a=0
for row in ls:
    print(row)
    fw.write(','.join(row)+'\n')
fw.write('语文最高分为{}，最低分为{}，平均分为{}'.format(max(ls_1),min(ls_1),ch/5)+'\n')
fw.write('数学最高分为{}，最低分为{}，平均分为{}'.format(max(ls_2),min(ls_2),ma/5)+'\n')
fw.write('英语最高分为{}，最低分为{}，平均分为{}'.format(max(ls_3),min(ls_3),en/5)+'\n')
fr.close()
fw.close()
