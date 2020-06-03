from odoo import models, fields, api, exceptions,_


class Author(models.Model):
    _inherit = 'res.partner'
    _description = 'Biblioteca Fran Autores'

    is_author=fields.Boolean(string="Es autor",default=False)
    libro_ids=fields.One2many('bibliotecafran.libro','author_id',string="Libros del autor")

class Reserva(models.Model):
    _name='bibliotecafran.reserva'
    _description = 'Biblioteca Fran Reservas'

    name=fields.Char(string="Id de la reserva",default=_('New'))
    reserva_date=fields.Date(string="Fecha de la reserva")
    client_id=fields.Many2one('res.partner',string="Cliente de la reserva")
    libro_ids=fields.Many2many('bibliotecafran.libro', string="Libros de la reserva")

    @api.model
    def create(self,vals):
        if vals.get('name',_('New'))==_('New'):
            vals['name']=self.env['ir.sequence'].next_by_code('seq.reserva') or _('New')
        return super(Reserva,self).create(vals)

class Cliente(models.Model):
    _inherit = 'res.partner'
    _description = 'Biblioteca Fran Clientes'

    is_cbiblioteca=fields.Boolean(string="Es cliente",default=False)
    reservas_ids=fields.One2many('bibliotecafran.reserva','client_id',string="Reservas del cliente")

class Libro(models.Model):
    _name = 'bibliotecafran.libro'
    _description = 'Biblioteca Fran Libros'

    name=fields.Char(string="Nombre del libro", required=True)
    description=fields.Text(string="Descripcion del libro")
    date_published=fields.Date(string="Fecha de publicacion del libro")

    author_id=fields.Many2one('res.partner',string="Autor del libro")

