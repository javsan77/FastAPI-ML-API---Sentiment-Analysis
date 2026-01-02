from fastapi import HTTPException, status
from app.config.security import verify_password, create_access_token

class AuthService:

    def __init__(self, repo):
        self.repo = repo
    
    def login(self, email: str, password: str):
        user = self.repo.find_by_email(email)

        if not user:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        if not verify_password(password, user.PasswordHash):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        token = create_access_token({"sub": str(user.Id)})

        return {"access_token": token}
    

    
