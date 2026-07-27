import { useParams } from "react-router-dom";
import Header from "../components/Header";
import Footer from "../components/Footer";
import courses from "../data/couses";

function CourseDetailPage() {

  const { courseId } = useParams();

  const course = courses.find(
    (course) => course.id === Number(courseId)
  );

  return (
    <>
      <Header
        siteName="Student Portal"
        count={0}
      />

      {course ? (
        <div className="course-card">
          <h2>Course Details</h2>

          <h3>Name: {course.name}</h3>
          <h3>Code: {course.code}</h3>
          <h3>Credits: {course.credits}</h3>
        </div>
      ) : (
        <h2>Course not found</h2>
      )}

      <Footer />
    </>
  );
}

export default CourseDetailPage;