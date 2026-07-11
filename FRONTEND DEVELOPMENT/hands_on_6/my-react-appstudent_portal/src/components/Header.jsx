import { Link } from "react-router-dom";
import "../App.css";
import { useContext } from "react";
import { EnrollmentContext } from "../context/EnrollmentContext";

function Header({ siteName }) {

  const { enrolledCourses } = useContext(EnrollmentContext);

  return (
    <div>
      <h1>{siteName}</h1>

      <nav>
        <Link to="/">Home</Link>
        <Link to="/courses">Courses</Link>
        <Link to="/profile">Profile</Link>
      </nav>

      <h3 className="course-count">
        Number of courses enrolled : {enrolledCourses.length}
      </h3>
    </div>
  );
}

export default Header;