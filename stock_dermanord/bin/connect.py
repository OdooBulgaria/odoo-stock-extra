#!/usr/bin/python
# -*- coding: utf-8 -*-
##############################################################################
#
# OpenERP, Open Source Management Solution, third party addon
# Copyright (C) 2016- Vertel AB (<http://vertel.se>).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

#pip install odoorpc
import odoorpc

local_server = 'localhost'
local_user = 'anders.wallenquist@vertel.se'
local_passwd = ''
local_database = 'dev_migrated12okt15'
local_port = 8069




# Prepare the connection to the server
#odoo = odoorpc.ODOO(local_server, protocol='xmlrpc', port=local_port)
odoo = odoorpc.ODOO(local_server, port=local_port)
print odoo.config['admin_password']

# Check available databases
print(odoo.db.list())

exit()
# Login (the object returned is a browsable record)
odoo.login(local_database,local_user, local_passwd)
#user = odoo.env.user
#print(user.name)            # name of the user connected
#print(user.company_id.name) # the name of its company

#for template in oerp.get('product.template').browse(oerp.get('product.template').search([('','','')])):
#for template in oerp.get('product.template').browse(oerp.get('product.template').search([])):

#~ attribute_id = odoo.env['product.attribute'].search([('name', '=', 'Volume')])
#~ if len(attribute_id) == 0:
    #~ attribute_id = odoo.env['product.attribute'].create({'name': 'Volume'})
#~ else:
    #~ attribute_id = attribute_id[0]
#~ print(attribute_id)
#~ variants = []
#~ for id in odoo.env['product.template'].search([('name', 'like', ',')]):
    #~ record = odoo.env['product.template'].read(id,['name'])
    #~ i = record['name'].find(',')
    #~ name = record['name'][0:i]
    #~ variant = record['name'][i + 2:]
    #~ if variant[-2:] != 'ml':
        #~ variants.append(record['name'])
    #~ else:
        #~ products[name] = [variant]
#~ for key in products:
    #~ print('Product name: |%s|\nVariants: |%s|\n' % (key, products[key]))
    #products = [line.product_id.name for line in order.order_line]
    #print(products)
    
#~ import codecs
#~ import sys 
#~ UTF8Writer = codecs.getwriter('utf8')
#~ sys.stdout = UTF8Writer(sys.stdout)
#~ for v in variants:
    #~ print(v)
# Update data through a browsable record
#user.name = "Brian Jones"
#oerp.write_record(user)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
