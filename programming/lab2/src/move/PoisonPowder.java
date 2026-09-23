package move;

import ru.ifmo.se.pokemon.*;

public class PoisonPowder extends StatusMove {
    public PoisonPowder() {
        super(Type.POISON, 0, 75);
    }

    @Override
    public void	applyOppEffects(Pokemon p) {
        Effect.poison(p);
    }

    @Override
    public String describe() {
        return "использует Poison Powder";
    }
}
