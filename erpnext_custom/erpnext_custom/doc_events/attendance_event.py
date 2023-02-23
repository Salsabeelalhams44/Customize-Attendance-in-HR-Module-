import frappe 
from frappe.utils import get_datetime, time_diff_in_hours
#@frappe.whitelist()

def validate_create_task(doc, method):
	if doc.status=='Left':
		task_doc=  frappe.new_doc("Task")
		task_doc.subject ="end of service "+ str(doc.employee_name)
		task_doc.employee_responsible=doc.employee_responsible_
		task_doc.insert()

def validate_show_task_in_calender(doc, method):
	event_doc=  frappe.new_doc("Event")
	event_doc.subject ="Subject of event "
	event_doc.starts_on=get_datetime().strftime('%Y-%m-%d %H:%M:%S')
	event_doc.event_type="Private"
	event_doc.insert()

# solution for task
def calculate_hours(doc,method):
	if doc.check_in and doc.check_out:
		#  frappe.msgprint(str(method))
		hours= time_diff_in_hours(doc.check_out,doc.check_in)
		doc.hours= float(hours)
	if not doc.check_in or  not doc.check_out:
		#frappe.msgprint(str(doc))
		doc.status='Absent'
