# Return back to the [README.md](README.md) file.

## Manual Testing

- All core functionality of the Pass-It application was manually tested to ensure the system behaves as expected across different user interactions. The table below outlines the test cases performed, expected outcomes, and results.

## Manual Test Cases

| Page       | User Action                                | Expected Result                                 | Pass/Fail | 
| ---------- | ------------------------------------------ | ----------------------------------------------- | --------- | 
| **Navbar** |                                            |                                                 |           | 
|            | Click on Logo                              | Redirects user to the handover list (home page) | Pass      |
|            | Click on Handovers link                    | Redirects to handover list page                 | Pass      |
|            | Click on New Handover (authenticated user) | Redirects to create handover form               | Pass      |
|            | Click on Login link (unauthenticated user) | Redirects to login page                         | Pass      |
|            | Click on Register link                     | Redirects to registration page                  | Pass      |
|            | Click on Profile link                      | Redirects to user profile page                  | Pass      |
|            | Click on Logout link                       | Logs user out and redirects to login page       | Pass      |

## Login Page

| Page       | User Action                       | Expected Result                                       | Pass/Fail |
| ---------- | --------------------------------- | ----------------------------------------------------- | --------- |
| Login Page | Enter valid username and password | User is authenticated and redirected to handover list | Pass      |
| Login Page | Enter invalid credentials         | Error message is displayed                            | Pass      |
| Login Page | Click register link               | Redirects to registration page                        | Pass      |

## Register PAge

| Page          | User Action                      | Expected Result                          | Pass/Fail |
| ------------- | -------------------------------- | ---------------------------------------- | --------- |
| Register Page | Enter valid registration details | Account is created and user is logged in | Pass      |
| Register Page | Submit empty form                | Validation errors are displayed          | Pass      |
| Register Page | Enter mismatched passwords       | Error message is displayed               | Pass      |

## Handover List Page

| Page          | User Action                  | Expected Result                            | Pass/Fail |
| ------------- | ---------------------------- | ------------------------------------------ | --------- |
| Handover List | View handover list           | All handovers are displayed in card format | Pass      |
| Handover List | Click on a handover title    | Redirects to handover detail page          | Pass      |
| Handover List | Click on New handover button | Redirects to create handover page          | Pass      |
| Handover List | View list while logged out   | Redirects user to login page               | Pass      |

## Create Handover Page

| Page            | User Action                  | Expected Result                                | Pass/Fail |
| --------------- | ---------------------------- | ---------------------------------------------- | --------- |
| Create Handover | Enter valid handover details | Handover is saved to database                  | Pass      |
| Create Handover | Upload an image              | Image is successfully attached to the handover | Pass      |
| Create Handover | Leave required fields empty  | Validation errors are displayed                | Pass      |
| Create Handover | Click submit                 | Redirects to handover detail page              | Pass      |
| Create Handover | Click cancel                 | Redirects back to handover list page           | Pass      |

## Handover Detail Page

| Page            | User Action                | Expected Result                                   | Pass/Fail |
| --------------- | -------------------------- | ------------------------------------------------- | --------- |
| Handover Detail | View handover content      | Title, metadata, content, and image are displayed | Pass      |
| Handover Detail | Click image                | Image opens in new tab or enlarged view           | Pass      |
| Handover Detail | Click edit (author only)   | Redirects to edit handover page                   | Pass      |
| Handover Detail | Click delete (author only) | Confirmation prompt appears                       | Pass      |
| Handover Detail | Confirm delete             | Handover is removed from database                 | Pass      |

## Edit Handover Page

| Page          | User Action             | Expected Result                        | Pass/Fail |
| ------------- | ----------------------- | -------------------------------------- | --------- |
| Edit Handover | View edit form          | Form is pre-filled with existing data  | Pass      |
| Edit Handover | Update handover content | Changes are saved successfully         | Pass      |
| Edit Handover | Click cancel            | Redirects back to handover detail page | Pass      |

## Comments Section 

| Page     | User Action                  | Expected Result                    | Pass/Fail |
| -------- | ---------------------------- | ---------------------------------- | --------- |
| Comments | Add a valid comment          | Comment appears under the handover | Pass      |
| Comments | Submit empty comment         | Validation error is displayed      | Pass      |
| Comments | Delete own comment           | Comment is removed                 | Pass      |
| Comments | Attempt delete as non-author | Action is denied                   | Pass      |

## Profile Page

| Page    | User Action                | Expected Result                          | Pass/Fail |
| ------- | -------------------------- | ---------------------------------------- | --------- |
| Profile | View profile               | Username and profile image are displayed | Pass      |
| Profile | Upload profile image       | Image is saved and displayed             | Pass      |
| Profile | Update profile information | Changes are saved successfully           | Pass      |
| Profile | Enter invalid data         | Validation error is displayed            | Pass      |

## Logout

| Page   | User Action  | Expected Result                               | Pass/Fail |
| ------ | ------------ | --------------------------------------------- | --------- |
| Logout | Click logout | User session ends and login page is displayed | Pass      |

## User Stories Validation

All defined user stories for the Pass-It project have been successfully fulfilled through manual testing.

| User Story                                                                          | Evidence                                   |
| ----------------------------------------------------------------------------------- | ------------------------------------------ |
| As a user, I can register an account so that I can access handovers                 | Registration and login tested successfully |
| As a user, I can log in and log out securely                                        | Authentication and session handling tested |
| As a user, I can create a handover so that I can pass information to the next shift | Create handover form tested                |
| As a user, I can edit or delete my own handovers                                    | Permission-based access tested             |
| As a user, I can upload images to a handover                                        | Image upload tested                        |
| As a user, I can comment on handovers                                               | Comment creation and deletion tested       |
| As a user, I can manage my profile                                                  | Profile edit and image upload tested       |
| As a non-authenticated user, I am restricted from protected pages                   | Access control tested                      |
