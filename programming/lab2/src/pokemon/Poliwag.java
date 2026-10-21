package pokemon;

import move.special.*;
import move.status.*;
import ru.ifmo.se.pokemon.*;

public class Poliwag extends Pokemon {
    private Pokemon[] ally;

    public Poliwag(String name, int level) {
        super(name, level);
        setType(Type.WATER);
        setStats(40, 50, 40, 40, 40, 90);

        addMove(new DoubleTeam());
        addMove(new Blizzard());
    }

    public void setAlly(Pokemon[] ally) {
        this.ally = ally;
    }

    public Pokemon[] getAlly() {
        return this.ally;
    }
}
