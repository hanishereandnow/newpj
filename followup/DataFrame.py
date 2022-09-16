#!/usr/bin/env python
# coding: utf-8

# 4-2 기초분석을 위한 라이브러리

# # DataFrame 만들기

# In[3]:


# pandas를 pd이름으로 호출
import pandas as pd

# customer_lib_1.csv 파일을 불러와서 변수 customer_1 값으로 할당
customer_1 = pd.read_csv('~/aiffel/data_analysis_basic/data/customer_lib_1.csv')

# customer_lib_2.csv 파일을 불러와서 변수 customer_2 값으로 할당
customer_2 = pd.read_csv('~/aiffel/data_analysis_basic/data/customer_lib_2.csv')

# 할당된 customer_1 변수 호출
customer_1


# # DataFrame 읽어오기

# In[4]:


# 할당된 customer_2 변수 호출
customer_2


# In[5]:


# 데이터프레임 헤드 부분 읽어오기
customer_1.head()


# In[6]:


# 데이터프레임 테일 부분 읽어오기
customer_2.tail()


# In[7]:


# 데이터프레임 열이름(컬럼) 확인하기
customer_1.columns


# In[8]:


# 데이터프레임 개별 값의 자료형태 확인하기
customer_1.dtypes


# In[9]:


# 데이터프레임의 종합 정보 확인하기
customer_1.info()


# In[10]:


# 데이터프레임의 기술 통계량 확인하기
customer_2.describe()


# # 시리즈 선택하기

# In[11]:


# 데이터프레임의 특정 열(Name) 선택하기
customer_1['Name']


# # 여러 개의 열 선택하기

# In[12]:


# 데이터프레임의 여러 열(Name, Email) 선택하기
customer_1[['Name', 'Email']]


# # 열 값을 기준으로 필터링 하기

# In[13]:


# OS열값이 Android인 행들만 선택하기
customer_1[customer_1['OS'] == 'Android']


# In[14]:


# OS열값이 Android이고 MobileCompany열값이 SKT인 행들만 선택하기
customer_1[(customer_1['OS']=='Android') & (customer_1['MobileCompany']=='SKT')]


# # 행 값을 기준으로 인덱싱 하기

# In[15]:


# 인덱스 11인 행 값 불러오기
customer_1.iloc[11]


# In[16]:


# 인덱스 11인 행 값 중 3번째 열까지 불러오기
customer_1.iloc[11, :3]


# ### 행 값을 기준으로 인덱싱을 할 때 loc()과 iloc()의 쓰임새는 같습니다. 하지만 열 값까지 인덱싱을 할 때는 다르죠.
# ### iloc()은 인자로 숫자만 받는 반면 (x번째 행, y번째 열, ...), loc()은 행과 열의 이름(Customer_Id, Name, ...)을 사용할 수 있습니다.

# In[17]:


# 인덱스명이 11인 행 값 불러오기
customer_1.loc[11]


# In[18]:


# 인덱스 이름이 11인 값 중 열 이름 'Customer_Id','Name','Nickname'에 대한 값 불러오기
customer_1.loc[11,['Customer_Id','Name','Nickname']]


# # 열 값 계산하기

# In[19]:


# HP 열 값과 MP 열 값을 더하기
customer_2['HP'] + customer_2['MP']


# # 새로운 열 추가하기

# In[20]:


# Avg열을 만들고 HP 열 값과 MP 열 값의 평균값으로 채우기
customer_2['Avg'] = (customer_2['HP'] + customer_2['MP']) / 2
customer_2


# # 두 개의 데이터프레임 결합하기

# In[21]:


# 데이터프레임 customer_1과 customer_2를 세로 방향으로 결합하기
pd.concat([customer_1, customer_2])


# In[22]:


# 데이터프레임 customer_1과 customer_2를 가로 방향으로 결합하기
pd.concat([customer_1, customer_2], axis=1).head()


# In[23]:


# 데이터프레임 customer_1의 오른쪽에 customer_2를 결합하기
customer = pd.merge(customer_1, customer_2)
customer


# # 필요없는 열 삭제하기

# In[30]:


# Password와 C.P.열을 삭제한 데이터프레임을 기존 데이터프레임에 저장하기
customer = customer.drop(['Password', 'C.P.'], axis=1)
customer


# # 열 값을 기준으로 정렬하기

# In[31]:


# Avg열값을 내림차순으로 정렬하기
customer.sort_values(by=['Avg'], ascending=False)


# In[32]:


# Avg열값 중 가장 큰 값의 인덱스 찾기
customer['Avg'].idxmax(axis=0)


# In[33]:


# 데이터프레임 중 인덱스명 306 찾기
customer.loc[306]


# # Numpy: 다차원배열(ndarray)를 기본 자료구조로 사용한다

# In[34]:


# Numpy를 np이름으로 호출하기
import numpy as np


# In[35]:


# Customer 데이터프레임 중 20개를 샘플링해보기
customer.sample(n=20)


# In[36]:


# Customer 데이터프레임 중 10%를 샘플링하고 customer_sample로 저장하기
customer_sample = customer.sample(frac=0.1)
customer_sample.info()


# In[37]:


#customer_sample에서 HP와 Defense 간 상관계수 도출하기
np.corrcoef(customer_sample['HP'], customer_sample['Defense'])

