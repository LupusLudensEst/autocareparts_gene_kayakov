from behave import *

@then('Verify email "{eml}" is here')
def vrf_eml_here(context, eml):
    """
    Verify email "sales@autocareparts.com" is here
    """
    context.app.main_page.vrf_eml_here(eml)