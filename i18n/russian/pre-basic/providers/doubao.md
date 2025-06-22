
{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}

# ByteDance (Doubao)

*   Войдите в [VolcEngine](https://console.volcengine.com/)
*   Или сразу перейдите по [этой ссылке](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D)

<figure><img src="../../.gitbook/assets/image (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

### Получение API-ключа

*   В боковом меню выберите раздел [Управление API-ключами](https://console.volcengine.com/ark/region:ark+cn-beijing/apiKey)
*   Создайте новый API-ключ

<figure><img src="../../.gitbook/assets/image (6) (2).png" alt=""><figcaption></figcaption></figure>

*   После создания кликните на значок глаза 🔍 рядом с ключом для просмотра и скопируйте его

<figure><img src="../../.gitbook/assets/image (7) (2).png" alt=""><figcaption></figcaption></figure>

*   Вставьте скопированный API-ключ в CherryStudio и активируйте переключатель провайдера

<figure><img src="../../.gitbook/assets/image (8) (2).png" alt=""><figcaption></figcaption></figure>

### Активация и добавление моделей

*   В разделе [Управление активациями](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D\&OpenTokenDrawer=false) боковой панели активируйте нужные модели (серия Doubao, DeepSeek и др.)

<figure><img src="../../.gitbook/assets/image (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

*   В [документе со списком моделей](https://www.volcengine.com/docs/82379/1330310#%E6%96%87%E6%9C%AC%E7%94%9F%E6%88%90) найдите ID нужной модели

<figure><img src="../../.gitbook/assets/火山引擎_模型ID.png" alt="Пример списка ID моделей VolcEngine"><figcaption></figcaption></figure>

*   В настройках CherryStudio откройте раздел [Модели провайдеров](../../cherrystudio/preview/settings/providers.md) → VolcEngine
*   Нажмите "Добавить" и вставьте ID модели в соответствующее поле

<figure><img src="../../.gitbook/assets/volc_ark_01.png" alt=""><figcaption></figcaption></figure>

*   Повторите процедуру для добавления всех необходимых моделей

### Адрес API

Доступно два варианта записи адреса API:
1.  Стандартный в клиенте: `https://ark.cn-beijing.volces.com/api/v3/`
2.  Альтернативный: `https://ark.cn-beijing.volces.com/api/v3/chat/completions#`

{% hint style="info" %}
Оба варианта функционально идентичны. Рекомендуется использовать значение по умолчанию.  
Разница между окончаниями `/` и `#` объясняется в разделе [Настройки провайдеров](../../cherrystudio/preview/settings/providers.md#api-di-zhi)
{% endhint %}

<figure><img src="../../.gitbook/assets/image (3) (2).png" alt=""><figcaption><p>Пример cURL из официальной документации</p></figcaption></figure>