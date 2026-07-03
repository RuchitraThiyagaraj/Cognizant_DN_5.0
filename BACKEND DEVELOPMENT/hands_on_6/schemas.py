from pydantic import BaseModel, ConfigDict
from typing import Optional

#this file tells how the input and output should look like suing pydantic classes
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


class CourseResponse(BaseModel):
    id: int
    name: str
    code: str
    credits: int
    department_id: int

    model_config = ConfigDict(from_attributes=True)


class DepartmentResponse(BaseModel):
    department_id: int
    courses: list[CourseResponse]