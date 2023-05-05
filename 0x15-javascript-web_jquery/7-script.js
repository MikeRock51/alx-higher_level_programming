const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

$.ajax({
  url: url,
  success: (response) => {
    $('div#character').text(response.name);
  },
  error: (xhr, status, error) => {
    alert(error);
  }
});
