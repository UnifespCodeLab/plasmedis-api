from api import db
from api.model.database.privileges import Privilegio

def GetPrivileges():
    privileges = Privilegio.query.all()
    results = [
        {
            "user_type": privilege.user_type
        } for privilege in privileges]

    return {"count": len(results), "privileges": results, "message": "success"}

def PostPrivileges(data):
    new_privilege = Privilegio(user_type=data['user_type'])

    db.session.add(new_privilege)
    db.session.commit()

    return {"message": f"Privilégio criado com sucesso"}