import BD.Estructura as Estructura
from BD.Estructura import Venta

def create(Fecha, Total, session=None):
    if session is None:
        session = Estructura.get_session()
    venta = Venta(Fecha=Fecha, Total=Total)
    session.add(venta)
    session.commit()
    return venta

def read(id_venta):
    session = Estructura.get_session()
    venta = session.query(Venta).filter(Venta.Id == id_venta).first()
    session.close()
    return venta

def list():
    session = Estructura.get_session()
    ventas = session.query(Venta).all()
    session.close()
    return ventas

def list_by_fecha(fecha):
    session = Estructura.get_session()
    ventas = session.query(Venta).filter(Venta.Fecha == fecha).all()
    session.close()
    return ventas

def update(venta, Fecha=None, Total=None):
    session = Estructura.get_session()
    venta = session.query(Venta).filter(Venta.Id == venta.Id).first()
    if Fecha is not None:
        venta.Fecha = Fecha
    if Total is not None:
        venta.Total = Total
    session.commit()

def delete(venta):
    session = Estructura.get_session()
    session.delete(venta)
    session.commit()