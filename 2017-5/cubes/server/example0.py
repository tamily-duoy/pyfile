# -*- coding: utf-8 -*-
# from flask import Blueprint, Flask, Response, request, g, current_app
from flask import Blueprint, Flask
# from functools import wraps
#
# from ..workspace import Workspace
# from ..auth import NotAuthorized
# from ..query import Cell, cut_from_dict
# from ..query import SPLIT_DIMENSION_NAME
# from ..query import cuts_from_string
# from ..errors import *
# from .utils import *
# from .errors import *
# from .local import *
# from ..calendar import CalendarMemberConverter
#
# from contextlib import contextmanager
#
# # Utils
# #-----
#
# def prepare_cell(argname="cut", target="cell", restrict=False):
#     """Sets `g.cell` with a `Cell` object from argument with name `argname`"""
#     # Used by prepare_browser_request and in /aggregate for the split cell
#
#
#     # TODO: experimental code, for now only for dims with time role
#     converters = {
#         "time": CalendarMemberConverter(workspace.calendar)
#     }
#
#     cuts = []
#     for cut_string in request.args.getlist(argname):
#         cuts += cuts_from_string(g.cube, cut_string,
#                                  role_member_converters=converters)
#
#     if cuts:
#         cell = Cell(g.cube, cuts)
#     else:
#         cell = None
#
#     if restrict:
#         if workspace.authorizer:
#             cell = workspace.authorizer.restricted_cell(g.auth_identity,
#                                                         cube=g.cube,
#                                                         cell=cell)
#     setattr(g, target, cell)
