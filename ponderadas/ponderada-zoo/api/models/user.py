from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.config import Base

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    money = Column(Integer)
    
    zoos = relationship('zoo', back_populates='user')
    
    
    
    def __repr__(self) -> str:
        return f'<User(username={self.username}, email={self.email}, money={self.money}, zoos={self.zoos})'
    
    def json(self) -> dict:
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "money": self.money,
            "zoos": self.zoos,
        }

