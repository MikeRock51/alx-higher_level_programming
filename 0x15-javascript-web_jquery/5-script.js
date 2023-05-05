const trigger = $('div#add_item');

trigger.on('click', () => {
  $('ul.my_list').append('<li>Item</li>');
});
