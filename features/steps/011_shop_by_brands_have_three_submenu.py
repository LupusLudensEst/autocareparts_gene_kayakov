from behave import *

@then("Verify that Shop By Brand has {qntty} elements")
def shop_by_brands(context, qntty):
    """
    Verify that Shop By Brand has 9 elements
    """
    context.app.main_page.shop_by_brands(qntty)