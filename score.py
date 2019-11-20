fr=open('d:\手机文件\文件\工作.CSV','r')
fw=open('score.csv','w')
ls=[]
ls_chinese=[]
ls_math=[]
ls_english=[]
a,b,c=0,0,1
chinese,math,english=0,0,0
for line in fr:
    line=line.replace('\n','')
    ls.append(line.split(','))
ls[0].append('总分')    
for i in range(1,len(ls)):
    ls_chinese.append(ls[i][1])
    chinese=eval(ls[i][1])+chinese
    ls_math.append(ls[i][2])
    math=eval(ls[i][2])+math
    ls_english.append(ls[i][3])
    english=eval(ls[i][3])+english
    for j in range(1,len(ls[i])):
        a=eval(ls[i][j])+a
    ls[i].append(str(a))
    a=0
for row in ls:
    print(row)
    fw.write(','.join(row)+'\n')
fw.write('语文最高分为{}，最低分为{}，平均分为{}'.format(max(ls_1),min(ls_1),chinese/5)+'\n')
fw.write('数学最高分为{}，最低分为{}，平均分为{}'.format(max(ls_2),min(ls_2),math/5)+'\n')
fw.write('英语最高分为{}，最低分为{}，平均分为{}'.format(max(ls_3),min(ls_3),english/5)+'\n')
fr.close()
fw.close()
