public interface IBattle {
    War startWar(String name, IBattle enemy);
    Contract endWar(War war, String nameConract) throws WarEnded;
    void addWar(War war);
    void removeWar(War war);
    void takeDamage(double damage);
    double getPatience();
}