from api import db
from api.model.database.forms import Form_Socioeconomico

def PostFormSocio(data):
    new_form = Form_Socioeconomico(nome_rep_familia=data['nome_rep_familia'], pessoa=data['pessoa'], qtd_pessoas_familia=data['qtd_pessoas_familia'],
    pessoa_amamenta=data['pessoa_amamenta'], qtd_criancas=data['qtd_criancas'], gestante=data['gestante'], qtd_amamentando=data['qtd_amamentando'], qtd_criancas_deficiencia=data['qtd_criancas_deficiencia'], qtd_gestantes=data['qtd_gestantes'])
    db.session.add(new_form)
    db.session.commit()

    return {"message": f"Formulário enviado!"}

def GetFormSocio(id):
    forms = Form_Socioeconomico.query.filter_by(pessoa=id).all()
    results = []
    for form in forms:
        if form.preenchido:
            results.append({
                "preenchido": form.preenchido,
                "nome_rep": form.nome_rep_familia,
                "qtd_pessoas": form.qtd_pessoas_familia,
                "qtd_criancas": form.qtd_criancas,
                "gestante": form.gestante,
                "qtd_amamentando": form.qtd_amamentando,
                "qtd_criancas_deficiencia": form.qtd_criancas_deficiencia,
                "pessoa_amamenta": form.pessoa_amamenta,
                "qtd_gestantes": form.qtd_gestantes
            })

    return {"count": len(results), "users": results}

def PostFormSocioGetByUser(data, user_id):
    form = Form_Socioeconomico.query.filter_by(pessoa=user_id).first()
    if form is None:
        new_form = Form_Socioeconomico(nome_rep_familia=data['nome_rep_familia'], pessoa=user_id, qtd_pessoas_familia=data['qtd_pessoas_familia'],
        pessoa_amamenta=data['pessoa_amamenta'], qtd_criancas=data['qtd_criancas'], gestante=data['gestante'], qtd_amamentando=data['qtd_amamentando'], qtd_criancas_deficiencia=data['qtd_criancas_deficiencia'], qtd_gestantes=data['qtd_gestantes'])
        db.session.add(new_form)
        db.session.commit()
        return {"status":"1000", "message":"created"}

    else:
        form.nome_rep_familia = data['nome_rep_familia']
        form.qtd_pessoas_familia = data['qtd_pessoas_familia']
        form.pessoa_amamenta = data['pessoa_amamenta']
        form.qtd_criancas = data['qtd_criancas']
        form.gestante = data['gestante']
        form.qtd_amamentando = data['qtd_amamentando']
        form.qtd_criancas_deficiencia = data['qtd_criancas_deficiencia']
        form.qtd_gestantes = data['qtd_gestantes']

        db.session.add(form)
        db.session.commit()

        return {"status":"1000", "message":"updated"}

def GetFormSocioGetByUser(user_id):
    form = Form_Socioeconomico.query.filter_by(pessoa=user_id).one()
    response = {
            "nome_rep_familia": form.nome_rep_familia,
            "qtd_pessoas_familia": form.qtd_pessoas_familia,
            "pessoa_amamenta": form.pessoa_amamenta,
            "qtd_criancas": form.qtd_criancas,
            "gestante": form.gestante,
            "qtd_amamentando": form.qtd_amamentando,
            "qtd_criancas_deficiencia": form.qtd_criancas_deficiencia,
            "qtd_gestantes": form.qtd_gestantes,
    }

    return {"message": "success", "form": response}