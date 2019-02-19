$(document).ready(function(){
  $("div#update_header").click(function(){
    $("<header>New Header!!!</header>").replaceAll("header");
  });
});
