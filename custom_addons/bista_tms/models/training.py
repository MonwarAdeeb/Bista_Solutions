# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class TrainingSubjects(models.Model):
    _name = "bista.training.subject"
    _description = "Bista Training Management System - Training Subjects"

    name = fields.Char(string="Name", required=True)
    description = fields.Html(string="Description")
    topic = fields.One2many("bista.training.topic", "subject", string="Topic")
    trainers = fields.Many2many("bista.trainer", string="Trainers")


class TrainingTopics(models.Model):
    _name = "bista.training.topic"
    _description = "Bista Training Management System - Training Topics"

    name = fields.Char(string="Name", required=True)
    subject = fields.Many2one("bista.training.subject",
                              string="Subject", readonly=True)


class TrainingStages(models.Model):
    _name = "bista.training.stage"
    _description = "Bista Training Management System - Training Stages"

    name = fields.Char(string="Name")
    available_batch = fields.Boolean(string="Available on Batch")
    available_training_record = fields.Boolean(
        string="Available on Training Record")
    status = fields.Selection([("draft", "Draft"), ("progress", "Progress"),
                               ("done", "Done")], string="Status", default="draft")
