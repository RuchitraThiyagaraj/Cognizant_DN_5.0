import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { getAllCourses } from "../api/courseApi";

// Async thunk for fetching courses
export const fetchAllCourses = createAsyncThunk(
  "courses/fetchAll",
  async () => {
    const data = await getAllCourses();
    return data;
  }
);


const courseSlice = createSlice({
  name: "courses",

  initialState: {
    courses: [],
    loading: false,
    error: null,
  },

  reducers: {},

  extraReducers: (builder) => {
    builder

      // API request started
      .addCase(fetchAllCourses.pending, (state) => {
        state.loading = true;
        state.error = null;
      })

      // API success
      .addCase(fetchAllCourses.fulfilled, (state, action) => {
        state.loading = false;
        state.courses = action.payload;
      })

      // API failed
      .addCase(fetchAllCourses.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message;
      });
  },
});


// Selectors
export const selectCourses = (state) => state.courses.courses;

export const selectCoursesLoading = (state) => state.courses.loading;

export const selectCoursesError = (state) => state.courses.error;


export default courseSlice.reducer;