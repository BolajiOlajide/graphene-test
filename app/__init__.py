from flask import Flask, g
from flask_graphql import GraphQLView
from graphql.execution.executors.asyncio import AsyncioExecutor

from .schema import schema
from .dataloaders import UserLoader


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True

    @app.before_request
    def initialize_loaders():
        g.user_loader = UserLoader()

    @app.route("/")
    def hello_world():
        return "Hello World!"

    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True,  # for having the GraphiQL interface
            executor=AsyncioExecutor()
        )
    )

    return app
