import asyncio

import jwt

from saola_graphql_client.graphql_client import Client as SaolaGraphQLClient


access_token = ""
jwt_payload = jwt.decode(access_token, options={"verify_signature": False})
user_id = jwt_payload.get("hasura", {}).get("x-hasura-user-id")

client = SaolaGraphQLClient(
    url="https://app.saola.sg/v1/graphql",
    headers={"Authorization": f"Bearer {access_token}"},
)


async def get_and_print_current_user(client, user_id):
    current_user = await client.get_user(id=user_id)
    print(current_user)


asyncio.run(get_and_print_current_user(client, user_id))
