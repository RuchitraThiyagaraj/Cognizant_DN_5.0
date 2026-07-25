# Hands-On 2: SDLC vs TDLC — V-Model & Agile QA Integration

**Author:** Ruchitra T

---

# Task 1: V-Model Mapping

## 1. V-Model Diagram

The V-Model represents the relationship between software development phases (SDLC) and testing phases (TDLC). Each development activity has a corresponding testing activity.

```text
        SDLC (Verification)              TDLC (Validation)
        --------------------             -------------------

   Requirements Analysis  -------------> Acceptance Testing
            |                                  ▲
            |                                  |
            ▼                                  |
       System Design  -----------------> System Testing
            |                                  ▲
            |                                  |
            ▼                                  |
   Architecture Design  -------------> Integration Testing
            |                                  ▲
            |                                  |
            ▼                                  |
      Module Design  ----------------> Unit Testing
            |                                  ▲
            |                                  |
            ▼                                  |
             Coding --------------------------|
```

---

# 2. SDLC and TDLC Phase Mapping

| SDLC Phase | Corresponding Testing Phase | Test Artifacts |
|------------|----------------------------|----------------|
| Requirements Analysis | Acceptance Testing | Acceptance Test Plan and user acceptance scenarios are prepared based on business requirements. |
| System Design | System Testing | System Test Plan and complete end-to-end test cases are created using system specifications. |
| Architecture Design | Integration Testing | Integration Test Plan and API/interface validation scripts are prepared based on component interactions. |
| Module Design | Unit Testing | Unit test scenarios and logic validation cases are prepared based on module-level design. |

---

# 3. Entry and Exit Criteria for Testing Levels

| Testing Level | Entry Criteria | Exit Criteria |
|---------------|----------------|---------------|
| Unit Testing | Code compilation is successful.<br>Code review is completed.<br>Unit test cases are prepared. | All planned unit tests pass.<br>Required code coverage is achieved.<br>No critical defects remain. |
| Integration Testing | Unit testing is completed.<br>Modules are deployed to integration environment.<br>Database connections are verified. | Integration tests execute successfully.<br>Components communicate correctly.<br>No critical integration defects remain. |
| System Testing | Integration testing is completed.<br>Stable build is deployed in QA environment.<br>Test data is prepared. | All system test cases are executed.<br>Expected pass percentage is achieved.<br>No critical or high severity defects remain. |
| Acceptance Testing | System testing sign-off is completed.<br>UAT environment is ready.<br>Business test data is available. | Business users approve the system.<br>Requirements are satisfied.<br>User documentation is validated. |

---

# 4. QA Engagement Points in Course Management API Project

## Point 1: Requirement Review

QA participates during the requirement analysis phase.

QA verifies unclear requirements such as:

- Should course code contain numbers only?
- Should course code support alphabets?
- Is course duration mandatory?

Finding issues early prevents development problems later.

---

## Point 2: API Schema Review

QA reviews Swagger/OpenAPI documentation during architecture design.

QA validates:

- API request structure
- Response format
- Validation rules
- Error handling

Example:

Missing required fields should return:

```
400 Bad Request
```

---

# Task 2: Agile QA and Shift-Left Testing

---

# 5. Problems with Traditional Waterfall Testing

## 1. Late Defect Discovery

Testing happens after development completion.

Major defects found late can require large code changes.

---

## 2. Limited Testing Time

Development delays reduce QA time.

This can result in:

- Reduced test coverage
- Missing edge cases
- Increased production issues

---

## 3. High Fixing Cost

Requirement or design mistakes become expensive to fix when discovered during later stages.

---

# 6. QA Role in Agile Ceremonies

| Agile Ceremony | QA Responsibility |
|----------------|------------------|
| Sprint Planning | QA defines acceptance criteria and ensures user stories are testable. |
| Daily Standup | QA shares testing progress, blockers, and environment issues. |
| Sprint Review | QA verifies completed features and provides quality feedback. |
| Sprint Retrospective | QA analyzes escaped defects and suggests improvements. |

---

# 7. Shift-Left Testing Practices for Course Management API

## 1. Requirement Review for Testability

QA identifies unclear requirements before development starts.

Example:

Instead of:

```
API should be fast
```

Define:

```
API response time should be below 200ms
```

---

## 2. Writing Test Cases Before Code

QA prepares test scenarios before development.

Approaches:

- TDD (Test Driven Development)
- BDD (Behavior Driven Development)

Benefits:

- Clear expectations
- Better code quality
- Faster defect detection

---

## 3. Static Code Analysis

Code quality tools are used before integration testing.

Examples:

- Flake8
- SonarQube

Checks:

- Coding errors
- Security issues
- Code quality problems

---

## 4. API Contract Testing

QA verifies APIs according to Swagger/OpenAPI specifications.

Validates:

- Request format
- Response structure
- Status codes
- Validation rules

---

# 8. Acceptance Criteria Using Given-When-Then (Gherkin)

```gherkin
Feature: Course Creation Management

  Scenario: Create a new course successfully

    Given the college admin is authenticated
    When the admin sends a POST request to "/api/courses/" with valid course details
    Then the API should return status code 201
    And the response should contain a unique course ID
    And the course should be saved successfully


  Scenario: Prevent duplicate course creation

    Given the college admin is authenticated
    And a course with code "CS-102" already exists
    When the admin creates another course with the same course code
    Then the API should return status code 400
    And the error message should be "Course code already exists"


  Scenario: Prevent course creation when required fields are missing

    Given the college admin is authenticated
    When the admin sends a request without a course name
    Then the API should return status code 400
    And the error message should be "Course name field is required"
```

---

# Quick Summary

## V-Model

- Development and testing phases are connected.
- Testing activities are planned early.
- Each development phase has a corresponding validation phase.

## Agile QA

- QA is involved throughout the development process.
- Shift-left testing helps detect defects early.
- Continuous testing improves software quality.

---

**Prepared by: Ruchitra T**