'''import logging

import json_log_formatter

formatter = json_log_formatter.JSONFormatter()

json_handler = logging.FileHandler(filename='./my-log.json')
json_handler.setFormatter(formatter)

logger = logging.getLogger('my_json')
logger.addHandler(json_handler)
logger.setLevel(logging.INFO)

logger.info('Sign up', extra={'referral_code': '52d6ce'})'''


from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_api import LogsApi
from datadog_api_client.v2.model.content_encoding import ContentEncoding
from datadog_api_client.v2.model.http_log import HTTPLog
from datadog_api_client.v2.model.http_log_item import HTTPLogItem

body = HTTPLog(
    [
        HTTPLogItem(
            ddsource="nginx",
            ddtags="env:staging,version:5.1",
            hostname="i-012345678",
            message="2019-11-19T14:37:58,995 INFO [process.name][20081] work 2.0",
            service="scoring",
            status="warning"
        ),
        HTTPLogItem(
            ddsource="nginx",
            ddtags="env:staging,version:5.1",
            hostname="i-012345678",
            message="2019-11-19T14:37:58,995 INFO [process.name][20081] work 2.0",
            service="scoring",
            status="error"
        ),

    ]
)

configuration = Configuration()
configuration.api_key['apiKeyAuth'] = 'f963793a6649166ab972a8ff91beb1b5ff' #not the real key

with ApiClient(configuration) as api_client:
    api_instance = LogsApi(api_client)
    response = api_instance.submit_log(content_encoding=ContentEncoding("deflate"), body=body,)

    print(response.status_code)
