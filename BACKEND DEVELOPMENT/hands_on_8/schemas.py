from typing import Optional,List
from pydantic import BaseModel, ConfigDict, EmailStr


class CourseCreate(BaseModel):
    name: str
    code: str
    credits: int
    department_id: int


class CourseUpdate(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    credits: Optional[int] = None
    department_id: Optional[int] = None

'''
USE of     model_config = ConfigDict(from_attributes=True):

pydantic works with JSON / dict / Pydantic models
but SQLAlchemy gives ORM objects
so we enable Pydantic to read ORM objects using attributes
'''
class CourseResponse(BaseModel):
    id: int
    name: str
    code: str
    credits: int
    department_id: int

    model_config = ConfigDict(from_attributes=True)


class StudentCreate(BaseModel):
    name: str
    email: str
    age: Optional[int] = None
    department_id: Optional[int] = None

#studentupdate is used when a user sends the details whereas the other one is the app sending to the frontent
class StudentUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None
    department_id: Optional[int] = None


class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    age: Optional[int] = None
    department_id: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)



class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int


class EnrollmentOut(BaseModel):
    id: int
    student_id: int
    course_id: int

    model_config = ConfigDict(from_attributes=True)


class EnrollmentUpdate(BaseModel):
    student_id: Optional[int] = None
    course_id: Optional[int] = None



class DepartmentResponse(BaseModel):
    department_id: int
    courses: list[CourseResponse]

#for DRF [in GET /api/v1/courses]
class PaginatedCourseResponse(BaseModel):
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: List[CourseResponse]