package move;

import pokemon.*;
import ru.ifmo.se.pokemon.*;

public class MagnetRise extends StatusMove {
    public MagnetRise() {
        super(Type.ELECTRIC, 0, 0);
    }

    @Override
    public void applySelfEffects(Pokemon p) {
        Effect e = new Effect().turns(5);
        // требуется наложить защиту от землянных атак, но таких атак нет, так что ничего не накладываем :/

        p.addEffect(e);
    }

    @Override
    public String describe() {
        return "использует Magnet Rise";
    }
}
