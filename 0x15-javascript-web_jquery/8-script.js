const link = 'https://swapi.co/api/films/?format=json'
$.get(link, function (data, textStatus) {
      const list = data.results;
      for (const m in list) {
        $('#list_movies').append('<li>' + list[m].title + '</li>');
    }
  });
