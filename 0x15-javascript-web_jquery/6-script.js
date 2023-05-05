const header = $('header');
const trigger = $('div#update_header');

trigger.on('click', () => {
	header.text('New Header!!!');
});
