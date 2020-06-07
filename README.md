# Tesseract Backend Api Documentation

# Registration 
     /api/auth/register/
        {
            "name" : "",
            "username" : "",
            "password": "",
            "email" : "",
        }
# Login
     /api/auth/register/
        {
            "username" : "",
            "password": "",
        }
# All Quizes
    get request
    /api/quizzes/
    headers
        {
        "Authorization" : "Token {token}",
        "Content-Type" : "application/json",
        }
# Specific quiz 
    get request
    /api/quizzes/<slug url>
    headers
        {
        "Authorization" : "Token {token}",
        "Content-Type" : "application/json",
        }
