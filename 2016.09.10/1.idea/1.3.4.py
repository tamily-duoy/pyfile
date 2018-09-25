#例子１

import matplotlib.pyplot as plt
friends = [70,65,72,63,71,64,60,64,67]
minutes = [175,170,205,120,220,130,105,145,190]
labels = ['a','b','c','d','e','f','g','h','i']

plt.scatter(friends,minutes)

for label,friend_count,minute_count in zip(labels,friends,minutes):
    plt.annotate(label,
                 xy=(friend_count,minute_count),
                 xytext=(5,-5),
                 textcoords='offset points')

plt.title("w")
plt.xlabel("v")
plt.ylabel("m")
plt.show()







#例子２

import matplotlib.pyplot as plt

test_1_grades = [99,90,85,97,80]
test_2_grades = [100,85,60,90,70]
plt.scatter(test_1_grades,test_2_grades)

# plt.axis("equal")　
# 加了这行，图形会更精确地显示大多数变化发生在测验２上

plt.title("w")
plt.xlabel("v")     #测验１的分数
plt.ylabel("m")     #测验２的分数
plt.show()