from odoo import models, fields, api

class Buku(models.Model):
    _name="perpus.mahasiswa"
    _rec_name = "Nama"
    
    NIM = fields.Char("NIM", required=True, size=100)
    Nama = fields.Char("Nama", required=True, size=100)
