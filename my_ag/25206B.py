grade_sum = 0
all_sum = 0

for _ in range(20):
    score = list(map(str,input().split()))

    if score[2] == 'A+':
        grade_sum += float(score[1])
        all_sum += (float(score[1])*4.5)
    
    elif score[2] == 'A0':
        grade_sum += float(score[1])
        all_sum += (float(score[1])*4.0)
    elif score[2] == 'B+':  
        grade_sum += float(score[1])
        all_sum += (float(score[1])*3.5) 
    elif score[2] == 'B0':
        grade_sum += float(score[1])
        all_sum += (float(score[1])*3.0)

    elif score[2] == 'C+': 
        grade_sum += float(score[1])
        all_sum += (float(score[1])*2.5)

    elif score[2] == 'C0':
        grade_sum += float(score[1])
        all_sum += (float(score[1])*2.0)

    elif score[2] == 'D+': 
        grade_sum += float(score[1])
        all_sum += (float(score[1])*1.5)

    elif score[2] == 'D0': 
        grade_sum += float(score[1])
        all_sum += (float(score[1])*1.0)

    elif  score[2] == 'F':
          grade_sum += float(score[1])
          all_sum += (float(score[1])*0)
    else:
        pass   
print(all_sum/grade_sum)       
      
        



    