const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

$.ajax({
	url: url,
	dataType: 'json',
	crossDomain: true,
	xhrFields: {
		withCredentials: true
	},
	success: (response) => {
		$('div#hello').text(response.hello);
	},
	error: (xhr, status, error) => {
		console.log("OOPS!!!")
	}
});
