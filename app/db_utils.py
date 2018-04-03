# -*- coding: utf-8 -*-
from data import *

import os
import csv
from app import db
from models.Brand import Brand
from models.Model import Model
from models.Generation import Generation
from models.Series import Series
from models.Modifications import Modifications


print(os.path.abspath(__file__))

def drop_table(tclass):
    items_list = tclass.query.all()
    for item in items_list:
        db.session.delete(item)
    db.session.commit()

def drop_all_tables():
    drop_table(Modifications)
    drop_table(Series)
    drop_table(Generation)
    drop_table(Model)
    drop_table(Brand)

def init_db_brands():
    with open(INIT_BRANDS_DATA, 'r') as csvfile:
        brand_list = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(brand_list, None) # Skip header line
        for row in brand_list:
            brand = Brand(id=row[0], name=row[1])
            db.session.add(brand)
    db.session.commit()

def init_db_models():
    with open(INIT_MODEL_DATA, 'r') as csvfile:
        model_list = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(model_list, None)  # Skip header line
        for row in model_list:
            brand = Brand.query.get(row[1])
            model = Model(id=row[0], name=row[2], brand=brand)
            db.session.add(model)
    db.session.commit()

def init_db_generations():
    colnames = {"generation_id":0,"generation_name":1,"model_id":2,"year_begin":3,"year_end":4}

    with open(INIT_GENERATION_DATA, 'r') as csvfile:
        gen_list = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(gen_list, None)  # Skip header line
        for row in gen_list:
            model = Model.query.get(row[colnames['model_id']])

            gen = Generation(id=row[colnames['generation_id']],
                             name=row[colnames['generation_name']],
                             model=model,
                             year_begin=row[colnames['year_begin']],
                             year_end=row[colnames['year_end']])
            db.session.add(gen)
    db.session.commit()

def init_db_series():
    colnames = {"series_id":0,"model_id":1,"series_name":2,"generation_id":3}

    with open(INIT_SERIES_DATA, 'r') as csvfile:
        series_list = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(series_list, None)  # Skip header line
        for row in series_list:
            model = Model.query.get(row[colnames['model_id']])
            generation = Generation.query.get(row[colnames['generation_id']])

            series = Series(id=row[colnames['series_id']],
                            name=row[colnames['series_name']],
                            model=model,
                            generation=generation)
            db.session.add(series)
    db.session.commit()

def init_db_modifications():
    colnames = {"modification_id":0,"series_id":1,"model_id":2,"modification_name":3,
                "start_production_year":4,"end_production_year":5}

    with open(INIT_MODIFICATIONS_DATA, 'r') as csvfile:
        mod_list = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(mod_list, None)  # Skip header line
        for row in mod_list:
            model = Model.query.get(row[colnames['model_id']])
            series = Series.query.get(row[colnames['series_id']])

            mod = Modifications(id=row[colnames['modification_id']],
                            name=row[colnames['modification_name']],
                            model=model,
                            series=series,
                            year_begin=row[colnames['start_production_year']],
                            year_end=row[colnames['end_production_year']])
            db.session.add(mod)
    db.session.commit()


def reinit_database():
    drop_all_tables()
    init_db_brands()
    init_db_models()
    init_db_generations()
    init_db_series()
    init_db_modifications()