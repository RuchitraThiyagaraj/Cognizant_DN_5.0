import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";

import {
  fetchAllCourses,
  selectCourses,
  selectCoursesLoading,
  selectCoursesError,
} from "../redux/courseSlice";

import CourseCard from "../components/CourseCard";

function CoursesPage() {
  const dispatch = useDispatch();

  const courses = useSelector(selectCourses);
  const loading = useSelector(selectCoursesLoading);
  const error = useSelector(selectCoursesError);

  useEffect(() => {
    dispatch(fetchAllCourses());
  }, [dispatch]);


  if (loading) {
    return <h2>Loading courses...</h2>;
  }


  if (error) {
    return <h2>Error: {error}</h2>;
  }


  return (
    <div>
      <h1>Courses</h1>

      <div>
        {courses.map((course) => (
          <CourseCard
            key={course.id}
            course={course}
          />
        ))}
      </div>

    </div>
  );
}

export default CoursesPage;