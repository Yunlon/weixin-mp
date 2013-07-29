#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# Created at May 03 12:43 by BlahGeek@Gmail.com

import sys
if hasattr(sys, 'setdefaultencoding'):
    sys.setdefaultencoding('UTF-8')

from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.http import require_http_methods
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib import messages
from .utils import *
from .messages import *
from response import response

def index(req):
    if not checkSig(req):
        return HttpResponseForbidden()
    if req.method == 'GET':
        return HttpResponse(req.GET.get('echostr', ''))
    req_msg = parseXml(req)
    ret = 'Null Response.'

    if req_msg.get('MsgType', '') == 'text':
        ret = response(req_msg.get('Content', ''))

    return HttpResponse(makeTextMsg(req_msg, ret))
