import asyncio

from saola_graphql_client.graphql_client import Client as SaolaGraphQLClient


access_token = ""


async def get_chats_with_crm_records():
    client = SaolaGraphQLClient(
        url="https://app.saola.sg/v1/graphql",
        headers={"Authorization": f"Bearer {access_token}"},
    )

    chats = (await client.get_chats()).chats

    for chat in chats:
        print(f"Chat ID: {chat.id}")

        # read all chat messages
        messages = []
        for message in chat.messages:
            messages.append(f"{message['role']}: {message['content']}")

        # get crm records with type lead, contact, note, task
        crm_records = []
        for crm_record in filter(
            lambda x: x.type in ["lead", "contact", "note", "task"], chat.crm_records
        ):
            crm_records.append(f"{crm_record.id}: {crm_record.attributes}")

        print(f"Chat messages: {messages}")
        print(f"CRM Records: {crm_records}")
        print("========")


asyncio.run(get_chats_with_crm_records())
