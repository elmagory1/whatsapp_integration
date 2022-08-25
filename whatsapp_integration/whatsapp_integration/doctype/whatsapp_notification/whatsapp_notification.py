# Copyright (c) 2022, Dexciss Technology Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
import json
import requests
from frappe.model.document import Document

class WhatsAppNotification(Document):
	def validate(self):
		url = "https://graph.facebook.com/v13.0/{0}?fields=id&access_token={1}".format(self.whatsapp_business_account_id,self.bearer_token)
		response = requests.request("GET", url)
		if response.status_code != 200:
			rc = json.loads(response.content)
			print(rc["error"]["message"])
			frappe.throw(rc["error"]["message"])
		
		else:
			frappe.msgprint("WhatsApp Account with Id - {0} Verified !".format(self.whatsapp_business_account_id))
	
	@frappe.whitelist()
	def get_variables(self):
		if self.whatsapp_template:
			temp = frappe.db.get_all("WhatsApp Variables",{"parent":self.whatsapp_template},["*"],order_by="idx")
			if temp:
				for values in temp:
					print("********************************88",values)
					self.append("variables",{
						"value":values.value,
						"field_name":values.field_name,
						"field_type":values.field_type
					
					})
					

