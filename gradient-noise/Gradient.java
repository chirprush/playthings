// I'm going into AP CS A this year, so I might as well program something in
// Java, right?
import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;
// Hmmmmmmmmmm this is what the internet says to do, but I would like to be
// explicit in my imports
import java.util.*;
import java.util.stream.*;

public class Gradient {
    // The parameter `value` is guaranteed to be between -1 and 1.
    public static int toPixel(double value) {
        double clamp = Math.max(0, Math.min(value, 1));
        return (int) (255 * clamp);
    }

    public static void main(String[] args) {
        // I'm actually quite surprised to learn that Java doesn't have
        // unsigned integer types, so I guess we're just going with this.
        final int length = 800;
        // final int seedSkips = 40;
        // final int seedsL = length / seedSkips + 1;
        final int seedsN = 400; // (int) Math.pow(seedsL, 2);

        double values[][] = new double[length][length];
        Seed[] seeds = new Seed[seedsN];

        var rng = new Random();

        for (int i = 0; i < seedsN; i++) {
            double weight = 2.0 * (rng.nextDouble() - 0.5);
            var pos = new Pair(rng.nextInt(length), rng.nextInt(length));
            seeds[i] = new Seed(weight, pos);
        }

        /* 
        for (int y = 0; y < seedsL; y++) {
            for (int x = 0; x < seedsL; x++) {
                int i = seedsL * y + x;
                double weight = 2.0 * (rng.nextDouble() - 0.5);
                var pos = new Pair(seedSkips * x, seedSkips * y);
                seeds[i] = new Seed(weight, pos);
            }
        }
        */

        /*
        for (int y = 0; y < length; y++) {
            for (int x = 0; x < length; x++) {
                if (x % seedSkips == 0 && y % seedSkips == 0) {
                    continue;
                } else if (x % seedSkips == 0) {
                } else if (y % seedSkips == 0) {
                } else {
                    // This doesn't quite give the effect I was going for, but
                    // it still looks rather interesting, so I'll keep it here
                    // for fun.
                    // var topLeft = new Pair(seedSkips * (x / seedSkips), seedSkips * (y / seedSkips));
                    // var topRight = new Pair(seedSkips * (x / seedSkips + 1), seedSkips * (y / seedSkips));
                    // var bottomLeft = new Pair(seedSkips * (x / seedSkips), seedSkips * (y / seedSkips + 1));
                    // var bottomRight = new Pair(seedSkips * (x / seedSkips + 1), seedSkips * (y / seedSkips + 1));
                    // var pos = new Pair(x, y);

                    // Pair[] points = {topLeft, topRight, bottomLeft, bottomRight};
                    // var totalDist = Arrays.stream(points).mapToDouble(point -> Pair.distance(point, pos)).sum();

                    // double value = 0;

                    // for (var point : points) {
                    //     value += values[point.y][point.x] * (Pair.distance(point, pos) / totalDist);
                    // }

                    values[y][x] = value;
                }
            }
        }
        */

        for (int y = 0; y < length; y++) {
            for (int x = 0; x < length; x++) {
                var pos = new Pair(x, y);
                double value = 0.0;
                for (var seed : seeds) {
                    value += Math.pow(2.0 * seed.weight, 3) / Math.pow(Pair.distance(seed.pos, pos), 0.6);
                }
                values[y][x] = value;
            }
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
