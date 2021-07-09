from odoo import models, fields, api

class Buku(models.Model):
    _name="perpus.penerbit"
    _rec_name = "nama"
    
    kota = fields.Char("Kota")
    nama = fields.Char("Nama", required=True, size=100)
