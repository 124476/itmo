public interface Battleable {
    War startWar(String name, Leader enemy);
    void endWar(Contract contract, Leader enemy) throws NotHaveWar;
}