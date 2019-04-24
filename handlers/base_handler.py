from aiohttp import web
import pickle
import matplotlib.pyplot as plt
import japanize_matplotlib
import json
import io
import base64
import numpy as np
import pandas as pd
import aiohttp_jinja2

class BaseHandler:
    def __init__(self):
        pass

    @aiohttp_jinja2.template('index.html')
    async def index(self, request):
        return {}

    @aiohttp_jinja2.template('answer.html')
    async def post(self, request):
        return_json = {}
        return return_json
