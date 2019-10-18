import random

st = set()

while len(st)<250:
    x = random.randint(1,201)
    y = random.randint(1,201)
    st.add((x,y))



for x in st:
    print(str(x[0])+","+str(x[1]))