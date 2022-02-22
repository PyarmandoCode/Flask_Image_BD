#pip install psycopg2-binary
class Config(object):
    #todo conectand a la base de datos de POSTGRESS modificado el dialecto
    #todo conectado a la base de datos de MYSQL
    ##SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/ecommerce_cargamos'
    #SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:rioazulq12@localhost:5432/ecommerce_cargamos'
    #SQLALCHEMY_TRACK_MODIFICATIONS = True
    #todo conectand a la base de datos de POSTGRESS modificado el dialecto
    #SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:rioazulq12@localhost:5432/tiendaonline_cargamos'
    SQLALCHEMY_DATABASE_URI = 'postgresql://mgcvqsjisxomdy:0655309c5bc75dbcc9a6aef6ffc8f70022ab0c9065df7d2715b4d393bb767b0e@ec2-52-204-196-4.compute-1.amazonaws.com:5432/d5sgo5evgrc95p'
    SQLALCHEMY_TRACK_MODIFICATIONS = True