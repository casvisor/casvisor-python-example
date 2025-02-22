from datetime import datetime, timezone, timedelta
import time
import random
from casvisor import BaseClient, Record, _RecordSDK

TestEndpoint = "https://demo.casvisor.com"
TestClientId = "111111"
TestClientSecret = "124140638b4f9de7e78e79ba22d451c17bfa9688"
TestOrganization = "casbin"
TestApplication = "app-client"


def get_random_code(length):
    std_nums = "0123456789"
    result = "".join(random.choice(std_nums) for _ in range(length))
    return result


def get_random_name(prefix):
    return f"{prefix}_{get_random_code(6)}"


def get_rfc3339_timestamp():
    now = datetime.now()

    local_time = time.localtime()
    offset = timedelta(seconds=local_time.tm_gmtoff)

    local_timezone = timezone(offset)

    rfc3339_time = now.astimezone(local_timezone).replace(microsecond=0).isoformat()
    return rfc3339_time


if __name__=="__main__":
    name = get_random_name("blockchain_record")

    createdTime = get_rfc3339_timestamp()

    user = "Alice Green"
    client = "Federated Learning"

    # Create a new record
    record = Record(
        owner=TestOrganization,
        name=name,
        createdTime=createdTime,
        organization=TestOrganization,
        clientIp="",
        user=user,
        method="POST",
        requestUri="/api/add-blockchain-record",
        action=client,
        object="test_object",
        language="en",
        response='{"status":"ok","msg":""}',
        isTriggered=False,
    )

    client = BaseClient(TestClientId, TestClientSecret, TestEndpoint)
    sdk = _RecordSDK(client, TestOrganization)

    # Add a new record
    try:
        result = sdk.add_record(record)
        print(f"add_record() OK: {result}")
    except Exception as e:
        print(f"Failed to add record: {e}")
