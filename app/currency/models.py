from app.db import Base
from sqlalchemy import Column, Integer, Float,String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Currency(Base):
    __tablename__ = "currency"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, index=True, nullable=False)
    code = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relación: Una moneda puede estar en muchos pares
    # El back_populates debe coincidir con el nombre del atributo en la otra clase
    pairs = relationship("PairCurrency", back_populates="currency", foreign_keys="[PairCurrency.currency_id]")

class PairCurrency(Base):
    __tablename__ = "pair_currency"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    
    # Claves Foráneas: Conectan la tabla físicamente
    base_currency_id = Column(Integer, ForeignKey("currency.id"), index=True)
    currency_id = Column(Integer, ForeignKey("currency.id"), index=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relaciones de Python: Para hacer par.currency.name
    currency = relationship("Currency", back_populates="pairs", foreign_keys=[currency_id])
    prices = relationship("CurrencyPrice", back_populates="pair")

class CurrencyPrice(Base):
    __tablename__ = "currency_price"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    
    # Clave Foránea hacia el Par
    pair_currency_id = Column(Integer, ForeignKey("pair_currency.id"), index=True)
    
    price = Column(Float) # Tip: considera usar Numeric o Float para precios
    volume = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relación de Python
    pair = relationship("PairCurrency", back_populates="prices")