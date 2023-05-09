from werkzeug.security import generate_password_hash, check_password_hash

class UserStore:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(UserStore, cls).__new__(cls)
            cls.__instance.users = {}
            cls.__instance.logged_in_users = {}
        return cls.__instance

    def register_user(self, email, password, display_name):
        if email in self.users:
            return False
        self.users[email] = {'password_hash': generate_password_hash(password), 'display_name': display_name}
        return True

    def authenticate_user(self, email, password):
        if email not in self.users or not check_password_hash(self.users[email]['password_hash'], password):
            return None
        if self.logged_in_users and email not in self.logged_in_users:
            return None
        self.logged_in_users = {email: self.users[email]['display_name']}
        return self.logged_in_users[email]

    def logout_user(self, email):
        if email not in self.logged_in_users:
            return False
        del self.logged_in_users[email]
        return True
