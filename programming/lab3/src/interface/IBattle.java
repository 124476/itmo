public interface IBattle {
    War startWar(String name, Leader enemy);
    Contract endWar(War war, String nameConract) throws WarEnded;
    void takeDamage(double damage);
    double getPatience();
}