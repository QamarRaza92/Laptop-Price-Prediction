from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,SelectField,IntegerField,FloatField
from wtforms.validators import DataRequired



company =            ['Lenovo', 'Acer', 'Asus', 'Dell', 'HP', 'MSI', 'Toshiba']
Typename =           ['Notebook', '2 in 1 Convertible', 'Gaming', 'Ultrabook','Workstation', 'Netbook']
Screenresolution =   ['Full HD 1920x1080', '1366x768','IPS Panel Full HD / Touchscreen 1920x1080',
                      'Full HD /   Touchscreen 1920x1080', 'IPS Panel Full HD 1920x1080','1600x900', 'IPS Panel 4K Ultra HD 3840x2160','Quad HD+ / Touchscreen 3200x1800','IPS Panel 4K Ultra HD / Touchscreen 3840x2160','Touchscreen 1366x768']
Opsys =              ['No OS', 'Linux', 'Windows 10', 'Windows 7', 'Chrome OS']
CPU_Company =        ['Intel', 'AMD']
Processor_Gen =      ['i5', 'i7', 'i3', 'Quad', 'A6-Series', 'M', 'Dual', 'Ryzen',
                     'E-Series', 'A12-Series', 'A9-Series', 'A8-Series', 'x5-Z8350',
                     'FX', 'A10-Series', 'E3-1535M', 'E3-1505M']
ROM_byte =           ['TB', 'GB']
Storage_drive =      ['HDD', 'SSD', 'Flash Storage']
ram =                [ 4,  8, 16, 12,  6, 32,  2, 64, 24]
rom =                [  1, 500, 256, 128, 180, 512,  32,   2,  16,  64,   8]



class InputForm(FlaskForm):
    Company          = SelectField(label='Company',choices=company,validators=[DataRequired()])
    TypeName         = SelectField(label='TypeName',choices=Typename,validators=[DataRequired()])
    Inches           = FloatField(label='Inches',validators=[DataRequired()])
    ScreenResolution = SelectField(label='Screen Resolution',choices=Screenresolution,validators=[DataRequired()])
    OpSys            = SelectField(label='Operating System',choices=Opsys,validators=[DataRequired()])
    CPU_company      = SelectField(label='CPU Company',choices=CPU_Company,validators=[DataRequired()])
    Processor_gen    = SelectField(label='Processor Generation',choices=Processor_Gen,validators=[DataRequired()])
    RAM              = SelectField(label='RAM',choices=ram,validators=[DataRequired()])
    ROM              = SelectField(label='ROM',choices=rom,validators=[DataRequired()])
    ROM_Byte         = SelectField(label='ROM Byte',choices=ROM_byte,validators=[DataRequired()])
    Storage_Drive    = SelectField(label='Storage Drive',choices=Storage_drive,validators=[DataRequired()])
    Submit           = SubmitField('Predict Laptop Price')
    