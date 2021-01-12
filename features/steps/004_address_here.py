from behave import *

@then('Verify address "{addrss}" is here')
def vrf_addrss_here(context, addrss):
    """
    Verify address "20350 NE 16TH PL" is here
    """
    context.app.main_page.vrf_addrss_here(addrss)