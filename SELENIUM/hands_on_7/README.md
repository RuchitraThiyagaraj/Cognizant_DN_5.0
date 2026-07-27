## Why Page Object Model?


Without POM:

- Locators are repeated in every test.
- If UI changes, we need to modify many test files.
- Test files become difficult to maintain.


Example:

driver.find_element(By.ID,"username")


With POM:

- Locators are stored in page classes.
- Tests only call methods.
- UI changes require updating only one file.


Golden Rule:

Page classes -> Actions and locators

Test classes -> Assertions