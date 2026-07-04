from fastapi import FastAPI, Depends, HTTPException, status , BackgroundTasks, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select , func , or_
from typing import Optional

from database import get_db

from models import (
    Student,
    Course,
    Enrollment
)

from schemas import (
    StudentCreate,
    StudentUpdate,
    StudentResponse,
    CourseCreate,
    CourseUpdate,
    CourseResponse,
    EnrollmentCreate,
    EnrollmentUpdate,
    EnrollmentOut,
    PaginatedCourseResponse
)

'''
I used URL versioning in this api by adding /v1/ to all endpoints (eg /api/v1/courses). This makes it easier to introduce future versions like /v2 without affecting users who are still using the older version.

Another way to version an API is by using headers.In that approach,the URL stays the same (for example, /api/courses), and the client tells the server which version to use by sending a header like Accept: application/vnd.api+json;version=1. While this keeps the URLs clean, URL versioning is simpler to understand, test, and maintain.
'''

#adding some extra details which would be visible in /docs
app = FastAPI(
    title="Course Management API",
    description='''A REST API to manage courses, departments, and students.
                   GITHUB URL: https://github.com/RuchitraThiyagaraj/Cognizant_DN_5.0/tree/main''',
    version="1.0",
    contact={
        "name": "Ruchitra",
        "email": "ruchitra@example.com",
    }
)

'''
HTTP 204 means:
the request succeeded but there is no content to send back
'''

@app.get("/api/v1/")
async def root():
    return {
        "message": "API running"
    }


@app.post(
    "/api/v1/courses",
    response_model=CourseResponse,
    tags=["Courses"],
    summary="Create a new course",
    response_description="The created course with generated ID",
    status_code=201
)
async def create_course(
    course: CourseCreate,
    response: Response,
    db: AsyncSession = Depends(get_db)
):

    new_course = Course(
        name=course.name,
        code=course.code,
        credits=course.credits,
        department_id=course.department_id
    )
    

    db.add(new_course)
    await db.commit()
    await db.refresh(new_course)
    
    response.headers["Location"] = f"/api/v1/courses/{new_course.id}/"
    return new_course

#get a specific course [when a new course is entered , automatically the course ids would be stored using auto_increment]

