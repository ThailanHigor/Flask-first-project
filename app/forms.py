from flask_wtf import Form
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired, Length

class RegisterForm(Form):
    name = StringField("Nome", validators=[
        DataRequired("campo obrigatório"),
        Length(5, 100, "O nome deve ter entre 5 e 100 caracteres")
    ])
    email = StringField("E-mail", validators=[
        DataRequired("campo obrigatório"),
        Email("Formato de E-mail inválido"),
        Length(5, 100, "O nome deve ter entre 5 e 100 caracteres")
    ])
    password = PasswordField("Senha", validators=[
        DataRequired("campo obrigatório"),
    ])

    submit = SubmitField("Cadastrar")


class LoginForm(Form):
    email = StringField("E-mail", validators=[
        DataRequired("campo obrigatório"),
        Email("Formato de E-mail inválido"),
    ])
    password = PasswordField("Senha", validators=[
        DataRequired("campo obrigatório"), 
    ])

    submit = SubmitField("Entrar")


