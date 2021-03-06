#!/usr/bin/env python
import csv
import functools
import xmlrpclib
import base64
HOST = '172.17.0.2'
PORT = 8069
DB = 'encuesta'
USER = 'pcs@soluciones4g.com'
PASS = 'seguridad2017'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST, PORT)

# 1. Login
uid = xmlrpclib.ServerProxy(ROOT + 'common').login(DB, USER, PASS)
print "Logged in as %s (uid:%d)" % (USER, uid)

call = functools.partial(
    xmlrpclib.ServerProxy(ROOT + 'object').execute,
    DB, uid, PASS)
#*****************************************************************************************
#*****************************************************************************************

reader = csv.reader(open('res.partner.csv', 'rb'))

campo=[]
partner_template={}
band=1
for row in reader:
    if band == 1:
        campo=row
        band=2
    else:
        cont=0  
        for col in campo:  
            partner_template.update({campo[cont]: row[cont]})
            cont=cont+1            
        print partner_template

        #partner_id = call('res.partner', 'create', partner_template)
        #print partner_id


img = open('images.jpg', 'rb').read()
data = base64.b64encode(img)
# Write data to odoo
ids = call('res.partner', 'create',  {'name':'ferras','image':data})
print "\n partner ids %s" % ids