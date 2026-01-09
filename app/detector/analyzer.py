import json
from detector.parser import parse_ssh_log
from detector.rules import detect_ssh_bruteforce

def analyze_log(logfile, output_path, threshold=5):
    """
    Main analysis pipeline.
    """
    print("[+] Parsing log file...")
    events = parse_ssh_log(logfile)

    print(f"[+] Parsed {len(events)} events")

    print("[+] Running detection rules...")
    alerts = detect_ssh_bruteforce(events, threshold=threshold)

    report = {
        "logfile": logfile,
        "total_events": len(events),
        "alerts": alerts
    }

    with open(output_path, "w") as f:
        json.dump(report, f, indent=2)

    print(f"[+] Analysis complete. Alerts written to {output_path}")
