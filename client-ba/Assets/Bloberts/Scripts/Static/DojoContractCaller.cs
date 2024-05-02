using Dojo.Starknet;
using dojo_bindings;
using System;
using System.Threading.Tasks;
using UnityEngine;


namespace DojoContractCommunication
{
    public struct EndpointDojoCallStruct
    {
        public Account account;
        public string functionName;
        public string addressOfSystem;
    }

    public static class BlobertContract
    {
        public enum BlobertFunction
        {
            MintBlobert,
        }

        public static string EnumToString(this BlobertFunction knockoutFunction)
        {
            switch (knockoutFunction)
            {
                case BlobertFunction.MintBlobert:
                    return "mint";
                default:
                    return "";
            }
        }

        public struct MintBlobertStruct
        {
            public FieldElement owner;
        }

        /// <summary>
        /// Given the address this should be minting the blobert for the user
        /// </summary>
        /// <param name="dataStruct"></param>
        /// <param name="endpointData"></param>
        /// <returns></returns>
        public static async Task<FieldElement> MintBlobert(MintBlobertStruct dataStruct, EndpointDojoCallStruct endpointData)
        {
            try
            {
                var transaction = await endpointData.account.ExecuteRaw(new dojo.Call[]
                {
                new dojo.Call
                {
                    calldata = new dojo.FieldElement[]
                    {
                       dataStruct.owner.Inner
                    },
                    selector = endpointData.functionName,
                    to = endpointData.addressOfSystem,
                }
                });

                return transaction;
            }
            catch (Exception ex)
            {
                Debug.Log("issue with mint" + ex.Message);
                return null;
            }
        }
    }


    /// <summary>
    /// not working right now dont use
    /// </summary>
    public static class LobbyContract
    {
        public enum FunctionNames
        {
            CreateLobby,
            JoinLobby,
            LeaveLobby,
            CloseLobby
        }

        public static string EnumToString(this FunctionNames knockoutFunction)
        {
            switch (knockoutFunction)
            {
                case FunctionNames.CreateLobby:
                    return "create";
                case FunctionNames.JoinLobby:
                    return "join";
                case FunctionNames.LeaveLobby:
                    return "leave";
                case FunctionNames.CloseLobby:
                    return "close";
                default:
                    return "";
            }
        }

        public struct CreateLobbyStruct
        {
            public FieldElement blobertId;
        }

        public struct JoinLobbyStruct
        {
            public FieldElement lobbyId;
            public FieldElement blobertId;
        }

        public static async Task<FieldElement> CreateLobby(CreateLobbyStruct dataStruct, EndpointDojoCallStruct endpointData)
        {
            try
            {
                var transaction = await endpointData.account.ExecuteRaw(new dojo.Call[]
                {
                new dojo.Call
                {
                    calldata = new dojo.FieldElement[]
                    {
                        dataStruct.blobertId.Inner
                    },
                    selector = endpointData.functionName,
                    to = endpointData.addressOfSystem,
                }
                });

                return transaction;
            }
            catch (Exception ex)
            {
                Debug.Log("issue with creating lobby: " + ex.Message);
                return null;
            }
        }

        public static async Task<FieldElement> JoinLobby(JoinLobbyStruct dataStruct, EndpointDojoCallStruct endpointData)
        {
            try
            {
                var transaction = await endpointData.account.ExecuteRaw(new dojo.Call[]
                {
                new dojo.Call
                {
                    calldata = new dojo.FieldElement[]
                    {
                        dataStruct.lobbyId.Inner,
                        dataStruct.blobertId.Inner
                    },
                    selector = endpointData.functionName,
                    to = endpointData.addressOfSystem,
                }
                });

                return transaction;
            }
            catch (Exception ex)
            {
                Debug.Log("issue with joining lobby: " + ex.Message);
                return null;
            }
        }

