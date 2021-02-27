guestUser = {"username": "miguel", "access_level": "guest"}
adminUser = {"username": "jose", "access_level": "admin"}

def get_admin_password():
    return "1234"

def make_secure(func):
    def secure_function(user):
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}"
    
    return secure_function

get_admin_password = make_secure(get_admin_password)

print(get_admin_password(guestUser))
print(get_admin_password(adminUser))