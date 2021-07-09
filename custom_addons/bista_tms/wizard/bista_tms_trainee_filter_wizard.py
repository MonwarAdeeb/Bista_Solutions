# -*- coding: utf-8 -*-

from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError
from datetime import datetime


class TraineeFilter(models.TransientModel):
    _name = "bista.trainee.filter"
    _description = "Bista Training Management System - Trainee Filter Wizard"

    from_date = fields.Date(
        string="Date From", default=lambda self: fields.datetime.today())

    to_date = fields.Date(
        string="Date To", default=lambda self: fields.datetime.today())

    def view_filtered_trainees(self):
        return {
            'name': "Filtered Trainees",
            'type': "ir.actions.act_window",
            'res_model': "bista.trainee",
            'view_mode': "tree",
            'domain': ['&', ('date_of_birth', '>=', self.from_date), ('date_of_birth', '<=', self.to_date)]
        }

    def print_filtered_trainees(self):
        # This data is retrieved from TraineeReport abstract class below
        data = {
            'form': self.read()[0]
        }

        return self.env.ref('bista_tms.action_report_bista_tms_trainee').report_action(self, data=data)


class TraineeReport(models.AbstractModel):
    # _name format is: report.module_name.report_template_id
    _name = 'report.bista_tms.trainee_report_document'
    _description = 'Bista Training Management System - Trainee Filter Wizard Report'

    @api.model
    def _get_report_values(self, docids, data=None):

        # this checks if from_date & to_date fields have any inputs, then filters them accordingly
        if data['form']['from_date'] and data['form']['to_date']:
            trainees = self.env['bista.trainee'].search(
                ['&', ('date_of_birth', '>=', data['form']['from_date']), ('date_of_birth', '<=', data['form']['to_date'])])
        else:
            trainees = self.env['bista.trainee'].search([])

        return{
            'doc_model': 'bista.trainee',
            'docs': trainees,
        }
