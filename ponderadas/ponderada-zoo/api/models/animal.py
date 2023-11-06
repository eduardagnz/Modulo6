from sqlalchemy import Column, Integer, String, ForeignKey, relationship, BaseSchema
from __init__ import Base

class Animal(Base):
    __tablename__ = 'animal'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    specie = Column(String)
    happiness = Column(Integer)
    habitatId = Column(Integer, ForeignKey("habitat.id") )
    
    habitat = relationship("habitat", back_populates='animal')
    
    def __repr__(self) -> str:
        return f'<Animal(name={self.name}, specie={self.specie},happiness={self.happiness}, habitat={self.habitatId})'
    
    def json(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "specie": self.specie,
            "happiness": self.happiness,
            "habitatId": self.habitatId,
        }

class AnimalSchema(BaseSchema):
    name: str
    specie: str
    happiness: int
    habitatId: int
    