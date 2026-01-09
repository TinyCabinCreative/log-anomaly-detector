Log Anomaly Detector

A Mini SIEM Component

Overview

The Log Anomaly Detector is a lightweight, containerized security tool that ingests system or application logs and flags potentially suspicious activity using simple rule-based and statistical detection techniques.

It is designed to demonstrate core detection engineering concepts found in SIEM, XDR, and SOC environments — including log parsing, anomaly identification, and auditable reporting — without relying on heavy enterprise platforms.

This project is intentionally minimal, transparent, and extensible, making it suitable as a learning tool, portfolio project, or foundation for more advanced detection systems.

Key Capabilities

📄 Parse common log formats (e.g. SSH auth logs, Apache access logs)

🚨 Detect suspicious patterns such as:

Brute-force login attempts

Repeated authentication failures

Unusual IP address activity

📊 Generate structured reports of flagged events

🐳 Fully containerized with Docker for reproducibility

🧠 Clear separation of parsing, rules, and analysis logic

**Lightweight UI for viewing detection output**

**Why This Project Exists**

Enterprise SIEM tools are powerful but opaque. This project focuses on understanding the fundamentals:

- How logs are ingested and normalized

- How detection rules are constructed

- How suspicious behavior is identified and surfaced

- How results are stored and reviewed

**This makes the project especially useful for:**

- SOC / Blue Team roles

- Detection engineering

- Security-minded software developers

- Interview and portfolio demonstrations
