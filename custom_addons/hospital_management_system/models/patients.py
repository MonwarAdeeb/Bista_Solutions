from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError
from datetime import datetime


class Patients(models.Model):
    _name = "hms.patients"
    _description = "Features for Patients"
    _rec_name = "name"

    # General Fields
    photo = fields.Binary(string="Photo", attachment=True)
    name = fields.Char(string="Patient's Name", required=True,
                       help="Enter Your Name Here")
    patient_id = fields.Char(string="Patient ID", required=True)
    date_of_admission = fields.Datetime(
        string="Date of Admission", default=datetime.now())
    symptoms = fields.Text(string="Symptoms")
    diagnosis = fields.Text(string="Diagnostics")
    bill = fields.Float(string="Due Bill")
    discount_given = fields.Boolean()
    discount_percentage = fields.Float(string="Discount Percentage")
    contact_number = fields.Char(string="Contact Number")
    email = fields.Char(string="Email")

    # Relational Fields
    assigned_doctor = fields.Many2one("hms.doctors", string="Assigned Doctor")
    assigned_medicines = fields.Many2many(
        "hms.medicines", string="Assigned Medicines")

    # Computed Fields
    discounted_bill = fields.Float(
        string="Discounted Bill", compute="_get_discount")

    # Functions for Computed Field

    def generate_discount(self):
        bill_after_discount = 0

        if self.bill and self.discount_percentage:
            bill_after_discount = self.bill * \
                (1-(self.discount_percentage/100))

        return bill_after_discount

    def _get_discount(self):
        for item in self:
            item.discounted_bill = item.generate_discount()
