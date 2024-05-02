using UnityEngine;

namespace Dojo
{
    public enum EnvironmentType
    {
        LOCAL,
        TORII,
        TESTNET,
        MAINNET
    }

    [CreateAssetMenu(fileName = "WorldManagerData", menuName = "ScriptableObjects/WorldManagerData", order = 2)]
    public class WorldManagerData : ScriptableObject
    {
        [Header("Environment")]
        public EnvironmentType environmentType;

        [Space(30)]
        [Header("Enpoint URLs")]
        public string toriiUrl = "http://localhost:8080/graphql";
        public string rpcUrl = "http://localhost:5050";

        public string relayUrl = "/ip4/127.0.0.1/tcp/9090";
        public string relayWebrtcUrl = "/ip4/127.0.0.1/udp/9091/webrtc-direct/certhash/uEiDx-luHsovHTHPuU5qzNHCCFkYYpFPirTn2p7ZIFP0Dig";

        [Space(30)]
        [Header("Game Contracts Addresses")]
        public string worldAddress = "";

        public string blobertContractAddress = "";
        public string knockoutContractAddress = "";
        public string challengeblobertContractAddress = "";
        public string lobbyContractAddress = "";

        [Space(30)]
        [Header("Account Addresses")]
        public string masterAddress = "";
        public string masterPrivateKey = "";

        public uint limit = 1000;
    }
}
