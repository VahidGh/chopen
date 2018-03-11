from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


Cell_Type_CHOICES = (
    ('Xenopus Oocytes', 'Xenopus Oocytes'),
    ('Caenorhabditis elegans body wall muscle', 'Caenorhabditis elegans body wall muscle'),
    ('HEK', 'HEK'),
    ('CHO', 'CHO'),
    ('COS-7', 'COS-7'),
    ('Generic', 'Generic'),
)


class Cell(models.Model):
    cell_type = models.CharField(max_length=300,choices=Cell_Type_CHOICES,default='Xenopus Oocytes')
    membrane_capacitance = models.FloatField(default=2e-7, max_length=200,blank=True, null=True,verbose_name='Capacitance of the membrane (F)')
    specific_capacitance = models.FloatField(default=0.01,blank=True, null=True,verbose_name='Specific capacitance of the membrane (F/m2)')
    area = models.FloatField(default=2e-5, blank=True, null=True,verbose_name='Total area of the cell (m2)')

    def __unicode__(self):
        return self.cell_type

Method_CHOICES = (
    ('TMVC', 'Two Microelectrode Voltage Clamp'),
    ('Inside-Out', 'Inside-Out Patch Clamp'),
)

# TODO: Consider measurement fields: https://pypi.python.org/pypi/django-measurement


class PatchClamp(models.Model):
    cell = models.ForeignKey(Cell, default=1, on_delete=models.CASCADE)
    method = models.CharField(max_length=200,choices=Method_CHOICES,default='TMVC')
    duration = models.FloatField(verbose_name='Patch-Clamp Duration (ms)')
    start_time = models.FloatField(default=0,verbose_name='Start time (ms)')
    end_time = models.FloatField(verbose_name='End time (ms) (default=duration)')
    holding_potential = models.FloatField(verbose_name='Holding potential (mV)')
    voltage_start = models.FloatField(verbose_name='Initial voltage (mV)')
    voltage_end = models.FloatField(verbose_name='Final voltage (mV)')
    voltage_steps = models.FloatField(verbose_name='Voltage steps (mV)', default=10)
    depolarization_step = models.FloatField(blank=True, null=True, verbose_name='Depolarization step (mV)')
    cell_age = models.FloatField(default=None, blank=True, null=True,verbose_name='Age of the cell (days)')
    temperature = models.FloatField(default=21, blank=True, null=True,verbose_name='Temperature (Celsius)')
    Ca_concentration = models.FloatField(default=None, blank=True, null=True,verbose_name='Initial molar concentration of Calcium (uM)')
    Cl_concentration = models.FloatField(default=None, blank=True, null=True,verbose_name='Initial molar concentration of Chloride (mM)')
    blockers = models.CharField(max_length=300, blank=True, null=True, verbose_name='Ion channel blockers (e.g. 500e-6 Cd2+,...)')
    extra_solution = models.TextField(blank=True, null=True, verbose_name='Extracellular Solution (e.g. 140e-3 NaCl, 5e-3 KCl,...)')
    pipette_solution = models.TextField(blank=True, null=True, verbose_name='Pipette Solution (e.g. 120e-3 KCl, 20e-3 KOH,...)')

    def __unicode__(self):
        return repr(self.cell) + ", " + str(self.method) + ", " + str(self.temperature) + " (C), " + "Holding Potential: " + \
               str(self.holding_potential) + " (mV), From: " + str(self.voltage_start) + ", To: " + str(self.voltage_end) + \
               ", Duration: "+str(self.duration) + " (ms), From: " + str(self.start_time) + ", To: " + str(self.end_time) + \
               ", [Ca]: " + str(self.Ca_concentration) + " (mM)"


Reference_Type_CHOICES = (
    ('Genomics', 'Genomics'),
    ('Proteomics', 'Proteomics'),
    ('Electrophysiology', 'Electrophysiology'),
    ('Combination', 'Combination')
)


