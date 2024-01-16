from random import randint, choice
from app import app
from models import db, Hero, Hero_Power, Power

powers_data = [
    {"name": "super strength", "description": "gives the wielder super-human strengths"},
    {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
    {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
    {"name": "elasticity", "description": "can stretch the human body to extreme lengths"}
]

heroes_data = [
    {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
    {"name": "Doreen Green", "super_name": "Squirrel Girl"},
    {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
    {"name": "Janet Van Dyne", "super_name": "The Wasp"},
    {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
    {"name": "Carol Danvers", "super_name": "Captain Marvel"},
    {"name": "Jean Grey", "super_name": "Dark Phoenix"},
    {"name": "Ororo Munroe", "super_name": "Storm"},
    {"name": "Kitty Pryde", "super_name": "Shadowcat"},
    {"name": "Elektra Natchios", "super_name": "Elektra"}
]

with app.app_context():
    Power.query.delete()
    Hero.query.delete()
    Hero_Power.query.delete()
    
    pow = []
    for power_info in powers_data:
        power = Power(**power_info)
        pow.append(power)
        db.session.add(power)

    db.session.commit()

    
    her = []
    for hero_info in heroes_data:
        hero = Hero(**hero_info)
        her.append(hero)
        db.session.add(hero)

    db.session.commit()


    strengths = ["Strong", "Weak", "Average"]


    for hero in her:
        for _ in range(randint(1, 3)):
            power = choice(pow)
            hero_power = Hero_Power(hero=hero, power=power, strength=choice(strengths))
            db.session.add(hero_power)

    db.session.commit()

