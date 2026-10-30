public interface Battleable {
    War startWar(String name, Person enemy) throws NotLeaderWar;
}