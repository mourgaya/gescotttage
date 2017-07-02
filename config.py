import os
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'poulmarvezen2018.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
