"""module where we generate the content to send back the requests according to MVT pattern"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from flask import (Flask, request, jsonify, render_template)

from Flask_api.chat import random_chat
from Flask_api.constant import stopwords, control_characters
from Flask_api.map import MapRequests
from Flask_api.parser import Parser
from Flask_api.wiki import WikiSummary, wikipedia

# Read the google map secret key api key from environment variables
API_KEY_FRONT = os.environ.get('API_KEY_FRONT')
API_KEY_BACK = os.environ.get('API_KEY_BACK')

# Starting with ../ moves one directory backwards and starts there. instantiation of Flask
app=Flask(__name__, template_folder='../templates', static_folder='../static')


@app.route('/')
def index():
    # Show the user the template html files stored in the 'templates' directory inside the flask package.
    return render_template("template.html", API_KEY_FRONT=API_KEY_FRONT)  # display the Google Map api key to template


@app.route('/api', methods=['POST', 'GET'])  # ajax following the URL does not appear in browser
def ajax_request():
    """Response to front-end"""
    msg_received=request.args.get("question")  # The name attribute "question" specifies the name for the input HTML
    # element. This name attribute can be used to reference the element in a JavaScript.
    # instantiation of Parser class
    response=Parser(msg_received, stopwords, control_characters).process_parser()
    # instantiation of MapRequests class and used of get_position method
    ggmap=MapRequests(API_KEY_BACK, response).get_position()
    # random sentences from papybot
    sentences=random_chat()
    # instantiation of Wiki
    wiki_response=WikiSummary(wiki=wikipedia, msg_parsed=response)

    if ggmap == 'no result':
        answer={'chat_address_ko': sentences['chat_address_ko'], 'wiki_ko': "Pas de recherche wiki car pas de map",
                }
        return jsonify(answer)  # return random sentences if no result found from google map API

    elif wiki_response.get_address() == 'no result':  # if previous conditions not true, then try this condition
        answer={'address': ggmap['address'],
                'lat': ggmap['latitude'],
                'lng': ggmap['longitude'],
                'chat_address_ok': sentences['chat_address_ok'],
                'wik_ko': sentences['wik_ko'],
                }
        return jsonify(answer)  # return random sentences if no result found from wiki API

    else:
        address=wiki_response.get_address()
        wiki_response.get_place_summary(address)
        answer={'address': ggmap['address'],
                'lat': ggmap['latitude'],
                'lng': ggmap['longitude'],
                'sum': [wiki_response.summary],
                'chat_address_ok': sentences['chat_address_ok'],
                'wik_ok': sentences['wik_ok'],
                }
        return jsonify(answer)  # this will send a JSON response to the browser
