import Header from "../components/Header";
import Footer from "../components/Footer";

function HomePage() {
  return (
    <>
      <Header
        siteName="Student Portal"
        count={0}
      />

      <div>
        <h2>Welcome to Student Portal</h2>
        <p>Browse and enroll in courses.</p>
      </div>

      <Footer />
    </>
  );
}

export default HomePage;