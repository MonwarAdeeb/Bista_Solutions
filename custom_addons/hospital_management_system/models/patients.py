from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError
from datetime import datetime
import re


class Patients(models.Model):
    _name = "hms.patients"
    _description = "Features for Patients"
    _rec_name = "name"

    # General Fields
    photo = fields.Binary(string="Photo", attachment=True)
    name = fields.Char(string="Patient's Name", required=True,
                       help="Enter Your Name Here")
    age = fields.Integer(string="Age", required=True)
    patient_id = fields.Char(string="Patient ID", required=True)
    date_of_admission = fields.Datetime(
        string="Date of Admission", default=datetime.now())
    symptoms = fields.Text(string="Symptoms")
    diagnosis = fields.Text(string="Diagnostics")
    bill = fields.Float(string="Due Bill")
    discount_given = fields.Boolean()
    discount_percentage = fields.Float(string="Discount Percentage")
    address = fields.Text(string="Address")
    contact_number = fields.Char(string="Contact Number")
    email = fields.Char(string="Email")

    # Relational Fields to See Assigned Doctor and Assigned Medicines
    assigned_doctor = fields.Many2one("hms.doctors", string="Assigned Doctor")
    assigned_medicines = fields.Many2many(
        "hms.medicines", string="Assigned Medicines")

    # Computed Fields : To Calculate Discounted Bill
    discounted_bill = fields.Float(
        string="Discounted Bill", compute="_get_discount")

    # Functions called by _get_discount to calculate discounted Bill
    def generate_discount(self):
        bill_after_discount = 0

        if self.bill and self.discount_percentage:
            bill_after_discount = self.bill * \
                (1-(self.discount_percentage/100))

        return bill_after_discount

    # Internal Function to Generate Discounted Field [that call another function for better encapsulation]
    def _get_discount(self):
        for item in self:
            item.discounted_bill = item.generate_discount()

    # API Decorators

    # Email Validation using Onchance
    @api.onchange('email')
    def validate_email(self):
        if self.email:
            match = re.match(
                '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
            if match == None:
                raise ValidationError('Please Enter a Valid E-mail ID')

    # Address Field Manipulation using Create
    @api.model
    def create(self, values):
        if not values['address']:
            values['address'] = "Not Provided"
        return super(Patients, self).create(values)

    # Address Field Manipulation using Write
    def write(self, values):
        if 'address' in values.keys() and not values['address']:
            values['address'] = "Address Was Deleted"
        return super(Patients, self).write(values)


# Class to Filter Patients' Admission Dates
class PatientsAdmissionDatesFilter(models.TransientModel):
    _name = "hms.patients.admission.dates.filter"
    _description = "Features for Filtering Patient's Admission Date"

    # General Date Fields to Select Dates in Form
    from_date = fields.Date(
        string='Date From', default=datetime.today())
    to_date = fields.Date(
        string='Date To', default=datetime.today())

    # Function to Filter Admission Dates and Return View
    def filter_patients_admission_dates(self):
        # Empty lists to store filtered dates later
        # filtered_dates = []
        filtered_dates_ids = []

        # filtering dates from database
        filtered_dates = self.env["hms.patients"].search(
            ['&', ('date_of_admission', '>=', self.from_date), ('date_of_admission', '<=', self.to_date)])

        # Retrieving IDs of Filtered Dates
        for date in filtered_dates:
            filtered_dates_ids.append(date.id)

        # Passing ids to the default views of the class
        return{
            "name": "Patients' Admission Date Filter",
            "type": "ir.actions.act_window",
            "res_model": "hms.patients",
            "view_mode": "tree,form",
            "domain": [("id", "in", filtered_dates_ids)],
        }
