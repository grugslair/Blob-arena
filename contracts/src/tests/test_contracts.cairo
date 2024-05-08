use starknet::{class_hash::Felt252TryIntoClassHash, syscalls::deploy_syscall, ContractAddress,};
#[cfg(test)]
use dojo::{
    test_utils::{deploy_contract, spawn_test_world,},
    world::{IWorldDispatcher, IWorldDispatcherTrait,},
};
use blob_arena::{
    components::{
        blobert::{Blobert, blobert,},
        challenge::{ChallengeInvite, challenge_invite, ChallengeResponse, challenge_response,},
        combat::{TwoHashes, two_hashes, TwoMoves, two_moves,},
        knockout::{Healths, healths, Knockout, knockout, LastRound, last_round,},
        stake::{Stake, stake,},
    },
    contracts::{
        blobert::{blobert_actions, IBlobertActionsDispatcher,},
        challenge::{challenge_actions, IChallengeActionsDispatcher,},
        knockout::{knockout_actions, IKnockoutActionsDispatcher,},
    },
};

#[cfg(test)]
#[derive(Copy, Drop)]
struct TestContracts {
    world: IWorldDispatcher,
    blobert_actions: IBlobertActionsDispatcher,
    challenge_actions: IChallengeActionsDispatcher,
    knockout_actions: IKnockoutActionsDispatcher,
}

#[cfg(test)]
fn make_test_world() -> TestContracts {
    let mut models = array![
        blobert::TEST_CLASS_HASH,
        challenge_invite::TEST_CLASS_HASH,
        challenge_response::TEST_CLASS_HASH,
        two_hashes::TEST_CLASS_HASH,
        two_moves::TEST_CLASS_HASH,
        healths::TEST_CLASS_HASH,
        knockout::TEST_CLASS_HASH,
        last_round::TEST_CLASS_HASH,
        stake::TEST_CLASS_HASH,
    ];

    let world = spawn_test_world(models);
    let blobert_actions_dispatcher = IBlobertActionsDispatcher {
        contract_address: world
            .deploy_contract(
                'blobert_actions', blobert_actions::TEST_CLASS_HASH.try_into().unwrap()
            )
    };
    let challenge_actions_dispatcher = IChallengeActionsDispatcher {
        contract_address: world
            .deploy_contract(
                'challenge_actions', challenge_actions::TEST_CLASS_HASH.try_into().unwrap()
            )
    };
    let knockout_actions_dispatcher = IKnockoutActionsDispatcher {
        contract_address: world
            .deploy_contract(
                'knockout_actions', knockout_actions::TEST_CLASS_HASH.try_into().unwrap()
            )
    };

    TestContracts {
        world,
        blobert_actions: blobert_actions_dispatcher,
        challenge_actions: challenge_actions_dispatcher,
        knockout_actions: knockout_actions_dispatcher,
    }
}
