public abstract class Leader extends Person implements Battleable {
    private double patience;

    public Leader(String name, double patience) {
        super(name);
        this.patience = patience;
    }

    protected double getPatience() { return this.patience; }

    protected void decreasePatience(double amount) {
        this.patience = Math.max(0, this.patience - amount);
    }

    public void accuse(Leader enemy, String reason) throws BrokenOathException {
        System.out.println(this.getName() + " обвиняет " + enemy.getName() + " в том, что он " + reason);
        if (enemy.getPatience() < 50) {
            throw new BrokenOathException(enemy.getName());
        }
    }

    @Override
    public War startWar(String name, Person enemy) throws NotLeaderWar {
        if (!(enemy instanceof Leader)) {
            throw new NotLeaderWar(enemy.getName());
        }
        return new War(name, this, (Leader) enemy);
    }
}