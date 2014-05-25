from planout.experiment import SimpleExperiment
import os

import psycopg2 as pg
from psycopg2.extras import Json as pJson

CONN_PARAMS = {'database': 'experiments',
               'user': os.getenv('DB_ENV_USER'),
               'password': os.getenv('DB_ENV_PASS'),
               'host': os.getenv('DB_PORT_5432_TCP_ADDR'),
               'port': os.getenv('DB_PORT_5432_TCP_PORT')}

class PostgresLoggedExperiment(SimpleExperiment):

    def configure_logger(self):
        self.conn = pg.connect(**CONN_PARAMS)

    def log(self, data):
        cursor = self.conn.cursor()

        columns = ['inputs', 'name', 'checksum', 'params', 'time', 'salt',
                   'event']

        names = ','.join(columns)
        placeholders = ','.join(['%s']*len(columns))
        ins_statement = ("insert into experiments ({}) values ({})"
                         .format(names, placeholders))

        row = []
        for column in columns:
            value = data[column]
            row.append(pJson(value) if isinstance(value, dict) else value)

        with self.conn.cursor() as curr:
            curr.execute(ins_statement, row)

        self.conn.commit()
