package pokemon;

import move.*;
import ru.ifmo.se.pokemon.*;

public class Bayleef extends Pokemon {
    public Bayleef(String name, int level) {
        super(name, level);
        setType(Type.GRASS);
        setStats(60, 62, 80, 63, 80, 60);

        this.addMove(new PoisonPowder());
        this.addMove(new FakeOut());
        this.addMove(new Flamethrower());
    }
}
