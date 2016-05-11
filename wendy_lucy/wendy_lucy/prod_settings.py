import dj_database_url
from settings import *

DATABASES['default'] = dj_database_url.config(conn_max_age=600)

STATIC_ROOT='/home/rosskarchner/mysite/static'
