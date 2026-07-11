import "../App.css";
import { useNavigate } from "react-router-dom";

function CourseCard({ course, onEnroll }) {

  const navigate = useNavigate();

  const handleEnroll = (e) => {

    e.stopPropagation();

    onEnroll(course);

    //navigate("/profile");

  };

  const handleViewDetails = () => {

    navigate(`/courses/${course.id}`);

  };

  const { name, code, credits, grade } = course;

  return (

    <div
      className="course-card"
      onClick={handleViewDetails}
    >

      <h2>{name}</h2>
      <h2>{code}</h2>
      <h2>{credits}</h2>
      <h2>{grade}</h2>

      <button
        className="enroll-button"
        onClick={handleEnroll}
      >
        Enroll
      </button>

    </div>

  );

}

export default CourseCard;