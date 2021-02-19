from behave import *

@then("Verify after registration and click on Submit text here {txt}")
def rgstrtn_sbmt_txt_hr(context, txt):
    """
    Verify after registration and click on Submit text here Your answer wasn't correct, please try again
    """
    context.app.main_page.rgstrtn_sbmt_txt_hr(txt)