const header = $('header');
const trigger = $('div#toggle_header');

trigger.on('click', () => {
  header.toggleClass('green red');
});
