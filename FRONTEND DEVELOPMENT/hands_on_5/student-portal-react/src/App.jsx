import { useState, useEffect } from "react";
import Header from "./components/Header";
import Footer from "./components/Footer";
import CourseCard from "./components/CourseCard";
import courses from "./data/courses";
import StudentProfile from "./components/StudentProfile";

function App() {

  //CONSTANTS
  const siteName = "Student Portal";

  //STATES
  const [courseList, setCourseList] = useState([]);

  const [searchTerm, setSearchTerm] = useState("");

  //loading state
  const [loading, setLoading] = useState(true);

  //error state
  const [errorMessage, setErrorMessage] = useState("");

  //enroll state
  const [enrolledCourses, setEnrolledCourses] = useState([]);
  useEffect(() => {
    console.log("Courses updated");
  }, [courseList]);


  //FETCH COURSES
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


      } 

      catch(error) {

        console.log(error);

        setErrorMessage("Error loading course data");

      }

      finally {

        setLoading(false);

      }

    };


    fetchCourses();

  }, []);



  //search
  const handleSearch = (e) => {
    setSearchTerm(e.target.value);
  };



  //enrollment
  const handleEnroll = (selectedCourse) => {

    const alreadyEnrolled = enrolledCourses.some(
      (course) => course.code === selectedCourse.code
    );


    if(alreadyEnrolled){

      alert("You have already enrolled in this course");

    }

    else{

      setEnrolledCourses([
        ...enrolledCourses,
        selectedCourse
      ]);

    }

  };



  return (

    <>

      <Header
        siteName={siteName}
        count={enrolledCourses.length}
      />


      <input
        type="text"
        placeholder="Search"
        value={searchTerm}
        onChange={handleSearch}
      />
      <StudentProfile />


      {loading && (
        <p>Loading course data...</p>
      )}


      {errorMessage && (
        <p>{errorMessage}</p>
      )}



      {!loading && !errorMessage && (

        <div className="course-grid">

          {courseList
            .filter((course)=>
              course.name
              .toLowerCase()
              .includes(searchTerm.toLowerCase())
            )

            .map((course)=>(

              <CourseCard
                key={course.id}
                course={course}
                onEnroll={handleEnroll}
              />

            ))

          }

        </div>

      )}



      <Footer />

    </>

  );

}

export default App;