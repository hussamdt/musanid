from django.contrib import admin
from .models import Report, Alert


class AlertInline(admin.StackedInline):
    model = Alert
    extra = 1

class ReportAdmin(admin.ModelAdmin):
    
    fieldsets = [
                  ( None, {'fields': ['report_name', 'created_at']}),
                ]
            
    list_display =  ('report_name', 'created_at', 'created_by')
    
    list_filter = ['report_name', 'created_at']
    search_fields = ['report_name', 'created_by']
    
    inlines = [AlertInline,]

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user.username
        super().save_model(request, obj, form, change)

admin.site.register(Report, ReportAdmin)

class AlertAdmin(admin.ModelAdmin):
    
    fieldsets = [
                  ( None, {'fields': ['report', 'alert_type', 'alert_name','priorty', 'malaware_family', 'http_hostname', 'reference_url']}),
                  ('Source Information', {'fields': ['src_hostname', 'src_ip', 'src_country', 'attack_reference']}),
                  ('Destination Information', {'fields': ['dst_ip', 'dst_hostname', 'dst_country']}),
                  ('Recommendation & Description', {'fields': ['recommendation', 'description']}),
                  ('Others', {'fields': ['other_tls_subject', 'other_tls_fingerprint', 'other_username', 'other_source_nt_domain', 'other_destination_asset', 'other']}),
                  ('Time', {'fields': ['time']})
            ]
            
    list_display =  ('alert_name', 'alert_type', 'priorty', 'time')
    
    list_filter = ['time']
    search_fields = ['alert_name', 'alert_type']

admin.site.register(Alert, AlertAdmin)

