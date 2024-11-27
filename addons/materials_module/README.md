# Material and Supplier Module

This Odoo 14 module provides a system for managing materials and suppliers, with REST APIs for CRUD operations.

---

## Features

- Manage materials with the following attributes:
    - Material Code (Required)
    - Material Name (Required)
    - Material Type (Dropdown: Fabric, Jeans, Cotton)
    - Material Buy Price (Must be ≥ 100)
    - Supplier (Linked to Supplier model)
- Manage suppliers with the following attribute:
    - Supplier Name (Required)
- Filter materials by type.
- REST APIs for Material CRUD operations.

---

## Installation

1. Copy `materials_module` into your Odoo custom addons directory
   ```bash
   cp -r materials_module /your/custom/odoo-addons/path
   ```
2. Update Module List from Odoo UI:
    1. **Login to Odoo**.
    2. **Activate Developer Mode**:
        - Go to **Settings** > Scroll down and click **Activate Developer Mode**.
    3. **Update Apps List**:
        - Go to **Apps** > Click on the "Update Apps List" button.
        - Search for your custom module and install it.

## Usage

To manage materials and suppliers, go to the corresponding menu in Odoo.

Use the provided REST APIs to interact with the module programmatically:

- **GET /materials**: List all materials.
- **POST /materials**: Create a material.
- **PUT /materials/<material_id>**: Update a material.
- **DELETE /materials/<material_id>**: Delete a material.

## Documentation

- Entity-Relationship Diagram: Check the `docs/erd.dbml` file.

## Dependencies

- Odoo 14
- Base module

## Developer Info

Having problem with this module? [Contact me](mailto:mrhabibiesmk@gmail.com).