
using Dojo.Starknet;
using dojo_bindings;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Threading.Tasks;
using UnityEngine;
using static DojoContractCommunication;
using static JSInteropManager;

public static class DojoContractCommunication
{
    // what could be interesting is maybe send the function not the name but mayeb get the name as they both takje in the string

    public enum WalletType
    {
        BURNER,
        ARGENT_X,
        BRAAVOS
    }

    public static WalletType selectedWalletType { get; set; }

    public struct EndpointDojoCallStruct
    {
        public string functionName;
        public string addressOfSystem;

        public EndpointDojoCallStruct(string functionName, string addressOfSystem)
        {
            this.functionName = functionName;
            this.addressOfSystem = addressOfSystem;
        }
    }

    [Serializable]
    public class ContractCall
    {
        public string contractAddress;
        public string entrypoint;
        public string[] calldata;

        //make a constructor
        public ContractCall(string contractAddress, string entrypoint, string[] calldata)
        {
            this.contractAddress = contractAddress;
            this.entrypoint = entrypoint;
            this.calldata = calldata;
        }
    }

    public async static Task<FieldElement> InvokeContract(List<object> structInstances, string objectName = "", string functionName = "", Account account = null)
    {
        if (selectedWalletType == WalletType.BURNER)
        {
            if (account == null)
            {
                Debug.LogError("Account is null, cannot execute contract calls.");
                return null;
            }

            var calls = new List<dojo.Call>();

            foreach (var structInstance in structInstances)
            {
                if (structInstance == null)
                {
                    Debug.LogWarning("Encountered a null instance in the list, skipping.");
                    continue;
                }

                Type structType = structInstance.GetType();

                var endpointData = (EndpointDojoCallStruct)structType
                    .GetField("endpointData")
                    ?.GetValue(structInstance);

                var fields = structType.GetFields().Where(f => f.Name != "endpointData").ToArray();

                var calldata = new List<dojo.FieldElement>();

                foreach (var field in fields)
                {
                    var fieldValue = field.GetValue(structInstance);
                    switch (fieldValue)
                    {
                        case FieldElement fe:
                            calldata.Add(fe.Inner);
                            break;
                        case byte by:
                            calldata.Add(new FieldElement(by.ToString("X")).Inner);
                            break;
                        case UInt16 u16:
                            calldata.Add(new FieldElement(u16.ToString("X")).Inner);
                            break;
                        case UInt32 u32:
                            calldata.Add(new FieldElement(u32.ToString("X")).Inner);
                            break;
                        case UInt64 u64:
                            calldata.Add(new FieldElement(u64.ToString("X")).Inner);
                            break;
                        case BigInteger bi:
                            calldata.Add(new FieldElement(bi.ToString("X")).Inner);
                            break;
                        case bool bo:
                            //calldata.Add(new FieldElement(bo.ToString("X")).Inner);
                            break;
                        default:
                            Debug.LogError($"Unsupported field type: {fieldValue.GetType().Name}");
                            break;
                    }
                }

                // Add the call to the list
                calls.Add(new dojo.Call
                {
                    calldata = calldata.ToArray(),
                    selector = endpointData.functionName,
                    to = endpointData.addressOfSystem
                });
            }

            return await InvokeViaBurner(calls, account);
        }
        else
        {
            if (string.IsNullOrEmpty(objectName) || string.IsNullOrEmpty(functionName))
            {
                Debug.LogError("Object name or function name is empty, cannot execute contract calls.");
                return null;
            }

            var calls = new List<ContractCall>();

            foreach (var structInstance in structInstances)
            {
                if (structInstance == null)
                {
                    Debug.LogWarning("Encountered a null instance in the list, skipping.");
                    continue;
                }

                Type structType = structInstance.GetType();

                var endpointData = (EndpointDojoCallStruct)structType
                    .GetField("endpointData")
                    ?.GetValue(structInstance);

                var fields = structType.GetFields().Where(f => f.Name != "endpointData").ToArray();

                var calldata = new List<string>();

                foreach (var field in fields)
                {
                    var fieldValue = field.GetValue(structInstance);
                    switch (fieldValue)
                    {
                        case FieldElement fe:
                            calldata.Add(fe.Hex());
                            break;
                        case byte by:
                            calldata.Add(by.ToString());
                            break;
                        case UInt16 u16:
                            calldata.Add(u16.ToString());
                            break;
                        case UInt32 u32:
                            calldata.Add(u32.ToString());
                            break;
                        case UInt64 u64:
                            calldata.Add(u64.ToString());
                            break;
                        case BigInteger bi:
                            calldata.Add(bi.ToString());
                            calldata.Add("0");
                            break;
                        case bool bo:
                            //calldata.Add(new FieldElement(bo.ToString("X")).Inner);
                            Debug.LogError("bool has yet to be implemented, message alex");
                            break;
                        default:
                            Debug.LogError($"Unsupported field type: {fieldValue.GetType().Name}");
                            break;
                    }
                }

                calls.Add(new ContractCall(calldata: calldata.ToArray(), contractAddress: endpointData.addressOfSystem, entrypoint: endpointData.functionName));
            }

            return await InvokeViaWallet(calls, objectName, functionName);
        }
    }

