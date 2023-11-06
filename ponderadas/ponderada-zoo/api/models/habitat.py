from sqlalchemy import Column, Integer, String, relationship, ForeignKey
from __init__ import Base

class Habitat(Base):
    __tablename__ = 'habitat'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    specie = Column(String)
    cleanliness = Column(Integer)
    zooId = Column(Integer, ForeignKey("zoo.id"))
    
    animals = relationship('animals', back_populates='habitat')
    zoo = relationship('zoo', back_populates='habitat')
    
    def __repr__(self) -> str:
        return f'<Habita(specie={self.specie}, animals={self.animals} zoo={self.zoo})'
    
    def json(self) -> dict:
        return {
            "id": self.id,
            "specie": self.specie,
            "cleanliness": self.cleanliness,
            "zoo": self.zooId
        }