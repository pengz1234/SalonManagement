# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class salon_base(models.Model):
#     _name = 'salon_base.salon_base'
#     _description = 'salon_base.salon_base'
#
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


class SalonBaseHospital(models.Model):
    """
    门店信息
    """
    _name = 'salon_base.hospital'
    _description = '门店'
    _rec_name = 'name'
    _inherit = ['mail.thread']

    name = fields.Char(string='门店', required=True, track_visibility='onchange')
    address = fields.Char(string='地址', required=True, track_visibility='onchange')
    tel = fields.Char(string='联系电话', track_visibility='onchange')
    rank = fields.Char(string='等级', required=True, track_visibiliyu='onchange')
    remark = fields.Char(string='备注', track_visibility='onchange')


    # @api.model
    # def onchange(self):
    #     return self.env.uid