class Reference(models.Model):
    doi = models.CharField(max_length=300, unique=True, blank=True, null=True)
    PMID = models.CharField(max_length=300, unique=True, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    citation = models.TextField(blank=True, null=True)
    year = models.CharField(max_length=300,blank=True, null=True)
    authors = models.CharField(max_length=300,blank=True, null=True)
    journal = models.CharField(max_length=300,blank=True, null=True)
    volume = models.CharField(max_length=300,blank=True, null=True)
    issue = models.CharField(max_length=300,blank=True, null=True)
    pages = models.CharField(max_length=300,blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True)
    username = models.ForeignKey(User,verbose_name='Contributor', on_delete=models.CASCADE)
    tags = models.TextField(blank=True, null=True)
    subject = models.CharField(max_length=300,choices=Reference_Type_CHOICES,default='Electrophysiology')
    file_url = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.PMID + ", " + self.citation + ", " + self.year

    def clean(self):
        if self.doi == '' and self.PMID == '':
            raise ValidationError(_('Enter either DOI or PMID.'))


Channel_Type_CHOICES = (
    ('Voltage-gated potassium channels', 'KV'),
    ('Calcium-activated potassium channels', 'KCa'),
    ('Inwardly rectifying potassium channels', 'Kir'),
    ('Two-P potassium channels', 'K2p'),
    ('Voltage-gated calcium channels', 'CaV'),
    ('Voltage-gated sodium channels', 'NaV'),
    ('Voltage-gated proton channels', 'HV'),
    ('Voltage-gated chloride channels', 'ClV'),
    ('Transient receptor potential cation channels', 'TRP'),
    ('Cation channels sperm associated', 'CATSPER'),
    ('Cyclic nucleotide gated channels', 'CNG'),
    ('Two pore segment channels', 'TPCN'),
    ('Unknown', 'Unknown'),
)
Ion_Type_CHOICES = (
    ('Ca2+', 'Calcium'),
    ('K+', 'Potassium'),
    ('Cl-', 'Chloride'),
    ('Na+', 'Sodium'),
    ('Cation', 'Cation')
)
ANIMAL_CHOICES = (
    ('Homo sapiens (Human)', 'Human'),
    ('Rattus norvegicus (Rat)', 'Rat'),
    ('Mus musculus (Mouse)', 'Mouse'),
    ('Oryctolagus cuniculus (rabbit)', 'Rabbit'),
    ('Canis lupus familiaris (Dog)', 'Dog'),
    ('Xenopus laevis (African clawed frog)', 'African clawed frog'),
    ('Drosophila melanogaster (Fruit fly)', 'Fruit fly'),
    ('Caenorhabditis elegans (C. elegans)', 'C. elegans'),
    ('Danio rerio (zebrafish)', 'Zebrafish'),
    ('Panulirus interruptus (California spiny lobster)', 'California spiny lobster'),
    ('Panulirus argus (Caribbean spiny lobster)', 'Caribbean spiny lobster'),
    ('Aplysia californica (California sea hare)', 'California sea hare'),
    ('Schistosoma mansoni (Blood fluke)', 'Blood fluke'),
    ('Polyorchis penicillatus (penicillate jellyfish)', 'Penicillate Jellyfish'),
    ('Mustela putorius furo (domestic ferret)', 'Domestic ferret'),
    ('Doryteuthis pealeii (Longfin inshore squid) (Loligo pealeii)', 'Loligo pealeii'),
    ('Aplysia sp. (Sea hare)', 'Sea hare'),
    ('Ictalurus punctatus (channel catfish)', 'Channel catfish' ),
    ('Polyorchis penicillatus (penicillate jellyfish)', 'Penicillate jellyfish'),
    ('Squalus acanthias (Spiny dogfish)', 'Spiny dogfish'),
    ('Nematostella vectensis (starlet sea anemone)', 'Starlet sea anemone'),
    ('Cavia porcellus (domestic guinea pig)', 'Domestic guinea pig'),
    ('Blattella germanica (German cockroach)', 'German cockroach'),
    ('Ciona intestinalis (vase tunicate)', 'Vase tunicate'),
    ('Arabidopsis thaliana (thale cress)', 'Arabidopsis thaliana (thale cress)'),
    ('Zea mays', 'Zea mays'),
    ('Others', 'Others'),
)
Current_Type_CHOICES = (
    ('A-type', 'IA'),
    ('Delayed rectifier', 'Id'),
    ('M-type', 'IM'),
    ('Inwardly-rectifying', 'Iir'),
    ('Inwardly-rectifying and A-type', 'IA-Iir'),
    ('Outwardly-rectifying', 'Io'),
    ('Proton Current', 'Ih'),
    ('Inwardly-rectifying Proton Current', 'Ih-Iir'),
    ('Calcium Current', 'ICa'),
    ('Calcium L-type Current', 'ICa-L'),
    ('Calcium P/Q-type Current', 'ICa-P/Q'),
    ('Calcium N-type Current', 'ICa-N'),
    ('Calcium R-type Current', 'ICa-R'),
    ('Sodium Current', 'INa'),
    ('S-type', 'IS'),
)


class IonChannel(models.Model):
    channel_name = models.CharField(max_length=300, unique=True)
    full_name = models.CharField(blank=True, null=True, max_length=300)
    gene_symbol = models.CharField(null=True, max_length=300)
    isoform = models.CharField(blank=True, null=True, max_length=20)
    animal = models.CharField(blank=True, null=True, max_length=200,choices=ANIMAL_CHOICES)
    channel_type = models.CharField(blank=True, null=True, max_length=300,choices=Channel_Type_CHOICES)
    class_symbol = models.CharField(blank=True, null=True, max_length=300)
    subfamily = models.CharField(blank=True, null=True, max_length=20)
    member = models.CharField(blank=True, null=True, max_length=20)
    current_type = models.CharField(blank=True, null=True, max_length=300)
    aliases = models.CharField(blank=True, null=True, max_length=300)
    ion_type = models.CharField(blank=True, null=True, max_length=200,choices=Ion_Type_CHOICES)
    uniprot_id = models.CharField(blank=True, null=True, max_length=300)
    refSeq_id = models.CharField(blank=True, null=True, max_length=300)
    gene_id = models.CharField(blank=True, null=True, max_length=300)
    conductance = models.FloatField(default=10, blank=True, null=True, verbose_name='Single Channel Conductance (ps)')
    sequence = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField()
    last_update = models.DateTimeField(auto_now=True)
    username = models.ForeignKey(User,verbose_name='Curator', on_delete=models.CASCADE)
    references = models.ManyToManyField(Reference, blank=True)
    links = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.channel_name


Axis_Type_CHOICES = (
    ('I', 'Current'),
    ('T', 'Time'),
    ('Tau_a', 'Activation Time'),
    ('Tau_i', 'Inactivation Time'),
    ('I_ss', 'Steady-state Current'),
    ('I_peak', 'Peak Current'),
    ('I_norm', 'Normalized Current'),
    ('I_norm_i', 'Normalized Inactivation Current'),
    ('V', 'Voltage'),
    ('G', 'Conductance'),
    ('G/G_max', 'G/G_max'),
    ('Po', 'Open Probability'),
    ('Po_Peak', 'Peak Open Probability'),
    ('Ca_concentration', 'Calcium Concentration'),
    ('Cl_concentration', 'Chloride Concentration'),
    ('Bar', 'Bar Chart'),
)


class Graph(models.Model):
    ion_channel = models.ForeignKey(IonChannel, on_delete=models.CASCADE)
    patch_clamp = models.ForeignKey(PatchClamp, on_delete=models.CASCADE)
    reference = models.ForeignKey(Reference, on_delete=models.CASCADE)
    x_axis_type = models.CharField(max_length=50, choices=Axis_Type_CHOICES, default='T')
    x_axis_unit = models.CharField(max_length=50,verbose_name='Axis unit in the original figure (e.g. ms)', default='ms')
    x_axis_toSI = models.FloatField(default=1e-3,verbose_name='Multiply by this value to convert to SI (e.g. 1e-3)')
    y_axis_type = models.CharField(max_length=50, choices=Axis_Type_CHOICES, default='I')
    y_axis_unit = models.CharField(max_length=50,verbose_name='Axis unit in the original figure (e.g. uA)', default='uA')
    y_axis_toSI = models.FloatField(default=1e-6,verbose_name='Multiply by this value to convert to SI (e.g. 1e-6)')
    figure_ref_address = models.CharField(max_length=50,verbose_name='Figure number (e.g. 2A)')
    figure_ref_caption = models.TextField(verbose_name='Figure caption')
    file = models.ImageField(upload_to='ion_channel/graph/%Y/%m/%d')
    digitized_plot = models.ImageField(blank=True, null=True, upload_to='ion_channel/plots')
    digitized_plot_file = models.FileField(blank=True, null=True, upload_to='ion_channel/plots')
    # interpolated_plot = models.ImageField(blank=True, null=True, upload_to='ion_channel/plots')
    # interpolated_plot_file = models.FileField(blank=True, null=True, upload_to='ion_channel/plots')
    comments = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return str(self.y_axis_type) + "-" + str(self.x_axis_type) + " relationship of " + repr(self.ion_channel) + ". From: Fig. " + \
                   str(self.figure_ref_address) + ", " + self.reference.citation + ", " + self.reference.year


class GraphData(models.Model):
    graph = models.ForeignKey(Graph, on_delete=models.CASCADE)
    series_name = models.CharField(max_length=200)
    series_data = models.TextField()
    # interpolated_data = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.series_name

    def asarray(self):
        xy = self.series_data.splitlines()
        data = list()
        for row in xy:
            data += [map(float, row.split(','))]

        return data

    def interpolate(self, range=100):
        import numpy as np
        xp, yp = list(map(list, zip(*self.asarray())))
        x = np.linspace(np.min(xp), np.max(xp), range)
        return (x, np.interp(x, xp, yp))

Modeling_Method_CHOICES = (
    ('Experimental', 'Experimental'),
    ('Estimated', 'Estimated')
)

Model_Type_CHOICES = (
    ('HH', 'Hodgkin-Huxley'),
    ('Markov', 'Markov')
)


class IonChannelModel(models.Model):
    channel_name = models.ForeignKey(IonChannel, on_delete=models.CASCADE)
    cell_name = models.ForeignKey(Cell, blank=True, null=True, on_delete=models.CASCADE)
    model_type = models.CharField(max_length=300,choices=Model_Type_CHOICES, default='HH')
    modeling_type = models.CharField(max_length=300,choices=Modeling_Method_CHOICES,default='Experimental')
    graphs = models.ManyToManyField(Graph)
    username = models.ManyToManyField(User,verbose_name='Curator(s)')
    date = models.DateTimeField(auto_now=True)
    score = models.FloatField(default=None, blank=True, null=True,verbose_name='Evaluated Score')
    parameters = models.FilePathField(blank=True, null=True)
    neuroML_file = models.FilePathField(blank=True, null=True)
    neuron_file = models.FilePathField(blank=True, null=True)
    references = models.ManyToManyField(Reference)

    def __unicode__(self):
        return repr(self.channel_name)
