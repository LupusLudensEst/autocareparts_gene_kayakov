from behave import *

@then("Verify that cart has {qntty} item")
def cart_has_ine_item(context, qntty):
    """
    Verify that cart has 1 item
    """
    context.app.main_page.cart_has_ine_item(qntty)