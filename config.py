#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7196653974:AAFBhgQKJ1F7z-L1X62NX5KjFxgC8IXEBNM")
    API_ID = int(os.environ.get("API_ID", "23163380"))
    API_HASH = os.environ.get("API_HASH", "2dca155e786c7db2d295e5b4ab10783b")
    

