from flask import Flask, request, jsonify
import cx_Oracle


app = Flask(__name__)  # essa linha é para importar o framework flask

oracle_connection = cx_Oracle.connect()
cursor = oracle_connection.cursor()
