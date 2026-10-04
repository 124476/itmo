# Лаба 2

Информацию о характеристиках брать с [сайта](https://pokemondb.net/search)

Компиляция проекта

## Windows
```bash
javac -encoding UTF-8 -cp "./Pokemon.jar;." Main.java
```

Запуск
```bash
java -cp "./Pokemon.jar;." Main
```

## Linux
```bash
javac -encoding UTF-8 -cp "./Pokemon.jar:" Main.java
```

Запуск
```bash
java -cp "./Pokemon.jar:" Main
```

Удаление 
```bash
rm *.class */*.class */*/*.class
```

Создание манифеста
```bash
cat > manifest <<EEE
Class-Path: Pokemon.jar
Main-Class: Main
EEE
```

Упаковка в .jar
```bash 
jar -cfm main.jar manifest Main.class pokemon move
```