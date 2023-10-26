
from __future__ import unicode_literals
import frappe


def after_install():
	frappe.get_doc({"doctype": "Role", "role_name": "Salesportal Admin"}).insert()
	frappe.get_doc({"doctype": "Role", "role_name": "Salesportal User","desk_access": 0}).insert()
	frappe.db.commit()
 