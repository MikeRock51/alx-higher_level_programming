const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$.ajax({
	url: url,
	success: (response) => {
		for (title of response.results) {
			$('ul#list_movies').append(`<li>${title.title}</li>`);
		}
	},
	error: (xhr, status, error) => {
		console.log(error);
	}
});
