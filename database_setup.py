from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import datetime

# Declaring Instances and/or Variables
Base = declarative_base()

class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key = True)
	name = Column(String(250), nullable = False)
	email = Column(String(250), nullable = False)
	picture = Column(String)

	@property
	def serialize(self):
		return {
			'name': self.name,
			'id': self.id,
		}

class Category(Base):
	__tablename__ = 'category'

	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable = False)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)
	items = relationship("Item", cascade = "all, delete-orphan")

	@property
	def serialize(self):
		return {
			'name': self.name,
			'id': self.id,
			'user_id': self.user_id
		}

class Item(Base):
	__tablename__ = 'item'

	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable = False)
	description = Column(String(250))
	price = Column(String(8))
	createdDate = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
	category_id = Column(Integer, ForeignKey('category.id'))
	category = relationship(Category)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)

	@property
	def serialize(self):
		return {
			'name': self.name,
			'id': self.id,
			'description': self.description,
			'user_id': self.user_id
		}	
		
####### insert at end of file ######

engine = create_engine('sqlite:///itemcatalog.db', echo=True)
Base.metadata.create_all(engine)