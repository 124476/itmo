package move.special;

import ru.ifmo.se.pokemon.*;

public final class Blizzard extends SpecialMove {
    public Blizzard() {
        super(Type.ICE, 110, 70);
    }

    @Override
    protected void applyOppEffects(Pokemon p) {
        Effect e = new Effect().chance(0.1).condition(Status.FREEZE);
        p.addEffect(e);
    }

    @Override
    protected String describe() {
        return "использует Blizzard";
    }
}
