import java.util.ArrayList;
import java.util.List;

public abstract class Leader extends Person implements IBattle {
    private double patience;
    private List<War> activeWars = new ArrayList<War>();

    public Leader(String name, double patience) {
        super(name);
        this.patience = patience;
    }

    public double getPatience() {
        return this.patience;
    }

    public void takeDamage(double damage) {
        this.patience = Math.max(0, this.patience - damage);
    }

    @Override
    public War startWar(String name, IBattle enemy) {
        return new War(name, this, enemy);
    }

    @Override
    public Contract endWar(War war, String nameConract) throws WarEnded {
        Contract contract = new Contract(nameConract, war);
        war.endWar();
        return contract;
    }

    public void addWar(War war) {
        activeWars.add(war);
    }

    public void removeWar(War war) {
        activeWars.remove(war);
    }
}