from flask import Flask
from flask_graphql import GraphQLView

from .schema import schema

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return "Hello World!"

    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True  # for having the GraphiQL interface
        )
    )

    return app
