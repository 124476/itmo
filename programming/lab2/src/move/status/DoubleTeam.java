package move.status;

import pokemon.Poliwag;
import ru.ifmo.se.pokemon.*;

public final class DoubleTeam extends StatusMove {
    public DoubleTeam() {
        super(Type.NORMAL, 0, 0);
    }

    @Override
    protected void applySelfEffects(Pokemon p) {
        if (p instanceof Poliwag) {
            Pokemon[] ally = ((Poliwag) p).getAlly();
            ally[0].setMod(Stat.EVASION, +1);
            ally[1].setMod(Stat.EVASION, +1);
            ally[2].setMod(Stat.EVASION, +1);
        }
    }

    @Override
    protected String describe() {
        return "использует Double Team";
    }
}
