import json
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from formtools.wizard.views import SessionWizardView
from datetime import datetime

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from web_app.views import AjaxMixinListView, AjaxMixinCreateView, AjaxMixinUpdateView, AjaxMixinDeleteView
from .models import *
from .form import *
from ion_channel.models import Graph, PatchClamp

def index(request):
    return render(request, 'channelworm/index.html')


class IonChannelGeneList(ListView):
    model = IonChannelGene
    context_object_name = 'ion_channels'

    def get_context_data(self, **kwargs):
        context = super(IonChannelGeneList, self).get_context_data(**kwargs)
        context['graphs'] = Graph.objects.filter(x_axis_type='T', y_axis_type='I')
        # context['Graphs'] = Graph.objects.filter(ion_channel_id=int(self.kwargs['pk']))
        return context


class IonChannelGeneDetail(AjaxMixinUpdateView, UpdateView):
    model = IonChannelGene
    template_name_suffix = '_detail'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(IonChannelGeneDetail, self).get_context_data(**kwargs)
        context['ion_channel'] = IonChannelGene.objects.filter(id=int(self.kwargs['pk']))
        context['graphs'] = Graph.objects.filter(ion_channel_id=int(self.kwargs['pk']))
        context['patch_clamps'] = PatchClamp.objects.filter(id__in=[graph.id for graph in context['graphs']])
        context['proteins'] = Protein.objects.filter(ion_channel_id=int(self.kwargs['pk']))
        return context


class IonChannelGeneCreate(AjaxMixinCreateView, CreateView):
    model = IonChannelGene
    form_class = IonChannelGeneForm
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('channelworm:ion-channel-gene-index')
    json_success_response = {'status': 'success', 'result': 'Ion Channel saved.'}

    def form_valid(self, form):
        form.instance.username = self.request.user
        form.instance.create_date = datetime.now()
        form.instance.last_update = datetime.now()
        return super(IonChannelGeneCreate, self).form_valid(form)


class IonChannelGeneUpdate(AjaxMixinUpdateView, UpdateView):
    model = IonChannelGene
    form_class = IonChannelGeneForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('channelworm:ion-channel-index')
    json_success_response = {'status': 'success', 'result': 'Ion Channel updated.'}

    def form_valid(self, form):
        form.instance.last_update = datetime.now()
        return super(IonChannelGeneUpdate, self).form_valid(form)


class IonChannelGeneDelete(DeleteView):
    model = IonChannelGene
    success_url = reverse_lazy('channelworm:ion-channel-gene-index')


class ProteinList(ListView):
    model = Protein
    context_object_name = 'protein'


class ProteinCreate(CreateView):
    model = Protein
    context_object_name = 'protein'


class ProteinUpdate(UpdateView):
    model = Protein
    context_object_name = 'protein'


class ProteinDelete(DeleteView):
    model = Protein
    success_url = reverse_lazy('channelworm:ion-channel-gene-index')
