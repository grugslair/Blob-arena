use starknet::{ContractAddress};

struct Lobby {
    #[key]
    id: ContractAddress,
    running: bool,
}

struct LobbyPlayer {
    #[key]
    lobby_id: ContractAddress,
    #[key]
    player_id: ContractAddress,
    blobert_id: u128,
    wins: u128,
    joined: bool,
}
