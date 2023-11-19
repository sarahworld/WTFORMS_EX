from models import Pet, db
from app import app

db.drop_all()
db.create_all()

p1 = Pet(name="puppy", species="dog",photo_url="https://images.unsplash.com/photo-1587402092301-725e37c70fd8?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8cHVwcHklMjBkb2d8ZW58MHx8MHx8fDA%3D", age=1,is_available=True);
p2 = Pet(name="tom", species="cat", photo_url="https://hips.hearstapps.com/hmg-prod/images/cute-photos-of-cats-looking-at-camera-1593184780.jpg?crop=0.6672958942897593xw:1xh;center,top&resize=980:*", age=1,is_available=True);
p3 = Pet(name='nimo',species='fish', photo_url="https://www.animates.co.nz/media/animates/blog/Why_is_my_fish_dead_V22.jpg",age=2,is_available=False);

db.session.add_all([p1,p2,p3]);
db.session.commit();