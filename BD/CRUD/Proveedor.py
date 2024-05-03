import BD.Estructura as Estructura
from BD.Estructura import Proveedor

def create(Nombre, Descripcion, session=None):
    if session is None:
        session = Estructura.get_session()
    prov = Proveedor(Nombre=Nombre, Descripcion=Descripcion)
    session.add(prov)
    session.commit()
    return prov

def read(Nombre):
    session = Estructura.get_session()
    prov = session.query(Proveedor).filter(Proveedor.Nombre == Nombre).first()
    session.close()
    return prov

def read_by_id(Id):
    session = Estructura.get_session()
    prov = session.query(Proveedor).filter(Proveedor.Id == Id).first()
    session.close()
    return prov

def list():
    session = Estructura.get_session()
    provs = session.query(Proveedor).all()
    session.close()
    return provs

def update(prov, Descripcion=None):
    session = Estructura.get_session()
    prov = session.query(Proveedor).filter(Proveedor.Nombre == prov.Nombre).first()
    if Descripcion is not None:
        prov.Descripcion = Descripcion
    session.commit()

def delete(prov):
    session = Estructura.get_session()
    session.delete(prov)
    session.commit()