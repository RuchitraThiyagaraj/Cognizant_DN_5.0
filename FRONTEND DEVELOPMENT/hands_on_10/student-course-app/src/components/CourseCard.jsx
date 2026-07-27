import { useContext } from "react";
import { EnrollmentContext } from "../context/EnrollmentContext";

function CourseCard({ course }) {
  const { enrolledCourses, setEnrolledCourses } =
    useContext(EnrollmentContext);


  const handleEnroll = () => {
    setEnrolledCourses([
      ...enrolledCourses,
      course,
    ]);
  };


  return (
    <div className="course-card">

      <h2>
        {course.title}
      </h2>

      <p>
        {course.body}
      </p>


      <button onClick={handleEnroll}>
        Enroll
      </button>

    </div>
  );
}

export default CourseCard;