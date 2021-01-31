from behave import *

@then('Verify searched word "{txt}" is here')
def vrf_srchwrd_here(context, txt):
    """
    Verify searched word "gorilla" is here'
    """
    context.app.main_page.vrf_srchwrd_here(txt)