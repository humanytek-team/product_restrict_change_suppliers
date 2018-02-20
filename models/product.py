# -*- coding: utf-8 -*-
###############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2017 Humanytek (<www.humanytek.com>).
#    Manuel Márquez <manuel@humanytek.com>
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
###############################################################################

from openerp import api, fields, models
from openerp.exceptions import ValidationError
from openerp.tools.translate import _


class ProductTemplate(models.Model):
    _inherit = "product.template"

    authorize_change_suppliers = fields.Boolean(
        'Authorize change of suppliers')

    @api.multi
    def write(self, vals):

        if not self.authorize_change_suppliers:
            if 'seller_ids' in vals:
                raise ValidationError(_(
                    'This product is not authorized to change of suppliers.'))
        return super(ProductTemplate, self).write(vals)
