import "../App.css";

function CourseCard({ course, onEnroll }) {

    const handleEnroll = () => {
        onEnroll(course);
    };

    const { name, code, credits, grade } = course;

    return (

        <div className="course-card">

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