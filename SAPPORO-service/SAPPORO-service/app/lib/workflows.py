# coding: utf-8
import requests
from flask import abort
from requests.exceptions import RequestException

from .util import read_workflow_info


def read_workflow_setting_file():
    workflow_info = read_workflow_info()
    data = dict()
    data["workflows"] = []
    for workflow in workflow_info["workflows"]:
        workflow["workflow_content"] = fetch_file(
            workflow["workflow_location"])
        workflow["workflow_parameters_template"] = fetch_file(
            workflow["workflow_parameters_template_location"])
        data["workflows"].append(workflow)

    return data


def fetch_file(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except RequestException:
        abort(400, "Can not get file: {}".format(url))

    return response.content.decode()
