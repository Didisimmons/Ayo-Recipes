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


var ingredients = document.getElementById('ingredient-list');
var add_button = document.getElementById('add-more-button');
var remove_button = document.getElementById('remove-button');

/* Allow user to input or delete more ingredients on the create recipe page
 * code taken from Abdul Basit at  https://www.youtube.com/watch?v=MLBLsxcB3Dc
 */
 add_button.onclick = function(){
    var inputmore = document.createElement('input');
    inputmore.setAttribute('type', 'text');
    inputmore.setAttribute('id', 'ingredients');
    inputmore.setAttribute('name', 'ingredients');
    inputmore.setAttribute('class', ' validate input-ingredients');
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

var add_more_directions = document.getElementById('add-more-directions');
var remove_directions = document.getElementById('delete-directions');
var recipe_directions = document.getElementById('instruction-list');

/* Allow user to input or delete recipe instructions on the create recipe page
 * code taken from Abdul Basit at  https://www.youtube.com/watch?v=MLBLsxcB3Dc
 */
add_more_directions.onclick = function(){
  var nextInstruction = document.createElement('textarea');
  nextInstruction.setAttribute('type', 'text');
  nextInstruction.setAttribute('id', 'recipe_instructions');
  nextInstruction.setAttribute('name', 'recipe_instructions');
  nextInstruction.setAttribute('class', 'materialize-textarea validate instructions');
  nextInstruction.setAttribute('minlength', '5');
  nextInstruction.setAttribute('maxlength', '500s');
  nextInstruction.setAttribute('required', 'true');
  nextInstruction.setAttribute('placeholder', 'provide directions for the recipe');
  recipe_directions.appendChild(nextInstruction);
};

remove_directions.onclick = function(){
  var instruction_fields = document.getElementsByClassName('instructions');
  if(instruction_fields.length > 1) {
    recipe_directions.removeChild(instruction_fields[(instruction_fields.length) - 1]);
  }
};