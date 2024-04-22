use starknet::{ContractAddress};

struct Lobby {
    #[key]
    id: u128,
}

struct LobbyPlayer {
    #[key]
    lobby_id: u128,
    #[key]
    player_id: ContractAddress,
    blobert_id: u128,
    wins: u128,
}
