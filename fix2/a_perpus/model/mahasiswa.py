from odoo import models, fields, api

class Buku(models.Model):
    _name="perpus.mhs"
    _rec_name = "nama"
    
    nomor_induk = fields.Char("NIM", required=True, size=100)
    nama = fields.Char("Nama", required=True, size=100)