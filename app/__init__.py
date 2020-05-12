from flask import Flask
from flask_graphql import GraphQLView
from graphql.execution.executors.asyncio import AsyncioExecutor

from .schema import schema
from .dataloaders import UserLoader


context = lambda: {
    "user_loader": UserLoader()
}

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True

    @app.route("/")
    def hello_world():
        return "Hello World!"

    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True,  # for having the GraphiQL interface
            get_context=context,
            executor=AsyncioExecutor()
        )
    )

    return app
