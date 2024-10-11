

f=open('answers.csv','r')

answers=[]
for row in f:
    print(repr(row))
    answers.append(row)
f.close()

list=[]
for i in answers:
    list.append(i.strip().split(","))
print(list)

resultsHeader="No estudiante, No aciertos\n"
with open("ResultsExam.csv","w") as outputFile:
    outputFile.write(resultsHeader)

answerKey=["D","B","D","C","C","D","A","E","A","D"]
print("\t Student number \tCorrect answers")
print("\t---------------------------------------------------------------------------------")

for j in range (len(list)):
    results=""
    correctAnswers=0
    for k in range(len(list[j])):
        if list[j][k]==answerKey[k]:
            correctAnswers+=1
    print(f"\t\t{[j+1]}\t\t\t\t{correctAnswers}")
    results+=str(j)+","+str(correctAnswers)+"\n"
    outputFile.write(results)