        public static async Task<FieldElement> LeaveLobby(EndpointDojoCallStruct endpointData)
        {
            try
            {
                var transaction = await endpointData.account.ExecuteRaw(new dojo.Call[]
                {
                new dojo.Call
                {
                    calldata = new dojo.FieldElement[] {},
                    selector = endpointData.functionName,
                    to = endpointData.addressOfSystem,
                }
                });

                return transaction;
            }
            catch (Exception ex)
            {
                Debug.Log("issue with leaving lobby: " + ex.Message);
                return null;
            }
        }

        public static async Task<FieldElement> CloseLobby(EndpointDojoCallStruct endpointData)
        {
            try
            {
                var transaction = await endpointData.account.ExecuteRaw(new dojo.Call[]
                {
                new dojo.Call
                {
                    calldata = new dojo.FieldElement[] {},
                    selector = endpointData.functionName,
                    to = endpointData.addressOfSystem,
                }
                });

                return transaction;
            }
            catch (Exception ex)
            {
                Debug.Log("issue with closing lobby: " + ex.Message);
                return null;
            }
        }
    }


    public static class KnockoutContract
    {
        public enum FunctionNames
        {
            Commit,
            Reveal,
        }

        public static string EnumToString(this FunctionNames knockoutFunction)
        {
            switch (knockoutFunction)
            {
                case FunctionNames.Commit:
                    return "commit";
                case FunctionNames.Reveal:
                    return "reveal";
                default:
                    return "";
            }
        }

        public struct CommitMoveStruct
        {
            public FieldElement combat_id;
            public FieldElement hash;
        }

        public struct RevealMoveStruct
        {
            public FieldElement combat_id;
            public BlobertUtils.Move move;
            public FieldElement salt;
        }

        public static async Task<FieldElement> CommitMove(CommitMoveStruct dataStruct, EndpointDojoCallStruct endpointData)
        {
            try
            {
                var transaction = await endpointData.account.ExecuteRaw(new dojo.Call[]
                {
                new dojo.Call
                {
                    calldata = new dojo.FieldElement[]
                    {
                        dataStruct.combat_id.Inner,
                        dataStruct.hash.Inner
                    },
                    selector = endpointData.functionName,
                    to = endpointData.addressOfSystem,
                }
                });

                return transaction;
            }
            catch (Exception ex)
            {
                Debug.Log("issue with committing move: " + ex.Message);
                return null;
            }
        }

        public static async Task<FieldElement> RevealMove(RevealMoveStruct dataStruct, EndpointDojoCallStruct endpointData)
        {
            try
            {
                var transaction = await endpointData.account.ExecuteRaw(new dojo.Call[]
                {
                new dojo.Call
                {
                    calldata = new dojo.FieldElement[]
                    {
                        dataStruct.combat_id.Inner,
                        new FieldElement(dataStruct.move).Inner,
                        dataStruct.salt.Inner
                    },
                    selector = endpointData.functionName,
                    to = endpointData.addressOfSystem,
                }
                });

                return transaction;
            }
            catch (Exception ex)
            {
                Debug.Log("issue with revealing move: " + ex.Message);
                return null;
            }
        }
    }

    public static class ChallengeContract
    {
        public enum FunctionNames
        {
            SendInvite,
            CloseInvite,
            RespondInvite,
            CloseResponse,
            RejectInvite,
            RejectResponse,
            AcceptResponse
        }

        public static string EnumToString(this FunctionNames challengeFunction)
        {
            switch (challengeFunction)
            {
                case FunctionNames.SendInvite:
                    return "send_invite";
                case FunctionNames.CloseInvite:
                    return "close_invite";
                case FunctionNames.RespondInvite:
                    return "respond_invite";
                case FunctionNames.CloseResponse:
                    return "close_response";
                case FunctionNames.RejectInvite:
                    return "reject_invite";
                case FunctionNames.RejectResponse:
                    return "reject_response";
                case FunctionNames.AcceptResponse:
                    return "accept_response";
                default:
                    return "";
            }
        }

        public struct SendInviteStruct
        {
            /// <summary>
            /// Address of the other player being challenged
            /// </summary>
            public FieldElement receiver;
            /// <summary>
            /// The blobert id of the player sending the invite
            /// </summary>
            public FieldElement blobertId;
        }