@app.get("/api/v1/courses/{course_id}", tags=["Courses"],  response_model=CourseResponse)
async def get_course(
    course_id: int,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    course = result.scalar_one_or_none()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return course

'''
diff from previous version:
added page , page_size rather than skip , limit
computed skip and limit
sent the response in DRF[django response format] -> {count , list of rows , previojs , next}
implemented search functionality
'''

#testing the pagination[skip and limit]

@app.get(
    "/api/v1/courses",
    tags=["Courses"],
    response_model=PaginatedCourseResponse)

async def get_courses(
    page: int = 1,
    page_size: int = 10,
    department_id: Optional[int] = None,
    search: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    query = select(Course)

    #filter it if deptid isnt none
    if department_id is not None:
        query = query.where(Course.department_id == department_id)
    if search:
        search = search.lower()
        
        query = query.where(
            or_(
                func.lower(Course.name).like(f"%{search}%"),
                func.lower(Course.code).like(f"%{search}%")
            )
        )

    #count of rows
    count_query = select(func.count()).select_from(Course)
    
 
    if search:
        count_query = count_query.where(
            or_(
                func.lower(Course.name).like(f"%{search}%"),
                func.lower(Course.code).like(f"%{search}%")
            ) 
        )

    if department_id is not None:
        count_query = count_query.where(Course.department_id == department_id)

    total_count = (await db.execute(count_query)).scalar()

    #calculatinh skip value using page and page_size
    skip = (page - 1) * page_size
    query = query.offset(skip).limit(page_size)

    #fetch data using 
    result = await db.execute(query)
    courses = result.scalars().all()

    #returning in DRF [django response format]
    return {
        "count": total_count,
        "next": f"/api/v1/courses?page={page+1}&page_size={page_size}&department_id={department_id}&search={search}" if page * page_size < total_count else None,
        "previous": f"/api/v1/courses?page={page-1}&page_size={page_size}&department_id={department_id}&search={search}" if page > 1 else None,        
        "results": courses
    }

'''
using ilike -> postgresql
if search:
    query = query.where(
        or_(
            Course.name.ilike(f"%{search}%"),
            Course.code.ilike(f"%{search}%")
        )
    )
'''

'''
Another method for computing the count:
all_courses = await db.execute(select(Course))
courses = all_courses.scalars().all()
count = len(courses)

but it is too slow coz it loads ALL rows into memory
'''


@app.patch("/api/v1/courses/{course_id}", tags=["Courses"],  response_model=CourseResponse)
async def patch_course(
    course_id: int,
    course: CourseUpdate,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    existing_course = result.scalar_one_or_none()

    if existing_course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    for key, value in course.model_dump(exclude_unset=True).items():
        setattr(existing_course, key, value)

    await db.commit()
    await db.refresh(existing_course)

    return existing_course



@app.delete("/api/v1/courses/{course_id}" , tags=["Courses"], status_code=204)
async def delete_course(
    course_id: int,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    course = result.scalar_one_or_none()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    await db.delete(course)

    await db.commit()


#create new stufent
@app.post(
    "/api/v1/students",
    response_model=StudentResponse,
    tags=["Students"],
    status_code=201
)
async def create_student(
    student: StudentCreate,
    response: Response,
    db: AsyncSession = Depends(get_db)
):

    new_student = Student(**student.model_dump())

    db.add(new_student)
    await db.commit()
    await db.refresh(new_student)
    
    response.headers["Location"] = f"/api/v1/students/{new_student.id}/"
    return new_student

#get a specific student by their id
@app.get("/api/v1/students/{student_id}",tags=["Students"], response_model=StudentResponse)
async def get_student(
    student_id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Student).where(Student.id == student_id)
    )

    student = result.scalar_one_or_none()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student

#get all students
@app.get("/api/v1/students",tags=["Students"], response_model=list[StudentResponse])
async def get_students(
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(Student))
    return result.scalars().all()


#UPDATE A STUDENT
#user enters name , email , age , dept [StudentResponse]
#app sends id , name , email , age , department
#user cant update an id because it is auto incremented by the app

@app.patch("/api/v1/students/{student_id}",tags=["Students"], response_model=StudentResponse)
async def update_student(
    student_id: int,
    student: StudentUpdate,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Student).where(Student.id == student_id)
    )

    existing_student = result.scalar_one_or_none()

    if existing_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    updated_data = student.model_dump(exclude_unset=True)

    for key, value in updated_data.items():
        setattr(existing_student, key, value)

    await db.commit()
    await db.refresh(existing_student)

    return existing_student

#what if the user didnt post the age during creation and tries to update the age => age would be updated from null to the given value
'''
Instead of that , we can use     
for key, value in student.model_dump(exclude_unset=True).items():
        setattr(existing_student, key, value)

'''

#Delete a student

@app.delete(
    "/api/v1/students/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT,tags=["Students"],
)
async def delete_student(
    student_id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Student).where(Student.id == student_id)
    )

    student = result.scalar_one_or_none()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    await db.delete(student)
    await db.commit()


#Get all enrollments
@app.get("/api/v1/enrollments",tags=["Enrollments"], response_model=list[EnrollmentOut])
async def get_enrollments(db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(Enrollment))
    enrollments = result.scalars().all()

    return enrollments


#get an enrollment by id
@app.get("/api/v1/enrollments/{enrollment_id}", tags=["Enrollments"],response_model=EnrollmentOut)
async def get_enrollment(
    enrollment_id: int,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Enrollment).where(Enrollment.id == enrollment_id)
    )

    enrollment = result.scalar_one_or_none()

    if enrollment is None:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    return enrollment

