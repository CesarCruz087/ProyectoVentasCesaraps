import BD.Estructura as Estructura
from BD.Estructura import Detalles

def create(VentaId, ProductoId, Cantidad, Descuento, session=None):
    if session is None:
        session = Estructura.get_session()
    detalle = Detalles(VentaId=VentaId, ProductoId=ProductoId, Cantidad=Cantidad, Descuento=Descuento)
    session.add(detalle)
    session.commit()
    return detalle

def read(id_detalle):
    session = Estructura.get_session()
    detalle = session.query(Detalles).filter(Detalles.Id == id_detalle).first()
    session.close()
    return detalle

def list():
    session = Estructura.get_session()
    detalles = session.query(Detalles).all()
    session.close()
    return detalles

def list_por_venta(venta):
    session = Estructura.get_session()
    detalles = session.query(Detalles).filter(Detalles.VentaId == venta.Id).all()
    session.close()
    return detalles

def update(detalle, Cantidad=None, Descuento=None):
    session = Estructura.get_session()
    detalle = session.query(Detalles).filter(Detalles.Id == detalle.Id).first()
    if Cantidad is not None:
        detalle.Cantidad = Cantidad
    if Descuento is not None:
        detalle.Descuento = Descuento
    session.commit()

def delete(detalle):
    session = Estructura.get_session()
    session.delete(detalle)
    session.commit()