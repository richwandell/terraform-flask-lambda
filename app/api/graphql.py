from typing import Dict

import graphene
import graphql
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from app.auth.models import Account, User


class AccountObject(SQLAlchemyObjectType):
    class Meta:
        model = Account
        interfaces = (graphene.relay.Node, )


class UserObject(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (graphene.relay.Node, )


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_accounts = SQLAlchemyConnectionField(AccountObject)
    all_users = SQLAlchemyConnectionField(UserObject)

    user = graphene.Field(
        UserObject,
        username=graphene.Argument(type=graphene.String)
    )

    @staticmethod
    def resolve_user(
            args: Dict,
            info: graphql.execution.base.ResolveInfo,
            username: str
    ):
        query = UserObject.get_query(info=info)

        if username:
            query.filter(User.username == username)

        user = query.first()


        return user


schema = graphene.Schema(query=Query)