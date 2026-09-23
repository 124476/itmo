import pokemon.*;
import ru.ifmo.se.pokemon.*;

public class Main {
    public static void main(String[] args) {
        Battle b = new Battle();
        Pokemon p1 = new Solrock("Покеном 1", 2);
        Pokemon p2 = new Solrock("Покеном 2", 2);
        Pokemon p3 = new Bayleef("Покеном 3", 1);
        Pokemon e1 = new Solrock("Босс", 1000);
        b.addAlly(p1);
        b.addAlly(p2);
        b.addAlly(p3);
        b.addFoe(e1);
        b.go();
    }
}