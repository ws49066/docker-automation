# Define como o usuário sera retonado 

def user_serializer(user):
    return {
        "id": str(user["_id"]),
        "email": user["email"],
        "role": user["role"],
    }