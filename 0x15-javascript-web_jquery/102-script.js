$(document).ready(() => {
  const url = 'https://www.fourtonfish.com/hellosalut/hello/';

  $('input#btn_translate').on('click', () => {
    const language = $('input#language_code').val();
    $.get(url + language, (response) => {
      $('div#hello').text(response.hello);
    });
  });
});
