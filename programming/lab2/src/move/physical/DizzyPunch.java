package move.physical;

import ru.ifmo.se.pokemon.*;

public final class DizzyPunch extends PhysicalMove {
    public DizzyPunch() {
        super(Type.NORMAL, 70, 100);
    }

    @Override
    protected void applyOppEffects(Pokemon p) {
        if (Math.random() < 0.2) {
            Effect.confuse(p);
        }
    }

    @Override
    protected String describe() {
        return "использует Dizzy Punch";
    }
}
