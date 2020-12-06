$(document).ready(function () {
    $("#sidebarCollapse").click(function (e) {
        e.preventDefault();
        $(".sidebar").toggleClass("toggled");
    });
});
