$(document).ready(() => {
  const url = 'https://www.fourtonfish.com/hellosalut/hello/?lang=';

  function sayHello () {
    const language = $('input#language_code').val();
    $.get(url + language, (response) => {
      $('div#hello').text(response.hello);
    });
  }
  $('input#btn_translate').on('click', sayHello());
  $('input#language_code').focus(function () {
    $(this).keydown((event) => {
      if (event.which === 13) {
        sayHello();
      }
    });
  });
});
