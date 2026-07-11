import Header from "../components/Header";
import Footer from "../components/Footer";
import StudentProfile from "../components/StudentProfile";

function ProfilePage() {
  return (
    <>
      <Header
        siteName="Student Portal"
        count={0}
      />

      <StudentProfile />

      <Footer />
    </>
  );
}

export default ProfilePage;