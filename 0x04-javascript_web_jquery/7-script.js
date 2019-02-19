const $ = window.$;
$(document).ready(function () {
  let url = 'https://swapi.co/api/people/5/?format=json';
  $.get(url, function (data, status) {
    $('<div>' + data['name'] + '</div>').replaceAll('div#character');
  });
});
