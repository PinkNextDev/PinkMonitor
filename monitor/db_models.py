
from sqlalchemy import Column, SmallInteger, Integer, BigInteger, String, Float, Text, DateTime
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Block(Base):
    __tablename__ = "blockchain"

    height = Column(Integer, primary_key=True)
    hash = Column(String(length=64), index=True)
    size = Column(Integer)
    version = Column(Integer)
    merkleroot = Column(String(length=64))
    mint = Column(Float)
    time = Column(DateTime)
    nonce = Column(BigInteger)
    bits = Column(String(length=8))
    difficulty = Column(Float)
    blocktrust = Column(String(length=64))
    chaintrust = Column(String(length=64))
    previousblockhash = Column(String(length=64))
    nextblockhash = Column(String(length=64))
    flags = Column(String(length=64))
    proofhash = Column(String(length=64))
    entropybit = Column(SmallInteger)
    modifier = Column(String(length=16))
    tx = Column(ARRAY(String(length=64)))
    signature = Column(Text)
