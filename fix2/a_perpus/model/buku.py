from odoo import models, fields, api

class Buku(models.Model):
    _name="perpus.buku"
    _rec_name = "judul"
    
    judul = fields.Char("Judul", required=True, size=100)
    penerbit = fields.Many2one(comodel_name="perpus.penerbit",
        string="Penerbit")
    deskripsi = fields.Text("Deskripsi")
