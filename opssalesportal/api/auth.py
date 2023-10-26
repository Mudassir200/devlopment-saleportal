import frappe
from frappe import auth
from frappe.sessions import Session, clear_sessions, delete_session

@frappe.whitelist( allow_guest=True )
def login(usr, pwd):
    try:
        login_manager = frappe.auth.LoginManager()
        login_manager.authenticate(user=usr, pwd=pwd)
        login_manager.post_login()
    except frappe.exceptions.AuthenticationError:
        frappe.clear_messages()
        frappe.local.response["message"] = {
            "success_key":0,
            "message":"Authentication Error!"
        }

        return

    user = frappe.get_doc('User', frappe.session.user)
    
    if frappe.session.user:
       return checkRolePermission(user, login_manager)

    
def checkRolePermission(user, login_manager):
    is_login = 0
    validUserRoles = ["Salesportal User" ,"Salesportal Admin"]
    if len(user.roles) > 0:
      for role in user.roles:
        if role.get("role") in validUserRoles:
            is_login = 1
    else:
        is_login = 0
    
    if(is_login == 1):
      frappe.local.response["message"] = {
        "success_key":1,
        "message":"Authentication success",
        "sid":frappe.session.sid,
        "username":user.username,
        "user_id":user.name,        
        "email":user.email,
        "user":user,
        "is_login":user.roles
      }
    else:
        delete_session(frappe.session.sid, user=frappe.session.user, reason="User has permission denied!")
        message  = user.name + " user has permission denied!"
        login_manager.clear_cookies()  
        frappe.clear_messages()
        frappe.local.response["message"] = {
            "success_key":0,
            "message": message
        }
    
    return
       

@frappe.whitelist()
def get_user_info():
    user = frappe.get_doc('User', frappe.session.user)
    return user


@frappe.whitelist()
def create_roles():
    doc = frappe.new_doc('Role')
    doc.role_name = "Test 10"
    doc.desk_access = 0
    doc.insert()
    frappe.db.commit()
    return doc