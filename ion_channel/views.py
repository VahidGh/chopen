import json
import os
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from formtools.wizard.views import SessionWizardView
from datetime import datetime
from django.conf import settings
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
import sys
from web_app.views import AjaxMixinListView, AjaxMixinCreateView, AjaxMixinUpdateView, AjaxMixinDeleteView, AjaxResponseMixin
from .models import *
from .form import *
from channelworm.models import *
# from fitter import initiators


def index(request):
    return render(request, 'ion_channel/index.html')


class ReferenceList(AjaxMixinListView, ListView):
    model = Reference
    context_object_name = 'references'

    def get_queryset(self):
        if self.kwargs.get("ionChannelId"):
            ref_id = None
            if Graph.objects.filter(ion_channel_id=self.kwargs.get("ionChannelId")):
                graph = Graph.objects.get(ion_channel_id=self.kwargs.get("ionChannelId"))
                ref_id = graph.reference_id
            return Reference.objects.filter(id=ref_id)
        return Reference.objects.all()


class ReferenceCreate(AjaxMixinCreateView, CreateView):
    model = Reference
    form_class = ReferenceForm
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('ion_channel:reference-index')
    json_success_response = {'status': 'success', 'result': 'New reference saved.'}

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super(ReferenceCreate, self).form_valid(form)


class ReferenceWizard(SessionWizardView):
    template_name = 'ion_channel/reference_auto_create_form.html'

    def done(self, form_list, **kwargs):

        new = Reference()
        new.username = self.request.user
        for k, v in self.get_cleaned_data_for_step('1').iteritems():
            setattr(new, k, v)
        new.save()
        return redirect('/ion_channel/reference')

    def get_form_initial(self, step):
        initial = {}
        if step == '1':

            from metapub import pubmedfetcher

            data = self.get_cleaned_data_for_step('0')
            fetch = pubmedfetcher.PubMedFetcher()
            if data['DOI'] != '':
                article = fetch.article_by_doi(data['DOI'])
            elif data['PMID'] != '':
                article = fetch.article_by_pmid(data['PMID'])

            initial['doi'] = article.doi
            initial['PMID'] = article.pmid
            initial['title'] = article.title
            initial['citation'] = article.__str__()
            initial['year'] = article.year
            initial['authors'] = article.authors_str
            initial['journal'] = article.journal
            initial['volume'] = article.volume
            initial['issue'] = article.issue
            initial['pages'] = article.pages
            initial['url'] = article.url

        return initial


class ReferenceUpdate(AjaxMixinUpdateView, UpdateView):
    model = Reference
    form_class = ReferenceForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('ion_channel:reference-index')
    json_success_response = {'status': 'success', 'result': 'Reference updated.'}


class ReferenceDelete(DeleteView):
    model = Reference
    success_url = reverse_lazy('ion_channel:reference-index')

@login_required
def ionchannel_wizard(request):
    return render(request, 'ion_channel/ionchannel_wizard.html')

@login_required
def ionchannel_dashboard(request):
    return render(request, 'ion_channel/ionchannel_dashboard.html')


class CellCreate(CreateView):
    model = Cell
    fields = '__all__'
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('ion_channel:ion-channel-index')


class IonChannelList(ListView):
    model = IonChannel
    context_object_name = 'ion_channels'

    def get_context_data(self, **kwargs):
        context = super(IonChannelList, self).get_context_data(**kwargs)
        context['graphs'] = Graph.objects.filter(x_axis_type='T', y_axis_type='I')
        # context['Graphs'] = Graph.objects.filter(ion_channel_id=int(self.kwargs['pk']))
        return context


class IonChannelDetail(AjaxMixinUpdateView, UpdateView):
    model = IonChannel
    template_name_suffix = '_detail'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(IonChannelDetail, self).get_context_data(**kwargs)
        context['ion_channel'] = IonChannel.objects.filter(id=int(self.kwargs['pk']))
        context['graphs'] = Graph.objects.filter(ion_channel_id=int(self.kwargs['pk']))
        context['patch_clamps'] = PatchClamp.objects.filter(id__in=[graph.id for graph in context['graphs']])
        return context


class IonChannelDetailAjax(AjaxMixinUpdateView, UpdateView):
    template_name = 'ion_channel/ionchannel_detail_ajax.html'
    model = IonChannel
    fields = '__all__'


class IonChannelCreate(AjaxMixinCreateView, CreateView):
    model = IonChannel
    form_class = IonChannelForm
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('ion_channel:ion-channel-index')
    json_success_response = {'status': 'success', 'result': 'Ion Channel saved.'}

    def form_valid(self, form):
        form.instance.username = self.request.user
        form.instance.create_date = datetime.now()
        form.instance.last_update = datetime.now()
        return super(IonChannelCreate, self).form_valid(form)


class IonChannelUpdate(AjaxMixinUpdateView, UpdateView):
    model = IonChannel
    form_class = IonChannelForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('ion_channel:ion-channel-index')
    json_success_response = {'status': 'success', 'result': 'Ion Channel updated.'}

    def form_valid(self, form):
        form.instance.last_update = datetime.now()
        return super(IonChannelUpdate, self).form_valid(form)


class IonChannelDelete(DeleteView):
    model = IonChannel
    success_url = reverse_lazy('ion_channel:ion-channel-index')


class IonChannelModelList(ListView):
    model = IonChannelModel
    context_object_name = 'ion_channel_models'


class IonChannelModelCreate(CreateView):
    model = IonChannelModel
    fields = '__all__'
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('ion_channel:ion-channel-model-index')


class IonChannelModelUpdate(UpdateView):
    model = IonChannelModel
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('ion_channel:ion-channel-model-index')


