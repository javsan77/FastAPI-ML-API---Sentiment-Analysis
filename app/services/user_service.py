from fastapi import HTTPException, status
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate
from app.core.security import hash_password

class UserService:

    def __init__(self):
        self.repo = UserRepository()

    def create_user(self, user: UserCreate) -> dict:
        hashed = hash_password(user.password)
        user_id = self.repo.create(user.name, user.email, hashed)        
        return self.get_user_by_id(user_id)

    def get_all_users(self):
        rows = self.repo.find_all()
        return [
            {
                "id": r.Id,
                "name": r.Name,
                "email": r.Email,
                "created_at": r.CreatedAt
            }
            for r in rows
        ]

    def get_user_by_id(self, user_id: int):
        row = self.repo.find_by_id(user_id)
        if not row:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        return {
            "id": row.Id,
            "name": row.Name,
            "email": row.Email,
            "created_at": row.CreatedAt
        }
