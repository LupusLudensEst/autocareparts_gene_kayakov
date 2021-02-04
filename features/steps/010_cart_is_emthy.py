from behave import *

@then('Click on the Cart button and verify text "{txt}" is here')
def click_on_emthy_cart_btn(context, txt):
    """
    Click on the Cart button and verify text "YOUR CART IS CURRENTLY EMPTY." is here
    """
    context.app.main_page.click_on_emthy_cart_btn(txt)