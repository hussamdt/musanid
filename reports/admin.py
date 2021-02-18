from django.contrib import admin
from .models import Report


class ReportAdmin(admin.ModelAdmin):
    
    fieldsets = [
                  ( None, {'fields': ['alert_type', 'alert_name','priorty', 'malaware_family', 'http_hostname', 'reference_url']}),
                  ('Source Information', {'fields': ['src_hostname', 'src_ip', 'src_country', 'attack_reference']}),
                  ('Destination Information', {'fields': ['dst_ip', 'dst_hostname', 'dst_country']}),
                  ('Recommendation & Description', {'fields': ['recommendation', 'description']}),
                  ('Others', {'fields': ['other_tls_subject', 'other_tls_fingerprint', 'other_username', 'other_source_nt_domain', 'other_destination_asset', 'other']}),
                  ('Time', {'fields': ['time']})
            ]
            
    list_display =  ('alert_name', 'alert_type', 'priorty', 'time')
    
    list_filter = ['time']
    search_fields = ['alert_name', 'alert_type']

admin.site.register(Report, ReportAdmin)