from behave import given


@given('there are no codecasts')
def clear_codecasts(context):
    raise NotImplementedError('STEP: Given there are no codecasts')


@given('user U is logged in')
def step_impl(context):
    raise NotImplementedError('STEP: Given user U is logged in')


@when('system presents codecasts for user U')
def step_impl(context):
    raise NotImplementedError('STEP: When system presents codecasts for user U')


@then('no codecasts are presented')
def step_impl(context):
    raise NotImplementedError('STEP: Then no codecasts are presented')
