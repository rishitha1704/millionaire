questions=[
 ["What is the capital of India?","New Delhi","Hyderabad","Mumbai","Kolkata",1],
 ["What is the National Bird of India?","Crow","peacock","parrot","swan",2],
 ["Who is the first president of India?","Ram prasad","Jawharlal nehru","Rajendra prasad","Amebedkar",3],
["What is the national currency of India","Rupee","ponds","Dollars","None",1],
["Which is the largest state in India by area ?","Telangana","Karnataka","Rajasthan","Madhya pradesh",3],
 ["Which Indian festival is known as 'Festival of lights' in India?","Dusserha","Holi","Diwali","None",3],
 ["Who is the current prime minister of India?","Rahil Gandhi","Narendra Modi","KCR","YSR",2],
 ["What is the highest civilan award in India?","Bharata Ratna","Padma shri","Padma Bhushan","None",1],
 ["Who is the chief Minister of Telangana?","KTR","Modi","YSR","None",4],
["Who was the first woman Prime Minister of India?","Lalitha","Sonia Gandhi","Indira gandhi","none",3],
 ["Which river is often referred to as the 'Ganga of the South'?","Ganga","Godavari","Narmada","Bramaputra",2],
["Which state is famous for its backwaters and houseboat tourism?","kerala","karnataka","AP","Tamil nadu",1],
["who is lead actor of Bhahubali?","Ram","NTR","Prabhas","Rana",3],
["Who is the Director of RRR?","DNR","Trivikram","Sukumar","Rajamouli",4]
]
level=[1000,2000,3000,4000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
money=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"Here is your question for RS {level[i]} ")
    print(f"{question[0]}")
    print(f"a.{question[1]}    b.{question[2]}")
    print(f"c.{question[3]}    d.{question[4]}")
    reply=int(input("Enter your answer (1-4) or 0 to quit: "))
    if(reply==0):
        money=level[i-1]
        break
    if(reply==question[-1]):
        print(f"Correct answer,your have won Rs {level[i]}")
        if(i==4):
            money=10000
        elif(i==9):
            money=320000
        elif(i==14):
            money=10000000
    else:
        print("Wrong answer!!")
        money=question[i]
print(f"Yo're home take money is {money}")

