$(document).ready(function () {
    $("#sidebarCollapse").click(function (e) {
        e.preventDefault();
        $(".app-wrapper").toggleClass("toggled");
    });
});