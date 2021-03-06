# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
# Generated by the OpenERP plugin for Dia !
from openerp import api
from openerp.osv import fields, osv
from datetime import date, datetime



class sisr_helpdesk_incidencia(osv.osv):
    _name = 'sisr.helpdesk.incidencia'
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    _rec_name = 'codigo'

    
    _columns = {
        'codigo': fields.char('Código', size=10, help="Código de la Incidencia"),
        'solicitante_id': fields.many2one('sisr.helpdesk.solicitante', string="Solicitante", help='Nombre Completo del Solicitante de la Incidencia'),
        'dependencia_id': fields.many2one('sisr.base.dependencia_gerencia','Dependencia'),
        'area_incidencia_id': fields.many2one('sisr.helpdesk.area_incidencia', string="Área de Incidencia"),
        'tipo_incidencia_ids': fields.many2many('sisr.helpdesk.tipo_incidencia', 'incidencia_tipoincidencia_rel','incidencia_id', 'tipo_incidencia_id', string="Tipo de Incidencia"),
        #'state': fields.selection([('asignado','Asignado'),('proceso','En Proceso'),('atendido','Atendido'),('resuelto','Resuelto'),('cancelado','Cancelado')], string="Status", default="asignado"),
        'state': fields.selection([('registrado','Registrado'),('leido','Leido'),('asignado','Asignado'),('proceso','En Proceso'),('atendido','Atendido'),('resuelto','Resuelto')], "Status"),
        'observacion_ids': fields.one2many('sisr.helpdesk.observacion', 'incidencia_id', string="Observaciones", help='Observaciones de una incidencia'),
	'asignacion' : fields.many2one('res.users', 'Asignado a:'),
	'denominacion': fields.char('Descripción Corta', size=90),
    'forma_de_solicitud':fields.selection([('memo','Memo'),('correo','Correo Electrónico'),('llamada','Llamada Telefónica'),('presencial','Presencial'), ('gestion','Gestión Documental')], string="Forma de Solicitud"),
    #Para adjuntar los documentos a enviar.
    'adjunto' : fields.one2many('sisr.helpdesk.adjuntos', 'adjunto_id', string ="Adjuntos", help='Documentos adicionales, Respaldos Fisicos'),
    #Fin del adjunto
    'descripcion': fields.text('Descripción'),
    'procedimiento': fields.text('Procedimiento en la Solución'),
	'fecha_creacion': fields.datetime('Fecha de Creación'),
    'fecha_leido': fields.datetime('Fecha de Leido'),
    'fecha_asignado_a': fields.datetime('Fecha Asignado a'),
    'fecha_proceso': fields.datetime('Fecha Proceso'),
    'fecha_atendido': fields.datetime('Fecha Atendido'),
	'fecha_solucion': fields.datetime('Fecha Resuelto'),
#    'dia_creacion': fields.integer('Día de Creación'),
#    'dia_leido': fields.integer('Día de Leido'), 
#    'dia_asignado_a': fields.integer('Día de Asignado a'),
#    'dia_proceso': fields.integer('Día Proceso'),
#    'dia_atendido': fields.integer('Día Atendido'),
#    'dia_solucion': fields.integer('Día Resuelto'),
#    'retraso' : fields.integer('Retraso dias', help="Conteo de dias a partir de la fecha de entrega", readonly="True", compute="_compute_calculo_dias", store="False")
    
}

    def create(self, cr, uid, vals, context=None):
        vals.update({'codigo':self.pool.get('ir.sequence').get(cr, uid, 'sisr.helpdesk.incidencia')})
	vals.update({'fecha_creacion':datetime.today()})
        new_id = super(sisr_helpdesk_incidencia, self).create(cr, uid, vals, context=None)
        return new_id
    
    # Accion para Botones en el proceso Workflow

    @api.one
    def action_registrado(self):
        #self.fecha_asignado_a=datetime.today()
        self.state='registrado'

    @api.one
    def action_leido(self):
        self.fecha_leido=datetime.today()
        self.state='leido'


    @api.one
    def action_asignado(self):
        self.fecha_asignado_a=datetime.today()
        self.state='asignado'

    @api.one
    def action_proceso(self):
        self.fecha_proceso=datetime.today()
        self.state='proceso'

    @api.one
    def action_atendido(self):
        self.fecha_atendido=datetime.today()
        self.state='atendido'

    @api.one
    def action_resuelto(self):
        self.fecha_solucion=datetime.today()
        self.state='resuelto'

    
    #Fin de los botones


    #Calculo de dias transcurridos

    #@api.depends('fecha_doc')
#    def _compute_calculo_dias(self):
#        #raise ValidationError("el valor de la fecha es %s" %(self.fecha_doc))
#        carga = datetime.strptime(self.fecha_doc,'%Y-%m-%d')
#        #today = date.today()
#        #dias = today.year - carga.year - ((today.month, today.day) < (carga.month, carga.day))
#        #dias = today.day - carga.day 
#        dias = datetime.today() - carga
#       #v = {'value':{}}
#       #v['value']['retraso'] = dias
#        self.retraso = dias.days
#        return True
sisr_helpdesk_incidencia()


class sisr_helpdesk_tipo_incidencia(osv.osv):
    """Especificación del tipo de Incidencia, depende del área de incidencia. Ej: Sistema X, Sistema Y, Consumibles, Impresora, Soporte Técnico, Correo, Acceso a Internet, Telefonía, Etc"""
    _name = 'sisr.helpdesk.tipo_incidencia'
    _columns = {
        'codigo': fields.char('Código', size=10, help='Código de este tipo de incidencia'),
        'nombre': fields.char('Nombre', size=60, help='Nombre de este tipo de incidencia'),
        'incidencia_ids': fields.many2many('sisr.helpdesk.incidencia', 'incidencia_tipoincidencia_rel', 'tipo_incidencia_id', 'incidencia_id', string="Incidencias", help='Incidencias realizadas para este tipo de incidencia'),
        'area_incidencia_id': fields.many2one('sisr.helpdesk.area_incidencia', string="Área de Incidencia", help='Área de Incidencia a la que pertenece este tipo'),
        'descripcion': fields.text('Descripción'),
    }
