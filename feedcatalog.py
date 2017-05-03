from flask import url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, User, Category, Item

engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# Create dummy user
user1 = User(name="Bambino's Corner", email="warriorbambino23@gmail.com", picture="https://cdn2.iconfinder.com/data/icons/happy-users/100/users09-512.png")
session.add(user1)
session.commit()

# Create category #1 and add items to the category
category1 = Category(name="Orks", user_id=1)
session.add(category1)
session.commit()

item1 = Item(user_id=1, name="Ork Horde",
                     description="What can I say, they're orks and fight for the WAAAAAGGGHHHHH!",
                     image="/static/orks.jpg",
                     category=category1)
session.add(item1)
session.commit()

# Create category #2 and add items to the category
category2 = Category(name="Humans", user_id=1)
session.add(category2)
session.commit()

item2 = Item(user_id = 1, name = "Space Marines",
                     description ="These are human soldiers in advanced armored exo suits for combating those who oppose the Emperor's rule and reach.",
                     image="/static/spacemarine.jpg",
                     category=category2)
session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Astra Militarum",
             description="The regular military for the terran forces within the galaxy.",
             image="/static/astramilitarum.jpg",
             category=category2)
session.add(item3)
session.commit()

# Create category #3 and add items to the category
category3 = Category(name="Daemons", user_id=1)
session.add(category3)
session.commit()

item4 = Item(user_id=1, name="Chaos Space Marines",
             description="They sweep the battlefield with chaos and destruction alongside their daemon bretheren.",
             image="/static/chaosspacemarine.jpg",
             category=category3)
session.add(item4)
session.commit()

# Create category #4 and add items to the category
category4 = Category(name="Xenos", user_id=1)
session.add(category4)
session.commit()

item5 = Item(user_id=1, name="Tau Empire",
             description="They are aliens that spread through the galaxy for their own belief of the greater good!",
             image="/static/tau.jpg",
             category=category4)
session.add(item5)
session.commit()

item6 = Item(user_id=1, name="Eldars",
             description="Eldars are advanced alien species from Warhammer 40k Universe.",
             image="/static/eldar.jpg",
             category=category4)
session.add(item6)
session.commit()