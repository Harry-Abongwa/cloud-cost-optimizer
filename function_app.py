import logging
import datetime
import azure.functions as func

from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.resourcegraph import ResourceGraphClient
from azure.mgmt.resourcegraph.models import QueryRequest

# Create the Function App instance
app = func.FunctionApp()

# Azure authentication
credential = DefaultAzureCredential()
subscription_id = "096fdeb1-5d6f-48b4-8833-17fef8aad119"

compute_client = ComputeManagementClient(credential, subscription_id)
resource_graph_client = ResourceGraphClient(credential)

# -------------------------------
# TIMER FUNCTION (runs hourly)
# -------------------------------
@app.schedule(
    schedule="*/30 * * * * *",  # every 30 seconds
    arg_name="costTimer",
    run_on_startup=True
)
def costOptimizerTimer(costTimer: func.TimerRequest) -> None:
    logging.info("🚀 Started Azure Cost Optimizer.")

    # ---- QUERY FOR VMs INSIDE THE FUNCTION ----
    query = """
    Resources
    | where type == "microsoft.compute/virtualmachines"
    | extend powerState = tostring(properties.extended.instanceView.powerState.code)
    | project name, resourceGroup, powerState
    """

    request = QueryRequest(subscriptions=[subscription_id], query=query)
    result = resource_graph_client.resources(request)

    vms = result.data
    stopped = 0

    logging.info(f"Found {len(vms)} virtual machines.")

    # ---- STOP RUNNING VMs ----
    for vm in vms:
        if vm["powerState"] == "PowerState/running":
            name = vm["name"]
            rg = vm["resourceGroup"]

            logging.info(f"🛑 Stopping VM: {name} in {rg}")
            compute_client.virtual_machines.begin_power_off(rg, name)
            stopped += 1

    now = datetime.datetime.utcnow().isoformat()
    logging.info(f"✨ Optimization completed at {now}. Total stopped VMs: {stopped}")