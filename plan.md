
# Plait Room Development Plan

## Goal

Build a full-stack booking website for Plait Room where customers can:

- Browse braiding services
- View available appointment times
- Submit booking requests
- Receive confirmation after the stylist approves their booking

Customers do not need accounts.

The stylist has an admin account that allows her to:

- Log in and log out
- Manage services
- Set her availability
- View booking requests
- Approve or decline bookings

## Tech Stack

### Frontend

- Next.js
- TypeScript

### Backend

- FastAPI
- Python
- SQLAlchemy

### Database

- PostgreSQL

### Authentication

- Argon2 password hashing
- JWT authentication
- HTTP-only cookies

## Development Roadmap

### Phase 1 — Project Setup

- [X] Create monorepo
- [X] Create Next.js frontend
- [X] Create FastAPI backend
- [X] Set up PostgreSQL
- [X] Connect FastAPI to PostgreSQL
- [X] Configure Alembic migrations

### Phase 2 — Services

- [X] Create Service database model
- [X] Create services table
- [X] Create service endpoint
- [X] Retrieve services from PostgreSQL

### Phase 3 — Admin Authentication

- [X] Create Admin database model
- [X] Create admin migration
- [X] Hash passwords with Argon2
- [X] Create admin setup script
- [X] Create admin login endpoint
- [X] Create JWT access tokens
- [X] Store JWT in HTTP-only cookie
- [X] Create reusable get_current_admin authentication dependency
- [X] Create /admin/me
- [X] Create logout endpoint

### Phase 4 — Availability

- [ ] Design availability database model
- [ ] Create recurring weekly availability
- [ ] Create date-specific exceptions
- [ ] Protect availability management with admin authentication
- [ ] Generate available appointment times

### Phase 5 — Booking

- [ ] Create Booking database model
- [ ] Allow customers to submit booking requests
- [ ] Prevent conflicting bookings
- [ ] Create pending booking status
- [ ] Allow admin to approve bookings
- [ ] Allow admin to decline bookings

### Phase 6 — Frontend

- [ ] Build public services page
- [ ] Build customer booking flow
- [ ] Build admin login page
- [ ] Build admin dashboard
- [ ] Build availability management interface
- [ ] Build booking management interface

### Phase 7 — Production

- [ ] Configure frontend/backend CORS
- [ ] Configure production environment variables
- [ ] Deploy frontend
- [ ] Deploy backend
- [ ] Deploy PostgreSQL database
- [ ] Enable secure cookies over HTTPS
- [ ] Test complete booking flow
