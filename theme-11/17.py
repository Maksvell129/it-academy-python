class User:

    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email



print(User.is_valid_email("alex@example.com"))
print(User.is_valid_email("invalid"))
