# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Portal Purchase Stock',
    'version': '0.1',
    'category': 'Tools',
    'complexity': 'easy',
    'description': """
This module adds purchase menu and features to your portal if purchase,stock and portal are installed.
======================================================================================================

add "Manage Lots / Serial Numbers" for suppliers that do picking with lots / serial numbers

URL for signup for a new supplier who gets a Purchase Order for the first time:
http://localhost:8069/web/signup?redirect=%2Fweb%23action%3Dmail.action_mail_redirect%26model%3Dpurchase.order%26id%3D<purchase id>&token=<token>&db=<database>

URL for existing user, arbitary model and resource id:
http://localhost:8069/web?db=<database>#action=mail.action_mail_redirect&login=<user%40domain.com>&res_id=<id>&model=<model>



    """,
    'author': 'Vertel AB',
    'depends': ['purchase','stock','portal'],
    'data': [
        'portal_purchase_view.xml',
        'security/ir.model.access.csv',
        'security/portal_security.xml',
    ],
    'installable': True,
    'auto_install': True,
    'category': 'Hidden',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
