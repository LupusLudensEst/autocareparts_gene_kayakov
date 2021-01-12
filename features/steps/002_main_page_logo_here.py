from behave import *

@then('Verify logo "Auto Care Parts" is here')
def vrf_logo_here(context):
    """
    Verify logo "Auto Care Parts" is here
    """
    context.app.main_page.vrf_logo_here()