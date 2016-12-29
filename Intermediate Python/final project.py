from statistics import mean as m

admins = {'Aykut':'aykut5396','user2':'Pass182'}

studentDict = {'Jeff': [78,88,98],'Alex':[92,76,93,],'Sam':[89,92,93]}

def enterGrades():
    nameToEnter = input('Student Name:')
    gradeToEnter = input('Grade:')

    if nameToEnter in studentDict:
        print('Adding Grade.....')
        studentDict[nameToEnter].append(float(gradeToEnter))
    else:
        print('Student does not exist.')

    print(studentDict)

def removeStudent():
    nameToRemove == input('What student to remove?:')
    if nameToRemove in studentDict:
        print('Removing student.....')
        del studentDict[nameToRemove]

        print(studentDict)

def StudentAVGs():
    for eachStudent in studentDict:
        gradeList = studentDict[eachStudent]
        avgGrade = m(gradeList)

        print(eachStudent,'has a average of:',avgGrade)


def main():
    print("""
    Welcome to the grade book

    [1] - Enter Grade
    [2] - Remove Student
    [3] - Student Average Grades
    [4] - Exit
    """)

    action = input('what would you like to do today (Enter a number)')

    if action == '1':
        enterGrades()
    elif action == '2':
        removeStudent()
    elif action == '3':
        StudentAVGs()
    else:
        print('no valid choice')

login = input('Username:')
passw = input('Password:')

if login in admins:
    if admins[login] == passw:
        print('Welcome',login)
        while True:
            main()
        else:
            print('Invalid password, exploding in two seconds')

else:
    print('Invalid username or password, try again....')

