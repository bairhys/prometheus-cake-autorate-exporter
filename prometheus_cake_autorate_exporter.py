import time
import logging
import subprocess
from prometheus_client.core import Gauge, Info, Enum
from prometheus_client import start_http_server

LOG_FILE = '/var/log/cake-autorate.primary.log'
DEBUG = False
EXPORTER_PORT = 9101

DATA_HEADER = Enum('cake_autorate_data_header_enum', 'Log Type', states=['DATA',  'LOAD', 'SHAPER', 'SUMMARY']) # [0]
# LOG_DATETIME = Info('LOG_DATETIME','LOG_DATETIME') # [1]
LOG_TIMESTAMP = Gauge('cake_autorate_log_timestamp_seconds', 'Log timestamp (seconds)') # [2]
PROC_TIME = Gauge('cake_autorate_proc_timestamp_seconds', 'Process time (seconds)')  # [3]

DL_ACHIEVED_RATE = Gauge('cake_autorate_dl_achieved_rate_bits_per_second', 'Measured download rate (bits/second)') # [4]
UL_ACHIEVED_RATE = Gauge('cake_autorate_ul_achieved_rate_bits_per_second', 'Measured upload rate (bits/second)') # [5]
DL_LOAD_PERCENT = Gauge('cake_autorate_dl_load_percent', 'Download load (percent)') # [6]
UL_LOAD_PERCENT = Gauge('cake_autorate_ul_load_percent', 'Upload load (percent)') # [7]

ICMP_TIMESTAMP = Gauge('cake_autorate_icmp_timestamp_seconds', 'ICMP Timestamp (seconds)') # [8]
REFLECTOR = Info('cake_autorate_reflector','Reflector target address', ['reflector']) # [9]
SEQUENCE =  Gauge('cake_autorate_sequence','Sequence', ['reflector']) # [10]

DL_OWD_BASELINE = Gauge('cake_autorate_dl_owd_baseline_seconds', '(seconds)', ['reflector']) # [11]
DL_OWD = Gauge('cake_autorate_dl_owd_seconds', '(seconds)', ['reflector']) # [12]
DL_OWD_DELTA_EWMA = Gauge('cake_autorate_dl_owd_delta_ewma_seconds', '(seconds)', ['reflector']) # [13]
DL_OWD_DELTA = Gauge('cake_autorate_dl_owd_delta_seconds', '(seconds)', ['reflector']) # [14]
DL_ADJ_DELAY_THR = Gauge('cake_autorate_dl_adj_delay_thr_seconds', '(seconds)', ['reflector']) # [15]

UL_OWD_BASELINE = Gauge('cake_autorate_ul_owd_baseline_seconds', '(seconds)', ['reflector']) # [16]
UL_OWD = Gauge('cake_autorate_ul_owd_seconds', '(seconds)', ['reflector']) # [17]
UL_OWD_DELTA_EWMA = Gauge('cake_autorate_ul_owd_delta_ewma_seconds', '(seconds)', ['reflector']) # [18]
UL_OWD_DELTA = Gauge('cake_autorate_ul_owd_delta_seconds', '(seconds)', ['reflector']) # [19]
UL_ADJ_DELAY_THR = Gauge('cake_autorate_ul_adj_delay_thr_seconds', '(seconds)', ['reflector']) # [20]

DL_SUM_DELAYS = Gauge('cake_autorate_dl_sum_delays_seconds', 'Total download delays (seconds)', ['reflector']) # [21]
DL_AVG_OWD_DELTA = Gauge('cake_autorate_dl_avg_owd_delta_seconds', 'Total download average owd delta (seconds)', ['reflector']) # [22]
DL_ADJ_OWD_DELTA_THR = Gauge('cake_autorate_dl_adj_owd_delta_thr_seconds', 'Total adj owd delta thr (seconds)', ['reflector']) # [23]

UL_SUM_DELAYS = Gauge('cake_autorate_ul_sum_delays_seconds', 'Total upload delays (seconds)', ['reflector']) # [24]
UL_AVG_OWD_DELTA = Gauge('cake_autorate_ul_avg_owd_delta_seconds', 'Total download average owd delta (seconds)', ['reflector']) # [25]
UL_ADJ_OWD_DELTA_THR= Gauge('cake_autorate_ul_adj_owd_delta_thr_seconds', 'Total adj owd delta thr (seconds)', ['reflector']) # [26]

DL_LOAD_CONDITION = Enum('cake_autorate_dl_load_condition_enum', 'Download state', states=['dl_idle', 'dl_idle_bb',  'dl_low', 'dl_low_bb', 'dl_high', 'dl_high_bb']) # [27]
UL_LOAD_CONDITION = Enum('cake_autorate_ul_load_condition_enum', 'Upload state', states=['ul_idle', 'ul_idle_bb',  'ul_low', 'ul_low_bb', 'ul_high', 'ul_high_bb']) # [28]

