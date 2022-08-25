from email import header
from posixpath import abspath
import frappe
from pymysql import NULL
import requests
import json

def on_submit(self,method):
    wt = frappe.db.get_all("WhatsApp Notification",{"doctype_name":self.doctype,"enabled":1},["*"])
    params = []
    vb_list = []
    vrb = {}
    types = []
    values = []
    



    if wt:
        print("555555555555555555555555555555555555555555555",wt)
        wpid = ""
        btoken = ""
        wtemplate = ""
        body = ""
        var = ""

        for i in wt:
            print("6666666666666666666666666666666666666666666666",i)

            wpid = i.whatsapp_phone_number_id
            btoken = i.bearer_token
            wtemplate = i.whatsapp_template
            body = i.body_text

            ct = frappe.db.get_all("WhatsApp Variables",{"parent":i.name},["*"],order_by='idx')
            
            for k in ct:
                print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",k)
                # vrb.update({
                #     "type":k.field_type,
                #     "name":k.field_name
                # })
                vb_list.append({
                    "type": k.field_type,
                    "name" : k.field_name
                })

        print("7777777777777777777777777777777777777",vb_list)
        for i in vb_list:
            print("514561561515615616151531",i)
            if i.get("type") == "Data":
                
                i.update({
                    "type":"text",
                    "text":frappe.db.get_value(self.doctype,{"name":self.name},[i.get("name")])
                })
                del i["name"]
            
            if i.get("type") == "Currency":
                print("yes***************************")
                
                i.update({
                    "type":"currency",
                    "currency":{
                        "fallback_value":frappe.db.get_value(self.doctype,{"name":self.name},[i.get("name")]),
                        "code":frappe.db.get_value(self.doctype,{"name":self.name},["currency"]),
                        "amount_1000":1000*frappe.db.get_value(self.doctype,{"name":self.name},[i.get("name")])

                    }
                })
                del i["name"]
            
            params.append(i)
            print("999999999999999999999999999999999999999999999999999999",params)

                    
                    


    
    
    

            

     
#     obj = "self.customer"

#     print(obj.replace('"',''))

        url = "https://graph.facebook.com/v13.0/{0}/messages".format(wpid)

        
        payload = json.dumps({
                    "recipient_type": "individual",
                    "to": "917276603390",
                    "type": "template",
                    "messaging_product":"whatsapp",
                    "template": {
                            "name": wtemplate.lower(),
                            "language": {
                                "code": "en_GB"
                            },
                            "components": [{
                                "type": "body",
                                "parameters": params
                            }]
                        }
    })
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {0}'.format(btoken)
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.content)
    
        print("924215156115161561651",params)

    

    
        url2 = "https://graph.facebook.com/v14.0/{0}/messages".format(wpid)

        payload2 = json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": "917276603390",
        "type": "document",
        "document": {
            "link": "https://www.clickdimensions.com/links/TestPDFfile.pdf",
            "caption": "Invoice"
        }
        })
        headers2 = {
        'Authorization': 'Bearer {0}'.format(btoken),
        'Content-Type': 'application/json'
        }

        response2 = requests.request("POST", url2, headers=headers2, data=payload2)

        print("22222222222222222222222222222222222222222",response2.content)
                    

                    
                   

                    




    


        