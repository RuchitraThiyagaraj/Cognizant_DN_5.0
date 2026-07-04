from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import get_db
from models import Course
from schemas import (
    CourseCreate,
    CourseUpdate,
    CourseResponse
)

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


@app.get("/")
async def root():
    return {
        "message": "API running"
    }


@app.post("/api/courses", response_model=CourseResponse)
async def create_course(
    course: CourseCreate,
    db: AsyncSession = Depends(get_db)
):

    new_course = Course(
        name=course.name,
        code=course.code,
        credits=course.credits,
        department_id=course.department_id
    )

    '''
    instead of this we can use new_course = Course(**course.model_dump()) , course.model_dump() converts the Pydantic model into a dictionary
    and ** unpacks it
    '''

    db.add(new_course)

    await db.commit()
    await db.refresh(new_course)

    return new_course

#get a specific course [when a new course is entered , automatically the course ids would be stored using auto_increment]

@app.get("/api/courses/{course_id}", response_model=CourseResponse)
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


#testing the pagination[skip and limit]
@app.get("/api/courses", response_model=list[CourseResponse])
async def get_courses(
    skip: int = 0,
    limit: int = 10,
    department_id: int | None = None,
    #We can also use Optional[int]=None
    db: AsyncSession = Depends(get_db)
):

    query = select(Course)

    #query.where isnt an async func so await isnt needed
    if department_id is not None:
        query = query.where(
            Course.department_id == department_id
        )

    query = query.offset(skip).limit(limit)

    result = await db.execute(query)

    courses = result.scalars().all()

    return courses


@app.put("/api/courses/{course_id}", response_model=CourseResponse)
async def update_course(
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

    if course.name is not None:
        existing_course.name = course.name

    if course.code is not None:
        existing_course.code = course.code

    if course.credits is not None:
        existing_course.credits = course.credits

    if course.department_id is not None:
        existing_course.department_id = course.department_id

    await db.commit()
    await db.refresh(existing_course)

    return existing_course



@app.delete("/api/courses/{course_id}")
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

    return {
        "message": "Course deleted successfully"
    }