CAKE_DL_RATE = Gauge('cake_autorate_cake_dl_rate_bits_per_second', 'CAKE download rate (bits/sec)') # [29]
CAKE_UL_RATE = Gauge('cake_autorate_cake_ul_rate_bits_per_second', 'CAKE upload rate (bits/sec)') # [30]

KBPS = 1000.0 # number of bits in kilobit
US = 1000000.0 # number of microseconds in a second


def readLineData(data):
    reflector = data[9].replace(' ', '')
    DATA_HEADER.state(data[0].replace(' ', ''))
    # LOG_DATETIME.info({'version': '1.2.3', 'buildhost': 'foo@bar'})
    LOG_TIMESTAMP.set(data[2])
    PROC_TIME.set(data[3])
    DL_ACHIEVED_RATE.set(float(data[4])*KBPS) # to 
    UL_ACHIEVED_RATE.set(float(data[5])*KBPS)
    DL_LOAD_PERCENT.set(data[6])
    UL_LOAD_PERCENT.set(data[7])
    ICMP_TIMESTAMP.set(data[8])
    REFLECTOR.labels(reflector).info({'address': reflector})
    SEQUENCE.labels(reflector).set(data[10])

    DL_OWD_BASELINE.labels(reflector).set(float(data[11])/US)
    DL_OWD.labels(reflector).set(float(data[12])/US)
    DL_OWD_DELTA_EWMA.labels(reflector).set(float(data[13])/US)
    DL_OWD_DELTA.labels(reflector).set(float(data[14])/US)
    DL_ADJ_DELAY_THR.labels(reflector).set(float(data[15])/US)

    UL_OWD_BASELINE.labels(reflector).set(float(data[16])/US)
    UL_OWD.labels(reflector).set(float(data[17])/US)
    UL_OWD_DELTA_EWMA.labels(reflector).set(float(data[18])/US)
    UL_OWD_DELTA.labels(reflector).set(float(data[19])/US)
    UL_ADJ_DELAY_THR.labels(reflector).set(float(data[20])/US)

    DL_SUM_DELAYS.labels(reflector).set(float(data[21])/US)
    DL_AVG_OWD_DELTA.labels(reflector).set(float(data[22])/US)
    DL_ADJ_OWD_DELTA_THR.labels(reflector).set(float(data[23])/US)

    UL_SUM_DELAYS.labels(reflector).set(float(data[24])/US)
    UL_AVG_OWD_DELTA.labels(reflector).set(float(data[25])/US)
    UL_ADJ_OWD_DELTA_THR.labels(reflector).set(float(data[26])/US)

    DL_LOAD_CONDITION.state(data[27].replace(' ', ''))
    UL_LOAD_CONDITION.state(data[28].replace(' ', ''))

    CAKE_DL_RATE.set(float(data[29])*KBPS)
    CAKE_UL_RATE.set(float(data[30])*KBPS)


def readLineLoad(data):
    DATA_HEADER.state(data[0].replace(' ', ''))
    # LOG_DATETIME.info({'version': '1.2.3', 'buildhost': 'foo@bar'})
    LOG_TIMESTAMP.set(data[2])
    PROC_TIME.set(data[3])
    DL_ACHIEVED_RATE.set(float(data[4])*KBPS)
    UL_ACHIEVED_RATE.set(float(data[5])*KBPS)

    CAKE_DL_RATE.set(float(data[6])*KBPS)
    CAKE_UL_RATE.set(float(data[7])*KBPS)


def readLineShaper(data):
    DATA_HEADER.state(data[0].replace(' ', ''))


def tail(f, n, offset=0):
    # https://stackoverflow.com/a/136280
    proc = subprocess.Popen(['tail', '-n', str(n + offset), f], stdout=subprocess.PIPE)
    lines = proc.stdout.readlines()
    return lines 


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    if DEBUG: logging.basicConfig(level=logging.DEBUG)
    else: logging.basicConfig(level=logging.INFO)

    start_http_server(EXPORTER_PORT)

    logging.info('Log file {}, metrics at: http://localhost:{}/metrics'.format(LOG_FILE, EXPORTER_PORT))

    while True:
        lastLines = tail(LOG_FILE, 5)

        for line in reversed(lastLines):
            data = line.decode().split(';')
            if data[0] == "DATA":
                logging.debug(line)
                readLineData(data)
                break
            elif data[0] == "LOAD":
                logging.debug(line)
                readLineLoad(data)
            elif data[0] == "SHAPER":
                logging.debug(line)
                readLineShaper(data)
        
        time.sleep(1)
        