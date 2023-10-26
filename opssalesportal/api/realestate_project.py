import frappe
import json
from datetime import date,timedelta

@frappe.whitelist()
def get_home_filter():
    sql="""SELECT DISTINCT project.name as value,project.project_name as label
        FROM `tabRealestate Property` property 
        LEFT JOIN `tabRealestate Project` project 
        ON property.project_id = project.name 
        WHERE property.property_status IN ('Reserved','Available') AND project.status = 'Active' AND property.status = 'Active'"""
    
    total="""SELECT COUNT(DISTINCT project.name) as total , MIN(property.total_price) as min , MAX(property.total_price) as max
        FROM `tabRealestate Property` property 
        LEFT JOIN `tabRealestate Project` project 
        ON property.project_id = project.name 
        WHERE property.property_status IN ('Reserved','Available') AND project.status = 'Active' AND property.status = 'Active'"""
    

    property_type = frappe.db.get_all('Property Type',
        filters={
            "active": 1
        },
        pluck="property_type"
    )

    state = frappe.db.get_all('State',
        filters={
            "active": 1
        },
        pluck="state_name"
    )

    agent = frappe.db.get_all('Vendor',
        filters={
            "vendor_group": "Agent"
        },
        fields=['vendor_name', 'name']
    )

    realestate_project = frappe.db.sql(sql,as_dict=1)
    extra = frappe.db.sql(total,as_dict=1)
    
    return { "projects":realestate_project, "propertyTypes":property_type,"states":state, "agents":agent, **extra[0] }

@frappe.whitelist()
def get_project_vendor_details(agent=None,developer=None,builder=None):
    details = {}
    if agent:
        details['agentDetails'] = frappe.get_doc('Vendor', agent)
    if developer:
        details['developerDetails'] = frappe.get_doc('Vendor', developer)
    if builder:
        details['builderDetails'] = frappe.get_doc('Vendor', builder)
    
    return { **details } 
 
@frappe.whitelist()
def get_project_details(project):
    projectdetails = frappe.get_doc('Realestate Project', project)

    sql="""SELECT (SELECT MIN(pro.total_price)
        FROM `tabRealestate Property` pro
        WHERE pro.project_id = project.name AND pro.property_status IN ('Reserved','Available')) AS minPrice,
        (SELECT MAX(pro.total_price)  
        FROM `tabRealestate Property` pro
        WHERE pro.project_id = project.name AND pro.property_status IN ('Reserved','Available')) AS maxPrice,
        (SELECT AVG(pro.bedrooms)  
        FROM `tabRealestate Property` pro
        WHERE pro.project_id = project.name AND pro.property_status IN ('Reserved','Available')) AS bedrooms,
        (SELECT AVG(pro.bathrooms)  
        FROM `tabRealestate Property` pro
        WHERE pro.project_id = project.name AND pro.property_status IN ('Reserved','Available')) AS bathrooms,
        (SELECT AVG(pro.included_carparks)  
        FROM `tabRealestate Property` pro
        WHERE pro.project_id = project.name AND pro.property_status IN ('Reserved','Available')) AS carparks,
        (SELECT COUNT(DISTINCT pro.name)  
        FROM `tabRealestate Property` pro
        WHERE pro.project_id = project.name AND pro.property_status IN ('Available')) AS availabel,
        (SELECT COUNT(DISTINCT pro.name)  
        FROM `tabRealestate Property` pro
        WHERE pro.project_id = project.name AND pro.property_status IN ('Reserved')) AS reserved,
        (SELECT COUNT(DISTINCT pro.name)  
        FROM `tabRealestate Property` pro
        WHERE pro.project_id = project.name AND pro.property_status IN ('Sold')) AS sold,
        (SELECT COUNT(pro.name)  
        FROM `tabRealestate Property` pro
        WHERE pro.project_id = project.name AND pro.status IN ('Active')) AS totalAllocation
        FROM `tabRealestate Project` project 
        LEFT JOIN `tabRealestate Property` property         
        ON project.name = property.project_id
        WHERE project.status = 'Active' AND property.status = 'Active'"""

    sql += ' AND project.name = "{0}"'.format(project)

    summury = frappe.db.sql(sql,as_dict=1)
    return { "projectdetails":projectdetails,**summury[0]}

