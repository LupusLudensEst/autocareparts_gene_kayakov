from behave import *

@then("Verify text {txt} is here")
def verify_text_here(context, txt):
    """
    Verify texts of Payment System is here
    """
    context.app.main_page.verify_text_here(txt)