sisr_helpdesk_tipo_incidencia()

class sisr_helpdesk_solicitante(osv.osv):
    """Debería ser una Extensión de la clase hr.employee. Esta clase debe ir en sisr.base"""
    _name = 'sisr.helpdesk.solicitante'
    _rec_name = 'cedula'
    _columns = {
        'cedula': fields.integer(string="Cédula", help='Cedula de Identidad del Solicitante'),
        'nombres': fields.char(string="Nombres", size=60, help='Nombres del Solicitante'),
        'apellidos': fields.char(string="Apellidos", size=60, help='Apellidos del Solicitante'),
        'cargo': fields.many2one('sisr.base.hr_cargo', string="Cargo", help='Cargo del Solicitante'),
        'dependencia_direccion_id': fields.many2one('sisr.base.dependencia_direccion', string="Dirección"),
        'dependencia_gerencia_id': fields.many2one('sisr.base.dependencia_gerencia', string="Gerencia", help='Gerencia General o Regional a la que pertenece el solicitante'),
        'dependencia_gerencia_linea_id': fields.many2one('sisr.base.dependencia_gerencia_linea', string="Gerencia de Línea", help='Gerencia de Línea a la que pertenece el solicitante (En caso de Gerencia General)'),
        'dependencia_cfs_id': fields.many2one('sisr.base.dependencia_cfs', string="C.F.S.", help='C.F.S al que pertenece el solicitante (En caso de Gerencia Regional)'),
        'dependencia_division_id': fields.many2one('sisr.base.dependencia_division', string="División", help='División a la que pertenece el solicitante'),
        'dependencia_coordinacion_id': fields.many2one('sisr.base.dependencia_coordinacion', string="Coordinación", help='Coordinación a la que pertenece el solicitante'),
        'email': fields.char(string="Correo Institucional", size=100, help='Correo Electrónico Institucional del solicitante'),
        'ext_telefono': fields.char(string="Extensión", size=5, help='Extensión Telefónica del Solicitante: Ej: 2066'),
        'telefono_personal': fields.char(string="Teléfono Personal", size=11, help='Telefóno Personal del Solicitante. Ej: 04261231234'),
        'incidencia_ids': fields.one2many('sisr.helpdesk.incidencia', 'solicitante_id', 'Incidencias Asociadas'),
    }

    _sql_constraints = [('cedula_solicitante_uniq', 'unique(cedula)', 'Este solicitante ya ha sido registrado en el sistema (cedula repetida)')]    

      
    def name_get(self, cr, uid, ids, context=None):
        res = []
        solicitantes = self.browse(cr, uid, ids, context)
        for solicitante in solicitantes:
            res.append((solicitante.id, str(solicitante.cedula) + ' - ' + solicitante.nombres + ' ' + solicitante.apellidos))
        return res

sisr_helpdesk_solicitante()

class sisr_helpdesk_area_incidencia(osv.osv):
    """Especificación del Área de Incidencia,. Ej: Desarrollo, Base de Datos, Soporte, Servidores, Telecomunicaciones"""
    _name = 'sisr.helpdesk.area_incidencia'
    _rec_name = 'nombre'
    _columns = {
        'codigo': fields.char('Código', size=10, help='Código de esta área de incidencias'),
        'nombre': fields.char('Nombre', size=60, help='Nombre de esta Área de Incidencia'),
        'tipo_incidencia': fields.one2many('sisr.helpdesk.tipo_incidencia', 'area_incidencia_id', string="tipos de Incidencia", help='Tipos de incidencias que pertenecen a esta Área'),
        'dependencia_id': fields.many2one('sisr.base.dependencia_gerencia','Dependencia')
    }
sisr_helpdesk_area_incidencia()

class sisr_helpdesk_observacion(osv.osv):
    _name = 'sisr.helpdesk.observacion'
    _columns = {
        'observacion': fields.text(string="Observación"),
        'state_rel': fields.char(string="Status", size=30, help='Status que tiene la incidencia al momento de hacer la observación'),
        'incidencia_id': fields.many2one('sisr.helpdesk.incidencia', help='Relación Inversa del One2many'),
    }
sisr_helpdesk_observacion()

class res_users_inherit(osv.osv):
    _inherit= 'res.users'
    _name= 'res.users'
    _columns = {
        'dependencia_id':fields.many2one('sisr.base.dependencia_gerencia','Gerencia'),
        'area_incidencia_id':fields.many2one('sisr.helpdesk.area_incidencia','Area'),
}
res_users_inherit()
#nueva clase para adjuntar mas de un documento a la incidencia.
class sisr_helpdesk_adjuntos(osv.osv):
    _name = 'sisr.helpdesk.adjuntos'
    _rec_name = 'nombre'
    _columns = {

        'adjunto' : fields.binary(string="Adjuntos", help='Se suben los archivos adicionales que guardan relacion con el documento'),
        'numero': fields.char(string="Número de adjunto", size=10, help='Numero de adjunto'),
        'nombre': fields.char(string="Nombre del Archivo", size=60, help='Nombre del archivo adjuntado'),
        'observacion' : fields.text(string="Descripción", size=50, help='Breve nota sobre el archivo que se adjunta'),
        'adjunto_id' : fields.many2one('sisr.helpdesk.incidencia', 'incidencia'),
}
sisr_helpdesk_adjuntos()
#Fin de la clase

