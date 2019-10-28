import random

st = set()

x1 = 20
y1 = 20
r = 30


while len(st)<50:
    x = random.randint(0,r) + x1
    y = random.randint(0,r) + y1
    st.add((x,y,1))

x1 = 100
y1 = 100
r = 30

while len(st)<100:
    x = random.randint(0,r) + x1
    y = random.randint(0,r) + y1
    st.add((x,y,2))

x1 = 50
y1 = 70
r = 30

while len(st)<150:
    x = random.randint(0,r) + x1
    y = random.randint(0,r) + y1
    st.add((x,y,3))


for x in st:
    print(str(x[0])+","+str(x[1])+","+str(x[2]))