// Copyright (c) 2022, Dexciss Technology Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('WhatsApp Notification', {
	whatsapp_template: function(frm) {
		if(frm.doc.whatsapp_template){
			frappe.call({
				method:"get_variables",
				doc:frm.doc,
				callback:function(frm){
					console.log("22222222222222222222222")
					cur_frm.refresh_field("variables")
					
				}
			})
		}
		
	},


});

window.addEventListener('beforeunload', function (e) {
    e.preventDefault();
	console.log(e)
    e.returnValue = '';
});
