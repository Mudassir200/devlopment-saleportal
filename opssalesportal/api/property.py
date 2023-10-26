import frappe


@frappe.whitelist()
def get_property_details(property):
    propertydetails = frappe.get_doc('Realestate Property', property)
    projectdetails = frappe.get_doc('Realestate Project', propertydetails.project_id)
    return {"propertydetails":propertydetails,"projectdetails":projectdetails}

