# Handson 01: QA Concepts and Defect Management

**Author:** Ruchitra T

---

## 1. Testing Levels

Software testing is divided into different levels based on the scope and purpose of testing.

### 1.1 Unit Testing

**Focus:** Smallest independent part of the application.

**Purpose:**  
To verify that individual functions, methods, or components work correctly.

**Example:**

Testing a validation function:

```python
validate_course_duration(duration)
```

Test cases:

- Negative value: `-5`
- Large value: `500`
- Valid value: `10`

---

### 1.2 Integration Testing

**Focus:** Interaction between different modules or components.

**Purpose:**  
To verify that multiple parts of the system work together correctly.

**Example:**

Checking whether:

- Repository layer
- Service layer
- Database layer

work together correctly while saving course data.

---

### 1.3 System Testing

**Focus:** Complete application workflow.

**Purpose:**  
To validate the complete system from user input to final output.

**Example:**

Sending a request:

```
POST /api/courses/
```

and verifying:

- Course is created successfully
- Correct status code is returned
- Data is stored in the database

---

### 1.4 User Acceptance Testing (UAT)

**Focus:** Real user and business requirements.

**Purpose:**  
To confirm that the application satisfies business expectations.

**Example:**

An administrator creates a course through the UI and verifies that students can view the course successfully.

---

# 2. Functional vs Non-Functional Testing

## Functional Testing

Functional testing verifies whether the application performs the required functionality.

### Examples:

- User login
- Course creation
- Form validation
- API response validation
- Data processing

---

## Non-Functional Testing

Non-functional testing verifies the quality and performance of the application.

### Examples:

- Performance
- Security
- Reliability
- Scalability
- Usability

### Example:

Performance test:

```
Send 1000 requests to GET /api/courses/
within 2 seconds.
```

Verify:

- Response time is acceptable
- System remains stable
- No failures occur

---

# 3. Black-Box vs White-Box Testing

| Testing Type | Description | Performed By |
|--------------|-------------|--------------|
| Black-Box Testing | Testing application behaviour using inputs and outputs without checking internal code | QA Engineers |
| White-Box Testing | Testing internal code logic, structure, and implementation | Developers |

## Difference

**Black-Box Testing:**

"Does the application work correctly?"

**White-Box Testing:**

"Why does the application work or fail?"

---

# 4. Sample Test Cases for POST /api/courses/

| Test Case ID | Scenario | Preconditions | Expected Result |
|--------------|----------|---------------|----------------|
| TC_API_001 | Create course with valid data | Admin user logged in with valid token | API returns `201 Created` and course is created |
| TC_API_002 | Create course without name | Admin user logged in with valid token | API returns `400 Bad Request` with validation message |
| TC_API_003 | Create course with negative duration | Admin user logged in with valid token | API rejects request with duration validation error |

---

# 5. Defect Lifecycle

A defect generally follows these stages:

```
New → Assigned → Open → Fixed → Retest → Verified → Closed
```

## Defect Status Explanation

| Status | Description |
|--------|-------------|
| New | Defect is identified and reported |
| Assigned | Defect is assigned to the responsible developer |
| Open | Developer starts investigating the issue |
| Fixed | Developer completes the fix |
| Retest | QA verifies the fix |
| Verified | QA confirms that the issue is resolved |
| Closed | Defect is completed and removed from tracking |

## Other Possible Outcomes

- **Rejected:** Defect is not considered valid
- **Deferred:** Defect is valid but postponed for a future release

---

# 6. Bug Classification Examples

## Example 1

**Defect:**  
POST `/api/courses/` returns `500 Internal Server Error` for all requests.

**Severity:** Critical  
**Priority:** P1  

**Reason:**  
The main functionality is completely unavailable.

---

## Example 2

**Defect:**  
Course names longer than 150 characters are automatically truncated.

**Severity:** Medium  
**Priority:** P2  

**Reason:**  
The application works, but data accuracy is affected.

---

## Example 3

**Defect:**  
Swagger documentation contains spelling mistakes.

**Severity:** Low  
**Priority:** P4  

**Reason:**  
It is a cosmetic issue and does not affect functionality.

---

## Example 4

**Defect:**  
Login occasionally returns `401 Unauthorized` during the first attempt.

**Severity:** High  
**Priority:** P1  

**Reason:**  
Authentication problems affect user experience.

---

# 7. Sample Defect Report

## Defect Details

| Field | Details |
|------|---------|
| Defect ID | BUG-DN5-001 |
| Reported By | Ruchitra T |
| Title | API returns 500 error while creating a course |
| Environment | QA-Staging-Cluster 02 |
| Build Version | Release v5.0-alpha-3 |
| Severity | Critical |
| Priority | P1 |

---

## Steps to Reproduce

1. Login to QA environment using a valid admin account.
2. Open Postman.
3. Send a POST request:

```
POST /api/courses/
```

4. Use the payload:

```json
{
    "name": "QA Basics Class",
    "duration": 12
}
```

5. Click Send.

---

## Expected Result

- API should return `201 Created`.
- Course should be saved successfully.
- Created course details should be returned.

---

## Actual Result

API returns:

```
500 Internal Server Error
```

---

## Attachment

- Error response screenshot
- Server logs
- API request details

---

# 8. Severity vs Priority

## Severity

Severity defines the technical impact of the defect.

**Focus:**

- System damage
- Functional impact

---

## Priority

Priority defines how quickly the defect should be fixed.

**Focus:**

- Business importance
- Release urgency

---

## Example

A defect can have:

- High severity
- Low priority

when it affects an old feature that is rarely used.

---

# Quick Summary

Quality Assurance (QA) ensures that software is:

- Correct
- Reliable
- Secure
- User-friendly

Effective testing helps:

- Find defects early
- Improve software quality
- Reduce production issues
- Increase user confidence

---

**Prepared by: Ruchitra T**