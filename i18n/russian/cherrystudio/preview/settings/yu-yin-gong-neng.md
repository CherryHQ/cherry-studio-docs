---
hidden: true
icon: phone-arrow-up-right
---

# Голосовые функции

{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}

```markdown
# Голосовые функции

```

Руководство по использованию голосовых функций Cherry Studio

1. Обзор голосовых функций

Cherry Studio предоставляет три основных модуля голосовых функций: TTS (преобразование текста в речь), ASR (распознавание речи) и голосовые звонки. Эти функции позволяют вести естественное голосовое общение с ИИ, улучшая пользовательский опыт.

* **TTS (Text-to-Speech)**: преобразование текстовых ответов ИИ в речь
* **ASR (Speech Recognition)**: преобразование вашей речи в текст
* **Голосовые звонки**: комбинация TTS и ASR для получения голосового диалогового опыта, аналогичного ChatGPT

2. Функция TTS (Text-to-Speech)
3. Поддерживаемые типы сервисов

Cherry Studio поддерживает четыре типа TTS-сервисов:

* **OpenAI**: использование TTS API от OpenAI, требует API-ключа
* **Браузерный TTS**: использование встроенной функции синтеза речи браузера, бесплатно без настройки
* **Siliconflow**: использование TTS-сервиса Siliconflow, требует API-ключа
* **Бесплатный онлайн TTS**: использование бесплатных онлайн-сервисов, не требует API-ключа

2. Настройка
3. Перейдите в раздел настроек, выберите вкладку "Голосовые функции"
4. Во вкладке "TTS":
   * Включите функцию TTS (активируйте переключатель)
   * Выберите тип TTS-сервиса
   * Настройте параметры в соответствии с выбранным сервисом:
     * OpenAI: укажите API-ключ, адрес API, выберите голос и модель
     * Браузерный TTS: выберите голос
     * Siliconflow: укажите API-ключ, адрес API, выберите голос, модель, формат ответа и скорость речи
     * Бесплатный онлайн TTS: выберите голос и формат вывода
5. Настройте фильтрацию TTS (опционально):
   * Фильтровать процесс мышления
   * Фильтровать разметку Markdown
   * Фильтровать блоки кода
6. Установите, показывать ли индикатор прогресса TTS
7. Нажмите кнопку "Проверить TTS" для тестирования настроек
8. Использование

* При включённой функции TTS ответы ИИ автоматически преобразуются в речь
* Под каждым ответом ИИ в интерфейсе чата отображается кнопка воспроизведения TTS
* Нажмите кнопку воспроизведения для включения/паузы голоса
* При активации индикатора прогресса под текстом отображается прогресс воспроизведения
* Длинные тексты автоматически разбиваются на сегменты и воспроизводятся последовательно

3. Функция ASR (распознавание речи)
4. Поддерживаемые типы сервисов

Cherry Studio поддерживает три типа ASR-сервисов:

* **OpenAI**: использование модели Whisper от OpenAI, требует API-ключа
* **Браузер**: использование встроенной функции распознавания речи браузера, бесплатно без настройки
* **Локальный сервер**: подключение к локальному WebSocket-серверу для распознавания речи

2. Настройка
3. Перейдите в раздел настроек, выберите вкладку "Голосовые функции"
4. Во вкладке "ASR":
   * Включите функцию ASR (активируйте переключатель)
   * Выберите тип ASR-сервиса
   * Настройте параметры в соответствии с выбранным сервисом:
     * OpenAI: укажите API-ключ, адрес API, выберите модель
     * Браузер: дополнительная настройка не требуется
     * Локальный сервер: можно установить автоматический запуск ASR-сервера при запуске приложения
   * Выберите язык распознавания речи (по умолчанию: китайский)
5. Нажмите кнопку "Проверить ASR" для тестирования настроек
6. Использование

* При включённой функции ASR рядом с полем ввода появляется кнопка распознавания речи
* Нажмите кнопку для начала записи
* После речи она преобразуется в текст и вставляется в поле ввода
* Повторное нажатие кнопки останавливает запись
* Поддерживается непрерывное распознавание нескольких фраз с накоплением результатов

4. Функция голосовых звонков
5. Особенности

* Комбинация TTS и ASR для реализации диалогового опыта, аналогичного ChatGPT
* Использует перемещаемое всплывающее окно
* Поддерживает режим удержания для разговора
* Поддерживает настройку горячих клавиш
* Поддерживает свёртывание окна
* Можно выбрать специализированную модель для голосовых звонков
* Поддерживаются пользовательские промпты

