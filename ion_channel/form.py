from django.forms import ModelForm
from django import forms
from .models import Reference, IonChannel, Graph


class ReferenceForm(ModelForm):
    class Meta:
        model = Reference
        exclude = ('username','create_date')

class GraphForm(ModelForm):
    class Meta:
        model = Graph
        exclude = ('digitized_plot','digitized_plot_file')

class IonChannelForm(ModelForm):
    class Meta:
        model = IonChannel
        exclude = ('username','create_date', 'last_update')

class PubForm(forms.Form):
    DOI = forms.CharField(max_length=100,required=False,label='Search by DOI')
    PMID = forms.IntegerField(required=False,label='Search by PMID')
