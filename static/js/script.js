$(document).ready(function(){
    $('.sidenav').sidenav({draggable: true});
    $("#copyright").text(new Date().getFullYear());
    $('#demo-carousel-content').carousel({fullWidth: true});
  setInterval(function() {
    $('#demo-carousel-content').carousel('next');
  }, 2000);
   $(".dropdown-trigger").dropdown();
  });