import java.util.ArrayList;
import java.util.List;

public abstract class Leader extends Person implements Battleable {
    private double patience;
    private List<War> activeWars = new ArrayList<War>();

    public Leader(String name, double patience) {
        super(name);
        this.patience = patience;
    }

    protected double getPatience() {
        return this.patience;
    }

    protected void decreasePatience(double amount) {
        this.patience = Math.max(0, this.patience - amount);
    }

    @Override
    public War startWar(String name, Leader enemy) {
        return new War(name, this, (Leader) enemy);
    }

    @Override
    public void endWar(Contract contract, Leader enemy) throws NotHaveWar {
        for (War war : activeWars) {
            if (war.equalsWar(this, enemy)) {
                war.makePeace(contract);
                this.removeWar(war);
                enemy.removeWar(war);
                return;
            }
        }

        throw new NotHaveWar(getName(), enemy.getName());
    }

    protected void addWar(War war) {
        activeWars.add(war);
    }

    protected void removeWar(War war) {
        activeWars.remove(war);
    }
}