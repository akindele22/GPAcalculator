def gpa():
    num_courses = int(input("Enter num of courses: "))
    student_name = input(" Enter a name : ")
    grades = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 1, "F": 0}
    total_cu = 0
    x = 0

    for num in range(num_courses):  # this is to loop the calculation of each course
        # Collection of user data           #x = num.split(" ")
        # User course code in capitalization
        course_code = input("Enter your course code: ").upper()

        #score = int(input('Enter a score : '))  # user score

        # User credit unit for each use course
        credit_unit = int(input('Enter a credit unit : '))

        # User grade point bonus for each course scores
        grade_points = input('Enter a grade point: ').upper()
        if grade_points in grades:
            new = int(grades[grade_points])
            x = new * credit_unit
            total_cu = + credit_unit
            cgpa = x/total_cu

    #print('The CGPA result of ', student_name, cgpa)
    print(cgpa)


gpa()
