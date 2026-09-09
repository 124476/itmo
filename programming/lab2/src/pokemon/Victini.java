package pokemon;

import ru.ifmo.se.pokemon.*;
import move.*;

public class Victini extends Pokemon {
    public Victini(String name, int level) {
        super(name, level);
        setType(Type.PSYCHIC, Type.FIRE);
        setStats(100, 100, 100, 100, 100, 100);

        this.addMove(new SecretPower());
        this.addMove(new BlastBurn());
    }
}
