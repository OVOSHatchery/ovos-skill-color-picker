from behave import given, when, then

from test.integrationtests.voight_kampff import (
    emit_utterance,
    format_dialog_match_error,
    wait_for_dialog_match,
)


@given("the active color is set to {pre_color}")
def given_active_color_is(context, pre_color):
    context.set_color_state(pre_color)

@then("the active color changes to {post_color}")
def given_active_color_is(context, post_color):
    assert(context.active_color == post_color)
    
