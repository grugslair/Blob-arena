
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

    public static class BlobertActionsContract
    {

        public enum FunctionNames
        {
            Mint,

        }

        public static string EnumToString(this FunctionNames functionName)
        {
            switch (functionName)
            {

                case FunctionNames.Mint:
                    return "mint";


                default:
                    return "";
            }
        }

        public struct MintStruct
        {
            public FieldElement owner;


            public MintStruct(FieldElement owner)
            {
                this.owner = owner;

            }
        }

        public static async Task<FieldElement> MintCall(MintStruct dataStruct, EndpointDojoCallStruct endpointData)
        {
            try
            {
                var transaction = await endpointData.account.ExecuteRaw(new dojo.Call[]
                {
                new dojo.Call
                {
                    calldata = new dojo.FieldElement[]
                    {
                       dataStruct.owner.Inner,

                    },
                    selector = endpointData.functionName,
                    to = endpointData.addressOfSystem,
                }
                });

                return transaction;
            }
            catch (Exception ex)
            {
                Debug.Log("issue with Mint" + ex.Message);
                return null;
            }
        }
    }

    public static class ChallengeActionsContract
    {

        public enum FunctionNames
        {
            SendInvite,
            RescindInvite,
            RespondInvite,
            RescindResponse,
            RejectInvite,
            RejectResponse,
            AcceptResponse,
            CommitMove,
            RevealMove,

        }

        public static string EnumToString(this FunctionNames functionName)
        {
            switch (functionName)
            {

                case FunctionNames.SendInvite:
                    return "send_invite";


                case FunctionNames.RescindInvite:
                    return "rescind_invite";


                case FunctionNames.RespondInvite:
                    return "respond_invite";


                case FunctionNames.RescindResponse:
                    return "rescind_response";


                case FunctionNames.RejectInvite:
                    return "reject_invite";


                case FunctionNames.RejectResponse:
                    return "reject_response";


                case FunctionNames.AcceptResponse:
                    return "accept_response";


                case FunctionNames.CommitMove:
                    return "commit_move";


                case FunctionNames.RevealMove:
                    return "reveal_move";


                default:
                    return "";
            }
        }


        public struct SendInviteStruct
        {
            public FieldElement receiver;
            public FieldElement blobertId;


            public SendInviteStruct(FieldElement receiver, FieldElement blobertId)
            {
                this.receiver = receiver;
                this.blobertId = blobertId;

            }
        }

        public struct RescindInviteStruct
        {
            public FieldElement challengeId;


            public RescindInviteStruct(FieldElement challengeId)
            {
                this.challengeId = challengeId;

            }
        }

        public struct RespondInviteStruct
        {
            public FieldElement challengeId;
            public FieldElement blobertId;


            public RespondInviteStruct(FieldElement challengeId, FieldElement blobertId)
            {
                this.challengeId = challengeId;
                this.blobertId = blobertId;

            }
        }

        public struct RescindResponseStruct
        {
            public FieldElement challengeId;


            public RescindResponseStruct(FieldElement challengeId)
            {
                this.challengeId = challengeId;

            }
        }

        public struct RejectInviteStruct
        {
            public FieldElement challengeId;


            public RejectInviteStruct(FieldElement challengeId)
            {
                this.challengeId = challengeId;

            }
        }

        public struct RejectResponseStruct
        {
            public FieldElement challengeId;


            public RejectResponseStruct(FieldElement challengeId)
            {
                this.challengeId = challengeId;

            }
        }

        public struct AcceptResponseStruct
        {
            public FieldElement challengeId;


            public AcceptResponseStruct(FieldElement challengeId)
            {
                this.challengeId = challengeId;

            }
        }

        public struct CommitMoveStruct
        {
            public FieldElement challengeId;
            public FieldElement hash;

            public CommitMoveStruct(FieldElement challengeId, FieldElement hash)
            {
                this.challengeId = challengeId;
                this.hash = hash;
            }
        }

        public struct RevealMoveStruct
        {
            public FieldElement challengeId;
            public BlobertUtils.Move move;
            public FieldElement salt;

            public RevealMoveStruct(FieldElement challengeId, BlobertUtils.Move move, FieldElement salt)
            {
                this.challengeId = challengeId;
                this.move = move;
                this.salt = salt;

            }
        }

        public static async Task<FieldElement> SendInviteCall(SendInviteStruct dataStruct, EndpointDojoCallStruct endpointData)
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
                        dataStruct.blobertId.Inner,
                    },
                    selector = endpointData.functionName,
                    to = endpointData.addressOfSystem,
                }
                });

                return transaction;
            }
            catch (Exception ex)
            {
                Debug.Log("issue with SendInvite" + ex.Message);
                return null;
            }
        }

        public static async Task<FieldElement> RescindInviteCall(RescindInviteStruct dataStruct, EndpointDojoCallStruct endpointData)
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

                    },
                    selector = endpointData.functionName,
                    to = endpointData.addressOfSystem,
                }
                });

                return transaction;
            }
            catch (Exception ex)
            {
                Debug.Log("issue with RescindInvite" + ex.Message);
                return null;
            }
        }

        public static async Task<FieldElement> RespondInviteCall(RespondInviteStruct dataStruct, EndpointDojoCallStruct endpointData)
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
dataStruct.blobertId.Inner,

                    },
                    selector = endpointData.functionName,
                    to = endpointData.addressOfSystem,
                }
                });

                return transaction;
            }
            catch (Exception ex)
            {
                Debug.Log("issue with RespondInvite" + ex.Message);
                return null;
            }
        }

        public static async Task<FieldElement> RescindResponseCall(RescindResponseStruct dataStruct, EndpointDojoCallStruct endpointData)
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

                    },
                    selector = endpointData.functionName,
                    to = endpointData.addressOfSystem,
                }
                });

                return transaction;
            }
            catch (Exception ex)
            {
                Debug.Log("issue with RescindResponse" + ex.Message);
                return null;
            }
        }

        public static async Task<FieldElement> RejectInviteCall(RejectInviteStruct dataStruct, EndpointDojoCallStruct endpointData)
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

                    },
                    selector = endpointData.functionName,
                    to = endpointData.addressOfSystem,
                }
                });

                return transaction;
            }
            catch (Exception ex)
            {
                Debug.Log("issue with RejectInvite" + ex.Message);
                return null;
            }
        }

        public static async Task<FieldElement> RejectResponseCall(RejectResponseStruct dataStruct, EndpointDojoCallStruct endpointData)
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

                    },
                    selector = endpointData.functionName,
                    to = endpointData.addressOfSystem,
                }
                });

                return transaction;
            }
            catch (Exception ex)
            {
                Debug.Log("issue with RejectResponse" + ex.Message);
                return null;
            }
        }

        public static async Task<FieldElement> AcceptResponseCall(AcceptResponseStruct dataStruct, EndpointDojoCallStruct endpointData)
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

                    },
                    selector = endpointData.functionName,
                    to = endpointData.addressOfSystem,
                }
                });

                return transaction;
            }
            catch (Exception ex)
            {
                Debug.Log("issue with AcceptResponse" + ex.Message);
                return null;
            }
        }

        public static async Task<FieldElement> CommitMoveCall(CommitMoveStruct dataStruct, EndpointDojoCallStruct endpointData)
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
dataStruct.hash.Inner,

                    },
                    selector = endpointData.functionName,
                    to = endpointData.addressOfSystem,
                }
                });

                return transaction;
            }
            catch (Exception ex)
            {
                Debug.Log("issue with CommitMove" + ex.Message);
                return null;
            }
        }

        public static async Task<FieldElement> RevealMoveCall(RevealMoveStruct dataStruct, EndpointDojoCallStruct endpointData)
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
new FieldElement(dataStruct.move.ToString("X")).Inner,
dataStruct.salt.Inner,

                    },
                    selector = endpointData.functionName,
                    to = endpointData.addressOfSystem,
                }
                });

                return transaction;
            }
            catch (Exception ex)
            {
                Debug.Log("issue with RevealMove" + ex.Message);
                return null;
            }
        }

    }

}
