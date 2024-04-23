use blob_arena::components::blobert::BlobertTrait;
use blob_arena::components::{
    blobert::Blobert, stats::Stats, combat::{Move, MatchResult, Outcome, AB},
};


fn calculate_win_damage(attacker: Stats, defender: Stats, winning_mode: Move) -> u8 {
    let (attacker_var, defender_var): (u8, u8) = match winning_mode {
        Move::Beat => (attacker.strength, defender.strength),
        Move::Counter => (attacker.speed, defender.strength),
        Move::Rush => (attacker.speed, defender.speed),
    };

    (attacker.attack + 10) * 2 / (defender.defense + defender_var) * (attacker_var + 10)
}

fn calculate_draw_damage(attacker: Stats, defender: Stats, mode: Move) -> u8 {
    match mode {
        Move::Beat => (attacker.attack + 10)
            * 2
            / (defender.defense + 10)
            * (attacker.strength + 10),
        Move::Counter => 0,
        Move::Rush => (attacker.attack + 10) * 2 / (defender.defense + 10) * (attacker.speed + 10),
    }
}


fn calculate_damage(player_a: Stats, player_b: Stats, outcome: Outcome) -> (u8, u8) {
    match outcome.result {
        MatchResult::Draw => (
            calculate_draw_damage(player_a, player_b, outcome.move),
            calculate_draw_damage(player_b, player_a, outcome.move)
        ),
        MatchResult::Winner(winner) => {
            let (attacker, defender): (Stats, Stats) = match winner {
                AB::A => (player_a, player_b),
                AB::B => (player_b, player_a),
            };
            let damage = calculate_win_damage(attacker, defender, outcome.move);

            match winner {
                AB::A => (0, damage),
                AB::B => (damage, 0),
            }
        }
    }
}


fn get_outcome(move_a: Move, move_b: Move) -> Outcome {
    let result_u8: u8 = (3_u8 + move_a.into() - move_b.into()) % 3;
    if result_u8 == 0 {
        return Outcome { result: MatchResult::Draw, move: move_a };
    };

    let winner: AB = match (result_u8 % 2).is_non_zero() {
        false => AB::A,
        true => AB::B,
    };
    let move = match winner {
        AB::A => move_a,
        AB::B => move_b,
    };

    return Outcome { result: MatchResult::Winner(winner), move };
}

