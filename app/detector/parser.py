import re
from datetime import datetime

SSH_FAILED_REGEX = re.compile(
    r'(?P<timestamp>\w+\s+\d+\s[\d:]+).*Failed password for (invalid user )?(?P<user>\w+) from (?P<ip>[\d.]+)'
)

SSH_ACCEPTED_REGEX = re.compile(
    r'(?P<timestamp>\w+\s+\d+\s[\d:]+).*Accepted password for (?P<user>\w+) from (?P<ip>[\d.]+)'
)

def parse_ssh_log(filepath):
    """
    Parses an SSH auth log and returns normalized events.
    """
    events = []

    with open(filepath, "r") as f:
        for line in f:
            failed_match = SSH_FAILED_REGEX.search(line)
            accepted_match = SSH_ACCEPTED_REGEX.search(line)

            if failed_match:
                events.append({
                    "event_type": "ssh_failed_login",
                    "timestamp": failed_match.group("timestamp"),
                    "user": failed_match.group("user"),
                    "ip": failed_match.group("ip"),
                })

            elif accepted_match:
                events.append({
                    "event_type": "ssh_success_login",
                    "timestamp": accepted_match.group("timestamp"),
                    "user": accepted_match.group("user"),
                    "ip": accepted_match.group("ip"),
                })

    return events
