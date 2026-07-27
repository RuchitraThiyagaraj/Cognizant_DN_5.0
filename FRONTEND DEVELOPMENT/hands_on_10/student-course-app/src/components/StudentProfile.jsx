import { useState } from "react";

function StudentProfile() {

    //local state of this component
    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    const [semester, setSemester] = useState("");


    return (
        <div>

            <h2>Student Profile</h2>

            <form>

                <input
                    type="text"
                    placeholder="Enter name"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                />


                <input
                    type="email"
                    placeholder="Enter email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />


                <input
                    type="text"
                    placeholder="Enter semester"
                    value={semester}
                    onChange={(e) => setSemester(e.target.value)}
                />

            </form>


            <h3>Name: {name}</h3>
            <h3>Email: {email}</h3>
            <h3>Semester: {semester}</h3>

        </div>
    );
}

export default StudentProfile;