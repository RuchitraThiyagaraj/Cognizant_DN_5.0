import apiClient from "./apiClient";

// Get all courses
export const getAllCourses = async () => {
  return await apiClient.get("/posts");
};

// Get course by id
export const getCourseById = async (id) => {
  return await apiClient.get(`/posts/${id}`);
};

// Enroll student into course
export const enrollStudent = async (studentId, courseId) => {
  return await apiClient.post("/posts", {
    studentId,
    courseId,
  });
};