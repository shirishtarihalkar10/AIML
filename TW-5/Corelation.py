#Implementation of AND gate using Correlation Learning Rule

lr=0.2
X=[[-1,-1,1],[-1,1,1],[1,-1,1],[1,1,1]] #its in a form of [x1,x2, b]   i.e dataFrame of x1,x2 and bias
Y=[-1,-1,-1,1] #Output required
def NetValue(W): #This function takes final weights and bias from WeightBiasMat Matrix
    FinalW1,FinalW2,FinalBias=W
    Net=[]
    for i in X:
        NetV=FinalW1*i[0]+FinalW2*i[1]#formula used to calculate net value wrt imputs x1,x2
        Net.append(NetV)

    return Net


def ANDwithCorr_LR():
    weight1=weight2=b=0
    WeightBiasMat=[]#matrix to hold updated weights wrt inputs
    count=0
    while count<4:#for learning and updating weights
        for i in X:
            #print(i)
            temp=[]
            weight1+=i[0]
            weight2+=i[0]
            b+=1
            if (weight1 and weight2)>=0: #most +ve
                weight1*=i[0]*1*lr
                weight2*=i[0]*1*lr
                b*=1*lr
            else:                        #most -ve
                weight1*=i[0]*-1*lr
                weight2*=i[0]*-1*lr
                b*=-1*lr


            temp.append(round(weight1,3))
            temp.append(round(weight2,3))
            temp.append(round(b,3))

            WeightBiasMat.append(temp)
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
    print("Required >>>{} \nPredicted From Correlation Learning Rule >>>{}".format(Y,Prediction))

ANDwithCorr_LR()

#Code works for both AND and OR gate
