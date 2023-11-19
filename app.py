from flask import Flask, render_template, request, redirect
from models import Pet, connect_db, db
from forms import AddPetForm, EditPetForm
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Its a secret';
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///db_pets'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def index():
    """LIst all the pets."""
    pets = Pet.query.all();
    return render_template('homepage.html', page_title='Homepage', pets=pets)

@app.route('/add', methods=['GET','POST'])
def add_pet_form():
    """To create new pet"""
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data;
        photo_url = form.photo_url.data;
        age = form.age.data;
        notes = form.notes.data;
        is_available = form.is_available.data;

        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, is_available=is_available);
        db.session.add(new_pet);
        db.session.commit();
        pets = Pet.query.all();

        return redirect('/')
    
    else:
        return render_template('add_pet_form.html', form=form, page_title='Add a Pet')


@app.route('/edit/<int:pet_id>', methods=['GET','POST'])
def edit_pet_page(pet_id):
    """To edit the pet details like photo, notes and availability"""
    
    edit_pet = Pet.query.get_or_404(pet_id);
    form = EditPetForm(obj=edit_pet)

    if form.validate_on_submit():
        edit_pet.photo_url = form.photo_url.data;
        edit_pet.notes = form.notes.data;
        edit_pet.is_available = form.is_available.data;

        db.session.add(edit_pet);
        db.session.commit();
        return redirect(f'/')
    else:
        return render_template('edit_pet_form.html', form=form, page_title='Edit a pet')

    
