package move;

import ru.ifmo.se.pokemon.*;

public class Flamethrower extends SpecialMove {
    public Flamethrower() {
        super(Type.FIRE, 90, 100);
    }

    @Override
    public void applyOppEffects(Pokemon p) {
        Effect e = new Effect().chance(0.1).condition(Status.BURN);
        p.addEffect(e);
    }

    @Override
    public String describe() {
        return "использует Flamethrower";
    }
}
