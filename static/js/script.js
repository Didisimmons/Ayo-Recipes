$(document).ready(function(){
    $('.sidenav').sidenav({draggable: true});
    $("#copyright").text(new Date().getFullYear());
    $('#demo-carousel-content').carousel({fullWidth: true});
  setInterval(function() {
    $('#demo-carousel-content').carousel('next');
  }, 2000);
   $(".dropdown-trigger").dropdown();
   $('.tooltipped').tooltip();
   $('select').formSelect();
  });




var add_button = document.getElementById('add-more-button');
var remove_button = document.getElementById('remove-button');
var ingredients = document.getElementById('ingredient-list');

/* Allow user to input or delete more ingredients on the create recipe page
 * code taken from Abdul Basit at  https://www.youtube.com/watch?v=MLBLsxcB3Dc
 */
 add_button.onclick = function(){
    var inputmore = document.createElement('input');
    inputmore.setAttribute('type', 'text');
    inputmore.setAttribute('id', 'ingredients');
    inputmore.setAttribute('name', 'ingredients');
    inputmore.setAttribute('class', 'input-ingredients');
    inputmore.setAttribute('minlength', '5');
    inputmore.setAttribute('required', 'true');
    inputmore.setAttribute('placeholder', 'insert ingredients');
    ingredients.appendChild(inputmore);
};

remove_button.onclick = function(){
    var fields = document.getElementsByClassName('input-ingredients');
    if(fields.length > 1) {
        ingredients.removeChild(fields[(fields.length) - 1]);
    }
};