@frappe.whitelist()
def get_stage_project(project):
    sql="""SELECT DISTINCT project.*,
        (SELECT MIN(pro.total_price)
        FROM `tabRealestate Property` pro
        WHERE pro.project_id = project.name AND pro.property_status IN ('Reserved','Available')) AS minPrice,
        (SELECT MAX(pro.total_price)  
        FROM `tabRealestate Property` pro
        WHERE pro.project_id = project.name AND pro.property_status IN ('Reserved','Available')) AS maxPrice,
        (SELECT AVG(pro.bedrooms)  
        FROM `tabRealestate Property` pro
        WHERE pro.project_id = project.name AND pro.property_status IN ('Reserved','Available')) AS bedrooms,
        (SELECT AVG(pro.bathrooms)  
        FROM `tabRealestate Property` pro
        WHERE pro.project_id = project.name AND pro.property_status IN ('Reserved','Available')) AS bathrooms,
        (SELECT COUNT(pro.name)  
        FROM `tabRealestate Property` pro
        WHERE pro.project_id = project.name AND pro.property_status IN ('Available')) AS available,
        (SELECT COUNT(pro.name)  
        FROM `tabRealestate Property` pro
        WHERE pro.project_id = project.name AND pro.status IN ('Active')) AS totalAllocation,
        (SELECT vendor.vendor_name  
        FROM `tabVendor` vendor
        WHERE vendor.name = project.builder) AS builder
        FROM `tabRealestate Project` project 
        LEFT JOIN `tabRealestate Property` property         
        ON project.name = property.project_id
        WHERE project.status = 'Active' AND property.status = 'Active'"""

    sql += ' AND parent_project_id = "{0}" AND realestate_type = "Stage"'.format(project)

    stageprojects = frappe.db.sql(sql,as_dict=1)

    return stageprojects

@frappe.whitelist(methods=['POST'])
def get_project_properties(project,filter=None):
    stageProjects = frappe.db.get_all('Realestate Project',
        filters={
            "status": "Active",
            "parent_project_id": project,
            "realestate_type": "Stage",
        },
        pluck="name"
    )
  
    sql="""SELECT DISTINCT property.*, project.project_enddate, project.stage, project.title_date FROM `tabRealestate Property` property LEFT JOIN  `tabRealestate Project` project ON property.project_id=project.name WHERE property.status = 'Active'"""
    total="""SELECT COUNT(DISTINCT property.name) as total FROM `tabRealestate Property` property LEFT JOIN  `tabRealestate Project` project ON property.project_id=project.name WHERE property.status = 'Active'"""

    
    filterColumns = ""
    #filterColumns = ["stage","from","to","titlewithin","contract_type","min","max","bathroom","bedroom","property_status"];
    filterColumns += ' AND (property.project_id = "{0}"'.format(project)
    for stageProject in stageProjects:
        filterColumns += ' OR property.project_id = "{0}"'.format(stageProject)

    filterColumns += ')'


    if filter :
        filters = filter
        if "stage" in filters.keys():
            filterColumns += ' AND project.stage = "{0}"'.format(filters['stage'])
        if "from" in filters.keys():
            filterColumns += ' AND project.project_enddate >= "{0}"'.format(filters['from'])
        if "to" in filters.keys():
            filterColumns += ' AND project.project_enddate <= "{0}"'.format(filters['to'])
        if "titlewithin" in filters.keys():
            enddate = (date.today()+timedelta(days=90)).isoformat()
            filterColumns += ' AND (project.title_status = "Titled" OR project.title_date < "{0}")'.format(enddate)
        if "contract_type" in filters.keys():
            filterColumns += ' AND property.contract_type = "{0}"'.format(filters['contract_type'])
        if "min" in filters.keys():
            filterColumns += ' AND property.total_price >= {0}'.format(filters['min'])
        if "max" in filters.keys():
            filterColumns += ' AND property.total_price <= {0}'.format(filters['max'])
        if "bathroom" in filters.keys():
            if filters['bathroom'].find('+') == -1:
                filterColumns += ' AND property.bathrooms >= {0}'.format(filters['bathroom'].replace('+', ''))
            else:
                filterColumns += ' AND property.bathrooms = {0}'.format(filters['bathroom'])
        if "bedroom" in filters.keys():
            if filters['bedroom'].find('+') == -1:
                filterColumns += ' AND property.bedrooms >= {0}'.format(filters['bedroom'].replace('+', ''))
            else:
                filterColumns += ' AND property.bedrooms = {0}'.format(filters['bedroom'])
        if "property_status" in filters.keys():    
            property_status = ""
            if is_array(filters['property_status']) > 0:
                for status in filters['property_status']:
                    if property_status == "":
                        property_status += ' AND ( property.property_status = "{0}"'.format(status)
                    else:
                        property_status += ' OR property.property_status = "{0}"'.format(status)
                property_status += ')'
                filterColumns += property_status    
    else:
        filterColumns += ' AND property.property_status IN ("Reserved","Available")'

    sql+= filterColumns
    total+= filterColumns

    properties = frappe.db.sql(sql,as_dict=1)
    totals = frappe.db.sql(total,as_dict=1)

    return {"properties":properties,**totals[0]}

