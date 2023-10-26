# Copyright (c) 2023, Oappsit and contributors
# For license information, please see license.txt

# import frappe
import json

import frappe
import frappe.defaults
from frappe import _, msgprint, qb

from frappe.model.document import Document
from frappe.contacts.address_and_contact import (
	delete_contact_and_address,
	load_address_and_contact,
)

class Customer(Document):
	def onload(self):
		"""Load address and contacts in `__onload`"""
		load_address_and_contact(self)

	def link_lead_address_and_contact(self):
		if self.lead_name:
			# assign lead address and contact to customer (if already not set)
			linked_contacts_and_addresses = frappe.get_all(
				"Dynamic Link",
				filters=[
					["parenttype", "in", ["Contact", "Address"]],
					["link_doctype", "=", "Lead"],
					["link_name", "=", self.lead_name],
				],
				fields=["parent as name", "parenttype as doctype"],
			)

			for row in linked_contacts_and_addresses:
				linked_doc = frappe.get_doc(row.doctype, row.name)
				if not linked_doc.has_link("Customer", self.name):
					linked_doc.append("links", dict(link_doctype="Customer", link_name=self.name))
					linked_doc.save(ignore_permissions=self.flags.ignore_permissions)
