def OR():
    w1=0;w2=0;a=0.2;t=0
    X=[[0,0],[0,1],[1,0],[1,1]]
    Y=[0,1,1,1]

    while(True):
        Out=[]
        count = 0
        for i in X:
            step=(w1*i[0]+w2*i[1])
            if step<=t:
                O=0
                if O==Y[count]:
                    Out.append(O)
                    count+=1
                else:
                    w1=w1+(a*i[0]*1)
                    w2=w2+(a*i[1]*1)
                    print(w1,w2)

            else:
                O=1
                if O==Y[count]:
                    Out.append(O)
                    count+=1
                else:
                    w1 = w1 + (a * i[0] * 0)
                    w2 = w2 + (a * i[1] * 0)
                    print(w1,w2)
        print("------->")
        if Out[0:]==Y[0:]:
            print("Final Output of OR ::\n")
            print("Weights: w1={} and w2={} >>>> {}".format(w1,w2,Out))
            break

OR()