from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///Inventarios.db', echo=False)
Base = declarative_base()

class Proveedor(Base):
    __tablename__ = 'Proveedor'

    Id = Column(Integer, primary_key=True)
    Nombre = Column(String)
    Descripcion = Column(String)

    productos = relationship('Producto', back_populates='proveedor')

    def __str__(self):
        return f"Proveedor(Id={self.Id}, Nombre='{self.Nombre}', Descripcion='{self.Descripcion}')"


class Categoria(Base):
    __tablename__ = 'Categoria'

    Id = Column(Integer, primary_key=True)
    Nombre = Column(String)
    Descripcion = Column(String)

    productos = relationship('Producto', back_populates='categoria')

    def __str__(self):
        return f"Categoria(Id={self.Id}, Nombre='{self.Nombre}', Descripcion='{self.Descripcion}')"


class Producto(Base):
    __tablename__ = 'Producto'

    Id = Column(Integer, primary_key=True)
    Nombre = Column(String)
    Descripcion = Column(String)
    PrecioUnitario = Column(Float)
    CantidadDisponible = Column(Integer)
    CategoriaId = Column(Integer, ForeignKey('Categoria.Id'))
    ProveedorId = Column(Integer, ForeignKey('Proveedor.Id'))

    categoria = relationship('Categoria', back_populates='productos')
    proveedor = relationship('Proveedor', back_populates='productos')
    detalles = relationship('Detalles', back_populates='producto')

    def __str__(self):
        return f"Producto(Id={self.Id}, Nombre='{self.Nombre}', Descripcion='{self.Descripcion}', PrecioUnitario={self.PrecioUnitario}, CantidadDisponible={self.CantidadDisponible}, CategoriaId={self.CategoriaId}, ProveedorId={self.ProveedorId})"


class Venta(Base):
    __tablename__ = 'Venta'

    Id = Column(Integer, primary_key=True)
    Fecha = Column(DateTime)
    Total = Column(Float)

    detalles = relationship('Detalles', back_populates='venta')

    def __str__(self):
        return f"Venta(Id={self.Id}, Fecha='{self.Fecha}', Total={self.Total})"


class Detalles(Base):
    __tablename__ = 'Detalles'

    Id = Column(Integer, primary_key=True)
    VentaId = Column(Integer, ForeignKey('Venta.Id'))
    ProductoId = Column(Integer, ForeignKey('Producto.Id'))
    Cantidad = Column(Integer)
    Descuento = Column(Integer)

    venta = relationship('Venta', back_populates='detalles')
    producto = relationship('Producto', back_populates='detalles')

    def __str__(self):
        return f"Detalle(Id={self.Id}, VentaId={self.VentaId}, ProductoId={self.ProductoId}, Cantidad={self.Cantidad}, Descuento={self.Descuento})"

Base.metadata.create_all(engine)

def get_session():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session