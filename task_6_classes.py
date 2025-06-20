def InfoStudent(student_id,**kwargs):
    print(f"Student_id: {student_id}")
    if 'student_name' in kwargs:
        print(f"Student Name: {kwargs['student_name']}" )
    if 'student_class' in kwargs:
        print(f"Student Class: {kwargs['student_class']}" )


InfoStudent(1,student_name = 'Ahmad')