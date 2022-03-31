import time
i=time.time()

k=0
while(k<=10):
    print(k)
    #time.sleep(1)
    k=k+1
print("while loop ",time.time()-i)

i2=time.time()
for x in range(10):
    print(x)
print("for loop",time.time()-i2)