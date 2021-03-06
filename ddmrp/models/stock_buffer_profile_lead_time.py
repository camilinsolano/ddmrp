# Copyright 2016-18 Eficent Business and IT Consulting Services S.L.
#   (http://www.eficent.com)
# Copyright 2016 Aleph Objects, Inc. (https://www.alephobjects.com/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class StockBufferProfileLeadTime(models.Model):
    _name = 'stock.buffer.profile.lead.time'
    _string = 'Buffer Profile Lead Time Factor'

    name = fields.Char(string='Name', required=True)
    factor = fields.Float(string='Lead Time Factor', required=True)
    company_id = fields.Many2one(
        'res.company', 'Company', required=True,
        default=lambda self: self.env['res.company']._company_default_get(
            'stock.buffer.profile.lead.time'))
