from flask import Flask
from flask_restful import Api
from ..instance.config import app_config
from .v1.auth.views import Login, SignUp