import psycopg2
import boto3
import argparse
import os
import sys


def AddUser(conn, f_name,l_name,email,username,p_word):
    cur = conn.cursor()
    cur.execute("INSERT INTO users VALUES (%s, %s, %s, %s, %s)", (f_name, l_name,email,username,p_word))
    conn.commit()
    