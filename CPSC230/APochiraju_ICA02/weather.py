c=int(input("give a temperature in Celsius"))
(c*(9/5))+32
f=(c*(9/5)+32)
if(f<32):
    print("it's too cold")
elif(32<f<75):
    print("it's moderate")
elif(f>75):
    print("it's too hot")
