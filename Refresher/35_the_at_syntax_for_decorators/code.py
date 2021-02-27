import functools
guestUser = {"username": "miguel", "access_level": "guest"}
adminUser = {"username": "jose", "access_level": "admin"}

def make_secure(func):
    @functools.wraps(func) # keeps the name and documentation passed as func.
    def secure_function(user):
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}"
    
    return secure_function

@make_secure
def get_admin_password():
    return "1234"

print(get_admin_password(guestUser))
print(get_admin_password(adminUser))