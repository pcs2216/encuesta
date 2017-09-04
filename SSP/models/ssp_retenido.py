# -*- coding: utf-8 -*-
from odoo import fields, models


class Partner(models.Model):
    #_name = 'ssp.partner'

    _inherit = 'res.partner'

    # Add a new column to the res.partner model, by default partners are not
    # instructors
    edad = fields.Integer(string="Edad")
    # vivienda_id = fields.Many2one('res.partner.title', string='Vivienda',
    #                          ondelete='cascade')
    vivienda_id = fields.Selection(
        [('1', 'Propia'), ('2', 'Rentada'), ('3', 'Prestada'), ('4', 'Hípotecada'), ('5', 'Otro')], 'Tipo')
    otro_vivienda = fields.Char(string='Otro')
