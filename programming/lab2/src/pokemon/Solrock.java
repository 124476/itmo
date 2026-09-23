package pokemon;

import move.*;
import ru.ifmo.se.pokemon.*;

public class Solrock extends Pokemon {
    public Solrock(String name, int level) {
        super(name, level);
        setType(Type.ROCK, Type.PSYCHIC);
        setStats(90, 95, 85, 55, 65, 70);

        this.addMove(new Tackle());
        this.addMove(new MagnetRise());
        this.addMove(new Overheat());
        this.addMove(new MachPunch());
    }
}
