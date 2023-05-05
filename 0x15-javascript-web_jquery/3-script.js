const header = $('header');
const trigger = $('div#red_header');

trigger.on('click', () => {
	header.addClass('red');
});
