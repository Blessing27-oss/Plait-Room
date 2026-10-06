from getpass import getpass

from app.auth import hash_password
from app.database import SessionLocal
from app.models import Admin


def create_admin():
    email = input("Admin email: ").strip().lower() # Ask for the email interactively
    password = getpass("Admin password: ") # getpass prevents the password from appearing on your screen while you type it.

    db = SessionLocal()

    try:
        existing_admin = db.query(Admin).filter(Admin.email == email).first()

        if existing_admin:
            print("An admin with that email already exists.")
            return

        admin = Admin(
            email=email,
            password_hash=hash_password(password) # means PostgreSQL receives the Argon2 hash—not the password itself.
        )

        db.add(admin)
        db.commit()

        print("Admin created successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    create_admin()