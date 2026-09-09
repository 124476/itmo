package move;

import ru.ifmo.se.pokemon.*;
import pokemon.*;

public class BlastBurn extends SpecialMove {
    public BlastBurn() {
        super(Type.FIRE, 150, 90);
    }

    @Override public String describe() {
        return "использует Blast Burn";
    }
}
