from datetime import datetime

from peewee import *
import sqlite3

db = SqliteDatabase('tahlel.db')
mysql_db = MySQLDatabase('tahlel', user='root', password='12345',
                         host='localhost', port=3306)
import MySQLdb


class AddAnalyst(Model):
    name = CharField(unique=True)
    default_result1 = FloatField(default=True, null=True)
    default_result2 = FloatField(default=True, null=True)
    result_choices = CharField()
    price = DecimalField()

    class Meta:
        database = mysql_db

class AddClient(Model):
    client_name = CharField(null=True)
    client_age = IntegerField(default=1,null=True)
    client_genus = CharField(null=True)
    client_doctor = CharField(null=True)
    class Meta:
        database = mysql_db
class Doctor(Model):
    doctor_name = CharField()

    class Meta:
        database = mysql_db

class AddNewItem(Model):
    client_name = CharField()
    client_age = IntegerField(default=1)
    genus = IntegerField(default=0)
    doctor_name = IntegerField(default=0)
    notes = TextField(null=True)
    analyse_name = CharField()
    analyse_result = CharField

    class Meta:
        database = mysql_db


class AddBuys(Model):
    buys_type = CharField()
    signal_item_price = IntegerField()
    total_price = IntegerField()
    quantity = IntegerField()

    class Meta:
        database = mysql_db


class Report(Model):
    date = DateField()
    time = TimeField()
    report_type = IntegerField()

    class Meta:
        database = mysql_db


class AddUser(Model):
    user_name = CharField()
    user_password = CharField()

    class Meta:
        database = mysql_db


class UserPer(Model):
    add_sale_item_page = IntegerField()
    analyst_page = IntegerField()
    clients_page = IntegerField()
    history_page = IntegerField()
    settings_page = IntegerField()
    show_analyst = IntegerField()
    add_analyst = IntegerField()
    edit_analyst = IntegerField()
    delete_analyst = IntegerField()
    change_theme = IntegerField()
    add_buys = IntegerField()
    report = IntegerField()

    class Meta:
        database = mysql_db


db.connect()
db.create_tables([AddAnalyst,Doctor,AddNewItem,AddBuys,Report,AddUser,UserPer,AddClient])
print('ok')