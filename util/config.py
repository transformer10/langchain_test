import configparser

import yaml
import os


class Config:
    keys: dict
    mysql: dict
    postgresql: dict
    proxy: dict

    def __init__(self, file: str = os.path.join(os.path.join(os.getcwd(), "config"), "config.ini")):
        con = configparser.ConfigParser()
        con.read(file, encoding='utf-8')
        self.keys = dict(con.items('keys'))
        self.mysql = dict(con.items('mysql'))
        self.postgresql = dict(con.items('postgresql'))
        self.proxy = dict(con.items('proxy'))


def get_yml_config():
    with open(os.path.join(os.path.join(os.getcwd(), "config"), "config.yml")) as f:
        conf = yaml.load(f.read(), yaml.FullLoader)
    return conf


def get_ini_config():
    con = configparser.ConfigParser()
    file = os.path.join(os.path.join(os.getcwd(), "config"), "config.ini")
    con.read(file, encoding='utf-8')
    return con
