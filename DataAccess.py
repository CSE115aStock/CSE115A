import psycopg2
import boto3
import argparse
import os
import sys

from passlib.hash import bcrypt

#Class of functions to interface with the user db
class UserDB:
    #Adds user to DB
    @staticmethod
    def AddUser(cls,conn, f_name,l_name,email,username,p_word):
        cur = conn.cursor()
        cur.execute("INSERT INTO users VALUES (%s, %s, %s, %s, %s)", (f_name, l_name,email,username,bcrypt.hash(p_word)))
        conn.commit()


    #Checks if user credentials match a user entry in the DB.
    #Returns user if correct username and password combination are passed
    #Returns false otherwise.
    @staticmethod
    def AuthenticateUser(conn,username,p_word):
        cur = conn.cursor()
        cur.execute('SELECT * from users where username = %(usr)s', {'usr': username})
        user = cur.fetchone()
        if not user:
            return False
        else:    
            hashed_pword = user[4]
            if not UserDB.check_password(p_word,hashed_pword):
                return False
        
            return user

    
    #Checks if entered password matches hashed password in the db. 
    def check_password(plain_password, hashed_password):
        return bcrypt.verify(plain_password, hashed_password)

