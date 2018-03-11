from django.db import models
from django.contrib.auth.models import User
from ion_channel.models import IonChannel


Channel_Type_CHOICES = (
    ('Calcium Channel', 'Calcium Channel'),
    ('Potassium Channel', 'Potassium Channel'),
    ('Transient Receptor Potential Channel', 'Transient Receptor Potential Channel'),
    ('Cyclic Nucleotide-Gated Channel', 'Cyclic Nucleotide-Gated Channel'),
    ('Ligand-Gated Ion Channel', 'Ligand-Gated Ion Channel'),
    ('Ionotropic Glutamate Receptors', 'Ionotropic Glutamate Receptors'),
    ('DEG/ENaC Channels', 'DEG/ENaC Channels'),
    ('Chloride Channel', 'Chloride Channel')
)
# Channel_Subype_CHOICES = (
#     ('CaV', 'Voltage-gated'),
#     ('KV1', 'Voltage-gated, Shaker/Kv1'),
#     ('KV2', 'Voltage-gated, Shab/Kv2'),
#     ('KV3', 'Voltage-gated, Shaw/Kv3'),
#     ('KV4', 'Voltage-gated, Shal/Kv4'),
#     ('KQT', 'KQT'),
#     ('KV10-12', 'Voltage-gated, Eag-like/Kv10-12'),
#     ('KCa-Slo', 'Calcium-activated Slo'),
#     ('KCa-SK', 'Calcium-activated SK'),
#     ('TWK', 'TWK'),
#     ('Kir', 'Inward-Rectifier'),
#     ('Cation, TRP', 'Transient Receptor Potential Cation Channel'),
#     ('CNG', 'Cyclic Nucleotide-Gated Channel'),
#     ('LGIC', 'Ligand-Gated Ion Channel'),
#     ('iGluRs', 'Ionotropic Glutamate Receptors'),
#     ('DEG/ENaC/ASIC', 'DEGenerin/Epithelial Na+ Channels/Acid Sensing Ion Channels'),
#     ('CLC', 'Chloride Channels And Transporters'),
#     ('Auxiliary', 'Auxiliary subunit')
# )
Ion_Type_CHOICES = (
    ('Ca2+', 'Calcium'),
    ('K+', 'Potassium'),
    ('Cl-', 'Chloride'),
    ('Na+', 'Cation'),
    ('Cation', 'Cation')
)
Ligand_Type_CHOICES = (
    ('ATP', 'ATP'),
    ('Glutamate', 'Glutamate'),
    ('Acetylcholine', 'Acetylcholine'),
    ('Serotonin', 'Serotonin'),
    ('Tyramine', 'Tyramine')
)


class IonChannelGene(models.Model):
    channel_name = models.CharField(null=True, max_length=300)
    description = models.TextField(blank=True, null=True)
    description_evidences = models.TextField(blank=True, null=True,verbose_name='PMID for description evidence')
    channel_type = models.CharField(blank=True, null=True, max_length=300,choices=Channel_Type_CHOICES)
    channel_subtype = models.CharField(blank=True, null=True, max_length=300)
    ion_type = models.CharField(blank=True, null=True, max_length=200,choices=Ion_Type_CHOICES)
    ligand_type = models.CharField(blank=True, null=True, max_length=200,choices=Ligand_Type_CHOICES)
    gene_name = models.CharField(blank=True, null=True, max_length=300)
    gene_WB_ID = models.CharField(blank=True, null=True, max_length=300)
    gene_class = models.CharField(blank=True, null=True, max_length=300)
    proteins = models.CharField(blank=True, null=True, max_length=300)
    expression_pattern = models.TextField(blank=True, null=True)
    expression_evidences = models.TextField(blank=True, null=True,verbose_name='PMID for expression evidence')
    last_update = models.DateTimeField(auto_now=True, null=True)
    ion_channel = models.ForeignKey(IonChannel, on_delete=models.CASCADE, blank=True, null=True)
    username = models.ForeignKey(User, verbose_name='Contributor', on_delete=models.CASCADE, default='1')

    def __unicode__(self):
        return self.channel_name


class Protein(models.Model):
    name = models.CharField(max_length=300, unique=True)
    ion_channel = models.ForeignKey(IonChannelGene, on_delete=models.CASCADE)
    sequence = models.TextField(blank=True, null=True)
    fasta = models.TextField(blank=True, null=True)
    gi = models.CharField(max_length=300,blank=True, null=True,verbose_name='GI number')
    uniprot_ID = models.CharField(blank=True, null=True, max_length=300)
    wb_ID = models.CharField(blank=True, null=True, max_length=300)
    pdb_ID = models.CharField(blank=True, null=True, max_length=300)
    interpro_ID = models.CharField(blank=True, null=True, max_length=300)
    structure = models.TextField(blank=True, null=True)
    structure_image = models.ImageField(blank=True, null=True, upload_to='ion_channel/structures/')

    def __unicode__(self):
        return self.name
