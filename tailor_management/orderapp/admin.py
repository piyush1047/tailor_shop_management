from django.contrib import admin
from orderapp.models import Order
from import_export.admin import ImportExportModelAdmin

class OrderAdmin(ImportExportModelAdmin):
    list_display = ('order_name', 'customer', 'description','order_date','deliver_date','priority','Total_payment','Advance_Payment','due_payment','quantity','product_img','garment_type','get_measurements')
    search_fields = ('order_name', 'customer')
    list_filter = ('garment_type',)

    def get_measurements(self, obj):
        if obj.garment_type == 'Topwear':
            return f"Neck: {obj.neck_size}, Chest: {obj.chest_size}, Sleeve: {obj.sleeve_length},Shirt-length: {obj.shirt_length},stomach: {obj.stomach},heap: {obj.heap},Shoulder: {obj.shoulder},Remark: {obj.remark_shirt}"
        elif obj.garment_type == 'Bottomwear':
            return f"Waist: {obj.waist_size}, Length: {obj.length_size},pant-heap: {obj.pant_heap},heap_loosing: {obj.heap_loosing},mohri: {obj.mohri},Thai: {obj.thai},Knee_size: {obj.Knee_Size},langot: {obj.langot},pindli: {obj.pindli},Remark: {obj.remark}"
        elif obj.garment_type == 'Top-Bottom':
            return f"Waist: {obj.waist_size}, Length: {obj.length_size},pant-heap: {obj.pant_heap},heap_loosing: {obj.heap_loosing},mohri: {obj.mohri},Thai: {obj.thai},Knee_size: {obj.Knee_Size},langot: {obj.langot},pindli: {obj.pindli},Remark: {obj.remark},Neck: {obj.neck_size}, Chest: {obj.chest_size}, Sleeve: {obj.sleeve_length},Shirt-length: {obj.shirt_length},stomach: {obj.stomach},heap: {obj.heap},Shoulder: {obj.shoulder},Remark: {obj.remark}"
        return "N/A"
    
    get_measurements.short_description = 'Measurements'

# Register the Order model with the admin site
admin.site.register(Order, OrderAdmin)
