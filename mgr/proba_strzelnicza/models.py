# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Pliki(models.Model):
    id_proby = models.OneToOneField('ProbaStrzelnicza', models.DO_NOTHING, db_column='id_proby', primary_key=True)
    kamera_zwykla = models.CharField(max_length=50)
    kamera_szybka = models.CharField(max_length=50)
    kamera_ir = models.CharField(max_length=50)
    kamera_ir_szybka = models.CharField(max_length=50)
    zdjecie = models.CharField(max_length=50)
    proba_strzelnicza_id_proby = models.IntegerField()



class Pocisk(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nazwa = models.TextField(db_column='Nazwa', unique=True)  # Field name made lowercase. This field type is a guess.

    def __str__(self):
        return f"{self.nazwa}"

class Bron(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    bron = models.TextField(db_column='Bron', unique=True)  # Field name made lowercase. This field type is a guess.

    def __str__(self):
        return f"{self.bron}"

class Czynniki(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    czynnik = models.CharField(max_length=50, null=False)
    parametr = models.CharField(max_length=50, null=False)
    temperatura = models.IntegerField()
    wypelnienie = models.FloatField()

    def __str__(self):
        return f"{self.czynnik}"

class Material(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    rodzaj = models.TextField(db_column='Rodzaj', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    id_czynnik = models.ForeignKey(Czynniki, models.DO_NOTHING)

    def __str__(self):
        return f"{self.rodzaj}"
class Podloza(models.Model):
    id_podloze = models.AutoField(primary_key=True)
    podloze = models.TextField(unique=True, blank=True, null=True)  # This field type is a guess.

    def __str__(self):
        return f"{self.podloze}"


class ProbaStrzelnicza(models.Model):
    id_proby = models.CharField(max_length=60, primary_key=True)
    id_bron = models.ForeignKey(Bron, models.DO_NOTHING, db_column='id_bron')
    id_pocisk = models.ForeignKey(Pocisk, models.DO_NOTHING, db_column='id_pocisk')
    temperatura = models.FloatField(blank=True, null=True)
    warunki_atmosferyczne = models.TextField()  # This field type is a guess.
    predkosc_wiatru = models.IntegerField()
    material = models.ForeignKey(Material, models.DO_NOTHING)
    podloze = models.ForeignKey(Podloza, models.DO_NOTHING)
    rykoszet = models.ForeignKey('Rykoszet', models.DO_NOTHING)
    czynnik = models.ForeignKey(Czynniki, models.DO_NOTHING)
    def __str__(self):
        return f"{self.id_proby} ({self.id_bron}, {self.id_pocisk})"




class Rykoszet(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    material = models.TextField(blank=True, null=True)  # This field type is a guess.
    def __str__(self):
        return f"{self.material}"
