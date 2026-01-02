CREATE TABLE dbo.Users (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Name NVARCHAR(100) NOT NULL,
    Email NVARCHAR(150) NOT NULL,
    CreatedAt DATETIME NOT NULL DEFAULT GETDATE()
);
GO

---------------------

ALTER TABLE fastapi_user_api.dbo.Users
ADD PasswordHash nvarchar(255) NOT NULL;


-----------------------

CREATE PROCEDURE dbo.usp_user_create
    @name NVARCHAR(100),
    @email NVARCHAR(150),
    @password_hash NVARCHAR(255)
AS
BEGIN
    SET NOCOUNT ON;

    INSERT INTO Users (Name, Email, CreatedAt, PasswordHash)
    VALUES (@name, @email, GETDATE(),@password_hash);

    SELECT SCOPE_IDENTITY() AS UserId;
END;
GO

---------------------

CREATE PROCEDURE dbo.usp_user_list
AS
BEGIN
    SET NOCOUNT ON;

    SELECT
        Id,
        Name,
        Email,
        CreatedAt
    FROM dbo.Users
    ORDER BY Id DESC;
END;
GO


----------------------

CREATE PROCEDURE dbo.usp_user_get_by_id
    @Id INT
AS
BEGIN
    SET NOCOUNT ON;

    SELECT
        Id,
        Name,
        Email,
        CreatedAt
    FROM dbo.Users
    WHERE Id = @Id;
END;
GO

----------------------

USE fastapi_user_api;
GO

CREATE PROCEDURE dbo.usp_user_get_by_email
    @Email NVARCHAR(150)
AS
BEGIN
    SET NOCOUNT ON;

    SELECT 
        Id,
        Name,
        Email,
        PasswordHash,
        CreatedAt
    FROM dbo.Users
    WHERE Email = @Email;
END;
GO
