function updateProgressBar() {
    const progressBar = document.querySelector('.progress-bar');
    const progressText = document.querySelector('.progress-text');

    // Получите текущее значение атрибута 'aria-valuenow'
    const currentValue = parseInt(progressBar.getAttribute('aria-valuenow'));

    // Увеличьте значение прогресса на 1
    const newValue = (currentValue + 1) % 101;

    // Установите новое значение в атрибут 'aria-valuenow'
    progressBar.setAttribute('aria-valuenow', newValue);

    // Обновите текст прогресса
    progressText.innerText = newValue + '%';

    // Установите новую ширину для прогресс-бара
    progressBar.style.width = newValue + '%';

    // Запустите эту функцию повторно через определенный интервал времени (например, каждую секунду)
    setTimeout(updateProgressBar, 200); // Интервал в миллисекундах
  }

  // Вызовите функцию для начала автоматической анимации прогресс-бара
  updateProgressBar();