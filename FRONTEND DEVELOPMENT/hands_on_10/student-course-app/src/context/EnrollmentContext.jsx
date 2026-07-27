import { createContext, useState } from "react";

export const EnrollmentContext = createContext();

function EnrollmentProvider({ children }) {
  const [enrolledCourses, setEnrolledCourses] = useState([]);

  return (
    <EnrollmentContext.Provider
      value={{ enrolledCourses, setEnrolledCourses }}
    >
      {children}
    </EnrollmentContext.Provider>
  );
}
export default EnrollmentProvider;
