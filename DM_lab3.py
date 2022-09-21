import numpy as np

def main():
    Score = np.random.randint(100, size=(10, 4))
    MathScore(Score)
    StdScore(Score)
    Bool(Score)
    Change(Score)


def MathScore(Score):
    print('모든 학생의 수학 점수 ==',Score[:,2])

def StdScore(Score):
    print('각 학생의 총 합 점수',Score.sum())

def Bool(Score):
    bool =np.array([True,False,False,False,True,False,True,False,True,True])
    print(Score[bool])


def Change(Score):
    print('10 * 4 ---> 4*10 ==\n',Score.transpose())

main()

