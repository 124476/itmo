import pokemon.Victini;
import ru.ifmo.se.pokemon.*;

public class Main {
    public static void main(String[] args) {
        Battle b = new Battle();
        Pokemon p1 = new Victini("Чужой", 2);
        Pokemon p2 = new Pokemon("Хищник", 100);
        b.addAlly(p1);
        b.addFoe(p2);
        b.go();
    }
}