from django.db import models
from django.utils import timezone


class Report(models.Model):
    report_name     = models.CharField('Report Name', max_length=100)
    created_at       = models.DateTimeField('Time', auto_now_add=True)
    created_by      = models.CharField('Created By', max_length=100)

    # generated URL
    generated_url   = models.CharField('Generated URL', max_length=200)

    def __str__(self):
        return self.report_name

    def get_full_url(self, request):
        url_prefix = str(request.scheme) + '://' + str(request.get_host())
        return url_prefix + self.generated_url


class Alert(models.Model):
    
    report                  = models.ForeignKey('Report', on_delete=models.CASCADE)

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
    time                    = models.CharField('Time', max_length=100)
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