class IonChannelModelDelete(DeleteView):
    model = IonChannelModel
    success_url = reverse_lazy('ion_channel:ion-channel-model-index')


class PatchClampList(AjaxMixinListView, ListView):
    model = PatchClamp
    context_object_name = 'patch_clamps'

    def get_queryset(self):
        if self.kwargs.get("ionChannelId"):
            pc_id = None
            if Graph.objects.filter(ion_channel_id=self.kwargs.get("ionChannelId")):
                graph = Graph.objects.get(ion_channel_id=self.kwargs.get("ionChannelId"))
                pc_id = graph.patch_clamp_id
            return PatchClamp.objects.filter(id=pc_id)
        return PatchClamp.objects.all()


class PatchClampDetail(UpdateView):
    model = PatchClamp
    template_name_suffix = '_detail'
    fields = '__all__'


class PatchClampCreate(AjaxMixinCreateView, CreateView):
    model = PatchClamp
    fields = '__all__'
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('ion_channel:patch-clamp-index')
    json_success_response = {'status': 'success', 'result': 'New patch-clamp saved.'}

    def get_initial(self):
        if self.kwargs.get("ionChannelId"):
            return {
                "ion_channel": self.kwargs.get("ionChannelId")
            }


class PatchClampUpdate(AjaxMixinUpdateView, UpdateView):
    model = PatchClamp
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('ion_channel:patch-clamp-index')
    json_success_response = {'status': 'success', 'result': 'Patch-clamp updated.'}


class PatchClampDelete(AjaxMixinDeleteView, DeleteView):
    model = PatchClamp
    success_url = reverse_lazy('ion_channel:patch-clamp-index')
    json_success_response = {'status': 'success', 'result': 'Patch-clamp deleted.'}


class GraphList(AjaxMixinListView, ListView):
    model = Graph
    context_object_name = 'graphs'

    def get_queryset(self):
        if self.kwargs.get("ionChannelId"):
            ion_channel = get_object_or_404(IonChannel, id__exact=self.kwargs.get("ionChannelId"))
            return Graph.objects.filter(ion_channel=ion_channel)
        return Graph.objects.all()


class GraphCreate(AjaxMixinCreateView, CreateView):
    model = Graph
    form_class = GraphForm
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('ion_channel:graph-index')
    json_success_response = {'status': 'success', 'result': 'New graph saved.'}

    def get_initial(self):
        if self.kwargs.get('ionChannelId'):
            return {
                "ion_channel": self.kwargs.get('ionChannelId')
            }


class GraphUpdate(AjaxMixinUpdateView, UpdateView):
    model = Graph
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('ion_channel:graph-index')
    json_success_response = {'status': 'success', 'result': 'Graph updated.'}


class GraphDelete(AjaxMixinDeleteView, DeleteView):
    model = Graph
    success_url = reverse_lazy('ion_channel:graph-index')
    json_success_response = {'status': 'success', 'result': 'Graph deleted.'}


class GraphDataList(ListView):
    model = GraphData
    context_object_name = 'graph_data'

    def get_queryset(self):
        print(self.kwargs)
        self.graph = get_object_or_404(Graph, id=self.kwargs['graph_id'])
        return GraphData.objects.filter(graph=self.graph)

class GraphDataUpdate(UpdateView):
    model = GraphData
    fields = '__all__'
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('ion_channel:graph-data-index', kwargs={'graph_id': self.object.graph_id})


class GraphDataDelete(DeleteView):
    model = GraphData

    def get_success_url(self):
        return reverse_lazy('ion_channel:graph-data-index', kwargs={'graph_id': self.object.graph_id})


def save_graph_data(request):
    response_data = {'status': 'error', 'result': 'Saving graph data failed'}
    print(response_data)
    if request.method == 'POST':
        print("is post")
        graph = get_object_or_404(Graph, pk=request.POST.get("graph_id"))
        data = GraphData(graph=graph, series_name=request.POST.get("series_name"),
                         series_data=request.POST.get("series_data"))
        data.save()

        # TODO: get from api
        # graph_id = request.POST.get("graph_id")
        # myInitiator = initiators.Initiator()
        # media_root = settings.MEDIA_ROOT
        # media_file = 'ion_channel/plots/' + graph_id + '/'
        # fp = media_root + '/' + media_file
        # if not os.path.exists(fp):
        #     os.mkdir(fp)
        # plot_file = media_file + myInitiator.get_graphdata_from_db(graph_id, plot=True, path=fp)
        # graph = Graph.objects.filter(id=graph_id)
        # graph.update(digitized_plot=plot_file + '.png', digitized_plot_file=plot_file + '.pickle')
        response_data = {'status': 'success', 'result': 'New graph saved.'}

    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )


def save_digitized_plot(request, pk=None):
    response_data = {'status': 'error', 'result': 'Saving digitized plot failed'}
    print(response_data)
    if request.method == 'POST':
        graph_id = request.POST.get("graph_id")
    else:
        graph_id = pk

    # TODO: get from api
    # myInitiator = initiators.Initiator()
    # media_root = settings.MEDIA_ROOT
    # media_file = 'ion_channel/plots/' + graph_id + '/'
    # fp = media_root + '/' + media_file
    # if not os.path.exists(fp):
    #     os.mkdir(fp)
    # plot_file = media_file + myInitiator.get_graphdata_from_db(graph_id, plot=True, path=fp)
    # graph = Graph.objects.filter(id=graph_id)
    # graph.update(digitized_plot=plot_file + '.png', digitized_plot_file=plot_file + '.pickle')
    response_data = {'status': 'success', 'result': 'New digitized plot saved.'}

    return redirect('ion_channel:graph-index')
    # return reverse_lazy('ion_channel:graph-index')