#delete an enrollment
@app.delete("/api/v1/enrollments/{enrollment_id}",tags=["Enrollments"], status_code=status.HTTP_204_NO_CONTENT)
async def delete_enrollment(
    enrollment_id: int,
    db: AsyncSession = Depends(get_db)
):

#we can also use status_code=status.HTTP_204_NO_CONTENT

    result = await db.execute(
        select(Enrollment).where(Enrollment.id == enrollment_id)
    )

    enrollment = result.scalar_one_or_none()

    if enrollment is None:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    await db.delete(enrollment)
    await db.commit()

#BACKGROUND TASKS
def send_confirmation_email(student_email: str):
    print(f"Sending confirmation to {student_email}")

'''
checks if student exists
checks if course exists
checks if enrollment exists 

if(true) then raise exception
'''

#fastapi automatically injects BackGround tasks from from fastapi import BackgroundTasks during runtimeuvicorn
#add enrollments
@app.post(
    "/api/v1/enrollments",
    response_model=EnrollmentOut,
    tags=["Enrollments"],
    status_code=201
)
async def create_enrollment(
    enrollment: EnrollmentCreate,
    background_tasks: BackgroundTasks,
    response: Response,
    db: AsyncSession = Depends(get_db),

):

    result = await db.execute(
        select(Student).where(Student.id == enrollment.student_id)
    )
    student = result.scalar_one_or_none()

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    result = await db.execute(
        select(Course).where(Course.id == enrollment.course_id)
    )
    course = result.scalar_one_or_none()

    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    result = await db.execute(
        select(Enrollment).where(
            Enrollment.student_id == enrollment.student_id,
            Enrollment.course_id == enrollment.course_id
        )
    )
    existing_enrollment = result.scalar_one_or_none()

    if existing_enrollment:
        raise HTTPException(
            status_code=409,
            detail="Student is already enrolled in this course"
        )

    new_enrollment = Enrollment(
        student_id=enrollment.student_id,
        course_id=enrollment.course_id
    )

    db.add(new_enrollment)
    await db.commit()
    await db.refresh(new_enrollment)

    response.headers["Location"] = f"/api/v1/enrollments/{new_enrollment.id}/"

    background_tasks.add_task(
        send_confirmation_email,
        student.email
    )

    return new_enrollment
#update enrollment
@app.patch("/api/v1/enrollments/{enrollment_id}",tags=["Enrollments"], response_model=EnrollmentOut)
async def update_enrollment(
    enrollment_id: int,
    enrollment: EnrollmentUpdate,
    db: AsyncSession = Depends(get_db)
):

    # Check if enrollment exists
    result = await db.execute(
        select(Enrollment).where(Enrollment.id == enrollment_id)
    )

    existing_enrollment = result.scalar_one_or_none()

    if existing_enrollment is None:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    # Check if student exists
    if enrollment.student_id is not None:
        result = await db.execute(
            select(Student).where(Student.id == enrollment.student_id)
        )

        student = result.scalar_one_or_none()

        if student is None:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

    # Check if course exists
    if enrollment.course_id is not None:
        result = await db.execute(
            select(Course).where(Course.id == enrollment.course_id)
        )

        course = result.scalar_one_or_none()

        if course is None:
            raise HTTPException(
                status_code=404,
                detail="Course not found"
            )

    # Update only the fields sent by the user
    updated_data = enrollment.model_dump(exclude_unset=True)

    for key, value in updated_data.items():
        setattr(existing_enrollment, key, value)

    await db.commit()
    await db.refresh(existing_enrollment)

    return existing_enrollment


#get all students enrolled in a specific
@app.get("/api/v1/courses/{course_id}/students",tags=["Enrollments"], response_model=list[StudentResponse])
async def get_course_students(
    course_id: int,
    db: AsyncSession = Depends(get_db)
):

    #check if the course exists
    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    course = result.scalar_one_or_none()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    #get all students enrolled in the course
    result = await db.execute(
        select(Student)
        .join(Enrollment, Student.id == Enrollment.student_id)
        .where(Enrollment.course_id == course_id)
    )

    students = result.scalars().all()

    return students