
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String,ForeignKey ,Boolean

Base=declarative_base()

#without usin relationship()

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    code = Column(String(20), nullable=False)
    credits = Column(Integer)
    department_id = Column(Integer)

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True )
    name = Column(String(20), nullable=False)
    email = Column(String(20), unique=True, nullable=False)
    age = Column(Integer)
    department_id = Column(Integer)

#Student  -> Enrollment <-  Course since student and course is many to many we have to use another table 

class Enrollment(Base):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True, index=True , autoincrement=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)

class User(Base):
    __tablename__="Users"
    id=Column(Integer , primary_key=True , index=True , autoincrement=True)
    email=Column(String(20) , nullable=False)
    hashed_password=Column(String)
    is_active=Column(Boolean)
'''
auto_increment=true isnt compulsory because 
because SQLAlchemy automatically makes an Integer primary key auto-increment in most databases 
(including SQLite and MySQL).
'''