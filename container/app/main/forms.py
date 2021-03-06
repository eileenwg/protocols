from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextField, FormField, FieldList
from wtforms.validators import ValidationError, DataRequired
from app.models import User




class EditProfileForm(FlaskForm):
    username = StringField('Nom d\'utilisateur', validators=[DataRequired()])
    submit = SubmitField('Soumettre')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Veuillez utiliser un nom d\'utilisateur différent.')

class InstallationPatient_dureeForm(FlaskForm):
    class Meta:
        csrf = False
    Durée = TextField("Durée", validators=[DataRequired()])

class sub_Injection(FlaskForm):
    class Meta:
        csrf = False
    Contraste = TextField("Contraste", validators=[DataRequired()])
    pré_scan = TextField("pré_scan", validators=[DataRequired()])
    per_scan = TextField("per_scan", validators=[DataRequired()])

class sub_Séquences(FlaskForm):
    class Meta:
        csrf = False
    Nom = TextField("Nom", validators=[DataRequired()])
    Durée = TextField("Durée", validators=[DataRequired()])


class Production(FlaskForm):
    class Meta:
        csrf = False
    Production = TextField("Production", validators=[DataRequired()])

class EditProtocolsForm(FlaskForm):
    Implantation = TextField("Implantation ",validators=[DataRequired()])
    InstallationPatient = FormField(InstallationPatient_dureeForm)
    Antenne = TextField("Antenne ",validators=[DataRequired()])
    Séquences = FieldList(FormField(sub_Séquences))
    Injection = FormField(sub_Injection)
    Protocole_machine = TextField("Protocole_machine ",validators=[DataRequired()])
    Durée_acquisition = TextField("Durée_acquisition ",validators=[DataRequired()])
    Durée_examen = TextField("Durée_examen ",validators=[DataRequired()])
    Durée_bloc_irm = TextField("Durée_bloc_irm ",validators=[DataRequired()])
    Date_création = TextField("Date_création ",validators=[DataRequired()])
    Date_dernière_modification = TextField("Date_dernière_modification ",validators=[DataRequired()])
    Auteur = TextField("Auteur ",validators=[DataRequired()])
    Statut = FormField(Production)
    submit = SubmitField('Soumettre')
