# -*- coding: utf-8 -*-
from odoo import api, fields, models


class partner_inherit(models.Model):
    
    _inherit = 'res.partner'

    
    x_alerta = fields.Boolean(
        string='Alerta',
    )
    