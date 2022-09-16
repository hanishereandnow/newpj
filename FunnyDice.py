#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from random import randrange

class FunnyDice:
    def __init__(self, n=6):    # n의 디폴트 값: 6
            # 인스턴스 변수들
            self.n = int(n)
            self.numbers = list(range(1, n+1))    # 주사위 눈들
            self.index = randrange(0, self.n)    # number 리스트의 인덱스
            self.val = self.numbers[self.index]    # 주사위 눈
    
    def throw(self):    # 랜덤으로 주사위 눈이 나오게 함
        self.index = randrange(0, self.n)
        self.val = self.numbers[self.index]
    
    def getval(self):    # 주사위 눈 변수 val을 반환, getval 메서드를 호출하면 주사위 눈의 값을 얻을 수 있음
        return self.val
    # 주사위 눈 속성에 바로 접근할 수도 있지만 일반적으로 이렇게 속성에 접근하는 메서드를 구현하여 제공
    
    def setval(self, val:int):    # 사용자가 주사위 눈을 세팅할 수 있도록 만든 메서드
        if val <= self.n:
            self.val = val
        else:
            msg = "주사위에 없는 숫자입니다. 주사위는 1 ~ {0}까지 있습니다.".format(self.n)
            raise ValueError(msg)    # 범위를 벗어나면 에러 발생
    
    def get_inputs():
    n = int(input("주사위 면의 개수를 입력하세요: "))
    return n

    def main():
    n = get.inputs()
    mydice = Funnydice(n)
    mydice.throw()
    print("행운의 숫자는? {}".format(mydice.getval()))
    
    if __name__ == '__main__':
        main()

