package move.status;

import ru.ifmo.se.pokemon.*;

public final class Flash extends StatusMove {
    public Flash() {
        super(Type.NORMAL, 0, 100);
    }

    @Override
    protected void applyOppEffects(Pokemon p) {
        p.setMod(Stat.ACCURACY, -1);
    }

    @Override
    protected String describe() {
        return "использует Flash";
    }
}
