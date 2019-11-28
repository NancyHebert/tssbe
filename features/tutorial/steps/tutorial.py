from behave import *

use_step_matcher("re")


@given("the ninja has a third level black-belt")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass

@when(u'attacked by a samurai')
def step_impl(context):
    raise NotImplementedError(u'STEP: When attacked by a samurai')

@then(u'the ninja should engage the opponent')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the ninja should engage the opponent')

@when(u'attacked by Chuck Norris')
def step_impl(context):
    raise NotImplementedError(u'STEP: When attacked by Chuck Norris')

@then(u'the ninja should run for his life')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the ninja should run for his life')
