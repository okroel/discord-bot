from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(Integer, primary_key=True)
    address = Column(String(50), unique=True, nullable=False)
    name = Column(String, nullable=False)
    chain = Column(String)

    def __repr__(self):
        return f"Wallet(address={self.address!r}, name={self.name!r}, \
                        chain={self.chain})"
