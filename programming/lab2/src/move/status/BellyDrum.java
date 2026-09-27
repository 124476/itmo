package move.status;

import ru.ifmo.se.pokemon.*;

public final class BellyDrum extends StatusMove {
    public BellyDrum() {
        super(Type.NORMAL, 0, 0);
    }

    @Override
    protected void applySelfEffects(Pokemon p) {
        int damage = (int)(p.getStat(Stat.HP) / 2);
        p.setMod(Stat.HP, damage); // умрет, если меньше половины хп (походу так должно быть)
        p.setMod(Stat.ATTACK, +6);
    }

    @Override
    protected String describe() {
        return "использует Belly Drum";
    }
}
