import { useState, useEffect, useContext } from "react";
import Header from "../components/Header";
import Footer from "../components/Footer";
import CourseCard from "../components/CourseCard";
import courses from "../data/couses";
import { EnrollmentContext } from "../context/EnrollmentContext";

function CoursesPage() {

  const siteName = "Student Portal";

  const [courseList, setCourseList] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");
  const [loading, setLoading] = useState(true);
  const [errorMessage, setErrorMessage] = useState("");

  const { enrolledCourses, setEnrolledCourses } =
    useContext(EnrollmentContext);


  useEffect(() => {

    const fetchCourses = async () => {

      try {

        setLoading(true);

        const response = await fetch(
          "https://jsonplaceholder.typicode.com/posts"
        );

        if (!response.ok) {
          throw new Error("Failed to fetch courses");
        }

        const data = await response.json();

        const mergedCourses = courses.map((course, index) => ({
          ...data[index],
          id: course.id,
          name: course.name,
          credits: course.credits,
          code: course.code,
          grade: course.grade,
        }));

        setCourseList(mergedCourses);

      } catch (error) {

        console.log(error);
        setErrorMessage("Error loading course data");

      } finally {

        setLoading(false);

      }

    };

    fetchCourses();

  }, []);


  const handleSearch = (e) => {
    setSearchTerm(e.target.value);
  };


  const handleEnroll = (selectedCourse) => {

    const alreadyEnrolled = enrolledCourses.some(
      (course) => course.code === selectedCourse.code
    );

    if (alreadyEnrolled) {

      alert("You have already enrolled in this course");

    } else {

      setEnrolledCourses([
        ...enrolledCourses,
        selectedCourse,
      ]);

    }

  };


  return (
    <>

      <Header siteName={siteName} />


      <input
        type="text"
        placeholder="Search"
        value={searchTerm}
        onChange={handleSearch}
      />


      {loading && <p>Loading course data...</p>}


      {errorMessage && <p>{errorMessage}</p>}


      {!loading && !errorMessage && (

        <div className="course-grid">

          {courseList
            .filter((course) =>
              course.name
                .toLowerCase()
                .includes(searchTerm.toLowerCase())
            )
            .map((course) => (

              <CourseCard
                key={course.id}
                course={course}
                onEnroll={handleEnroll}
              />

            ))}

        </div>

      )}


      <Footer />

    </>
  );
}

export default CoursesPage;