@frappe.whitelist(methods=['POST'])
def get_project_list(filter=None,sort='name',order='ASC',limit=20,start_index=0):
    sql="""SELECT DISTINCT project.*,
        (SELECT MIN(pro.total_price)
        FROM `tabRealestate Property` pro
        WHERE pro.project_id = project.name AND pro.property_status IN ('Reserved','Available')) AS minPrice,
        (SELECT MAX(pro.total_price)  
        FROM `tabRealestate Property` pro
        WHERE pro.project_id = project.name AND pro.property_status IN ('Reserved','Available')) AS maxPrice,
        (SELECT AVG(pro.bedrooms)  
        FROM `tabRealestate Property` pro
        WHERE pro.project_id = project.name AND pro.property_status IN ('Reserved','Available')) AS bedrooms,
        (SELECT AVG(pro.bathrooms)  
        FROM `tabRealestate Property` pro
        WHERE pro.project_id = project.name AND pro.property_status IN ('Reserved','Available')) AS bathrooms,
        (SELECT AVG(pro.included_carparks)  
        FROM `tabRealestate Property` pro
        WHERE pro.project_id = project.name AND pro.property_status IN ('Reserved','Available')) AS carparks,
        (SELECT COUNT(DISTINCT pro.name)  
        FROM `tabRealestate Property` pro
        WHERE pro.project_id = project.name AND pro.property_status IN ('Available')) AS available,
        (SELECT COUNT(DISTINCT pro.name)  
        FROM `tabRealestate Property` pro
        WHERE pro.project_id = project.name AND pro.property_status IN ('Reserved')) AS reserved,
        (SELECT vendor.image 
        FROM `tabVendor` vendor
        WHERE vendor.name = project.agent) AS vendorProfile
        FROM `tabRealestate Property` property 
        LEFT JOIN `tabRealestate Project` project 
        ON property.project_id = project.name 
        WHERE project.status = 'Active' AND property.status = 'Active'"""

    
    column="""SHOW COLUMNS FROM `tabRealestate Project`"""
    projectColumns = frappe.db.sql(column,as_dict=1)
    column="""SHOW COLUMNS FROM `tabRealestate Project`"""
    propertyColumns = frappe.db.sql(column,as_dict=1)

    #filterColumns = ["project","realestate_type","property_type","contract_type","agent","state","titlewithin","construction_started","from","to","min","max","bathroom","bedroom","carparks","available","min_yield","is_featured"];
    # return filter['project']
    filterColumns = ""
    if filter:
        if "available" in filter.keys():
            if filter['available'] == "yes" or filter['available'] == "1":
                filterColumns += ' AND property.property_status = "Available"'
            
        if filterColumns == "":
            filterColumns += ' AND property.property_status IN ("Reserved","Available")'
        if "project" in filter.keys():
            filterColumns += ' AND project.name = "{0}"'.format(filter['project'])
        if "realestate_type" in filter.keys():
            filterColumns += ' AND project.realestate_type = "{0}"'.format(filter['realestate_type'])
        if "property_type" in filter.keys():
            filterColumns += ' AND project.property_type = "{0}"'.format(filter['property_type'])
        if "agent" in filter.keys():
            filterColumns += ' AND project.agent = "{0}"'.format(filter['agent'])
        if "state" in filter.keys():
            filterColumns += ' AND project.state = "{0}"'.format(filter['state'])
        if "from" in filter.keys():
            filterColumns += ' AND project.project_enddate >= "{0}"'.format(filter['from'])
        if "to" in filter.keys():
            filterColumns += ' AND project.project_enddate <= "{0}"'.format(filter['to'])
        if "titlewithin" in filter.keys():
            enddate = (date.today()+timedelta(days=90)).isoformat()
            filterColumns += ' AND (project.title_status = "Titled" OR project.title_date < "{0}")'.format(enddate)
        if "construction_started" in filter.keys():
            if "construction_started" == '1':
                filterColumns += ' AND project.project_startdate <= {0}'.format(date.today())
            else:
                filterColumns += ' AND project.project_startdate > {0}'.format(date.today())
        if "contract_type" in filter.keys():
            filterColumns += ' AND property.contract_type = "{0}"'.format(filter['contract_type'])
        if "min" in filter.keys():
            filterColumns += ' AND property.total_price >= {0}'.format(filter['min'])
        if "max" in filter.keys():
            filterColumns += ' AND property.total_price <= {0}'.format(filter['max'])
        if "bathroom" in filter.keys():
            if filter['bathroom'].find('+') == -1:
                filterColumns += ' AND property.bathrooms >= {0}'.format(filter['bathroom'].replace('+', ''))
            else:
                filterColumns += ' AND property.bathrooms = {0}'.format(filter['bathroom'])
        if "bedroom" in filter.keys():
            if filter['bedroom'].find('+') == -1:
                filterColumns += ' AND property.bedrooms >= {0}'.format(filter['bedroom'].replace('+', ''))
            else:
                filterColumns += ' AND property.bedrooms = {0}'.format(filter['bedroom'])
        if "carparks" in filter.keys():
            if filter['carparks'] == "3+":
                filterColumns += ' AND property.included_carparks >= 3'
            else:
                filterColumns += ' AND property.included_carparks = {0}'.format(filter['carparks'])
        if "min_yield" in filter.keys():
            filterColumns += ' AND property.rental_yield >= {0}'.format(filter['min_yield'])
        if "is_featured" in filter.keys():
            filterColumns += ' AND property.is_featured = 1'
    else:
        filterColumns += ' AND property.property_status IN ("Reserved","Available")'
    

    sql+= filterColumns

    sortvalid = False
    ordervalid = False
    orderValidOption = ['asc','desc']
    if sort == None:
        sortvalid=True
    else:
        for column in projectColumns:
            if column.Field == sort:
                sortvalid = True

    if sort == None:
        sortvalid=True
        sort = "name"


    if order == None:
        ordervalid=True
    else:
        if order.lower() in orderValidOption:
            ordervalid = True
            order = order.upper()
        else:
            ordervalid=True
            order = "ASC"


    if sortvalid and ordervalid:
        if(sort and order):
            sql+= " ORDER BY "+sort+" "+order
        elif sort:
            sql+= " ORDER BY "+sort+" ASC"
        elif order:
            sql+= " ORDER BY name "+order
        else:
            sql+= " ORDER BY name ASC"
    

    if(int(start_index) >= 0):
        sql+= " LIMIT {0},".format(start_index)
    else:
        sql+= " LIMIT 0,"

    if(int(limit) <= 100):
        sql+= "{0}".format(limit)
    else:
        sql+= "20"


    total="""SELECT COUNT(DISTINCT project.name) as total FROM `tabRealestate Property` property  LEFT JOIN `tabRealestate Project` project  ON property.project_id = project.name  WHERE project.status = 'Active' AND property.status = 'Active'"""

    total+= filterColumns

    totals = frappe.db.sql(total,as_dict=1)
    realestate_project = frappe.db.sql(sql,as_dict=1)

    return { "projects":realestate_project,**totals[0] }


