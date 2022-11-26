import random
dic={}
score=0
n=int(input("Enter total number of question : "))
if n>=5:
    for i in range(1,n+1):
        q=input("ENTER YOUR QUESTION HERE : ")
        a=input("ENTER CORRECT ANSWER(True/False) : ")
        A=a.upper()
        dic[q]=A
    list_keys=list(dic.keys())
    list_values=list(dic.values())
    for i in range(1,6):
        m=random.randrange(0,n)
        print('QUESTION',i)
        print(list_keys[m])
        ans=input("enter your answer :")
        Ans=ans.upper()
        if Ans==list_values[m]:
            print("congrats!!! your answer is correct")
            score=score+1
        else:
            print("sorry!!! your answer is wrong")
    print("your total marks is : ",score)
    print("THANK YOU")
else:
    print("INVALID NUMBER OF QUESTION")


