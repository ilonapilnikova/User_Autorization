function animateLetters(element) {
    var text = element.text();
    element.empty();
  
    text.split('').forEach(function(char, index) {
      var letter = $('<span>' + char + '</span>').hide();
      element.append(letter);
  
      letter.delay(index * 100).fadeIn(1000, function() {
        
        $(this).css('color', '#eea54e');
      });
    });
  }
  
  $(document).ready(function() {
    var h1Element = $('h1'); 
    animateLetters(h1Element);
  });
  


  $(document).ready(function() {
    var element = $('.effect'); 
    var visible = true; // Изначально элемент видим
  
  
    var blinkInterval = setInterval(function() {
      if (visible) {
        element.hide(); // Если видим, скрываем элемент
      } else {
        element.show(); // Если скрыт, показываем элемент
      }
      visible = !visible; 
    }, 1000); // Интервал в миллисек
  
    // остановить мигание через 
    setTimeout(function() {
      clearInterval(blinkInterval);
      element.show(); 
    }, 30000); 
  });
  

      // Изменяем цвет фона <input> при наведении

  $(document).ready(function() {
    var inputs = $('input');
  
    inputs.on('mouseenter', function() {
      $(this).css('background-color', 'bisque'); 
    });
  
    inputs.on('mouseleave', function() {
      // Возвращаем исходный цвет фона 
      $(this).css('background-color', ''); // Сброс цвета
    });
  });
  


  function showTemporaryNotification(message, type) {
    var notification = $('<div class="notification ' + type + '">' + message + '</div>');
    notification.css({
        'border': '2px solid bisque', 
        'padding': '10px',
        'margin': '10px',
        'text-align': 'center'
    });
    notification.insertAfter($('.reg'));
    notification.insertAfter($('.log'));

    notification.fadeIn(500).delay(2000).fadeOut(500, function() {
        notification.remove();
    });
}

$(document).ready(function() {
    
    $('.log').click(function() {
        showTemporaryNotification('Проверяем Ваши данные...', 'success');
    });

    
    $('.reg').click(function() {
        showTemporaryNotification('Проверяем Ваши данные...', 'success');
    });
});



