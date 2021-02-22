from behave import *

@then('Verify captcha works and "{txt}" text is here')
def captcha_works(context, txt):
    """
    Verify captcha works and "Select" text is here
    """
    context.app.main_page.captcha_works(txt)