// Copyright (c) 2023, monir and contributors
// For license information, please see license.txt

frappe.ui.form.on("Purchase Order", {
	 refresh: function(frm) {
      frm.add_custom_button(__('Send WhatsApp'), function(){
      frappe.call({
        method: "purshase_order.purchase_order.doctype.purchase_order.purchase_order.send_telegram",
        args: {
          name:frm.doc.name,

        },
        callback: function(r) {
          frappe.throw(r.toSetString)
        }
      });    });
  }
});

frappe.ui.form.on('Purchase Order', {
    refresh: function(frm){
        // frappe.throw((frappe.session.user).toSetString())
        if (frappe.session.user !== "ahmad@gmail.com") {
            frm.toggle_enable("status", 0)
        } else {
            frm.toggle_enable("status", 1)
        }
        // frm.refresh_field('status');
    }
});
