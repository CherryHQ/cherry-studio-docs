
{% hint style="warning" %}
Ten dokument został przetłumaczony z chińskiego przez AI i nie został jeszcze zweryfikowany.
{% endhint %}

# Huawei Cloud

1. Utwórz konto i zaloguj się na [Huawei Cloud](https://auth.huaweicloud.com/authui/login)

2. Kliknij [ten link](https://console.huaweicloud.com/modelarts/?region=cn-southwest-2#/model-studio/homepage), aby przejść do konsoli MaaS

3. Autoryzacja

<details>

<summary>Kroki autoryzacji (pomiń, jeśli już autoryzowano)</summary>

1. Po wejściu na stronę z linku w punkcie (2), postępuj zgodnie z podpowiedziami, aby przejść do strony autoryzacji (kliknij IAM > Użytkownicy podrzędni > Dodaj delegowanie > Zwykły użytkownik)

![](<../../.gitbook/assets/image (49).png>)

2. Po kliknięciu "Utwórz" wróć do strony z punktu (2)
3. Zostanie wyświetlony komunikat o niedostatecznych uprawnieniach dostępu, kliknij "Kliknij tutaj" w komunikacie
4. Dodaj istniejące uprawnienia i potwierdź

![](<../../.gitbook/assets/image (50).png>)

Uwaga: Ta metoda jest przeznaczona dla początkujących - nie musisz czytać dodatkowych materiałów, wystarczy klikać zgodnie z podpowiedziami. Jeśli możesz samodzielnie przeprowadzić autoryzację, możesz to zrobić w dowolny sposób.

</details>

4. Kliknij "Zarządzanie uwierzytelnianiem" w pasku bocznym, utwórz klucz API i skopiuj go

<figure><img src="../../.gitbook/assets/微信截图_20250214034650.png" alt=""><figcaption></figcaption></figure>

Następnie w CherryStudio utwórz nowego dostawcę usług

<figure><img src="../../.gitbook/assets/image (1) (2).png" alt="" width="300"><figcaption></figcaption></figure>

Po utworzeniu wklej klucz

5. Kliknij "Wdrażanie modelu" w pasku bocznym i odbierz wszystkie dostępne zasoby

<figure><img src="../../.gitbook/assets/微信截图_20250214034751.png" alt=""><figcaption></figcaption></figure>

6. Kliknij "Wywołaj"

<figure><img src="../../.gitbook/assets/image (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

Skopiuj adres z miejsca ①, wklej go do pola adresu dostawcy w CherryStudio i dodaj na końcu pięć znaków "#" (pound/hash):

``` 
Adres + #####
```

Dlaczego dodać "#"? [Zobacz wyjaśnienie](https://docs.cherry-ai.com/cherrystudio/preview/settings/providers#api-di-zhi)

> Możesz pominąć wyjaśnienie i postępować zgodnie z instrukcją;
> Możesz też usunąć fragment v1/chat/completions - jeśli wiesz jak to zrobić, wybierz dowolną metodę. Jeśli nie jesteś pewien, trzymaj się instrukcji.

<figure><img src="../../.gitbook/assets/image (2) (3).png" alt=""><figcaption></figcaption></figure>

Następnie skopiuj nazwę modelu z miejsca ②, w CherryStudio kliknij przycisk "+ Dodaj", aby utworzyć nowy model

<figure><img src="../../.gitbook/assets/image (4) (3).png" alt=""><figcaption></figcaption></figure>

Wprowadź nazwę modelu dokładnie tak, jak w przykładzie - bez dodatków i bez cudzysłowów.

<figure><img src="../../.gitbook/assets/image (3) (3).png" alt=""><figcaption></figcaption></figure>

Kliknij "Dodaj model" aby zakończyć.

{% hint style="info" %}
W Huawei Cloud każdy model ma inny adres końcowy, więc dla każdego modelu musisz utworzyć oddzielnego dostawcę usług, powtarzając powyższe kroki.
{% endhint %}