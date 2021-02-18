from django.db import models


class Report(models.Model):
    
    alert_type              = models.CharField('Alert Type', max_length=100)
    alert_name              = models.CharField('Alert Name', max_length=100)
    priorty                 = models.CharField('Priorty', max_length=100)
    malaware_family         = models.CharField('Malaware Family', max_length=100)
    http_hostname           = models.CharField('HTTP Hostname', max_length=200)
    attack_reference        = models.CharField('Attack Reference', max_length=50)
    src_hostname            = models.CharField('Source Hostname', max_length=100)
    src_ip                  = models.CharField('Source IP', max_length=50)
    dst_ip                  = models.CharField('Destination IP', max_length=50)
    dst_country             = models.CharField('Destination Country', max_length=100)
    time                    = models.DateTimeField('Time')
    reference_url           = models.CharField('Reference URL', max_length=200)
    src_country             = models.CharField('Source Country', max_length=100)
    dst_hostname            = models.CharField('Destination Hostname', max_length=100)
    recommendation          = models.TextField('Recommendation')
    description             = models.TextField('Description')
    other_tls_subject       = models.CharField('Other TLS Subject', max_length=255)
    other_tls_fingerprint   = models.CharField('Other TLS Fingerprint', max_length=255)
    other_username          = models.CharField('Other Username', max_length=100)
    other_source_nt_domain  = models.CharField('Other source NT domain', max_length=100)
    other_destination_asset = models.CharField('Other destination asset', max_length=100)
    other                   = models.CharField('Other', max_length=100)
    
    # generated URL
    generated_url           = models.CharField('Generated URL', max_length=200)