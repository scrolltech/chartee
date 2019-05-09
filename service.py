import hug

from apphelpers.rest.hug import APIFactory
from be.app.endpoints import setup_routes

import be.app.models

from converge import settings


def make_app():
    router = hug.route.API(__name__)

    api_factory = APIFactory(router)
    api_factory.setup_db_transaction(be.app.models.db)

    setup_routes(api_factory)


make_app()
