# Sports Scouting Platform

A web-based scouting platform that allows coaches and analysts to access, edit, and analyze tactical reports for 10 Premier League teams. Designed to streamline opposition analysis and replace manual scouting documents with structured, visual, and interactive digital data.

---

## Features

### Role-Based Access
- **Coach**
  - Can view reports
  - Can select a team to scout
  - Can view 3 tactical panels:
    - In Possession
    - Out of Possession
    - Pressing Systems
  - Can view statistical data (as charts)
  - Can view tactical images
  - Can write and save **personal notes** under each team
  - **Read-only access**

- **Analyst**
  - Can view and **edit** reports
  - Can update tactical text, stats, and upload images for each panel
  - Has full CRUD access to the scouting content

---

## Tech Stack

### Frontend
- **React.js**
- **Material UI** for consistent styling
- **Chart.js / Recharts** for displaying statistical data
- **Axios** for API integration

### Backend
- **Django REST Framework**
- **JWT Authentication**
- Role-based permissions
- Image upload support (media files)
- Structured API for report data

### 🗃️ Database
- **PostgreSQL** (production-ready relational database)

---

## 🗂️ App Structure

### 🧍 Authentication
- Sign up / Login for **Coach** and **Analyst**
- Email & password authentication
- JWT token storage (for frontend)

### 🏟️ Team Selection
- After login, users are presented with a list of 10 Premier League teams.
- Clicking on a team opens the scouting interface.

### 📋 Scouting Reports
Each team has 3 panels:
- **In Possession**
- **Out of Possession**
- **Pressing Systems**

Each panel includes:
- **Tactical Analysis** (text)
- **Statistical Data** (rendered as interactive charts)
- **Images** (uploaded via backend, rendered in the UI)

### 📝 Coach Notes
- Coaches can write and save personal notes per team.
- These notes are private and only visible to the coach who wrote them.

---

## Permissions

| Feature                | Coach     | Analyst   |
|------------------------|-----------|-----------|
| View Teams             | ✅        | ✅        |
| View Reports           | ✅        | ✅        |
| Add/Edit Reports       | ❌        | ✅        |
| Upload Images          | ❌        | ✅        |
| View/Edit Notes        | ✅ (own)  | ❌        |

---

