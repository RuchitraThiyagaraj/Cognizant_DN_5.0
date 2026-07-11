import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import EnrollmentProvider from "./context/EnrollmentContext.jsx";
import "./index.css";
import App from "./App.jsx";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <BrowserRouter>
    <EnrollmentProvider>
      <App />
      </EnrollmentProvider>    
    </BrowserRouter>
  </StrictMode>
);