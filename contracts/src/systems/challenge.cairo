use starknet::{ContractAddress, get_caller_address};
use dojo::world::{IWorldDispatcherTrait};
use blob_arena::{
    components::{
        blobert::BlobertTrait,
        challenge::{ChallengeInvite, ChallengeResponse, Challenge, make_challenge, ChallengeTrait},
        world::{World}
    },
    systems::{blobert::BlobertWorldTrait, knockout::{KnockoutGameTrait}}
};

#[generate_trait]
impl ChallengeImpl of ChallengeSystemTrait {
    fn get_challenge_invite(self: World, challenge_id: u128) -> ChallengeInvite {
        get!(self, challenge_id, ChallengeInvite)
    }

    fn get_challenge_response(self: World, challenge_id: u128) -> ChallengeResponse {
        get!(self, challenge_id, ChallengeResponse)
    }

    fn get_challenge(self: World, challenge_id: u128) -> Challenge {
        make_challenge(
            self.get_challenge_invite(challenge_id), self.get_challenge_response(challenge_id)
        )
    }

    fn get_open_challenge(self: World, challenge_id: u128) -> Challenge {
        let challenge = self.get_challenge(challenge_id);
        assert(challenge.invite_open, 'Challenge already closed');
        assert(challenge.combat_id.is_zero(), 'Combat already started');
        challenge
    }

    fn send_challenge_invite(self: World, receiver: ContractAddress, blobert_id: u128) -> u128 {
        let challenge_id: u128 = self.uuid().into();
        let sender = get_caller_address();
        self.assert_blobert_owner(blobert_id, sender);
        let challenge = ChallengeInvite { challenge_id, sender, receiver, blobert_id, open: true, };
        set!(self, (challenge,));
        challenge_id
    }

    fn close_challenge_invite(self: World, challenge_id: u128) {
        let caller = get_caller_address();
        let mut challenge = self.get_open_challenge(challenge_id);
        assert(challenge.sender == caller, 'Not the sender');
        challenge.invite_open = false;
        let challenge_invite = challenge.invite();
        set!(self, (challenge_invite,));
    }

    fn respond_challenge_invite(self: World, challenge_id: u128, blobert_id: u128) {
        let caller = get_caller_address();
        let mut challenge = self.get_open_challenge(challenge_id);
        assert(challenge.receiver == caller, 'Not the receiver');
        self.assert_blobert_owner(blobert_id, caller);
        challenge.receiver_blobert = blobert_id;
        challenge.response_open = true;
        set!(self, (challenge.response(),));
    }

    fn close_challenge_response(self: World, challenge_id: u128) {
        let caller = get_caller_address();
        let mut challenge = self.get_open_challenge(challenge_id);
        assert(challenge.receiver == caller, 'Not the receiver');
        assert(challenge.response_open, 'Response already closed');
        challenge.response_open = false;
        set!(self, (challenge.response(),));
    }

    fn reject_challenge_invite(self: World, challenge_id: u128) {
        let caller = get_caller_address();
        let mut challenge = self.get_open_challenge(challenge_id);
        assert(challenge.receiver == caller, 'Not the receiver');
        challenge.invite_open = false;
        set!(self, (challenge.invite(),));
    }

    fn reject_challenge_response(self: World, challenge_id: u128) {
        let caller = get_caller_address();
        let mut challenge = self.get_open_challenge(challenge_id);
        assert(challenge.sender == caller, 'Not the sender');
        assert(challenge.response_open, 'Response already closed');
        challenge.response_open = false;
        set!(self, (challenge.response(),));
    }

    fn accept_challenge_response(self: World, challenge_id: u128) -> u128 {
        let caller = get_caller_address();
        let mut challenge = self.get_open_challenge(challenge_id);
        assert(challenge.sender == caller, 'Not the sender');
        assert(challenge.response_open, 'Response already closed');
        challenge
            .combat_id = self
            .new_knockout(
                challenge.sender,
                challenge.receiver,
                challenge.sender_blobert,
                challenge.receiver_blobert
            );
        set!(self, (challenge.response(),));
        challenge.combat_id
    }
}
