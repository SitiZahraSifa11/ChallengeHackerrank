if __name__ == '__main__':
    grade = []
    student = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name,score])
        grade.append(score)
        
    grade.sort()
    second_min=0
    mini=grade[0]
    student.sort()
    for i in grade :
        if i != mini:
            second_min=i
            break
    for i in student:
        if i [1]==second_min:
            print(i[0])