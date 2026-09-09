# ИТМО | СППО | Программирование | Лабораторные работы

<details>
<summary style="font-size: 1.5em; font-weight: bold;">Лаба 1</summary>

<p></p>

- [x] [Отчет](lab1/docs/Отчет.pdf)
- [x] [Исходный код](lab1/src/Main.java)

Подключение к helios
```
ssh s000000@helios.cs.ifmo.ru -p 2222
```

Отправка кода в helios
```
scp -P 2222 Main.java s000000@helios.cs.ifmo.ru:~
```

Компиляция исходного кода
```
javac Main.java
```

Создание исполняемого файла .jar
```
jar -c -f main.jar -e Main Main.class
```

</details>
