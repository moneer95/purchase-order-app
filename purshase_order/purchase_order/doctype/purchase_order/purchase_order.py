# Copyright (c) 2023, monir and contributors
# For license information, please see license.txt
import asyncio
import frappe
from frappe.model.document import Document
import telegram
from weasyprint import HTML
from io import BytesIO


class PurchaseOrder(Document):
    pass


# Get the HTML content of the print format for a specific document
def get_print_format(name):
    return frappe.get_print(doctype="Purchase Order", name=name, print_format="format builder PO")


# @frappe.whitelist()
# def send_email(name, subject, message):
#     html_content = get_print_format(name)
#     pdf_content = HTML(string=html_content).write_pdf()
#
#     attachment = [{
#         "fname": f'{name}.pdf',
#         "fcontent": pdf_content
#     }]
#     frappe.sendmail(recipients='mnyrskyk@gmail.com', subject=subject, message=message, attachments=attachment)
#     frappe.msgprint("email sent!")
@frappe.whitelist()
def send_telegram(name):
    frappe.msgprint("1")
    html_content = get_print_format(name)
    pdf_content = HTML(string=html_content).write_pdf()
    pdf_file = BytesIO(pdf_content)


    bot = telegram.Bot(token='6074560289:AAHt0bXHDE5F-HoRwVVVwL5Nu9PyS1FXLXc')

    chat_id = '5602315398'

    message = 'new purchse order sent!\napprove it:'


    # Use the send_message method of the bot to send the message and await the result
    async def send_message():
        await bot.send_document(chat_id=chat_id, document=pdf_file, filename='file.pdf', caption=message)
        await bot.send_message(chat_id=chat_id, url='http://192.168.0.123:8001/app/purchase-order')


    # Call the send_message function to send the message
    asyncio.run(send_message())


