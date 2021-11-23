document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.datepicker');
  var options = { format: 'yyyy-mm-dd' };
  var instances = M.Datepicker.init(elems, options);
});


function dropdown() {
  var x = document.getElementById("myLinks");
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}


$(document).ready(function(){
  $('select').formSelect();
});
