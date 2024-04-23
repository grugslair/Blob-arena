use blob_arena::{components::{combat::Move, utils::{Status}}};
use starknet::{ContractAddress};

#[starknet::interface]
trait IKnockoutActions<TContractState> {
    fn commit(self: @TContractState, combat_id: u128, hash: felt252);
    fn reveal(self: @TContractState, combat_id: u128, move: Move, salt: felt252);
}

#[dojo::contract]
mod knockout_actions {
    use super::IKnockoutActions;
    use starknet::{ContractAddress};

    use blob_arena::{
        components::{combat::Move, utils::{AB, Status}},
        systems::{knockout::{KnockoutGame, KnockoutGameTrait}}
    };
    #[abi(embed_v0)]
    impl KnockoutActionsImpl of IKnockoutActions<ContractState> {
        fn commit(self: @ContractState, combat_id: u128, hash: felt252) {
            self.get_game(combat_id).commit_move(hash);
        }
        fn reveal(self: @ContractState, combat_id: u128, move: Move, salt: felt252) {
            self.get_game(combat_id).reveal_move(move, salt);
        }
    }

    #[generate_trait]
    impl KnockoutInternalImpl of KnockoutInternalTrait {
        #[inline(always)]
        fn get_game(self: @ContractState, combat_id: u128) -> KnockoutGame {
            self.world_dispatcher.read().get_knockout_game(combat_id)
        }
    }
}