        public struct CloseInviteStruct
        {
            public FieldElement challengeId;
        }

        public struct RespondInviteStruct
        {
            public FieldElement challengeId;
            public FieldElement blobertId;
        }

        public struct CloseResponseStruct
        {
            public FieldElement challengeId;
        }

        public struct RejectInviteStruct
        {
            public FieldElement challengeId;
        }

        public struct RejectResponseStruct
        {
            public FieldElement challengeId;
        }

        public struct AcceptResponseStruct
        {
            public FieldElement challengeId;
        }

        /// <summary>
        /// Send An invite to another player
        /// </summary>
        /// <param name="dataStruct"></param>
        /// <param name="endpointData"></param>
        /// <returns>ChallengeInvite id entity is created</returns>
        public static async Task<FieldElement> SendInvite(SendInviteStruct dataStruct, EndpointDojoCallStruct endpointData)
        {
            try
            {
                var transaction = await endpointData.account.ExecuteRaw(new dojo.Call[]
                {
                    new dojo.Call
                    {
                        calldata = new dojo.FieldElement[]
                        {
                            dataStruct.receiver.Inner,
                            dataStruct.blobertId.Inner
                        },
                        selector = endpointData.functionName,
                        to = endpointData.addressOfSystem,
                    }
                });

                return transaction;
            }
            catch (Exception ex)
            {
                Debug.Log("issue with sending invite: " + ex.Message);
                return null;
            }
        }

        /// <summary>
        /// This can only be called from the admin it self to close the whole thing
        /// </summary>
        /// <param name="dataStruct"></param>
        /// <param name="endpointData"></param>
        /// <returns>ChallengeInvite changed opened var to false</returns>
        public static async Task<FieldElement> CloseInvite(CloseInviteStruct dataStruct, EndpointDojoCallStruct endpointData)
        {
            try
            {
                var transaction = await endpointData.account.ExecuteRaw(new dojo.Call[]
                {
                    new dojo.Call
                    {
                        calldata = new dojo.FieldElement[]
                        {
                            dataStruct.challengeId.Inner
                        },
                        selector = endpointData.functionName,
                        to = endpointData.addressOfSystem,
                    }
                });

                return transaction;
            }
            catch (Exception ex)
            {
                Debug.Log("issue with closing invite: " + ex.Message);
                return null;
            }
        }

        /// <summary>
        /// This should confirm the invite
        /// </summary>
        /// <param name="dataStruct"></param>
        /// <param name="endpointData"></param>
        /// <returns></returns>
        public static async Task<FieldElement> RespondInvite(RespondInviteStruct dataStruct, EndpointDojoCallStruct endpointData)
        {
            try
            {
                var transaction = await endpointData.account.ExecuteRaw(new dojo.Call[]
                {
                    new dojo.Call
                    {
                        calldata = new dojo.FieldElement[]
                        {
                            dataStruct.challengeId.Inner,
                            dataStruct.blobertId.Inner
                        },
                        selector = endpointData.functionName,
                        to = endpointData.addressOfSystem,
                    }
                });

                return transaction;
            }
            catch (Exception ex)
            {
                Debug.Log("issue with responding invite: " + ex.Message);
                return null;
            }
        }

        /// <summary>
        /// i think this is for the when the lobby is made and the user wants to go back
        /// </summary>
        /// <param name="dataStruct"></param>
        /// <param name="endpointData"></param>
        /// <returns></returns>
        public static async Task<FieldElement> CloseResponse(CloseResponseStruct dataStruct, EndpointDojoCallStruct endpointData)
        {
            try
            {
                var transaction = await endpointData.account.ExecuteRaw(new dojo.Call[]
                {
                    new dojo.Call
                    {
                        calldata = new dojo.FieldElement[]
                        {
                            dataStruct.challengeId.Inner
                        },
                        selector = endpointData.functionName,
                        to = endpointData.addressOfSystem,
                    }
                });

                return transaction;
            }
            catch (Exception ex)
            {
                Debug.Log("issue with closing response: " + ex.Message);
                return null;
            }
        }

