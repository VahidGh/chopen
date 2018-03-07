from django.contrib import admin
from .models import *
admin.site.register(Cell)
admin.site.register(PatchClamp)
admin.site.register(Reference)
admin.site.register(IonChannel)
admin.site.register(IonChannelModel)
admin.site.register(Graph)
admin.site.register(GraphData)
# Register your models here.
