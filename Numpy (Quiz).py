#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np 


# 1.จงเขียน array ที่มีแต่เลข 0 แบบ vector 10 ตัว และ แบบ Matrix 4x4

# In[3]:


np.zeros(10)


# In[5]:


np.zeros((4,4))


# 2.จงเขียน array ที่มีแต่เลข 1 แบบ vector 5 ตัว และ แบบ Matrix 3x3

# In[6]:


np.ones(5)


# In[7]:


np.ones((3,3))


# 3.จงเขียน array ที่มีเป็นการ random ตัวเลข 20 ตัว แบบ float ค่าอยู่ในช่วง 10-99 แล้วนำแต่ละเลขยกกำลังสอง

# In[111]:


x = np.random.uniform(10,100,[20])
print(x ** 2)


# 4.ทำเหมือนข้อ 3 แต่เขียนแบบ List comprehension

# In[112]:


a = [i ** 2 for i in x]
print(a)


# 5.นำข้อ 3 และ 4 มาเปรียบเวลากัน โดยใช้ฟังก์ชั่น time.time( ) เพื่อจับเวลา แสดงผลลัพธ์ในรูปแบบมิลลิวินาที

# In[116]:


x = np.random.uniform(10,100,[20])
import time 
time1 = time.time()

a = [i ** 2 for i in x]
time2 = time.time()

print(time2-time1)


# 6.จงเขียน array ที่ใช้ฟังก์ชั่นใน numpy ได้เลข 10 ถึง 1000  

# In[12]:


np.arange(10,1001)


# 7.จงเขียน array ที่ใช้ฟังก์ชั่นใน numpy ได้เลขคู่ 10 ถึง 2000 

# In[132]:


arr = np.arange(10,2001) 

arr[arr % 2 == 0]


# จงเขียน array ที่ใช้ฟังก์ชั่นใน numpy ได้เลขคี่ 12 ถึง 900

# In[133]:


arr = np.arange(12,901) 

arr[arr % 2 != 0]


# 9.จงสร้าง identity matrix แบบ 4x4

# In[25]:


np.eye(4)


# 10.จงหาว่า array ที่มีสมาชิก 100 ตัว เริ่มจาก 5 ถึง 25 มีผลต่างแต่ละตัวเท่ากับเท่าใด

# In[59]:


a = np.linspace(5,25,100)
print(a[1])
print(a[0])
print(a[1] - a[0])


# 11.จงเขียนฟังก์ชั่น random ตัวเลขแบบ float ในช่วง 0-1 ขึ้นมา 1 ตัว

# In[47]:


np.random.rand(1)


# 12. จงเขียนฟังก์ชั่นที่ random ตัวเลขแบบ int ในช่วง 50-100 โดยให้อยู่ในรูป Matrix 4x4 และ Transpose  

# In[52]:


x = np.random.randint(50,100,(4,4))
print(x.T)


# 13. ให้ array ที่กำหนด จงเขียนโค้ดที่เลือกเฉพาะ 8,9,13,14 

# In[93]:


A = np.arange(1,26)
arr = A.reshape(5,5)
print(arr)


# In[98]:


arr[1:3,2:4]


# 14. ให้ array ที่กำหนด จงเขียนโค้ดที่เลือกเฉพาะ 18,19,20

# In[99]:


arr[3,2:]


# 15. ให้ array ที่กำหนด จงเขียนโค้ดที่เลือกเฉพาะ 16,17,21,22

# In[100]:


arr[3:,0:2]


# 16. ให้ array ที่กำหนด จงเขียนโค้ดที่เลือกทั้งแถว 3
# 

# In[102]:


arr[:,2]    #not sure whether it is row 3 or column 3


# In[103]:


arr[2,:]    #not sure whether it is row 3 or column 3


# 17. จงเขียนโค้ดที่ทำให้ได้ array นี้ออกมา

# In[85]:


A = np.arange(1,26)
A.reshape(5,5)


# 18. จงเขียนโปรแกรมสุ่มเลขจำนวนเต็มในช่วง 10-100 ออกมาอยู่ใน matrix 5x5 และใช้ If-else เช็คทีละตัวว่าตัวใดบ้างที่มีค่ามากกว่า
#       50 และปริ้นออกมา

# In[199]:


arr = np.random.randint(10,100,(5,5))
#print(arr > 50)
print(arr[arr > 50])


# In[165]:


arr = np.random.randint(10,100,(5,5))
print(arr)

#if arr > 50:
    #print(arr[arr > 50])
#else: 

#ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()


# 19. จงเขียนโปรแกรมสุ่มเลขจำนวนเต็มในช่วง 10-100 ออกมาอยู่ใน matrix 5x5 และใช้ conditional selection เช็คว่าตัวใดบ้างมีค่า  
#       มากกว่า 40 นำมาใส่ List ที่สร้างใหม่ และปริ้นออกมา

# In[145]:


arr = np.random.randint(10,100,(5,5))
print(arr)

lst = []
lst.append(arr[arr > 40])
print(lst)


# 20. เขียนโปรแกรมรับค่าจากผู้ใช้ให้ป้อนเลข 9 ตัว แต่ละตัวต้องไม่ซ้ำกันและมีค่าอยู่ในช่วง 10-100 นำเลข 9 ตัวนั้นมาทำเป็น matrix 
#       3x3 และ transport และหาเลขอยู่ตำแหน่งที่ (2,2)

# In[198]:


lst = []
for i in range(9):
    r = np.random.randint(10,100)
    if r not in lst: 
        lst.append(r)
        
A = np.array(lst)  #list to array 
#print(A)

B = A.reshape(3,3)
#print(B)

C = B.T
#print(C)

print(C[2,2])

