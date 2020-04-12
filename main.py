from open_config_files import open_config
from write_message import write_file


from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerChannel


async def main(phone):

    await client.start()
    print("Client Created")

    if await client.is_user_authorized() == False:
        await client.send_code_request(phone)

        try:
            await client.sign_in(phone, input('Password: '))

        except SessionPasswordNeededError:
            await client.sign_in(phone, input('Password: '))

    user_input_channel = 'https://t.me/IntegratedThoughtsQuotes'
    # user_input_channel = input('Channel Entity (URL or ID): ')

    if user_input_channel.isdigit():
        entity = PeerChannel(int(user_input_channel))

    else:
        entity = user_input_channel

    # Converting the entity into valid Telegram User | Channel | Group | Chat.
    channel = await client.get_entity(entity)

    # Setting parameters.
    offset_id = 0
    limit = 100
    all_messages = list()
    total_messages = 0
    total_count_limit = 0

    while True:
        print("Current Offset ID is:", offset_id,
              "; Total Messages:", total_messages)

        history = await client(GetHistoryRequest(
            peer=channel,
            offset_id=offset_id,
            offset_date=None,
            add_offset=0,
            limit=limit,
            max_id=0,
            min_id=0,
            hash=0
        ))

        if not history.messages:
            break

        messages = history.messages

        for message in messages:

            dict_msg = message.to_dict()
            # print(dict_msg)
            for key in dict_msg:

                if str(key) == 'message':
                    all_messages.append(dict_msg[key])

        offset_id = messages[len(messages) - 1].id
        total_messages = len(all_messages)

        if total_count_limit != 0 and total_messages >= total_count_limit:
            break

        for line in all_messages:
            write_file(str(all_messages.index(line) + 1), line)


if __name__ == '__main__':

    api_id, api_hash, username, phone = open_config()
    client = TelegramClient(username, api_id, api_hash)

    with client:
        client.loop.run_until_complete(main(phone))
