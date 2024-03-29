from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom user model.

    If you’re starting a new project, it’s highly recommended to set up a
    custom user model, even if the default User model is sufficient for you.
    This model behaves identically to the default user model,
    but you’ll be able to customize it in the future if the need arises.

    Refer to https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#substituting-a-custom-user-model
    """  # noqa: E501

    pass
