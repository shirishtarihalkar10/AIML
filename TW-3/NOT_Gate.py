def NOT():
    X=[0,1]
    Y=[1,0]
    weight=-1
    bias=1;Out=[]

    for i in X:
        j=weight*i+bias
        Out.append(j)
    for i in X:
        print("NOT Gate {}-->{}".format(X[i],Out[i]))

NOT()