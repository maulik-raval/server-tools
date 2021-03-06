# -*- coding: utf-8 -*-
# Copyright 2015 Antiun Ingenieria S.L. - Javier Iniesta
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestIrExportsLineCase(TransactionCase):

    def setUp(self):
        super(TestIrExportsLineCase, self).setUp()
        m_ir_exports = self.env['ir.exports']
        self.export = m_ir_exports.create({'name': 'Partner Test',
                                           'resource': 'res.partner'})

    def test_check_name(self):
        m_ir_exports_line = self.env['ir.exports.line']
        m_ir_exports_line.create({'name': 'name',
                                  'export_id': self.export.id})
        with self.assertRaises(ValidationError):
            m_ir_exports_line.create({'name': 'name',
                                      'export_id': self.export.id})
        with self.assertRaises(ValidationError):
            m_ir_exports_line.create({'name': 'bad_error_name',
                                      'export_id': self.export.id})

    def test_get_label_string(self):
        m_ir_exports_line = self.env['ir.exports.line']
        export_line = m_ir_exports_line.create({'name': 'parent_id/name',
                                                'export_id': self.export.id})
        check_label = " (res.partner) (parent_id/name)"
        self.assertEqual(export_line.with_context(lang="en_US").label,
                         "Related Company (res.partner)/Name" + check_label)
        with self.assertRaises(ValidationError):
            m_ir_exports_line.create({'name': '',
                                      'export_id': self.export.id})
