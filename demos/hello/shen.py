# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li
    :license: MIT, see LICENSE for more details.
"""
import click
from flask import Flask

shen = Flask(__name__)       # app 或 application 的实例


# the minimal Flask application
@shen.route('/')     # shen  注册路由，负责管理 URL 和函数之间的映射[必须以斜杠（\）开始]
def index():        # shen  此函数为，视图函数
    return '<h1>Hello, Shen!</h1>'


# bind multiple URL for one view function
@shen.route('/hi')
@shen.route('/hello')
def say_hello():
    return '<h1>Hello, Flask!</h1>'


# dynamic route, URL variable default
@shen.route('/greet', defaults={'name': 'Programmer'})
@shen.route('/greet/<name>')
def greet(name):
    return '<h1>Hello, %s!</h1>' % name


# custom flask cli command
@shen.cli.command()
def hello():
    """Just say hello."""
    click.echo('Hello, Human!')
