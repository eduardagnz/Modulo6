from sqlalchemy import Column, Integer, String, List, relationship, ForeignKey
from __init__ import Base

class Zoo(Base):
    __tablename__ = 'zoo'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    visitants = Column(Integer)
    user_id = Column(Integer, ForeignKey("user.id"))
    
    habitats = relationship('habitat', back_populates='zoo')
    user = relationship('user', back_populates='zoo')    
    
    
    def __repr__(self) -> str:
        return f'<Zoo(name={self.name}, specie={self.specie},happiness={self.happiness}, habitats={self.habitats}, user={self.user_id})'
    
    def json(self) -> dict:
        return {
            "id": self.id,
            "visitants": self.visitants,
            "habitats": self.habitats,
            "user": self.user,
        }