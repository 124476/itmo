package pokemon;

import move.special.*;
import ru.ifmo.se.pokemon.*;

public final class Grumpig extends Spoink {
    public Grumpig(String name, int level) {
        super(name, level);
        setStats(80, 45, 65, 90, 110, 80);

        addMove(new FocusBlast());
    }
}
