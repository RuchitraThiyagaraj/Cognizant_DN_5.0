# Hands-On 3: Test Automation Process, Lifecycle & Framework Types

## Task 2: Compare Automation Framework Types

## 21. Comparison of Automation Framework Types

Automation frameworks provide a structured approach to designing, developing, and maintaining automated test scripts. Different frameworks are used based on project size, complexity, and testing requirements.

---

# 1. Linear Framework

## Description

The Linear Framework is the simplest automation framework where all test steps are written in a single script from beginning to end.

There is no separation between test data, reusable functions, and automation logic. It is mainly suitable for small projects and beginners learning Selenium automation.

## Advantages

- Easy to understand and implement.
- Requires less framework setup.

## Disadvantages

- High code duplication.
- Difficult to maintain when the project grows.
- Changes in one functionality may require updates in multiple scripts.

## Example

For a Course Management System, the Linear Framework can automate the "Create Course" functionality where browser opening, login, course creation, validation, and browser closing are written in one script.

---

# 2. Modular Framework

## Description

The Modular Framework divides the application into different independent modules such as Login, Courses, Students, and Faculty.

Each module contains reusable functions that can be called by multiple test cases, reducing duplicate code.

## Advantages

- Improves code reusability.
- Easier maintenance.
- Better organization of test scripts.

## Disadvantages

- Requires proper planning during framework design.
- Initial development takes more time.

## Example

In the Course Management System, the Login module can be created once and reused across multiple test cases instead of rewriting login steps repeatedly.

---

# 3. Data-Driven Framework

## Description

The Data-Driven Framework separates test data from test scripts.

Test data is stored externally in files such as:

- Excel
- CSV
- JSON

The same automation script can execute multiple times with different input values.

## Advantages

- Supports testing with multiple datasets.
- Reduces duplicate test scripts.
- Easy to update test data.

## Disadvantages

- Managing external data files increases complexity.
- Requires additional data handling utilities.

## Example

The login functionality of the Course Management System can be tested using multiple username and password combinations stored in an Excel file.

---

# 4. Keyword-Driven Framework

## Description

The Keyword-Driven Framework allows testers to create test cases using predefined keywords instead of writing programming code.

Examples of keywords:

- OpenBrowser
- Click
- EnterText
- Verify

The automation engine reads these keywords and performs the required actions.

## Advantages

- Allows non-technical users to create test cases.
- Reduces programming dependency.

## Disadvantages

- Framework development is complex.
- Requires maintenance of keyword libraries.

## Example

A manual tester can create login test cases using keywords without directly writing Selenium Python code.

---

# 5. Hybrid Framework

## Description

The Hybrid Framework combines multiple framework approaches such as:

- Modular Framework
- Data-Driven Framework
- Keyword-Driven Framework

It is commonly used in real-world Selenium automation projects because it provides scalability, flexibility, and better maintenance.

## Advantages

- Highly reusable.
- Suitable for enterprise-level projects.
- Supports multiple test data sources.
- Easier long-term maintenance.

## Disadvantages

- Initial setup requires more time.
- Requires experienced automation engineers.

## Example

The Course Management System can use:

- Page Object Model classes for reusable pages.
- Excel files for test data.
- Keyword files for business-level test execution.

---

# Framework Comparison Table

| Framework | Best Used For | Main Advantage | Main Disadvantage |
|------------|---------------|----------------|-------------------|
| Linear | Small projects | Easy implementation | Poor maintenance |
| Modular | Medium projects | Code reusability | Requires planning |
| Data-Driven | Multiple input combinations | Supports multiple datasets | Data management complexity |
| Keyword-Driven | Non-technical testers | Less coding required | Complex framework design |
| Hybrid | Enterprise projects | Flexible and scalable | Longer initial setup |

---

# 22. Recommended Framework for the Given Scenario

## Scenario

The Selenium automation team needs to:

- Test login functionality using 50 different username and password combinations.
- Reuse login functionality across 20 different test cases.
- Allow both technical and non-technical team members to contribute.

---

## Recommendation

The recommended framework is a:

**Hybrid Framework**

It combines:

- Modular Framework
- Data-Driven Framework
- Keyword-Driven Framework

---

## Justification

### Modular Framework

- Creates reusable components like Login, Course Management, and Student modules.
- Avoids duplicate automation code.

### Data-Driven Framework

- Stores multiple username and password combinations externally.
- Allows execution of the same test with different datasets.

### Keyword-Driven Framework

- Allows non-technical users to create and modify test scenarios using keywords.
- Reduces dependency on programming knowledge.

---

## Final Conclusion

A Hybrid Framework is the best choice because it provides:

- Code reusability.
- Multiple test data support.
- Better maintainability.
- Collaboration between technical and non-technical team members.

It is widely used in enterprise Selenium automation projects.

---

# 23. Hybrid Framework Folder Structure

```text
CourseManagementAutomation/
│
├── config/
│   ├── config.py
│   └── settings.json
│
├── test_data/
│   ├── login_data.csv
│   ├── course_data.csv
│   └── users.xlsx
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── course_page.py
│   ├── student_page.py
│   └── faculty_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_create_course.py
│   ├── test_update_course.py
│   ├── test_delete_course.py
│   └── test_student.py
│
├── utilities/
│   ├── driver_factory.py
│   ├── excel_reader.py
│   ├── logger.py
│   ├── screenshot.py
│   └── wait_utils.py
│
├── reports/
│
├── screenshots/
│
├── requirements.txt
├── conftest.py
└── README.md