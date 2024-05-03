import BD.Estructura as Estructura
from BD.Estructura import Producto

def create(Nombre, Descripcion, PrecioUnitario, CantidadDisponible, CategoriaId, ProveedorId, session=None):
    if session is None:
        session = Estructura.get_session()
    prod = Producto(Nombre=Nombre, Descripcion=Descripcion, PrecioUnitario=PrecioUnitario, 
                    CantidadDisponible=CantidadDisponible, CategoriaId=CategoriaId, ProveedorId=ProveedorId)
    session.add(prod)
    session.commit()
    return prod

def read(Nombre):
    session = Estructura.get_session()
    prod = session.query(Producto).filter(Producto.Nombre == Nombre).first()
    session.close()
    return prod

def read_by_id(Id):
    session = Estructura.get_session()
    prod = session.query(Producto).filter(Producto.Id == Id).first()
    session.close()
    return prod

def list():
    session = Estructura.get_session()
    prods = session.query(Producto).all()
    session.close()
    return prods

def list_by_categoria(cat):
    session = Estructura.get_session()
    prods = session.query(Producto).filter(Producto.CategoriaId == cat.Id).all()
    session.close()
    return prods

def list_by_proveedor(prov):
    session = Estructura.get_session()
    prods = session.query(Producto).filter(Producto.ProveedorId == prov.Id).all()
    session.close()
    return prods

def list_by_existence():
    session = Estructura.get_session()
    prods = session.query(Producto).filter(Producto.CantidadDisponible > 0).all()
    session.close()
    return prods

def update(prod, Descripcion=None, PrecioUnitario=None, CantidadDisponible=None):
    session = Estructura.get_session()
    prod = session.query(Producto).filter(Producto.Nombre == prod.Nombre).first()
    if Descripcion is not None:
        prod.Descripcion = Descripcion
    if PrecioUnitario is not None:
        prod.PrecioUnitario = PrecioUnitario
    if CantidadDisponible is not None:
        prod.CantidadDisponible = CantidadDisponible
    session.commit()

def delete(prod):
    session = Estructura.get_session()
    session.delete(prod)
    session.commit()