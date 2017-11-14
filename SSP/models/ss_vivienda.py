# -*- coding: utf-8 -*-
from odoo import fields, models


class Vivienda(models.Model):
    #_name = 'ssp.partner'

    _inherit = 'res.partner.title'

    # Add a new column to the res.partner model, by default partners are not
    # instructors
    field_id = fields.Char(string='Soltero')
    