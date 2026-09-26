import pokemon.*;
import ru.ifmo.se.pokemon.*;

public class Main {
    public static void main(String[] args) {
        Battle b = new Battle();

        Pokemon p1 = new Volbeat("Пчелка", 67);
        Pokemon p2 = new Spoink("Попрыгунчик", 68);
        Pokemon p3 = new Grumpig("Крот", 69);

        Pokemon e1 = new Poliwag("Рыбка", 67);
        Pokemon e2 = new Poliwhirl("Друган", 68);
        Pokemon e3 = new Poliwrath("Гигант", 69);

        b.addAlly(p1);
        b.addAlly(p2);
        b.addAlly(p3);

        b.addFoe(e1);
        b.addFoe(e2);
        b.addFoe(e3);

        b.go();
    }
}