    public async static Task<FieldElement> InvokeViaBurner(List<dojo.Call> callsData, Account account)
    {
        Debug.Log("InvokeViaBurner");
        return await account.ExecuteRaw(callsData.ToArray());
    }

    public async static Task<FieldElement> InvokeViaWallet(List<ContractCall> callsData, string objectName, string callBackFunc)
    {
        foreach (var call in callsData)
        {
            Debug.Log($"Contract address: {call.contractAddress}, entrypoint: {call.entrypoint}, calldata: {string.Join(", ", call.calldata)}");
        }

        SendMultiCallTransaction(BuildCallsJsString(callsData.ToArray()), objectName, callBackFunc);

        return new FieldElement("0");
    }

    public static string BuildCallsJsString(ContractCall[] calls)
    {
        var sb = new StringBuilder();
        sb.Append("[");

        for (int i = 0; i < calls.Length; i++)
        {
            var call = calls[i];
            sb.Append("{");
            sb.AppendFormat("contractAddress: \"{0}\", ", call.contractAddress);
            sb.AppendFormat("entrypoint: \"{0}\", ", call.entrypoint);
            sb.Append("calldata: [");
            sb.Append(string.Join(", ", call.calldata.Select(d => $"\"{d}\"")));
            sb.Append("]");
            sb.Append("}");

            if (i < calls.Length - 1)
            {
                sb.Append(", ");
            }
        }

        sb.Append("]");

        return sb.ToString();
    }
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
        public EndpointDojoCallStruct endpointData;

        public MintStruct(FieldElement owner, EndpointDojoCallStruct endpointData)
        {
            this.owner = owner;
            this.endpointData = endpointData;
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
        public EndpointDojoCallStruct endpointData;

        public SendInviteStruct(FieldElement receiver, FieldElement blobertId, EndpointDojoCallStruct endpointData)
        {
            this.receiver = receiver;
            this.blobertId = blobertId;
            this.endpointData = endpointData;
        }
    }

    public struct RescindInviteStruct
    {
        public FieldElement challengeId;
        public EndpointDojoCallStruct endpointData;

        public RescindInviteStruct(FieldElement challengeId, EndpointDojoCallStruct endpointData)
        {
            this.challengeId = challengeId;
            this.endpointData = endpointData;
        }
    }

    public struct RespondInviteStruct
    {
        public FieldElement challengeId;
        public FieldElement blobertId;
        public EndpointDojoCallStruct endpointData;

        public RespondInviteStruct(FieldElement challengeId, FieldElement blobertId, EndpointDojoCallStruct endpointData)
        {
            this.challengeId = challengeId;
            this.blobertId = blobertId;
            this.endpointData = endpointData;
        }
    }

    public struct RescindResponseStruct
    {
        public FieldElement challengeId;
        public EndpointDojoCallStruct endpointData;

        public RescindResponseStruct(FieldElement challengeId, EndpointDojoCallStruct endpointData)
        {
            this.challengeId = challengeId;
            this.endpointData = endpointData;
        }
    }

    public struct RejectInviteStruct
    {
        public FieldElement challengeId;
        public EndpointDojoCallStruct endpointData;

        public RejectInviteStruct(FieldElement challengeId, EndpointDojoCallStruct endpointData)
        {
            this.challengeId = challengeId;
            this.endpointData = endpointData;
        }
    }

    public struct RejectResponseStruct
    {
        public FieldElement challengeId;
        public EndpointDojoCallStruct endpointData;

        public RejectResponseStruct(FieldElement challengeId, EndpointDojoCallStruct endpointData)
        {
            this.challengeId = challengeId;
            this.endpointData = endpointData;
        }
    }

    public struct AcceptResponseStruct
    {
        public FieldElement challengeId;
        public EndpointDojoCallStruct endpointData;

        public AcceptResponseStruct(FieldElement challengeId, EndpointDojoCallStruct endpointData)
        {
            this.challengeId = challengeId;
            this.endpointData = endpointData;
        }
    }

    public struct CommitMoveStruct
    {
        public FieldElement challengeId;
        public FieldElement hash;
        public EndpointDojoCallStruct endpointData;

        public CommitMoveStruct(FieldElement challengeId, FieldElement hash, EndpointDojoCallStruct endpointData)
        {
            this.challengeId = challengeId;
            this.hash = hash;
            this.endpointData = endpointData;
        }
    }

    public struct RevealMoveStruct
    {
        public FieldElement challengeId;
        public BlobertUtils.Move move;
        public FieldElement salt;
        public EndpointDojoCallStruct endpointData;

        public RevealMoveStruct(FieldElement challengeId, BlobertUtils.Move move, FieldElement salt, EndpointDojoCallStruct endpointData)
        {
            this.challengeId = challengeId;
            this.move = move;
            this.salt = salt;
            this.endpointData = endpointData;
        }
    }

}
