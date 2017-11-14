# -*- coding: utf-8 -*-
from datetime import timedelta
from odoo import api, fields, models


class Partner(models.Model):
    #_name = 'ssp.partner'

    _inherit = 'res.partner'

    fecha_nacimiento = fields.Date(string=u'Fecha_Nac')
    fecha_actual = fields.Date(default=fields.Date.today)
    edad = fields.Integer(string="Edad", compute="_calcular_edad")

    vivienda_id = fields.Selection(
        [('1', 'Propia'), ('2', 'Rentada'), ('3', 'Prestada'), ('4', 'Hípotecada'), ('5', 'Otro')], 'Tipo')
    otro_vivienda = fields.Char(string='Otro')

    @api.depends('fecha_nacimiento', 'fecha_actual')
    def _calcular_edad(self):
        for r in self:
            if not (r.fecha_nacimiento and r.fecha_actual):
                continue
            # diff = (datetime.date.today() - r.fecha_nac).days
            #r.edad =  int(diff / 365)
            #start_date = fields.Date.today
            start_date = fields.Datetime.from_string(r.fecha_nacimiento)
            end_date = fields.Datetime.from_string(r.fecha_actual)
            r.edad = (end_date - start_date).days/365
            #r.edad = 10 * 10
