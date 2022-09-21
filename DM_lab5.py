import numpy as np
import matplotlib.pyplot as plt

def main():
    Score = np.random.randint(100,size=(10,4))
    Q1(Score)
    print('1.\n')
    Q2(Score)
    print('2.\n')
    Q3(Score)
    print('3.\n')
    Q4(Score)
    print('4.\n')


def Q1(Score): #1번문제
    x=Score[:,1:2]
    y=Score[:,0:1]
    plt.plot(x,y,'^')
    plt.xlabel('English')
    plt.ylabel('Korea')
    plt.show()

def Q2(Score): #2번문제

    plt.figure()
    Korea=Score[:,0:1]
    English=Score[:,1:2]
    Math=Score[:,2:3]
    Science=Score[:,3:4]

    plt.subplot(2, 2, 1)
    plt.hist(Korea)
    plt.xlabel('Korea')
    plt.ylabel('Count')

    plt.subplot(2, 2, 2)
    plt.hist(English)
    plt.xlabel('English')
    plt.ylabel('Count')

    plt.subplot(2, 2, 3)
    plt.hist(Math)
    plt.xlabel('Math')
    plt.ylabel('Count')

    plt.subplot(2, 2, 4)
    plt.hist(Science)
    plt.xlabel('Science')
    plt.ylabel('Count')

    plt.subplots_adjust(hspace=0.5, wspace=0.5)
    plt.show()

def Q3(Score): #3번문제
    arr1=Score[:,0:1]
    arr2=[0,0,0,0]
    arr3=np.where(arr1>=90, 'A',np.where(arr1>=80,'B',np.where(arr1>=70,'C','D')))
    for i in arr3:
        if i =='A':
            arr2[0] += 1
        elif i == 'B':
            arr2[1] += 1
        elif i == 'C':
            arr2[2] += 1
        else:
            arr2[3] += 1

    label=['A','B','C','D']
    plt.pie(arr2,labels=label)
    plt.show()

def Q4(Score): #4번문제
    plt.boxplot(Score)
    plt.xticks([1,2,3,4],['Korea','English','Math','Science'])
    plt.show()

main()
