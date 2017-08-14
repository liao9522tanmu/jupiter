import uuid

import time

from firstaio.db.TestModel import TestModelC
from firstaio.http.HttpDecorator import get, post


@get('/')
async def index():
    return '<h1>hello world</h1>'


@get('/redirect')
async def redirect():
    return 'redirect:http://www.threecss.com'


@get('/examples')
async def getUsers():
    r = await TestModelC.findAll()
    return {
        'examples': r
    }


@get('/templates')
async def getTemplates():
    return {
        '__template__': 'blogs1.html',
        '__user__': {
            'name': 'firstaio'
        },
        'blogs': [
            {
                'id': uuid.uuid4().hex,
                'name': 'firstaio作品展示',
                'summary': 200,
                'created_at': 1501006589.27344
            },
            {
                'id': uuid.uuid4().hex,
                'name': 'firstaio作品展示',
                'summary': 200,
                'created_at': 1501006589.27344
            },
            {
                'id': uuid.uuid4().hex,
                'name': 'firstaio作品展示',
                'summary': 200,
                'created_at': time.time()
            }
        ]

    }


@post('/api/examples')
async def api_register_user(request, *, userEmail, userName, userPassword):
    pass
