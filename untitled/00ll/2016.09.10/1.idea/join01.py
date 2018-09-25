#对序列进行操作（分别使用' '与':'作为分隔符）
seq1 = ['hello', 'good', 'boy', 'doiido']
print(' '.join(seq1))
print (":".join(seq1))


#对字符串进行操作
seq2 = "hello good boy doiido"
print(':'.join(seq2))



#对元组进行操作
seq3 = ('hello','good','boy','doiido')
print(':'.join(seq3))




#对字典进行操作
seq4 = {'hello':1,'good':2,'boy':3,'doiido':4}
print(':'.join(seq4))

#打印与给出结果不符合　boy:good:doiido:hello

#合并目录
import os
print(os.path.join('/hello/','good/boy/','doiido'))
# 打印与给出结果不符合　'/hello/good/boy/doiido'　　，且需要调用print