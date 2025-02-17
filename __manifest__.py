# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Droga Physioterapy ',
    'version' : '1',
    'summary': 'physio odoo erp',
    'sequence': 1,
    'description': """
Droga tranning on Odoo Development
====================
This module is not for production purpose it is used for train some droga staffs on how to develop on Odoo ERP system. this is basic
tutorial do not contain all""",
    'category': 'Physio',
    'website': 'https://www.drogapharma.com',
    'depends' : ['base_setup','hr'],
    
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/share.xml',
        'views/services.xml',
        # 'views/contracts.xml',
        'views/medical_certifcate.xml',
        'views/prescription_pdf.xml',
        'views/employee_contract.xml',
        # 'views/clinicians.xml',
        'report/report_template.xml',
        'views/investigation.xml',
        'views/appointment.xml',
        'views/examination.xml',
        'views/prescription.xml',



        # 'views/physio.xml',
        # 'views/physio_report.xml',
        # 'views/physio_report_template.xml',
    
        # 'views/prescription_report.xml',
        # 'views/prescription_report_template.xml',
    
        ],
    'installable': True,
    'application': True,
    'images': [
    'static/description/icon.png',
],
}
