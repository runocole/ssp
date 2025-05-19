# Sports Scouting Platform

A coach-only web-based platform that allows users to view official tactical reports and create personal scouting drafts for 10 Premier League teams. Designed to simplify opposition analysis with clean visuals, chart-based stats, and editable personal notes.

---

## Features

### Coach Role 
- Register/Login
- View 10 Premier League teams
- For each team:
  - View the **Official Report** structured in 3 panels:
    - In Possession
    - Out of Possession
    - Pressing Systems
  - Each panel includes:
    - Tactical write-ups
    - Charts (statistical data)
    - Tactical images
  - **Create/Edit Personal Draft Reports**
    - Add text per panel
    - Upload custom images
    - Save notes privately per team

---

## Tech Stack

### Frontend
- React.js
- Material UI
- Chart.js or Recharts (for stats)
- Axios

### Backend
- Django + Django REST Framework
- JWT Auth (for coach login)
- PostgreSQL
- Admin Panel for uploading official reports
- Media upload support for images
- Coach draft report model with per-user ownership

---

