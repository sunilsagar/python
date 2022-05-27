import prometheus_client
from prometheus_client import start_http_server, Summary
import random
import time
import psutil

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

UPDATE_PERIOD = 10
SYSTEM_USAGE = prometheus_client.Gauge('system_usage',
                                       'Hold current system resource usage',
                                       ['resource_type'])

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        SYSTEM_USAGE.labels('CPU').set(psutil.cpu_percent())
        SYSTEM_USAGE.labels('Memory').set(psutil.virtual_memory()[2])
        SYSTEM_USAGE.labels('Disk').set(psutil.disk_usage(mountpoint='C:\\'))
        time.sleep(UPDATE_PERIOD)
        process_request(random.random())







