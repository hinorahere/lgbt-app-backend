from accounts.models import CustomUser as User


def get_user(user_id):
    try:
        user = User.objects.get(id=user_id)
    except Exception as error:
        raise Exception(repr(error))

    return user
