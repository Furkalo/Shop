from django.contrib.auth.models import BaseUserManager  # Importing the base user manager class from Django

# Custom user manager for creating user and superuser
class UserManager(BaseUserManager):

    # Method to create a regular user
    def create_user(self, email, full_name, password):
        if not email:
            raise ValueError('Email is required!')
        if not full_name:
            raise ValueError('Full name is required!')

        # Create user with the provided email and full name, normalize the email
        user = self.model(email=self.normalize_email(email), full_name=full_name)
        user.set_password(password)
        user.save(using=self.db)
        return user

    # Method to create a superuser (user with admin privileges)
    def create_superuser(self, email, full_name, password):
        user = self.create_user(email, full_name, password)
        user.is_admin = True
        user.save(using=self.db)
        return user
