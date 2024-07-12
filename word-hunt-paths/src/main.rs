#[derive(Debug, Copy, Clone, PartialEq)]
struct Tile {
    x: i32,
    y: i32
}

impl Tile {
    fn valid(&self) -> bool {
        0 <= self.x && self.x < 4 && 0 <= self.y && self.y < 4
    }

    fn get_neighbors(&self) -> Vec<Tile> {
        let mut neighbors: Vec<Tile> = vec![];

        for dx in -1..=1 {
            for dy in -1..=1 {
                if dx == 0 && dy == 0 {
                    continue;
                }

                let neighbor = Tile { x: self.x + dx, y: self.y + dy };

                if neighbor.valid() {
                    neighbors.push(neighbor);
                }
            }
        }

        neighbors
    }

    fn count_paths(self) -> u32 {
        let mut v = vec![self];
        self.count_paths_alt(&mut v)
    }

    fn count_paths_alt(&self, path: &mut Vec<Tile>) -> u32 {
        let mut sum = if path.len() >= 3 { 1 } else { 0 };

        for neighbor in self.get_neighbors() {
            // Technically O(n) but let's see if we can get away with this
            if !path.contains(&neighbor) {
                path.push(neighbor);
                sum += neighbor.count_paths_alt(path);
                path.remove(path.len() - 1);
            }
        }

        sum
    }
}

fn main() {
    let mut sum: u32 = 0;

    // We make an argument by symmetry
    for tile in &[Tile { x: 0, y: 0 }, Tile { x: 1, y: 0 }, Tile { x: 1, y: 0 }, Tile { x: 1, y: 1 }] {
        sum += tile.count_paths();
    }

    // This outputs 12029640 if we don't have the condition that words need to be at least 3
    // letters long (see OEIS A236690)
    //
    // With the aforementioned condition, the number becomes 12029540, which does seem to check
    // out.
    println!("{}", 4 * sum);
}
