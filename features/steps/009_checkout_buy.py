from behave import *

@then("Verify Contact=email(randomized) and Ship to=address '{txt}' are here")
def contact_and_address_here(context, txt):
    """
    Verify captcha works and "Select all images with" text is here'
    """
    context.app.main_page.contact_and_address_here(txt)