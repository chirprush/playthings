use std::collections::HashSet;
use gcd::Gcd;

use crate::EdgeType::NoEdge;
use crate::EdgeType::Coprime;
use crate::EdgeType::NonCoprime;

#[derive(PartialEq, Copy, Clone, Debug)]
enum EdgeType {
    NoEdge,
    Coprime,
    NonCoprime
}

impl EdgeType {
    pub fn matches_edge(&self, a: u32, b: u32) -> bool {
        match self {
            NoEdge => true,
            Coprime => a.gcd(b) == 1,
            NonCoprime => a.gcd(b) != 1
        }
    }
}

const NUMS: [u32; 12] = [20, 21, 22, 23, 24, 25, 27, 28, 30, 32, 33, 35];
const ADJ: [[EdgeType; 12]; 12] = [
    [NoEdge, NonCoprime, NoEdge, Coprime, Coprime, NoEdge, NoEdge, NoEdge, NoEdge, NoEdge, NoEdge, NoEdge],
    [NonCoprime, NoEdge, Coprime, NoEdge, NonCoprime, Coprime, NoEdge, NoEdge, NoEdge, NoEdge, NoEdge, NoEdge],
    [NoEdge, Coprime, NoEdge, NoEdge, NoEdge, Coprime, NonCoprime, NoEdge, NoEdge, NoEdge, NoEdge, NoEdge],
    [Coprime, NoEdge, NoEdge, NoEdge, Coprime, NoEdge, NoEdge, Coprime, NoEdge, NoEdge, NoEdge, NoEdge],
    [Coprime, NonCoprime, NoEdge, Coprime, NoEdge, Coprime, NoEdge, Coprime, NonCoprime, NoEdge, NoEdge, NoEdge],
    [NoEdge, Coprime, Coprime, NoEdge, Coprime, NoEdge, Coprime, NoEdge, NonCoprime, NonCoprime, NoEdge, NoEdge],
    [NoEdge, NoEdge, NonCoprime, NoEdge, NoEdge, Coprime, NoEdge, NoEdge, NoEdge, Coprime, NoEdge, NoEdge],
    [NoEdge, NoEdge, NoEdge, Coprime, Coprime, NoEdge, NoEdge, NoEdge, Coprime, NoEdge, NonCoprime, NoEdge],
    [NoEdge, NoEdge, NoEdge, NoEdge, NonCoprime, NonCoprime, NoEdge, Coprime, NoEdge, Coprime, NonCoprime, Coprime],
    [NoEdge, NoEdge, NoEdge, NoEdge, NoEdge, NonCoprime, Coprime, NoEdge, Coprime, NoEdge, NoEdge, Coprime],
    [NoEdge, NoEdge, NoEdge, NoEdge, NoEdge, NoEdge, NoEdge, NonCoprime, NonCoprime, NoEdge, NoEdge, NonCoprime],
    [NoEdge, NoEdge, NoEdge, NoEdge, NoEdge, NoEdge, NoEdge, NoEdge, Coprime, Coprime, NonCoprime, NoEdge],
];

enum SearchResult {
    Success(GraphState),
    Failure(GraphState)
}

#[derive(Copy, Clone, Debug)]
struct Neighbor {
    index: usize,
    connection: EdgeType
}

struct GraphState {
    arrangement: [u32; 12],
    available: HashSet<u32>,
}

impl GraphState {
    pub fn empty_index(&self) -> Option<usize> {
        for i in 0..12 {
            if self.arrangement[i] == 0 {
                return Some(i);
            }
        }
        None
    }

    pub fn get_possible(&self, index: usize) -> Vec<u32> {
        let mut possible: Vec<u32> = Vec::new();
        let neighbors: Vec<Neighbor> = self.get_neighbors(index);

        for num in self.available.iter() {
            let mut matches_all = true;

            for neighbor in &neighbors {
                let a = *num;
                let b = self.arrangement[neighbor.index];

                if b == 0 { continue; }

                if !neighbor.connection.matches_edge(a, b) {
                    matches_all = false;
                }
            }

            if matches_all {
                possible.push(*num);
            }
        }

        possible
    }

    pub fn get_neighbors(&self, index: usize) -> Vec<Neighbor> {
        let mut neighbors: Vec<Neighbor> = Vec::new();

        for i in 0..12 {
            match ADJ[index][i] {
                NoEdge => {},
                edge_type => { neighbors.push(Neighbor { index: i, connection: edge_type }) }
            }
        }

        neighbors
    }
}

fn search(mut state: GraphState) -> SearchResult {
    let index = match state.empty_index() {
        Some(i) => i,
        None => {
            return SearchResult::Success(state);
        }
    };

    for num in state.get_possible(index) {
        state.arrangement[index] = num;
        state.available.remove(&num);

        match search(state) {
            SearchResult::Success(new_state) => {
                return SearchResult::Success(new_state);   
            },
            SearchResult::Failure(failed_state) => {
                state = failed_state;
                state.available.insert(num);
            }
        };
    }

    state.arrangement[index] = 0;
    SearchResult::Failure(state)
}

fn main() {
    let start: GraphState = GraphState {
        arrangement: [
            0, 0, 0,
            23, 0, 0, 0,
            0, 0, 0,
            30, 0
        ],
        available: HashSet::from([20, 21, 22, 24, 25, 27, 28, 32, 33, 35])
    };

    // println!("{:?}", start.get_possible(8));
    let success: GraphState;

    match search(start) {
        SearchResult::Success(completed) => {
            success = completed;
            println!("{:?}", success.arrangement);
        },
        SearchResult::Failure(_) => {
            println!("Did not work");
            return;
        }
    }

    for i in 0..12 {
        for j in 0..i {
            let connection = ADJ[i][j];
            let a = success.arrangement[i];
            let b = success.arrangement[j];

            // \draw[line width=1.00mm] (l28) -- (l22);
            // \draw[line width=0.50mm, white] (l28) -- (l22);

            if connection == EdgeType::Coprime {
                println!("\\draw[line width=0.30mm] (l{}) -- (l{});", a, b);
            } else if connection == EdgeType::NonCoprime {
                println!("\\draw[line width=1.00mm] (l{}) -- (l{});", a, b);
                println!("\\draw[line width=0.50mm, white] (l{}) -- (l{});", a, b);
            }
        }
    }
}
