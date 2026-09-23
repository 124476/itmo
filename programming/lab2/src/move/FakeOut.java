package move;

import ru.ifmo.se.pokemon.*;

public class FakeOut extends PhysicalMove {
    public FakeOut() {
        super(Type.NORMAL, 40, 100, 3, 1);
    }

    @Override
    public void	applyOppEffects(Pokemon p) {
        Effect.poison(p);
    }

    @Override
    public String describe() {
        return "использует Fake Out";
    }
}
