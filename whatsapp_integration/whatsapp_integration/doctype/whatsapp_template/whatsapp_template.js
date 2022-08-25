// Copyright (c) 2022, Dexciss Technology Pvt. Ltd. and contributors
// For license information, please see license.txt

var count = 0;
frappe.ui.form.on('Whatsapp Template', {
	doctype_name: function(frm) {
		console.log("BEFORE")
		var el = [];
		var fields1=[];
		// frappe.model.with_doctype(frm.doc.doctype_name, () => {
		// 	frappe.get_meta(frm.doc.doctype_name).fields.map(df => {
		// 		console.log(df)
		// 		// el.push(df.label)
		// 		// fields1.push({label:df.fieldname})


		// 	})
		// })
		// console.log("el",el)

		
		var labels = []
		frappe.call({
			method:"whatsapp_integration.whatsapp_integration.doctype.whatsapp_template.whatsapp_template.get_list",
			args:{
				"docname":frm.doc.doctype_name
			},
			callback:function(r){
				if(r.message){
					fields1.push(r.message)
					labels = Object.keys(fields1[0])
					console.log("labels",labels)
					frm.fields_dict.variables.grid.update_docfield_property(
						'value',
						'options',
						[""].concat(labels)

						);
				}



			}
			
		})
		
		
		
		
		// frm.set_df_property('lablist', 'options', fields1.label);
		
	}
});

frappe.ui.form.on("WhatsApp Variables",{
	value:function(frm,cdt,cdn){
		let child = locals[cdt][cdn]
		var fields2 = [];
		if(frm.doc.doctype_name){
			frappe.call({
				method:"whatsapp_integration.whatsapp_integration.doctype.whatsapp_template.whatsapp_template.get_list",
				args:{
					"docname":frm.doc.doctype_name
				},
				callback:function(r){
					if(r.message){
						fields2.push(r.message)
						for (const [key, value] of Object.entries(fields2[0])) {
							console.log(key, value);
							if(child.value == key){
								frappe.model.set_value(cdt,cdn,"field_name",value[0])
								frappe.model.set_value(cdt,cdn,"field_type",value[1])
							}
						  }
						  
					}
	
	
	
				}
				
			})

			// frm.fields_dict.vaiables.grid.update_docfield_property(
			// 	'value',
			// 	'options',
			// 	Object.keys(fields1[0])
			// 	);
		}
	}
	
})
