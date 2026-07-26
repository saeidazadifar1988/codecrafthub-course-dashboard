# codecrafthub-course-dashboard
"CRUD dashboard for CodeCraftHub learning platform


A simple Learning Management Dashboard that provides a complete **CRUD (Create, Read, Update, Delete)** interface for managing courses. The frontend is built using **HTML, CSS, and Vanilla JavaScript** and communicates with a RESTful backend API.

## Features

- View all courses
- Add a new course
- Edit existing courses
- Delete courses
- Responsive user interface
- Loading indicators
- Success and error notifications
- Client-side form validation

## Technologies Used

- HTML5
- CSS3
- JavaScript (ES6)
- REST API

## Project Structure

```
.
├── index.html
├── README.md
└── screenshots/ (optional)
```

The application is contained in a single HTML file with embedded CSS and JavaScript.

## Prerequisites

Before running the frontend, ensure that:

- Your backend service is running.
- The backend exposes the following REST endpoints:

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/courses` | Retrieve all courses |
| GET | `/api/courses/{id}` | Retrieve a single course |
| POST | `/api/courses` | Create a new course |
| PUT | `/api/courses/{id}` | Update an existing course |
| DELETE | `/api/courses/{id}` | Delete a course |

### Backend URL

For Node.js or Python:

```
http://localhost:5000/api/courses
```

For Java Spring Boot:

```
http://localhost:8080/api/courses
```

Update the API base URL in `index.html` if your backend is hosted elsewhere.

## Course Model

Each course contains the following fields:

| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Auto-generated course ID |
| name | String | Course name |
| description | String | Course description |
| target_date | Date | Target completion date (YYYY-MM-DD) |
| status | String | Not Started, In Progress, or Completed |
| created_at | DateTime | Creation timestamp |

## Running the Application

### 1. Start the backend server

Run your backend application.

### 2. Open the frontend

Open `index.html` in your web browser.

Alternatively, use the VS Code Live Server extension.

## CRUD Operations

### Read Courses

When the page loads, the application sends:

```
GET /api/courses
```

### Create Course

Submitting the form sends:

```
POST /api/courses
```

### Update Course

Editing a course sends:

```
PUT /api/courses/{id}
```

### Delete Course

Clicking the Delete button sends:

```
DELETE /api/courses/{id}
```

## Error Handling

The application includes:

- Form validation
- API error messages
- Loading indicators
- Success notifications

## Responsive Design

The dashboard is responsive and works on desktop, tablet, and mobile devices.

## Future Improvements

- User authentication
- Search courses
- Course filtering
- Pagination
- Dark mode
- Sorting
- Dashboard analytics

## Author

Developed as the final project for the **CodeCraftHub Learning Dashboard** using Bolt AI for frontend generation and a RESTful backend service.