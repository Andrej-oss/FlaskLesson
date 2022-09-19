from flask import Blueprint, render_template, request, redirect, url_for

from app import db
from app.owner.forms import RegisterOwner, RegisterPet
from app.owner.models import OwnerModel, PetModel

owner = Blueprint('owner', __name__, 'static', template_folder='templates', url_prefix='/owner')


@owner.route('/')
def show_all():
    owners = OwnerModel.query.all()
    return render_template('owner/index.html', owners=owners)


@owner.route('/register', methods=['GET', 'POST'])
def register_owner():
    form = RegisterOwner(request.form)
    if request.method == 'POST' and form.validate():
        data = dict(request.form)
        del data['save']
        owner = OwnerModel(**data)
        owner.save_to_db()
        return redirect(url_for('owner.show_all'))
    return render_template('owner/register.html', form=form)


@owner.route('/pet/<int:owner_id>')
def show_all_pets_by_owner_id(owner_id):
    pets = PetModel.find_pets_by_owner_id(owner_id)
    print(pets)
    if not pets:
        return redirect(url_for('owner.register_pet', owner_id=owner_id))
    return render_template('owner/pets.html', pets=pets, owner_id=owner_id)


@owner.route('/pet/register/<int:owner_id>', methods=['GET', 'POST'])
def register_pet(owner_id):
    print('dsadasda')
    form = RegisterPet(request.form)
    if request.method == 'POST' and form.validate():
        data = dict(**request.form)
        del data['save']
        pet = PetModel(**data)
        owner = OwnerModel.query.get(owner_id)
        owner.pets.append(pet)
        owner.save_to_db()
        print(owner)
        # pet.save_to_db()
        return redirect(url_for('owner.show_all_pets_by_owner_id', owner_id=owner_id))
    return render_template('owner/register_pet.html', form=form, owner_id=owner_id)
