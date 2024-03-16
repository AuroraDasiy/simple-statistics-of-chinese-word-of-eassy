import jieba
#str>>str
def bzh(x):
    for i in x:
        if i in "!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏.":
            x=x.replace(i,' ')
    return x
#str>>list
def jieba1(x):
    y=jieba.lcut(x)
    return y
#list>>dict>>list
def tongji(x):
    y={}
    for i in x:
        if i in y:
            y[i]+=1
        else:
            y[i]=1
    y=list(y.items())
    y.sort(key=lambda x:x[1],reverse=True)
    return y
#list>>list
#刪掉不符合要求的内容可自行添加
def delete(x):
    z='qwertyuiopasdfghjklzxcvbnm123456789'
    y=[]
    for i in x:
        if  i[0] not in z and i[0] not in [] and len(i[0])>1:
            y.append(i)
    return y
file=open("666.txt",'r+',encoding='utf-8')
str1=file.read()
list1=delete(tongji(jieba1(bzh(str1))))
for i in list1:
    print(i)

