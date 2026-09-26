package pokemon;

import move.physical.*;
import move.status.*;
import ru.ifmo.se.pokemon.*;

public final class Volbeat extends Pokemon {
    public Volbeat(String name, int level) {
        super(name, level);
        setType(Type.BUG);
        setStats(65, 73, 75, 47, 85, 85);

        addMove(new QuickAttack());
        addMove(new Flash());
        addMove(new AerialAce());
        addMove(new DizzyPunch());
    }
}
