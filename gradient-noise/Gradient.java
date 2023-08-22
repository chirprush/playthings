// I'm going into AP CS A this year, so I might as well program something in
// Java, right?
import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

public class Gradient {
    // The parameter `value` is guaranteed to be between -1 and 1.
    public static int toPixel(double value) {
        double clamp = Math.max(0, Math.min(value, 1));
        return (int) (255 * clamp);
    }

    // I could probably wrap the Gradient into a class and it would be a bit
    // easier to inspect weights and all that, but I can do that later.
    public static void main(String[] args) {
        // I'm actually quite surprised to learn that Java doesn't have
        // unsigned integer types, so I guess we're just going with this.
        final int length = 400;
        // final int seedSkips = 40;
        // final int seedsL = length / seedSkips + 1;
        final int seedsN = 100; // (int) Math.pow(seedsL, 2);

        double values[][] = new double[length][length];
        Seed[] seeds = new Seed[seedsN];

        var rng = new Random();

        for (int i = 0; i < seedsN; i++) {
            double weight = 2.0 * ((float)i / (seedsN - 1) - 0.5); //  2.0 * (rng.nextDouble() - 0.5);
            var pos = new Pair(rng.nextInt(length), rng.nextInt(length));
            seeds[i] = new Seed(weight, pos);
        }

        for (int y = 0; y < length; y++) {
            for (int x = 0; x < length; x++) {
                var pos = new Pair(x, y);
                double value = 0.0;
                for (var seed : seeds) {
                    value += seed.weight / Math.pow(Pair.distance(seed.pos, pos) / 20.0, 1.0);
                }
                values[y][x] = value;
            }
        }

        for (var seed : seeds) {
            System.out.println(String.format("Seed: (%d, %d)", seed.pos.x, seed.pos.y));
            System.out.println(String.format("Weight: %f", seed.weight));
            System.out.println("Neighbors: ");
            for (int y = -1; y < 2; y += 2) {
                for (int x = -1; x < 2; x += 2) {
                    if (seed.pos.y + y < length && seed.pos.y + y >= 0 && seed.pos.x + x < length && seed.pos.x + x >= 0) {
                        System.out.print(String.format("%f ", values[seed.pos.y + y][seed.pos.x + x]));
                    }
                }
            }
            System.out.println("\n");
        }

        try {
            var output = new FileWriter("./bin/output.pgm");

            // Header for the PGM file
            output.write(String.format("P2\n%d %d\n255\n", length, length));

            for (int y = 0; y < length; y++) {
                for (int x = 0; x < length; x++) {
                    output.write(String.format("%d ", toPixel(values[y][x])));
                }
                output.write("\n");
            }

            output.close();
        } catch (IOException e) {
            System.err.println("File IO error");
            e.printStackTrace();
        }
    }
}
