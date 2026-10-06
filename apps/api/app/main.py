"""The aim for this document is for API endpoints/Routes"""



# importing FASTAPI from the package I just installed, Depends is FastAPI's dependency injection system. We're going to tell FastAPI:
# Whenever this endpoint runs, give it a database session from get_db(), HTTP lets us return proper HTTP errors
from fastapi import FastAPI, Depends, HTTPException, Response, Cookie
# FastAPI uses Pydantic to define and validate the shape of incoming data.
from pydantic import BaseModel

from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Service, Admin
from app.auth import verify_password, create_access_token, verify_access_token


# This class means we are willing to accept when someone creates a service
class ServiceCreate(BaseModel):
    name: str
    price: float
    duration_minutes: int

# creates the FAST application
app = FastAPI()

# When someone sends an HTTP GET request to /, execute the function immediately below.
@app.get("/")

# returns a Python dictionary. FastAPI automatically converts that to JSON for the client
def root():
    return {"message": "Welcome to the Plait Room API"}

# WHEN THE CLIENT SENDS : GET /services API finds @app.get("/services") and executes def get_services():
@app.get("/services")
def get_services(db: Session = Depends(get_db)):
    services = db.query(Service).all()
    return services


@app.post("/services", status_code=201)
def create_service(
    service: ServiceCreate,
    db: Session = Depends(get_db) # means FastAPI calls get_db() for us and gives this request a SQLAlchemy session called db.
):
    new_service = Service( # creates a SQLAlchemy Service object in Python.
        name=service.name,
        price=service.price,
        duration_minutes=service.duration_minutes
    )

    db.add(new_service) # tells SQLAlchemy, I want this object inserted into the database.
    db.commit() # actually commits the transaction to PostgreSQL.
    db.refresh(new_service) # asks PostgreSQL/SQLAlchemy to reload the object with database-generated information. This matters because PostgreSQL generated the id.

    return new_service

class AdminLogin(BaseModel):
    email: str
    password: str

# Create the login endpoint for Admin
@app.post("/admin/login")
def admin_login(
    credentials: AdminLogin,
    response: Response,
    db: Session = Depends(get_db)
):
    admin = (
        db.query(Admin)
        .filter(Admin.email == credentials.email.lower())
        .first()
    )

    if not admin:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(credentials.password, admin.password_hash):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    token = create_access_token(admin.id)

    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        max_age=60 * 60,
        samesite="lax",
        secure=False
    )

    return {
        "message": "Login successful",
        "admin_id": admin.id,
        "email": admin.email
    }

def get_current_admin(
    access_token: str | None = Cookie(default=None),
    db: Session = Depends(get_db)
):
    if not access_token:
        raise HTTPException(
            status_code=401,
            detail="Not authenticated"
        )

    payload = verify_access_token(access_token)

    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired authentication"
        )

    admin_id = int(payload["sub"])

    admin = db.query(Admin).filter(Admin.id == admin_id).first()

    if not admin:
        raise HTTPException(
            status_code=401,
            detail="Admin not found"
        )

    return admin

# Create admin/me. 
@app.get("/admin/me")
def admin_me(
    admin: Admin = Depends(get_current_admin) # Admin is the variable we are creating, Depends tells FASTAPI 
    # before you run admin_me(), run get_current_admin()
):
    return {
        "id": admin.id,
        "email": admin.email
    }

# Add the logout endpoint
@app.post("/admin/logout")
def admin_logout(response: Response):
    response.delete_cookie(
        key="access_token"
    )

    return {
        "message": "Logout successful"
    }