$(document).ready(function () {

    $('.editfolder_modal_btn').on('click', function () {
        id = $(this).data("id");
        name = $(this).attr("data-name");
        $("input[name=new_title]").val(name)
        $('#folder_id').val(id);
    });

    $('.changeprojectfolder_modal_btn').on('click', function () {
        $('#changeprojectfolder_modal #project_id').val($(this).data("id"));
    });

    $('.deleteproject_modal_btn').on('click', function () {
        $('#project_id').val( $(this).data("id"));
        if($(this).attr("data-name")=='manager'){
            $('#deleteproject_modal .modal-title').text("Projekt löschen");
            $('#deleteproject_modal .modal-desc').html("Möchtest du das Projekt wirklich löschen? <br/><br/>Bei einem Team-Projekt wird das Projekt auch für alle anderen Mitglieder gelöscht.");
        } else if($(this).attr("data-name")=='member'){
            $('#deleteproject_modal .modal-title').text("Projekt verlassen");
            $('#deleteproject_modal .modal-desc').text("Möchtest du das Projekt wirklich verlassen?");
        }
    });

    $('.deletemember_modal_btn').on('click', function () {
        $('#deletemember_modal #member_id').val($(this).data("id"));
    });

    $('#id_team').change(function() {
       $('#team-text').toggle();
   });
});