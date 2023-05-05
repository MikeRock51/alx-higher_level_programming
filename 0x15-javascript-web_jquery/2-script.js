const header = $('header');
const color = '#FF0000';
const trigger = $('div#red_header');

trigger.on('click', () => {
	header.css('color', color);
});
