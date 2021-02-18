import pandas as pd
from reports.models import Report

data = pd.read_csv('data.csv')

for row in range(data.shape[0]):
    
    report = Report()
    
    report.alert_type               =   data.iloc[row]['Alert_Type']
    report.alert_name               =   data.iloc[row]['Alert_Name']
    report.priorty                  =   data.iloc[row]['Priorty']
    report.malaware_family          =   data.iloc[row]['Malaware_family']
    report.http_hostname            =   data.iloc[row]['HTTP_Hostname']
    report.attack_reference         =   data.iloc[row]['Attack_reference']
    report.src_hostname             =   data.iloc[row]['Src_hostname']
    report.src_ip                   =   data.iloc[row]['Src_ip']
    report.dst_ip                   =   data.iloc[row]['Dst_ip']
    report.dst_country              =   data.iloc[row]['Dst_country']
    report.time                     =   data.iloc[row]['time']
    report.reference_url            =   data.iloc[row]['reference_URL']
    report.src_country              =   data.iloc[row]['src_Country']
    report.dst_hostname             =   data.iloc[row]['Dst_Hostname']
    report.recommendation           =   data.iloc[row]['Recommendation']
    report.description              =   data.iloc[row]['description']
    report.other_tls_subject        =   data.iloc[row]['Other_TLS_Subject']
    report.other_tls_fingerprint    =   data.iloc[row]['Other_TLS_Fingerprint']
    report.other_username           =   data.iloc[row]['Other_Username']
    report.other_source_nt_domain   =   data.iloc[row]['Other_SOURCE_NT_DOMAIN']
    report.other_destination_asset  =   data.iloc[row]['Other_DESTINATION_ASSET']
    report.other                    =   data.iloc[row]['OTHER']
    
    report.save()
    
    print('Record saved ', row)