$(document).ready(function () {

    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });

    $('#dropdownCollapse').on('click', function () {
        $('#dropdownCollapse').prev('a').attr('aria-expanded',$(this).attr('aria-expanded')==='true'?'false':'true' );
    });

    // Custom File Input
    $(".custom-file-input").on("change", function() {
      var fileName = $(this).val().split("\\").pop();
      $(this).siblings(".custom-file-label").addClass("selected").html(fileName);
    });

});