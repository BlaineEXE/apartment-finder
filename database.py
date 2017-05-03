from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, Boolean
from sqlalchemy.sql import select

class Database:

    def __init__(self):
        engine = create_engine('sqlite:///apt_results.db')#, echo=True)
        metadata = MetaData()
        self.apt_results = Table('apt_results', metadata,
            Column('id', String, primary_key=True),
            Column('name', String),
            Column('url', String),
            Column('datetime', String),
            Column('price', String),
            Column('where', String),
            Column('has_image', Boolean),
            Column('has_map', Boolean),
            Column('geotag', String)
        )
        metadata.create_all(engine)
        self.conn = engine.connect()

    def add(self, listing):
        # add to db
        ins = self.apt_results.insert().values(
            id=listing['id'],
            name=listing['name'],
            url=listing['url'],
            datetime=listing['datetime'],
            price=listing['price'],
            where=listing['where'],
            has_image=listing['has_image'],
            has_map=listing['has_map'],
            geotag=str(listing['geotag'])
        )
        self.conn.execute(ins)

    def get(self, listing_id):
        # get from db by id
        sel = select([self.apt_results]).where(self.apt_results.c.id == listing_id)
        rows = self.conn.execute(sel)
        if not rows:
            return None
        return rows.fetchone() # there should only ever be one anyway


    def contains(self, listing_id):
        # return true if id exists in db
        if self.get(listing_id):
            return True
        return False
