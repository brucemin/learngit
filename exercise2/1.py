# if分支课后练习
#    输入小明的考试成绩，显示所获奖励
#    成绩==100分，爸爸给他买辆车
#    成绩>=90分，妈妈给他买MP4
#    90分>成绩>=60分，妈妈给他买本参考书
#    成绩<60分，什么都不买

grade=int(input('请输入小明的成绩：'))
if grade == 100:
    print('爸爸给他买辆车')
elif grade >= 90:
    print('妈妈给她买本参考书')
elif grade >= 60:
    print('妈妈给他买本参考书')
else:
    print('什么都不买')