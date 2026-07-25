# Hands-On 3: Test Automation Process, Lifecycle & Framework Types

## Task 1: Automation Decision and Test Case Selection

## 17. Criteria for Deciding Whether a Test Case Should Be Automated

Before automating any test case, it is important to evaluate whether automation will provide long-term value.

Not every test is suitable for automation. The following are important criteria used to decide whether a test case should be automated.

---

## 1. Repetitive Execution

Tests that are executed frequently should be automated because automation reduces manual effort and saves time.

### Application to the Given Scenario

The **POST `/api/courses/`** endpoint is tested after every code update.

Since this test is performed repeatedly, automating it ensures:

- Faster execution
- Consistent results
- Reduced manual effort

---

## 2. Regression Testing

Regression testing verifies that existing features continue to work after new changes are introduced.

These tests are executed regularly, making them ideal candidates for automation.

### Application to the Given Scenario

Every time the Course Management API is modified, the system should still return:

**HTTP Status Code 201 (Created)**

when valid course details are submitted.

Automation ensures that existing functionality is not affected by future changes.

---

## 3. Stable Functionality

Automation is most effective for features that rarely change.

Stable features require less maintenance and make automation scripts more reliable.

### Application to the Given Scenario

Creating a course is one of the core functionalities of the Course Management System.

Since this feature is expected to remain stable over time, it is a strong candidate for automation.

---

## 4. Business-Critical Functionality

Features that directly impact business operations should always be tested thoroughly.

Automating these features helps identify issues quickly before they affect users.

### Application to the Given Scenario

If the API fails to create a course successfully, administrators cannot add new courses.

Since course creation is a critical feature, it should be automated.

---

## 5. Data-Driven Testing

When the same test must be executed with multiple sets of input data, automation becomes much more efficient than manual testing.

### Application to the Given Scenario

The API can be tested with different combinations of:

- Course names
- Course codes
- Course descriptions

using external data files such as:

- Excel
- CSV
- JSON

---

# 18. Automate or Manual – Decision with Justification

| Test Case | Decision | Justification |
|-----------|----------|---------------|
| Regression testing for all CRUD endpoints after every code change | Automate | Regression tests are repetitive and need to be executed after every build. Automation saves significant time. |
| Exploratory testing of a new search feature | Manual | Exploratory testing requires human observation, creativity, and decision-making which cannot be effectively automated. |
| Performance testing with 100 concurrent users calling GET `/api/courses/` | Automate | Performance testing requires automation tools to simulate multiple users simultaneously. |
| UI testing of the login form | Automate | Login is a stable and frequently tested feature. Selenium automation improves speed and consistency. |
| Verify Swagger API documentation | Manual | Documentation should be reviewed manually to ensure content accuracy and readability. |
| Smoke testing after deployment | Automate | Smoke tests should run automatically after every deployment to quickly verify that the application is working correctly. |

---

# 19. Test Automation ROI

## Definition

**Test Automation ROI (Return on Investment)** measures whether the time and effort spent creating and maintaining automation scripts provide greater benefits compared to performing the same tests manually.

---

## Given Information

- Time required to automate one regression test = **4 hours**
- Time required to execute the test manually = **30 minutes (0.5 hour)**

---

## Break-even Calculation

Automation Development Time:

**4 hours**

Manual Execution Time per Run:

**0.5 hour**

Break-even calculation:

**Break-even Point = 4 ÷ 0.5 = 8 runs**

Therefore, automation becomes beneficial after the **8th execution**.

---

## Maintenance Overhead

After the **10th execution**, each automated run requires **20% maintenance effort**.

Manual execution time:

**0.5 hour**

Maintenance effort:

**20% × 0.5 = 0.1 hour**

After the 10th run:

- Manual execution takes **0.5 hour**
- Automated execution requires only **0.1 hour** for maintenance

Automation continues to save approximately **0.4 hour per execution**, making it more efficient in the long run.

---

## Conclusion

Although automation requires a higher initial investment, it becomes more cost-effective after repeated executions.

It improves:

- Execution speed
- Testing efficiency
- Consistency of results
- Regression coverage

---

# 20. Flaky Test

## Definition

A **flaky test** is a test that produces inconsistent results.

It may pass during one execution and fail during another even though there are no changes in the application.

Flaky tests reduce confidence in the automation suite because failures may not always represent actual application defects.

---

## Example

Suppose a Selenium script clicks the **Login** button immediately after opening a webpage.

- If the page loads quickly, the test passes.
- If the page loads slowly, Selenium cannot find the button and the test fails.

The application is working correctly, but the automation script behaves inconsistently.

This is called a flaky test.

---

# Strategies to Prevent or Fix Flaky Tests

## 1. Use Explicit Waits

Replace `time.sleep()` with **WebDriverWait**.

Selenium should wait until an element becomes:

- Visible
- Clickable
- Available

This improves test stability.

---

## 2. Use Stable Locators

Prefer locating elements using:

- ID
- CSS Selectors

Avoid absolute XPath expressions because small page structure changes can break the test.

---

## 3. Make Tests Independent

Each test should:

- Create its own data
- Avoid depending on previous tests
- Clean up after execution

Independent tests avoid failures caused by shared data or execution order.

---

# Summary

## Suitable Candidates for Automation

- Regression Testing
- Smoke Testing
- Stable Features
- Data-Driven Testing
- Performance Testing

---

## Better Performed Manually

- Exploratory Testing
- One-Time Testing
- Frequently Changing Features
- Documentation Verification

---

# Conclusion

Automation should be applied to repetitive, stable, and business-critical test cases where it provides long-term benefits.

Manual testing remains important for exploratory activities and areas requiring human judgment.

Selecting the right test cases for automation helps improve:

- Software quality
- Testing efficiency
- Release confidence
- Overall project productivity