import java.util.Random;

public class Main {
    public static float getNumber(short e, float x) {
        switch (e) {
            case 12: {
                return (float) Math.sin(Math.sin(Math.pow(Math.E, x)));
            }
            case 2, 4, 8, 16, 18, 24: {
                return (float) Math.asin(Math.PI / 4.0 * Math.pow((x - 0.5) / 15.0, 2));
            }
            default: {
                double a1 = 0.5 * Math.pow(Math.pow(x, 1.0 / 3.0) + 3, 2);
                double a2 = 1.0 / 2.0 + Math.asin((x - 0.5) / 15.0);
                double a3 = Math.pow(x / (1.0 / 4.0), x);

                return (float) Math.cos(Math.pow(4 / a1, Math.pow(a2, a3)));
            }
        }
    }

    public static void printMatrix(float[][] k) {
        for (var floats : k) {
            for (var val : floats) {
                System.out.printf("%.4f ", val);
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        int n = (24 - 2) / 2 + 1;
        int m = 15;

        short[] e = new short[n];
        for (int i = 0; i < n; i++) {
            e[i] = (short) (24 - 2 * i);
        }

        Random random = new Random();
        float[] x = new float[m];
        for (int i = 0; i < m; i++) {
            x[i] = random.nextFloat(15) - 8;
        }

        float[][] k = new float[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                k[i][j] = getNumber(e[i], x[j]);
            }
        }

        printMatrix(k);
    }
}