@frappe.whitelist(allow_guest=True)
def get_properties_filter(project):
    stageProjects = frappe.db.get_all('Realestate Project',
        filters={
            "status": "Active",
            "parent_project_id": project,
            "realestate_type": "Stage",
        },
        pluck="name"
    )    

    filterColumns = ""
    filterColumns += ' AND (property.project_id = "{0}"'.format(project)
    for stageProject in stageProjects:
        filterColumns += ' OR property.project_id = "{0}"'.format(stageProject)

    filterColumns += ')'

    sql="""SELECT COUNT(DISTINCT property.name) as total , MIN(property.total_price) as min , MAX(property.total_price) as max
        FROM `tabRealestate Property` property 
        LEFT JOIN `tabRealestate Project` project 
        ON property.project_id = project.name 
        WHERE project.status = 'Active' AND property.status = 'Active'"""

    sql+= filterColumns
    
    property_status = frappe.db.get_all('Property Status',
        filters={
            "active": 1,
        },
        pluck="status"
    )
    
    stages = frappe.db.get_all('Realestate Project',
        filters={
            "status": "Active",
            "parent_project_id": project,
            "realestate_type": "Stage",
        },
        pluck="stage"
    )

    extra = frappe.db.sql(sql,as_dict=1)

    return {**extra[0],"property_status":property_status,"stages":stages}


def is_json(myjson):
  try:
    json.loads(myjson)
  except ValueError as e:
    return False
  return True


def is_array(arr):
  try:
    return len(arr)
  except ValueError as e:
    return False


