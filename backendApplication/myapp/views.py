from django.http import JsonResponse
from .models import Student, Course, StudentCourse, Mentor


def getStudents(request):
    try:
        students = Student.objects.all()
        data = {"students": list(students.values())}
        return JsonResponse(data, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def getMentors(request):
    try:
        mentors = Mentor.objects.all()
        data = {"mentors": list(mentors .values())}
        return JsonResponse(data, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def getCourses(request):
    try:
        courses = Course.objects.all()
        data = {"courses": []}

        for course in courses:
            mentor_name = course.mentor.name if course.mentor else None
            course_data = {
                "id": course.id,
                "name": course.name,
                "price": course.price,
                "specialty": course.specialty,
                "mentor": mentor_name + " id: " + str(course.mentor.id),
            }
            data["courses"].append(course_data)

        return JsonResponse(data, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def getStudentCourse(request):
    try:
        student_courses = StudentCourse.objects.all()
        data = {"studentCourse": []}

        for el_student_course in student_courses:
            student_name = el_student_course.student.name if el_student_course.student else None
            course_name = el_student_course.course.name if el_student_course.course else None

            course_data = {
                "id": el_student_course.id,
                "student": student_name + " id: " + str(el_student_course.student.id),
                "course": course_name + " id: " + str(el_student_course.course.id),
            }
            data["studentCourse"].append(course_data)

        return JsonResponse(data, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
