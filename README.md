Azure Cloud Cost Optimizer 🚀

An automated **Azure Cost Optimization engine** built using **Python + Azure Functions** that periodically scans Azure subscriptions, analyzes virtual machine usage, and produces optimization insights while tracking execution health and error rates through Azure dashboards.

This project demonstrates real-world cloud cost governance, observability, and automation practices.

---

 What This Project Does

- Runs on a **Timer-triggered Azure Function**
- Authenticates securely using **Managed Identity**
- Queries Azure Resource Manager to analyze resources
- Identifies unused or underutilized Virtual Machines
- Logs optimization results and execution status
- Tracks **success rate, error rate, and run frequency**
- Visualizes metrics using **Azure Application Insights + Dashboards**

---

💡 Why This Project Matters

Cloud environments often incur unnecessary costs due to idle or underutilized resources.
This project demonstrates how **automation, monitoring, and governance** can be combined
to proactively control cloud spend without impacting availability.

By leveraging **serverless execution, managed identity, and real-time observability**,
this solution reflects how modern cloud teams implement **cost efficiency as code.


Architecture Overview
Azure Function (Python)
└── Timer Trigger
└── Managed Identity Authentication
└── Azure Resource Manager API
└── Virtual Machine Analysis
└── Logs + Metrics
└── Azure Application Insights
└── Azure Dashboard

---

☁️ Azure Services Used

- **Azure Functions** (Consumption Plan, Python 3.10)
- **Managed Identity** (secure, passwordless auth)
- **Azure Resource Manager (ARM)**
- **Application Insights**
- **Azure Monitor / KQL**
- **Azure Dashboards**
- **GitHub** (source control)

---

Observability & Monitoring

The solution tracks:
- Function execution count
- Successful optimization runs
- Error rate
- Execution duration
- Optimization completion events

 KQL Query (Run Count)
kql
traces
| where cloud_RoleName == "harry-cost-optimizer-func"
| where message contains "Optimization completed"
| summarize Runs=count() by bin(timestamp, 5m)
| render timechart

📁 Project Structure

cloud-cost-optimizer/
├── function_app.py        # Main Azure Function logic
├── host.json              # Function host configuration
├── requirements.txt       # Python dependencies
├── .funcignore            # Azure Functions ignore file
├── .gitignore             # Git ignore rules


Author

Harry Abongwa
Cloud / Security / DevOps Engineer
GitHub: https://github.com/Harry-Abongwa
