# Лаба 1

## Ссылки

- [x] [Отчет](docs/report.pdf)
- [x] [Исходный код](src/Main.java)

## Работа на helios

Подключение к helios
```bash
ssh s000000@helios.cs.ifmo.ru -p 2222
```

Отправка кода в helios
```bash
scp -P 2222 Main.java s000000@helios.cs.ifmo.ru:~
```

Компиляция исходного кода
```bash
javac Main.java
```

Создание исполняемого файла .jar
```bash
jar -c -f main.jar -e Main Main.class
```

Еще пример создания через флаги
```bash
jar -cfe main.jar Main Main.class
```

Запуск исполняемого файла .jar
```bash
java -jar main.jar
```
