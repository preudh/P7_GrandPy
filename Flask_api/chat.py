"""Papybot random sentences file"""
import random

from Flask_api.constant import bot_address_ko, bot_address_ok, bot_message_wiki_ok, bot_message_wiki_ko


def random_chat():
    """Return a random sentence"""
    chat_address_ko = random.choice(bot_address_ko)  # if map does not exist
    chat_address_ok = random.choice(bot_address_ok)  # if map does exist
    wik_ok = random.choice(bot_message_wiki_ok)  # if wiki summary does exist
    wik_ko = random.choice(bot_message_wiki_ko)  # if wiki summary does not exist
    return {'chat_address_ko': chat_address_ko, 'chat_address_ok': chat_address_ok, 'wik_ok': wik_ok,
            'wik_ko': wik_ko}
