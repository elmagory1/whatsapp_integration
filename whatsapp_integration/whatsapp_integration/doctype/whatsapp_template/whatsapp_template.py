# Copyright (c) 2022, Dexciss Technology Pvt. Ltd. and contributors
# For license information, please see license.txt

from email import header
import frappe
from pymysql import NULL
import requests
import json
import os

from frappe.model.document import Document

class WhatsappTemplate(Document):
	def before_save(self):
		fields = frappe.get_meta(self.doctype_name)
		print("shvhiiviuuiwhfuihiuohiuohv",fields)

		



	


	def before_submit(self):
		wts = frappe.get_doc("WhatsApp Settings")

		fields =[]
		for i in self.variables:
			full = "self" + "." + i.field_name
			fields.append(full)
		print(fields)

		
		

		


		
		url = "https://graph.facebook.com/v14.0/{0}/message_templates".format(wts.whatsapp_business_account_id)
		name= self.name.lower()
		category = self.category
		body_text = self.body_text
		header_text = self.text
		footer_text = self.footer_text

		lang = self.language.replace("-","_")
		components = []
		pld = {}
		body = {}
		header = {}
		footer = {}
		buttons = {}

		if self.category:
			pld.update({
				"category":self.category
			})
		else:
			frappe.throw("Please Mention Template Category")
		
		if self.body_text:
			body.update({
				"type":"BODY",
				"text":"{0}".format(body_text)
			})
			components.append(body)
		
		if self.header != "None":
			header.update({
				"type":"HEADER",
				"format":"TEXT",
				"text":"{0}".format(header_text),
				
			})
			components.append(header)
		
		if self.footer_text:
			footer.update({
				"type":"FOOTER",
				"text":"{0}".format(footer_text)
			})
			components.append(footer)
		
		if self.button_type in ("Call to Action","Quick Reply"):
			if self.button_type == "Call to Action":
				ph = self.dial_code + "" + self.phone_number
				
				buttons.update({
					"type":"BUTTONS",
					"buttons":[{"type":"PHONE_NUMBER","text":self.button_text,"phone_number":ph}]
						
				})
				components.append(buttons)
		
		
		
		
		print("924244145145154",components)
		pld.update({"components":components})
		pld.update({
			"name":"{0}".format(name),
			"language":"{0}".format(lang)
		})
		


		

					

				
			
			

		



		
	
		payload = json.dumps(pld)
		headers = {
		'Content-Type': 'application/json',
		'Authorization': 'Bearer {0}'.format(wts.bearer_token)
		}

		response =requests.request("POST", url, headers=headers, data=payload)
		rc = json.loads(response.content)
		print(rc)
		if response.status_code != 200:
			
			frappe.throw(rc["error"]["error_user_msg"])
		else:
			frappe.msgprint("Template Created With Id - {0} ".format(name))

		

		
	


@frappe.whitelist()
def get_list(docname):
	print(docname)
	docfields = {
		
	}
	for row in frappe.get_all('DocField', fields = ['fieldname','label','fieldtype'],
		filters = {'parent': docname, 'fieldtype': ["not in",["Column Break","Section Break","Table"]]}):

		docfields.update({
			row.label:[row.fieldname,row.fieldtype]
		})
	
	return docfields
	


		






			
			
		

		