from odoo import http
from odoo.http import request


class MaterialController(http.Controller):

    @http.route('/materials', type='json', auth='public', methods=['GET'])
    def get_materials(self, **kwargs):
        materials = request.env['material.material'].search([])
        return materials.read(['code', 'name', 'type', 'buy_price', 'supplier_id'])

    @http.route('/materials', type='json', auth='public', methods=['POST'])
    def create_material(self, **kwargs):
        data = kwargs
        material = request.env['material.material'].create(data)
        return material.read(['id', 'code', 'name', 'type', 'buy_price', 'supplier_id'])

    @http.route('/materials/<int:material_id>', type='json', auth='public', methods=['PUT'])
    def update_material(self, material_id, **kwargs):
        material = request.env['material.material'].browse(material_id)
        material.write(kwargs)
        return material.read(['id', 'code', 'name', 'type', 'buy_price', 'supplier_id'])

    @http.route('/materials/<int:material_id>', type='json', auth='public', methods=['DELETE'])
    def delete_material(self, material_id, **kwargs):
        material = request.env['material.material'].browse(material_id)
        material.unlink()
        return {"message": "Material deleted"}
