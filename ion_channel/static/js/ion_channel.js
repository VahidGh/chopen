chopen.ion_channel = (function () {
    var ionChannelId = -1;

    var url = {
        ionChannelCreateURL: '',
        ionChannelUpdateURL: '',
        ionChannelDetailURL: '',
        referenceIndex: '',
        referenceCreate: '',
        referenceCreateAuto: '',
        referenceUpdate: '',
        patchClampIndex: '',
        patchClampCreate: '',
        patchClampUpdate: '',
        graphIndex: '',
        graphCreate: '',
        graphUpdate: '',
        IonChannelModelIndex: '',
        IonChannelModelCreate: '',
        IonChannelModelUpdate: '',
        IonChannelGeneIndex: '',
        IonChannelGeneCreate: '',
        IonChannelGeneUpdate: '',
    };

    function init(config) {
        url.ionChannelCreateURL = config.url.ionChannelCreateURL;
        url.ionChannelUpdateURL = config.url.ionChannelUpdateURL;
        url.ionChannelDetailURL = config.url.ionChannelDetailURL;

        url.ionChannelGeneIndex = config.url.ionChannelGeneIndex;
        url.ionChannelGeneCreate = config.url.ionChannelGeneCreate;
        url.ionChannelGeneUpdate = config.url.ionChannelGeneUpdate;

        url.referenceIndex = config.url.referenceIndex;
        url.referenceCreate = config.url.referenceCreate;
        url.referenceCreateAuto = config.url.referenceCreateAuto;
        url.referenceUpdate = config.url.referenceUpdate;

        url.patchClampIndex = config.url.patchClampIndex;
        url.patchClampCreate = config.url.patchClampCreate;
        url.patchClampUpdate = config.url.patchClampUpdate;

        url.graphIndex = config.url.graphIndex;
        url.graphCreate = config.url.graphCreate;
        url.graphUpdate = config.url.graphUpdate;

        url.IonChannelModelIndex = config.url.IonChannelModelIndex;
        url.IonChannelModelCreate = config.url.IonChannelModelCreate;
        url.IonChannelModelUpdate = config.url.IonChannelModelUpdate;

        $("#ion_channel_form").load(url.ionChannelCreateURL);
        $("#ion_channel_detail").load(url.ionChannelDetailURL);
    }

    function loadReference() {
        $("#reference_loading").css("display", "block");
        $("#reference").load(url.referenceIndex + ionChannelId, function () {
            $("#reference_loading").css("display", "none")
        });
    }

    function loadPatchClamp() {
        $("#patch_clamp_loading").css("display", "block");
        $("#patch_clamp").load(url.patchClampIndex + ionChannelId, function () {
            $("#patch_clamp_loading").css("display", "none")
        });
    }

    function loadGraph() {
        $("#graph_loading").css("display", "block");
        $("#graph").load(url.graphIndex + ionChannelId, function () {
            $("#graph_loading").css("display", "none")
        });
    }

    function loadIonChannelModel() {
        $("#ionChannelModel_loading").css("display", "block");
        $("#ionChannelModel").load(url.IonChannelModelIndex + ionChannelId, function () {
            $("#ionChannelModel_loading").css("display", "none")
        });
    }

    function saveIonChannel() {
        var ionChannelUpdateURL = url.ionChannelUpdateURL;

        chopen.ajax.submit({
            form: 'frm_ion_channel',
            loadingMask: 'loading',
            success: function (response) {
                if (response.status == 'success') {
                    ionChannelId = response.pk;
                    var lastSlashIndex = ionChannelUpdateURL.lastIndexOf("/");
                    var updateURL = ionChannelUpdateURL.substring(0, lastSlashIndex) + "/" + ionChannelId;
                    $("#ion_channel_form_wrapper").load(updateURL);
                    $('#loading').css("display", "none");

                    $("#reference").load(url.referenceCreate);
                    $("#patch_clamp").load(url.patchClampCreate);
                    loadGraph();
                }
            }
        });

        return false;
    }

    function saveIonChannelGene() {
        var ionChannelGeneUpdate = url.ionChannelGeneUpdate;

        chopen.ajax.submit({
            form: 'frm_ion_channel_gene',
            loadingMask: 'loading',
            success: function (response) {
                if (response.status == 'success') {
                    ionChannelId = response.pk;
                    var lastSlashIndex = ionChannelUpdateURL.lastIndexOf("/");
                    var updateURL = ionChannelUpdateURL.substring(0, lastSlashIndex) + "/" + ionChannelId;
                    $("#ion_channel_gene_form_wrapper").load(updateURL);
                    $('#loading').css("display", "none");

                    $("#reference").load(url.referenceCreate);
                    $("#patch_clamp").load(url.patchClampCreate);
                    loadGraph();
                }
            }
        });

        return false;
    }

    function deleteIonChannel(){
        return saveIonChannel();
    }

    function saveReference() {
        chopen.ajax.submit({
            form: 'frm_reference',
            loadingMask: 'form_loading',
            containFile: true,
            success: function (response) {
                if (response.status == 'success') {
                    $('#loading').css("display", "none");
                    $("#reference").load(url.referenceCreate);
                }
            }
        });

        return false;
    }

    function deleteReference(){
        return saveReference();
    }

    function savePatchClamp() {
        chopen.ajax.submit({
            form: 'frm_patch_clamp',
            loadingMask: 'form_loading',
            success: function (response) {
                if (response.status == 'success') {
                    $('#loading').css("display", "none");
                    $("#patch_clamp").load(url.patchClampCreate);
                }
            }
        });

        return false;
    }

    function deletePatchClamp(){
        return savePatchClamp();
    }

    function saveGraph() {
        chopen.ajax.submit({
            form: 'frm_graph',
            loadingMask: 'form_loading',
            containFile: true,
            success: function (response) {
                if (response.status == 'success') {
                    $('#form_loading').css("display", "block");
                    loadGraph();
                    closeModal();
                }
            }
        });

        return false;
    }

    function deleteGraph(){
        return saveGraph();
    }

    function saveIonChannelModel() {
        chopen.ajax.submit({
            form: 'frm_ionChannelModel',
            loadingMask: 'form_loading',
            containFile: true,
            success: function (response) {
                if (response.status == 'success') {
                    $('#form_loading').css("display", "block");
                    loadIonChannelModel();
                    closeModal();
                }
            }
        });

        return false;
    }

    function deleteIonChannelModel(){
        return saveIonChannelModel();
    }

    function openModal(title){
        $('.modal-title').html(title)
        $('.modal').modal('show');
    }

    function openPatchClampCreateForm() {
        openModal('<i class="fa fa-pinterest-p"></i> Patch Clamp')
        $("#form-container").load(url.patchClampCreate + ionChannelId);
    }

    function openPatchClampUpdateForm(url) {
        openModal('<i class="fa fa-pinterest-p"></i> Patch Clamp')
        $("#form-container").load(url);
    }

    function confirmDeletePatchClamp(url){
        openModal('<i class="fa fa-warning"></i> Confirm')
        $("#form-container").load(url);
    }

    function openReferenceCreateForm() {
        openModal('<i class="fa fa-file-text-o"></i> Reference')
        $("#form-container").load(url.referenceCreate + ionChannelId);
    }

    function openReferenceCreateAutoForm() {
        openModal('<i class="fa fa-file-text-o"></i> Reference')
        $("#form-container").load(url.referenceCreateAuto + ionChannelId);
    }

    function openReferenceUpdateForm(url) {
        openModal('<i class="fa fa-file-text-o"></i> Reference')
        $("#form-container").load(url);
    }

    function confirmDeleteReference(url){
        openModal('<i class="fa fa-warning"></i> Confirm')
        $("#form-container").load(url);
    }

    function openGraphCreateForm() {
        openModal('<i class="fa fa-bar-chart"></i> Graph')
        $("#form-container").load(url.graphCreate + ionChannelId);
    }

    function closeModal(){
        $('.modal').modal('hide');
    }

    function openGraphUpdateForm(url) {
        $('.modal-title').html('<i class="fa fa-bar-chart"></i> Graph')
        $('.modal').modal('show');
        $("#form-container").load(url);
    }

    function confirmDeleteGraph(url){
        openModal('<i class="fa fa-warning"></i> Confirm')
        $("#form-container").load(url);
    }

    function openIonChannelModelCreateForm() {
        openModal('<i class="fa fa-area-chart"></i> IonChannelModel')
        $("#form-container").load(url.IonChannelModelCreate + ionChannelId);
    }

    function openIonChannelModelUpdateForm(url) {
        openModal('<i class="fa fa-area-chart"></i> IonChannelModel')
        $("#form-container").load(url);
    }

    function confirmDeleteIonChannelModel(url){
        openModal('<i class="fa fa-warning"></i> Confirm')
        $("#form-container").load(url);
    }

    return {
        init: init,
        saveIonChannel: saveIonChannel,
        reference: {
            openCreateForm: openReferenceCreateForm,
            openCreateAutoForm: openReferenceCreateAutoForm,
            openUpdateForm: openReferenceUpdateForm,
            confirmDelete: confirmDeleteReference,
            refresh: loadReference,
            save: saveReference,
            delete: deleteReference
        },
        patchClamp: {
            openCreateForm: openPatchClampCreateForm,
            openUpdateForm: openPatchClampUpdateForm,
            confirmDelete: confirmDeletePatchClamp,
            refresh: loadPatchClamp,
            save: savePatchClamp,
            delete: deletePatchClamp
        },
        graph: {
            openCreateForm: openGraphCreateForm,
            openUpdateForm: openGraphUpdateForm,
            confirmDelete: confirmDeleteGraph,
            refresh: loadGraph,
            save: saveGraph,
            delete: deleteGraph
        },
        ionChannelModel: {
            openCreateForm: openIonChannelModelCreateForm,
            openUpdateForm: openIonChannelModelUpdateForm,
            confirmDelete: confirmDeleteIonChannelModel,
            refresh: loadIonChannelModel,
            save: saveIonChannelModel,
            delete: deleteIonChannelModel
        },
        modal: {
            close: closeModal
        }
    }
})();