from . import __version__ as app_version

app_name = "whatsapp_integration"
app_title = "Whatsapp Integration"
app_publisher = "Dexciss Technology Pvt. Ltd."
app_description = "Integration Of Whatsapp Services into ERPNext System"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "nmistry@dexciss.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/whatsapp_integration/css/whatsapp_integration.css"
# app_include_js = "/assets/whatsapp_integration/js/whatsapp_integration.js"

# include js, css files in header of web template
# web_include_css = "/assets/whatsapp_integration/css/whatsapp_integration.css"
# web_include_js = "/assets/whatsapp_integration/js/whatsapp_integration.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "whatsapp_integration/public/scss/website"

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

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "whatsapp_integration.install.before_install"
# after_install = "whatsapp_integration.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "whatsapp_integration.uninstall.before_uninstall"
# after_uninstall = "whatsapp_integration.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "whatsapp_integration.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Sales Order": {
		"on_submit": "whatsapp_integration.api.on_submit",
		
	},
	# "*":{
	# 	"validate":"whatsapp_integration.api.on_submit"
	# }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"whatsapp_integration.tasks.all"
# 	],
# 	"daily": [
# 		"whatsapp_integration.tasks.daily"
# 	],
# 	"hourly": [
# 		"whatsapp_integration.tasks.hourly"
# 	],
# 	"weekly": [
# 		"whatsapp_integration.tasks.weekly"
# 	]
# 	"monthly": [
# 		"whatsapp_integration.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "whatsapp_integration.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "whatsapp_integration.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "whatsapp_integration.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"whatsapp_integration.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []
