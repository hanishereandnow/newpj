#!/usr/bin/env python
# coding: utf-8

# # < 메소드 오버라이딩과 메소드 오버로딩 in Python>

# ## 메소드 오버라이딩
# ### - 부모 클래스의 메소드를 자식 클래스에서 '재정의(override)'하여 사용
# ### - 기존 부모 클래스의 메소드가 자식 클래스에서 변경된다
# ### - 다형성 구현이 가능하다 : 하나의 부모를 정하고 다양한 형태로 상속을 받는다

# In[7]:


# 메소드 오버라이딩의 예

class Car:
    color = 'red'
    category = 'sports car'

    def drive(self):
        print("I'm driving")

class NewCar(Car):
    def fly(self):
        print("I'm flying!! This is the new car!!")

    def drive(self):    # 오버라이딩이 일어난다
        print("I'm driving and can fly") 
        
cr = Car()
ncr = NewCar()

cr.drive()
ncr.drive()


# ## 메소드 오버로딩
# ### - 같은 클래스 내에서 매개변수의 개수 또는 자료형이 다른, 같은 이름의 메소드를 정의
# ### - 다양한 매개변수를 처리하기 위해 필요하다

# In[14]:


# 메소드 오버로딩의 예 1

class Fruits:

    def buy(self, a, b, p):
        print("apple:",a, " banana:",b, " peach:",p)
        
    def buy(self, g, pr):
        print(" grapes:",g, " pear:",pr)
    
fr = Fruits()
fr.buy(1, 2, 3)

# TypeError 발생
# 파이썬에서는 메소드 오버로딩을 지원하지 않는다


# In[35]:


# 메소드 오버로딩의 예 2
# 자료형에 따른 분기처리

class Option:

    def add(self, datatype, *args):    # *args: 여러 개의 인자를 받기 위해 쓰인다
        if datatype == 'int':
            return sum(args)
        if datatype == 'str':
            return ''.join([x for x in args])
        
op = Option()
print("자료형이 int면 합을 구합니다.", op.add('int', 5, 7, 9))
print("자료형이 str면 나열합니다.", op.add('str', 'method', ' ','overloading'))


# In[19]:


# 메소드 오버로딩의 예 3

from multipledispatch import dispatch    # pip install multipledispatch로 패키지를 다운로드 하면 오버로딩 사용할 수 있다

class Fruits:
    
    @dispatch(int, int, int)
    def buy(self, a, b, p):
        print("apple:",a, " banana:",b, " peach:",p)
    
    @dispatch(int, int)
    def buy(self, g, pr):
        print("grapes:",g, " pear:",pr)
    
fr = Fruits()
fr.buy(1, 2, 3)
fr.buy(5, 6)


# 참고: https://junior-datalist.tistory.com/96
