from collections import defaultdict

def detect_ssh_bruteforce(events, threshold=5):
    """
    Detects SSH brute-force attempts based on repeated failed logins
    from the same IP.
    """
    failures_by_ip = defaultdict(int)
    alerts = []

    for event in events:
        if event["event_type"] == "ssh_failed_login":
            failures_by_ip[event["ip"]] += 1

    for ip, count in failures_by_ip.items():
        if count >= threshold:
            alerts.append({
                "alert_type": "ssh_bruteforce",
                "source_ip": ip,
                "failure_count": count,
                "severity": "high" if count >= threshold * 2 else "medium"
            })

    return alerts