2. Настройка
3. Перейдите в раздел настроек, выберите вкладку "Голосовые функции"
4. Во вкладке "Функция звонков":
   * Включите функцию голосовых звонков (активируйте переключатель)
   * Нажмите кнопку "Выбрать модель", чтобы выбрать ИИ-модель для звонков
   * В текстовом поле промпта введите пользовательский промпт (опционально)
   * Нажмите "Сохранить" для сохранения промпта или "Сброс" для восстановления промпта по умолчанию
5. Использование
6. В интерфейсе чата нажмите кнопку голосового звонка (иконка телефона) справа от поля ввода
7. Откроется окно голосового звонка с приветственным сообщением
8. Удерживайте кнопку "Удерживайте для разговора" для начала записи (или используйте назначенную горячую клавишу)
9. Отпустите кнопку для завершения записи и отправки ИИ
10. ИИ сгенерирует ответ и воспроизведёт его через TTS
11. Используйте элементы управления в окне:
    * Кнопка отключения звука: управление выходом TTS
    * Кнопка паузы: приостановка/возобновление разговора
    * Кнопка настроек: конфигурация горячих клавиш
    * Кнопка сворачивания: свёртывание окна до строки удержания
12. Нажмите кнопку закрытия для завершения звонка
13. Настройка горячих клавиш
14. В окне голосового звонка нажмите кнопку настроек
15. В панели настроек нажмите кнопку горячих клавиш
16. Нажмите клавишу, которую хотите назначить (например, пробел, Shift и т.д.)
17. Нажмите "Сохранить" для применения настроек
18. Используйте: удерживайте назначенную клавишу для начала записи, отпустите для завершения записи и отправки
19. Частые проблемы и решения
20. Проблемы с TTS

* Проблема: TTS не воспроизводит звук\
  Решение: проверьте включение TTS, правильность типа сервиса и обязательных параметров
* Проблема: низкое качество воспроизведения TTS\
  Решение: попробуйте другой тип TTS-сервиса или голос
* Проблема: при воспроизведении TTS отображается сообщение об ошибке\
  Решение: проверьте правильность API-ключа и подключение к сети

2. Проблемы с ASR

* Проблема: ASR не распознаёт речь\
  Решение: проверьте включение ASR, правильность типа сервиса и обязательных параметров
* Проблема: низкая точность распознавания ASR\
  Решение: попробуйте другой тип ASR-сервиса, отрегулируйте положение и громкость микрофона
* Проблема: ошибка подключения к ASR-серверу\
  Решение: проверьте работу локального сервера или перезапустите приложение

3. Проблемы с голосовыми звонками

* Проблема: окно голосового звонка не открывается\
  Решение: проверьте включение функции звонков, правильность настройки TTS и ASR
* Проблема: функция удержания не реагирует\
  Решение: проверьте разрешение микрофона или перезапустите звонок
* Проблема: ответы ИИ не озвучиваются\
  Решение: проверьте включение TTS и отсутствие отключения звука

6. Расширенные настройки и параметры
7. Расширенные настройки TTS

* Фильтрация: можно фильтровать процесс мышления, разметку Markdown и блоки кода для плавного воспроизведения
* Индикатор прогресса: выбор отображения индикатора прогресса TTS
* Пользовательские голоса и модели: добавление пользовательских параметров голосов и моделей

2. Расширенные настройки ASR

* Автозапуск сервера: настройка автоматического запуска ASR-сервера при старте приложения
* Выбор языка: выбор языка для распознавания речи

3. Расширенные настройки голосовых звонков

* Пользовательские промпты: настройка промптов для управления стилем ответов ИИ
* Выбор специализированной модели: выбор отдельной ИИ-модели для звонков
* Настройка горячих клавиш: назначение пользовательских горячих клавиш для управления записью

7. Рекомендации по использованию
8. Выбор TTS-сервиса:
   * Для высокого качества используйте OpenAI или Siliconflow
   * Для работы без настройки используйте браузерный или бесплатный онлайн TTS
9. Выбор ASR-сервиса:
   * Для высокой точности используйте OpenAI
   * Для работы без настройки используйте встроенный распознаватель браузера
10. Оптимизация голосовых звонков:
    * Использование наушников предотвращает повторный захват голоса TTS
    * Тихое окружение улучшает точность распознавания
    * Пользовательские промпты адаптируют ответы ИИ для голосового воспроизведения
11. Настройка под задачи:
    * Используйте только TTS при основном текстовом общении
    * Используйте только ASR при основном голосовом вводе
    * Включите функцию голосовых звонков для полного диалогового опыта

Надеемся, что это руководство поможет вам максимально эффективно использовать голосовые функции Cherry Studio для удобного и естественного взаимодействия с ИИ!

```
```
