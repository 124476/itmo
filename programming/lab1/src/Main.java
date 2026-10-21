import static java.lang.Math.*;

public class Main {
    public static float getNumber(short e, float x) {
        switch (e) {
            case 12: {
                return (float) sin(sin(pow(E, x)));
            }
            case 2, 4, 8, 16, 18, 24: {
                return (float) asin(PI / 4.0 * pow((x - 0.5) / 15.0, 2));
            }
            default: {
                double a1 = 0.5 * pow(pow(x, 1.0 / 3.0) + 3, 2);
                double a2 = 1.0 / 2.0 + asin((x - 0.5) / 15.0);
                double a3 = pow(x / (1.0 / 4.0), x);

                return (float) cos(pow(4 / a1, pow(a2, a3)));
            }
        }
    }

    public static void printMatrix(float[][] k) {
        for (var floats : k) {
            for (var val : floats) {
                System.out.printf("%.4f\t", val);
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        final int N = 12, M = 15;

        final short[] e = new short[N];
        for (int i = 0; i < N; i++) {
            e[i] = (short) (24 - 2 * i);
        }
        final float[] x = new float[M];
        for (int i = 0; i < M; i++) {
            x[i] = (float)random() * 15 - 8;
        }

        final float[][] k = new float[N][M];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                k[i][j] = getNumber(e[i], x[j]);
            }
        }

        printMatrix(k);
    }
}