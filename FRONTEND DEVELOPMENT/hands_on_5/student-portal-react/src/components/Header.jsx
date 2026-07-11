import "../App.css";

function Header({ siteName, count }) {

    return (

        <div>

            <h1>{siteName}</h1>

            <nav>
                <a href="#">Home</a>
                <a href="#">Courses</a>
                <a href="#">Profile</a>
            </nav>

            <h3 className="course-count">
                Number of courses enrolled : {count}
            </h3>

        </div>

    );

}

export default Header;