import BD.Estructura as Estructura
from BD.Estructura import Categoria

def create(Nombre, Descripcion, session=None):
    if session is None:
        session = Estructura.get_session()
    cat = Categoria(Nombre=Nombre, Descripcion=Descripcion)
    session.add(cat)
    session.commit()
    return cat

def read(Nombre):
    session = Estructura.get_session()
    cat = session.query(Categoria).filter(Categoria.Nombre == Nombre).first()
    session.close()
    return cat

def read_by_id(Id):
    session = Estructura.get_session()
    cat = session.query(Categoria).filter(Categoria.Id == Id).first()
    session.close()
    return cat

def list():
    session = Estructura.get_session()
    cats = session.query(Categoria).all()
    session.close()
    return cats

def update(cat, Descripcion=None):
    session = Estructura.get_session()
    cat = session.query(Categoria).filter(Categoria.Nombre == cat.Nombre).first()
    if Descripcion is not None:
        cat.Descripcion = Descripcion
    session.commit()

def delete(cat):
    session = Estructura.get_session()
    session.delete(cat)
    session.commit()