        /// <summary>
        /// this si the correct one to call to end the invite
        /// </summary>
        /// <param name="dataStruct"></param>
        /// <param name="endpointData"></param>
        /// <returns></returns>
        public static async Task<FieldElement> RejectInvite(RejectInviteStruct dataStruct, EndpointDojoCallStruct endpointData)
        {
            try
            {
                var transaction = await endpointData.account.ExecuteRaw(new dojo.Call[]
                {
                    new dojo.Call
                    {
                        calldata = new dojo.FieldElement[]
                        {
                            dataStruct.challengeId.Inner
                        },
                        selector = endpointData.functionName,
                        to = endpointData.addressOfSystem,
                    }
                });

                return transaction;
            }
            catch (Exception ex)
            {
                Debug.Log("issue with rejecting invite: " + ex.Message);
                return null;
            }
        }

        /// <summary>
        /// When the lobby is made the admin can reject the response and go back
        /// </summary>
        /// <param name="dataStruct"></param>
        /// <param name="endpointData"></param>
        /// <returns></returns>
        public static async Task<FieldElement> RejectResponse(RejectResponseStruct dataStruct, EndpointDojoCallStruct endpointData)
        {
            try
            {
                var transaction = await endpointData.account.ExecuteRaw(new dojo.Call[]
                {
                    new dojo.Call
                    {
                        calldata = new dojo.FieldElement[]
                        {
                            dataStruct.challengeId.Inner
                        },
                        selector = endpointData.functionName,
                        to = endpointData.addressOfSystem,
                    }
                });

                return transaction;
            }
            catch (Exception ex)
            {
                Debug.Log("issue with rejecting response: " + ex.Message);
                return null;
            }
        }

        /// <summary>
        /// The admin Confirms the game and it starts
        /// </summary>
        /// <param name="dataStruct"></param>
        /// <param name="endpointData"></param>
        /// <returns></returns>
        public static async Task<FieldElement> AcceptResponse(AcceptResponseStruct dataStruct, EndpointDojoCallStruct endpointData)
        {
            try
            {
                var transaction = await endpointData.account.ExecuteRaw(new dojo.Call[]
                {
                    new dojo.Call
                    {
                        calldata = new dojo.FieldElement[]
                        {
                            dataStruct.challengeId.Inner
                        },
                        selector = endpointData.functionName,
                        to = endpointData.addressOfSystem,
                    }
                });

                return transaction;
            }
            catch (Exception ex)
            {
                Debug.Log("issue with accepting response: " + ex.Message);
                return null;
            }
        }
    }
}







//Local
//public static readonly string knockoutAddress = "0x66821c7071e66a727918207afb0255e5dac1677b1732a95104c7672fc98d51e";
//public static readonly string blobertActionsAddress = "0x3e2408ea9affd43d731fcb31e67f7c2c6899cef4c1279dc597dc5d14b240d12";

//public static readonly string worldAddress = "0x3a0394af68d1727a0019949a94fa584e8bc132903d49bb545888eb1bd427cf4";

//public static readonly string masterAddress = "0xb3ff441a68610b30fd5e2abbf3a1548eb6ba6f3559f2862bf2dc757e5828ca";
//public static readonly string masterPrivateKey = "0x2bbf4f9fd0bbb2e60b0316c1fe0b76cf7a4d0198bd493ced9b8df2a3a24d68a";

//slot
//public static readonly string knockoutAddress = "0x5ca704bee322163577a552e6debdbe6c7b20e209cbeae8e5fbada33ea6510ee";
//    public static readonly string blobertActionsAddress = "0x212384234554c179f0875ffc07db99a4952532f61c76cb43d6ea14d0491b610";

//    public static readonly string worldAddress = "0x786c41c25759a24772df96df1272cded0b118b64df75c77fa9d5aa669c25b66";

//    public static readonly string masterAddress = "0x472c5f0ee5e5224a198e4cd4e26fd7cef51acd64778e0a2fca5af1697d5e5e";
//    public static readonly string masterPrivateKey = "0xb320c4fe6c2a03aa2b915f9b3e92654c257dec19c1bf77fefa004690bd65eb";

