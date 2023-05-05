$(document).ready(() => {
  const addTrigger = $('div#add_item');
  const removeTrigger = $('div#remove_item');
  const clearTrigger = $('div#clear_list');
  const list = $('ul.my_list');

  addTrigger.on('click', () => {
    list.append('<li>Item</li>');
  });
  removeTrigger.on('click', () => {
    list.find('li').last().remove();
  });
  clearTrigger.on('click', () => {
    list.find('li').remove();
  });
});
