# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models

# Create your models here.
class Avaluo(models.Model):
    """
    Entidad que representa un avaluo en concreto
    El inmueble por defecto no esta publicado, se debe
    publicar como una accion aparte.
    """
    direccion = models.CharField(
        max_length=100,
        verbose_name="Dirreccion del inmueble",
    )
    tipoImmueble= models.CharField(
        max_length=50,
        verbose_name="Tipo del inmueble",
    )
    banos= models.CharField(
        max_length=10,
        verbose_name="Baños",
    )
    area_construida = models.DecimalField(
        default=0,
        max_digits=20,
        decimal_places=0,
    )
    estrato= models.CharField(
        max_length=10,
        verbose_name="Area construida",
    )
    fecha_Cons = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Fecha de Construccion",
    )
    administracion = models.DecimalField(
        default=0,
        max_digits=20,
        decimal_places=0,
    )
    deposito = models.BooleanField(
        verbose_name="Deposito",
    )
    ascensor = models.BooleanField(
        verbose_name="Ascensor",
    )
    vigilancia = models.BooleanField(
        verbose_name="Vigilancia",
    )
    conjunto_cerrado = models.BooleanField(
        verbose_name="Conjunto Cerrado",
    )
    gimnasio = models.BooleanField(
        verbose_name="gimnasio",
    )
    parqueadero = models.BooleanField(
        verbose_name="Parqueadero",
    )
    precio = models.DecimalField(
        default=0,
        max_digits=20,
        decimal_places=0
    )
    precioCalc = models.DecimalField(
        default=0,
        max_digits=20,
        decimal_places=0
    )
    Lat = models.FloatField()
    Long = models.FloatField()
    geom = models.PointField()
        #default = GEOSGeometry('POINT(-74 4)', srid=4686)
    #)
class Barrio(models.Model):
    """
    Entidad que representa un Barrio
    """
    gid = models.IntegerField(
        verbose_name="GID",
    )
    nombre= models.CharField(
        max_length=40,
        verbose_name="Nombre",
    )
    amun_codgr= models.CharField(
        max_length=5,
        verbose_name="Codigo Municipio",
    )
    amun_nombr= models.CharField(
        max_length=100,
        verbose_name="Nombre Municipio",
    )
    zona_id= models.IntegerField(
        verbose_name="Zona ID",
    )
    vpm2= models.IntegerField(
        verbose_name="Zona ID",
    )
    geom = models.MultPolygonField()
