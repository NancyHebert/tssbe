from behave import *

use_step_matcher("re")


@step("the username and password are passed to the authentication service")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given(u'that a user must log on')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given that a user must log on')


@when(u'the user provides a username and password')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user provides a username and password')


@then(u'the service should pass pass a JWT token')
def x(context):
    raise NotImplementedError(u'STEP: Then the service should pass pass a JWT token')
