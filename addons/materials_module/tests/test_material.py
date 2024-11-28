from odoo.tests.common import TransactionCase


class TestMaterial(TransactionCase):

    def setUp(self):
        super(TestMaterial, self).setUp()
        self.supplier = self.env['material.supplier'].create({
            'name': 'Test Supplier'
        })
        self.assertTrue(self.supplier.id, "Supplier should be created.")
        self.assertEqual(self.supplier.name, 'Test Supplier')

    def test_material_creation(self):
        self.material = self.env['material.material'].create({
            'code': 'MAT001',
            'name': 'Test Material',
            'type': 'fabric',
            'buy_price': 200,
            'supplier_id': self.supplier.id,
        })
        self.assertTrue(self.material.id, "Material should be created.")
        self.assertEqual(self.material.name, 'Test Material')
        self.assertEqual(self.material.code, 'MAT001', "Material code is incorrect.")
        self.assertEqual(self.material.type, 'Fabric', "Material type is incorrect.")
        self.assertGreater(self.material.buy_price, 200, "Material buy price should be greater than 100.")
        self.assertEqual(self.material.supplier_id, self.supplier.id, "Material supplier is incorrect.")

    def test_material_update(self):
        """Test that material can be updated correctly."""
        self.material.name = 'Updated Material Name'
        self.material.buy_price = 100
        self.material.sudo().write({
            'material_name': 'Updated Material Name',
            'material_buy_price': 100
        })
        self.material.refresh()
        self.assertEqual(self.material.name, 'Updated Material Name', "Material name should be updated.")
        self.assertEqual(self.material.buy_price, 100, "Material price should be updated.")

    def test_material_delete(self):
        """Test the deletion of a material record."""
        # Verify the material exists before deletion
        material_count_before = self.env['material.material'].search_count([('id', '=', self.material.id)])
        self.assertEqual(material_count_before, 1, "Material should exist before deletion")

        # Delete the material
        self.material.unlink()

        # Verify the material no longer exists after deletion
        material_count_after = self.env['material.material'].search_count([('id', '=', self.material.id)])
        self.assertEqual(material_count_after, 0, "Material should not exist after deletion")
