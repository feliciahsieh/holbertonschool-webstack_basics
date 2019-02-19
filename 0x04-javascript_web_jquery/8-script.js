const $ = window.$;
$(document).ready(function () {
  let url = 'https://swapi.co/api/films?format=json';
  $.get(url, function (data, status) {
    for (let i = 0; i < data['count']; i++) {
      $('UL#list_movies').append('<div>' + data['results'][i]['title'] + '</div>');
    }
  });
});
