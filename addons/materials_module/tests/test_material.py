from odoo.exceptions import ValidationError
from odoo.tests.common import TransactionCase


class TestMaterial(TransactionCase):

    def setUp(self):
        super(TestMaterial, self).setUp()
        self.supplier = self.env['material.supplier'].create({
            'name': 'Test Supplier'
        })

    def test_material_creation(self):
        material = self.env['material.material'].create({
            'code': 'MAT001',
            'name': 'Test Material',
            'type': 'fabric',
            'buy_price': 200,
            'supplier_id': self.supplier.id,
        })
        self.assertEqual(material.name, 'Test Material')

    def test_buy_price_validation(self):
        with self.assertRaises(ValidationError):
            self.env['material.material'].create({
                'code': 'MAT002',
                'name': 'Invalid Material',
                'type': 'jeans',
                'buy_price': 50,
                'supplier_id': self.supplier.id,
            })
