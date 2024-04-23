use starknet::ContractAddress;
#[starknet::interface]
trait IChallengeActions<TContractState> {
    fn send_invite(self: @TContractState, receiver: ContractAddress, blobert_id: u128) -> u128;
    fn close_invite(self: @TContractState, challenge_id: u128);
    fn respond_invite(self: @TContractState, challenge_id: u128, blobert_id: u128);
    fn close_response(self: @TContractState, challenge_id: u128);
    fn reject_invite(self: @TContractState, challenge_id: u128);
    fn reject_response(self: @TContractState, challenge_id: u128);
    fn accept_response(self: @TContractState, challenge_id: u128) -> u128;
}
#[dojo::contract]
mod challenge_actions {
    use super::IChallengeActions;
    use starknet::ContractAddress;
    use blob_arena::{components::world::World, systems::challenge::ChallengeSystemTrait};
    #[abi(embed_v0)]
    impl ChallengeActionsImpl of IChallengeActions<ContractState> {
        fn send_invite(self: @ContractState, receiver: ContractAddress, blobert_id: u128) -> u128 {
            self.get_world().send_challenge_invite(receiver, blobert_id)
        }
        fn close_invite(self: @ContractState, challenge_id: u128) {
            self.get_world().close_challenge_invite(challenge_id);
        }
        fn respond_invite(self: @ContractState, challenge_id: u128, blobert_id: u128) {
            self.get_world().respond_challenge_invite(challenge_id, blobert_id);
        }
        fn close_response(self: @ContractState, challenge_id: u128) {
            self.get_world().close_challenge_response(challenge_id);
        }
        fn reject_invite(self: @ContractState, challenge_id: u128) {
            self.get_world().reject_challenge_invite(challenge_id);
        }
        fn reject_response(self: @ContractState, challenge_id: u128) {
            self.get_world().reject_challenge_response(challenge_id);
        }
        fn accept_response(self: @ContractState, challenge_id: u128) -> u128 {
            self.get_world().accept_challenge_response(challenge_id)
        }
    }
    #[generate_trait]
    impl WorldImpl of WorldTrait {
        fn get_world(self: @ContractState) -> World {
            self.world_dispatcher.read()
        }
    }
}
