import frappe 

@frappe.whitelist()

def validate_add_remarks(doc, method):
	items=""
	for item in doc.get("items"):
		items = str(items)+ " "+str(item.item_code)
	doc.remarks= str(items)


def validate_add_notes_to_remarks(doc, method):
	items=""
	for item in doc.get("items"):
		items = str(items)+ " "+str(item.note_field_custom)
	doc.remarks= str(items)


def validate_payments(doc, method):
	if doc.is_pos:
		payments = doc.get("payments")
		if payments:
			for payment in payments:
				if payment.amount == 0:
					frappe.throw("Payment cannot be zero.")
		else:
			frappe.throw("No payment found on document.")

def validate_sales_invoice(doc, method):
	validate_add_notes_to_remarks(doc, method)
	validate_payments(doc, method)
