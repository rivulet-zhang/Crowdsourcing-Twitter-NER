#!/usr/local/bin/python2.7
# vim: set fileencoding=utf8 noexpandtab tabstop=4 shiftwidth=4:   # boilerplate
from __future__ import division as _, unicode_literals as _; del _ # boilerplate

# Credit: 	Armin Ronacher et al; adapted from Flask documentation; BSD license
#           http://flask.pocoo.org/docs/0.12/patterns/sqlite3/
import ast
try:
	from pysqlite2 import dbapi2 as sqlite3  # Try to import newer sqlite3 module
except ImportError:
	import sqlite3 # Fall back to old sqlite3 module, which may lack a few things.
import flask
import config


def query(sql, parameters=()):
	"""
	Run an SQL query, ""
	"""
	if not isinstance(parameters, (tuple, list)):
		raise TypeError(parameters) # must be tuple or list
	conn = get_connection()
	rows = conn.execute(sql, parameters)
	conn.commit()
	return rows.fetchall()


def get_connection():
	"""
	Open a connection to the database.  This will be used to connect on demand.
	"""
	# flask.g documentation:  http://flask.pocoo.org/docs/0.12/api/#flask.g
	try:
		conn = flask.g._database_connection
	except AttributeError:
		conn = flask.g._database_connection = sqlite3.connect(config.PATH_DATABASE,
				detect_types=sqlite3.PARSE_DECLTYPES)  # allows storing datetime, etc.
		conn.row_factory = sqlite3.Row
	return conn


def close_connection_if_open():
	"""
	Close the connection to the database, if any.
	"""
	try:
		conn = flask.g._database_connection
	except AttributeError:
		pass
	else:
		conn.close()
		del flask.g._database_connection


# Allow storing tuple, dict, or bool directly in the database
sqlite3.register_adapter(tuple, repr)
sqlite3.register_converter(str("tuple"), ast.literal_eval)
sqlite3.register_adapter(dict, repr)
sqlite3.register_converter(str("dict"), ast.literal_eval)
sqlite3.register_adapter(bool, lambda b:{True:1, False:0, None:None}[b])
sqlite3.register_converter(str("boolean"), lambda s:{1:True, 0:False, None:None}[s])
