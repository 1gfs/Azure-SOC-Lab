A very simple SOC home lab that I tweaked around with to understanding studying logs!

Features

    ELK Stack (Elasticsearch, Logstash, Kibana) for log management

    Python log generator simulating security events

    Real-time monitoring dashboard

    Docker containerization for easy setup

Quick Start
Prerequisites

    Docker & Docker Compose

    Python 3

Installation

    Start the containers:
    bash

docker-compose up -d

Generate logs:
bash

python3 scripts/log-generator.py

    Access dashboards:

        Kibana: http://localhost:5601

        Web Dashboard: http://localhost:8080/dashboard.html

Project Structure
text

home-soc-lab/
├── docker-compose.yml          # Container configuration
├── logstash.conf               # Log processing pipeline
├── scripts/
│   └── log-generator.py       # Security event simulator
├── dashboards/
│   └── dashboard.html         # Real-time monitoring UI
├── config/                    # Configuration files
└── README.md                  # This file

Components
1. ELK Stack

    Elasticsearch: Stores and indexes logs

    Logstash: Processes and parses log data

    Kibana: Visualizes logs with dashboards

2. Log Generator

Python script that simulates:

    Failed login attempts

    Port scans

    SQL injection attempts

    DDoS attack patterns

    Normal system events

3. Monitoring Dashboard

Simple HTML dashboard showing:

    Real-time security events

    Alert counts by severity

    Live log feed

Technologies Used

    Docker & Docker Compose

    ELK Stack (Elasticsearch, Logstash, Kibana)

    Python 3

    HTML/CSS/JavaScript

    Nginx

License

MIT
