# Teledocker

Этот репозиторий содержит исходный код телеграм-бота. Чтобы запустить бота, выполните следующие шаги (можете все скопировать и вставить в консоль):

```bash
# Шаг 1: Склонируйте репозиторий
git clone https://github.com/romnatall/teledocker.git

# Шаг 2: Перейдите в папку с проектом
cd teledocker

# Шаг 3: установите свой токен, (инструкция https://helpdesk.bitrix24.ru/open/17538378/)
echo "YOUR_TOKEN"> token.txt

# Шаг 4: Соберите Docker-образ (необходим docker)
docker build -t doctelbot .

# Шаг 5: Запустите бота
docker run doctelbot
```

после выполненных шагов бот запустится, логи сохраняются в mflog.log

