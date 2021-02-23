import pandas as pd
import datetime
from django.utils import timezone
from django.conf import settings
from .models import Report, Alert
import os
import threading
import time

class Loader:

    def __init__(self):
        self.loader_status = False
        self.loader_worker = None
        self.last_check = 'Never'
        self.next_check = ''
        self.sleep_time = 5

    def set_status(self, status):
        self.loader_status = status

    def get_status(self):
        return self.loader_status


    def start_loader(self):
        self.loader_status = True
        if self.loader_worker is None or not self.loader_worker.is_alive():
            worker = threading.Thread(target=self.loader_loop, name='loader', daemon=True)
            worker.start()
            # we can check the status of thread by this variable
            self.loader_worker = worker

    def stop_loader(self):
        self.set_status(False)

    def get_loaded_reports(self):
        loadded_reports = []
        try:
            with open(settings.BASE_DIR / 'loadedReports.txt', 'r') as file:
                for report in file:
                    loadded_reports.append(report[:-1])
        except:
            pass
        return loadded_reports

    def add_loaded_report(sefl, report):
        with open(settings.BASE_DIR / 'loadedReports.txt', 'a') as file:
            file.write(report)
            file.write('\n')


    def log(self, msg):
        with open(settings.BASE_DIR / 'dataLoader.log', 'a') as file:
            file.write(msg)
            file.write('\n')

    def get_logs(self):
        logs = []
        try:
            with open(settings.BASE_DIR / 'dataLoader.log', 'r') as file:
                for line in file:
                    logs.append(line)
        except:
            logs = ['Somthing went wrong, could not load log file']
        
        return logs


    def loader_loop(self):
        while self.loader_status:
            self.load_data()
            time.sleep(self.sleep_time)


    def load_data(self):
        loaded_reports = self.get_loaded_reports()
        found = 0
        with os.scandir(settings.BASE_DIR / 'data/') as entries:
            for entry in entries:
                if entry.name not in loaded_reports:
                    try:
                        data = pd.read_csv(settings.BASE_DIR / 'data/' / entry)
                        
                        report = Report()
                        report_name = os.path.splitext(entry.name)[0]     # remove the extension
                        report.report_name = report_name
                        report.created_at = timezone.now()
                        report.created_by = 'System'
                        
                        report.save()

                        for row in range(data.shape[0]):
                            alert = Alert()
                            alert.report = report

                            alert.alert_type               =   data.iloc[row]['Alert_Type']
                            alert.alert_name               =   data.iloc[row]['Alert_Name']
                            alert.priorty                  =   data.iloc[row]['Priorty']
                            alert.malaware_family          =   data.iloc[row]['Malaware_family']
                            alert.http_hostname            =   data.iloc[row]['HTTP_Hostname']
                            alert.attack_reference         =   data.iloc[row]['Attack_reference']
                            alert.src_hostname             =   data.iloc[row]['Src_hostname']
                            alert.src_ip                   =   data.iloc[row]['Src_ip']
                            alert.dst_ip                   =   data.iloc[row]['Dst_ip']
                            alert.dst_country              =   data.iloc[row]['Dst_country']
                            alert.time                     =   data.iloc[row]['time']
                            alert.reference_url            =   data.iloc[row]['reference_URL']
                            alert.src_country              =   data.iloc[row]['src_Country']
                            alert.dst_hostname             =   data.iloc[row]['Dst_Hostname']
                            alert.recommendation           =   data.iloc[row]['Recommendation']
                            alert.description              =   data.iloc[row]['description']
                            alert.other_tls_subject        =   data.iloc[row]['Other_TLS_Subject']
                            alert.other_tls_fingerprint    =   data.iloc[row]['Other_TLS_Fingerprint']
                            alert.other_username           =   data.iloc[row]['Other_Username']
                            alert.other_source_nt_domain   =   data.iloc[row]['Other_SOURCE_NT_DOMAIN']
                            alert.other_destination_asset  =   data.iloc[row]['Other_DESTINATION_ASSET']
                            alert.other                    =   data.iloc[row]['OTHER']
                            
                            alert.save()

                              
                        self.add_loaded_report(entry.name)
                        log_time = timezone.now().today().strftime('%Y-%m-%d %H:%M:%S')
                        self.log(f'INFO [{log_time}] file {str(entry.name)} loaded')
                        found +=1

                    except Exception as e:
                        self.log(f'ERROR [{log_time}] file {str(entry.name)} did not load, error: {e}')
                        print('########################################',e)
                
                else:
                    pass
            
            now  = timezone.now().today().strftime('%Y-%m-%d %H:%M:%S')
            next = timezone.now().today() + datetime.timedelta(seconds=self.sleep_time)
            next = next.strftime('%Y-%m-%d  %H:%M:%S')
            if found > 0:
                self.last_check = f'on {now} found and loaded {found} report/s.'
                self.next_check = next
            else:
                self.last_check = f'{ now } Did not find new reports'
                self.next_check = next


loader = Loader()