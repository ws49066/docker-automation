def serialize_user(user):
    return {
        "email": user.get("email"),
        "role": user.get("role", "cliente")
    }
