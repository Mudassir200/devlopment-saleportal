from . import __version__ as app_version

app_name = "opssalesportal"
app_title = "Opssalesportal"
app_publisher = "Oappsit"
app_description = "Sales Portal"
app_email = "oappsit@gmail.com"
app_license = "MIT"
# app_icon_url = "/assets/opssalesportal/frontend/logo.png"
app_icon_route = "/s"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/opssalesportal/css/opssalesportal.css"
# app_include_js = "/assets/opssalesportal/js/opssalesportal.js"

# include js, css files in header of web template
# web_include_css = "/assets/opssalesportal/css/opssalesportal.css"
# web_include_js = "/assets/opssalesportal/js/opssalesportal.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "opssalesportal/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

website_route_rules = [
	{"from_route": "/s/<path:app_path>", "to_route": "s"},    
]

website_redirects = [
	{"source": "/", "target": "/s"},
	{"source": "/login", "target": "/s/login"},
	{"source": "/app", "target": "/app/private/sales-portal"}
]
# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "opssalesportal.utils.jinja_methods",
#	"filters": "opssalesportal.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "opssalesportal.install.before_install"
after_install = "opssalesportal.setup.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "opssalesportal.uninstall.before_uninstall"
# after_uninstall = "opssalesportal.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "opssalesportal.utils.before_app_install"
# after_app_install = "opssalesportal.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "opssalesportal.utils.before_app_uninstall"
# after_app_uninstall = "opssalesportal.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "opssalesportal.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

on_login = 'opssalesportal.www.s.on_login'

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"opssalesportal.tasks.all"
#	],
#	"daily": [
#		"opssalesportal.tasks.daily"
#	],
#	"hourly": [
#		"opssalesportal.tasks.hourly"
#	],
#	"weekly": [
#		"opssalesportal.tasks.weekly"
#	],
#	"monthly": [
#		"opssalesportal.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "opssalesportal.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "opssalesportal.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "opssalesportal.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["opssalesportal.utils.before_request"]
# after_request = ["opssalesportal.utils.after_request"]

# Job Events
# ----------
# before_job = ["opssalesportal.utils.before_job"]
# after_job = ["opssalesportal.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"opssalesportal.auth.validate"
# ]
