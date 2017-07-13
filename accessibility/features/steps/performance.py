'''
Feature: Our app performs well

  Scenario: The application can load over a flaky connection

    Given we have valid json alert output
    When we find the flaky connection section
    Then it should have an overall score above "0.8"
'''
import os
import json
import re
import sys
from environment_variables import QA_FOLDER_PATH
from environment import FILE_NAME
from behave import when, then

results_file = '%saccessibility/output/%s.report.json' % (
    QA_FOLDER_PATH,
    FILE_NAME
)


@when('we find the flaky connection section')
def step_impl(context):
    context.flaky = context.results_json[
        'aggregations'][0]['score'][0]['overall']
    assert True


@then('it should have an overall score above "{expected_score}"')
def step_impl(context, expected_score):
    print (context.flaky)
    if context.flaky < float(expected_score):
        sys.stderr.write(
            "Expected a score above %s:\nInstead got %i" % (
                expected_score,
                context.flaky
            )
        )
        assert False
    else:
        assert True
