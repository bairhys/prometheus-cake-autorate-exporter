# Prometheus CAKE Autorate exporter

This is a Prometheus exporter for [CAKE-autorate](https://github.com/lynxthecat/cake-autorate/) stats.

[GitHub](https://github.com/bairhys/prometheus-cake-autorate-exporter)

[Grafana Dashboard](https://grafana.com/grafana/dashboards/18597)

![Grafana](https://raw.githubusercontent.com/bairhys/prometheus-cake-autorate-exporter/main/grafana.png)

## Run the exporter on an OpenWRT router

Once [CAKE-autorate](https://github.com/lynxthecat/cake-autorate/) is running, to setup this exporter

1. Install `python3` and `python3-pip`

```bash
opkg update
opkg install python3 python3-pip
```

2. Install `prometheus-client`

```bash
pip install prometheus-client
```

3. Download the exporter
   
```bash
cd /root
wget https://raw.githubusercontent.com/bairhys/prometheus-cake-autorate-exporter/main/prometheus_cake_autorate_exporter.py
```

4. Start exporter manually

```bash
python prometheus_cake_autorate_exporter.py
```

5. Test to determine if metrics working. In a browser, try accessing [http://192.168.1.1:9101/](http://192.168.1.1:9101/), should see raw metrics like below

```yaml
# HELP python_gc_objects_collected_total Objects collected during gc
# TYPE python_gc_objects_collected_total counter
python_gc_objects_collected_total{generation="0"} 102.0
python_gc_objects_collected_total{generation="1"} 289.0
python_gc_objects_collected_total{generation="2"} 0.0
# HELP python_gc_objects_uncollectable_total Uncollectable object found during GC
# TYPE python_gc_objects_uncollectable_total counter
python_gc_objects_uncollectable_total{generation="0"} 0.0
python_gc_objects_uncollectable_total{generation="1"} 0.0
python_gc_objects_uncollectable_total{generation="2"} 0.0
# HELP python_gc_collections_total Number of times this generation was collected
# TYPE python_gc_collections_total counter
python_gc_collections_total{generation="0"} 42.0
python_gc_collections_total{generation="1"} 3.0
python_gc_collections_total{generation="2"} 0.0
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="3",minor="10",patchlevel="9",version="3.10.9"} 1.0
# HELP process_virtual_memory_bytes Virtual memory size in bytes.
# TYPE process_virtual_memory_bytes gauge
process_virtual_memory_bytes 2.3035904e+07
# HELP process_resident_memory_bytes Resident memory size in bytes.
# TYPE process_resident_memory_bytes gauge
process_resident_memory_bytes 1.8583552e+07
# HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
# TYPE process_start_time_seconds gauge
process_start_time_seconds 1.68230686708e+09
# HELP process_cpu_seconds_total Total user and system CPU time spent in seconds.
# TYPE process_cpu_seconds_total counter
process_cpu_seconds_total 6.0
# HELP process_open_fds Number of open file descriptors.
# TYPE process_open_fds gauge
process_open_fds 7.0
# HELP process_max_fds Maximum number of open file descriptors.
# TYPE process_max_fds gauge
process_max_fds 1024.0
# HELP DATA_HEADER DATA_HEADER
# TYPE DATA_HEADER gauge
DATA_HEADER{DATA_HEADER="DATA"} 1.0
DATA_HEADER{DATA_HEADER="LOAD"} 0.0
DATA_HEADER{DATA_HEADER="SHAPER"} 0.0
# HELP LOG_TIMESTAMP LOG_TIMESTAMP
# TYPE LOG_TIMESTAMP gauge
LOG_TIMESTAMP 1.682307438446743e+09
# HELP PROC_TIME_US PROC_TIME_US
# TYPE PROC_TIME_US gauge
PROC_TIME_US 1.682307438446161e+09
# HELP DL_ACHIEVED_RATE DL_ACHIEVED_RATE
# TYPE DL_ACHIEVED_RATE gauge
DL_ACHIEVED_RATE 757.0
# HELP UL_ACHIEVED_RATE UL_ACHIEVED_RATE
# TYPE UL_ACHIEVED_RATE gauge
UL_ACHIEVED_RATE 127.0
# HELP DL_LOAD_PERCENT DL_LOAD_PERCENT
# TYPE DL_LOAD_PERCENT gauge
DL_LOAD_PERCENT 0.0
# HELP UL_LOAD_PERCENT UL_LOAD_PERCENT
# TYPE UL_LOAD_PERCENT gauge
UL_LOAD_PERCENT 0.0
# HELP RTT_TIMESTAMP RTT_TIMESTAMP
# TYPE RTT_TIMESTAMP gauge
RTT_TIMESTAMP 1.68230743843855e+09
# HELP REFLECTOR_info REFLECTOR
# TYPE REFLECTOR_info gauge
REFLECTOR_info{address=" 1.0.0.1"} 1.0
# HELP SEQUENCE SEQUENCE
# TYPE SEQUENCE gauge
SEQUENCE 4840.0
# HELP DL_OWD_BASELINE DL_OWD_BASELINE
# TYPE DL_OWD_BASELINE gauge
DL_OWD_BASELINE 0.010209
# HELP DL_OWD_US DL_OWD_US
# TYPE DL_OWD_US gauge
DL_OWD_US 0.01205
# HELP DL_OWD_DELTA_EWMA_US DL_OWD_DELTA_EWMA_US
# TYPE DL_OWD_DELTA_EWMA_US gauge
DL_OWD_DELTA_EWMA_US 0.00496
# HELP DL_OWD_DELTA_US DL_OWD_DELTA_US
# TYPE DL_OWD_DELTA_US gauge
DL_OWD_DELTA_US 0.001841
# HELP DL_ADJ_DELAY_THR DL_ADJ_DELAY_THR
# TYPE DL_ADJ_DELAY_THR gauge
DL_ADJ_DELAY_THR 0.030016
# HELP UL_OWD_BASELINE UL_OWD_BASELINE
# TYPE UL_OWD_BASELINE gauge
UL_OWD_BASELINE 0.010209
# HELP UL_OWD_US UL_OWD_US
# TYPE UL_OWD_US gauge
UL_OWD_US 0.01205
# HELP UL_OWD_DELTA_EWMA_US UL_OWD_DELTA_EWMA_US
# TYPE UL_OWD_DELTA_EWMA_US gauge
UL_OWD_DELTA_EWMA_US 0.00496
# HELP UL_OWD_DELTA_US UL_OWD_DELTA_US
# TYPE UL_OWD_DELTA_US gauge
UL_OWD_DELTA_US 0.001841
# HELP UL_ADJ_DELAY_THR UL_ADJ_DELAY_THR
# TYPE UL_ADJ_DELAY_THR gauge
UL_ADJ_DELAY_THR 0.030375
# HELP SUM_DL_DELAYS SUM_DL_DELAYS
# TYPE SUM_DL_DELAYS gauge
SUM_DL_DELAYS 0.0
# HELP SUM_UL_DELAYS SUM_UL_DELAYS
# TYPE SUM_UL_DELAYS gauge
SUM_UL_DELAYS 0.0
# HELP DL_LOAD_CONDITION DL_LOAD_CONDITION
# TYPE DL_LOAD_CONDITION gauge
DL_LOAD_CONDITION{DL_LOAD_CONDITION="dl_idle"} 1.0
DL_LOAD_CONDITION{DL_LOAD_CONDITION="dl_idle_bb"} 0.0
DL_LOAD_CONDITION{DL_LOAD_CONDITION="dl_low"} 0.0
DL_LOAD_CONDITION{DL_LOAD_CONDITION="dl_low_bb"} 0.0
DL_LOAD_CONDITION{DL_LOAD_CONDITION="dl_high"} 0.0
DL_LOAD_CONDITION{DL_LOAD_CONDITION="dl_high_bb"} 0.0
# HELP UL_LOAD_CONDITION UL_LOAD_CONDITION
# TYPE UL_LOAD_CONDITION gauge
UL_LOAD_CONDITION{UL_LOAD_CONDITION="ul_idle"} 1.0
UL_LOAD_CONDITION{UL_LOAD_CONDITION="ul_idle_bb"} 0.0
UL_LOAD_CONDITION{UL_LOAD_CONDITION="ul_low"} 0.0
UL_LOAD_CONDITION{UL_LOAD_CONDITION="ul_low_bb"} 0.0
UL_LOAD_CONDITION{UL_LOAD_CONDITION="ul_high"} 0.0
UL_LOAD_CONDITION{UL_LOAD_CONDITION="ul_high_bb"} 0.0
# HELP CAKE_DL_RATE CAKE_DL_RATE
# TYPE CAKE_DL_RATE gauge
CAKE_DL_RATE 9.1023e+07
# HELP CAKE_UL_RATE CAKE_UL_RATE
# TYPE CAKE_UL_RATE gauge
CAKE_UL_RATE 4e+06
```

6. Stop running exporter manually (Ctrl+C)

5. Setup service

```bash
cd /root
wget https://raw.githubusercontent.com/bairhys/prometheus-cake-autorate-exporter/main/prometheus-node-exporter-cake-autorate
```

6. Enable and start service

```bash
service enable prometheus-node-exporter-cake-autorate
service start prometheus-node-exporter-cake-autorate
```

7. Test to determine if metrics working with service. In a browser, try accessing [http://192.168.1.1:9101/](http://192.168.1.1:9101/), should see raw metrics again like above

### Setup Prometheus

If you don't already have Prometheus set up to scrape the CAKE Autorate metrics, setup Prometheus to run on your server

- create Prometheus config file `prometheus.yml`
- copy example below into `prometheus.yml`, replacing `192.168.1.1:9101` with the IP address and port of your exporter.

  ```yaml
  # my global config
  global:
    scrape_interval: 15s # Set the scrape interval to every 15 seconds. Default is every 1 minute.
    evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.
    # scrape_timeout is set to the global default (10s).
   
  # A scrape configuration containing exactly one endpoint to scrape:
  # Here it's Prometheus itself.
  scrape_configs:
    # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
    - job_name: "prometheus"
      static_configs:
        - targets: ["localhost:9090"]
  
    - job_name: 'router_cake_autorate'
      scrape_interval: 3s
      metrics_path: /metrics
      static_configs:
        - targets: ["192.168.1.1:9101"]

  ```

- Run Prometheus docker container by replacing `/path/to/prometheus.yml` to point to the `prometheus.yml` just created

  ```bash
  docker run \
      -d \
      --restart unless-stopped \
      -p 9090:9090 \
      -v /path/to/prometheus.yml:/etc/prometheus/prometheus.yml \
      prom/prometheus
  ```

To see if Prometheus is scraping the exporter, go to Prometheus targets page [http://your-prometheus-ip:9090/targets](http://your-prometheus-ip:9090/targets) and look for `UP` for `router_cake_autorate` job.

### Setup Grafana

If you don't already have Grafana set up, setup Grafana to run on your server

- run Grafana

    ```bash
    docker run \
        -d \
        --restart unless-stopped \
        -p 3000:3000 \
        grafana/grafana-oss
    ```

- Go to Grafana [http://your-grafana-ip:3000](http://your-grafana-ip:3000) (might take a few minutes first run). Use admin:admin to log in
- Go to [http://your-grafana-ip:3000/datasources](http://your-grafana-ip:3000/datasources)
  - add Prometheus datasource
  - Set Prometheus URL `http://<your-prometheus-ip>:9090`
  - Click `Save and Test` to check if connected
- Go to [http://your-grafana-ip:3000/dashboards](http://your-grafana-ip:3000/dashboards)
  - New -> Import
  - Enter in `Import via grafana.com`: `18597` (id can be found at [Grafana Dashboard](https://grafana.com/grafana/dashboards/18597)) and click Load
  - Set the datasource as Prometheus instance set up before then click Import
- Should now be able to see CAKE Autorate time series metrics in the Grafana dashboard
