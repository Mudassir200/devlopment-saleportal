import frappe

@frappe.whitelist(allow_guest=True)
def get_project_filter():
    realestate_project = frappe.db.sql("""SELECT DISTINCT project.name,project.project_name FROM `tabRealestate Property` property LEFT JOIN `tabRealestate Project` project ON property.project_id = project.name WHERE property.property_status IN ('Reserved','Available')""",as_dict=1)
    
    return { "realestate_project":realestate_project }