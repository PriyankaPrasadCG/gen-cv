import os
import logging
from applicationinsights import TelemetryClient

# Set the Application Insights Instrumentation Key
instrumentation_key = "1cbd322a-9f07-4eb1-9ad0-db7e89a9815f"
os.environ["APPINSIGHTS_INSTRUMENTATIONKEY"] = instrumentation_key

# Initialize the TelemetryClient
tc = TelemetryClient(instrumentation_key)

# Set up logging to use Application Insights
class ApplicationInsightsHandler(logging.Handler):
    def __init__(self, instrumentation_key, *args, **kwargs):
        self.instrumentation_key = instrumentation_key
        super().__init__(*args, **kwargs)

    def emit(self, record):
        msg = self.format(record)
        tc.track_trace(msg)
        tc.flush()

# Set up the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Add the Application Insights handler to the logger
ai_handler = ApplicationInsightsHandler(instrumentation_key)
logger.addHandler(ai_handler)

# Export the logger for use in other files
app_logger = logger