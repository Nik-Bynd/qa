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
from behave import when, then
from qa.accessibility.features.environment import FILE_NAME
from qa.environment_variables import QA_FOLDER_PATH

results_file = '%saccessibility/output/%s.report.json' % (
    QA_FOLDER_PATH,
    FILE_NAME
)


@when('we find the flaky connection section')
def step_impl(context):
    assert context.results_json[
        'aggregations'][0]['score'][0]['name'] == \
        'App can load on offline/flaky connections', \
        'Flaky Connection Json not where it is expected'
    context.current_node = context.results_json[
        'aggregations'][0]['score'][0]['overall']
    assert True
