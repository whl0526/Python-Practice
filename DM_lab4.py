import numpy as np


def main():
    Score = np.random.randint(100,size=(10,4))
    Q1(Score)
    print('\n')
    Q2(Score)
    print('\n')
    Q3(Score)
    print('\n')
    Q4()
    print('\n')



def Q1(Score):#1번문제
    a=np.where(Score >= 90, 'A',np.where(Score >= 80, 'B',np.where(Score >= 70, 'C',np.where(Score < 70, 'D',Score))))
    print('1번.\n',a)

def Q2(Score):#2번문제
      arr1=Score.mean(axis=0)
      a1=(Score[:10, 0] - arr1[0]).reshape(10,1)
      a2=(Score[:10, 1] - arr1[1]).reshape(10,1)
      a3=(Score[:10, 2] - arr1[2]).reshape(10,1)
      a4=(Score[:10, 3] - arr1[3]).reshape(10,1)
      b=np.hstack((a1,a2,a3,a4))
      print('2번.\n',b)

def Q3(Score):#3번문제
    global d
    c=np.array([])
    for i in range(10):
        c= np.append(c,[Score[i,:].sum()])
    d=np.c_[Score,c]
    print('3번.\n',d)

def Q4():#4번문제
    arr2 = d.mean(axis=1)
    g=np.c_[d,arr2]
    arr3 =g.mean(axis=0)

    h= np.r_[g,[arr3]]
    print('4번.\n',h)


main()
