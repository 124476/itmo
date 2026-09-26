package pokemon;

import move.physical.*;
import move.status.*;
import move.special.*;
import ru.ifmo.se.pokemon.*;

public class Spoink extends Pokemon {
    public Spoink(String name, int level) {
        super(name, level);
        setType(Type.PSYCHIC);
        setStats(60, 25, 35, 70, 80, 60);

        addMove(new ChargeBeam());
        addMove(new CalmMind());
        addMove(new ThunderWave());
    }
}
