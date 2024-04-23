#[cfg(test)]
mod test {
    use blob_arena::{
        components::{stats::Stats, combat::{Move, MatchResult, Outcome, AB}},
        systems::combat::{get_outcome, calculate_damage}
    };
    #[test]
    #[available_gas(3000000000)]
    fn test_combat() {
        let stats_a = Stats { attack: 10, defense: 20, speed: 20, strength: 20, };
        let stats_b = Stats { attack: 0, defense: 0, speed: 0, strength: 0, };
        let mut n: u8 = 0;
        loop {
            let move_a: Move = n.into();
            let mut m: u8 = 0;
            loop {
                let move_b: Move = m.into();
                let outcome = get_outcome(move_a, move_b);
                let (damage_a, damage_b) = calculate_damage(stats_a, stats_b, outcome);

                println!(
                    "a: {} \t{}\tb: {} \t{}\tresult: {} ",
                    move_a,
                    damage_a,
                    move_b,
                    damage_b,
                    outcome
                );

                if m == 2 {
                    break;
                }
                m += 1;
            };
            if n == 2 {
                break;
            }
            n += 1;
        };
    }
}
