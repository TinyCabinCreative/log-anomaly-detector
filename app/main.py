import argparse
from detector.analyzer import analyze_log

def main():
    parser = argparse.ArgumentParser(description="Log Anomaly Detector")
    parser.add_argument("--logfile", required=True, help="Path to log file")
    parser.add_argument(
        "--threshold",
        type=int,
        default=5,
        help="Failed login threshold for alerts"
    )

    args = parser.parse_args()

    analyze_log(
        logfile=args.logfile,
        output_path="app/output/report.json",
        threshold=args.threshold
    )

if __name__ == "__main__":
    main()
