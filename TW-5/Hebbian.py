#Implementation of AND gate using Hebbian Learning Rule

X=[[-1,-1,1],[-1,1,1],[1,-1,1],[1,1,1]] #its in a form of [x1,x2, b]   i.e dataFrame of x1,x2 and bias
Y=[-1,-1,-1,1] #Output required

def NetValue(W): #This function takes final weights and bias from WeightBiasMat Matrix
    FinalW1,FinalW2,FinalBias=W
    Net=[]
    for i in X:
        NetV=FinalW1*i[0]+FinalW2*i[1]+FinalBias#formula used to calculate net value wrt imputs x1,x2
        Net.append(NetV)

    return Net


def ANDwithHebb_LR():
    weight1=weight2=b=0#initial weights and bias
    WeightBiasMat=[]#matrix to hold updated weights wrt inputs
    count=0
    while count<4:#for learning and updating weights
        for i in X:
            temp=[]
            weight1+=i[0] * Y[count]#formula to update weights Weight(new)=Weight(old)+x*y
            weight2+=i[0]*Y[count]

            b+=1 *Y[count]#formula to update bias; bias(new)=bias(old)+y

            temp.append(weight1)
            temp.append(weight2)
            temp.append(b)

            WeightBiasMat.append(temp) #append list to matrix

            count+=1
    print("Weight Matrix>>>",WeightBiasMat)
    print()
    ResultFromNet=NetValue(WeightBiasMat[-1]) #last row of Matrix is final required weight and bias
    Prediction=[] # Values in ResulFromNet will be combination of +ve & -ve where +ve => 1 ; and -ve => -1 or 0 in Binary
    print("NetWeightMatrix",ResultFromNet)
    print()
    for i in ResultFromNet:
        if i>0:
            Prediction.append(1)
        else:
            Prediction.append(-1)
    print("Required >>>{}\nPredicted From Hebbian Learning Rule >>>{}".format(Y,Prediction))

ANDwithHebb_LR()

#Code works for both AND and OR gate
