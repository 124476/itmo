# Лаба 3

```bash
scp -P 2222 -r src s558473@helios.cs.ifmo.ru:~/
```

```bash
javac -encoding UTF-8 *.java */*.java
````

```bash
java -cp .:model:interface:exception:enum Main
```

```bash
cat > manifest <<EE
Class-Path: ./ enum/ exception/ model/ interface/
Main-Class: Main
EE
```

```bash
jar -cfm main.jar manifest Main.class enum model exception interface
```

```bash
rm *.class 
rm model/*.class 
rm interface/*.class 
rm enum/*.class 
rm exception/*.class 
```