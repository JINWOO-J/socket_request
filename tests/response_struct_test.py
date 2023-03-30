#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json
import sys
from pawnlib.config import pawn
from pawnlib.output import dump, classdump
parent_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
# sys.path.append(parent_dir)
sys.path.insert(0, parent_dir)

from socket_request.utils.data import ResponseField

response = ResponseField(status_code=200, text='{"sdsd":"xxxx"}')

pawn.console.log(response.__dict__)
print(response.status_code)
s
