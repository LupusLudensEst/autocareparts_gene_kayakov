from behave import *

@then('Verify searched word in Shop by Brand, Numbers, 1 Shot "{txt}" is here')
def shopbybrand_numbers_oneshot(context, txt):
    """
    Verify searched word "gorilla" is here'
    """
    context.app.main_page.shopbybrand_numbers_oneshot(txt)