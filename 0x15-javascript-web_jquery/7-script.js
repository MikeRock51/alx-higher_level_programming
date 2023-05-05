const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

$.get(url, (response) => {
	$('div#character').text(response.name);
});
