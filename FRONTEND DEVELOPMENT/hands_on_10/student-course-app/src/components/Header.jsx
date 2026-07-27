import { useContext } from "react";
import { Link } from "react-router-dom";

import { EnrollmentContext } from "../context/EnrollmentContext";

function Header() {

  const { enrolledCourses } = useContext(EnrollmentContext);


  return (
    <header>

      <h1>Student Course App</h1>

      <nav>
        <Link to="/">Home</Link>

        {" | "}

        <Link to="/courses">
          Courses
        </Link>

        {" | "}

        <Link to="/profile">
          Profile
        </Link>

        {" | "}

        <span>
          Enrolled: {enrolledCourses.length}
        </span>

      </nav>

    </header>
  );
}

export default Header;