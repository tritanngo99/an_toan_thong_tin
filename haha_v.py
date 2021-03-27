#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pwn import *


# In[2]:


r = remote('mercury.picoctf.net',20266)


# In[3]:


rka = r.recvline()
print(rka)
rka = r.recvline()
print(rka)
rka = r.recvline()
print(rka)
rka = r.recvline()
print(rka)
#tmp = "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
tmp = ""
charr = "0"
for i in range(0,144):
    tmp = tmp + charr
for i in range(0,351):
    print("Lan {0}: ".format(i))
    r.sendline(str(tmp).encode())
    rka = r.recvline()
    print(rka)
    rka = r.recvline()
    print(rka)


