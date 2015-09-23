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
# Generated by the Odoo plugin for Dia !
{
        "name" : "Localización Venezolana",
        "version" : "0.1",
        "author" : "Bachaco-ve",
        "website" : "http://www.bachaco.org.ve",
        "category" : "Bachaco",
        "description": """ Módulo de localización Venezolana """,
        "depends" : ['base'],
        "init_xml" : ['data/estados.xml','data/municipios.xml','data/parroquias.xml' ],
        "demo_xml" : [ ],
        "update_xml" : ['views/l10n_ve_dpt_view.xml'],
        "installable": True
}
