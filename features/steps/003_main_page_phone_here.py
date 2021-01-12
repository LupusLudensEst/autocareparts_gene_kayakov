from behave import *

@then('Verify phone "{phone}" is here')
def vrf_phn_here(context, phone):
    """
    Verify phone "310.817.0370" is here
    """
    context.app.main_page.vrf_phn_here(phone)