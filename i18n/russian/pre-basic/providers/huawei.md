
{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}

# Huawei Cloud

1. Создайте учётную запись и войдите на [Huawei Cloud](https://auth.huaweicloud.com/authui/login)
2. Перейдите в [консоль ModelArts](https://console.huaweicloud.com/modelarts/?region=cn-southwest-2#/model-studio/homepage), нажав на эту ссылку
3. Авторизация

<details>

<summary>Шаги авторизации (пропустите, если уже авторизованы)</summary>

1. После перехода по ссылке из шага 2, следуйте подсказкам на странице авторизации (нажмите IAM Sub-user → Create Delegation → Common User)

![](<../../.gitbook/assets/image (49).png>)

2. После создания вернитесь на страницу по ссылке из шага 2
3. При появлении сообщения о недостаточных правах доступа нажмите "Click Here" в уведомлении
4. Добавьте существующую авторизацию и подтвердите

![](<../../.gitbook/assets/image (50).png>)

&#x20;Примечание: Этот метод подходит для новичков — не нужно изучать много информации, просто следуйте подсказкам. Если вам удалось успешно авторизоваться с первого раза, действуйте по своему усмотрению.

</details>

4. В боковой панели перейдите в "Authentication Management", создайте и скопируйте API Key (секретный ключ)

<figure><img src="../../.gitbook/assets/微信截图_20250214034650.png" alt=""><figcaption></figcaption></figure>

Затем создайте нового поставщика в CherryStudio

<figure><img src="../../.gitbook/assets/image (1) (2).png" alt="" width="300"><figcaption></figcaption></figure>

После создания вставьте секретный ключ

5. В боковой панели перейдите в "Model Deployment" и активируйте все предложения

<figure><img src="../../.gitbook/assets/微信截图_20250214034751.png" alt=""><figcaption></figcaption></figure>

6. Нажмите "Call"

<figure><img src="../../.gitbook/assets/image (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

Скопируйте адрес из места ①, вставьте его в поле адреса поставщика в CherryStudio и добавьте в конце символ "#"

И добавьте в конце символ "#"

И добавьте в конце символ "#"

И добавьте в конце символ "#"

И добавьте в конце символ "#"

Зачем добавлять "#"? [Смотрите здесь](https://docs.cherry-ai.com/cherrystudio/preview/settings/providers#api-di-zhi)

> Конечно, можно не смотреть, просто следуйте инструкциям;
> 
> Также можно использовать метод удаления v1/chat/completions при заполнении — делайте как удобно, но если не уверены, строго следуйте инструкциям.

<figure><img src="../../.gitbook/assets/image (2) (3).png" alt=""><figcaption></figcaption></figure>

Затем скопируйте название модели из места ②, в CherryStudio нажмите "+Add" для создания новой модели

<figure><img src="../../.gitbook/assets/image (4) (3).png" alt=""><figcaption></figcaption></figure>

Введите название модели без изменений и без кавычек, как показано в примере.

<figure><img src="../../.gitbook/assets/image (3) (3).png" alt=""><figcaption></figcaption></figure>

Нажмите "Add Model", чтобы завершить добавление.

{% hint style="info" %}
В Huawei Cloud каждый модель имеет уникальный адрес, поэтому для каждой модели необходимо создать отдельного поставщика, повторив описанные шаги.
{% endhint %}