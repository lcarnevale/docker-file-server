# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""File Server

This implementation does its best to follow the Robert Martin's Clean code guidelines.
The comments follows the Google Python Style Guide:
    https://github.com/google/styleguide/blob/gh-pages/pyguide.md
"""

__copyright__ = 'Copyright 2021, FCRlab at University of Messina'
__author__ = 'Lorenzo Carnevale <lcarnevale@unime.it>'
__credits__ = ''
__description__ = 'File Server'

import os
import logging
import argparse
from app import app
from flask import Flask
from flask import abort
from flask import request
from flask import send_file
from flask import render_template

DIRECTORY = '/mnt/fileshare'

@app.route('/')
def upload_form():
	return render_template('download.html')

"""Download file

Queries:
    filename (str): requested filenamelished

Returns:

"""
@app.route('/download', methods = ['GET'])
def download_file():
    args = request.args

    if 'filename' in args:
        filename = request.args['filename']
        logging.info('Serving file: %s' % (filename))
        filepath = '%s/%s' % (DIRECTORY, filename)
        return send_file(filepath, as_attachment=True)

    else:
        return get_bad_request()

def get_bad_request(message='Bad Request'):
    code = 400
    abort(code, message)

def __setup_logging(verbosity):
    format = "%(asctime)s %(filename)s:%(lineno)d %(levelname)s - %(message)s"
    filename='log/fileserver.log'
    datefmt = "%d/%m/%Y %H:%M:%S"
    level = logging.INFO
    if (verbosity):
        level = logging.DEBUG
    logging.basicConfig(filename=filename, filemode='a', format=format, level=level, datefmt=datefmt)


def main():
    description = ('%s\n%s' % (__author__, __description__))
    epilog = ('%s\n%s' % (__credits__, __copyright__))
    parser = argparse.ArgumentParser(
        description = description,
        epilog = epilog
    )

    parser.add_argument('-H', '--host',
                        dest='host',
                        help='Define the hostname',
                        type=str, default='0.0.0.0')

    parser.add_argument('-p', '--port',
                        dest='port',
                        help='Define the host port',
                        type=int, default=5000)
    
    parser.add_argument('-v', '--verbosity',
                        dest='verbosity',
                        help='Set application as verbose',
                        action="store_true")

    options = parser.parse_args()
    logdir_name = 'log'

    if not os.path.exists(logdir_name):
        os.makedirs(logdir_name)

    __setup_logging(options.verbosity)
    app.run(host=options.host, port=options.port, 
        threaded=True, debug = options.verbosity)

if __name__ == "__main__":
    main()