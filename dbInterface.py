# dbInterface.py

from sqlalchemy import (
    create_engine,
    MetaData,
    Column,
    Integer,
    String,
    ForeignKey,
    Date,
)
from sqlalchemy.orm import Session, registry, relationship, declarative_base

class StockDatabase:
    """An abstraction of the sqlAlchemy orm to facilitate db reading and writing."""
    base = declarative_base()
    def __init__(self, dbLocation='sqlite:///testdatabase.db'):
        self.dbLocation = dbLocation
        self.engine = create_engine(self.dbLocation, future=True)
        self.session = Session(self.engine)
        self.base = StockDatabase.base
    
    class CompanyListing(base):
        __tablename__ = 'company_listing'
        id = Column(Integer, primary_key=True)
        symbol = Column(String(20), nullable=False)
        name = Column(String(50), default='', nullable=False)
        exchange = Column(String(50), default='', nullable=False)
        assetType = Column(String(20), default='', nullable=False)

        def __repr__(self):
            return f'Company: {self.name} Listed as {self.symbol} on the {self.exchange}'
    
    def add_listing(self, symbol, name, exchange, assetType):
        listing = self.CompanyListing(symbol=symbol, name=name, exchange=exchange, assetType=assetType)
        self.base.metadata.create_all(self.engine)
        self.session.add(listing)

    def commit(self):
        self.session.commit()

    def close(self):
        self.session.close()

def main():
    db = StockDatabase()
    db.add_listing('ABBV', 'Abbvie Inc', 'NYSE', 'Stock')
    db.commit()
    db.close()
    print('Done')


if __name__ == "__main__":
    main()