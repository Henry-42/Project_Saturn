import mysql.connector


def get_db_connect():
    connection = mysql.connector.connect(user='kyley9',
                                         password='224085274',
                                         host='10.8.37.226',
                                         database='kyley9_db')
    return connection


def get_x_schedule(status):
    match status:
        case "Teacher":
            return 'Teacher'
        # Return procedure for the thingy
        case "Student":
            sid = input("Enter Student ID: ")

            results = get_student_schedule(sid)

            for result in results:
                period = results[1]
                course_name = results[2]
                room = results[3]
                teacher_name = results[4]
                print("Period:", period)
                print("Course:", course_name)
                print("Room:", room)
                print("Teacher:", teacher_name)
                print()


def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    results = []

    for row in cursor:
        results.append(row)
    cursor.close()
    connection.close()

    return results


def get_student_schedule(sid):
    statement = "CALL Student_Scehdule_Procedure(" + sid + ")"
    return execute_query(get_db_connect(), statement)


status = input("Are you a teacher or a student? ")

get_x_schedule(status)
