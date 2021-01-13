# -*- coding: utf-8 -*-
"""
Modified by jack
Created on Wed Jul 15 13:01:03 2020
@author: 12shu
"""


import psycopg2 as pg
#from credentials import postgres
import os

def remove_s3_sql(event, context):

    key = event['Records'][0]['s3']['object']['key']      

    # creating connection to PostgreSQL
    conn = pg.connect(user=os.environ['postgres_user'],
                          password=os.environ['postgres_pwd'],
                          host='kubrickgroupmi.ccwjw5h2ozjv.eu-west-2.rds.amazonaws.com',
                          port='5432',
                          database='kubrickgroupmidb')
     
        
    cursor = conn.cursor()
    
    # Executing queries       
       
    query = '''
    
    delete from cdp.training_media
    where s3_location = {}; 
    
    '''
    url = "'https://kubrick-cdp.s3.eu-west-2.amazonaws.com/{}'".format(key)
    cursor.execute(query.format(url))
    
    conn.commit()
 
    conn.close()
    
    return {
        'statusCode': 200,
        'body': "All done"
    }
